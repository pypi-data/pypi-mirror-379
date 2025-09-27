# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cloudwatch import type_defs as bs_td


class CLOUDWATCHCaster:

    def delete_alarms(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_insight_rules(
        self,
        res: "bs_td.DeleteInsightRulesOutputTypeDef",
    ) -> "dc_td.DeleteInsightRulesOutput":
        return dc_td.DeleteInsightRulesOutput.make_one(res)

    def describe_alarm_contributors(
        self,
        res: "bs_td.DescribeAlarmContributorsOutputTypeDef",
    ) -> "dc_td.DescribeAlarmContributorsOutput":
        return dc_td.DescribeAlarmContributorsOutput.make_one(res)

    def describe_alarm_history(
        self,
        res: "bs_td.DescribeAlarmHistoryOutputTypeDef",
    ) -> "dc_td.DescribeAlarmHistoryOutput":
        return dc_td.DescribeAlarmHistoryOutput.make_one(res)

    def describe_alarms(
        self,
        res: "bs_td.DescribeAlarmsOutputTypeDef",
    ) -> "dc_td.DescribeAlarmsOutput":
        return dc_td.DescribeAlarmsOutput.make_one(res)

    def describe_alarms_for_metric(
        self,
        res: "bs_td.DescribeAlarmsForMetricOutputTypeDef",
    ) -> "dc_td.DescribeAlarmsForMetricOutput":
        return dc_td.DescribeAlarmsForMetricOutput.make_one(res)

    def describe_anomaly_detectors(
        self,
        res: "bs_td.DescribeAnomalyDetectorsOutputTypeDef",
    ) -> "dc_td.DescribeAnomalyDetectorsOutput":
        return dc_td.DescribeAnomalyDetectorsOutput.make_one(res)

    def describe_insight_rules(
        self,
        res: "bs_td.DescribeInsightRulesOutputTypeDef",
    ) -> "dc_td.DescribeInsightRulesOutput":
        return dc_td.DescribeInsightRulesOutput.make_one(res)

    def disable_alarm_actions(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disable_insight_rules(
        self,
        res: "bs_td.DisableInsightRulesOutputTypeDef",
    ) -> "dc_td.DisableInsightRulesOutput":
        return dc_td.DisableInsightRulesOutput.make_one(res)

    def enable_alarm_actions(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def enable_insight_rules(
        self,
        res: "bs_td.EnableInsightRulesOutputTypeDef",
    ) -> "dc_td.EnableInsightRulesOutput":
        return dc_td.EnableInsightRulesOutput.make_one(res)

    def get_dashboard(
        self,
        res: "bs_td.GetDashboardOutputTypeDef",
    ) -> "dc_td.GetDashboardOutput":
        return dc_td.GetDashboardOutput.make_one(res)

    def get_insight_rule_report(
        self,
        res: "bs_td.GetInsightRuleReportOutputTypeDef",
    ) -> "dc_td.GetInsightRuleReportOutput":
        return dc_td.GetInsightRuleReportOutput.make_one(res)

    def get_metric_data(
        self,
        res: "bs_td.GetMetricDataOutputTypeDef",
    ) -> "dc_td.GetMetricDataOutput":
        return dc_td.GetMetricDataOutput.make_one(res)

    def get_metric_statistics(
        self,
        res: "bs_td.GetMetricStatisticsOutputTypeDef",
    ) -> "dc_td.GetMetricStatisticsOutput":
        return dc_td.GetMetricStatisticsOutput.make_one(res)

    def get_metric_stream(
        self,
        res: "bs_td.GetMetricStreamOutputTypeDef",
    ) -> "dc_td.GetMetricStreamOutput":
        return dc_td.GetMetricStreamOutput.make_one(res)

    def get_metric_widget_image(
        self,
        res: "bs_td.GetMetricWidgetImageOutputTypeDef",
    ) -> "dc_td.GetMetricWidgetImageOutput":
        return dc_td.GetMetricWidgetImageOutput.make_one(res)

    def list_dashboards(
        self,
        res: "bs_td.ListDashboardsOutputTypeDef",
    ) -> "dc_td.ListDashboardsOutput":
        return dc_td.ListDashboardsOutput.make_one(res)

    def list_managed_insight_rules(
        self,
        res: "bs_td.ListManagedInsightRulesOutputTypeDef",
    ) -> "dc_td.ListManagedInsightRulesOutput":
        return dc_td.ListManagedInsightRulesOutput.make_one(res)

    def list_metric_streams(
        self,
        res: "bs_td.ListMetricStreamsOutputTypeDef",
    ) -> "dc_td.ListMetricStreamsOutput":
        return dc_td.ListMetricStreamsOutput.make_one(res)

    def list_metrics(
        self,
        res: "bs_td.ListMetricsOutputTypeDef",
    ) -> "dc_td.ListMetricsOutput":
        return dc_td.ListMetricsOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def put_composite_alarm(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_dashboard(
        self,
        res: "bs_td.PutDashboardOutputTypeDef",
    ) -> "dc_td.PutDashboardOutput":
        return dc_td.PutDashboardOutput.make_one(res)

    def put_managed_insight_rules(
        self,
        res: "bs_td.PutManagedInsightRulesOutputTypeDef",
    ) -> "dc_td.PutManagedInsightRulesOutput":
        return dc_td.PutManagedInsightRulesOutput.make_one(res)

    def put_metric_alarm(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_metric_data(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_metric_stream(
        self,
        res: "bs_td.PutMetricStreamOutputTypeDef",
    ) -> "dc_td.PutMetricStreamOutput":
        return dc_td.PutMetricStreamOutput.make_one(res)

    def set_alarm_state(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


cloudwatch_caster = CLOUDWATCHCaster()
