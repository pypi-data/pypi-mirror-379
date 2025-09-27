# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_application_autoscaling import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Alarm:
    boto3_raw_data: "type_defs.AlarmTypeDef" = dataclasses.field()

    AlarmName = field("AlarmName")
    AlarmARN = field("AlarmARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlarmTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AlarmTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityForecast:
    boto3_raw_data: "type_defs.CapacityForecastTypeDef" = dataclasses.field()

    Timestamps = field("Timestamps")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CapacityForecastTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityForecastTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDimension:
    boto3_raw_data: "type_defs.MetricDimensionTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricDimensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricDimensionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteScalingPolicyRequest:
    boto3_raw_data: "type_defs.DeleteScalingPolicyRequestTypeDef" = dataclasses.field()

    PolicyName = field("PolicyName")
    ServiceNamespace = field("ServiceNamespace")
    ResourceId = field("ResourceId")
    ScalableDimension = field("ScalableDimension")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteScalingPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteScalingPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteScheduledActionRequest:
    boto3_raw_data: "type_defs.DeleteScheduledActionRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceNamespace = field("ServiceNamespace")
    ScheduledActionName = field("ScheduledActionName")
    ResourceId = field("ResourceId")
    ScalableDimension = field("ScalableDimension")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteScheduledActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteScheduledActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterScalableTargetRequest:
    boto3_raw_data: "type_defs.DeregisterScalableTargetRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceNamespace = field("ServiceNamespace")
    ResourceId = field("ResourceId")
    ScalableDimension = field("ScalableDimension")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeregisterScalableTargetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterScalableTargetRequestTypeDef"]
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
class DescribeScalableTargetsRequest:
    boto3_raw_data: "type_defs.DescribeScalableTargetsRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceNamespace = field("ServiceNamespace")
    ResourceIds = field("ResourceIds")
    ScalableDimension = field("ScalableDimension")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeScalableTargetsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScalableTargetsRequestTypeDef"]
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
class DescribeScalingActivitiesRequest:
    boto3_raw_data: "type_defs.DescribeScalingActivitiesRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceNamespace = field("ServiceNamespace")
    ResourceId = field("ResourceId")
    ScalableDimension = field("ScalableDimension")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    IncludeNotScaledActivities = field("IncludeNotScaledActivities")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeScalingActivitiesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScalingActivitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScalingPoliciesRequest:
    boto3_raw_data: "type_defs.DescribeScalingPoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceNamespace = field("ServiceNamespace")
    PolicyNames = field("PolicyNames")
    ResourceId = field("ResourceId")
    ScalableDimension = field("ScalableDimension")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeScalingPoliciesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScalingPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScheduledActionsRequest:
    boto3_raw_data: "type_defs.DescribeScheduledActionsRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceNamespace = field("ServiceNamespace")
    ScheduledActionNames = field("ScheduledActionNames")
    ResourceId = field("ResourceId")
    ScalableDimension = field("ScalableDimension")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeScheduledActionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScheduledActionsRequestTypeDef"]
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
class NotScaledReason:
    boto3_raw_data: "type_defs.NotScaledReasonTypeDef" = dataclasses.field()

    Code = field("Code")
    MaxCapacity = field("MaxCapacity")
    MinCapacity = field("MinCapacity")
    CurrentCapacity = field("CurrentCapacity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NotScaledReasonTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NotScaledReasonTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredefinedMetricSpecification:
    boto3_raw_data: "type_defs.PredefinedMetricSpecificationTypeDef" = (
        dataclasses.field()
    )

    PredefinedMetricType = field("PredefinedMetricType")
    ResourceLabel = field("ResourceLabel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PredefinedMetricSpecificationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredefinedMetricSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingMetricDimension:
    boto3_raw_data: "type_defs.PredictiveScalingMetricDimensionTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PredictiveScalingMetricDimensionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveScalingMetricDimensionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingPredefinedLoadMetricSpecification:
    boto3_raw_data: (
        "type_defs.PredictiveScalingPredefinedLoadMetricSpecificationTypeDef"
    ) = dataclasses.field()

    PredefinedMetricType = field("PredefinedMetricType")
    ResourceLabel = field("ResourceLabel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingPredefinedLoadMetricSpecificationTypeDef"
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
                "type_defs.PredictiveScalingPredefinedLoadMetricSpecificationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingPredefinedMetricPairSpecification:
    boto3_raw_data: (
        "type_defs.PredictiveScalingPredefinedMetricPairSpecificationTypeDef"
    ) = dataclasses.field()

    PredefinedMetricType = field("PredefinedMetricType")
    ResourceLabel = field("ResourceLabel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingPredefinedMetricPairSpecificationTypeDef"
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
                "type_defs.PredictiveScalingPredefinedMetricPairSpecificationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingPredefinedScalingMetricSpecification:
    boto3_raw_data: (
        "type_defs.PredictiveScalingPredefinedScalingMetricSpecificationTypeDef"
    ) = dataclasses.field()

    PredefinedMetricType = field("PredefinedMetricType")
    ResourceLabel = field("ResourceLabel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingPredefinedScalingMetricSpecificationTypeDef"
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
                "type_defs.PredictiveScalingPredefinedScalingMetricSpecificationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalableTargetAction:
    boto3_raw_data: "type_defs.ScalableTargetActionTypeDef" = dataclasses.field()

    MinCapacity = field("MinCapacity")
    MaxCapacity = field("MaxCapacity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScalableTargetActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalableTargetActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuspendedState:
    boto3_raw_data: "type_defs.SuspendedStateTypeDef" = dataclasses.field()

    DynamicScalingInSuspended = field("DynamicScalingInSuspended")
    DynamicScalingOutSuspended = field("DynamicScalingOutSuspended")
    ScheduledScalingSuspended = field("ScheduledScalingSuspended")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SuspendedStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SuspendedStateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepAdjustment:
    boto3_raw_data: "type_defs.StepAdjustmentTypeDef" = dataclasses.field()

    ScalingAdjustment = field("ScalingAdjustment")
    MetricIntervalLowerBound = field("MetricIntervalLowerBound")
    MetricIntervalUpperBound = field("MetricIntervalUpperBound")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepAdjustmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StepAdjustmentTypeDef"]],
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
    Tags = field("Tags")

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
class TargetTrackingMetricDimension:
    boto3_raw_data: "type_defs.TargetTrackingMetricDimensionTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TargetTrackingMetricDimensionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetTrackingMetricDimensionTypeDef"]
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
class DescribeScalableTargetsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeScalableTargetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ServiceNamespace = field("ServiceNamespace")
    ResourceIds = field("ResourceIds")
    ScalableDimension = field("ScalableDimension")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeScalableTargetsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScalableTargetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScalingActivitiesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeScalingActivitiesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ServiceNamespace = field("ServiceNamespace")
    ResourceId = field("ResourceId")
    ScalableDimension = field("ScalableDimension")
    IncludeNotScaledActivities = field("IncludeNotScaledActivities")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeScalingActivitiesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScalingActivitiesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScalingPoliciesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeScalingPoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ServiceNamespace = field("ServiceNamespace")
    PolicyNames = field("PolicyNames")
    ResourceId = field("ResourceId")
    ScalableDimension = field("ScalableDimension")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeScalingPoliciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScalingPoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScheduledActionsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeScheduledActionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ServiceNamespace = field("ServiceNamespace")
    ScheduledActionNames = field("ScheduledActionNames")
    ResourceId = field("ResourceId")
    ScalableDimension = field("ScalableDimension")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeScheduledActionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScheduledActionsRequestPaginateTypeDef"]
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

    Tags = field("Tags")

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
class PutScalingPolicyResponse:
    boto3_raw_data: "type_defs.PutScalingPolicyResponseTypeDef" = dataclasses.field()

    PolicyARN = field("PolicyARN")

    @cached_property
    def Alarms(self):  # pragma: no cover
        return Alarm.make_many(self.boto3_raw_data["Alarms"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutScalingPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutScalingPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterScalableTargetResponse:
    boto3_raw_data: "type_defs.RegisterScalableTargetResponseTypeDef" = (
        dataclasses.field()
    )

    ScalableTargetARN = field("ScalableTargetARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisterScalableTargetResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterScalableTargetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPredictiveScalingForecastRequest:
    boto3_raw_data: "type_defs.GetPredictiveScalingForecastRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceNamespace = field("ServiceNamespace")
    ResourceId = field("ResourceId")
    ScalableDimension = field("ScalableDimension")
    PolicyName = field("PolicyName")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetPredictiveScalingForecastRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPredictiveScalingForecastRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingActivity:
    boto3_raw_data: "type_defs.ScalingActivityTypeDef" = dataclasses.field()

    ActivityId = field("ActivityId")
    ServiceNamespace = field("ServiceNamespace")
    ResourceId = field("ResourceId")
    ScalableDimension = field("ScalableDimension")
    Description = field("Description")
    Cause = field("Cause")
    StartTime = field("StartTime")
    StatusCode = field("StatusCode")
    EndTime = field("EndTime")
    StatusMessage = field("StatusMessage")
    Details = field("Details")

    @cached_property
    def NotScaledReasons(self):  # pragma: no cover
        return NotScaledReason.make_many(self.boto3_raw_data["NotScaledReasons"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScalingActivityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScalingActivityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingMetricOutput:
    boto3_raw_data: "type_defs.PredictiveScalingMetricOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return PredictiveScalingMetricDimension.make_many(
            self.boto3_raw_data["Dimensions"]
        )

    MetricName = field("MetricName")
    Namespace = field("Namespace")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PredictiveScalingMetricOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveScalingMetricOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingMetric:
    boto3_raw_data: "type_defs.PredictiveScalingMetricTypeDef" = dataclasses.field()

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return PredictiveScalingMetricDimension.make_many(
            self.boto3_raw_data["Dimensions"]
        )

    MetricName = field("MetricName")
    Namespace = field("Namespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PredictiveScalingMetricTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveScalingMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutScheduledActionRequest:
    boto3_raw_data: "type_defs.PutScheduledActionRequestTypeDef" = dataclasses.field()

    ServiceNamespace = field("ServiceNamespace")
    ScheduledActionName = field("ScheduledActionName")
    ResourceId = field("ResourceId")
    ScalableDimension = field("ScalableDimension")
    Schedule = field("Schedule")
    Timezone = field("Timezone")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def ScalableTargetAction(self):  # pragma: no cover
        return ScalableTargetAction.make_one(
            self.boto3_raw_data["ScalableTargetAction"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutScheduledActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutScheduledActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledAction:
    boto3_raw_data: "type_defs.ScheduledActionTypeDef" = dataclasses.field()

    ScheduledActionName = field("ScheduledActionName")
    ScheduledActionARN = field("ScheduledActionARN")
    ServiceNamespace = field("ServiceNamespace")
    Schedule = field("Schedule")
    ResourceId = field("ResourceId")
    CreationTime = field("CreationTime")
    Timezone = field("Timezone")
    ScalableDimension = field("ScalableDimension")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def ScalableTargetAction(self):  # pragma: no cover
        return ScalableTargetAction.make_one(
            self.boto3_raw_data["ScalableTargetAction"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduledActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduledActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterScalableTargetRequest:
    boto3_raw_data: "type_defs.RegisterScalableTargetRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceNamespace = field("ServiceNamespace")
    ResourceId = field("ResourceId")
    ScalableDimension = field("ScalableDimension")
    MinCapacity = field("MinCapacity")
    MaxCapacity = field("MaxCapacity")
    RoleARN = field("RoleARN")

    @cached_property
    def SuspendedState(self):  # pragma: no cover
        return SuspendedState.make_one(self.boto3_raw_data["SuspendedState"])

    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisterScalableTargetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterScalableTargetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalableTarget:
    boto3_raw_data: "type_defs.ScalableTargetTypeDef" = dataclasses.field()

    ServiceNamespace = field("ServiceNamespace")
    ResourceId = field("ResourceId")
    ScalableDimension = field("ScalableDimension")
    MinCapacity = field("MinCapacity")
    MaxCapacity = field("MaxCapacity")
    RoleARN = field("RoleARN")
    CreationTime = field("CreationTime")
    PredictedCapacity = field("PredictedCapacity")

    @cached_property
    def SuspendedState(self):  # pragma: no cover
        return SuspendedState.make_one(self.boto3_raw_data["SuspendedState"])

    ScalableTargetARN = field("ScalableTargetARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScalableTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScalableTargetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepScalingPolicyConfigurationOutput:
    boto3_raw_data: "type_defs.StepScalingPolicyConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    AdjustmentType = field("AdjustmentType")

    @cached_property
    def StepAdjustments(self):  # pragma: no cover
        return StepAdjustment.make_many(self.boto3_raw_data["StepAdjustments"])

    MinAdjustmentMagnitude = field("MinAdjustmentMagnitude")
    Cooldown = field("Cooldown")
    MetricAggregationType = field("MetricAggregationType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StepScalingPolicyConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StepScalingPolicyConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepScalingPolicyConfiguration:
    boto3_raw_data: "type_defs.StepScalingPolicyConfigurationTypeDef" = (
        dataclasses.field()
    )

    AdjustmentType = field("AdjustmentType")

    @cached_property
    def StepAdjustments(self):  # pragma: no cover
        return StepAdjustment.make_many(self.boto3_raw_data["StepAdjustments"])

    MinAdjustmentMagnitude = field("MinAdjustmentMagnitude")
    Cooldown = field("Cooldown")
    MetricAggregationType = field("MetricAggregationType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StepScalingPolicyConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StepScalingPolicyConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetTrackingMetricOutput:
    boto3_raw_data: "type_defs.TargetTrackingMetricOutputTypeDef" = dataclasses.field()

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return TargetTrackingMetricDimension.make_many(
            self.boto3_raw_data["Dimensions"]
        )

    MetricName = field("MetricName")
    Namespace = field("Namespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetTrackingMetricOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetTrackingMetricOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetTrackingMetric:
    boto3_raw_data: "type_defs.TargetTrackingMetricTypeDef" = dataclasses.field()

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return TargetTrackingMetricDimension.make_many(
            self.boto3_raw_data["Dimensions"]
        )

    MetricName = field("MetricName")
    Namespace = field("Namespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetTrackingMetricTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetTrackingMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScalingActivitiesResponse:
    boto3_raw_data: "type_defs.DescribeScalingActivitiesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ScalingActivities(self):  # pragma: no cover
        return ScalingActivity.make_many(self.boto3_raw_data["ScalingActivities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeScalingActivitiesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScalingActivitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingMetricStatOutput:
    boto3_raw_data: "type_defs.PredictiveScalingMetricStatOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Metric(self):  # pragma: no cover
        return PredictiveScalingMetricOutput.make_one(self.boto3_raw_data["Metric"])

    Stat = field("Stat")
    Unit = field("Unit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingMetricStatOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveScalingMetricStatOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingMetricStat:
    boto3_raw_data: "type_defs.PredictiveScalingMetricStatTypeDef" = dataclasses.field()

    @cached_property
    def Metric(self):  # pragma: no cover
        return PredictiveScalingMetric.make_one(self.boto3_raw_data["Metric"])

    Stat = field("Stat")
    Unit = field("Unit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PredictiveScalingMetricStatTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveScalingMetricStatTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScheduledActionsResponse:
    boto3_raw_data: "type_defs.DescribeScheduledActionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ScheduledActions(self):  # pragma: no cover
        return ScheduledAction.make_many(self.boto3_raw_data["ScheduledActions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeScheduledActionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScheduledActionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScalableTargetsResponse:
    boto3_raw_data: "type_defs.DescribeScalableTargetsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ScalableTargets(self):  # pragma: no cover
        return ScalableTarget.make_many(self.boto3_raw_data["ScalableTargets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeScalableTargetsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScalableTargetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetTrackingMetricStatOutput:
    boto3_raw_data: "type_defs.TargetTrackingMetricStatOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Metric(self):  # pragma: no cover
        return TargetTrackingMetricOutput.make_one(self.boto3_raw_data["Metric"])

    Stat = field("Stat")
    Unit = field("Unit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TargetTrackingMetricStatOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetTrackingMetricStatOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetTrackingMetricStat:
    boto3_raw_data: "type_defs.TargetTrackingMetricStatTypeDef" = dataclasses.field()

    @cached_property
    def Metric(self):  # pragma: no cover
        return TargetTrackingMetric.make_one(self.boto3_raw_data["Metric"])

    Stat = field("Stat")
    Unit = field("Unit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetTrackingMetricStatTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetTrackingMetricStatTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingMetricDataQueryOutput:
    boto3_raw_data: "type_defs.PredictiveScalingMetricDataQueryOutputTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Expression = field("Expression")

    @cached_property
    def MetricStat(self):  # pragma: no cover
        return PredictiveScalingMetricStatOutput.make_one(
            self.boto3_raw_data["MetricStat"]
        )

    Label = field("Label")
    ReturnData = field("ReturnData")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingMetricDataQueryOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveScalingMetricDataQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingMetricDataQuery:
    boto3_raw_data: "type_defs.PredictiveScalingMetricDataQueryTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Expression = field("Expression")

    @cached_property
    def MetricStat(self):  # pragma: no cover
        return PredictiveScalingMetricStat.make_one(self.boto3_raw_data["MetricStat"])

    Label = field("Label")
    ReturnData = field("ReturnData")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PredictiveScalingMetricDataQueryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveScalingMetricDataQueryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetTrackingMetricDataQueryOutput:
    boto3_raw_data: "type_defs.TargetTrackingMetricDataQueryOutputTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Expression = field("Expression")
    Label = field("Label")

    @cached_property
    def MetricStat(self):  # pragma: no cover
        return TargetTrackingMetricStatOutput.make_one(
            self.boto3_raw_data["MetricStat"]
        )

    ReturnData = field("ReturnData")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TargetTrackingMetricDataQueryOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetTrackingMetricDataQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetTrackingMetricDataQuery:
    boto3_raw_data: "type_defs.TargetTrackingMetricDataQueryTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Expression = field("Expression")
    Label = field("Label")

    @cached_property
    def MetricStat(self):  # pragma: no cover
        return TargetTrackingMetricStat.make_one(self.boto3_raw_data["MetricStat"])

    ReturnData = field("ReturnData")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TargetTrackingMetricDataQueryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetTrackingMetricDataQueryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingCustomizedMetricSpecificationOutput:
    boto3_raw_data: (
        "type_defs.PredictiveScalingCustomizedMetricSpecificationOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def MetricDataQueries(self):  # pragma: no cover
        return PredictiveScalingMetricDataQueryOutput.make_many(
            self.boto3_raw_data["MetricDataQueries"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingCustomizedMetricSpecificationOutputTypeDef"
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
                "type_defs.PredictiveScalingCustomizedMetricSpecificationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingCustomizedMetricSpecification:
    boto3_raw_data: (
        "type_defs.PredictiveScalingCustomizedMetricSpecificationTypeDef"
    ) = dataclasses.field()

    @cached_property
    def MetricDataQueries(self):  # pragma: no cover
        return PredictiveScalingMetricDataQuery.make_many(
            self.boto3_raw_data["MetricDataQueries"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingCustomizedMetricSpecificationTypeDef"
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
                "type_defs.PredictiveScalingCustomizedMetricSpecificationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomizedMetricSpecificationOutput:
    boto3_raw_data: "type_defs.CustomizedMetricSpecificationOutputTypeDef" = (
        dataclasses.field()
    )

    MetricName = field("MetricName")
    Namespace = field("Namespace")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return MetricDimension.make_many(self.boto3_raw_data["Dimensions"])

    Statistic = field("Statistic")
    Unit = field("Unit")

    @cached_property
    def Metrics(self):  # pragma: no cover
        return TargetTrackingMetricDataQueryOutput.make_many(
            self.boto3_raw_data["Metrics"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomizedMetricSpecificationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomizedMetricSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomizedMetricSpecification:
    boto3_raw_data: "type_defs.CustomizedMetricSpecificationTypeDef" = (
        dataclasses.field()
    )

    MetricName = field("MetricName")
    Namespace = field("Namespace")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return MetricDimension.make_many(self.boto3_raw_data["Dimensions"])

    Statistic = field("Statistic")
    Unit = field("Unit")

    @cached_property
    def Metrics(self):  # pragma: no cover
        return TargetTrackingMetricDataQuery.make_many(self.boto3_raw_data["Metrics"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomizedMetricSpecificationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomizedMetricSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingMetricSpecificationOutput:
    boto3_raw_data: "type_defs.PredictiveScalingMetricSpecificationOutputTypeDef" = (
        dataclasses.field()
    )

    TargetValue = field("TargetValue")

    @cached_property
    def PredefinedMetricPairSpecification(self):  # pragma: no cover
        return PredictiveScalingPredefinedMetricPairSpecification.make_one(
            self.boto3_raw_data["PredefinedMetricPairSpecification"]
        )

    @cached_property
    def PredefinedScalingMetricSpecification(self):  # pragma: no cover
        return PredictiveScalingPredefinedScalingMetricSpecification.make_one(
            self.boto3_raw_data["PredefinedScalingMetricSpecification"]
        )

    @cached_property
    def PredefinedLoadMetricSpecification(self):  # pragma: no cover
        return PredictiveScalingPredefinedLoadMetricSpecification.make_one(
            self.boto3_raw_data["PredefinedLoadMetricSpecification"]
        )

    @cached_property
    def CustomizedScalingMetricSpecification(self):  # pragma: no cover
        return PredictiveScalingCustomizedMetricSpecificationOutput.make_one(
            self.boto3_raw_data["CustomizedScalingMetricSpecification"]
        )

    @cached_property
    def CustomizedLoadMetricSpecification(self):  # pragma: no cover
        return PredictiveScalingCustomizedMetricSpecificationOutput.make_one(
            self.boto3_raw_data["CustomizedLoadMetricSpecification"]
        )

    @cached_property
    def CustomizedCapacityMetricSpecification(self):  # pragma: no cover
        return PredictiveScalingCustomizedMetricSpecificationOutput.make_one(
            self.boto3_raw_data["CustomizedCapacityMetricSpecification"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingMetricSpecificationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveScalingMetricSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingMetricSpecification:
    boto3_raw_data: "type_defs.PredictiveScalingMetricSpecificationTypeDef" = (
        dataclasses.field()
    )

    TargetValue = field("TargetValue")

    @cached_property
    def PredefinedMetricPairSpecification(self):  # pragma: no cover
        return PredictiveScalingPredefinedMetricPairSpecification.make_one(
            self.boto3_raw_data["PredefinedMetricPairSpecification"]
        )

    @cached_property
    def PredefinedScalingMetricSpecification(self):  # pragma: no cover
        return PredictiveScalingPredefinedScalingMetricSpecification.make_one(
            self.boto3_raw_data["PredefinedScalingMetricSpecification"]
        )

    @cached_property
    def PredefinedLoadMetricSpecification(self):  # pragma: no cover
        return PredictiveScalingPredefinedLoadMetricSpecification.make_one(
            self.boto3_raw_data["PredefinedLoadMetricSpecification"]
        )

    @cached_property
    def CustomizedScalingMetricSpecification(self):  # pragma: no cover
        return PredictiveScalingCustomizedMetricSpecification.make_one(
            self.boto3_raw_data["CustomizedScalingMetricSpecification"]
        )

    @cached_property
    def CustomizedLoadMetricSpecification(self):  # pragma: no cover
        return PredictiveScalingCustomizedMetricSpecification.make_one(
            self.boto3_raw_data["CustomizedLoadMetricSpecification"]
        )

    @cached_property
    def CustomizedCapacityMetricSpecification(self):  # pragma: no cover
        return PredictiveScalingCustomizedMetricSpecification.make_one(
            self.boto3_raw_data["CustomizedCapacityMetricSpecification"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingMetricSpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveScalingMetricSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetTrackingScalingPolicyConfigurationOutput:
    boto3_raw_data: (
        "type_defs.TargetTrackingScalingPolicyConfigurationOutputTypeDef"
    ) = dataclasses.field()

    TargetValue = field("TargetValue")

    @cached_property
    def PredefinedMetricSpecification(self):  # pragma: no cover
        return PredefinedMetricSpecification.make_one(
            self.boto3_raw_data["PredefinedMetricSpecification"]
        )

    @cached_property
    def CustomizedMetricSpecification(self):  # pragma: no cover
        return CustomizedMetricSpecificationOutput.make_one(
            self.boto3_raw_data["CustomizedMetricSpecification"]
        )

    ScaleOutCooldown = field("ScaleOutCooldown")
    ScaleInCooldown = field("ScaleInCooldown")
    DisableScaleIn = field("DisableScaleIn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TargetTrackingScalingPolicyConfigurationOutputTypeDef"
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
                "type_defs.TargetTrackingScalingPolicyConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetTrackingScalingPolicyConfiguration:
    boto3_raw_data: "type_defs.TargetTrackingScalingPolicyConfigurationTypeDef" = (
        dataclasses.field()
    )

    TargetValue = field("TargetValue")

    @cached_property
    def PredefinedMetricSpecification(self):  # pragma: no cover
        return PredefinedMetricSpecification.make_one(
            self.boto3_raw_data["PredefinedMetricSpecification"]
        )

    @cached_property
    def CustomizedMetricSpecification(self):  # pragma: no cover
        return CustomizedMetricSpecification.make_one(
            self.boto3_raw_data["CustomizedMetricSpecification"]
        )

    ScaleOutCooldown = field("ScaleOutCooldown")
    ScaleInCooldown = field("ScaleInCooldown")
    DisableScaleIn = field("DisableScaleIn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TargetTrackingScalingPolicyConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetTrackingScalingPolicyConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadForecast:
    boto3_raw_data: "type_defs.LoadForecastTypeDef" = dataclasses.field()

    Timestamps = field("Timestamps")
    Values = field("Values")

    @cached_property
    def MetricSpecification(self):  # pragma: no cover
        return PredictiveScalingMetricSpecificationOutput.make_one(
            self.boto3_raw_data["MetricSpecification"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoadForecastTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoadForecastTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingPolicyConfigurationOutput:
    boto3_raw_data: "type_defs.PredictiveScalingPolicyConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MetricSpecifications(self):  # pragma: no cover
        return PredictiveScalingMetricSpecificationOutput.make_many(
            self.boto3_raw_data["MetricSpecifications"]
        )

    Mode = field("Mode")
    SchedulingBufferTime = field("SchedulingBufferTime")
    MaxCapacityBreachBehavior = field("MaxCapacityBreachBehavior")
    MaxCapacityBuffer = field("MaxCapacityBuffer")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingPolicyConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveScalingPolicyConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingPolicyConfiguration:
    boto3_raw_data: "type_defs.PredictiveScalingPolicyConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MetricSpecifications(self):  # pragma: no cover
        return PredictiveScalingMetricSpecification.make_many(
            self.boto3_raw_data["MetricSpecifications"]
        )

    Mode = field("Mode")
    SchedulingBufferTime = field("SchedulingBufferTime")
    MaxCapacityBreachBehavior = field("MaxCapacityBreachBehavior")
    MaxCapacityBuffer = field("MaxCapacityBuffer")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingPolicyConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveScalingPolicyConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPredictiveScalingForecastResponse:
    boto3_raw_data: "type_defs.GetPredictiveScalingForecastResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LoadForecast(self):  # pragma: no cover
        return LoadForecast.make_many(self.boto3_raw_data["LoadForecast"])

    @cached_property
    def CapacityForecast(self):  # pragma: no cover
        return CapacityForecast.make_one(self.boto3_raw_data["CapacityForecast"])

    UpdateTime = field("UpdateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetPredictiveScalingForecastResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPredictiveScalingForecastResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingPolicy:
    boto3_raw_data: "type_defs.ScalingPolicyTypeDef" = dataclasses.field()

    PolicyARN = field("PolicyARN")
    PolicyName = field("PolicyName")
    ServiceNamespace = field("ServiceNamespace")
    ResourceId = field("ResourceId")
    ScalableDimension = field("ScalableDimension")
    PolicyType = field("PolicyType")
    CreationTime = field("CreationTime")

    @cached_property
    def StepScalingPolicyConfiguration(self):  # pragma: no cover
        return StepScalingPolicyConfigurationOutput.make_one(
            self.boto3_raw_data["StepScalingPolicyConfiguration"]
        )

    @cached_property
    def TargetTrackingScalingPolicyConfiguration(self):  # pragma: no cover
        return TargetTrackingScalingPolicyConfigurationOutput.make_one(
            self.boto3_raw_data["TargetTrackingScalingPolicyConfiguration"]
        )

    @cached_property
    def PredictiveScalingPolicyConfiguration(self):  # pragma: no cover
        return PredictiveScalingPolicyConfigurationOutput.make_one(
            self.boto3_raw_data["PredictiveScalingPolicyConfiguration"]
        )

    @cached_property
    def Alarms(self):  # pragma: no cover
        return Alarm.make_many(self.boto3_raw_data["Alarms"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScalingPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScalingPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScalingPoliciesResponse:
    boto3_raw_data: "type_defs.DescribeScalingPoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ScalingPolicies(self):  # pragma: no cover
        return ScalingPolicy.make_many(self.boto3_raw_data["ScalingPolicies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeScalingPoliciesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScalingPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutScalingPolicyRequest:
    boto3_raw_data: "type_defs.PutScalingPolicyRequestTypeDef" = dataclasses.field()

    PolicyName = field("PolicyName")
    ServiceNamespace = field("ServiceNamespace")
    ResourceId = field("ResourceId")
    ScalableDimension = field("ScalableDimension")
    PolicyType = field("PolicyType")
    StepScalingPolicyConfiguration = field("StepScalingPolicyConfiguration")
    TargetTrackingScalingPolicyConfiguration = field(
        "TargetTrackingScalingPolicyConfiguration"
    )
    PredictiveScalingPolicyConfiguration = field("PredictiveScalingPolicyConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutScalingPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutScalingPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
