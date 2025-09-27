# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cost_optimization_hub import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccountEnrollmentStatus:
    boto3_raw_data: "type_defs.AccountEnrollmentStatusTypeDef" = dataclasses.field()

    accountId = field("accountId")
    status = field("status")
    lastUpdatedTimestamp = field("lastUpdatedTimestamp")
    createdTimestamp = field("createdTimestamp")

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
class AuroraDbClusterStorageConfiguration:
    boto3_raw_data: "type_defs.AuroraDbClusterStorageConfigurationTypeDef" = (
        dataclasses.field()
    )

    storageType = field("storageType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AuroraDbClusterStorageConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuroraDbClusterStorageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlockStoragePerformanceConfiguration:
    boto3_raw_data: "type_defs.BlockStoragePerformanceConfigurationTypeDef" = (
        dataclasses.field()
    )

    iops = field("iops")
    throughput = field("throughput")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BlockStoragePerformanceConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BlockStoragePerformanceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeConfiguration:
    boto3_raw_data: "type_defs.ComputeConfigurationTypeDef" = dataclasses.field()

    vCpu = field("vCpu")
    memorySizeInMB = field("memorySizeInMB")
    architecture = field("architecture")
    platform = field("platform")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComputeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeSavingsPlansConfiguration:
    boto3_raw_data: "type_defs.ComputeSavingsPlansConfigurationTypeDef" = (
        dataclasses.field()
    )

    accountScope = field("accountScope")
    term = field("term")
    paymentOption = field("paymentOption")
    hourlyCommitment = field("hourlyCommitment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ComputeSavingsPlansConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputeSavingsPlansConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DbInstanceConfiguration:
    boto3_raw_data: "type_defs.DbInstanceConfigurationTypeDef" = dataclasses.field()

    dbInstanceClass = field("dbInstanceClass")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DbInstanceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DbInstanceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DynamoDbReservedCapacityConfiguration:
    boto3_raw_data: "type_defs.DynamoDbReservedCapacityConfigurationTypeDef" = (
        dataclasses.field()
    )

    accountScope = field("accountScope")
    service = field("service")
    term = field("term")
    paymentOption = field("paymentOption")
    reservedInstancesRegion = field("reservedInstancesRegion")
    upfrontCost = field("upfrontCost")
    monthlyRecurringCost = field("monthlyRecurringCost")
    numberOfCapacityUnitsToPurchase = field("numberOfCapacityUnitsToPurchase")
    capacityUnits = field("capacityUnits")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DynamoDbReservedCapacityConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DynamoDbReservedCapacityConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageConfiguration:
    boto3_raw_data: "type_defs.StorageConfigurationTypeDef" = dataclasses.field()

    type = field("type")
    sizeInGb = field("sizeInGb")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceConfiguration:
    boto3_raw_data: "type_defs.InstanceConfigurationTypeDef" = dataclasses.field()

    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MixedInstanceConfiguration:
    boto3_raw_data: "type_defs.MixedInstanceConfigurationTypeDef" = dataclasses.field()

    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MixedInstanceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MixedInstanceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ec2InstanceSavingsPlansConfiguration:
    boto3_raw_data: "type_defs.Ec2InstanceSavingsPlansConfigurationTypeDef" = (
        dataclasses.field()
    )

    accountScope = field("accountScope")
    term = field("term")
    paymentOption = field("paymentOption")
    hourlyCommitment = field("hourlyCommitment")
    instanceFamily = field("instanceFamily")
    savingsPlansRegion = field("savingsPlansRegion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.Ec2InstanceSavingsPlansConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Ec2InstanceSavingsPlansConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ec2ReservedInstancesConfiguration:
    boto3_raw_data: "type_defs.Ec2ReservedInstancesConfigurationTypeDef" = (
        dataclasses.field()
    )

    accountScope = field("accountScope")
    service = field("service")
    term = field("term")
    paymentOption = field("paymentOption")
    reservedInstancesRegion = field("reservedInstancesRegion")
    upfrontCost = field("upfrontCost")
    monthlyRecurringCost = field("monthlyRecurringCost")
    normalizedUnitsToPurchase = field("normalizedUnitsToPurchase")
    numberOfInstancesToPurchase = field("numberOfInstancesToPurchase")
    offeringClass = field("offeringClass")
    instanceFamily = field("instanceFamily")
    instanceType = field("instanceType")
    currentGeneration = field("currentGeneration")
    platform = field("platform")
    tenancy = field("tenancy")
    sizeFlexEligible = field("sizeFlexEligible")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.Ec2ReservedInstancesConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Ec2ReservedInstancesConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElastiCacheReservedInstancesConfiguration:
    boto3_raw_data: "type_defs.ElastiCacheReservedInstancesConfigurationTypeDef" = (
        dataclasses.field()
    )

    accountScope = field("accountScope")
    service = field("service")
    term = field("term")
    paymentOption = field("paymentOption")
    reservedInstancesRegion = field("reservedInstancesRegion")
    upfrontCost = field("upfrontCost")
    monthlyRecurringCost = field("monthlyRecurringCost")
    normalizedUnitsToPurchase = field("normalizedUnitsToPurchase")
    numberOfInstancesToPurchase = field("numberOfInstancesToPurchase")
    instanceFamily = field("instanceFamily")
    instanceType = field("instanceType")
    currentGeneration = field("currentGeneration")
    sizeFlexEligible = field("sizeFlexEligible")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ElastiCacheReservedInstancesConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ElastiCacheReservedInstancesConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EstimatedDiscounts:
    boto3_raw_data: "type_defs.EstimatedDiscountsTypeDef" = dataclasses.field()

    savingsPlansDiscount = field("savingsPlansDiscount")
    reservedInstancesDiscount = field("reservedInstancesDiscount")
    otherDiscount = field("otherDiscount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EstimatedDiscountsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EstimatedDiscountsTypeDef"]
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
class PreferredCommitment:
    boto3_raw_data: "type_defs.PreferredCommitmentTypeDef" = dataclasses.field()

    term = field("term")
    paymentOption = field("paymentOption")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PreferredCommitmentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PreferredCommitmentTypeDef"]
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
class GetRecommendationRequest:
    boto3_raw_data: "type_defs.GetRecommendationRequestTypeDef" = dataclasses.field()

    recommendationId = field("recommendationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRecommendationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommendationRequestTypeDef"]
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
class ListEnrollmentStatusesRequest:
    boto3_raw_data: "type_defs.ListEnrollmentStatusesRequestTypeDef" = (
        dataclasses.field()
    )

    includeOrganizationInfo = field("includeOrganizationInfo")
    accountId = field("accountId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEnrollmentStatusesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnrollmentStatusesRequestTypeDef"]
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

    group = field("group")
    estimatedMonthlySavings = field("estimatedMonthlySavings")
    recommendationCount = field("recommendationCount")

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
class SummaryMetricsResult:
    boto3_raw_data: "type_defs.SummaryMetricsResultTypeDef" = dataclasses.field()

    savingsPercentage = field("savingsPercentage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SummaryMetricsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SummaryMetricsResultTypeDef"]
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
class MemoryDbReservedInstancesConfiguration:
    boto3_raw_data: "type_defs.MemoryDbReservedInstancesConfigurationTypeDef" = (
        dataclasses.field()
    )

    accountScope = field("accountScope")
    service = field("service")
    term = field("term")
    paymentOption = field("paymentOption")
    reservedInstancesRegion = field("reservedInstancesRegion")
    upfrontCost = field("upfrontCost")
    monthlyRecurringCost = field("monthlyRecurringCost")
    normalizedUnitsToPurchase = field("normalizedUnitsToPurchase")
    numberOfInstancesToPurchase = field("numberOfInstancesToPurchase")
    instanceType = field("instanceType")
    instanceFamily = field("instanceFamily")
    sizeFlexEligible = field("sizeFlexEligible")
    currentGeneration = field("currentGeneration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MemoryDbReservedInstancesConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemoryDbReservedInstancesConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenSearchReservedInstancesConfiguration:
    boto3_raw_data: "type_defs.OpenSearchReservedInstancesConfigurationTypeDef" = (
        dataclasses.field()
    )

    accountScope = field("accountScope")
    service = field("service")
    term = field("term")
    paymentOption = field("paymentOption")
    reservedInstancesRegion = field("reservedInstancesRegion")
    upfrontCost = field("upfrontCost")
    monthlyRecurringCost = field("monthlyRecurringCost")
    normalizedUnitsToPurchase = field("normalizedUnitsToPurchase")
    numberOfInstancesToPurchase = field("numberOfInstancesToPurchase")
    instanceType = field("instanceType")
    currentGeneration = field("currentGeneration")
    sizeFlexEligible = field("sizeFlexEligible")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OpenSearchReservedInstancesConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenSearchReservedInstancesConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsDbInstanceStorageConfiguration:
    boto3_raw_data: "type_defs.RdsDbInstanceStorageConfigurationTypeDef" = (
        dataclasses.field()
    )

    storageType = field("storageType")
    allocatedStorageInGb = field("allocatedStorageInGb")
    iops = field("iops")
    storageThroughput = field("storageThroughput")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RdsDbInstanceStorageConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsDbInstanceStorageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsReservedInstancesConfiguration:
    boto3_raw_data: "type_defs.RdsReservedInstancesConfigurationTypeDef" = (
        dataclasses.field()
    )

    accountScope = field("accountScope")
    service = field("service")
    term = field("term")
    paymentOption = field("paymentOption")
    reservedInstancesRegion = field("reservedInstancesRegion")
    upfrontCost = field("upfrontCost")
    monthlyRecurringCost = field("monthlyRecurringCost")
    normalizedUnitsToPurchase = field("normalizedUnitsToPurchase")
    numberOfInstancesToPurchase = field("numberOfInstancesToPurchase")
    instanceFamily = field("instanceFamily")
    instanceType = field("instanceType")
    sizeFlexEligible = field("sizeFlexEligible")
    currentGeneration = field("currentGeneration")
    licenseModel = field("licenseModel")
    databaseEdition = field("databaseEdition")
    databaseEngine = field("databaseEngine")
    deploymentOption = field("deploymentOption")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RdsReservedInstancesConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsReservedInstancesConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftReservedInstancesConfiguration:
    boto3_raw_data: "type_defs.RedshiftReservedInstancesConfigurationTypeDef" = (
        dataclasses.field()
    )

    accountScope = field("accountScope")
    service = field("service")
    term = field("term")
    paymentOption = field("paymentOption")
    reservedInstancesRegion = field("reservedInstancesRegion")
    upfrontCost = field("upfrontCost")
    monthlyRecurringCost = field("monthlyRecurringCost")
    normalizedUnitsToPurchase = field("normalizedUnitsToPurchase")
    numberOfInstancesToPurchase = field("numberOfInstancesToPurchase")
    instanceFamily = field("instanceFamily")
    instanceType = field("instanceType")
    sizeFlexEligible = field("sizeFlexEligible")
    currentGeneration = field("currentGeneration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RedshiftReservedInstancesConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftReservedInstancesConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservedInstancesPricing:
    boto3_raw_data: "type_defs.ReservedInstancesPricingTypeDef" = dataclasses.field()

    estimatedOnDemandCost = field("estimatedOnDemandCost")
    monthlyReservationEligibleCost = field("monthlyReservationEligibleCost")
    savingsPercentage = field("savingsPercentage")
    estimatedMonthlyAmortizedReservationCost = field(
        "estimatedMonthlyAmortizedReservationCost"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReservedInstancesPricingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservedInstancesPricingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Usage:
    boto3_raw_data: "type_defs.UsageTypeDef" = dataclasses.field()

    usageType = field("usageType")
    usageAmount = field("usageAmount")
    operation = field("operation")
    productCode = field("productCode")
    unit = field("unit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UsageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UsageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SageMakerSavingsPlansConfiguration:
    boto3_raw_data: "type_defs.SageMakerSavingsPlansConfigurationTypeDef" = (
        dataclasses.field()
    )

    accountScope = field("accountScope")
    term = field("term")
    paymentOption = field("paymentOption")
    hourlyCommitment = field("hourlyCommitment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SageMakerSavingsPlansConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SageMakerSavingsPlansConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlansPricing:
    boto3_raw_data: "type_defs.SavingsPlansPricingTypeDef" = dataclasses.field()

    monthlySavingsPlansEligibleCost = field("monthlySavingsPlansEligibleCost")
    estimatedMonthlyCommitment = field("estimatedMonthlyCommitment")
    savingsPercentage = field("savingsPercentage")
    estimatedOnDemandCost = field("estimatedOnDemandCost")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SavingsPlansPricingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlansPricingTypeDef"]
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
class EcsServiceConfiguration:
    boto3_raw_data: "type_defs.EcsServiceConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def compute(self):  # pragma: no cover
        return ComputeConfiguration.make_one(self.boto3_raw_data["compute"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EcsServiceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcsServiceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionConfiguration:
    boto3_raw_data: "type_defs.LambdaFunctionConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def compute(self):  # pragma: no cover
        return ComputeConfiguration.make_one(self.boto3_raw_data["compute"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaFunctionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsDbInstanceConfiguration:
    boto3_raw_data: "type_defs.RdsDbInstanceConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def instance(self):  # pragma: no cover
        return DbInstanceConfiguration.make_one(self.boto3_raw_data["instance"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RdsDbInstanceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsDbInstanceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EbsVolumeConfiguration:
    boto3_raw_data: "type_defs.EbsVolumeConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def storage(self):  # pragma: no cover
        return StorageConfiguration.make_one(self.boto3_raw_data["storage"])

    @cached_property
    def performance(self):  # pragma: no cover
        return BlockStoragePerformanceConfiguration.make_one(
            self.boto3_raw_data["performance"]
        )

    attachmentState = field("attachmentState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EbsVolumeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EbsVolumeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ec2InstanceConfiguration:
    boto3_raw_data: "type_defs.Ec2InstanceConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def instance(self):  # pragma: no cover
        return InstanceConfiguration.make_one(self.boto3_raw_data["instance"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Ec2InstanceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Ec2InstanceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ec2AutoScalingGroupConfiguration:
    boto3_raw_data: "type_defs.Ec2AutoScalingGroupConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def instance(self):  # pragma: no cover
        return InstanceConfiguration.make_one(self.boto3_raw_data["instance"])

    @cached_property
    def mixedInstances(self):  # pragma: no cover
        return MixedInstanceConfiguration.make_many(
            self.boto3_raw_data["mixedInstances"]
        )

    type = field("type")
    allocationStrategy = field("allocationStrategy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.Ec2AutoScalingGroupConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Ec2AutoScalingGroupConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourcePricing:
    boto3_raw_data: "type_defs.ResourcePricingTypeDef" = dataclasses.field()

    estimatedCostBeforeDiscounts = field("estimatedCostBeforeDiscounts")
    estimatedNetUnusedAmortizedCommitments = field(
        "estimatedNetUnusedAmortizedCommitments"
    )

    @cached_property
    def estimatedDiscounts(self):  # pragma: no cover
        return EstimatedDiscounts.make_one(self.boto3_raw_data["estimatedDiscounts"])

    estimatedCostAfterDiscounts = field("estimatedCostAfterDiscounts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourcePricingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourcePricingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filter:
    boto3_raw_data: "type_defs.FilterTypeDef" = dataclasses.field()

    restartNeeded = field("restartNeeded")
    rollbackPossible = field("rollbackPossible")
    implementationEfforts = field("implementationEfforts")
    accountIds = field("accountIds")
    regions = field("regions")
    resourceTypes = field("resourceTypes")
    actionTypes = field("actionTypes")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    resourceIds = field("resourceIds")
    resourceArns = field("resourceArns")
    recommendationIds = field("recommendationIds")

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
class Recommendation:
    boto3_raw_data: "type_defs.RecommendationTypeDef" = dataclasses.field()

    recommendationId = field("recommendationId")
    accountId = field("accountId")
    region = field("region")
    resourceId = field("resourceId")
    resourceArn = field("resourceArn")
    currentResourceType = field("currentResourceType")
    recommendedResourceType = field("recommendedResourceType")
    estimatedMonthlySavings = field("estimatedMonthlySavings")
    estimatedSavingsPercentage = field("estimatedSavingsPercentage")
    estimatedMonthlyCost = field("estimatedMonthlyCost")
    currencyCode = field("currencyCode")
    implementationEffort = field("implementationEffort")
    restartNeeded = field("restartNeeded")
    actionType = field("actionType")
    rollbackPossible = field("rollbackPossible")
    currentResourceSummary = field("currentResourceSummary")
    recommendedResourceSummary = field("recommendedResourceSummary")
    lastRefreshTimestamp = field("lastRefreshTimestamp")
    recommendationLookbackPeriodInDays = field("recommendationLookbackPeriodInDays")
    source = field("source")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class UpdatePreferencesRequest:
    boto3_raw_data: "type_defs.UpdatePreferencesRequestTypeDef" = dataclasses.field()

    savingsEstimationMode = field("savingsEstimationMode")
    memberAccountDiscountVisibility = field("memberAccountDiscountVisibility")

    @cached_property
    def preferredCommitment(self):  # pragma: no cover
        return PreferredCommitment.make_one(self.boto3_raw_data["preferredCommitment"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePreferencesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePreferencesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPreferencesResponse:
    boto3_raw_data: "type_defs.GetPreferencesResponseTypeDef" = dataclasses.field()

    savingsEstimationMode = field("savingsEstimationMode")
    memberAccountDiscountVisibility = field("memberAccountDiscountVisibility")

    @cached_property
    def preferredCommitment(self):  # pragma: no cover
        return PreferredCommitment.make_one(self.boto3_raw_data["preferredCommitment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPreferencesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPreferencesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnrollmentStatusesResponse:
    boto3_raw_data: "type_defs.ListEnrollmentStatusesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return AccountEnrollmentStatus.make_many(self.boto3_raw_data["items"])

    includeMemberAccounts = field("includeMemberAccounts")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEnrollmentStatusesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnrollmentStatusesResponseTypeDef"]
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
class UpdatePreferencesResponse:
    boto3_raw_data: "type_defs.UpdatePreferencesResponseTypeDef" = dataclasses.field()

    savingsEstimationMode = field("savingsEstimationMode")
    memberAccountDiscountVisibility = field("memberAccountDiscountVisibility")

    @cached_property
    def preferredCommitment(self):  # pragma: no cover
        return PreferredCommitment.make_one(self.boto3_raw_data["preferredCommitment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePreferencesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePreferencesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnrollmentStatusesRequestPaginate:
    boto3_raw_data: "type_defs.ListEnrollmentStatusesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    includeOrganizationInfo = field("includeOrganizationInfo")
    accountId = field("accountId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEnrollmentStatusesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnrollmentStatusesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationSummariesResponse:
    boto3_raw_data: "type_defs.ListRecommendationSummariesResponseTypeDef" = (
        dataclasses.field()
    )

    estimatedTotalDedupedSavings = field("estimatedTotalDedupedSavings")

    @cached_property
    def items(self):  # pragma: no cover
        return RecommendationSummary.make_many(self.boto3_raw_data["items"])

    groupBy = field("groupBy")
    currencyCode = field("currencyCode")

    @cached_property
    def metrics(self):  # pragma: no cover
        return SummaryMetricsResult.make_one(self.boto3_raw_data["metrics"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecommendationSummariesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationSummariesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservedInstancesCostCalculation:
    boto3_raw_data: "type_defs.ReservedInstancesCostCalculationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def pricing(self):  # pragma: no cover
        return ReservedInstancesPricing.make_one(self.boto3_raw_data["pricing"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReservedInstancesCostCalculationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservedInstancesCostCalculationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlansCostCalculation:
    boto3_raw_data: "type_defs.SavingsPlansCostCalculationTypeDef" = dataclasses.field()

    @cached_property
    def pricing(self):  # pragma: no cover
        return SavingsPlansPricing.make_one(self.boto3_raw_data["pricing"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SavingsPlansCostCalculationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlansCostCalculationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceCostCalculation:
    boto3_raw_data: "type_defs.ResourceCostCalculationTypeDef" = dataclasses.field()

    @cached_property
    def usages(self):  # pragma: no cover
        return Usage.make_many(self.boto3_raw_data["usages"])

    @cached_property
    def pricing(self):  # pragma: no cover
        return ResourcePricing.make_one(self.boto3_raw_data["pricing"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceCostCalculationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceCostCalculationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationSummariesRequestPaginate:
    boto3_raw_data: "type_defs.ListRecommendationSummariesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    groupBy = field("groupBy")

    @cached_property
    def filter(self):  # pragma: no cover
        return Filter.make_one(self.boto3_raw_data["filter"])

    metrics = field("metrics")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecommendationSummariesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationSummariesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationSummariesRequest:
    boto3_raw_data: "type_defs.ListRecommendationSummariesRequestTypeDef" = (
        dataclasses.field()
    )

    groupBy = field("groupBy")

    @cached_property
    def filter(self):  # pragma: no cover
        return Filter.make_one(self.boto3_raw_data["filter"])

    maxResults = field("maxResults")
    metrics = field("metrics")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecommendationSummariesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationSummariesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationsRequestPaginate:
    boto3_raw_data: "type_defs.ListRecommendationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filter(self):  # pragma: no cover
        return Filter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def orderBy(self):  # pragma: no cover
        return OrderBy.make_one(self.boto3_raw_data["orderBy"])

    includeAllRecommendations = field("includeAllRecommendations")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecommendationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationsRequest:
    boto3_raw_data: "type_defs.ListRecommendationsRequestTypeDef" = dataclasses.field()

    @cached_property
    def filter(self):  # pragma: no cover
        return Filter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def orderBy(self):  # pragma: no cover
        return OrderBy.make_one(self.boto3_raw_data["orderBy"])

    includeAllRecommendations = field("includeAllRecommendations")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecommendationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationsResponse:
    boto3_raw_data: "type_defs.ListRecommendationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return Recommendation.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecommendationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DynamoDbReservedCapacity:
    boto3_raw_data: "type_defs.DynamoDbReservedCapacityTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return DynamoDbReservedCapacityConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    @cached_property
    def costCalculation(self):  # pragma: no cover
        return ReservedInstancesCostCalculation.make_one(
            self.boto3_raw_data["costCalculation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DynamoDbReservedCapacityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DynamoDbReservedCapacityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ec2ReservedInstances:
    boto3_raw_data: "type_defs.Ec2ReservedInstancesTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return Ec2ReservedInstancesConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    @cached_property
    def costCalculation(self):  # pragma: no cover
        return ReservedInstancesCostCalculation.make_one(
            self.boto3_raw_data["costCalculation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Ec2ReservedInstancesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Ec2ReservedInstancesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElastiCacheReservedInstances:
    boto3_raw_data: "type_defs.ElastiCacheReservedInstancesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configuration(self):  # pragma: no cover
        return ElastiCacheReservedInstancesConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    @cached_property
    def costCalculation(self):  # pragma: no cover
        return ReservedInstancesCostCalculation.make_one(
            self.boto3_raw_data["costCalculation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ElastiCacheReservedInstancesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ElastiCacheReservedInstancesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemoryDbReservedInstances:
    boto3_raw_data: "type_defs.MemoryDbReservedInstancesTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return MemoryDbReservedInstancesConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    @cached_property
    def costCalculation(self):  # pragma: no cover
        return ReservedInstancesCostCalculation.make_one(
            self.boto3_raw_data["costCalculation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MemoryDbReservedInstancesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemoryDbReservedInstancesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenSearchReservedInstances:
    boto3_raw_data: "type_defs.OpenSearchReservedInstancesTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return OpenSearchReservedInstancesConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    @cached_property
    def costCalculation(self):  # pragma: no cover
        return ReservedInstancesCostCalculation.make_one(
            self.boto3_raw_data["costCalculation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenSearchReservedInstancesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenSearchReservedInstancesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsReservedInstances:
    boto3_raw_data: "type_defs.RdsReservedInstancesTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return RdsReservedInstancesConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    @cached_property
    def costCalculation(self):  # pragma: no cover
        return ReservedInstancesCostCalculation.make_one(
            self.boto3_raw_data["costCalculation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RdsReservedInstancesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsReservedInstancesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftReservedInstances:
    boto3_raw_data: "type_defs.RedshiftReservedInstancesTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return RedshiftReservedInstancesConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    @cached_property
    def costCalculation(self):  # pragma: no cover
        return ReservedInstancesCostCalculation.make_one(
            self.boto3_raw_data["costCalculation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedshiftReservedInstancesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftReservedInstancesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeSavingsPlans:
    boto3_raw_data: "type_defs.ComputeSavingsPlansTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return ComputeSavingsPlansConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    @cached_property
    def costCalculation(self):  # pragma: no cover
        return SavingsPlansCostCalculation.make_one(
            self.boto3_raw_data["costCalculation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComputeSavingsPlansTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputeSavingsPlansTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ec2InstanceSavingsPlans:
    boto3_raw_data: "type_defs.Ec2InstanceSavingsPlansTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return Ec2InstanceSavingsPlansConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    @cached_property
    def costCalculation(self):  # pragma: no cover
        return SavingsPlansCostCalculation.make_one(
            self.boto3_raw_data["costCalculation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Ec2InstanceSavingsPlansTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Ec2InstanceSavingsPlansTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SageMakerSavingsPlans:
    boto3_raw_data: "type_defs.SageMakerSavingsPlansTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return SageMakerSavingsPlansConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    @cached_property
    def costCalculation(self):  # pragma: no cover
        return SavingsPlansCostCalculation.make_one(
            self.boto3_raw_data["costCalculation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SageMakerSavingsPlansTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SageMakerSavingsPlansTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuroraDbClusterStorage:
    boto3_raw_data: "type_defs.AuroraDbClusterStorageTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return AuroraDbClusterStorageConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    @cached_property
    def costCalculation(self):  # pragma: no cover
        return ResourceCostCalculation.make_one(self.boto3_raw_data["costCalculation"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuroraDbClusterStorageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuroraDbClusterStorageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EbsVolume:
    boto3_raw_data: "type_defs.EbsVolumeTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return EbsVolumeConfiguration.make_one(self.boto3_raw_data["configuration"])

    @cached_property
    def costCalculation(self):  # pragma: no cover
        return ResourceCostCalculation.make_one(self.boto3_raw_data["costCalculation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EbsVolumeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EbsVolumeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ec2AutoScalingGroup:
    boto3_raw_data: "type_defs.Ec2AutoScalingGroupTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return Ec2AutoScalingGroupConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    @cached_property
    def costCalculation(self):  # pragma: no cover
        return ResourceCostCalculation.make_one(self.boto3_raw_data["costCalculation"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Ec2AutoScalingGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Ec2AutoScalingGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ec2Instance:
    boto3_raw_data: "type_defs.Ec2InstanceTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return Ec2InstanceConfiguration.make_one(self.boto3_raw_data["configuration"])

    @cached_property
    def costCalculation(self):  # pragma: no cover
        return ResourceCostCalculation.make_one(self.boto3_raw_data["costCalculation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Ec2InstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Ec2InstanceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsService:
    boto3_raw_data: "type_defs.EcsServiceTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return EcsServiceConfiguration.make_one(self.boto3_raw_data["configuration"])

    @cached_property
    def costCalculation(self):  # pragma: no cover
        return ResourceCostCalculation.make_one(self.boto3_raw_data["costCalculation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EcsServiceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EcsServiceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunction:
    boto3_raw_data: "type_defs.LambdaFunctionTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return LambdaFunctionConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    @cached_property
    def costCalculation(self):  # pragma: no cover
        return ResourceCostCalculation.make_one(self.boto3_raw_data["costCalculation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LambdaFunctionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LambdaFunctionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsDbInstanceStorage:
    boto3_raw_data: "type_defs.RdsDbInstanceStorageTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return RdsDbInstanceStorageConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    @cached_property
    def costCalculation(self):  # pragma: no cover
        return ResourceCostCalculation.make_one(self.boto3_raw_data["costCalculation"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RdsDbInstanceStorageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsDbInstanceStorageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsDbInstance:
    boto3_raw_data: "type_defs.RdsDbInstanceTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return RdsDbInstanceConfiguration.make_one(self.boto3_raw_data["configuration"])

    @cached_property
    def costCalculation(self):  # pragma: no cover
        return ResourceCostCalculation.make_one(self.boto3_raw_data["costCalculation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RdsDbInstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RdsDbInstanceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceDetails:
    boto3_raw_data: "type_defs.ResourceDetailsTypeDef" = dataclasses.field()

    @cached_property
    def lambdaFunction(self):  # pragma: no cover
        return LambdaFunction.make_one(self.boto3_raw_data["lambdaFunction"])

    @cached_property
    def ecsService(self):  # pragma: no cover
        return EcsService.make_one(self.boto3_raw_data["ecsService"])

    @cached_property
    def ec2Instance(self):  # pragma: no cover
        return Ec2Instance.make_one(self.boto3_raw_data["ec2Instance"])

    @cached_property
    def ebsVolume(self):  # pragma: no cover
        return EbsVolume.make_one(self.boto3_raw_data["ebsVolume"])

    @cached_property
    def ec2AutoScalingGroup(self):  # pragma: no cover
        return Ec2AutoScalingGroup.make_one(self.boto3_raw_data["ec2AutoScalingGroup"])

    @cached_property
    def ec2ReservedInstances(self):  # pragma: no cover
        return Ec2ReservedInstances.make_one(
            self.boto3_raw_data["ec2ReservedInstances"]
        )

    @cached_property
    def rdsReservedInstances(self):  # pragma: no cover
        return RdsReservedInstances.make_one(
            self.boto3_raw_data["rdsReservedInstances"]
        )

    @cached_property
    def elastiCacheReservedInstances(self):  # pragma: no cover
        return ElastiCacheReservedInstances.make_one(
            self.boto3_raw_data["elastiCacheReservedInstances"]
        )

    @cached_property
    def openSearchReservedInstances(self):  # pragma: no cover
        return OpenSearchReservedInstances.make_one(
            self.boto3_raw_data["openSearchReservedInstances"]
        )

    @cached_property
    def redshiftReservedInstances(self):  # pragma: no cover
        return RedshiftReservedInstances.make_one(
            self.boto3_raw_data["redshiftReservedInstances"]
        )

    @cached_property
    def ec2InstanceSavingsPlans(self):  # pragma: no cover
        return Ec2InstanceSavingsPlans.make_one(
            self.boto3_raw_data["ec2InstanceSavingsPlans"]
        )

    @cached_property
    def computeSavingsPlans(self):  # pragma: no cover
        return ComputeSavingsPlans.make_one(self.boto3_raw_data["computeSavingsPlans"])

    @cached_property
    def sageMakerSavingsPlans(self):  # pragma: no cover
        return SageMakerSavingsPlans.make_one(
            self.boto3_raw_data["sageMakerSavingsPlans"]
        )

    @cached_property
    def rdsDbInstance(self):  # pragma: no cover
        return RdsDbInstance.make_one(self.boto3_raw_data["rdsDbInstance"])

    @cached_property
    def rdsDbInstanceStorage(self):  # pragma: no cover
        return RdsDbInstanceStorage.make_one(
            self.boto3_raw_data["rdsDbInstanceStorage"]
        )

    @cached_property
    def auroraDbClusterStorage(self):  # pragma: no cover
        return AuroraDbClusterStorage.make_one(
            self.boto3_raw_data["auroraDbClusterStorage"]
        )

    @cached_property
    def dynamoDbReservedCapacity(self):  # pragma: no cover
        return DynamoDbReservedCapacity.make_one(
            self.boto3_raw_data["dynamoDbReservedCapacity"]
        )

    @cached_property
    def memoryDbReservedInstances(self):  # pragma: no cover
        return MemoryDbReservedInstances.make_one(
            self.boto3_raw_data["memoryDbReservedInstances"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecommendationResponse:
    boto3_raw_data: "type_defs.GetRecommendationResponseTypeDef" = dataclasses.field()

    recommendationId = field("recommendationId")
    resourceId = field("resourceId")
    resourceArn = field("resourceArn")
    accountId = field("accountId")
    currencyCode = field("currencyCode")
    recommendationLookbackPeriodInDays = field("recommendationLookbackPeriodInDays")
    costCalculationLookbackPeriodInDays = field("costCalculationLookbackPeriodInDays")
    estimatedSavingsPercentage = field("estimatedSavingsPercentage")
    estimatedSavingsOverCostCalculationLookbackPeriod = field(
        "estimatedSavingsOverCostCalculationLookbackPeriod"
    )
    currentResourceType = field("currentResourceType")
    recommendedResourceType = field("recommendedResourceType")
    region = field("region")
    source = field("source")
    lastRefreshTimestamp = field("lastRefreshTimestamp")
    estimatedMonthlySavings = field("estimatedMonthlySavings")
    estimatedMonthlyCost = field("estimatedMonthlyCost")
    implementationEffort = field("implementationEffort")
    restartNeeded = field("restartNeeded")
    actionType = field("actionType")
    rollbackPossible = field("rollbackPossible")

    @cached_property
    def currentResourceDetails(self):  # pragma: no cover
        return ResourceDetails.make_one(self.boto3_raw_data["currentResourceDetails"])

    @cached_property
    def recommendedResourceDetails(self):  # pragma: no cover
        return ResourceDetails.make_one(
            self.boto3_raw_data["recommendedResourceDetails"]
        )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRecommendationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommendationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
