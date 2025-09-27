# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cloudwatch import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AlarmContributor:
    boto3_raw_data: "type_defs.AlarmContributorTypeDef" = dataclasses.field()

    ContributorId = field("ContributorId")
    ContributorAttributes = field("ContributorAttributes")
    StateReason = field("StateReason")
    StateTransitionedTimestamp = field("StateTransitionedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlarmContributorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlarmContributorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlarmHistoryItem:
    boto3_raw_data: "type_defs.AlarmHistoryItemTypeDef" = dataclasses.field()

    AlarmName = field("AlarmName")
    AlarmContributorId = field("AlarmContributorId")
    AlarmType = field("AlarmType")
    Timestamp = field("Timestamp")
    HistoryItemType = field("HistoryItemType")
    HistorySummary = field("HistorySummary")
    HistoryData = field("HistoryData")
    AlarmContributorAttributes = field("AlarmContributorAttributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlarmHistoryItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlarmHistoryItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RangeOutput:
    boto3_raw_data: "type_defs.RangeOutputTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RangeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RangeOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Dimension:
    boto3_raw_data: "type_defs.DimensionTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DimensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DimensionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricCharacteristics:
    boto3_raw_data: "type_defs.MetricCharacteristicsTypeDef" = dataclasses.field()

    PeriodicSpikes = field("PeriodicSpikes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricCharacteristicsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricCharacteristicsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudwatchEventState:
    boto3_raw_data: "type_defs.CloudwatchEventStateTypeDef" = dataclasses.field()

    timestamp = field("timestamp")
    value = field("value")
    reason = field("reason")
    reasonData = field("reasonData")
    actionsSuppressedBy = field("actionsSuppressedBy")
    actionsSuppressedReason = field("actionsSuppressedReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudwatchEventStateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudwatchEventStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudwatchEventMetricStatsMetric:
    boto3_raw_data: "type_defs.CloudwatchEventMetricStatsMetricTypeDef" = (
        dataclasses.field()
    )

    metricName = field("metricName")
    namespace = field("namespace")
    dimensions = field("dimensions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CloudwatchEventMetricStatsMetricTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudwatchEventMetricStatsMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompositeAlarm:
    boto3_raw_data: "type_defs.CompositeAlarmTypeDef" = dataclasses.field()

    ActionsEnabled = field("ActionsEnabled")
    AlarmActions = field("AlarmActions")
    AlarmArn = field("AlarmArn")
    AlarmConfigurationUpdatedTimestamp = field("AlarmConfigurationUpdatedTimestamp")
    AlarmDescription = field("AlarmDescription")
    AlarmName = field("AlarmName")
    AlarmRule = field("AlarmRule")
    InsufficientDataActions = field("InsufficientDataActions")
    OKActions = field("OKActions")
    StateReason = field("StateReason")
    StateReasonData = field("StateReasonData")
    StateUpdatedTimestamp = field("StateUpdatedTimestamp")
    StateValue = field("StateValue")
    StateTransitionedTimestamp = field("StateTransitionedTimestamp")
    ActionsSuppressedBy = field("ActionsSuppressedBy")
    ActionsSuppressedReason = field("ActionsSuppressedReason")
    ActionsSuppressor = field("ActionsSuppressor")
    ActionsSuppressorWaitPeriod = field("ActionsSuppressorWaitPeriod")
    ActionsSuppressorExtensionPeriod = field("ActionsSuppressorExtensionPeriod")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CompositeAlarmTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CompositeAlarmTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashboardEntry:
    boto3_raw_data: "type_defs.DashboardEntryTypeDef" = dataclasses.field()

    DashboardName = field("DashboardName")
    DashboardArn = field("DashboardArn")
    LastModified = field("LastModified")
    Size = field("Size")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DashboardEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DashboardEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashboardValidationMessage:
    boto3_raw_data: "type_defs.DashboardValidationMessageTypeDef" = dataclasses.field()

    DataPath = field("DataPath")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DashboardValidationMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DashboardValidationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Datapoint:
    boto3_raw_data: "type_defs.DatapointTypeDef" = dataclasses.field()

    Timestamp = field("Timestamp")
    SampleCount = field("SampleCount")
    Average = field("Average")
    Sum = field("Sum")
    Minimum = field("Minimum")
    Maximum = field("Maximum")
    Unit = field("Unit")
    ExtendedStatistics = field("ExtendedStatistics")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatapointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatapointTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAlarmsInput:
    boto3_raw_data: "type_defs.DeleteAlarmsInputTypeDef" = dataclasses.field()

    AlarmNames = field("AlarmNames")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteAlarmsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAlarmsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDashboardsInput:
    boto3_raw_data: "type_defs.DeleteDashboardsInputTypeDef" = dataclasses.field()

    DashboardNames = field("DashboardNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDashboardsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDashboardsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInsightRulesInput:
    boto3_raw_data: "type_defs.DeleteInsightRulesInputTypeDef" = dataclasses.field()

    RuleNames = field("RuleNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInsightRulesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInsightRulesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PartialFailure:
    boto3_raw_data: "type_defs.PartialFailureTypeDef" = dataclasses.field()

    FailureResource = field("FailureResource")
    ExceptionType = field("ExceptionType")
    FailureCode = field("FailureCode")
    FailureDescription = field("FailureDescription")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PartialFailureTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PartialFailureTypeDef"]],
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
class DeleteMetricStreamInput:
    boto3_raw_data: "type_defs.DeleteMetricStreamInputTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMetricStreamInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMetricStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAlarmContributorsInput:
    boto3_raw_data: "type_defs.DescribeAlarmContributorsInputTypeDef" = (
        dataclasses.field()
    )

    AlarmName = field("AlarmName")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAlarmContributorsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAlarmContributorsInputTypeDef"]
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
class DescribeAlarmsInput:
    boto3_raw_data: "type_defs.DescribeAlarmsInputTypeDef" = dataclasses.field()

    AlarmNames = field("AlarmNames")
    AlarmNamePrefix = field("AlarmNamePrefix")
    AlarmTypes = field("AlarmTypes")
    ChildrenOfAlarmName = field("ChildrenOfAlarmName")
    ParentsOfAlarmName = field("ParentsOfAlarmName")
    StateValue = field("StateValue")
    ActionPrefix = field("ActionPrefix")
    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAlarmsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAlarmsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaiterConfig:
    boto3_raw_data: "type_defs.WaiterConfigTypeDef" = dataclasses.field()

    Delay = field("Delay")
    MaxAttempts = field("MaxAttempts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaiterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaiterConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInsightRulesInput:
    boto3_raw_data: "type_defs.DescribeInsightRulesInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInsightRulesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInsightRulesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InsightRule:
    boto3_raw_data: "type_defs.InsightRuleTypeDef" = dataclasses.field()

    Name = field("Name")
    State = field("State")
    Schema = field("Schema")
    Definition = field("Definition")
    ManagedRule = field("ManagedRule")
    ApplyOnTransformedLogs = field("ApplyOnTransformedLogs")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InsightRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InsightRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DimensionFilter:
    boto3_raw_data: "type_defs.DimensionFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DimensionFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DimensionFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableAlarmActionsInput:
    boto3_raw_data: "type_defs.DisableAlarmActionsInputTypeDef" = dataclasses.field()

    AlarmNames = field("AlarmNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableAlarmActionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableAlarmActionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableInsightRulesInput:
    boto3_raw_data: "type_defs.DisableInsightRulesInputTypeDef" = dataclasses.field()

    RuleNames = field("RuleNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableInsightRulesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableInsightRulesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableAlarmActionsInput:
    boto3_raw_data: "type_defs.EnableAlarmActionsInputTypeDef" = dataclasses.field()

    AlarmNames = field("AlarmNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableAlarmActionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableAlarmActionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableInsightRulesInput:
    boto3_raw_data: "type_defs.EnableInsightRulesInputTypeDef" = dataclasses.field()

    RuleNames = field("RuleNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableInsightRulesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableInsightRulesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Entity:
    boto3_raw_data: "type_defs.EntityTypeDef" = dataclasses.field()

    KeyAttributes = field("KeyAttributes")
    Attributes = field("Attributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDashboardInput:
    boto3_raw_data: "type_defs.GetDashboardInputTypeDef" = dataclasses.field()

    DashboardName = field("DashboardName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDashboardInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDashboardInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InsightRuleMetricDatapoint:
    boto3_raw_data: "type_defs.InsightRuleMetricDatapointTypeDef" = dataclasses.field()

    Timestamp = field("Timestamp")
    UniqueContributors = field("UniqueContributors")
    MaxContributorValue = field("MaxContributorValue")
    SampleCount = field("SampleCount")
    Average = field("Average")
    Sum = field("Sum")
    Minimum = field("Minimum")
    Maximum = field("Maximum")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InsightRuleMetricDatapointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InsightRuleMetricDatapointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LabelOptions:
    boto3_raw_data: "type_defs.LabelOptionsTypeDef" = dataclasses.field()

    Timezone = field("Timezone")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LabelOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LabelOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageData:
    boto3_raw_data: "type_defs.MessageDataTypeDef" = dataclasses.field()

    Code = field("Code")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetricStreamInput:
    boto3_raw_data: "type_defs.GetMetricStreamInputTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMetricStreamInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetricStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricStreamFilterOutput:
    boto3_raw_data: "type_defs.MetricStreamFilterOutputTypeDef" = dataclasses.field()

    Namespace = field("Namespace")
    MetricNames = field("MetricNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricStreamFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricStreamFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetricWidgetImageInput:
    boto3_raw_data: "type_defs.GetMetricWidgetImageInputTypeDef" = dataclasses.field()

    MetricWidget = field("MetricWidget")
    OutputFormat = field("OutputFormat")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMetricWidgetImageInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetricWidgetImageInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InsightRuleContributorDatapoint:
    boto3_raw_data: "type_defs.InsightRuleContributorDatapointTypeDef" = (
        dataclasses.field()
    )

    Timestamp = field("Timestamp")
    ApproximateValue = field("ApproximateValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InsightRuleContributorDatapointTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InsightRuleContributorDatapointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDashboardsInput:
    boto3_raw_data: "type_defs.ListDashboardsInputTypeDef" = dataclasses.field()

    DashboardNamePrefix = field("DashboardNamePrefix")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDashboardsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDashboardsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedInsightRulesInput:
    boto3_raw_data: "type_defs.ListManagedInsightRulesInputTypeDef" = (
        dataclasses.field()
    )

    ResourceARN = field("ResourceARN")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListManagedInsightRulesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedInsightRulesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetricStreamsInput:
    boto3_raw_data: "type_defs.ListMetricStreamsInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMetricStreamsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetricStreamsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricStreamEntry:
    boto3_raw_data: "type_defs.MetricStreamEntryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationDate = field("CreationDate")
    LastUpdateDate = field("LastUpdateDate")
    Name = field("Name")
    FirehoseArn = field("FirehoseArn")
    State = field("State")
    OutputFormat = field("OutputFormat")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricStreamEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricStreamEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInput:
    boto3_raw_data: "type_defs.ListTagsForResourceInputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceInputTypeDef"]
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
class ManagedRuleState:
    boto3_raw_data: "type_defs.ManagedRuleStateTypeDef" = dataclasses.field()

    RuleName = field("RuleName")
    State = field("State")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ManagedRuleStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedRuleStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatisticSet:
    boto3_raw_data: "type_defs.StatisticSetTypeDef" = dataclasses.field()

    SampleCount = field("SampleCount")
    Sum = field("Sum")
    Minimum = field("Minimum")
    Maximum = field("Maximum")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatisticSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatisticSetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricStreamFilter:
    boto3_raw_data: "type_defs.MetricStreamFilterTypeDef" = dataclasses.field()

    Namespace = field("Namespace")
    MetricNames = field("MetricNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricStreamFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricStreamFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricStreamStatisticsMetric:
    boto3_raw_data: "type_defs.MetricStreamStatisticsMetricTypeDef" = (
        dataclasses.field()
    )

    Namespace = field("Namespace")
    MetricName = field("MetricName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricStreamStatisticsMetricTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricStreamStatisticsMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDashboardInput:
    boto3_raw_data: "type_defs.PutDashboardInputTypeDef" = dataclasses.field()

    DashboardName = field("DashboardName")
    DashboardBody = field("DashboardBody")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutDashboardInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDashboardInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetAlarmStateInputAlarmSetState:
    boto3_raw_data: "type_defs.SetAlarmStateInputAlarmSetStateTypeDef" = (
        dataclasses.field()
    )

    StateValue = field("StateValue")
    StateReason = field("StateReason")
    StateReasonData = field("StateReasonData")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SetAlarmStateInputAlarmSetStateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetAlarmStateInputAlarmSetStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetAlarmStateInput:
    boto3_raw_data: "type_defs.SetAlarmStateInputTypeDef" = dataclasses.field()

    AlarmName = field("AlarmName")
    StateValue = field("StateValue")
    StateReason = field("StateReason")
    StateReasonData = field("StateReasonData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetAlarmStateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetAlarmStateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMetricStreamsInput:
    boto3_raw_data: "type_defs.StartMetricStreamsInputTypeDef" = dataclasses.field()

    Names = field("Names")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMetricStreamsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMetricStreamsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopMetricStreamsInput:
    boto3_raw_data: "type_defs.StopMetricStreamsInputTypeDef" = dataclasses.field()

    Names = field("Names")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopMetricStreamsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopMetricStreamsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceInput:
    boto3_raw_data: "type_defs.UntagResourceInputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyDetectorConfigurationOutput:
    boto3_raw_data: "type_defs.AnomalyDetectorConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ExcludedTimeRanges(self):  # pragma: no cover
        return RangeOutput.make_many(self.boto3_raw_data["ExcludedTimeRanges"])

    MetricTimezone = field("MetricTimezone")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AnomalyDetectorConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalyDetectorConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAlarmsForMetricInput:
    boto3_raw_data: "type_defs.DescribeAlarmsForMetricInputTypeDef" = (
        dataclasses.field()
    )

    MetricName = field("MetricName")
    Namespace = field("Namespace")
    Statistic = field("Statistic")
    ExtendedStatistic = field("ExtendedStatistic")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    Period = field("Period")
    Unit = field("Unit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAlarmsForMetricInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAlarmsForMetricInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAnomalyDetectorsInput:
    boto3_raw_data: "type_defs.DescribeAnomalyDetectorsInputTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    Namespace = field("Namespace")
    MetricName = field("MetricName")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    AnomalyDetectorTypes = field("AnomalyDetectorTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAnomalyDetectorsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAnomalyDetectorsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricOutput:
    boto3_raw_data: "type_defs.MetricOutputTypeDef" = dataclasses.field()

    Namespace = field("Namespace")
    MetricName = field("MetricName")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Metric:
    boto3_raw_data: "type_defs.MetricTypeDef" = dataclasses.field()

    Namespace = field("Namespace")
    MetricName = field("MetricName")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

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
class SingleMetricAnomalyDetectorOutput:
    boto3_raw_data: "type_defs.SingleMetricAnomalyDetectorOutputTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    Namespace = field("Namespace")
    MetricName = field("MetricName")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    Stat = field("Stat")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SingleMetricAnomalyDetectorOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SingleMetricAnomalyDetectorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SingleMetricAnomalyDetector:
    boto3_raw_data: "type_defs.SingleMetricAnomalyDetectorTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Namespace = field("Namespace")
    MetricName = field("MetricName")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    Stat = field("Stat")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SingleMetricAnomalyDetectorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SingleMetricAnomalyDetectorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudwatchEventMetricStats:
    boto3_raw_data: "type_defs.CloudwatchEventMetricStatsTypeDef" = dataclasses.field()

    period = field("period")
    stat = field("stat")

    @cached_property
    def metric(self):  # pragma: no cover
        return CloudwatchEventMetricStatsMetric.make_one(self.boto3_raw_data["metric"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudwatchEventMetricStatsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudwatchEventMetricStatsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInsightRulesOutput:
    boto3_raw_data: "type_defs.DeleteInsightRulesOutputTypeDef" = dataclasses.field()

    @cached_property
    def Failures(self):  # pragma: no cover
        return PartialFailure.make_many(self.boto3_raw_data["Failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInsightRulesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInsightRulesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAlarmContributorsOutput:
    boto3_raw_data: "type_defs.DescribeAlarmContributorsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AlarmContributors(self):  # pragma: no cover
        return AlarmContributor.make_many(self.boto3_raw_data["AlarmContributors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAlarmContributorsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAlarmContributorsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAlarmHistoryOutput:
    boto3_raw_data: "type_defs.DescribeAlarmHistoryOutputTypeDef" = dataclasses.field()

    @cached_property
    def AlarmHistoryItems(self):  # pragma: no cover
        return AlarmHistoryItem.make_many(self.boto3_raw_data["AlarmHistoryItems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAlarmHistoryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAlarmHistoryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableInsightRulesOutput:
    boto3_raw_data: "type_defs.DisableInsightRulesOutputTypeDef" = dataclasses.field()

    @cached_property
    def Failures(self):  # pragma: no cover
        return PartialFailure.make_many(self.boto3_raw_data["Failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableInsightRulesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableInsightRulesOutputTypeDef"]
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
class EnableInsightRulesOutput:
    boto3_raw_data: "type_defs.EnableInsightRulesOutputTypeDef" = dataclasses.field()

    @cached_property
    def Failures(self):  # pragma: no cover
        return PartialFailure.make_many(self.boto3_raw_data["Failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableInsightRulesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableInsightRulesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDashboardOutput:
    boto3_raw_data: "type_defs.GetDashboardOutputTypeDef" = dataclasses.field()

    DashboardArn = field("DashboardArn")
    DashboardBody = field("DashboardBody")
    DashboardName = field("DashboardName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDashboardOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDashboardOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetricStatisticsOutput:
    boto3_raw_data: "type_defs.GetMetricStatisticsOutputTypeDef" = dataclasses.field()

    Label = field("Label")

    @cached_property
    def Datapoints(self):  # pragma: no cover
        return Datapoint.make_many(self.boto3_raw_data["Datapoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMetricStatisticsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetricStatisticsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetricWidgetImageOutput:
    boto3_raw_data: "type_defs.GetMetricWidgetImageOutputTypeDef" = dataclasses.field()

    MetricWidgetImage = field("MetricWidgetImage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMetricWidgetImageOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetricWidgetImageOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDashboardsOutput:
    boto3_raw_data: "type_defs.ListDashboardsOutputTypeDef" = dataclasses.field()

    @cached_property
    def DashboardEntries(self):  # pragma: no cover
        return DashboardEntry.make_many(self.boto3_raw_data["DashboardEntries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDashboardsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDashboardsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDashboardOutput:
    boto3_raw_data: "type_defs.PutDashboardOutputTypeDef" = dataclasses.field()

    @cached_property
    def DashboardValidationMessages(self):  # pragma: no cover
        return DashboardValidationMessage.make_many(
            self.boto3_raw_data["DashboardValidationMessages"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutDashboardOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDashboardOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutManagedInsightRulesOutput:
    boto3_raw_data: "type_defs.PutManagedInsightRulesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Failures(self):  # pragma: no cover
        return PartialFailure.make_many(self.boto3_raw_data["Failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutManagedInsightRulesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutManagedInsightRulesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutMetricStreamOutput:
    boto3_raw_data: "type_defs.PutMetricStreamOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutMetricStreamOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutMetricStreamOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAlarmHistoryInputAlarmDescribeHistory:
    boto3_raw_data: "type_defs.DescribeAlarmHistoryInputAlarmDescribeHistoryTypeDef" = (
        dataclasses.field()
    )

    AlarmContributorId = field("AlarmContributorId")
    AlarmTypes = field("AlarmTypes")
    HistoryItemType = field("HistoryItemType")
    StartDate = field("StartDate")
    EndDate = field("EndDate")
    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")
    ScanBy = field("ScanBy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAlarmHistoryInputAlarmDescribeHistoryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAlarmHistoryInputAlarmDescribeHistoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAlarmHistoryInput:
    boto3_raw_data: "type_defs.DescribeAlarmHistoryInputTypeDef" = dataclasses.field()

    AlarmName = field("AlarmName")
    AlarmContributorId = field("AlarmContributorId")
    AlarmTypes = field("AlarmTypes")
    HistoryItemType = field("HistoryItemType")
    StartDate = field("StartDate")
    EndDate = field("EndDate")
    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")
    ScanBy = field("ScanBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAlarmHistoryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAlarmHistoryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInsightRuleReportInput:
    boto3_raw_data: "type_defs.GetInsightRuleReportInputTypeDef" = dataclasses.field()

    RuleName = field("RuleName")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Period = field("Period")
    MaxContributorCount = field("MaxContributorCount")
    Metrics = field("Metrics")
    OrderBy = field("OrderBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInsightRuleReportInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInsightRuleReportInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetricStatisticsInputMetricGetStatistics:
    boto3_raw_data: "type_defs.GetMetricStatisticsInputMetricGetStatisticsTypeDef" = (
        dataclasses.field()
    )

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Period = field("Period")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    Statistics = field("Statistics")
    ExtendedStatistics = field("ExtendedStatistics")
    Unit = field("Unit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMetricStatisticsInputMetricGetStatisticsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetricStatisticsInputMetricGetStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetricStatisticsInput:
    boto3_raw_data: "type_defs.GetMetricStatisticsInputTypeDef" = dataclasses.field()

    Namespace = field("Namespace")
    MetricName = field("MetricName")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Period = field("Period")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    Statistics = field("Statistics")
    ExtendedStatistics = field("ExtendedStatistics")
    Unit = field("Unit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMetricStatisticsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetricStatisticsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Range:
    boto3_raw_data: "type_defs.RangeTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAlarmHistoryInputPaginate:
    boto3_raw_data: "type_defs.DescribeAlarmHistoryInputPaginateTypeDef" = (
        dataclasses.field()
    )

    AlarmName = field("AlarmName")
    AlarmContributorId = field("AlarmContributorId")
    AlarmTypes = field("AlarmTypes")
    HistoryItemType = field("HistoryItemType")
    StartDate = field("StartDate")
    EndDate = field("EndDate")
    ScanBy = field("ScanBy")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAlarmHistoryInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAlarmHistoryInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAlarmsInputPaginate:
    boto3_raw_data: "type_defs.DescribeAlarmsInputPaginateTypeDef" = dataclasses.field()

    AlarmNames = field("AlarmNames")
    AlarmNamePrefix = field("AlarmNamePrefix")
    AlarmTypes = field("AlarmTypes")
    ChildrenOfAlarmName = field("ChildrenOfAlarmName")
    ParentsOfAlarmName = field("ParentsOfAlarmName")
    StateValue = field("StateValue")
    ActionPrefix = field("ActionPrefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAlarmsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAlarmsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAnomalyDetectorsInputPaginate:
    boto3_raw_data: "type_defs.DescribeAnomalyDetectorsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    Namespace = field("Namespace")
    MetricName = field("MetricName")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    AnomalyDetectorTypes = field("AnomalyDetectorTypes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAnomalyDetectorsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAnomalyDetectorsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDashboardsInputPaginate:
    boto3_raw_data: "type_defs.ListDashboardsInputPaginateTypeDef" = dataclasses.field()

    DashboardNamePrefix = field("DashboardNamePrefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDashboardsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDashboardsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAlarmsInputWaitExtra:
    boto3_raw_data: "type_defs.DescribeAlarmsInputWaitExtraTypeDef" = (
        dataclasses.field()
    )

    AlarmNames = field("AlarmNames")
    AlarmNamePrefix = field("AlarmNamePrefix")
    AlarmTypes = field("AlarmTypes")
    ChildrenOfAlarmName = field("ChildrenOfAlarmName")
    ParentsOfAlarmName = field("ParentsOfAlarmName")
    StateValue = field("StateValue")
    ActionPrefix = field("ActionPrefix")
    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAlarmsInputWaitExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAlarmsInputWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAlarmsInputWait:
    boto3_raw_data: "type_defs.DescribeAlarmsInputWaitTypeDef" = dataclasses.field()

    AlarmNames = field("AlarmNames")
    AlarmNamePrefix = field("AlarmNamePrefix")
    AlarmTypes = field("AlarmTypes")
    ChildrenOfAlarmName = field("ChildrenOfAlarmName")
    ParentsOfAlarmName = field("ParentsOfAlarmName")
    StateValue = field("StateValue")
    ActionPrefix = field("ActionPrefix")
    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAlarmsInputWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAlarmsInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInsightRulesOutput:
    boto3_raw_data: "type_defs.DescribeInsightRulesOutputTypeDef" = dataclasses.field()

    @cached_property
    def InsightRules(self):  # pragma: no cover
        return InsightRule.make_many(self.boto3_raw_data["InsightRules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInsightRulesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInsightRulesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetricsInputPaginate:
    boto3_raw_data: "type_defs.ListMetricsInputPaginateTypeDef" = dataclasses.field()

    Namespace = field("Namespace")
    MetricName = field("MetricName")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return DimensionFilter.make_many(self.boto3_raw_data["Dimensions"])

    RecentlyActive = field("RecentlyActive")
    IncludeLinkedAccounts = field("IncludeLinkedAccounts")
    OwningAccount = field("OwningAccount")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMetricsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetricsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetricsInput:
    boto3_raw_data: "type_defs.ListMetricsInputTypeDef" = dataclasses.field()

    Namespace = field("Namespace")
    MetricName = field("MetricName")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return DimensionFilter.make_many(self.boto3_raw_data["Dimensions"])

    NextToken = field("NextToken")
    RecentlyActive = field("RecentlyActive")
    IncludeLinkedAccounts = field("IncludeLinkedAccounts")
    OwningAccount = field("OwningAccount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListMetricsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetricsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDataResult:
    boto3_raw_data: "type_defs.MetricDataResultTypeDef" = dataclasses.field()

    Id = field("Id")
    Label = field("Label")
    Timestamps = field("Timestamps")
    Values = field("Values")
    StatusCode = field("StatusCode")

    @cached_property
    def Messages(self):  # pragma: no cover
        return MessageData.make_many(self.boto3_raw_data["Messages"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricDataResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricDataResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InsightRuleContributor:
    boto3_raw_data: "type_defs.InsightRuleContributorTypeDef" = dataclasses.field()

    Keys = field("Keys")
    ApproximateAggregateValue = field("ApproximateAggregateValue")

    @cached_property
    def Datapoints(self):  # pragma: no cover
        return InsightRuleContributorDatapoint.make_many(
            self.boto3_raw_data["Datapoints"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InsightRuleContributorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InsightRuleContributorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetricStreamsOutput:
    boto3_raw_data: "type_defs.ListMetricStreamsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Entries(self):  # pragma: no cover
        return MetricStreamEntry.make_many(self.boto3_raw_data["Entries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMetricStreamsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetricStreamsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceOutput:
    boto3_raw_data: "type_defs.ListTagsForResourceOutputTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedRule:
    boto3_raw_data: "type_defs.ManagedRuleTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")
    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ManagedRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ManagedRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutCompositeAlarmInput:
    boto3_raw_data: "type_defs.PutCompositeAlarmInputTypeDef" = dataclasses.field()

    AlarmName = field("AlarmName")
    AlarmRule = field("AlarmRule")
    ActionsEnabled = field("ActionsEnabled")
    AlarmActions = field("AlarmActions")
    AlarmDescription = field("AlarmDescription")
    InsufficientDataActions = field("InsufficientDataActions")
    OKActions = field("OKActions")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ActionsSuppressor = field("ActionsSuppressor")
    ActionsSuppressorWaitPeriod = field("ActionsSuppressorWaitPeriod")
    ActionsSuppressorExtensionPeriod = field("ActionsSuppressorExtensionPeriod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutCompositeAlarmInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutCompositeAlarmInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutInsightRuleInput:
    boto3_raw_data: "type_defs.PutInsightRuleInputTypeDef" = dataclasses.field()

    RuleName = field("RuleName")
    RuleDefinition = field("RuleDefinition")
    RuleState = field("RuleState")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ApplyOnTransformedLogs = field("ApplyOnTransformedLogs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutInsightRuleInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutInsightRuleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceInput:
    boto3_raw_data: "type_defs.TagResourceInputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagResourceInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedRuleDescription:
    boto3_raw_data: "type_defs.ManagedRuleDescriptionTypeDef" = dataclasses.field()

    TemplateName = field("TemplateName")
    ResourceARN = field("ResourceARN")

    @cached_property
    def RuleState(self):  # pragma: no cover
        return ManagedRuleState.make_one(self.boto3_raw_data["RuleState"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedRuleDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedRuleDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDatum:
    boto3_raw_data: "type_defs.MetricDatumTypeDef" = dataclasses.field()

    MetricName = field("MetricName")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    Timestamp = field("Timestamp")
    Value = field("Value")

    @cached_property
    def StatisticValues(self):  # pragma: no cover
        return StatisticSet.make_one(self.boto3_raw_data["StatisticValues"])

    Values = field("Values")
    Counts = field("Counts")
    Unit = field("Unit")
    StorageResolution = field("StorageResolution")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricDatumTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricDatumTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricStreamStatisticsConfigurationOutput:
    boto3_raw_data: "type_defs.MetricStreamStatisticsConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IncludeMetrics(self):  # pragma: no cover
        return MetricStreamStatisticsMetric.make_many(
            self.boto3_raw_data["IncludeMetrics"]
        )

    AdditionalStatistics = field("AdditionalStatistics")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MetricStreamStatisticsConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricStreamStatisticsConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricStreamStatisticsConfiguration:
    boto3_raw_data: "type_defs.MetricStreamStatisticsConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IncludeMetrics(self):  # pragma: no cover
        return MetricStreamStatisticsMetric.make_many(
            self.boto3_raw_data["IncludeMetrics"]
        )

    AdditionalStatistics = field("AdditionalStatistics")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MetricStreamStatisticsConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricStreamStatisticsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetricsOutput:
    boto3_raw_data: "type_defs.ListMetricsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Metrics(self):  # pragma: no cover
        return MetricOutput.make_many(self.boto3_raw_data["Metrics"])

    OwningAccounts = field("OwningAccounts")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListMetricsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetricsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricStatOutput:
    boto3_raw_data: "type_defs.MetricStatOutputTypeDef" = dataclasses.field()

    @cached_property
    def Metric(self):  # pragma: no cover
        return MetricOutput.make_one(self.boto3_raw_data["Metric"])

    Period = field("Period")
    Stat = field("Stat")
    Unit = field("Unit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricStatOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricStatOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudwatchEventMetric:
    boto3_raw_data: "type_defs.CloudwatchEventMetricTypeDef" = dataclasses.field()

    id = field("id")
    returnData = field("returnData")

    @cached_property
    def metricStat(self):  # pragma: no cover
        return CloudwatchEventMetricStats.make_one(self.boto3_raw_data["metricStat"])

    expression = field("expression")
    label = field("label")
    period = field("period")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudwatchEventMetricTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudwatchEventMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyDetectorConfiguration:
    boto3_raw_data: "type_defs.AnomalyDetectorConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ExcludedTimeRanges(self):  # pragma: no cover
        return Range.make_many(self.boto3_raw_data["ExcludedTimeRanges"])

    MetricTimezone = field("MetricTimezone")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnomalyDetectorConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalyDetectorConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetricDataOutput:
    boto3_raw_data: "type_defs.GetMetricDataOutputTypeDef" = dataclasses.field()

    @cached_property
    def MetricDataResults(self):  # pragma: no cover
        return MetricDataResult.make_many(self.boto3_raw_data["MetricDataResults"])

    @cached_property
    def Messages(self):  # pragma: no cover
        return MessageData.make_many(self.boto3_raw_data["Messages"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMetricDataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetricDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInsightRuleReportOutput:
    boto3_raw_data: "type_defs.GetInsightRuleReportOutputTypeDef" = dataclasses.field()

    KeyLabels = field("KeyLabels")
    AggregationStatistic = field("AggregationStatistic")
    AggregateValue = field("AggregateValue")
    ApproximateUniqueCount = field("ApproximateUniqueCount")

    @cached_property
    def Contributors(self):  # pragma: no cover
        return InsightRuleContributor.make_many(self.boto3_raw_data["Contributors"])

    @cached_property
    def MetricDatapoints(self):  # pragma: no cover
        return InsightRuleMetricDatapoint.make_many(
            self.boto3_raw_data["MetricDatapoints"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInsightRuleReportOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInsightRuleReportOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutManagedInsightRulesInput:
    boto3_raw_data: "type_defs.PutManagedInsightRulesInputTypeDef" = dataclasses.field()

    @cached_property
    def ManagedRules(self):  # pragma: no cover
        return ManagedRule.make_many(self.boto3_raw_data["ManagedRules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutManagedInsightRulesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutManagedInsightRulesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedInsightRulesOutput:
    boto3_raw_data: "type_defs.ListManagedInsightRulesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ManagedRules(self):  # pragma: no cover
        return ManagedRuleDescription.make_many(self.boto3_raw_data["ManagedRules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListManagedInsightRulesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedInsightRulesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityMetricData:
    boto3_raw_data: "type_defs.EntityMetricDataTypeDef" = dataclasses.field()

    @cached_property
    def Entity(self):  # pragma: no cover
        return Entity.make_one(self.boto3_raw_data["Entity"])

    @cached_property
    def MetricData(self):  # pragma: no cover
        return MetricDatum.make_many(self.boto3_raw_data["MetricData"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntityMetricDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityMetricDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetricStreamOutput:
    boto3_raw_data: "type_defs.GetMetricStreamOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")

    @cached_property
    def IncludeFilters(self):  # pragma: no cover
        return MetricStreamFilterOutput.make_many(self.boto3_raw_data["IncludeFilters"])

    @cached_property
    def ExcludeFilters(self):  # pragma: no cover
        return MetricStreamFilterOutput.make_many(self.boto3_raw_data["ExcludeFilters"])

    FirehoseArn = field("FirehoseArn")
    RoleArn = field("RoleArn")
    State = field("State")
    CreationDate = field("CreationDate")
    LastUpdateDate = field("LastUpdateDate")
    OutputFormat = field("OutputFormat")

    @cached_property
    def StatisticsConfigurations(self):  # pragma: no cover
        return MetricStreamStatisticsConfigurationOutput.make_many(
            self.boto3_raw_data["StatisticsConfigurations"]
        )

    IncludeLinkedAccountsMetrics = field("IncludeLinkedAccountsMetrics")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMetricStreamOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetricStreamOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDataQueryOutput:
    boto3_raw_data: "type_defs.MetricDataQueryOutputTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def MetricStat(self):  # pragma: no cover
        return MetricStatOutput.make_one(self.boto3_raw_data["MetricStat"])

    Expression = field("Expression")
    Label = field("Label")
    ReturnData = field("ReturnData")
    Period = field("Period")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricDataQueryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricDataQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricStat:
    boto3_raw_data: "type_defs.MetricStatTypeDef" = dataclasses.field()

    Metric = field("Metric")
    Period = field("Period")
    Stat = field("Stat")
    Unit = field("Unit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricStatTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricStatTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudwatchEventDetailConfiguration:
    boto3_raw_data: "type_defs.CloudwatchEventDetailConfigurationTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    description = field("description")

    @cached_property
    def metrics(self):  # pragma: no cover
        return CloudwatchEventMetric.make_many(self.boto3_raw_data["metrics"])

    actionsSuppressor = field("actionsSuppressor")
    actionsSuppressorWaitPeriod = field("actionsSuppressorWaitPeriod")
    actionsSuppressorExtensionPeriod = field("actionsSuppressorExtensionPeriod")
    threshold = field("threshold")
    evaluationPeriods = field("evaluationPeriods")
    alarmRule = field("alarmRule")
    alarmName = field("alarmName")
    treatMissingData = field("treatMissingData")
    comparisonOperator = field("comparisonOperator")
    timestamp = field("timestamp")
    actionsEnabled = field("actionsEnabled")
    okActions = field("okActions")
    alarmActions = field("alarmActions")
    insufficientDataActions = field("insufficientDataActions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CloudwatchEventDetailConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudwatchEventDetailConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutMetricDataInputMetricPutData:
    boto3_raw_data: "type_defs.PutMetricDataInputMetricPutDataTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EntityMetricData(self):  # pragma: no cover
        return EntityMetricData.make_many(self.boto3_raw_data["EntityMetricData"])

    StrictEntityValidation = field("StrictEntityValidation")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutMetricDataInputMetricPutDataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutMetricDataInputMetricPutDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutMetricDataInput:
    boto3_raw_data: "type_defs.PutMetricDataInputTypeDef" = dataclasses.field()

    Namespace = field("Namespace")

    @cached_property
    def MetricData(self):  # pragma: no cover
        return MetricDatum.make_many(self.boto3_raw_data["MetricData"])

    @cached_property
    def EntityMetricData(self):  # pragma: no cover
        return EntityMetricData.make_many(self.boto3_raw_data["EntityMetricData"])

    StrictEntityValidation = field("StrictEntityValidation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutMetricDataInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutMetricDataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutMetricStreamInput:
    boto3_raw_data: "type_defs.PutMetricStreamInputTypeDef" = dataclasses.field()

    Name = field("Name")
    FirehoseArn = field("FirehoseArn")
    RoleArn = field("RoleArn")
    OutputFormat = field("OutputFormat")
    IncludeFilters = field("IncludeFilters")
    ExcludeFilters = field("ExcludeFilters")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    StatisticsConfigurations = field("StatisticsConfigurations")
    IncludeLinkedAccountsMetrics = field("IncludeLinkedAccountsMetrics")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutMetricStreamInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutMetricStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricAlarm:
    boto3_raw_data: "type_defs.MetricAlarmTypeDef" = dataclasses.field()

    AlarmName = field("AlarmName")
    AlarmArn = field("AlarmArn")
    AlarmDescription = field("AlarmDescription")
    AlarmConfigurationUpdatedTimestamp = field("AlarmConfigurationUpdatedTimestamp")
    ActionsEnabled = field("ActionsEnabled")
    OKActions = field("OKActions")
    AlarmActions = field("AlarmActions")
    InsufficientDataActions = field("InsufficientDataActions")
    StateValue = field("StateValue")
    StateReason = field("StateReason")
    StateReasonData = field("StateReasonData")
    StateUpdatedTimestamp = field("StateUpdatedTimestamp")
    MetricName = field("MetricName")
    Namespace = field("Namespace")
    Statistic = field("Statistic")
    ExtendedStatistic = field("ExtendedStatistic")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    Period = field("Period")
    Unit = field("Unit")
    EvaluationPeriods = field("EvaluationPeriods")
    DatapointsToAlarm = field("DatapointsToAlarm")
    Threshold = field("Threshold")
    ComparisonOperator = field("ComparisonOperator")
    TreatMissingData = field("TreatMissingData")
    EvaluateLowSampleCountPercentile = field("EvaluateLowSampleCountPercentile")

    @cached_property
    def Metrics(self):  # pragma: no cover
        return MetricDataQueryOutput.make_many(self.boto3_raw_data["Metrics"])

    ThresholdMetricId = field("ThresholdMetricId")
    EvaluationState = field("EvaluationState")
    StateTransitionedTimestamp = field("StateTransitionedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricAlarmTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricAlarmTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricMathAnomalyDetectorOutput:
    boto3_raw_data: "type_defs.MetricMathAnomalyDetectorOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MetricDataQueries(self):  # pragma: no cover
        return MetricDataQueryOutput.make_many(self.boto3_raw_data["MetricDataQueries"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MetricMathAnomalyDetectorOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricMathAnomalyDetectorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudwatchEventDetail:
    boto3_raw_data: "type_defs.CloudwatchEventDetailTypeDef" = dataclasses.field()

    alarmName = field("alarmName")

    @cached_property
    def state(self):  # pragma: no cover
        return CloudwatchEventState.make_one(self.boto3_raw_data["state"])

    operation = field("operation")

    @cached_property
    def configuration(self):  # pragma: no cover
        return CloudwatchEventDetailConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    @cached_property
    def previousConfiguration(self):  # pragma: no cover
        return CloudwatchEventDetailConfiguration.make_one(
            self.boto3_raw_data["previousConfiguration"]
        )

    @cached_property
    def previousState(self):  # pragma: no cover
        return CloudwatchEventState.make_one(self.boto3_raw_data["previousState"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudwatchEventDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudwatchEventDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAlarmsForMetricOutput:
    boto3_raw_data: "type_defs.DescribeAlarmsForMetricOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MetricAlarms(self):  # pragma: no cover
        return MetricAlarm.make_many(self.boto3_raw_data["MetricAlarms"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAlarmsForMetricOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAlarmsForMetricOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAlarmsOutput:
    boto3_raw_data: "type_defs.DescribeAlarmsOutputTypeDef" = dataclasses.field()

    @cached_property
    def CompositeAlarms(self):  # pragma: no cover
        return CompositeAlarm.make_many(self.boto3_raw_data["CompositeAlarms"])

    @cached_property
    def MetricAlarms(self):  # pragma: no cover
        return MetricAlarm.make_many(self.boto3_raw_data["MetricAlarms"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAlarmsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAlarmsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricStatAlarm:
    boto3_raw_data: "type_defs.MetricStatAlarmTypeDef" = dataclasses.field()

    @cached_property
    def Metric(self):  # pragma: no cover
        return MetricAlarm.make_one(self.boto3_raw_data["Metric"])

    Period = field("Period")
    Stat = field("Stat")
    Unit = field("Unit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricStatAlarmTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricStatAlarmTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyDetector:
    boto3_raw_data: "type_defs.AnomalyDetectorTypeDef" = dataclasses.field()

    Namespace = field("Namespace")
    MetricName = field("MetricName")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    Stat = field("Stat")

    @cached_property
    def Configuration(self):  # pragma: no cover
        return AnomalyDetectorConfigurationOutput.make_one(
            self.boto3_raw_data["Configuration"]
        )

    StateValue = field("StateValue")

    @cached_property
    def MetricCharacteristics(self):  # pragma: no cover
        return MetricCharacteristics.make_one(
            self.boto3_raw_data["MetricCharacteristics"]
        )

    @cached_property
    def SingleMetricAnomalyDetector(self):  # pragma: no cover
        return SingleMetricAnomalyDetectorOutput.make_one(
            self.boto3_raw_data["SingleMetricAnomalyDetector"]
        )

    @cached_property
    def MetricMathAnomalyDetector(self):  # pragma: no cover
        return MetricMathAnomalyDetectorOutput.make_one(
            self.boto3_raw_data["MetricMathAnomalyDetector"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnomalyDetectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnomalyDetectorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDataQuery:
    boto3_raw_data: "type_defs.MetricDataQueryTypeDef" = dataclasses.field()

    Id = field("Id")
    MetricStat = field("MetricStat")
    Expression = field("Expression")
    Label = field("Label")
    ReturnData = field("ReturnData")
    Period = field("Period")
    AccountId = field("AccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricDataQueryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricDataQueryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudwatchEvent:
    boto3_raw_data: "type_defs.CloudwatchEventTypeDef" = dataclasses.field()

    version = field("version")
    id = field("id")
    detail - type = field("detail-type")
    source = field("source")
    account = field("account")
    time = field("time")
    region = field("region")
    resources = field("resources")

    @cached_property
    def detail(self):  # pragma: no cover
        return CloudwatchEventDetail.make_one(self.boto3_raw_data["detail"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CloudwatchEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CloudwatchEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDataQueryAlarm:
    boto3_raw_data: "type_defs.MetricDataQueryAlarmTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def MetricStat(self):  # pragma: no cover
        return MetricStatAlarm.make_one(self.boto3_raw_data["MetricStat"])

    Expression = field("Expression")
    Label = field("Label")
    ReturnData = field("ReturnData")
    Period = field("Period")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricDataQueryAlarmTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricDataQueryAlarmTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAnomalyDetectorsOutput:
    boto3_raw_data: "type_defs.DescribeAnomalyDetectorsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AnomalyDetectors(self):  # pragma: no cover
        return AnomalyDetector.make_many(self.boto3_raw_data["AnomalyDetectors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAnomalyDetectorsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAnomalyDetectorsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricMathAnomalyDetector:
    boto3_raw_data: "type_defs.MetricMathAnomalyDetectorTypeDef" = dataclasses.field()

    @cached_property
    def MetricDataQueries(self):  # pragma: no cover
        return MetricDataQuery.make_many(self.boto3_raw_data["MetricDataQueries"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricMathAnomalyDetectorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricMathAnomalyDetectorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetricDataInputPaginate:
    boto3_raw_data: "type_defs.GetMetricDataInputPaginateTypeDef" = dataclasses.field()

    MetricDataQueries = field("MetricDataQueries")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    ScanBy = field("ScanBy")

    @cached_property
    def LabelOptions(self):  # pragma: no cover
        return LabelOptions.make_one(self.boto3_raw_data["LabelOptions"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMetricDataInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetricDataInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetricDataInput:
    boto3_raw_data: "type_defs.GetMetricDataInputTypeDef" = dataclasses.field()

    MetricDataQueries = field("MetricDataQueries")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    NextToken = field("NextToken")
    ScanBy = field("ScanBy")
    MaxDatapoints = field("MaxDatapoints")

    @cached_property
    def LabelOptions(self):  # pragma: no cover
        return LabelOptions.make_one(self.boto3_raw_data["LabelOptions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMetricDataInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetricDataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutMetricAlarmInputMetricPutAlarm:
    boto3_raw_data: "type_defs.PutMetricAlarmInputMetricPutAlarmTypeDef" = (
        dataclasses.field()
    )

    AlarmName = field("AlarmName")
    EvaluationPeriods = field("EvaluationPeriods")
    ComparisonOperator = field("ComparisonOperator")
    AlarmDescription = field("AlarmDescription")
    ActionsEnabled = field("ActionsEnabled")
    OKActions = field("OKActions")
    AlarmActions = field("AlarmActions")
    InsufficientDataActions = field("InsufficientDataActions")
    Statistic = field("Statistic")
    ExtendedStatistic = field("ExtendedStatistic")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    Period = field("Period")
    Unit = field("Unit")
    DatapointsToAlarm = field("DatapointsToAlarm")
    Threshold = field("Threshold")
    TreatMissingData = field("TreatMissingData")
    EvaluateLowSampleCountPercentile = field("EvaluateLowSampleCountPercentile")
    Metrics = field("Metrics")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ThresholdMetricId = field("ThresholdMetricId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutMetricAlarmInputMetricPutAlarmTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutMetricAlarmInputMetricPutAlarmTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutMetricAlarmInput:
    boto3_raw_data: "type_defs.PutMetricAlarmInputTypeDef" = dataclasses.field()

    AlarmName = field("AlarmName")
    EvaluationPeriods = field("EvaluationPeriods")
    ComparisonOperator = field("ComparisonOperator")
    AlarmDescription = field("AlarmDescription")
    ActionsEnabled = field("ActionsEnabled")
    OKActions = field("OKActions")
    AlarmActions = field("AlarmActions")
    InsufficientDataActions = field("InsufficientDataActions")
    MetricName = field("MetricName")
    Namespace = field("Namespace")
    Statistic = field("Statistic")
    ExtendedStatistic = field("ExtendedStatistic")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    Period = field("Period")
    Unit = field("Unit")
    DatapointsToAlarm = field("DatapointsToAlarm")
    Threshold = field("Threshold")
    TreatMissingData = field("TreatMissingData")
    EvaluateLowSampleCountPercentile = field("EvaluateLowSampleCountPercentile")
    Metrics = field("Metrics")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ThresholdMetricId = field("ThresholdMetricId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutMetricAlarmInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutMetricAlarmInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAnomalyDetectorInput:
    boto3_raw_data: "type_defs.DeleteAnomalyDetectorInputTypeDef" = dataclasses.field()

    Namespace = field("Namespace")
    MetricName = field("MetricName")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    Stat = field("Stat")
    SingleMetricAnomalyDetector = field("SingleMetricAnomalyDetector")
    MetricMathAnomalyDetector = field("MetricMathAnomalyDetector")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAnomalyDetectorInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAnomalyDetectorInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAnomalyDetectorInput:
    boto3_raw_data: "type_defs.PutAnomalyDetectorInputTypeDef" = dataclasses.field()

    Namespace = field("Namespace")
    MetricName = field("MetricName")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    Stat = field("Stat")
    Configuration = field("Configuration")

    @cached_property
    def MetricCharacteristics(self):  # pragma: no cover
        return MetricCharacteristics.make_one(
            self.boto3_raw_data["MetricCharacteristics"]
        )

    SingleMetricAnomalyDetector = field("SingleMetricAnomalyDetector")
    MetricMathAnomalyDetector = field("MetricMathAnomalyDetector")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAnomalyDetectorInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAnomalyDetectorInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
