# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_autoscaling_plans import type_defs as bs_td


class AUTOSCALING_PLANSCaster:

    def create_scaling_plan(
        self,
        res: "bs_td.CreateScalingPlanResponseTypeDef",
    ) -> "dc_td.CreateScalingPlanResponse":
        return dc_td.CreateScalingPlanResponse.make_one(res)

    def describe_scaling_plan_resources(
        self,
        res: "bs_td.DescribeScalingPlanResourcesResponseTypeDef",
    ) -> "dc_td.DescribeScalingPlanResourcesResponse":
        return dc_td.DescribeScalingPlanResourcesResponse.make_one(res)

    def describe_scaling_plans(
        self,
        res: "bs_td.DescribeScalingPlansResponseTypeDef",
    ) -> "dc_td.DescribeScalingPlansResponse":
        return dc_td.DescribeScalingPlansResponse.make_one(res)

    def get_scaling_plan_resource_forecast_data(
        self,
        res: "bs_td.GetScalingPlanResourceForecastDataResponseTypeDef",
    ) -> "dc_td.GetScalingPlanResourceForecastDataResponse":
        return dc_td.GetScalingPlanResourceForecastDataResponse.make_one(res)


autoscaling_plans_caster = AUTOSCALING_PLANSCaster()
