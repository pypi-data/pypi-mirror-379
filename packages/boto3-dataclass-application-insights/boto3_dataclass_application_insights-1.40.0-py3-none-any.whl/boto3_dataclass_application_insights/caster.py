# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_application_insights import type_defs as bs_td


class APPLICATION_INSIGHTSCaster:

    def add_workload(
        self,
        res: "bs_td.AddWorkloadResponseTypeDef",
    ) -> "dc_td.AddWorkloadResponse":
        return dc_td.AddWorkloadResponse.make_one(res)

    def create_application(
        self,
        res: "bs_td.CreateApplicationResponseTypeDef",
    ) -> "dc_td.CreateApplicationResponse":
        return dc_td.CreateApplicationResponse.make_one(res)

    def create_log_pattern(
        self,
        res: "bs_td.CreateLogPatternResponseTypeDef",
    ) -> "dc_td.CreateLogPatternResponse":
        return dc_td.CreateLogPatternResponse.make_one(res)

    def describe_application(
        self,
        res: "bs_td.DescribeApplicationResponseTypeDef",
    ) -> "dc_td.DescribeApplicationResponse":
        return dc_td.DescribeApplicationResponse.make_one(res)

    def describe_component(
        self,
        res: "bs_td.DescribeComponentResponseTypeDef",
    ) -> "dc_td.DescribeComponentResponse":
        return dc_td.DescribeComponentResponse.make_one(res)

    def describe_component_configuration(
        self,
        res: "bs_td.DescribeComponentConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeComponentConfigurationResponse":
        return dc_td.DescribeComponentConfigurationResponse.make_one(res)

    def describe_component_configuration_recommendation(
        self,
        res: "bs_td.DescribeComponentConfigurationRecommendationResponseTypeDef",
    ) -> "dc_td.DescribeComponentConfigurationRecommendationResponse":
        return dc_td.DescribeComponentConfigurationRecommendationResponse.make_one(res)

    def describe_log_pattern(
        self,
        res: "bs_td.DescribeLogPatternResponseTypeDef",
    ) -> "dc_td.DescribeLogPatternResponse":
        return dc_td.DescribeLogPatternResponse.make_one(res)

    def describe_observation(
        self,
        res: "bs_td.DescribeObservationResponseTypeDef",
    ) -> "dc_td.DescribeObservationResponse":
        return dc_td.DescribeObservationResponse.make_one(res)

    def describe_problem(
        self,
        res: "bs_td.DescribeProblemResponseTypeDef",
    ) -> "dc_td.DescribeProblemResponse":
        return dc_td.DescribeProblemResponse.make_one(res)

    def describe_problem_observations(
        self,
        res: "bs_td.DescribeProblemObservationsResponseTypeDef",
    ) -> "dc_td.DescribeProblemObservationsResponse":
        return dc_td.DescribeProblemObservationsResponse.make_one(res)

    def describe_workload(
        self,
        res: "bs_td.DescribeWorkloadResponseTypeDef",
    ) -> "dc_td.DescribeWorkloadResponse":
        return dc_td.DescribeWorkloadResponse.make_one(res)

    def list_applications(
        self,
        res: "bs_td.ListApplicationsResponseTypeDef",
    ) -> "dc_td.ListApplicationsResponse":
        return dc_td.ListApplicationsResponse.make_one(res)

    def list_components(
        self,
        res: "bs_td.ListComponentsResponseTypeDef",
    ) -> "dc_td.ListComponentsResponse":
        return dc_td.ListComponentsResponse.make_one(res)

    def list_configuration_history(
        self,
        res: "bs_td.ListConfigurationHistoryResponseTypeDef",
    ) -> "dc_td.ListConfigurationHistoryResponse":
        return dc_td.ListConfigurationHistoryResponse.make_one(res)

    def list_log_pattern_sets(
        self,
        res: "bs_td.ListLogPatternSetsResponseTypeDef",
    ) -> "dc_td.ListLogPatternSetsResponse":
        return dc_td.ListLogPatternSetsResponse.make_one(res)

    def list_log_patterns(
        self,
        res: "bs_td.ListLogPatternsResponseTypeDef",
    ) -> "dc_td.ListLogPatternsResponse":
        return dc_td.ListLogPatternsResponse.make_one(res)

    def list_problems(
        self,
        res: "bs_td.ListProblemsResponseTypeDef",
    ) -> "dc_td.ListProblemsResponse":
        return dc_td.ListProblemsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_workloads(
        self,
        res: "bs_td.ListWorkloadsResponseTypeDef",
    ) -> "dc_td.ListWorkloadsResponse":
        return dc_td.ListWorkloadsResponse.make_one(res)

    def update_application(
        self,
        res: "bs_td.UpdateApplicationResponseTypeDef",
    ) -> "dc_td.UpdateApplicationResponse":
        return dc_td.UpdateApplicationResponse.make_one(res)

    def update_log_pattern(
        self,
        res: "bs_td.UpdateLogPatternResponseTypeDef",
    ) -> "dc_td.UpdateLogPatternResponse":
        return dc_td.UpdateLogPatternResponse.make_one(res)

    def update_workload(
        self,
        res: "bs_td.UpdateWorkloadResponseTypeDef",
    ) -> "dc_td.UpdateWorkloadResponse":
        return dc_td.UpdateWorkloadResponse.make_one(res)


application_insights_caster = APPLICATION_INSIGHTSCaster()
