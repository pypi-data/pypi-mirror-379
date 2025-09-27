# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_compute_optimizer import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccountEnrollmentStatus:
    boto3_raw_data: "type_defs.AccountEnrollmentStatusTypeDef" = dataclasses.field()

    accountId = field("accountId")
    status = field("status")
    statusReason = field("statusReason")
    lastUpdatedTimestamp = field("lastUpdatedTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountEnrollmentStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountEnrollmentStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingGroupConfiguration:
    boto3_raw_data: "type_defs.AutoScalingGroupConfigurationTypeDef" = (
        dataclasses.field()
    )

    desiredCapacity = field("desiredCapacity")
    minSize = field("minSize")
    maxSize = field("maxSize")
    instanceType = field("instanceType")
    allocationStrategy = field("allocationStrategy")
    estimatedInstanceHourReductionPercentage = field(
        "estimatedInstanceHourReductionPercentage"
    )
    type = field("type")
    mixedInstanceTypes = field("mixedInstanceTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutoScalingGroupConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingGroupConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingGroupEstimatedMonthlySavings:
    boto3_raw_data: "type_defs.AutoScalingGroupEstimatedMonthlySavingsTypeDef" = (
        dataclasses.field()
    )

    currency = field("currency")
    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutoScalingGroupEstimatedMonthlySavingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingGroupEstimatedMonthlySavingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UtilizationMetric:
    boto3_raw_data: "type_defs.UtilizationMetricTypeDef" = dataclasses.field()

    name = field("name")
    statistic = field("statistic")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UtilizationMetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UtilizationMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemorySizeConfiguration:
    boto3_raw_data: "type_defs.MemorySizeConfigurationTypeDef" = dataclasses.field()

    memory = field("memory")
    memoryReservation = field("memoryReservation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MemorySizeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemorySizeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CurrentPerformanceRiskRatings:
    boto3_raw_data: "type_defs.CurrentPerformanceRiskRatingsTypeDef" = (
        dataclasses.field()
    )

    high = field("high")
    medium = field("medium")
    low = field("low")
    veryLow = field("veryLow")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CurrentPerformanceRiskRatingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CurrentPerformanceRiskRatingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomizableMetricParameters:
    boto3_raw_data: "type_defs.CustomizableMetricParametersTypeDef" = (
        dataclasses.field()
    )

    threshold = field("threshold")
    headroom = field("headroom")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomizableMetricParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomizableMetricParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBStorageConfiguration:
    boto3_raw_data: "type_defs.DBStorageConfigurationTypeDef" = dataclasses.field()

    storageType = field("storageType")
    allocatedStorage = field("allocatedStorage")
    iops = field("iops")
    maxAllocatedStorage = field("maxAllocatedStorage")
    storageThroughput = field("storageThroughput")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBStorageConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBStorageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scope:
    boto3_raw_data: "type_defs.ScopeTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScopeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScopeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobFilter:
    boto3_raw_data: "type_defs.JobFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobFilterTypeDef"]]
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
class EBSSavingsEstimationMode:
    boto3_raw_data: "type_defs.EBSSavingsEstimationModeTypeDef" = dataclasses.field()

    source = field("source")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EBSSavingsEstimationModeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EBSSavingsEstimationModeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EBSEstimatedMonthlySavings:
    boto3_raw_data: "type_defs.EBSEstimatedMonthlySavingsTypeDef" = dataclasses.field()

    currency = field("currency")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EBSEstimatedMonthlySavingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EBSEstimatedMonthlySavingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EBSFilter:
    boto3_raw_data: "type_defs.EBSFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EBSFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EBSFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EBSUtilizationMetric:
    boto3_raw_data: "type_defs.EBSUtilizationMetricTypeDef" = dataclasses.field()

    name = field("name")
    statistic = field("statistic")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EBSUtilizationMetricTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EBSUtilizationMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ECSSavingsEstimationMode:
    boto3_raw_data: "type_defs.ECSSavingsEstimationModeTypeDef" = dataclasses.field()

    source = field("source")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ECSSavingsEstimationModeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ECSSavingsEstimationModeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ECSEstimatedMonthlySavings:
    boto3_raw_data: "type_defs.ECSEstimatedMonthlySavingsTypeDef" = dataclasses.field()

    currency = field("currency")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ECSEstimatedMonthlySavingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ECSEstimatedMonthlySavingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ECSServiceProjectedMetric:
    boto3_raw_data: "type_defs.ECSServiceProjectedMetricTypeDef" = dataclasses.field()

    name = field("name")
    timestamps = field("timestamps")
    upperBoundValues = field("upperBoundValues")
    lowerBoundValues = field("lowerBoundValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ECSServiceProjectedMetricTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ECSServiceProjectedMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ECSServiceProjectedUtilizationMetric:
    boto3_raw_data: "type_defs.ECSServiceProjectedUtilizationMetricTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    statistic = field("statistic")
    lowerBoundValue = field("lowerBoundValue")
    upperBoundValue = field("upperBoundValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ECSServiceProjectedUtilizationMetricTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ECSServiceProjectedUtilizationMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ECSServiceRecommendationFilter:
    boto3_raw_data: "type_defs.ECSServiceRecommendationFilterTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ECSServiceRecommendationFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ECSServiceRecommendationFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ECSServiceUtilizationMetric:
    boto3_raw_data: "type_defs.ECSServiceUtilizationMetricTypeDef" = dataclasses.field()

    name = field("name")
    statistic = field("statistic")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ECSServiceUtilizationMetricTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ECSServiceUtilizationMetricTypeDef"]
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

    key = field("key")
    value = field("value")

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
class EffectivePreferredResource:
    boto3_raw_data: "type_defs.EffectivePreferredResourceTypeDef" = dataclasses.field()

    name = field("name")
    includeList = field("includeList")
    effectiveIncludeList = field("effectiveIncludeList")
    excludeList = field("excludeList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EffectivePreferredResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EffectivePreferredResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalMetricsPreference:
    boto3_raw_data: "type_defs.ExternalMetricsPreferenceTypeDef" = dataclasses.field()

    source = field("source")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExternalMetricsPreferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExternalMetricsPreferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceSavingsEstimationMode:
    boto3_raw_data: "type_defs.InstanceSavingsEstimationModeTypeDef" = (
        dataclasses.field()
    )

    source = field("source")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InstanceSavingsEstimationModeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceSavingsEstimationModeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnrollmentFilter:
    boto3_raw_data: "type_defs.EnrollmentFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnrollmentFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnrollmentFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EstimatedMonthlySavings:
    boto3_raw_data: "type_defs.EstimatedMonthlySavingsTypeDef" = dataclasses.field()

    currency = field("currency")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EstimatedMonthlySavingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EstimatedMonthlySavingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filter:
    boto3_raw_data: "type_defs.FilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationPreferences:
    boto3_raw_data: "type_defs.RecommendationPreferencesTypeDef" = dataclasses.field()

    cpuVendorArchitectures = field("cpuVendorArchitectures")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendationPreferencesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationPreferencesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DestinationConfig:
    boto3_raw_data: "type_defs.S3DestinationConfigTypeDef" = dataclasses.field()

    bucket = field("bucket")
    keyPrefix = field("keyPrefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3DestinationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DestinationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Destination:
    boto3_raw_data: "type_defs.S3DestinationTypeDef" = dataclasses.field()

    bucket = field("bucket")
    key = field("key")
    metadataKey = field("metadataKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3DestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3DestinationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdleRecommendationFilter:
    boto3_raw_data: "type_defs.IdleRecommendationFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdleRecommendationFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdleRecommendationFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionRecommendationFilter:
    boto3_raw_data: "type_defs.LambdaFunctionRecommendationFilterTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LambdaFunctionRecommendationFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionRecommendationFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LicenseRecommendationFilter:
    boto3_raw_data: "type_defs.LicenseRecommendationFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LicenseRecommendationFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LicenseRecommendationFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RDSDBRecommendationFilter:
    boto3_raw_data: "type_defs.RDSDBRecommendationFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RDSDBRecommendationFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RDSDBRecommendationFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalMetricStatus:
    boto3_raw_data: "type_defs.ExternalMetricStatusTypeDef" = dataclasses.field()

    statusCode = field("statusCode")
    statusReason = field("statusReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExternalMetricStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExternalMetricStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecommendationError:
    boto3_raw_data: "type_defs.GetRecommendationErrorTypeDef" = dataclasses.field()

    identifier = field("identifier")
    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRecommendationErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommendationErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEffectiveRecommendationPreferencesRequest:
    boto3_raw_data: "type_defs.GetEffectiveRecommendationPreferencesRequestTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEffectiveRecommendationPreferencesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEffectiveRecommendationPreferencesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrderBy:
    boto3_raw_data: "type_defs.OrderByTypeDef" = dataclasses.field()

    dimension = field("dimension")
    order = field("order")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OrderByTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OrderByTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdleRecommendationError:
    boto3_raw_data: "type_defs.IdleRecommendationErrorTypeDef" = dataclasses.field()

    identifier = field("identifier")
    code = field("code")
    message = field("message")
    resourceType = field("resourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdleRecommendationErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdleRecommendationErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecommendationSummariesRequest:
    boto3_raw_data: "type_defs.GetRecommendationSummariesRequestTypeDef" = (
        dataclasses.field()
    )

    accountIds = field("accountIds")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRecommendationSummariesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommendationSummariesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Gpu:
    boto3_raw_data: "type_defs.GpuTypeDef" = dataclasses.field()

    gpuCount = field("gpuCount")
    gpuMemorySizeInMiB = field("gpuMemorySizeInMiB")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GpuTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GpuTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdleEstimatedMonthlySavings:
    boto3_raw_data: "type_defs.IdleEstimatedMonthlySavingsTypeDef" = dataclasses.field()

    currency = field("currency")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdleEstimatedMonthlySavingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdleEstimatedMonthlySavingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdleUtilizationMetric:
    boto3_raw_data: "type_defs.IdleUtilizationMetricTypeDef" = dataclasses.field()

    name = field("name")
    statistic = field("statistic")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdleUtilizationMetricTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdleUtilizationMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdleSummary:
    boto3_raw_data: "type_defs.IdleSummaryTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IdleSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IdleSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceEstimatedMonthlySavings:
    boto3_raw_data: "type_defs.InstanceEstimatedMonthlySavingsTypeDef" = (
        dataclasses.field()
    )

    currency = field("currency")
    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InstanceEstimatedMonthlySavingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceEstimatedMonthlySavingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationSource:
    boto3_raw_data: "type_defs.RecommendationSourceTypeDef" = dataclasses.field()

    recommendationSourceArn = field("recommendationSourceArn")
    recommendationSourceType = field("recommendationSourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendationSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaSavingsEstimationMode:
    boto3_raw_data: "type_defs.LambdaSavingsEstimationModeTypeDef" = dataclasses.field()

    source = field("source")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaSavingsEstimationModeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaSavingsEstimationModeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaEstimatedMonthlySavings:
    boto3_raw_data: "type_defs.LambdaEstimatedMonthlySavingsTypeDef" = (
        dataclasses.field()
    )

    currency = field("currency")
    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LambdaEstimatedMonthlySavingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaEstimatedMonthlySavingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionMemoryProjectedMetric:
    boto3_raw_data: "type_defs.LambdaFunctionMemoryProjectedMetricTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    statistic = field("statistic")
    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LambdaFunctionMemoryProjectedMetricTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionMemoryProjectedMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionUtilizationMetric:
    boto3_raw_data: "type_defs.LambdaFunctionUtilizationMetricTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    statistic = field("statistic")
    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LambdaFunctionUtilizationMetricTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionUtilizationMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricSource:
    boto3_raw_data: "type_defs.MetricSourceTypeDef" = dataclasses.field()

    provider = field("provider")
    providerArn = field("providerArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PreferredResource:
    boto3_raw_data: "type_defs.PreferredResourceTypeDef" = dataclasses.field()

    name = field("name")
    includeList = field("includeList")
    excludeList = field("excludeList")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PreferredResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PreferredResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectedMetric:
    boto3_raw_data: "type_defs.ProjectedMetricTypeDef" = dataclasses.field()

    name = field("name")
    timestamps = field("timestamps")
    values = field("values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProjectedMetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProjectedMetricTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RDSDBUtilizationMetric:
    boto3_raw_data: "type_defs.RDSDBUtilizationMetricTypeDef" = dataclasses.field()

    name = field("name")
    statistic = field("statistic")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RDSDBUtilizationMetricTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RDSDBUtilizationMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RDSDatabaseProjectedMetric:
    boto3_raw_data: "type_defs.RDSDatabaseProjectedMetricTypeDef" = dataclasses.field()

    name = field("name")
    timestamps = field("timestamps")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RDSDatabaseProjectedMetricTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RDSDatabaseProjectedMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RDSSavingsEstimationMode:
    boto3_raw_data: "type_defs.RDSSavingsEstimationModeTypeDef" = dataclasses.field()

    source = field("source")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RDSSavingsEstimationModeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RDSSavingsEstimationModeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RDSInstanceEstimatedMonthlySavings:
    boto3_raw_data: "type_defs.RDSInstanceEstimatedMonthlySavingsTypeDef" = (
        dataclasses.field()
    )

    currency = field("currency")
    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RDSInstanceEstimatedMonthlySavingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RDSInstanceEstimatedMonthlySavingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RDSStorageEstimatedMonthlySavings:
    boto3_raw_data: "type_defs.RDSStorageEstimatedMonthlySavingsTypeDef" = (
        dataclasses.field()
    )

    currency = field("currency")
    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RDSStorageEstimatedMonthlySavingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RDSStorageEstimatedMonthlySavingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReasonCodeSummary:
    boto3_raw_data: "type_defs.ReasonCodeSummaryTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReasonCodeSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReasonCodeSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnrollmentStatusRequest:
    boto3_raw_data: "type_defs.UpdateEnrollmentStatusRequestTypeDef" = (
        dataclasses.field()
    )

    status = field("status")
    includeMemberAccounts = field("includeMemberAccounts")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateEnrollmentStatusRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnrollmentStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VolumeConfiguration:
    boto3_raw_data: "type_defs.VolumeConfigurationTypeDef" = dataclasses.field()

    volumeType = field("volumeType")
    volumeSize = field("volumeSize")
    volumeBaselineIOPS = field("volumeBaselineIOPS")
    volumeBurstIOPS = field("volumeBurstIOPS")
    volumeBaselineThroughput = field("volumeBaselineThroughput")
    volumeBurstThroughput = field("volumeBurstThroughput")
    rootVolume = field("rootVolume")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VolumeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VolumeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingGroupSavingsOpportunityAfterDiscounts:
    boto3_raw_data: (
        "type_defs.AutoScalingGroupSavingsOpportunityAfterDiscountsTypeDef"
    ) = dataclasses.field()

    savingsOpportunityPercentage = field("savingsOpportunityPercentage")

    @cached_property
    def estimatedMonthlySavings(self):  # pragma: no cover
        return AutoScalingGroupEstimatedMonthlySavings.make_one(
            self.boto3_raw_data["estimatedMonthlySavings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutoScalingGroupSavingsOpportunityAfterDiscountsTypeDef"
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
                "type_defs.AutoScalingGroupSavingsOpportunityAfterDiscountsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerConfiguration:
    boto3_raw_data: "type_defs.ContainerConfigurationTypeDef" = dataclasses.field()

    containerName = field("containerName")

    @cached_property
    def memorySizeConfiguration(self):  # pragma: no cover
        return MemorySizeConfiguration.make_one(
            self.boto3_raw_data["memorySizeConfiguration"]
        )

    cpu = field("cpu")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerRecommendation:
    boto3_raw_data: "type_defs.ContainerRecommendationTypeDef" = dataclasses.field()

    containerName = field("containerName")

    @cached_property
    def memorySizeConfiguration(self):  # pragma: no cover
        return MemorySizeConfiguration.make_one(
            self.boto3_raw_data["memorySizeConfiguration"]
        )

    cpu = field("cpu")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerRecommendationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UtilizationPreference:
    boto3_raw_data: "type_defs.UtilizationPreferenceTypeDef" = dataclasses.field()

    metricName = field("metricName")

    @cached_property
    def metricParameters(self):  # pragma: no cover
        return CustomizableMetricParameters.make_one(
            self.boto3_raw_data["metricParameters"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UtilizationPreferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UtilizationPreferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRecommendationPreferencesRequest:
    boto3_raw_data: "type_defs.DeleteRecommendationPreferencesRequestTypeDef" = (
        dataclasses.field()
    )

    resourceType = field("resourceType")
    recommendationPreferenceNames = field("recommendationPreferenceNames")

    @cached_property
    def scope(self):  # pragma: no cover
        return Scope.make_one(self.boto3_raw_data["scope"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRecommendationPreferencesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRecommendationPreferencesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecommendationPreferencesRequest:
    boto3_raw_data: "type_defs.GetRecommendationPreferencesRequestTypeDef" = (
        dataclasses.field()
    )

    resourceType = field("resourceType")

    @cached_property
    def scope(self):  # pragma: no cover
        return Scope.make_one(self.boto3_raw_data["scope"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRecommendationPreferencesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommendationPreferencesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecommendationExportJobsRequest:
    boto3_raw_data: "type_defs.DescribeRecommendationExportJobsRequestTypeDef" = (
        dataclasses.field()
    )

    jobIds = field("jobIds")

    @cached_property
    def filters(self):  # pragma: no cover
        return JobFilter.make_many(self.boto3_raw_data["filters"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRecommendationExportJobsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecommendationExportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecommendationExportJobsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeRecommendationExportJobsRequestPaginateTypeDef"
    ) = dataclasses.field()

    jobIds = field("jobIds")

    @cached_property
    def filters(self):  # pragma: no cover
        return JobFilter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRecommendationExportJobsRequestPaginateTypeDef"
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
                "type_defs.DescribeRecommendationExportJobsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecommendationPreferencesRequestPaginate:
    boto3_raw_data: "type_defs.GetRecommendationPreferencesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    resourceType = field("resourceType")

    @cached_property
    def scope(self):  # pragma: no cover
        return Scope.make_one(self.boto3_raw_data["scope"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRecommendationPreferencesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommendationPreferencesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecommendationSummariesRequestPaginate:
    boto3_raw_data: "type_defs.GetRecommendationSummariesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    accountIds = field("accountIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRecommendationSummariesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommendationSummariesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnrollmentStatusResponse:
    boto3_raw_data: "type_defs.GetEnrollmentStatusResponseTypeDef" = dataclasses.field()

    status = field("status")
    statusReason = field("statusReason")
    memberAccountsEnrolled = field("memberAccountsEnrolled")
    lastUpdatedTimestamp = field("lastUpdatedTimestamp")
    numberOfMemberAccountsOptedIn = field("numberOfMemberAccountsOptedIn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnrollmentStatusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnrollmentStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnrollmentStatusesForOrganizationResponse:
    boto3_raw_data: "type_defs.GetEnrollmentStatusesForOrganizationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def accountEnrollmentStatuses(self):  # pragma: no cover
        return AccountEnrollmentStatus.make_many(
            self.boto3_raw_data["accountEnrollmentStatuses"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEnrollmentStatusesForOrganizationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnrollmentStatusesForOrganizationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnrollmentStatusResponse:
    boto3_raw_data: "type_defs.UpdateEnrollmentStatusResponseTypeDef" = (
        dataclasses.field()
    )

    status = field("status")
    statusReason = field("statusReason")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateEnrollmentStatusResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnrollmentStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EBSEffectiveRecommendationPreferences:
    boto3_raw_data: "type_defs.EBSEffectiveRecommendationPreferencesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def savingsEstimationMode(self):  # pragma: no cover
        return EBSSavingsEstimationMode.make_one(
            self.boto3_raw_data["savingsEstimationMode"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EBSEffectiveRecommendationPreferencesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EBSEffectiveRecommendationPreferencesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EBSSavingsOpportunityAfterDiscounts:
    boto3_raw_data: "type_defs.EBSSavingsOpportunityAfterDiscountsTypeDef" = (
        dataclasses.field()
    )

    savingsOpportunityPercentage = field("savingsOpportunityPercentage")

    @cached_property
    def estimatedMonthlySavings(self):  # pragma: no cover
        return EBSEstimatedMonthlySavings.make_one(
            self.boto3_raw_data["estimatedMonthlySavings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EBSSavingsOpportunityAfterDiscountsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EBSSavingsOpportunityAfterDiscountsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEBSVolumeRecommendationsRequest:
    boto3_raw_data: "type_defs.GetEBSVolumeRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    volumeArns = field("volumeArns")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filters(self):  # pragma: no cover
        return EBSFilter.make_many(self.boto3_raw_data["filters"])

    accountIds = field("accountIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEBSVolumeRecommendationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEBSVolumeRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ECSEffectiveRecommendationPreferences:
    boto3_raw_data: "type_defs.ECSEffectiveRecommendationPreferencesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def savingsEstimationMode(self):  # pragma: no cover
        return ECSSavingsEstimationMode.make_one(
            self.boto3_raw_data["savingsEstimationMode"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ECSEffectiveRecommendationPreferencesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ECSEffectiveRecommendationPreferencesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ECSSavingsOpportunityAfterDiscounts:
    boto3_raw_data: "type_defs.ECSSavingsOpportunityAfterDiscountsTypeDef" = (
        dataclasses.field()
    )

    savingsOpportunityPercentage = field("savingsOpportunityPercentage")

    @cached_property
    def estimatedMonthlySavings(self):  # pragma: no cover
        return ECSEstimatedMonthlySavings.make_one(
            self.boto3_raw_data["estimatedMonthlySavings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ECSSavingsOpportunityAfterDiscountsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ECSSavingsOpportunityAfterDiscountsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ECSServiceRecommendedOptionProjectedMetric:
    boto3_raw_data: "type_defs.ECSServiceRecommendedOptionProjectedMetricTypeDef" = (
        dataclasses.field()
    )

    recommendedCpuUnits = field("recommendedCpuUnits")
    recommendedMemorySize = field("recommendedMemorySize")

    @cached_property
    def projectedMetrics(self):  # pragma: no cover
        return ECSServiceProjectedMetric.make_many(
            self.boto3_raw_data["projectedMetrics"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ECSServiceRecommendedOptionProjectedMetricTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ECSServiceRecommendedOptionProjectedMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetECSServiceRecommendationsRequest:
    boto3_raw_data: "type_defs.GetECSServiceRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    serviceArns = field("serviceArns")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filters(self):  # pragma: no cover
        return ECSServiceRecommendationFilter.make_many(self.boto3_raw_data["filters"])

    accountIds = field("accountIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetECSServiceRecommendationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetECSServiceRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnrollmentStatusesForOrganizationRequestPaginate:
    boto3_raw_data: (
        "type_defs.GetEnrollmentStatusesForOrganizationRequestPaginateTypeDef"
    ) = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return EnrollmentFilter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEnrollmentStatusesForOrganizationRequestPaginateTypeDef"
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
                "type_defs.GetEnrollmentStatusesForOrganizationRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnrollmentStatusesForOrganizationRequest:
    boto3_raw_data: "type_defs.GetEnrollmentStatusesForOrganizationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return EnrollmentFilter.make_many(self.boto3_raw_data["filters"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEnrollmentStatusesForOrganizationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnrollmentStatusesForOrganizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferredWorkloadSaving:
    boto3_raw_data: "type_defs.InferredWorkloadSavingTypeDef" = dataclasses.field()

    inferredWorkloadTypes = field("inferredWorkloadTypes")

    @cached_property
    def estimatedMonthlySavings(self):  # pragma: no cover
        return EstimatedMonthlySavings.make_one(
            self.boto3_raw_data["estimatedMonthlySavings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferredWorkloadSavingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferredWorkloadSavingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsOpportunity:
    boto3_raw_data: "type_defs.SavingsOpportunityTypeDef" = dataclasses.field()

    savingsOpportunityPercentage = field("savingsOpportunityPercentage")

    @cached_property
    def estimatedMonthlySavings(self):  # pragma: no cover
        return EstimatedMonthlySavings.make_one(
            self.boto3_raw_data["estimatedMonthlySavings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SavingsOpportunityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsOpportunityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutoScalingGroupRecommendationsRequest:
    boto3_raw_data: "type_defs.GetAutoScalingGroupRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    accountIds = field("accountIds")
    autoScalingGroupArns = field("autoScalingGroupArns")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def recommendationPreferences(self):  # pragma: no cover
        return RecommendationPreferences.make_one(
            self.boto3_raw_data["recommendationPreferences"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAutoScalingGroupRecommendationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAutoScalingGroupRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEC2InstanceRecommendationsRequest:
    boto3_raw_data: "type_defs.GetEC2InstanceRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    instanceArns = field("instanceArns")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    accountIds = field("accountIds")

    @cached_property
    def recommendationPreferences(self):  # pragma: no cover
        return RecommendationPreferences.make_one(
            self.boto3_raw_data["recommendationPreferences"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEC2InstanceRecommendationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEC2InstanceRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportAutoScalingGroupRecommendationsRequest:
    boto3_raw_data: "type_defs.ExportAutoScalingGroupRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3DestinationConfig(self):  # pragma: no cover
        return S3DestinationConfig.make_one(self.boto3_raw_data["s3DestinationConfig"])

    accountIds = field("accountIds")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    fieldsToExport = field("fieldsToExport")
    fileFormat = field("fileFormat")
    includeMemberAccounts = field("includeMemberAccounts")

    @cached_property
    def recommendationPreferences(self):  # pragma: no cover
        return RecommendationPreferences.make_one(
            self.boto3_raw_data["recommendationPreferences"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportAutoScalingGroupRecommendationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportAutoScalingGroupRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportEBSVolumeRecommendationsRequest:
    boto3_raw_data: "type_defs.ExportEBSVolumeRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3DestinationConfig(self):  # pragma: no cover
        return S3DestinationConfig.make_one(self.boto3_raw_data["s3DestinationConfig"])

    accountIds = field("accountIds")

    @cached_property
    def filters(self):  # pragma: no cover
        return EBSFilter.make_many(self.boto3_raw_data["filters"])

    fieldsToExport = field("fieldsToExport")
    fileFormat = field("fileFormat")
    includeMemberAccounts = field("includeMemberAccounts")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportEBSVolumeRecommendationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportEBSVolumeRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportEC2InstanceRecommendationsRequest:
    boto3_raw_data: "type_defs.ExportEC2InstanceRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3DestinationConfig(self):  # pragma: no cover
        return S3DestinationConfig.make_one(self.boto3_raw_data["s3DestinationConfig"])

    accountIds = field("accountIds")

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    fieldsToExport = field("fieldsToExport")
    fileFormat = field("fileFormat")
    includeMemberAccounts = field("includeMemberAccounts")

    @cached_property
    def recommendationPreferences(self):  # pragma: no cover
        return RecommendationPreferences.make_one(
            self.boto3_raw_data["recommendationPreferences"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportEC2InstanceRecommendationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportEC2InstanceRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportECSServiceRecommendationsRequest:
    boto3_raw_data: "type_defs.ExportECSServiceRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3DestinationConfig(self):  # pragma: no cover
        return S3DestinationConfig.make_one(self.boto3_raw_data["s3DestinationConfig"])

    accountIds = field("accountIds")

    @cached_property
    def filters(self):  # pragma: no cover
        return ECSServiceRecommendationFilter.make_many(self.boto3_raw_data["filters"])

    fieldsToExport = field("fieldsToExport")
    fileFormat = field("fileFormat")
    includeMemberAccounts = field("includeMemberAccounts")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportECSServiceRecommendationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportECSServiceRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportAutoScalingGroupRecommendationsResponse:
    boto3_raw_data: "type_defs.ExportAutoScalingGroupRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")

    @cached_property
    def s3Destination(self):  # pragma: no cover
        return S3Destination.make_one(self.boto3_raw_data["s3Destination"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportAutoScalingGroupRecommendationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportAutoScalingGroupRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportDestination:
    boto3_raw_data: "type_defs.ExportDestinationTypeDef" = dataclasses.field()

    @cached_property
    def s3(self):  # pragma: no cover
        return S3Destination.make_one(self.boto3_raw_data["s3"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportDestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportEBSVolumeRecommendationsResponse:
    boto3_raw_data: "type_defs.ExportEBSVolumeRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")

    @cached_property
    def s3Destination(self):  # pragma: no cover
        return S3Destination.make_one(self.boto3_raw_data["s3Destination"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportEBSVolumeRecommendationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportEBSVolumeRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportEC2InstanceRecommendationsResponse:
    boto3_raw_data: "type_defs.ExportEC2InstanceRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")

    @cached_property
    def s3Destination(self):  # pragma: no cover
        return S3Destination.make_one(self.boto3_raw_data["s3Destination"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportEC2InstanceRecommendationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportEC2InstanceRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportECSServiceRecommendationsResponse:
    boto3_raw_data: "type_defs.ExportECSServiceRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")

    @cached_property
    def s3Destination(self):  # pragma: no cover
        return S3Destination.make_one(self.boto3_raw_data["s3Destination"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportECSServiceRecommendationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportECSServiceRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportIdleRecommendationsResponse:
    boto3_raw_data: "type_defs.ExportIdleRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")

    @cached_property
    def s3Destination(self):  # pragma: no cover
        return S3Destination.make_one(self.boto3_raw_data["s3Destination"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportIdleRecommendationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportIdleRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportLambdaFunctionRecommendationsResponse:
    boto3_raw_data: "type_defs.ExportLambdaFunctionRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")

    @cached_property
    def s3Destination(self):  # pragma: no cover
        return S3Destination.make_one(self.boto3_raw_data["s3Destination"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportLambdaFunctionRecommendationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportLambdaFunctionRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportLicenseRecommendationsResponse:
    boto3_raw_data: "type_defs.ExportLicenseRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")

    @cached_property
    def s3Destination(self):  # pragma: no cover
        return S3Destination.make_one(self.boto3_raw_data["s3Destination"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportLicenseRecommendationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportLicenseRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportRDSDatabaseRecommendationsResponse:
    boto3_raw_data: "type_defs.ExportRDSDatabaseRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")

    @cached_property
    def s3Destination(self):  # pragma: no cover
        return S3Destination.make_one(self.boto3_raw_data["s3Destination"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportRDSDatabaseRecommendationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportRDSDatabaseRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportIdleRecommendationsRequest:
    boto3_raw_data: "type_defs.ExportIdleRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3DestinationConfig(self):  # pragma: no cover
        return S3DestinationConfig.make_one(self.boto3_raw_data["s3DestinationConfig"])

    accountIds = field("accountIds")

    @cached_property
    def filters(self):  # pragma: no cover
        return IdleRecommendationFilter.make_many(self.boto3_raw_data["filters"])

    fieldsToExport = field("fieldsToExport")
    fileFormat = field("fileFormat")
    includeMemberAccounts = field("includeMemberAccounts")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExportIdleRecommendationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportIdleRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportLambdaFunctionRecommendationsRequest:
    boto3_raw_data: "type_defs.ExportLambdaFunctionRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3DestinationConfig(self):  # pragma: no cover
        return S3DestinationConfig.make_one(self.boto3_raw_data["s3DestinationConfig"])

    accountIds = field("accountIds")

    @cached_property
    def filters(self):  # pragma: no cover
        return LambdaFunctionRecommendationFilter.make_many(
            self.boto3_raw_data["filters"]
        )

    fieldsToExport = field("fieldsToExport")
    fileFormat = field("fileFormat")
    includeMemberAccounts = field("includeMemberAccounts")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportLambdaFunctionRecommendationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportLambdaFunctionRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLambdaFunctionRecommendationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.GetLambdaFunctionRecommendationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    functionArns = field("functionArns")
    accountIds = field("accountIds")

    @cached_property
    def filters(self):  # pragma: no cover
        return LambdaFunctionRecommendationFilter.make_many(
            self.boto3_raw_data["filters"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetLambdaFunctionRecommendationsRequestPaginateTypeDef"
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
                "type_defs.GetLambdaFunctionRecommendationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLambdaFunctionRecommendationsRequest:
    boto3_raw_data: "type_defs.GetLambdaFunctionRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    functionArns = field("functionArns")
    accountIds = field("accountIds")

    @cached_property
    def filters(self):  # pragma: no cover
        return LambdaFunctionRecommendationFilter.make_many(
            self.boto3_raw_data["filters"]
        )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetLambdaFunctionRecommendationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLambdaFunctionRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportLicenseRecommendationsRequest:
    boto3_raw_data: "type_defs.ExportLicenseRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3DestinationConfig(self):  # pragma: no cover
        return S3DestinationConfig.make_one(self.boto3_raw_data["s3DestinationConfig"])

    accountIds = field("accountIds")

    @cached_property
    def filters(self):  # pragma: no cover
        return LicenseRecommendationFilter.make_many(self.boto3_raw_data["filters"])

    fieldsToExport = field("fieldsToExport")
    fileFormat = field("fileFormat")
    includeMemberAccounts = field("includeMemberAccounts")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportLicenseRecommendationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportLicenseRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLicenseRecommendationsRequest:
    boto3_raw_data: "type_defs.GetLicenseRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    resourceArns = field("resourceArns")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filters(self):  # pragma: no cover
        return LicenseRecommendationFilter.make_many(self.boto3_raw_data["filters"])

    accountIds = field("accountIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLicenseRecommendationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLicenseRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportRDSDatabaseRecommendationsRequest:
    boto3_raw_data: "type_defs.ExportRDSDatabaseRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3DestinationConfig(self):  # pragma: no cover
        return S3DestinationConfig.make_one(self.boto3_raw_data["s3DestinationConfig"])

    accountIds = field("accountIds")

    @cached_property
    def filters(self):  # pragma: no cover
        return RDSDBRecommendationFilter.make_many(self.boto3_raw_data["filters"])

    fieldsToExport = field("fieldsToExport")
    fileFormat = field("fileFormat")
    includeMemberAccounts = field("includeMemberAccounts")

    @cached_property
    def recommendationPreferences(self):  # pragma: no cover
        return RecommendationPreferences.make_one(
            self.boto3_raw_data["recommendationPreferences"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportRDSDatabaseRecommendationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportRDSDatabaseRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRDSDatabaseRecommendationsRequest:
    boto3_raw_data: "type_defs.GetRDSDatabaseRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    resourceArns = field("resourceArns")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filters(self):  # pragma: no cover
        return RDSDBRecommendationFilter.make_many(self.boto3_raw_data["filters"])

    accountIds = field("accountIds")

    @cached_property
    def recommendationPreferences(self):  # pragma: no cover
        return RecommendationPreferences.make_one(
            self.boto3_raw_data["recommendationPreferences"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRDSDatabaseRecommendationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRDSDatabaseRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEC2RecommendationProjectedMetricsRequest:
    boto3_raw_data: "type_defs.GetEC2RecommendationProjectedMetricsRequestTypeDef" = (
        dataclasses.field()
    )

    instanceArn = field("instanceArn")
    stat = field("stat")
    period = field("period")
    startTime = field("startTime")
    endTime = field("endTime")

    @cached_property
    def recommendationPreferences(self):  # pragma: no cover
        return RecommendationPreferences.make_one(
            self.boto3_raw_data["recommendationPreferences"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEC2RecommendationProjectedMetricsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEC2RecommendationProjectedMetricsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetECSServiceRecommendationProjectedMetricsRequest:
    boto3_raw_data: (
        "type_defs.GetECSServiceRecommendationProjectedMetricsRequestTypeDef"
    ) = dataclasses.field()

    serviceArn = field("serviceArn")
    stat = field("stat")
    period = field("period")
    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetECSServiceRecommendationProjectedMetricsRequestTypeDef"
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
                "type_defs.GetECSServiceRecommendationProjectedMetricsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRDSDatabaseRecommendationProjectedMetricsRequest:
    boto3_raw_data: (
        "type_defs.GetRDSDatabaseRecommendationProjectedMetricsRequestTypeDef"
    ) = dataclasses.field()

    resourceArn = field("resourceArn")
    stat = field("stat")
    period = field("period")
    startTime = field("startTime")
    endTime = field("endTime")

    @cached_property
    def recommendationPreferences(self):  # pragma: no cover
        return RecommendationPreferences.make_one(
            self.boto3_raw_data["recommendationPreferences"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRDSDatabaseRecommendationProjectedMetricsRequestTypeDef"
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
                "type_defs.GetRDSDatabaseRecommendationProjectedMetricsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdleRecommendationsRequest:
    boto3_raw_data: "type_defs.GetIdleRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    resourceArns = field("resourceArns")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filters(self):  # pragma: no cover
        return IdleRecommendationFilter.make_many(self.boto3_raw_data["filters"])

    accountIds = field("accountIds")

    @cached_property
    def orderBy(self):  # pragma: no cover
        return OrderBy.make_one(self.boto3_raw_data["orderBy"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetIdleRecommendationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdleRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GpuInfo:
    boto3_raw_data: "type_defs.GpuInfoTypeDef" = dataclasses.field()

    @cached_property
    def gpus(self):  # pragma: no cover
        return Gpu.make_many(self.boto3_raw_data["gpus"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GpuInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GpuInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdleSavingsOpportunityAfterDiscounts:
    boto3_raw_data: "type_defs.IdleSavingsOpportunityAfterDiscountsTypeDef" = (
        dataclasses.field()
    )

    savingsOpportunityPercentage = field("savingsOpportunityPercentage")

    @cached_property
    def estimatedMonthlySavings(self):  # pragma: no cover
        return IdleEstimatedMonthlySavings.make_one(
            self.boto3_raw_data["estimatedMonthlySavings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IdleSavingsOpportunityAfterDiscountsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdleSavingsOpportunityAfterDiscountsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdleSavingsOpportunity:
    boto3_raw_data: "type_defs.IdleSavingsOpportunityTypeDef" = dataclasses.field()

    savingsOpportunityPercentage = field("savingsOpportunityPercentage")

    @cached_property
    def estimatedMonthlySavings(self):  # pragma: no cover
        return IdleEstimatedMonthlySavings.make_one(
            self.boto3_raw_data["estimatedMonthlySavings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdleSavingsOpportunityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdleSavingsOpportunityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceSavingsOpportunityAfterDiscounts:
    boto3_raw_data: "type_defs.InstanceSavingsOpportunityAfterDiscountsTypeDef" = (
        dataclasses.field()
    )

    savingsOpportunityPercentage = field("savingsOpportunityPercentage")

    @cached_property
    def estimatedMonthlySavings(self):  # pragma: no cover
        return InstanceEstimatedMonthlySavings.make_one(
            self.boto3_raw_data["estimatedMonthlySavings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InstanceSavingsOpportunityAfterDiscountsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceSavingsOpportunityAfterDiscountsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaEffectiveRecommendationPreferences:
    boto3_raw_data: "type_defs.LambdaEffectiveRecommendationPreferencesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def savingsEstimationMode(self):  # pragma: no cover
        return LambdaSavingsEstimationMode.make_one(
            self.boto3_raw_data["savingsEstimationMode"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LambdaEffectiveRecommendationPreferencesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaEffectiveRecommendationPreferencesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaSavingsOpportunityAfterDiscounts:
    boto3_raw_data: "type_defs.LambdaSavingsOpportunityAfterDiscountsTypeDef" = (
        dataclasses.field()
    )

    savingsOpportunityPercentage = field("savingsOpportunityPercentage")

    @cached_property
    def estimatedMonthlySavings(self):  # pragma: no cover
        return LambdaEstimatedMonthlySavings.make_one(
            self.boto3_raw_data["estimatedMonthlySavings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LambdaSavingsOpportunityAfterDiscountsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaSavingsOpportunityAfterDiscountsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LicenseConfiguration:
    boto3_raw_data: "type_defs.LicenseConfigurationTypeDef" = dataclasses.field()

    numberOfCores = field("numberOfCores")
    instanceType = field("instanceType")
    operatingSystem = field("operatingSystem")
    licenseEdition = field("licenseEdition")
    licenseName = field("licenseName")
    licenseModel = field("licenseModel")
    licenseVersion = field("licenseVersion")

    @cached_property
    def metricsSource(self):  # pragma: no cover
        return MetricSource.make_many(self.boto3_raw_data["metricsSource"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LicenseConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LicenseConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendedOptionProjectedMetric:
    boto3_raw_data: "type_defs.RecommendedOptionProjectedMetricTypeDef" = (
        dataclasses.field()
    )

    recommendedInstanceType = field("recommendedInstanceType")
    rank = field("rank")

    @cached_property
    def projectedMetrics(self):  # pragma: no cover
        return ProjectedMetric.make_many(self.boto3_raw_data["projectedMetrics"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RecommendedOptionProjectedMetricTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendedOptionProjectedMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RDSDatabaseRecommendedOptionProjectedMetric:
    boto3_raw_data: "type_defs.RDSDatabaseRecommendedOptionProjectedMetricTypeDef" = (
        dataclasses.field()
    )

    recommendedDBInstanceClass = field("recommendedDBInstanceClass")
    rank = field("rank")

    @cached_property
    def projectedMetrics(self):  # pragma: no cover
        return RDSDatabaseProjectedMetric.make_many(
            self.boto3_raw_data["projectedMetrics"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RDSDatabaseRecommendedOptionProjectedMetricTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RDSDatabaseRecommendedOptionProjectedMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RDSEffectiveRecommendationPreferences:
    boto3_raw_data: "type_defs.RDSEffectiveRecommendationPreferencesTypeDef" = (
        dataclasses.field()
    )

    cpuVendorArchitectures = field("cpuVendorArchitectures")
    enhancedInfrastructureMetrics = field("enhancedInfrastructureMetrics")
    lookBackPeriod = field("lookBackPeriod")

    @cached_property
    def savingsEstimationMode(self):  # pragma: no cover
        return RDSSavingsEstimationMode.make_one(
            self.boto3_raw_data["savingsEstimationMode"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RDSEffectiveRecommendationPreferencesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RDSEffectiveRecommendationPreferencesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RDSInstanceSavingsOpportunityAfterDiscounts:
    boto3_raw_data: "type_defs.RDSInstanceSavingsOpportunityAfterDiscountsTypeDef" = (
        dataclasses.field()
    )

    savingsOpportunityPercentage = field("savingsOpportunityPercentage")

    @cached_property
    def estimatedMonthlySavings(self):  # pragma: no cover
        return RDSInstanceEstimatedMonthlySavings.make_one(
            self.boto3_raw_data["estimatedMonthlySavings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RDSInstanceSavingsOpportunityAfterDiscountsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RDSInstanceSavingsOpportunityAfterDiscountsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RDSStorageSavingsOpportunityAfterDiscounts:
    boto3_raw_data: "type_defs.RDSStorageSavingsOpportunityAfterDiscountsTypeDef" = (
        dataclasses.field()
    )

    savingsOpportunityPercentage = field("savingsOpportunityPercentage")

    @cached_property
    def estimatedMonthlySavings(self):  # pragma: no cover
        return RDSStorageEstimatedMonthlySavings.make_one(
            self.boto3_raw_data["estimatedMonthlySavings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RDSStorageSavingsOpportunityAfterDiscountsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RDSStorageSavingsOpportunityAfterDiscountsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Summary:
    boto3_raw_data: "type_defs.SummaryTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @cached_property
    def reasonCodeSummaries(self):  # pragma: no cover
        return ReasonCodeSummary.make_many(self.boto3_raw_data["reasonCodeSummaries"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceConfiguration:
    boto3_raw_data: "type_defs.ServiceConfigurationTypeDef" = dataclasses.field()

    memory = field("memory")
    cpu = field("cpu")

    @cached_property
    def containerConfigurations(self):  # pragma: no cover
        return ContainerConfiguration.make_many(
            self.boto3_raw_data["containerConfigurations"]
        )

    autoScalingConfiguration = field("autoScalingConfiguration")
    taskDefinitionArn = field("taskDefinitionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EffectiveRecommendationPreferences:
    boto3_raw_data: "type_defs.EffectiveRecommendationPreferencesTypeDef" = (
        dataclasses.field()
    )

    cpuVendorArchitectures = field("cpuVendorArchitectures")
    enhancedInfrastructureMetrics = field("enhancedInfrastructureMetrics")
    inferredWorkloadTypes = field("inferredWorkloadTypes")

    @cached_property
    def externalMetricsPreference(self):  # pragma: no cover
        return ExternalMetricsPreference.make_one(
            self.boto3_raw_data["externalMetricsPreference"]
        )

    lookBackPeriod = field("lookBackPeriod")

    @cached_property
    def utilizationPreferences(self):  # pragma: no cover
        return UtilizationPreference.make_many(
            self.boto3_raw_data["utilizationPreferences"]
        )

    @cached_property
    def preferredResources(self):  # pragma: no cover
        return EffectivePreferredResource.make_many(
            self.boto3_raw_data["preferredResources"]
        )

    @cached_property
    def savingsEstimationMode(self):  # pragma: no cover
        return InstanceSavingsEstimationMode.make_one(
            self.boto3_raw_data["savingsEstimationMode"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EffectiveRecommendationPreferencesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EffectiveRecommendationPreferencesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEffectiveRecommendationPreferencesResponse:
    boto3_raw_data: "type_defs.GetEffectiveRecommendationPreferencesResponseTypeDef" = (
        dataclasses.field()
    )

    enhancedInfrastructureMetrics = field("enhancedInfrastructureMetrics")

    @cached_property
    def externalMetricsPreference(self):  # pragma: no cover
        return ExternalMetricsPreference.make_one(
            self.boto3_raw_data["externalMetricsPreference"]
        )

    lookBackPeriod = field("lookBackPeriod")

    @cached_property
    def utilizationPreferences(self):  # pragma: no cover
        return UtilizationPreference.make_many(
            self.boto3_raw_data["utilizationPreferences"]
        )

    @cached_property
    def preferredResources(self):  # pragma: no cover
        return EffectivePreferredResource.make_many(
            self.boto3_raw_data["preferredResources"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEffectiveRecommendationPreferencesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEffectiveRecommendationPreferencesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRecommendationPreferencesRequest:
    boto3_raw_data: "type_defs.PutRecommendationPreferencesRequestTypeDef" = (
        dataclasses.field()
    )

    resourceType = field("resourceType")

    @cached_property
    def scope(self):  # pragma: no cover
        return Scope.make_one(self.boto3_raw_data["scope"])

    enhancedInfrastructureMetrics = field("enhancedInfrastructureMetrics")
    inferredWorkloadTypes = field("inferredWorkloadTypes")

    @cached_property
    def externalMetricsPreference(self):  # pragma: no cover
        return ExternalMetricsPreference.make_one(
            self.boto3_raw_data["externalMetricsPreference"]
        )

    lookBackPeriod = field("lookBackPeriod")

    @cached_property
    def utilizationPreferences(self):  # pragma: no cover
        return UtilizationPreference.make_many(
            self.boto3_raw_data["utilizationPreferences"]
        )

    @cached_property
    def preferredResources(self):  # pragma: no cover
        return PreferredResource.make_many(self.boto3_raw_data["preferredResources"])

    savingsEstimationMode = field("savingsEstimationMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutRecommendationPreferencesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRecommendationPreferencesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationPreferencesDetail:
    boto3_raw_data: "type_defs.RecommendationPreferencesDetailTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def scope(self):  # pragma: no cover
        return Scope.make_one(self.boto3_raw_data["scope"])

    resourceType = field("resourceType")
    enhancedInfrastructureMetrics = field("enhancedInfrastructureMetrics")
    inferredWorkloadTypes = field("inferredWorkloadTypes")

    @cached_property
    def externalMetricsPreference(self):  # pragma: no cover
        return ExternalMetricsPreference.make_one(
            self.boto3_raw_data["externalMetricsPreference"]
        )

    lookBackPeriod = field("lookBackPeriod")

    @cached_property
    def utilizationPreferences(self):  # pragma: no cover
        return UtilizationPreference.make_many(
            self.boto3_raw_data["utilizationPreferences"]
        )

    @cached_property
    def preferredResources(self):  # pragma: no cover
        return EffectivePreferredResource.make_many(
            self.boto3_raw_data["preferredResources"]
        )

    savingsEstimationMode = field("savingsEstimationMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RecommendationPreferencesDetailTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationPreferencesDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetECSServiceRecommendationProjectedMetricsResponse:
    boto3_raw_data: (
        "type_defs.GetECSServiceRecommendationProjectedMetricsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def recommendedOptionProjectedMetrics(self):  # pragma: no cover
        return ECSServiceRecommendedOptionProjectedMetric.make_many(
            self.boto3_raw_data["recommendedOptionProjectedMetrics"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetECSServiceRecommendationProjectedMetricsResponseTypeDef"
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
                "type_defs.GetECSServiceRecommendationProjectedMetricsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ECSServiceRecommendationOption:
    boto3_raw_data: "type_defs.ECSServiceRecommendationOptionTypeDef" = (
        dataclasses.field()
    )

    memory = field("memory")
    cpu = field("cpu")

    @cached_property
    def savingsOpportunity(self):  # pragma: no cover
        return SavingsOpportunity.make_one(self.boto3_raw_data["savingsOpportunity"])

    @cached_property
    def savingsOpportunityAfterDiscounts(self):  # pragma: no cover
        return ECSSavingsOpportunityAfterDiscounts.make_one(
            self.boto3_raw_data["savingsOpportunityAfterDiscounts"]
        )

    @cached_property
    def projectedUtilizationMetrics(self):  # pragma: no cover
        return ECSServiceProjectedUtilizationMetric.make_many(
            self.boto3_raw_data["projectedUtilizationMetrics"]
        )

    @cached_property
    def containerRecommendations(self):  # pragma: no cover
        return ContainerRecommendation.make_many(
            self.boto3_raw_data["containerRecommendations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ECSServiceRecommendationOptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ECSServiceRecommendationOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LicenseRecommendationOption:
    boto3_raw_data: "type_defs.LicenseRecommendationOptionTypeDef" = dataclasses.field()

    rank = field("rank")
    operatingSystem = field("operatingSystem")
    licenseEdition = field("licenseEdition")
    licenseModel = field("licenseModel")

    @cached_property
    def savingsOpportunity(self):  # pragma: no cover
        return SavingsOpportunity.make_one(self.boto3_raw_data["savingsOpportunity"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LicenseRecommendationOptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LicenseRecommendationOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VolumeRecommendationOption:
    boto3_raw_data: "type_defs.VolumeRecommendationOptionTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return VolumeConfiguration.make_one(self.boto3_raw_data["configuration"])

    performanceRisk = field("performanceRisk")
    rank = field("rank")

    @cached_property
    def savingsOpportunity(self):  # pragma: no cover
        return SavingsOpportunity.make_one(self.boto3_raw_data["savingsOpportunity"])

    @cached_property
    def savingsOpportunityAfterDiscounts(self):  # pragma: no cover
        return EBSSavingsOpportunityAfterDiscounts.make_one(
            self.boto3_raw_data["savingsOpportunityAfterDiscounts"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VolumeRecommendationOptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VolumeRecommendationOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationExportJob:
    boto3_raw_data: "type_defs.RecommendationExportJobTypeDef" = dataclasses.field()

    jobId = field("jobId")

    @cached_property
    def destination(self):  # pragma: no cover
        return ExportDestination.make_one(self.boto3_raw_data["destination"])

    resourceType = field("resourceType")
    status = field("status")
    creationTimestamp = field("creationTimestamp")
    lastUpdatedTimestamp = field("lastUpdatedTimestamp")
    failureReason = field("failureReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendationExportJobTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationExportJobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingGroupRecommendationOption:
    boto3_raw_data: "type_defs.AutoScalingGroupRecommendationOptionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configuration(self):  # pragma: no cover
        return AutoScalingGroupConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    @cached_property
    def instanceGpuInfo(self):  # pragma: no cover
        return GpuInfo.make_one(self.boto3_raw_data["instanceGpuInfo"])

    @cached_property
    def projectedUtilizationMetrics(self):  # pragma: no cover
        return UtilizationMetric.make_many(
            self.boto3_raw_data["projectedUtilizationMetrics"]
        )

    performanceRisk = field("performanceRisk")
    rank = field("rank")

    @cached_property
    def savingsOpportunity(self):  # pragma: no cover
        return SavingsOpportunity.make_one(self.boto3_raw_data["savingsOpportunity"])

    @cached_property
    def savingsOpportunityAfterDiscounts(self):  # pragma: no cover
        return AutoScalingGroupSavingsOpportunityAfterDiscounts.make_one(
            self.boto3_raw_data["savingsOpportunityAfterDiscounts"]
        )

    migrationEffort = field("migrationEffort")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutoScalingGroupRecommendationOptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingGroupRecommendationOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdleRecommendation:
    boto3_raw_data: "type_defs.IdleRecommendationTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    resourceId = field("resourceId")
    resourceType = field("resourceType")
    accountId = field("accountId")
    finding = field("finding")
    findingDescription = field("findingDescription")

    @cached_property
    def savingsOpportunity(self):  # pragma: no cover
        return IdleSavingsOpportunity.make_one(
            self.boto3_raw_data["savingsOpportunity"]
        )

    @cached_property
    def savingsOpportunityAfterDiscounts(self):  # pragma: no cover
        return IdleSavingsOpportunityAfterDiscounts.make_one(
            self.boto3_raw_data["savingsOpportunityAfterDiscounts"]
        )

    @cached_property
    def utilizationMetrics(self):  # pragma: no cover
        return IdleUtilizationMetric.make_many(
            self.boto3_raw_data["utilizationMetrics"]
        )

    lookBackPeriodInDays = field("lookBackPeriodInDays")
    lastRefreshTimestamp = field("lastRefreshTimestamp")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdleRecommendationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdleRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceRecommendationOption:
    boto3_raw_data: "type_defs.InstanceRecommendationOptionTypeDef" = (
        dataclasses.field()
    )

    instanceType = field("instanceType")

    @cached_property
    def instanceGpuInfo(self):  # pragma: no cover
        return GpuInfo.make_one(self.boto3_raw_data["instanceGpuInfo"])

    @cached_property
    def projectedUtilizationMetrics(self):  # pragma: no cover
        return UtilizationMetric.make_many(
            self.boto3_raw_data["projectedUtilizationMetrics"]
        )

    platformDifferences = field("platformDifferences")
    performanceRisk = field("performanceRisk")
    rank = field("rank")

    @cached_property
    def savingsOpportunity(self):  # pragma: no cover
        return SavingsOpportunity.make_one(self.boto3_raw_data["savingsOpportunity"])

    @cached_property
    def savingsOpportunityAfterDiscounts(self):  # pragma: no cover
        return InstanceSavingsOpportunityAfterDiscounts.make_one(
            self.boto3_raw_data["savingsOpportunityAfterDiscounts"]
        )

    migrationEffort = field("migrationEffort")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceRecommendationOptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceRecommendationOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionMemoryRecommendationOption:
    boto3_raw_data: "type_defs.LambdaFunctionMemoryRecommendationOptionTypeDef" = (
        dataclasses.field()
    )

    rank = field("rank")
    memorySize = field("memorySize")

    @cached_property
    def projectedUtilizationMetrics(self):  # pragma: no cover
        return LambdaFunctionMemoryProjectedMetric.make_many(
            self.boto3_raw_data["projectedUtilizationMetrics"]
        )

    @cached_property
    def savingsOpportunity(self):  # pragma: no cover
        return SavingsOpportunity.make_one(self.boto3_raw_data["savingsOpportunity"])

    @cached_property
    def savingsOpportunityAfterDiscounts(self):  # pragma: no cover
        return LambdaSavingsOpportunityAfterDiscounts.make_one(
            self.boto3_raw_data["savingsOpportunityAfterDiscounts"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LambdaFunctionMemoryRecommendationOptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionMemoryRecommendationOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEC2RecommendationProjectedMetricsResponse:
    boto3_raw_data: "type_defs.GetEC2RecommendationProjectedMetricsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def recommendedOptionProjectedMetrics(self):  # pragma: no cover
        return RecommendedOptionProjectedMetric.make_many(
            self.boto3_raw_data["recommendedOptionProjectedMetrics"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEC2RecommendationProjectedMetricsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEC2RecommendationProjectedMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRDSDatabaseRecommendationProjectedMetricsResponse:
    boto3_raw_data: (
        "type_defs.GetRDSDatabaseRecommendationProjectedMetricsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def recommendedOptionProjectedMetrics(self):  # pragma: no cover
        return RDSDatabaseRecommendedOptionProjectedMetric.make_many(
            self.boto3_raw_data["recommendedOptionProjectedMetrics"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRDSDatabaseRecommendationProjectedMetricsResponseTypeDef"
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
                "type_defs.GetRDSDatabaseRecommendationProjectedMetricsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RDSDBInstanceRecommendationOption:
    boto3_raw_data: "type_defs.RDSDBInstanceRecommendationOptionTypeDef" = (
        dataclasses.field()
    )

    dbInstanceClass = field("dbInstanceClass")

    @cached_property
    def projectedUtilizationMetrics(self):  # pragma: no cover
        return RDSDBUtilizationMetric.make_many(
            self.boto3_raw_data["projectedUtilizationMetrics"]
        )

    performanceRisk = field("performanceRisk")
    rank = field("rank")

    @cached_property
    def savingsOpportunity(self):  # pragma: no cover
        return SavingsOpportunity.make_one(self.boto3_raw_data["savingsOpportunity"])

    @cached_property
    def savingsOpportunityAfterDiscounts(self):  # pragma: no cover
        return RDSInstanceSavingsOpportunityAfterDiscounts.make_one(
            self.boto3_raw_data["savingsOpportunityAfterDiscounts"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RDSDBInstanceRecommendationOptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RDSDBInstanceRecommendationOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RDSDBStorageRecommendationOption:
    boto3_raw_data: "type_defs.RDSDBStorageRecommendationOptionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def storageConfiguration(self):  # pragma: no cover
        return DBStorageConfiguration.make_one(
            self.boto3_raw_data["storageConfiguration"]
        )

    rank = field("rank")

    @cached_property
    def savingsOpportunity(self):  # pragma: no cover
        return SavingsOpportunity.make_one(self.boto3_raw_data["savingsOpportunity"])

    @cached_property
    def savingsOpportunityAfterDiscounts(self):  # pragma: no cover
        return RDSStorageSavingsOpportunityAfterDiscounts.make_one(
            self.boto3_raw_data["savingsOpportunityAfterDiscounts"]
        )

    estimatedMonthlyVolumeIOPsCostVariation = field(
        "estimatedMonthlyVolumeIOPsCostVariation"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RDSDBStorageRecommendationOptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RDSDBStorageRecommendationOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationSummary:
    boto3_raw_data: "type_defs.RecommendationSummaryTypeDef" = dataclasses.field()

    @cached_property
    def summaries(self):  # pragma: no cover
        return Summary.make_many(self.boto3_raw_data["summaries"])

    @cached_property
    def idleSummaries(self):  # pragma: no cover
        return IdleSummary.make_many(self.boto3_raw_data["idleSummaries"])

    recommendationResourceType = field("recommendationResourceType")
    accountId = field("accountId")

    @cached_property
    def savingsOpportunity(self):  # pragma: no cover
        return SavingsOpportunity.make_one(self.boto3_raw_data["savingsOpportunity"])

    @cached_property
    def idleSavingsOpportunity(self):  # pragma: no cover
        return SavingsOpportunity.make_one(
            self.boto3_raw_data["idleSavingsOpportunity"]
        )

    @cached_property
    def aggregatedSavingsOpportunity(self):  # pragma: no cover
        return SavingsOpportunity.make_one(
            self.boto3_raw_data["aggregatedSavingsOpportunity"]
        )

    @cached_property
    def currentPerformanceRiskRatings(self):  # pragma: no cover
        return CurrentPerformanceRiskRatings.make_one(
            self.boto3_raw_data["currentPerformanceRiskRatings"]
        )

    @cached_property
    def inferredWorkloadSavings(self):  # pragma: no cover
        return InferredWorkloadSaving.make_many(
            self.boto3_raw_data["inferredWorkloadSavings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecommendationPreferencesResponse:
    boto3_raw_data: "type_defs.GetRecommendationPreferencesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def recommendationPreferencesDetails(self):  # pragma: no cover
        return RecommendationPreferencesDetail.make_many(
            self.boto3_raw_data["recommendationPreferencesDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRecommendationPreferencesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommendationPreferencesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ECSServiceRecommendation:
    boto3_raw_data: "type_defs.ECSServiceRecommendationTypeDef" = dataclasses.field()

    serviceArn = field("serviceArn")
    accountId = field("accountId")

    @cached_property
    def currentServiceConfiguration(self):  # pragma: no cover
        return ServiceConfiguration.make_one(
            self.boto3_raw_data["currentServiceConfiguration"]
        )

    @cached_property
    def utilizationMetrics(self):  # pragma: no cover
        return ECSServiceUtilizationMetric.make_many(
            self.boto3_raw_data["utilizationMetrics"]
        )

    lookbackPeriodInDays = field("lookbackPeriodInDays")
    launchType = field("launchType")
    lastRefreshTimestamp = field("lastRefreshTimestamp")
    finding = field("finding")
    findingReasonCodes = field("findingReasonCodes")

    @cached_property
    def serviceRecommendationOptions(self):  # pragma: no cover
        return ECSServiceRecommendationOption.make_many(
            self.boto3_raw_data["serviceRecommendationOptions"]
        )

    currentPerformanceRisk = field("currentPerformanceRisk")

    @cached_property
    def effectiveRecommendationPreferences(self):  # pragma: no cover
        return ECSEffectiveRecommendationPreferences.make_one(
            self.boto3_raw_data["effectiveRecommendationPreferences"]
        )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ECSServiceRecommendationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ECSServiceRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LicenseRecommendation:
    boto3_raw_data: "type_defs.LicenseRecommendationTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    accountId = field("accountId")

    @cached_property
    def currentLicenseConfiguration(self):  # pragma: no cover
        return LicenseConfiguration.make_one(
            self.boto3_raw_data["currentLicenseConfiguration"]
        )

    lookbackPeriodInDays = field("lookbackPeriodInDays")
    lastRefreshTimestamp = field("lastRefreshTimestamp")
    finding = field("finding")
    findingReasonCodes = field("findingReasonCodes")

    @cached_property
    def licenseRecommendationOptions(self):  # pragma: no cover
        return LicenseRecommendationOption.make_many(
            self.boto3_raw_data["licenseRecommendationOptions"]
        )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LicenseRecommendationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LicenseRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VolumeRecommendation:
    boto3_raw_data: "type_defs.VolumeRecommendationTypeDef" = dataclasses.field()

    volumeArn = field("volumeArn")
    accountId = field("accountId")

    @cached_property
    def currentConfiguration(self):  # pragma: no cover
        return VolumeConfiguration.make_one(self.boto3_raw_data["currentConfiguration"])

    finding = field("finding")

    @cached_property
    def utilizationMetrics(self):  # pragma: no cover
        return EBSUtilizationMetric.make_many(self.boto3_raw_data["utilizationMetrics"])

    lookBackPeriodInDays = field("lookBackPeriodInDays")

    @cached_property
    def volumeRecommendationOptions(self):  # pragma: no cover
        return VolumeRecommendationOption.make_many(
            self.boto3_raw_data["volumeRecommendationOptions"]
        )

    lastRefreshTimestamp = field("lastRefreshTimestamp")
    currentPerformanceRisk = field("currentPerformanceRisk")

    @cached_property
    def effectiveRecommendationPreferences(self):  # pragma: no cover
        return EBSEffectiveRecommendationPreferences.make_one(
            self.boto3_raw_data["effectiveRecommendationPreferences"]
        )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VolumeRecommendationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VolumeRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecommendationExportJobsResponse:
    boto3_raw_data: "type_defs.DescribeRecommendationExportJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def recommendationExportJobs(self):  # pragma: no cover
        return RecommendationExportJob.make_many(
            self.boto3_raw_data["recommendationExportJobs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRecommendationExportJobsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecommendationExportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingGroupRecommendation:
    boto3_raw_data: "type_defs.AutoScalingGroupRecommendationTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")
    autoScalingGroupArn = field("autoScalingGroupArn")
    autoScalingGroupName = field("autoScalingGroupName")
    finding = field("finding")

    @cached_property
    def utilizationMetrics(self):  # pragma: no cover
        return UtilizationMetric.make_many(self.boto3_raw_data["utilizationMetrics"])

    lookBackPeriodInDays = field("lookBackPeriodInDays")

    @cached_property
    def currentConfiguration(self):  # pragma: no cover
        return AutoScalingGroupConfiguration.make_one(
            self.boto3_raw_data["currentConfiguration"]
        )

    @cached_property
    def currentInstanceGpuInfo(self):  # pragma: no cover
        return GpuInfo.make_one(self.boto3_raw_data["currentInstanceGpuInfo"])

    @cached_property
    def recommendationOptions(self):  # pragma: no cover
        return AutoScalingGroupRecommendationOption.make_many(
            self.boto3_raw_data["recommendationOptions"]
        )

    lastRefreshTimestamp = field("lastRefreshTimestamp")
    currentPerformanceRisk = field("currentPerformanceRisk")

    @cached_property
    def effectiveRecommendationPreferences(self):  # pragma: no cover
        return EffectiveRecommendationPreferences.make_one(
            self.boto3_raw_data["effectiveRecommendationPreferences"]
        )

    inferredWorkloadTypes = field("inferredWorkloadTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutoScalingGroupRecommendationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingGroupRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdleRecommendationsResponse:
    boto3_raw_data: "type_defs.GetIdleRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def idleRecommendations(self):  # pragma: no cover
        return IdleRecommendation.make_many(self.boto3_raw_data["idleRecommendations"])

    @cached_property
    def errors(self):  # pragma: no cover
        return IdleRecommendationError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetIdleRecommendationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdleRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceRecommendation:
    boto3_raw_data: "type_defs.InstanceRecommendationTypeDef" = dataclasses.field()

    instanceArn = field("instanceArn")
    accountId = field("accountId")
    instanceName = field("instanceName")
    currentInstanceType = field("currentInstanceType")
    finding = field("finding")
    findingReasonCodes = field("findingReasonCodes")

    @cached_property
    def utilizationMetrics(self):  # pragma: no cover
        return UtilizationMetric.make_many(self.boto3_raw_data["utilizationMetrics"])

    lookBackPeriodInDays = field("lookBackPeriodInDays")

    @cached_property
    def recommendationOptions(self):  # pragma: no cover
        return InstanceRecommendationOption.make_many(
            self.boto3_raw_data["recommendationOptions"]
        )

    @cached_property
    def recommendationSources(self):  # pragma: no cover
        return RecommendationSource.make_many(
            self.boto3_raw_data["recommendationSources"]
        )

    lastRefreshTimestamp = field("lastRefreshTimestamp")
    currentPerformanceRisk = field("currentPerformanceRisk")

    @cached_property
    def effectiveRecommendationPreferences(self):  # pragma: no cover
        return EffectiveRecommendationPreferences.make_one(
            self.boto3_raw_data["effectiveRecommendationPreferences"]
        )

    inferredWorkloadTypes = field("inferredWorkloadTypes")
    instanceState = field("instanceState")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def externalMetricStatus(self):  # pragma: no cover
        return ExternalMetricStatus.make_one(
            self.boto3_raw_data["externalMetricStatus"]
        )

    @cached_property
    def currentInstanceGpuInfo(self):  # pragma: no cover
        return GpuInfo.make_one(self.boto3_raw_data["currentInstanceGpuInfo"])

    idle = field("idle")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceRecommendationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionRecommendation:
    boto3_raw_data: "type_defs.LambdaFunctionRecommendationTypeDef" = (
        dataclasses.field()
    )

    functionArn = field("functionArn")
    functionVersion = field("functionVersion")
    accountId = field("accountId")
    currentMemorySize = field("currentMemorySize")
    numberOfInvocations = field("numberOfInvocations")

    @cached_property
    def utilizationMetrics(self):  # pragma: no cover
        return LambdaFunctionUtilizationMetric.make_many(
            self.boto3_raw_data["utilizationMetrics"]
        )

    lookbackPeriodInDays = field("lookbackPeriodInDays")
    lastRefreshTimestamp = field("lastRefreshTimestamp")
    finding = field("finding")
    findingReasonCodes = field("findingReasonCodes")

    @cached_property
    def memorySizeRecommendationOptions(self):  # pragma: no cover
        return LambdaFunctionMemoryRecommendationOption.make_many(
            self.boto3_raw_data["memorySizeRecommendationOptions"]
        )

    currentPerformanceRisk = field("currentPerformanceRisk")

    @cached_property
    def effectiveRecommendationPreferences(self):  # pragma: no cover
        return LambdaEffectiveRecommendationPreferences.make_one(
            self.boto3_raw_data["effectiveRecommendationPreferences"]
        )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaFunctionRecommendationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RDSDBRecommendation:
    boto3_raw_data: "type_defs.RDSDBRecommendationTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    accountId = field("accountId")
    engine = field("engine")
    engineVersion = field("engineVersion")
    promotionTier = field("promotionTier")
    currentDBInstanceClass = field("currentDBInstanceClass")

    @cached_property
    def currentStorageConfiguration(self):  # pragma: no cover
        return DBStorageConfiguration.make_one(
            self.boto3_raw_data["currentStorageConfiguration"]
        )

    dbClusterIdentifier = field("dbClusterIdentifier")
    idle = field("idle")
    instanceFinding = field("instanceFinding")
    storageFinding = field("storageFinding")
    instanceFindingReasonCodes = field("instanceFindingReasonCodes")
    currentInstancePerformanceRisk = field("currentInstancePerformanceRisk")
    currentStorageEstimatedMonthlyVolumeIOPsCostVariation = field(
        "currentStorageEstimatedMonthlyVolumeIOPsCostVariation"
    )
    storageFindingReasonCodes = field("storageFindingReasonCodes")

    @cached_property
    def instanceRecommendationOptions(self):  # pragma: no cover
        return RDSDBInstanceRecommendationOption.make_many(
            self.boto3_raw_data["instanceRecommendationOptions"]
        )

    @cached_property
    def storageRecommendationOptions(self):  # pragma: no cover
        return RDSDBStorageRecommendationOption.make_many(
            self.boto3_raw_data["storageRecommendationOptions"]
        )

    @cached_property
    def utilizationMetrics(self):  # pragma: no cover
        return RDSDBUtilizationMetric.make_many(
            self.boto3_raw_data["utilizationMetrics"]
        )

    @cached_property
    def effectiveRecommendationPreferences(self):  # pragma: no cover
        return RDSEffectiveRecommendationPreferences.make_one(
            self.boto3_raw_data["effectiveRecommendationPreferences"]
        )

    lookbackPeriodInDays = field("lookbackPeriodInDays")
    lastRefreshTimestamp = field("lastRefreshTimestamp")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RDSDBRecommendationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RDSDBRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecommendationSummariesResponse:
    boto3_raw_data: "type_defs.GetRecommendationSummariesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def recommendationSummaries(self):  # pragma: no cover
        return RecommendationSummary.make_many(
            self.boto3_raw_data["recommendationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRecommendationSummariesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommendationSummariesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetECSServiceRecommendationsResponse:
    boto3_raw_data: "type_defs.GetECSServiceRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ecsServiceRecommendations(self):  # pragma: no cover
        return ECSServiceRecommendation.make_many(
            self.boto3_raw_data["ecsServiceRecommendations"]
        )

    @cached_property
    def errors(self):  # pragma: no cover
        return GetRecommendationError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetECSServiceRecommendationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetECSServiceRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLicenseRecommendationsResponse:
    boto3_raw_data: "type_defs.GetLicenseRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def licenseRecommendations(self):  # pragma: no cover
        return LicenseRecommendation.make_many(
            self.boto3_raw_data["licenseRecommendations"]
        )

    @cached_property
    def errors(self):  # pragma: no cover
        return GetRecommendationError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetLicenseRecommendationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLicenseRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEBSVolumeRecommendationsResponse:
    boto3_raw_data: "type_defs.GetEBSVolumeRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def volumeRecommendations(self):  # pragma: no cover
        return VolumeRecommendation.make_many(
            self.boto3_raw_data["volumeRecommendations"]
        )

    @cached_property
    def errors(self):  # pragma: no cover
        return GetRecommendationError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEBSVolumeRecommendationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEBSVolumeRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutoScalingGroupRecommendationsResponse:
    boto3_raw_data: "type_defs.GetAutoScalingGroupRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def autoScalingGroupRecommendations(self):  # pragma: no cover
        return AutoScalingGroupRecommendation.make_many(
            self.boto3_raw_data["autoScalingGroupRecommendations"]
        )

    @cached_property
    def errors(self):  # pragma: no cover
        return GetRecommendationError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAutoScalingGroupRecommendationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAutoScalingGroupRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEC2InstanceRecommendationsResponse:
    boto3_raw_data: "type_defs.GetEC2InstanceRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def instanceRecommendations(self):  # pragma: no cover
        return InstanceRecommendation.make_many(
            self.boto3_raw_data["instanceRecommendations"]
        )

    @cached_property
    def errors(self):  # pragma: no cover
        return GetRecommendationError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEC2InstanceRecommendationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEC2InstanceRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLambdaFunctionRecommendationsResponse:
    boto3_raw_data: "type_defs.GetLambdaFunctionRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def lambdaFunctionRecommendations(self):  # pragma: no cover
        return LambdaFunctionRecommendation.make_many(
            self.boto3_raw_data["lambdaFunctionRecommendations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetLambdaFunctionRecommendationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLambdaFunctionRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRDSDatabaseRecommendationsResponse:
    boto3_raw_data: "type_defs.GetRDSDatabaseRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def rdsDBRecommendations(self):  # pragma: no cover
        return RDSDBRecommendation.make_many(
            self.boto3_raw_data["rdsDBRecommendations"]
        )

    @cached_property
    def errors(self):  # pragma: no cover
        return GetRecommendationError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRDSDatabaseRecommendationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRDSDatabaseRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
