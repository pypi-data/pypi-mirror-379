# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_application_autoscaling import type_defs as bs_td


class APPLICATION_AUTOSCALINGCaster:

    def describe_scalable_targets(
        self,
        res: "bs_td.DescribeScalableTargetsResponseTypeDef",
    ) -> "dc_td.DescribeScalableTargetsResponse":
        return dc_td.DescribeScalableTargetsResponse.make_one(res)

    def describe_scaling_activities(
        self,
        res: "bs_td.DescribeScalingActivitiesResponseTypeDef",
    ) -> "dc_td.DescribeScalingActivitiesResponse":
        return dc_td.DescribeScalingActivitiesResponse.make_one(res)

    def describe_scaling_policies(
        self,
        res: "bs_td.DescribeScalingPoliciesResponseTypeDef",
    ) -> "dc_td.DescribeScalingPoliciesResponse":
        return dc_td.DescribeScalingPoliciesResponse.make_one(res)

    def describe_scheduled_actions(
        self,
        res: "bs_td.DescribeScheduledActionsResponseTypeDef",
    ) -> "dc_td.DescribeScheduledActionsResponse":
        return dc_td.DescribeScheduledActionsResponse.make_one(res)

    def get_predictive_scaling_forecast(
        self,
        res: "bs_td.GetPredictiveScalingForecastResponseTypeDef",
    ) -> "dc_td.GetPredictiveScalingForecastResponse":
        return dc_td.GetPredictiveScalingForecastResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_scaling_policy(
        self,
        res: "bs_td.PutScalingPolicyResponseTypeDef",
    ) -> "dc_td.PutScalingPolicyResponse":
        return dc_td.PutScalingPolicyResponse.make_one(res)

    def register_scalable_target(
        self,
        res: "bs_td.RegisterScalableTargetResponseTypeDef",
    ) -> "dc_td.RegisterScalableTargetResponse":
        return dc_td.RegisterScalableTargetResponse.make_one(res)


application_autoscaling_caster = APPLICATION_AUTOSCALINGCaster()
