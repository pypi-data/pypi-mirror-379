# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_autoscaling_plans import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class TagFilterOutput:
    boto3_raw_data: "type_defs.TagFilterOutputTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagFilterOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagFilterOutputTypeDef"]],
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
class Datapoint:
    boto3_raw_data: "type_defs.DatapointTypeDef" = dataclasses.field()

    Timestamp = field("Timestamp")
    Value = field("Value")

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
class DeleteScalingPlanRequest:
    boto3_raw_data: "type_defs.DeleteScalingPlanRequestTypeDef" = dataclasses.field()

    ScalingPlanName = field("ScalingPlanName")
    ScalingPlanVersion = field("ScalingPlanVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteScalingPlanRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteScalingPlanRequestTypeDef"]
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
class DescribeScalingPlanResourcesRequest:
    boto3_raw_data: "type_defs.DescribeScalingPlanResourcesRequestTypeDef" = (
        dataclasses.field()
    )

    ScalingPlanName = field("ScalingPlanName")
    ScalingPlanVersion = field("ScalingPlanVersion")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeScalingPlanResourcesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScalingPlanResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredefinedLoadMetricSpecification:
    boto3_raw_data: "type_defs.PredefinedLoadMetricSpecificationTypeDef" = (
        dataclasses.field()
    )

    PredefinedLoadMetricType = field("PredefinedLoadMetricType")
    ResourceLabel = field("ResourceLabel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredefinedLoadMetricSpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredefinedLoadMetricSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredefinedScalingMetricSpecification:
    boto3_raw_data: "type_defs.PredefinedScalingMetricSpecificationTypeDef" = (
        dataclasses.field()
    )

    PredefinedScalingMetricType = field("PredefinedScalingMetricType")
    ResourceLabel = field("ResourceLabel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredefinedScalingMetricSpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredefinedScalingMetricSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagFilter:
    boto3_raw_data: "type_defs.TagFilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationSourceOutput:
    boto3_raw_data: "type_defs.ApplicationSourceOutputTypeDef" = dataclasses.field()

    CloudFormationStackARN = field("CloudFormationStackARN")

    @cached_property
    def TagFilters(self):  # pragma: no cover
        return TagFilterOutput.make_many(self.boto3_raw_data["TagFilters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationSourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateScalingPlanResponse:
    boto3_raw_data: "type_defs.CreateScalingPlanResponseTypeDef" = dataclasses.field()

    ScalingPlanVersion = field("ScalingPlanVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateScalingPlanResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateScalingPlanResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomizedLoadMetricSpecificationOutput:
    boto3_raw_data: "type_defs.CustomizedLoadMetricSpecificationOutputTypeDef" = (
        dataclasses.field()
    )

    MetricName = field("MetricName")
    Namespace = field("Namespace")
    Statistic = field("Statistic")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return MetricDimension.make_many(self.boto3_raw_data["Dimensions"])

    Unit = field("Unit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomizedLoadMetricSpecificationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomizedLoadMetricSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomizedLoadMetricSpecification:
    boto3_raw_data: "type_defs.CustomizedLoadMetricSpecificationTypeDef" = (
        dataclasses.field()
    )

    MetricName = field("MetricName")
    Namespace = field("Namespace")
    Statistic = field("Statistic")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return MetricDimension.make_many(self.boto3_raw_data["Dimensions"])

    Unit = field("Unit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomizedLoadMetricSpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomizedLoadMetricSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomizedScalingMetricSpecificationOutput:
    boto3_raw_data: "type_defs.CustomizedScalingMetricSpecificationOutputTypeDef" = (
        dataclasses.field()
    )

    MetricName = field("MetricName")
    Namespace = field("Namespace")
    Statistic = field("Statistic")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return MetricDimension.make_many(self.boto3_raw_data["Dimensions"])

    Unit = field("Unit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomizedScalingMetricSpecificationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomizedScalingMetricSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomizedScalingMetricSpecification:
    boto3_raw_data: "type_defs.CustomizedScalingMetricSpecificationTypeDef" = (
        dataclasses.field()
    )

    MetricName = field("MetricName")
    Namespace = field("Namespace")
    Statistic = field("Statistic")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return MetricDimension.make_many(self.boto3_raw_data["Dimensions"])

    Unit = field("Unit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomizedScalingMetricSpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomizedScalingMetricSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetScalingPlanResourceForecastDataResponse:
    boto3_raw_data: "type_defs.GetScalingPlanResourceForecastDataResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Datapoints(self):  # pragma: no cover
        return Datapoint.make_many(self.boto3_raw_data["Datapoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetScalingPlanResourceForecastDataResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetScalingPlanResourceForecastDataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScalingPlanResourcesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeScalingPlanResourcesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ScalingPlanName = field("ScalingPlanName")
    ScalingPlanVersion = field("ScalingPlanVersion")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeScalingPlanResourcesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScalingPlanResourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetScalingPlanResourceForecastDataRequest:
    boto3_raw_data: "type_defs.GetScalingPlanResourceForecastDataRequestTypeDef" = (
        dataclasses.field()
    )

    ScalingPlanName = field("ScalingPlanName")
    ScalingPlanVersion = field("ScalingPlanVersion")
    ServiceNamespace = field("ServiceNamespace")
    ResourceId = field("ResourceId")
    ScalableDimension = field("ScalableDimension")
    ForecastDataType = field("ForecastDataType")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetScalingPlanResourceForecastDataRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetScalingPlanResourceForecastDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetTrackingConfigurationOutput:
    boto3_raw_data: "type_defs.TargetTrackingConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    TargetValue = field("TargetValue")

    @cached_property
    def PredefinedScalingMetricSpecification(self):  # pragma: no cover
        return PredefinedScalingMetricSpecification.make_one(
            self.boto3_raw_data["PredefinedScalingMetricSpecification"]
        )

    @cached_property
    def CustomizedScalingMetricSpecification(self):  # pragma: no cover
        return CustomizedScalingMetricSpecificationOutput.make_one(
            self.boto3_raw_data["CustomizedScalingMetricSpecification"]
        )

    DisableScaleIn = field("DisableScaleIn")
    ScaleOutCooldown = field("ScaleOutCooldown")
    ScaleInCooldown = field("ScaleInCooldown")
    EstimatedInstanceWarmup = field("EstimatedInstanceWarmup")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TargetTrackingConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetTrackingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationSource:
    boto3_raw_data: "type_defs.ApplicationSourceTypeDef" = dataclasses.field()

    CloudFormationStackARN = field("CloudFormationStackARN")
    TagFilters = field("TagFilters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApplicationSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingInstructionOutput:
    boto3_raw_data: "type_defs.ScalingInstructionOutputTypeDef" = dataclasses.field()

    ServiceNamespace = field("ServiceNamespace")
    ResourceId = field("ResourceId")
    ScalableDimension = field("ScalableDimension")
    MinCapacity = field("MinCapacity")
    MaxCapacity = field("MaxCapacity")

    @cached_property
    def TargetTrackingConfigurations(self):  # pragma: no cover
        return TargetTrackingConfigurationOutput.make_many(
            self.boto3_raw_data["TargetTrackingConfigurations"]
        )

    @cached_property
    def PredefinedLoadMetricSpecification(self):  # pragma: no cover
        return PredefinedLoadMetricSpecification.make_one(
            self.boto3_raw_data["PredefinedLoadMetricSpecification"]
        )

    @cached_property
    def CustomizedLoadMetricSpecification(self):  # pragma: no cover
        return CustomizedLoadMetricSpecificationOutput.make_one(
            self.boto3_raw_data["CustomizedLoadMetricSpecification"]
        )

    ScheduledActionBufferTime = field("ScheduledActionBufferTime")
    PredictiveScalingMaxCapacityBehavior = field("PredictiveScalingMaxCapacityBehavior")
    PredictiveScalingMaxCapacityBuffer = field("PredictiveScalingMaxCapacityBuffer")
    PredictiveScalingMode = field("PredictiveScalingMode")
    ScalingPolicyUpdateBehavior = field("ScalingPolicyUpdateBehavior")
    DisableDynamicScaling = field("DisableDynamicScaling")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScalingInstructionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalingInstructionOutputTypeDef"]
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

    PolicyName = field("PolicyName")
    PolicyType = field("PolicyType")

    @cached_property
    def TargetTrackingConfiguration(self):  # pragma: no cover
        return TargetTrackingConfigurationOutput.make_one(
            self.boto3_raw_data["TargetTrackingConfiguration"]
        )

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
class TargetTrackingConfiguration:
    boto3_raw_data: "type_defs.TargetTrackingConfigurationTypeDef" = dataclasses.field()

    TargetValue = field("TargetValue")

    @cached_property
    def PredefinedScalingMetricSpecification(self):  # pragma: no cover
        return PredefinedScalingMetricSpecification.make_one(
            self.boto3_raw_data["PredefinedScalingMetricSpecification"]
        )

    CustomizedScalingMetricSpecification = field("CustomizedScalingMetricSpecification")
    DisableScaleIn = field("DisableScaleIn")
    ScaleOutCooldown = field("ScaleOutCooldown")
    ScaleInCooldown = field("ScaleInCooldown")
    EstimatedInstanceWarmup = field("EstimatedInstanceWarmup")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetTrackingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetTrackingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingPlan:
    boto3_raw_data: "type_defs.ScalingPlanTypeDef" = dataclasses.field()

    ScalingPlanName = field("ScalingPlanName")
    ScalingPlanVersion = field("ScalingPlanVersion")

    @cached_property
    def ApplicationSource(self):  # pragma: no cover
        return ApplicationSourceOutput.make_one(
            self.boto3_raw_data["ApplicationSource"]
        )

    @cached_property
    def ScalingInstructions(self):  # pragma: no cover
        return ScalingInstructionOutput.make_many(
            self.boto3_raw_data["ScalingInstructions"]
        )

    StatusCode = field("StatusCode")
    StatusMessage = field("StatusMessage")
    StatusStartTime = field("StatusStartTime")
    CreationTime = field("CreationTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScalingPlanTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScalingPlanTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingPlanResource:
    boto3_raw_data: "type_defs.ScalingPlanResourceTypeDef" = dataclasses.field()

    ScalingPlanName = field("ScalingPlanName")
    ScalingPlanVersion = field("ScalingPlanVersion")
    ServiceNamespace = field("ServiceNamespace")
    ResourceId = field("ResourceId")
    ScalableDimension = field("ScalableDimension")
    ScalingStatusCode = field("ScalingStatusCode")

    @cached_property
    def ScalingPolicies(self):  # pragma: no cover
        return ScalingPolicy.make_many(self.boto3_raw_data["ScalingPolicies"])

    ScalingStatusMessage = field("ScalingStatusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScalingPlanResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalingPlanResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScalingPlansRequestPaginate:
    boto3_raw_data: "type_defs.DescribeScalingPlansRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ScalingPlanNames = field("ScalingPlanNames")
    ScalingPlanVersion = field("ScalingPlanVersion")
    ApplicationSources = field("ApplicationSources")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeScalingPlansRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScalingPlansRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScalingPlansRequest:
    boto3_raw_data: "type_defs.DescribeScalingPlansRequestTypeDef" = dataclasses.field()

    ScalingPlanNames = field("ScalingPlanNames")
    ScalingPlanVersion = field("ScalingPlanVersion")
    ApplicationSources = field("ApplicationSources")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeScalingPlansRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScalingPlansRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScalingPlansResponse:
    boto3_raw_data: "type_defs.DescribeScalingPlansResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ScalingPlans(self):  # pragma: no cover
        return ScalingPlan.make_many(self.boto3_raw_data["ScalingPlans"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeScalingPlansResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScalingPlansResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScalingPlanResourcesResponse:
    boto3_raw_data: "type_defs.DescribeScalingPlanResourcesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ScalingPlanResources(self):  # pragma: no cover
        return ScalingPlanResource.make_many(
            self.boto3_raw_data["ScalingPlanResources"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeScalingPlanResourcesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScalingPlanResourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingInstruction:
    boto3_raw_data: "type_defs.ScalingInstructionTypeDef" = dataclasses.field()

    ServiceNamespace = field("ServiceNamespace")
    ResourceId = field("ResourceId")
    ScalableDimension = field("ScalableDimension")
    MinCapacity = field("MinCapacity")
    MaxCapacity = field("MaxCapacity")
    TargetTrackingConfigurations = field("TargetTrackingConfigurations")

    @cached_property
    def PredefinedLoadMetricSpecification(self):  # pragma: no cover
        return PredefinedLoadMetricSpecification.make_one(
            self.boto3_raw_data["PredefinedLoadMetricSpecification"]
        )

    CustomizedLoadMetricSpecification = field("CustomizedLoadMetricSpecification")
    ScheduledActionBufferTime = field("ScheduledActionBufferTime")
    PredictiveScalingMaxCapacityBehavior = field("PredictiveScalingMaxCapacityBehavior")
    PredictiveScalingMaxCapacityBuffer = field("PredictiveScalingMaxCapacityBuffer")
    PredictiveScalingMode = field("PredictiveScalingMode")
    ScalingPolicyUpdateBehavior = field("ScalingPolicyUpdateBehavior")
    DisableDynamicScaling = field("DisableDynamicScaling")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScalingInstructionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalingInstructionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateScalingPlanRequest:
    boto3_raw_data: "type_defs.CreateScalingPlanRequestTypeDef" = dataclasses.field()

    ScalingPlanName = field("ScalingPlanName")
    ApplicationSource = field("ApplicationSource")
    ScalingInstructions = field("ScalingInstructions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateScalingPlanRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateScalingPlanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateScalingPlanRequest:
    boto3_raw_data: "type_defs.UpdateScalingPlanRequestTypeDef" = dataclasses.field()

    ScalingPlanName = field("ScalingPlanName")
    ScalingPlanVersion = field("ScalingPlanVersion")
    ApplicationSource = field("ApplicationSource")
    ScalingInstructions = field("ScalingInstructions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateScalingPlanRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateScalingPlanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
