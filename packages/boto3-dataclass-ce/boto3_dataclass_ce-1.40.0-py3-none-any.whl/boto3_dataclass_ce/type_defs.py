# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ce import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AnomalyDateInterval:
    boto3_raw_data: "type_defs.AnomalyDateIntervalTypeDef" = dataclasses.field()

    StartDate = field("StartDate")
    EndDate = field("EndDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnomalyDateIntervalTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalyDateIntervalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyScore:
    boto3_raw_data: "type_defs.AnomalyScoreTypeDef" = dataclasses.field()

    MaxScore = field("MaxScore")
    CurrentScore = field("CurrentScore")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnomalyScoreTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnomalyScoreTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Subscriber:
    boto3_raw_data: "type_defs.SubscriberTypeDef" = dataclasses.field()

    Address = field("Address")
    Type = field("Type")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubscriberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubscriberTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Impact:
    boto3_raw_data: "type_defs.ImpactTypeDef" = dataclasses.field()

    MaxImpact = field("MaxImpact")
    TotalImpact = field("TotalImpact")
    TotalActualSpend = field("TotalActualSpend")
    TotalExpectedSpend = field("TotalExpectedSpend")
    TotalImpactPercentage = field("TotalImpactPercentage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImpactTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImpactTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComparisonMetricValue:
    boto3_raw_data: "type_defs.ComparisonMetricValueTypeDef" = dataclasses.field()

    BaselineTimePeriodAmount = field("BaselineTimePeriodAmount")
    ComparisonTimePeriodAmount = field("ComparisonTimePeriodAmount")
    Difference = field("Difference")
    Unit = field("Unit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComparisonMetricValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComparisonMetricValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostAllocationTagBackfillRequest:
    boto3_raw_data: "type_defs.CostAllocationTagBackfillRequestTypeDef" = (
        dataclasses.field()
    )

    BackfillFrom = field("BackfillFrom")
    RequestedAt = field("RequestedAt")
    CompletedAt = field("CompletedAt")
    BackfillStatus = field("BackfillStatus")
    LastUpdatedAt = field("LastUpdatedAt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CostAllocationTagBackfillRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CostAllocationTagBackfillRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostAllocationTagStatusEntry:
    boto3_raw_data: "type_defs.CostAllocationTagStatusEntryTypeDef" = (
        dataclasses.field()
    )

    TagKey = field("TagKey")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CostAllocationTagStatusEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CostAllocationTagStatusEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostAllocationTag:
    boto3_raw_data: "type_defs.CostAllocationTagTypeDef" = dataclasses.field()

    TagKey = field("TagKey")
    Type = field("Type")
    Status = field("Status")
    LastUpdatedDate = field("LastUpdatedDate")
    LastUsedDate = field("LastUsedDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CostAllocationTagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CostAllocationTagTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostCategoryInheritedValueDimension:
    boto3_raw_data: "type_defs.CostCategoryInheritedValueDimensionTypeDef" = (
        dataclasses.field()
    )

    DimensionName = field("DimensionName")
    DimensionKey = field("DimensionKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CostCategoryInheritedValueDimensionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CostCategoryInheritedValueDimensionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostCategoryProcessingStatus:
    boto3_raw_data: "type_defs.CostCategoryProcessingStatusTypeDef" = (
        dataclasses.field()
    )

    Component = field("Component")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CostCategoryProcessingStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CostCategoryProcessingStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostCategorySplitChargeRuleParameterOutput:
    boto3_raw_data: "type_defs.CostCategorySplitChargeRuleParameterOutputTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")
    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CostCategorySplitChargeRuleParameterOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CostCategorySplitChargeRuleParameterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostCategorySplitChargeRuleParameter:
    boto3_raw_data: "type_defs.CostCategorySplitChargeRuleParameterTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")
    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CostCategorySplitChargeRuleParameterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CostCategorySplitChargeRuleParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostCategoryValuesOutput:
    boto3_raw_data: "type_defs.CostCategoryValuesOutputTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")
    MatchOptions = field("MatchOptions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CostCategoryValuesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CostCategoryValuesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostCategoryValues:
    boto3_raw_data: "type_defs.CostCategoryValuesTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")
    MatchOptions = field("MatchOptions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CostCategoryValuesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CostCategoryValuesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DateInterval:
    boto3_raw_data: "type_defs.DateIntervalTypeDef" = dataclasses.field()

    Start = field("Start")
    End = field("End")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DateIntervalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DateIntervalTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoverageCost:
    boto3_raw_data: "type_defs.CoverageCostTypeDef" = dataclasses.field()

    OnDemandCost = field("OnDemandCost")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CoverageCostTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CoverageCostTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoverageHours:
    boto3_raw_data: "type_defs.CoverageHoursTypeDef" = dataclasses.field()

    OnDemandHours = field("OnDemandHours")
    ReservedHours = field("ReservedHours")
    TotalRunningHours = field("TotalRunningHours")
    CoverageHoursPercentage = field("CoverageHoursPercentage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CoverageHoursTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CoverageHoursTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoverageNormalizedUnits:
    boto3_raw_data: "type_defs.CoverageNormalizedUnitsTypeDef" = dataclasses.field()

    OnDemandNormalizedUnits = field("OnDemandNormalizedUnits")
    ReservedNormalizedUnits = field("ReservedNormalizedUnits")
    TotalRunningNormalizedUnits = field("TotalRunningNormalizedUnits")
    CoverageNormalizedUnitsPercentage = field("CoverageNormalizedUnitsPercentage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoverageNormalizedUnitsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoverageNormalizedUnitsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceTag:
    boto3_raw_data: "type_defs.ResourceTagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTagTypeDef"]]
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
class TagValuesOutput:
    boto3_raw_data: "type_defs.TagValuesOutputTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")
    MatchOptions = field("MatchOptions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagValuesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagValuesOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAnomalyMonitorRequest:
    boto3_raw_data: "type_defs.DeleteAnomalyMonitorRequestTypeDef" = dataclasses.field()

    MonitorArn = field("MonitorArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAnomalyMonitorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAnomalyMonitorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAnomalySubscriptionRequest:
    boto3_raw_data: "type_defs.DeleteAnomalySubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    SubscriptionArn = field("SubscriptionArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteAnomalySubscriptionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAnomalySubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCostCategoryDefinitionRequest:
    boto3_raw_data: "type_defs.DeleteCostCategoryDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    CostCategoryArn = field("CostCategoryArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCostCategoryDefinitionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCostCategoryDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCostCategoryDefinitionRequest:
    boto3_raw_data: "type_defs.DescribeCostCategoryDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    CostCategoryArn = field("CostCategoryArn")
    EffectiveOn = field("EffectiveOn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCostCategoryDefinitionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCostCategoryDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DimensionValuesOutput:
    boto3_raw_data: "type_defs.DimensionValuesOutputTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")
    MatchOptions = field("MatchOptions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DimensionValuesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DimensionValuesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DimensionValues:
    boto3_raw_data: "type_defs.DimensionValuesTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")
    MatchOptions = field("MatchOptions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DimensionValuesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DimensionValuesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DimensionValuesWithAttributes:
    boto3_raw_data: "type_defs.DimensionValuesWithAttributesTypeDef" = (
        dataclasses.field()
    )

    Value = field("Value")
    Attributes = field("Attributes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DimensionValuesWithAttributesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DimensionValuesWithAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DiskResourceUtilization:
    boto3_raw_data: "type_defs.DiskResourceUtilizationTypeDef" = dataclasses.field()

    DiskReadOpsPerSecond = field("DiskReadOpsPerSecond")
    DiskWriteOpsPerSecond = field("DiskWriteOpsPerSecond")
    DiskReadBytesPerSecond = field("DiskReadBytesPerSecond")
    DiskWriteBytesPerSecond = field("DiskWriteBytesPerSecond")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DiskResourceUtilizationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DiskResourceUtilizationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DynamoDBCapacityDetails:
    boto3_raw_data: "type_defs.DynamoDBCapacityDetailsTypeDef" = dataclasses.field()

    CapacityUnits = field("CapacityUnits")
    Region = field("Region")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DynamoDBCapacityDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DynamoDBCapacityDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EBSResourceUtilization:
    boto3_raw_data: "type_defs.EBSResourceUtilizationTypeDef" = dataclasses.field()

    EbsReadOpsPerSecond = field("EbsReadOpsPerSecond")
    EbsWriteOpsPerSecond = field("EbsWriteOpsPerSecond")
    EbsReadBytesPerSecond = field("EbsReadBytesPerSecond")
    EbsWriteBytesPerSecond = field("EbsWriteBytesPerSecond")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EBSResourceUtilizationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EBSResourceUtilizationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EC2InstanceDetails:
    boto3_raw_data: "type_defs.EC2InstanceDetailsTypeDef" = dataclasses.field()

    Family = field("Family")
    InstanceType = field("InstanceType")
    Region = field("Region")
    AvailabilityZone = field("AvailabilityZone")
    Platform = field("Platform")
    Tenancy = field("Tenancy")
    CurrentGeneration = field("CurrentGeneration")
    SizeFlexEligible = field("SizeFlexEligible")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EC2InstanceDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EC2InstanceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EC2ResourceDetails:
    boto3_raw_data: "type_defs.EC2ResourceDetailsTypeDef" = dataclasses.field()

    HourlyOnDemandRate = field("HourlyOnDemandRate")
    InstanceType = field("InstanceType")
    Platform = field("Platform")
    Region = field("Region")
    Sku = field("Sku")
    Memory = field("Memory")
    NetworkPerformance = field("NetworkPerformance")
    Storage = field("Storage")
    Vcpu = field("Vcpu")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EC2ResourceDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EC2ResourceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkResourceUtilization:
    boto3_raw_data: "type_defs.NetworkResourceUtilizationTypeDef" = dataclasses.field()

    NetworkInBytesPerSecond = field("NetworkInBytesPerSecond")
    NetworkOutBytesPerSecond = field("NetworkOutBytesPerSecond")
    NetworkPacketsInPerSecond = field("NetworkPacketsInPerSecond")
    NetworkPacketsOutPerSecond = field("NetworkPacketsOutPerSecond")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkResourceUtilizationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkResourceUtilizationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EC2Specification:
    boto3_raw_data: "type_defs.EC2SpecificationTypeDef" = dataclasses.field()

    OfferingClass = field("OfferingClass")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EC2SpecificationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EC2SpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ESInstanceDetails:
    boto3_raw_data: "type_defs.ESInstanceDetailsTypeDef" = dataclasses.field()

    InstanceClass = field("InstanceClass")
    InstanceSize = field("InstanceSize")
    Region = field("Region")
    CurrentGeneration = field("CurrentGeneration")
    SizeFlexEligible = field("SizeFlexEligible")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ESInstanceDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ESInstanceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElastiCacheInstanceDetails:
    boto3_raw_data: "type_defs.ElastiCacheInstanceDetailsTypeDef" = dataclasses.field()

    Family = field("Family")
    NodeType = field("NodeType")
    Region = field("Region")
    ProductDescription = field("ProductDescription")
    CurrentGeneration = field("CurrentGeneration")
    SizeFlexEligible = field("SizeFlexEligible")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ElastiCacheInstanceDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ElastiCacheInstanceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagValues:
    boto3_raw_data: "type_defs.TagValuesTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")
    MatchOptions = field("MatchOptions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagValuesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagValuesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerationSummary:
    boto3_raw_data: "type_defs.GenerationSummaryTypeDef" = dataclasses.field()

    RecommendationId = field("RecommendationId")
    GenerationStatus = field("GenerationStatus")
    GenerationStartedTime = field("GenerationStartedTime")
    GenerationCompletionTime = field("GenerationCompletionTime")
    EstimatedCompletionTime = field("EstimatedCompletionTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GenerationSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerationSummaryTypeDef"]
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
class TotalImpactFilter:
    boto3_raw_data: "type_defs.TotalImpactFilterTypeDef" = dataclasses.field()

    NumericOperator = field("NumericOperator")
    StartValue = field("StartValue")
    EndValue = field("EndValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TotalImpactFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TotalImpactFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnomalyMonitorsRequest:
    boto3_raw_data: "type_defs.GetAnomalyMonitorsRequestTypeDef" = dataclasses.field()

    MonitorArnList = field("MonitorArnList")
    NextPageToken = field("NextPageToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAnomalyMonitorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnomalyMonitorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnomalySubscriptionsRequest:
    boto3_raw_data: "type_defs.GetAnomalySubscriptionsRequestTypeDef" = (
        dataclasses.field()
    )

    SubscriptionArnList = field("SubscriptionArnList")
    MonitorArn = field("MonitorArn")
    NextPageToken = field("NextPageToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAnomalySubscriptionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnomalySubscriptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApproximateUsageRecordsRequest:
    boto3_raw_data: "type_defs.GetApproximateUsageRecordsRequestTypeDef" = (
        dataclasses.field()
    )

    Granularity = field("Granularity")
    ApproximationDimension = field("ApproximationDimension")
    Services = field("Services")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetApproximateUsageRecordsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApproximateUsageRecordsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCommitmentPurchaseAnalysisRequest:
    boto3_raw_data: "type_defs.GetCommitmentPurchaseAnalysisRequestTypeDef" = (
        dataclasses.field()
    )

    AnalysisId = field("AnalysisId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCommitmentPurchaseAnalysisRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCommitmentPurchaseAnalysisRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupDefinition:
    boto3_raw_data: "type_defs.GroupDefinitionTypeDef" = dataclasses.field()

    Type = field("Type")
    Key = field("Key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupDefinitionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SortDefinition:
    boto3_raw_data: "type_defs.SortDefinitionTypeDef" = dataclasses.field()

    Key = field("Key")
    SortOrder = field("SortOrder")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SortDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SortDefinitionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricValue:
    boto3_raw_data: "type_defs.MetricValueTypeDef" = dataclasses.field()

    Amount = field("Amount")
    Unit = field("Unit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricValueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservationPurchaseRecommendationMetadata:
    boto3_raw_data: "type_defs.ReservationPurchaseRecommendationMetadataTypeDef" = (
        dataclasses.field()
    )

    RecommendationId = field("RecommendationId")
    GenerationTimestamp = field("GenerationTimestamp")
    AdditionalMetadata = field("AdditionalMetadata")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReservationPurchaseRecommendationMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservationPurchaseRecommendationMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservationAggregates:
    boto3_raw_data: "type_defs.ReservationAggregatesTypeDef" = dataclasses.field()

    UtilizationPercentage = field("UtilizationPercentage")
    UtilizationPercentageInUnits = field("UtilizationPercentageInUnits")
    PurchasedHours = field("PurchasedHours")
    PurchasedUnits = field("PurchasedUnits")
    TotalActualHours = field("TotalActualHours")
    TotalActualUnits = field("TotalActualUnits")
    UnusedHours = field("UnusedHours")
    UnusedUnits = field("UnusedUnits")
    OnDemandCostOfRIHoursUsed = field("OnDemandCostOfRIHoursUsed")
    NetRISavings = field("NetRISavings")
    TotalPotentialRISavings = field("TotalPotentialRISavings")
    AmortizedUpfrontFee = field("AmortizedUpfrontFee")
    AmortizedRecurringFee = field("AmortizedRecurringFee")
    TotalAmortizedFee = field("TotalAmortizedFee")
    RICostForUnusedHours = field("RICostForUnusedHours")
    RealizedSavings = field("RealizedSavings")
    UnrealizedSavings = field("UnrealizedSavings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReservationAggregatesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservationAggregatesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RightsizingRecommendationConfiguration:
    boto3_raw_data: "type_defs.RightsizingRecommendationConfigurationTypeDef" = (
        dataclasses.field()
    )

    RecommendationTarget = field("RecommendationTarget")
    BenefitsConsidered = field("BenefitsConsidered")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RightsizingRecommendationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RightsizingRecommendationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RightsizingRecommendationMetadata:
    boto3_raw_data: "type_defs.RightsizingRecommendationMetadataTypeDef" = (
        dataclasses.field()
    )

    RecommendationId = field("RecommendationId")
    GenerationTimestamp = field("GenerationTimestamp")
    LookbackPeriodInDays = field("LookbackPeriodInDays")
    AdditionalMetadata = field("AdditionalMetadata")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RightsizingRecommendationMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RightsizingRecommendationMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RightsizingRecommendationSummary:
    boto3_raw_data: "type_defs.RightsizingRecommendationSummaryTypeDef" = (
        dataclasses.field()
    )

    TotalRecommendationCount = field("TotalRecommendationCount")
    EstimatedTotalMonthlySavingsAmount = field("EstimatedTotalMonthlySavingsAmount")
    SavingsCurrencyCode = field("SavingsCurrencyCode")
    SavingsPercentage = field("SavingsPercentage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RightsizingRecommendationSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RightsizingRecommendationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSavingsPlanPurchaseRecommendationDetailsRequest:
    boto3_raw_data: (
        "type_defs.GetSavingsPlanPurchaseRecommendationDetailsRequestTypeDef"
    ) = dataclasses.field()

    RecommendationDetailId = field("RecommendationDetailId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSavingsPlanPurchaseRecommendationDetailsRequestTypeDef"
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
                "type_defs.GetSavingsPlanPurchaseRecommendationDetailsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlansPurchaseRecommendationMetadata:
    boto3_raw_data: "type_defs.SavingsPlansPurchaseRecommendationMetadataTypeDef" = (
        dataclasses.field()
    )

    RecommendationId = field("RecommendationId")
    GenerationTimestamp = field("GenerationTimestamp")
    AdditionalMetadata = field("AdditionalMetadata")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SavingsPlansPurchaseRecommendationMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlansPurchaseRecommendationMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemoryDBInstanceDetails:
    boto3_raw_data: "type_defs.MemoryDBInstanceDetailsTypeDef" = dataclasses.field()

    Family = field("Family")
    NodeType = field("NodeType")
    Region = field("Region")
    CurrentGeneration = field("CurrentGeneration")
    SizeFlexEligible = field("SizeFlexEligible")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MemoryDBInstanceDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemoryDBInstanceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RDSInstanceDetails:
    boto3_raw_data: "type_defs.RDSInstanceDetailsTypeDef" = dataclasses.field()

    Family = field("Family")
    InstanceType = field("InstanceType")
    Region = field("Region")
    DatabaseEngine = field("DatabaseEngine")
    DatabaseEdition = field("DatabaseEdition")
    DeploymentOption = field("DeploymentOption")
    LicenseModel = field("LicenseModel")
    CurrentGeneration = field("CurrentGeneration")
    SizeFlexEligible = field("SizeFlexEligible")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RDSInstanceDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RDSInstanceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftInstanceDetails:
    boto3_raw_data: "type_defs.RedshiftInstanceDetailsTypeDef" = dataclasses.field()

    Family = field("Family")
    NodeType = field("NodeType")
    Region = field("Region")
    CurrentGeneration = field("CurrentGeneration")
    SizeFlexEligible = field("SizeFlexEligible")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedshiftInstanceDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftInstanceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCommitmentPurchaseAnalysesRequest:
    boto3_raw_data: "type_defs.ListCommitmentPurchaseAnalysesRequestTypeDef" = (
        dataclasses.field()
    )

    AnalysisStatus = field("AnalysisStatus")
    NextPageToken = field("NextPageToken")
    PageSize = field("PageSize")
    AnalysisIds = field("AnalysisIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCommitmentPurchaseAnalysesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCommitmentPurchaseAnalysesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCostAllocationTagBackfillHistoryRequest:
    boto3_raw_data: "type_defs.ListCostAllocationTagBackfillHistoryRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCostAllocationTagBackfillHistoryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCostAllocationTagBackfillHistoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCostAllocationTagsRequest:
    boto3_raw_data: "type_defs.ListCostAllocationTagsRequestTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    TagKeys = field("TagKeys")
    Type = field("Type")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCostAllocationTagsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCostAllocationTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCostCategoryDefinitionsRequest:
    boto3_raw_data: "type_defs.ListCostCategoryDefinitionsRequestTypeDef" = (
        dataclasses.field()
    )

    EffectiveOn = field("EffectiveOn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCostCategoryDefinitionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCostCategoryDefinitionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSavingsPlansPurchaseRecommendationGenerationRequest:
    boto3_raw_data: (
        "type_defs.ListSavingsPlansPurchaseRecommendationGenerationRequestTypeDef"
    ) = dataclasses.field()

    GenerationStatus = field("GenerationStatus")
    RecommendationIds = field("RecommendationIds")
    PageSize = field("PageSize")
    NextPageToken = field("NextPageToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSavingsPlansPurchaseRecommendationGenerationRequestTypeDef"
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
                "type_defs.ListSavingsPlansPurchaseRecommendationGenerationRequestTypeDef"
            ]
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

    ResourceArn = field("ResourceArn")

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
class ProvideAnomalyFeedbackRequest:
    boto3_raw_data: "type_defs.ProvideAnomalyFeedbackRequestTypeDef" = (
        dataclasses.field()
    )

    AnomalyId = field("AnomalyId")
    Feedback = field("Feedback")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProvideAnomalyFeedbackRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvideAnomalyFeedbackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationDetailHourlyMetrics:
    boto3_raw_data: "type_defs.RecommendationDetailHourlyMetricsTypeDef" = (
        dataclasses.field()
    )

    StartTime = field("StartTime")
    EstimatedOnDemandCost = field("EstimatedOnDemandCost")
    CurrentCoverage = field("CurrentCoverage")
    EstimatedCoverage = field("EstimatedCoverage")
    EstimatedNewCommitmentUtilization = field("EstimatedNewCommitmentUtilization")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RecommendationDetailHourlyMetricsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationDetailHourlyMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservationPurchaseRecommendationSummary:
    boto3_raw_data: "type_defs.ReservationPurchaseRecommendationSummaryTypeDef" = (
        dataclasses.field()
    )

    TotalEstimatedMonthlySavingsAmount = field("TotalEstimatedMonthlySavingsAmount")
    TotalEstimatedMonthlySavingsPercentage = field(
        "TotalEstimatedMonthlySavingsPercentage"
    )
    CurrencyCode = field("CurrencyCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReservationPurchaseRecommendationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservationPurchaseRecommendationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateRecommendationDetail:
    boto3_raw_data: "type_defs.TerminateRecommendationDetailTypeDef" = (
        dataclasses.field()
    )

    EstimatedMonthlySavings = field("EstimatedMonthlySavings")
    CurrencyCode = field("CurrencyCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TerminateRecommendationDetailTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateRecommendationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RootCauseImpact:
    boto3_raw_data: "type_defs.RootCauseImpactTypeDef" = dataclasses.field()

    Contribution = field("Contribution")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RootCauseImpactTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RootCauseImpactTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlansAmortizedCommitment:
    boto3_raw_data: "type_defs.SavingsPlansAmortizedCommitmentTypeDef" = (
        dataclasses.field()
    )

    AmortizedRecurringCommitment = field("AmortizedRecurringCommitment")
    AmortizedUpfrontCommitment = field("AmortizedUpfrontCommitment")
    TotalAmortizedCommitment = field("TotalAmortizedCommitment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SavingsPlansAmortizedCommitmentTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlansAmortizedCommitmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlansCoverageData:
    boto3_raw_data: "type_defs.SavingsPlansCoverageDataTypeDef" = dataclasses.field()

    SpendCoveredBySavingsPlans = field("SpendCoveredBySavingsPlans")
    OnDemandCost = field("OnDemandCost")
    TotalCost = field("TotalCost")
    CoveragePercentage = field("CoveragePercentage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SavingsPlansCoverageDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlansCoverageDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlansDetails:
    boto3_raw_data: "type_defs.SavingsPlansDetailsTypeDef" = dataclasses.field()

    Region = field("Region")
    InstanceFamily = field("InstanceFamily")
    OfferingId = field("OfferingId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SavingsPlansDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlansDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlans:
    boto3_raw_data: "type_defs.SavingsPlansTypeDef" = dataclasses.field()

    PaymentOption = field("PaymentOption")
    SavingsPlansType = field("SavingsPlansType")
    Region = field("Region")
    InstanceFamily = field("InstanceFamily")
    TermInYears = field("TermInYears")
    SavingsPlansCommitment = field("SavingsPlansCommitment")
    OfferingId = field("OfferingId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SavingsPlansTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SavingsPlansTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlansPurchaseRecommendationSummary:
    boto3_raw_data: "type_defs.SavingsPlansPurchaseRecommendationSummaryTypeDef" = (
        dataclasses.field()
    )

    EstimatedROI = field("EstimatedROI")
    CurrencyCode = field("CurrencyCode")
    EstimatedTotalCost = field("EstimatedTotalCost")
    CurrentOnDemandSpend = field("CurrentOnDemandSpend")
    EstimatedSavingsAmount = field("EstimatedSavingsAmount")
    TotalRecommendationCount = field("TotalRecommendationCount")
    DailyCommitmentToPurchase = field("DailyCommitmentToPurchase")
    HourlyCommitmentToPurchase = field("HourlyCommitmentToPurchase")
    EstimatedSavingsPercentage = field("EstimatedSavingsPercentage")
    EstimatedMonthlySavingsAmount = field("EstimatedMonthlySavingsAmount")
    EstimatedOnDemandCostWithCurrentCommitment = field(
        "EstimatedOnDemandCostWithCurrentCommitment"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SavingsPlansPurchaseRecommendationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlansPurchaseRecommendationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlansSavings:
    boto3_raw_data: "type_defs.SavingsPlansSavingsTypeDef" = dataclasses.field()

    NetSavings = field("NetSavings")
    OnDemandCostEquivalent = field("OnDemandCostEquivalent")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SavingsPlansSavingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlansSavingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlansUtilization:
    boto3_raw_data: "type_defs.SavingsPlansUtilizationTypeDef" = dataclasses.field()

    TotalCommitment = field("TotalCommitment")
    UsedCommitment = field("UsedCommitment")
    UnusedCommitment = field("UnusedCommitment")
    UtilizationPercentage = field("UtilizationPercentage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SavingsPlansUtilizationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlansUtilizationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCostAllocationTagBackfillRequest:
    boto3_raw_data: "type_defs.StartCostAllocationTagBackfillRequestTypeDef" = (
        dataclasses.field()
    )

    BackfillFrom = field("BackfillFrom")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartCostAllocationTagBackfillRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCostAllocationTagBackfillRequestTypeDef"]
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

    ResourceArn = field("ResourceArn")
    ResourceTagKeys = field("ResourceTagKeys")

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
class UpdateAnomalyMonitorRequest:
    boto3_raw_data: "type_defs.UpdateAnomalyMonitorRequestTypeDef" = dataclasses.field()

    MonitorArn = field("MonitorArn")
    MonitorName = field("MonitorName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAnomalyMonitorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAnomalyMonitorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCostAllocationTagsStatusError:
    boto3_raw_data: "type_defs.UpdateCostAllocationTagsStatusErrorTypeDef" = (
        dataclasses.field()
    )

    TagKey = field("TagKey")
    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCostAllocationTagsStatusErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCostAllocationTagsStatusErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostDriver:
    boto3_raw_data: "type_defs.CostDriverTypeDef" = dataclasses.field()

    Type = field("Type")
    Name = field("Name")
    Metrics = field("Metrics")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CostDriverTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CostDriverTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCostAllocationTagsStatusRequest:
    boto3_raw_data: "type_defs.UpdateCostAllocationTagsStatusRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CostAllocationTagsStatus(self):  # pragma: no cover
        return CostAllocationTagStatusEntry.make_many(
            self.boto3_raw_data["CostAllocationTagsStatus"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCostAllocationTagsStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCostAllocationTagsStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostCategoryReference:
    boto3_raw_data: "type_defs.CostCategoryReferenceTypeDef" = dataclasses.field()

    CostCategoryArn = field("CostCategoryArn")
    Name = field("Name")
    EffectiveStart = field("EffectiveStart")
    EffectiveEnd = field("EffectiveEnd")
    NumberOfRules = field("NumberOfRules")

    @cached_property
    def ProcessingStatus(self):  # pragma: no cover
        return CostCategoryProcessingStatus.make_many(
            self.boto3_raw_data["ProcessingStatus"]
        )

    Values = field("Values")
    DefaultValue = field("DefaultValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CostCategoryReferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CostCategoryReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostCategorySplitChargeRuleOutput:
    boto3_raw_data: "type_defs.CostCategorySplitChargeRuleOutputTypeDef" = (
        dataclasses.field()
    )

    Source = field("Source")
    Targets = field("Targets")
    Method = field("Method")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return CostCategorySplitChargeRuleParameterOutput.make_many(
            self.boto3_raw_data["Parameters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CostCategorySplitChargeRuleOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CostCategorySplitChargeRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ForecastResult:
    boto3_raw_data: "type_defs.ForecastResultTypeDef" = dataclasses.field()

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["TimePeriod"])

    MeanValue = field("MeanValue")
    PredictionIntervalLowerBound = field("PredictionIntervalLowerBound")
    PredictionIntervalUpperBound = field("PredictionIntervalUpperBound")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ForecastResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ForecastResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Coverage:
    boto3_raw_data: "type_defs.CoverageTypeDef" = dataclasses.field()

    @cached_property
    def CoverageHours(self):  # pragma: no cover
        return CoverageHours.make_one(self.boto3_raw_data["CoverageHours"])

    @cached_property
    def CoverageNormalizedUnits(self):  # pragma: no cover
        return CoverageNormalizedUnits.make_one(
            self.boto3_raw_data["CoverageNormalizedUnits"]
        )

    @cached_property
    def CoverageCost(self):  # pragma: no cover
        return CoverageCost.make_one(self.boto3_raw_data["CoverageCost"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CoverageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CoverageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ResourceTags"])

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
class CreateAnomalyMonitorResponse:
    boto3_raw_data: "type_defs.CreateAnomalyMonitorResponseTypeDef" = (
        dataclasses.field()
    )

    MonitorArn = field("MonitorArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAnomalyMonitorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAnomalyMonitorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAnomalySubscriptionResponse:
    boto3_raw_data: "type_defs.CreateAnomalySubscriptionResponseTypeDef" = (
        dataclasses.field()
    )

    SubscriptionArn = field("SubscriptionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAnomalySubscriptionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAnomalySubscriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCostCategoryDefinitionResponse:
    boto3_raw_data: "type_defs.CreateCostCategoryDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    CostCategoryArn = field("CostCategoryArn")
    EffectiveStart = field("EffectiveStart")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCostCategoryDefinitionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCostCategoryDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCostCategoryDefinitionResponse:
    boto3_raw_data: "type_defs.DeleteCostCategoryDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    CostCategoryArn = field("CostCategoryArn")
    EffectiveEnd = field("EffectiveEnd")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCostCategoryDefinitionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCostCategoryDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApproximateUsageRecordsResponse:
    boto3_raw_data: "type_defs.GetApproximateUsageRecordsResponseTypeDef" = (
        dataclasses.field()
    )

    Services = field("Services")
    TotalRecords = field("TotalRecords")

    @cached_property
    def LookbackPeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["LookbackPeriod"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetApproximateUsageRecordsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApproximateUsageRecordsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCostCategoriesResponse:
    boto3_raw_data: "type_defs.GetCostCategoriesResponseTypeDef" = dataclasses.field()

    NextPageToken = field("NextPageToken")
    CostCategoryNames = field("CostCategoryNames")
    CostCategoryValues = field("CostCategoryValues")
    ReturnSize = field("ReturnSize")
    TotalSize = field("TotalSize")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCostCategoriesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCostCategoriesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTagsResponse:
    boto3_raw_data: "type_defs.GetTagsResponseTypeDef" = dataclasses.field()

    NextPageToken = field("NextPageToken")
    Tags = field("Tags")
    ReturnSize = field("ReturnSize")
    TotalSize = field("TotalSize")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTagsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetTagsResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCostAllocationTagBackfillHistoryResponse:
    boto3_raw_data: "type_defs.ListCostAllocationTagBackfillHistoryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BackfillRequests(self):  # pragma: no cover
        return CostAllocationTagBackfillRequest.make_many(
            self.boto3_raw_data["BackfillRequests"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCostAllocationTagBackfillHistoryResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCostAllocationTagBackfillHistoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCostAllocationTagsResponse:
    boto3_raw_data: "type_defs.ListCostAllocationTagsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CostAllocationTags(self):  # pragma: no cover
        return CostAllocationTag.make_many(self.boto3_raw_data["CostAllocationTags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCostAllocationTagsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCostAllocationTagsResponseTypeDef"]
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
    def ResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ResourceTags"])

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
class ProvideAnomalyFeedbackResponse:
    boto3_raw_data: "type_defs.ProvideAnomalyFeedbackResponseTypeDef" = (
        dataclasses.field()
    )

    AnomalyId = field("AnomalyId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProvideAnomalyFeedbackResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvideAnomalyFeedbackResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCommitmentPurchaseAnalysisResponse:
    boto3_raw_data: "type_defs.StartCommitmentPurchaseAnalysisResponseTypeDef" = (
        dataclasses.field()
    )

    AnalysisId = field("AnalysisId")
    AnalysisStartedTime = field("AnalysisStartedTime")
    EstimatedCompletionTime = field("EstimatedCompletionTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartCommitmentPurchaseAnalysisResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCommitmentPurchaseAnalysisResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCostAllocationTagBackfillResponse:
    boto3_raw_data: "type_defs.StartCostAllocationTagBackfillResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BackfillRequest(self):  # pragma: no cover
        return CostAllocationTagBackfillRequest.make_one(
            self.boto3_raw_data["BackfillRequest"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartCostAllocationTagBackfillResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCostAllocationTagBackfillResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSavingsPlansPurchaseRecommendationGenerationResponse:
    boto3_raw_data: (
        "type_defs.StartSavingsPlansPurchaseRecommendationGenerationResponseTypeDef"
    ) = dataclasses.field()

    RecommendationId = field("RecommendationId")
    GenerationStartedTime = field("GenerationStartedTime")
    EstimatedCompletionTime = field("EstimatedCompletionTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartSavingsPlansPurchaseRecommendationGenerationResponseTypeDef"
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
                "type_defs.StartSavingsPlansPurchaseRecommendationGenerationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAnomalyMonitorResponse:
    boto3_raw_data: "type_defs.UpdateAnomalyMonitorResponseTypeDef" = (
        dataclasses.field()
    )

    MonitorArn = field("MonitorArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAnomalyMonitorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAnomalyMonitorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAnomalySubscriptionResponse:
    boto3_raw_data: "type_defs.UpdateAnomalySubscriptionResponseTypeDef" = (
        dataclasses.field()
    )

    SubscriptionArn = field("SubscriptionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAnomalySubscriptionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAnomalySubscriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCostCategoryDefinitionResponse:
    boto3_raw_data: "type_defs.UpdateCostCategoryDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    CostCategoryArn = field("CostCategoryArn")
    EffectiveStart = field("EffectiveStart")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCostCategoryDefinitionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCostCategoryDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpressionOutput:
    boto3_raw_data: "type_defs.ExpressionOutputTypeDef" = dataclasses.field()

    Or = field("Or")
    And = field("And")
    Not = field("Not")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return DimensionValuesOutput.make_one(self.boto3_raw_data["Dimensions"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagValuesOutput.make_one(self.boto3_raw_data["Tags"])

    @cached_property
    def CostCategories(self):  # pragma: no cover
        return CostCategoryValuesOutput.make_one(self.boto3_raw_data["CostCategories"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExpressionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpressionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpressionPaginatorOutput:
    boto3_raw_data: "type_defs.ExpressionPaginatorOutputTypeDef" = dataclasses.field()

    Or = field("Or")
    And = field("And")
    Not = field("Not")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return DimensionValuesOutput.make_one(self.boto3_raw_data["Dimensions"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagValuesOutput.make_one(self.boto3_raw_data["Tags"])

    @cached_property
    def CostCategories(self):  # pragma: no cover
        return CostCategoryValuesOutput.make_one(self.boto3_raw_data["CostCategories"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExpressionPaginatorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpressionPaginatorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDimensionValuesResponse:
    boto3_raw_data: "type_defs.GetDimensionValuesResponseTypeDef" = dataclasses.field()

    @cached_property
    def DimensionValues(self):  # pragma: no cover
        return DimensionValuesWithAttributes.make_many(
            self.boto3_raw_data["DimensionValues"]
        )

    ReturnSize = field("ReturnSize")
    TotalSize = field("TotalSize")
    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDimensionValuesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDimensionValuesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservedCapacityDetails:
    boto3_raw_data: "type_defs.ReservedCapacityDetailsTypeDef" = dataclasses.field()

    @cached_property
    def DynamoDBCapacityDetails(self):  # pragma: no cover
        return DynamoDBCapacityDetails.make_one(
            self.boto3_raw_data["DynamoDBCapacityDetails"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReservedCapacityDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservedCapacityDetailsTypeDef"]
        ],
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
    def EC2ResourceDetails(self):  # pragma: no cover
        return EC2ResourceDetails.make_one(self.boto3_raw_data["EC2ResourceDetails"])

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
class EC2ResourceUtilization:
    boto3_raw_data: "type_defs.EC2ResourceUtilizationTypeDef" = dataclasses.field()

    MaxCpuUtilizationPercentage = field("MaxCpuUtilizationPercentage")
    MaxMemoryUtilizationPercentage = field("MaxMemoryUtilizationPercentage")
    MaxStorageUtilizationPercentage = field("MaxStorageUtilizationPercentage")

    @cached_property
    def EBSResourceUtilization(self):  # pragma: no cover
        return EBSResourceUtilization.make_one(
            self.boto3_raw_data["EBSResourceUtilization"]
        )

    @cached_property
    def DiskResourceUtilization(self):  # pragma: no cover
        return DiskResourceUtilization.make_one(
            self.boto3_raw_data["DiskResourceUtilization"]
        )

    @cached_property
    def NetworkResourceUtilization(self):  # pragma: no cover
        return NetworkResourceUtilization.make_one(
            self.boto3_raw_data["NetworkResourceUtilization"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EC2ResourceUtilizationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EC2ResourceUtilizationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceSpecification:
    boto3_raw_data: "type_defs.ServiceSpecificationTypeDef" = dataclasses.field()

    @cached_property
    def EC2Specification(self):  # pragma: no cover
        return EC2Specification.make_one(self.boto3_raw_data["EC2Specification"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpressionPaginator:
    boto3_raw_data: "type_defs.ExpressionPaginatorTypeDef" = dataclasses.field()

    Or = field("Or")
    And = field("And")
    Not = field("Not")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return DimensionValues.make_one(self.boto3_raw_data["Dimensions"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagValues.make_one(self.boto3_raw_data["Tags"])

    @cached_property
    def CostCategories(self):  # pragma: no cover
        return CostCategoryValues.make_one(self.boto3_raw_data["CostCategories"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExpressionPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpressionPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSavingsPlansPurchaseRecommendationGenerationResponse:
    boto3_raw_data: (
        "type_defs.ListSavingsPlansPurchaseRecommendationGenerationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def GenerationSummaryList(self):  # pragma: no cover
        return GenerationSummary.make_many(self.boto3_raw_data["GenerationSummaryList"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSavingsPlansPurchaseRecommendationGenerationResponseTypeDef"
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
                "type_defs.ListSavingsPlansPurchaseRecommendationGenerationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnomalyMonitorsRequestPaginate:
    boto3_raw_data: "type_defs.GetAnomalyMonitorsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    MonitorArnList = field("MonitorArnList")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAnomalyMonitorsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnomalyMonitorsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnomalySubscriptionsRequestPaginate:
    boto3_raw_data: "type_defs.GetAnomalySubscriptionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    SubscriptionArnList = field("SubscriptionArnList")
    MonitorArn = field("MonitorArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAnomalySubscriptionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnomalySubscriptionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnomaliesRequestPaginate:
    boto3_raw_data: "type_defs.GetAnomaliesRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def DateInterval(self):  # pragma: no cover
        return AnomalyDateInterval.make_one(self.boto3_raw_data["DateInterval"])

    MonitorArn = field("MonitorArn")
    Feedback = field("Feedback")

    @cached_property
    def TotalImpact(self):  # pragma: no cover
        return TotalImpactFilter.make_one(self.boto3_raw_data["TotalImpact"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAnomaliesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnomaliesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnomaliesRequest:
    boto3_raw_data: "type_defs.GetAnomaliesRequestTypeDef" = dataclasses.field()

    @cached_property
    def DateInterval(self):  # pragma: no cover
        return AnomalyDateInterval.make_one(self.boto3_raw_data["DateInterval"])

    MonitorArn = field("MonitorArn")
    Feedback = field("Feedback")

    @cached_property
    def TotalImpact(self):  # pragma: no cover
        return TotalImpactFilter.make_one(self.boto3_raw_data["TotalImpact"])

    NextPageToken = field("NextPageToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAnomaliesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnomaliesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Group:
    boto3_raw_data: "type_defs.GroupTypeDef" = dataclasses.field()

    Keys = field("Keys")
    Metrics = field("Metrics")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservationUtilizationGroup:
    boto3_raw_data: "type_defs.ReservationUtilizationGroupTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")
    Attributes = field("Attributes")

    @cached_property
    def Utilization(self):  # pragma: no cover
        return ReservationAggregates.make_one(self.boto3_raw_data["Utilization"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReservationUtilizationGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservationUtilizationGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceDetails:
    boto3_raw_data: "type_defs.InstanceDetailsTypeDef" = dataclasses.field()

    @cached_property
    def EC2InstanceDetails(self):  # pragma: no cover
        return EC2InstanceDetails.make_one(self.boto3_raw_data["EC2InstanceDetails"])

    @cached_property
    def RDSInstanceDetails(self):  # pragma: no cover
        return RDSInstanceDetails.make_one(self.boto3_raw_data["RDSInstanceDetails"])

    @cached_property
    def RedshiftInstanceDetails(self):  # pragma: no cover
        return RedshiftInstanceDetails.make_one(
            self.boto3_raw_data["RedshiftInstanceDetails"]
        )

    @cached_property
    def ElastiCacheInstanceDetails(self):  # pragma: no cover
        return ElastiCacheInstanceDetails.make_one(
            self.boto3_raw_data["ElastiCacheInstanceDetails"]
        )

    @cached_property
    def ESInstanceDetails(self):  # pragma: no cover
        return ESInstanceDetails.make_one(self.boto3_raw_data["ESInstanceDetails"])

    @cached_property
    def MemoryDBInstanceDetails(self):  # pragma: no cover
        return MemoryDBInstanceDetails.make_one(
            self.boto3_raw_data["MemoryDBInstanceDetails"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationDetailData:
    boto3_raw_data: "type_defs.RecommendationDetailDataTypeDef" = dataclasses.field()

    AccountScope = field("AccountScope")
    LookbackPeriodInDays = field("LookbackPeriodInDays")
    SavingsPlansType = field("SavingsPlansType")
    TermInYears = field("TermInYears")
    PaymentOption = field("PaymentOption")
    AccountId = field("AccountId")
    CurrencyCode = field("CurrencyCode")
    InstanceFamily = field("InstanceFamily")
    Region = field("Region")
    OfferingId = field("OfferingId")
    GenerationTimestamp = field("GenerationTimestamp")
    LatestUsageTimestamp = field("LatestUsageTimestamp")
    CurrentAverageHourlyOnDemandSpend = field("CurrentAverageHourlyOnDemandSpend")
    CurrentMaximumHourlyOnDemandSpend = field("CurrentMaximumHourlyOnDemandSpend")
    CurrentMinimumHourlyOnDemandSpend = field("CurrentMinimumHourlyOnDemandSpend")
    EstimatedAverageUtilization = field("EstimatedAverageUtilization")
    EstimatedMonthlySavingsAmount = field("EstimatedMonthlySavingsAmount")
    EstimatedOnDemandCost = field("EstimatedOnDemandCost")
    EstimatedOnDemandCostWithCurrentCommitment = field(
        "EstimatedOnDemandCostWithCurrentCommitment"
    )
    EstimatedROI = field("EstimatedROI")
    EstimatedSPCost = field("EstimatedSPCost")
    EstimatedSavingsAmount = field("EstimatedSavingsAmount")
    EstimatedSavingsPercentage = field("EstimatedSavingsPercentage")
    ExistingHourlyCommitment = field("ExistingHourlyCommitment")
    HourlyCommitmentToPurchase = field("HourlyCommitmentToPurchase")
    UpfrontCost = field("UpfrontCost")
    CurrentAverageCoverage = field("CurrentAverageCoverage")
    EstimatedAverageCoverage = field("EstimatedAverageCoverage")

    @cached_property
    def MetricsOverLookbackPeriod(self):  # pragma: no cover
        return RecommendationDetailHourlyMetrics.make_many(
            self.boto3_raw_data["MetricsOverLookbackPeriod"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendationDetailDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationDetailDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlansPurchaseAnalysisDetails:
    boto3_raw_data: "type_defs.SavingsPlansPurchaseAnalysisDetailsTypeDef" = (
        dataclasses.field()
    )

    CurrencyCode = field("CurrencyCode")
    LookbackPeriodInHours = field("LookbackPeriodInHours")
    CurrentAverageCoverage = field("CurrentAverageCoverage")
    CurrentAverageHourlyOnDemandSpend = field("CurrentAverageHourlyOnDemandSpend")
    CurrentMaximumHourlyOnDemandSpend = field("CurrentMaximumHourlyOnDemandSpend")
    CurrentMinimumHourlyOnDemandSpend = field("CurrentMinimumHourlyOnDemandSpend")
    CurrentOnDemandSpend = field("CurrentOnDemandSpend")
    ExistingHourlyCommitment = field("ExistingHourlyCommitment")
    HourlyCommitmentToPurchase = field("HourlyCommitmentToPurchase")
    EstimatedAverageCoverage = field("EstimatedAverageCoverage")
    EstimatedAverageUtilization = field("EstimatedAverageUtilization")
    EstimatedMonthlySavingsAmount = field("EstimatedMonthlySavingsAmount")
    EstimatedOnDemandCost = field("EstimatedOnDemandCost")
    EstimatedOnDemandCostWithCurrentCommitment = field(
        "EstimatedOnDemandCostWithCurrentCommitment"
    )
    EstimatedROI = field("EstimatedROI")
    EstimatedSavingsAmount = field("EstimatedSavingsAmount")
    EstimatedSavingsPercentage = field("EstimatedSavingsPercentage")
    EstimatedCommitmentCost = field("EstimatedCommitmentCost")
    LatestUsageTimestamp = field("LatestUsageTimestamp")
    UpfrontCost = field("UpfrontCost")
    AdditionalMetadata = field("AdditionalMetadata")

    @cached_property
    def MetricsOverLookbackPeriod(self):  # pragma: no cover
        return RecommendationDetailHourlyMetrics.make_many(
            self.boto3_raw_data["MetricsOverLookbackPeriod"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SavingsPlansPurchaseAnalysisDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlansPurchaseAnalysisDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RootCause:
    boto3_raw_data: "type_defs.RootCauseTypeDef" = dataclasses.field()

    Service = field("Service")
    Region = field("Region")
    LinkedAccount = field("LinkedAccount")
    LinkedAccountName = field("LinkedAccountName")
    UsageType = field("UsageType")

    @cached_property
    def Impact(self):  # pragma: no cover
        return RootCauseImpact.make_one(self.boto3_raw_data["Impact"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RootCauseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RootCauseTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlansCoverage:
    boto3_raw_data: "type_defs.SavingsPlansCoverageTypeDef" = dataclasses.field()

    Attributes = field("Attributes")

    @cached_property
    def Coverage(self):  # pragma: no cover
        return SavingsPlansCoverageData.make_one(self.boto3_raw_data["Coverage"])

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["TimePeriod"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SavingsPlansCoverageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlansCoverageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlansPurchaseRecommendationDetail:
    boto3_raw_data: "type_defs.SavingsPlansPurchaseRecommendationDetailTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SavingsPlansDetails(self):  # pragma: no cover
        return SavingsPlansDetails.make_one(self.boto3_raw_data["SavingsPlansDetails"])

    AccountId = field("AccountId")
    UpfrontCost = field("UpfrontCost")
    EstimatedROI = field("EstimatedROI")
    CurrencyCode = field("CurrencyCode")
    EstimatedSPCost = field("EstimatedSPCost")
    EstimatedOnDemandCost = field("EstimatedOnDemandCost")
    EstimatedOnDemandCostWithCurrentCommitment = field(
        "EstimatedOnDemandCostWithCurrentCommitment"
    )
    EstimatedSavingsAmount = field("EstimatedSavingsAmount")
    EstimatedSavingsPercentage = field("EstimatedSavingsPercentage")
    HourlyCommitmentToPurchase = field("HourlyCommitmentToPurchase")
    EstimatedAverageUtilization = field("EstimatedAverageUtilization")
    EstimatedMonthlySavingsAmount = field("EstimatedMonthlySavingsAmount")
    CurrentMinimumHourlyOnDemandSpend = field("CurrentMinimumHourlyOnDemandSpend")
    CurrentMaximumHourlyOnDemandSpend = field("CurrentMaximumHourlyOnDemandSpend")
    CurrentAverageHourlyOnDemandSpend = field("CurrentAverageHourlyOnDemandSpend")
    RecommendationDetailId = field("RecommendationDetailId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SavingsPlansPurchaseRecommendationDetailTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlansPurchaseRecommendationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlansPurchaseAnalysisConfigurationOutput:
    boto3_raw_data: (
        "type_defs.SavingsPlansPurchaseAnalysisConfigurationOutputTypeDef"
    ) = dataclasses.field()

    AnalysisType = field("AnalysisType")

    @cached_property
    def SavingsPlansToAdd(self):  # pragma: no cover
        return SavingsPlans.make_many(self.boto3_raw_data["SavingsPlansToAdd"])

    @cached_property
    def LookBackTimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["LookBackTimePeriod"])

    AccountScope = field("AccountScope")
    AccountId = field("AccountId")
    SavingsPlansToExclude = field("SavingsPlansToExclude")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SavingsPlansPurchaseAnalysisConfigurationOutputTypeDef"
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
                "type_defs.SavingsPlansPurchaseAnalysisConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlansPurchaseAnalysisConfiguration:
    boto3_raw_data: "type_defs.SavingsPlansPurchaseAnalysisConfigurationTypeDef" = (
        dataclasses.field()
    )

    AnalysisType = field("AnalysisType")

    @cached_property
    def SavingsPlansToAdd(self):  # pragma: no cover
        return SavingsPlans.make_many(self.boto3_raw_data["SavingsPlansToAdd"])

    @cached_property
    def LookBackTimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["LookBackTimePeriod"])

    AccountScope = field("AccountScope")
    AccountId = field("AccountId")
    SavingsPlansToExclude = field("SavingsPlansToExclude")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SavingsPlansPurchaseAnalysisConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlansPurchaseAnalysisConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlansUtilizationAggregates:
    boto3_raw_data: "type_defs.SavingsPlansUtilizationAggregatesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Utilization(self):  # pragma: no cover
        return SavingsPlansUtilization.make_one(self.boto3_raw_data["Utilization"])

    @cached_property
    def Savings(self):  # pragma: no cover
        return SavingsPlansSavings.make_one(self.boto3_raw_data["Savings"])

    @cached_property
    def AmortizedCommitment(self):  # pragma: no cover
        return SavingsPlansAmortizedCommitment.make_one(
            self.boto3_raw_data["AmortizedCommitment"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SavingsPlansUtilizationAggregatesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlansUtilizationAggregatesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlansUtilizationByTime:
    boto3_raw_data: "type_defs.SavingsPlansUtilizationByTimeTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["TimePeriod"])

    @cached_property
    def Utilization(self):  # pragma: no cover
        return SavingsPlansUtilization.make_one(self.boto3_raw_data["Utilization"])

    @cached_property
    def Savings(self):  # pragma: no cover
        return SavingsPlansSavings.make_one(self.boto3_raw_data["Savings"])

    @cached_property
    def AmortizedCommitment(self):  # pragma: no cover
        return SavingsPlansAmortizedCommitment.make_one(
            self.boto3_raw_data["AmortizedCommitment"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SavingsPlansUtilizationByTimeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlansUtilizationByTimeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlansUtilizationDetail:
    boto3_raw_data: "type_defs.SavingsPlansUtilizationDetailTypeDef" = (
        dataclasses.field()
    )

    SavingsPlanArn = field("SavingsPlanArn")
    Attributes = field("Attributes")

    @cached_property
    def Utilization(self):  # pragma: no cover
        return SavingsPlansUtilization.make_one(self.boto3_raw_data["Utilization"])

    @cached_property
    def Savings(self):  # pragma: no cover
        return SavingsPlansSavings.make_one(self.boto3_raw_data["Savings"])

    @cached_property
    def AmortizedCommitment(self):  # pragma: no cover
        return SavingsPlansAmortizedCommitment.make_one(
            self.boto3_raw_data["AmortizedCommitment"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SavingsPlansUtilizationDetailTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlansUtilizationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCostAllocationTagsStatusResponse:
    boto3_raw_data: "type_defs.UpdateCostAllocationTagsStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Errors(self):  # pragma: no cover
        return UpdateCostAllocationTagsStatusError.make_many(
            self.boto3_raw_data["Errors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCostAllocationTagsStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCostAllocationTagsStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCostCategoryDefinitionsResponse:
    boto3_raw_data: "type_defs.ListCostCategoryDefinitionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CostCategoryReferences(self):  # pragma: no cover
        return CostCategoryReference.make_many(
            self.boto3_raw_data["CostCategoryReferences"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCostCategoryDefinitionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCostCategoryDefinitionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostCategorySplitChargeRule:
    boto3_raw_data: "type_defs.CostCategorySplitChargeRuleTypeDef" = dataclasses.field()

    Source = field("Source")
    Targets = field("Targets")
    Method = field("Method")
    Parameters = field("Parameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CostCategorySplitChargeRuleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CostCategorySplitChargeRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCostForecastResponse:
    boto3_raw_data: "type_defs.GetCostForecastResponseTypeDef" = dataclasses.field()

    @cached_property
    def Total(self):  # pragma: no cover
        return MetricValue.make_one(self.boto3_raw_data["Total"])

    @cached_property
    def ForecastResultsByTime(self):  # pragma: no cover
        return ForecastResult.make_many(self.boto3_raw_data["ForecastResultsByTime"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCostForecastResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCostForecastResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUsageForecastResponse:
    boto3_raw_data: "type_defs.GetUsageForecastResponseTypeDef" = dataclasses.field()

    @cached_property
    def Total(self):  # pragma: no cover
        return MetricValue.make_one(self.boto3_raw_data["Total"])

    @cached_property
    def ForecastResultsByTime(self):  # pragma: no cover
        return ForecastResult.make_many(self.boto3_raw_data["ForecastResultsByTime"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUsageForecastResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUsageForecastResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservationCoverageGroup:
    boto3_raw_data: "type_defs.ReservationCoverageGroupTypeDef" = dataclasses.field()

    Attributes = field("Attributes")

    @cached_property
    def Coverage(self):  # pragma: no cover
        return Coverage.make_one(self.boto3_raw_data["Coverage"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReservationCoverageGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservationCoverageGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyMonitorOutput:
    boto3_raw_data: "type_defs.AnomalyMonitorOutputTypeDef" = dataclasses.field()

    MonitorName = field("MonitorName")
    MonitorType = field("MonitorType")
    MonitorArn = field("MonitorArn")
    CreationDate = field("CreationDate")
    LastUpdatedDate = field("LastUpdatedDate")
    LastEvaluatedDate = field("LastEvaluatedDate")
    MonitorDimension = field("MonitorDimension")

    @cached_property
    def MonitorSpecification(self):  # pragma: no cover
        return ExpressionOutput.make_one(self.boto3_raw_data["MonitorSpecification"])

    DimensionalValueCount = field("DimensionalValueCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnomalyMonitorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalyMonitorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalySubscriptionOutput:
    boto3_raw_data: "type_defs.AnomalySubscriptionOutputTypeDef" = dataclasses.field()

    MonitorArnList = field("MonitorArnList")

    @cached_property
    def Subscribers(self):  # pragma: no cover
        return Subscriber.make_many(self.boto3_raw_data["Subscribers"])

    Frequency = field("Frequency")
    SubscriptionName = field("SubscriptionName")
    SubscriptionArn = field("SubscriptionArn")
    AccountId = field("AccountId")
    Threshold = field("Threshold")

    @cached_property
    def ThresholdExpression(self):  # pragma: no cover
        return ExpressionOutput.make_one(self.boto3_raw_data["ThresholdExpression"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnomalySubscriptionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalySubscriptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostAndUsageComparison:
    boto3_raw_data: "type_defs.CostAndUsageComparisonTypeDef" = dataclasses.field()

    @cached_property
    def CostAndUsageSelector(self):  # pragma: no cover
        return ExpressionOutput.make_one(self.boto3_raw_data["CostAndUsageSelector"])

    Metrics = field("Metrics")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CostAndUsageComparisonTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CostAndUsageComparisonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostCategoryRuleOutput:
    boto3_raw_data: "type_defs.CostCategoryRuleOutputTypeDef" = dataclasses.field()

    Value = field("Value")

    @cached_property
    def Rule(self):  # pragma: no cover
        return ExpressionOutput.make_one(self.boto3_raw_data["Rule"])

    @cached_property
    def InheritedValue(self):  # pragma: no cover
        return CostCategoryInheritedValueDimension.make_one(
            self.boto3_raw_data["InheritedValue"]
        )

    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CostCategoryRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CostCategoryRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostComparisonDriver:
    boto3_raw_data: "type_defs.CostComparisonDriverTypeDef" = dataclasses.field()

    @cached_property
    def CostSelector(self):  # pragma: no cover
        return ExpressionOutput.make_one(self.boto3_raw_data["CostSelector"])

    Metrics = field("Metrics")

    @cached_property
    def CostDrivers(self):  # pragma: no cover
        return CostDriver.make_many(self.boto3_raw_data["CostDrivers"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CostComparisonDriverTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CostComparisonDriverTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyMonitorPaginator:
    boto3_raw_data: "type_defs.AnomalyMonitorPaginatorTypeDef" = dataclasses.field()

    MonitorName = field("MonitorName")
    MonitorType = field("MonitorType")
    MonitorArn = field("MonitorArn")
    CreationDate = field("CreationDate")
    LastUpdatedDate = field("LastUpdatedDate")
    LastEvaluatedDate = field("LastEvaluatedDate")
    MonitorDimension = field("MonitorDimension")

    @cached_property
    def MonitorSpecification(self):  # pragma: no cover
        return ExpressionPaginatorOutput.make_one(
            self.boto3_raw_data["MonitorSpecification"]
        )

    DimensionalValueCount = field("DimensionalValueCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnomalyMonitorPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalyMonitorPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalySubscriptionPaginator:
    boto3_raw_data: "type_defs.AnomalySubscriptionPaginatorTypeDef" = (
        dataclasses.field()
    )

    MonitorArnList = field("MonitorArnList")

    @cached_property
    def Subscribers(self):  # pragma: no cover
        return Subscriber.make_many(self.boto3_raw_data["Subscribers"])

    Frequency = field("Frequency")
    SubscriptionName = field("SubscriptionName")
    SubscriptionArn = field("SubscriptionArn")
    AccountId = field("AccountId")
    Threshold = field("Threshold")

    @cached_property
    def ThresholdExpression(self):  # pragma: no cover
        return ExpressionPaginatorOutput.make_one(
            self.boto3_raw_data["ThresholdExpression"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnomalySubscriptionPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalySubscriptionPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostAndUsageComparisonPaginator:
    boto3_raw_data: "type_defs.CostAndUsageComparisonPaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CostAndUsageSelector(self):  # pragma: no cover
        return ExpressionPaginatorOutput.make_one(
            self.boto3_raw_data["CostAndUsageSelector"]
        )

    Metrics = field("Metrics")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CostAndUsageComparisonPaginatorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CostAndUsageComparisonPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostComparisonDriverPaginator:
    boto3_raw_data: "type_defs.CostComparisonDriverPaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CostSelector(self):  # pragma: no cover
        return ExpressionPaginatorOutput.make_one(self.boto3_raw_data["CostSelector"])

    Metrics = field("Metrics")

    @cached_property
    def CostDrivers(self):  # pragma: no cover
        return CostDriver.make_many(self.boto3_raw_data["CostDrivers"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CostComparisonDriverPaginatorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CostComparisonDriverPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceUtilization:
    boto3_raw_data: "type_defs.ResourceUtilizationTypeDef" = dataclasses.field()

    @cached_property
    def EC2ResourceUtilization(self):  # pragma: no cover
        return EC2ResourceUtilization.make_one(
            self.boto3_raw_data["EC2ResourceUtilization"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceUtilizationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceUtilizationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Expression:
    boto3_raw_data: "type_defs.ExpressionTypeDef" = dataclasses.field()

    Or = field("Or")
    And = field("And")
    Not = field("Not")
    Dimensions = field("Dimensions")
    Tags = field("Tags")
    CostCategories = field("CostCategories")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExpressionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExpressionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResultByTime:
    boto3_raw_data: "type_defs.ResultByTimeTypeDef" = dataclasses.field()

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["TimePeriod"])

    Total = field("Total")

    @cached_property
    def Groups(self):  # pragma: no cover
        return Group.make_many(self.boto3_raw_data["Groups"])

    Estimated = field("Estimated")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResultByTimeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResultByTimeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UtilizationByTime:
    boto3_raw_data: "type_defs.UtilizationByTimeTypeDef" = dataclasses.field()

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["TimePeriod"])

    @cached_property
    def Groups(self):  # pragma: no cover
        return ReservationUtilizationGroup.make_many(self.boto3_raw_data["Groups"])

    @cached_property
    def Total(self):  # pragma: no cover
        return ReservationAggregates.make_one(self.boto3_raw_data["Total"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UtilizationByTimeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UtilizationByTimeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservationPurchaseRecommendationDetail:
    boto3_raw_data: "type_defs.ReservationPurchaseRecommendationDetailTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")

    @cached_property
    def InstanceDetails(self):  # pragma: no cover
        return InstanceDetails.make_one(self.boto3_raw_data["InstanceDetails"])

    RecommendedNumberOfInstancesToPurchase = field(
        "RecommendedNumberOfInstancesToPurchase"
    )
    RecommendedNormalizedUnitsToPurchase = field("RecommendedNormalizedUnitsToPurchase")
    MinimumNumberOfInstancesUsedPerHour = field("MinimumNumberOfInstancesUsedPerHour")
    MinimumNormalizedUnitsUsedPerHour = field("MinimumNormalizedUnitsUsedPerHour")
    MaximumNumberOfInstancesUsedPerHour = field("MaximumNumberOfInstancesUsedPerHour")
    MaximumNormalizedUnitsUsedPerHour = field("MaximumNormalizedUnitsUsedPerHour")
    AverageNumberOfInstancesUsedPerHour = field("AverageNumberOfInstancesUsedPerHour")
    AverageNormalizedUnitsUsedPerHour = field("AverageNormalizedUnitsUsedPerHour")
    AverageUtilization = field("AverageUtilization")
    EstimatedBreakEvenInMonths = field("EstimatedBreakEvenInMonths")
    CurrencyCode = field("CurrencyCode")
    EstimatedMonthlySavingsAmount = field("EstimatedMonthlySavingsAmount")
    EstimatedMonthlySavingsPercentage = field("EstimatedMonthlySavingsPercentage")
    EstimatedMonthlyOnDemandCost = field("EstimatedMonthlyOnDemandCost")
    EstimatedReservationCostForLookbackPeriod = field(
        "EstimatedReservationCostForLookbackPeriod"
    )
    UpfrontCost = field("UpfrontCost")
    RecurringStandardMonthlyCost = field("RecurringStandardMonthlyCost")

    @cached_property
    def ReservedCapacityDetails(self):  # pragma: no cover
        return ReservedCapacityDetails.make_one(
            self.boto3_raw_data["ReservedCapacityDetails"]
        )

    RecommendedNumberOfCapacityUnitsToPurchase = field(
        "RecommendedNumberOfCapacityUnitsToPurchase"
    )
    MinimumNumberOfCapacityUnitsUsedPerHour = field(
        "MinimumNumberOfCapacityUnitsUsedPerHour"
    )
    MaximumNumberOfCapacityUnitsUsedPerHour = field(
        "MaximumNumberOfCapacityUnitsUsedPerHour"
    )
    AverageNumberOfCapacityUnitsUsedPerHour = field(
        "AverageNumberOfCapacityUnitsUsedPerHour"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReservationPurchaseRecommendationDetailTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservationPurchaseRecommendationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSavingsPlanPurchaseRecommendationDetailsResponse:
    boto3_raw_data: (
        "type_defs.GetSavingsPlanPurchaseRecommendationDetailsResponseTypeDef"
    ) = dataclasses.field()

    RecommendationDetailId = field("RecommendationDetailId")

    @cached_property
    def RecommendationDetailData(self):  # pragma: no cover
        return RecommendationDetailData.make_one(
            self.boto3_raw_data["RecommendationDetailData"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSavingsPlanPurchaseRecommendationDetailsResponseTypeDef"
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
                "type_defs.GetSavingsPlanPurchaseRecommendationDetailsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisDetails:
    boto3_raw_data: "type_defs.AnalysisDetailsTypeDef" = dataclasses.field()

    @cached_property
    def SavingsPlansPurchaseAnalysisDetails(self):  # pragma: no cover
        return SavingsPlansPurchaseAnalysisDetails.make_one(
            self.boto3_raw_data["SavingsPlansPurchaseAnalysisDetails"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalysisDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnalysisDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Anomaly:
    boto3_raw_data: "type_defs.AnomalyTypeDef" = dataclasses.field()

    AnomalyId = field("AnomalyId")

    @cached_property
    def AnomalyScore(self):  # pragma: no cover
        return AnomalyScore.make_one(self.boto3_raw_data["AnomalyScore"])

    @cached_property
    def Impact(self):  # pragma: no cover
        return Impact.make_one(self.boto3_raw_data["Impact"])

    MonitorArn = field("MonitorArn")
    AnomalyStartDate = field("AnomalyStartDate")
    AnomalyEndDate = field("AnomalyEndDate")
    DimensionValue = field("DimensionValue")

    @cached_property
    def RootCauses(self):  # pragma: no cover
        return RootCause.make_many(self.boto3_raw_data["RootCauses"])

    Feedback = field("Feedback")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnomalyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnomalyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSavingsPlansCoverageResponse:
    boto3_raw_data: "type_defs.GetSavingsPlansCoverageResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SavingsPlansCoverages(self):  # pragma: no cover
        return SavingsPlansCoverage.make_many(
            self.boto3_raw_data["SavingsPlansCoverages"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSavingsPlansCoverageResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSavingsPlansCoverageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SavingsPlansPurchaseRecommendation:
    boto3_raw_data: "type_defs.SavingsPlansPurchaseRecommendationTypeDef" = (
        dataclasses.field()
    )

    AccountScope = field("AccountScope")
    SavingsPlansType = field("SavingsPlansType")
    TermInYears = field("TermInYears")
    PaymentOption = field("PaymentOption")
    LookbackPeriodInDays = field("LookbackPeriodInDays")

    @cached_property
    def SavingsPlansPurchaseRecommendationDetails(self):  # pragma: no cover
        return SavingsPlansPurchaseRecommendationDetail.make_many(
            self.boto3_raw_data["SavingsPlansPurchaseRecommendationDetails"]
        )

    @cached_property
    def SavingsPlansPurchaseRecommendationSummary(self):  # pragma: no cover
        return SavingsPlansPurchaseRecommendationSummary.make_one(
            self.boto3_raw_data["SavingsPlansPurchaseRecommendationSummary"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SavingsPlansPurchaseRecommendationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SavingsPlansPurchaseRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommitmentPurchaseAnalysisConfigurationOutput:
    boto3_raw_data: "type_defs.CommitmentPurchaseAnalysisConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SavingsPlansPurchaseAnalysisConfiguration(self):  # pragma: no cover
        return SavingsPlansPurchaseAnalysisConfigurationOutput.make_one(
            self.boto3_raw_data["SavingsPlansPurchaseAnalysisConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CommitmentPurchaseAnalysisConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommitmentPurchaseAnalysisConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommitmentPurchaseAnalysisConfiguration:
    boto3_raw_data: "type_defs.CommitmentPurchaseAnalysisConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SavingsPlansPurchaseAnalysisConfiguration(self):  # pragma: no cover
        return SavingsPlansPurchaseAnalysisConfiguration.make_one(
            self.boto3_raw_data["SavingsPlansPurchaseAnalysisConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CommitmentPurchaseAnalysisConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommitmentPurchaseAnalysisConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSavingsPlansUtilizationResponse:
    boto3_raw_data: "type_defs.GetSavingsPlansUtilizationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SavingsPlansUtilizationsByTime(self):  # pragma: no cover
        return SavingsPlansUtilizationByTime.make_many(
            self.boto3_raw_data["SavingsPlansUtilizationsByTime"]
        )

    @cached_property
    def Total(self):  # pragma: no cover
        return SavingsPlansUtilizationAggregates.make_one(self.boto3_raw_data["Total"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSavingsPlansUtilizationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSavingsPlansUtilizationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSavingsPlansUtilizationDetailsResponse:
    boto3_raw_data: "type_defs.GetSavingsPlansUtilizationDetailsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SavingsPlansUtilizationDetails(self):  # pragma: no cover
        return SavingsPlansUtilizationDetail.make_many(
            self.boto3_raw_data["SavingsPlansUtilizationDetails"]
        )

    @cached_property
    def Total(self):  # pragma: no cover
        return SavingsPlansUtilizationAggregates.make_one(self.boto3_raw_data["Total"])

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["TimePeriod"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSavingsPlansUtilizationDetailsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSavingsPlansUtilizationDetailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoverageByTime:
    boto3_raw_data: "type_defs.CoverageByTimeTypeDef" = dataclasses.field()

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["TimePeriod"])

    @cached_property
    def Groups(self):  # pragma: no cover
        return ReservationCoverageGroup.make_many(self.boto3_raw_data["Groups"])

    @cached_property
    def Total(self):  # pragma: no cover
        return Coverage.make_one(self.boto3_raw_data["Total"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CoverageByTimeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CoverageByTimeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnomalyMonitorsResponse:
    boto3_raw_data: "type_defs.GetAnomalyMonitorsResponseTypeDef" = dataclasses.field()

    @cached_property
    def AnomalyMonitors(self):  # pragma: no cover
        return AnomalyMonitorOutput.make_many(self.boto3_raw_data["AnomalyMonitors"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAnomalyMonitorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnomalyMonitorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnomalySubscriptionsResponse:
    boto3_raw_data: "type_defs.GetAnomalySubscriptionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AnomalySubscriptions(self):  # pragma: no cover
        return AnomalySubscriptionOutput.make_many(
            self.boto3_raw_data["AnomalySubscriptions"]
        )

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAnomalySubscriptionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnomalySubscriptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCostAndUsageComparisonsResponse:
    boto3_raw_data: "type_defs.GetCostAndUsageComparisonsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CostAndUsageComparisons(self):  # pragma: no cover
        return CostAndUsageComparison.make_many(
            self.boto3_raw_data["CostAndUsageComparisons"]
        )

    TotalCostAndUsage = field("TotalCostAndUsage")
    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCostAndUsageComparisonsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCostAndUsageComparisonsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostCategory:
    boto3_raw_data: "type_defs.CostCategoryTypeDef" = dataclasses.field()

    CostCategoryArn = field("CostCategoryArn")
    EffectiveStart = field("EffectiveStart")
    Name = field("Name")
    RuleVersion = field("RuleVersion")

    @cached_property
    def Rules(self):  # pragma: no cover
        return CostCategoryRuleOutput.make_many(self.boto3_raw_data["Rules"])

    EffectiveEnd = field("EffectiveEnd")

    @cached_property
    def SplitChargeRules(self):  # pragma: no cover
        return CostCategorySplitChargeRuleOutput.make_many(
            self.boto3_raw_data["SplitChargeRules"]
        )

    @cached_property
    def ProcessingStatus(self):  # pragma: no cover
        return CostCategoryProcessingStatus.make_many(
            self.boto3_raw_data["ProcessingStatus"]
        )

    DefaultValue = field("DefaultValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CostCategoryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CostCategoryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCostComparisonDriversResponse:
    boto3_raw_data: "type_defs.GetCostComparisonDriversResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CostComparisonDrivers(self):  # pragma: no cover
        return CostComparisonDriver.make_many(
            self.boto3_raw_data["CostComparisonDrivers"]
        )

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCostComparisonDriversResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCostComparisonDriversResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnomalyMonitorsResponsePaginator:
    boto3_raw_data: "type_defs.GetAnomalyMonitorsResponsePaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AnomalyMonitors(self):  # pragma: no cover
        return AnomalyMonitorPaginator.make_many(self.boto3_raw_data["AnomalyMonitors"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAnomalyMonitorsResponsePaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnomalyMonitorsResponsePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnomalySubscriptionsResponsePaginator:
    boto3_raw_data: "type_defs.GetAnomalySubscriptionsResponsePaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AnomalySubscriptions(self):  # pragma: no cover
        return AnomalySubscriptionPaginator.make_many(
            self.boto3_raw_data["AnomalySubscriptions"]
        )

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAnomalySubscriptionsResponsePaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnomalySubscriptionsResponsePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCostAndUsageComparisonsResponsePaginator:
    boto3_raw_data: "type_defs.GetCostAndUsageComparisonsResponsePaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CostAndUsageComparisons(self):  # pragma: no cover
        return CostAndUsageComparisonPaginator.make_many(
            self.boto3_raw_data["CostAndUsageComparisons"]
        )

    TotalCostAndUsage = field("TotalCostAndUsage")
    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCostAndUsageComparisonsResponsePaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCostAndUsageComparisonsResponsePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCostComparisonDriversResponsePaginator:
    boto3_raw_data: "type_defs.GetCostComparisonDriversResponsePaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CostComparisonDrivers(self):  # pragma: no cover
        return CostComparisonDriverPaginator.make_many(
            self.boto3_raw_data["CostComparisonDrivers"]
        )

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCostComparisonDriversResponsePaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCostComparisonDriversResponsePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CurrentInstance:
    boto3_raw_data: "type_defs.CurrentInstanceTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    InstanceName = field("InstanceName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagValuesOutput.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResourceDetails(self):  # pragma: no cover
        return ResourceDetails.make_one(self.boto3_raw_data["ResourceDetails"])

    @cached_property
    def ResourceUtilization(self):  # pragma: no cover
        return ResourceUtilization.make_one(self.boto3_raw_data["ResourceUtilization"])

    ReservationCoveredHoursInLookbackPeriod = field(
        "ReservationCoveredHoursInLookbackPeriod"
    )
    SavingsPlansCoveredHoursInLookbackPeriod = field(
        "SavingsPlansCoveredHoursInLookbackPeriod"
    )
    OnDemandHoursInLookbackPeriod = field("OnDemandHoursInLookbackPeriod")
    TotalRunningHoursInLookbackPeriod = field("TotalRunningHoursInLookbackPeriod")
    MonthlyCost = field("MonthlyCost")
    CurrencyCode = field("CurrencyCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CurrentInstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CurrentInstanceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetInstance:
    boto3_raw_data: "type_defs.TargetInstanceTypeDef" = dataclasses.field()

    EstimatedMonthlyCost = field("EstimatedMonthlyCost")
    EstimatedMonthlySavings = field("EstimatedMonthlySavings")
    CurrencyCode = field("CurrencyCode")
    DefaultTargetInstance = field("DefaultTargetInstance")

    @cached_property
    def ResourceDetails(self):  # pragma: no cover
        return ResourceDetails.make_one(self.boto3_raw_data["ResourceDetails"])

    @cached_property
    def ExpectedResourceUtilization(self):  # pragma: no cover
        return ResourceUtilization.make_one(
            self.boto3_raw_data["ExpectedResourceUtilization"]
        )

    PlatformDifferences = field("PlatformDifferences")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetInstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetInstanceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCostAndUsageComparisonsRequestPaginate:
    boto3_raw_data: "type_defs.GetCostAndUsageComparisonsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BaselineTimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["BaselineTimePeriod"])

    @cached_property
    def ComparisonTimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["ComparisonTimePeriod"])

    MetricForComparison = field("MetricForComparison")
    BillingViewArn = field("BillingViewArn")
    Filter = field("Filter")

    @cached_property
    def GroupBy(self):  # pragma: no cover
        return GroupDefinition.make_many(self.boto3_raw_data["GroupBy"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCostAndUsageComparisonsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCostAndUsageComparisonsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCostComparisonDriversRequestPaginate:
    boto3_raw_data: "type_defs.GetCostComparisonDriversRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BaselineTimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["BaselineTimePeriod"])

    @cached_property
    def ComparisonTimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["ComparisonTimePeriod"])

    MetricForComparison = field("MetricForComparison")
    BillingViewArn = field("BillingViewArn")
    Filter = field("Filter")

    @cached_property
    def GroupBy(self):  # pragma: no cover
        return GroupDefinition.make_many(self.boto3_raw_data["GroupBy"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCostComparisonDriversRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCostComparisonDriversRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyMonitor:
    boto3_raw_data: "type_defs.AnomalyMonitorTypeDef" = dataclasses.field()

    MonitorName = field("MonitorName")
    MonitorType = field("MonitorType")
    MonitorArn = field("MonitorArn")
    CreationDate = field("CreationDate")
    LastUpdatedDate = field("LastUpdatedDate")
    LastEvaluatedDate = field("LastEvaluatedDate")
    MonitorDimension = field("MonitorDimension")

    @cached_property
    def MonitorSpecification(self):  # pragma: no cover
        return Expression.make_one(self.boto3_raw_data["MonitorSpecification"])

    DimensionalValueCount = field("DimensionalValueCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnomalyMonitorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnomalyMonitorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalySubscription:
    boto3_raw_data: "type_defs.AnomalySubscriptionTypeDef" = dataclasses.field()

    MonitorArnList = field("MonitorArnList")

    @cached_property
    def Subscribers(self):  # pragma: no cover
        return Subscriber.make_many(self.boto3_raw_data["Subscribers"])

    Frequency = field("Frequency")
    SubscriptionName = field("SubscriptionName")
    SubscriptionArn = field("SubscriptionArn")
    AccountId = field("AccountId")
    Threshold = field("Threshold")

    @cached_property
    def ThresholdExpression(self):  # pragma: no cover
        return Expression.make_one(self.boto3_raw_data["ThresholdExpression"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnomalySubscriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalySubscriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCostAndUsageResponse:
    boto3_raw_data: "type_defs.GetCostAndUsageResponseTypeDef" = dataclasses.field()

    NextPageToken = field("NextPageToken")

    @cached_property
    def GroupDefinitions(self):  # pragma: no cover
        return GroupDefinition.make_many(self.boto3_raw_data["GroupDefinitions"])

    @cached_property
    def ResultsByTime(self):  # pragma: no cover
        return ResultByTime.make_many(self.boto3_raw_data["ResultsByTime"])

    @cached_property
    def DimensionValueAttributes(self):  # pragma: no cover
        return DimensionValuesWithAttributes.make_many(
            self.boto3_raw_data["DimensionValueAttributes"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCostAndUsageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCostAndUsageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCostAndUsageWithResourcesResponse:
    boto3_raw_data: "type_defs.GetCostAndUsageWithResourcesResponseTypeDef" = (
        dataclasses.field()
    )

    NextPageToken = field("NextPageToken")

    @cached_property
    def GroupDefinitions(self):  # pragma: no cover
        return GroupDefinition.make_many(self.boto3_raw_data["GroupDefinitions"])

    @cached_property
    def ResultsByTime(self):  # pragma: no cover
        return ResultByTime.make_many(self.boto3_raw_data["ResultsByTime"])

    @cached_property
    def DimensionValueAttributes(self):  # pragma: no cover
        return DimensionValuesWithAttributes.make_many(
            self.boto3_raw_data["DimensionValueAttributes"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCostAndUsageWithResourcesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCostAndUsageWithResourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReservationUtilizationResponse:
    boto3_raw_data: "type_defs.GetReservationUtilizationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UtilizationsByTime(self):  # pragma: no cover
        return UtilizationByTime.make_many(self.boto3_raw_data["UtilizationsByTime"])

    @cached_property
    def Total(self):  # pragma: no cover
        return ReservationAggregates.make_one(self.boto3_raw_data["Total"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetReservationUtilizationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReservationUtilizationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservationPurchaseRecommendation:
    boto3_raw_data: "type_defs.ReservationPurchaseRecommendationTypeDef" = (
        dataclasses.field()
    )

    AccountScope = field("AccountScope")
    LookbackPeriodInDays = field("LookbackPeriodInDays")
    TermInYears = field("TermInYears")
    PaymentOption = field("PaymentOption")

    @cached_property
    def ServiceSpecification(self):  # pragma: no cover
        return ServiceSpecification.make_one(
            self.boto3_raw_data["ServiceSpecification"]
        )

    @cached_property
    def RecommendationDetails(self):  # pragma: no cover
        return ReservationPurchaseRecommendationDetail.make_many(
            self.boto3_raw_data["RecommendationDetails"]
        )

    @cached_property
    def RecommendationSummary(self):  # pragma: no cover
        return ReservationPurchaseRecommendationSummary.make_one(
            self.boto3_raw_data["RecommendationSummary"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReservationPurchaseRecommendationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservationPurchaseRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnomaliesResponse:
    boto3_raw_data: "type_defs.GetAnomaliesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Anomalies(self):  # pragma: no cover
        return Anomaly.make_many(self.boto3_raw_data["Anomalies"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAnomaliesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnomaliesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSavingsPlansPurchaseRecommendationResponse:
    boto3_raw_data: "type_defs.GetSavingsPlansPurchaseRecommendationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Metadata(self):  # pragma: no cover
        return SavingsPlansPurchaseRecommendationMetadata.make_one(
            self.boto3_raw_data["Metadata"]
        )

    @cached_property
    def SavingsPlansPurchaseRecommendation(self):  # pragma: no cover
        return SavingsPlansPurchaseRecommendation.make_one(
            self.boto3_raw_data["SavingsPlansPurchaseRecommendation"]
        )

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSavingsPlansPurchaseRecommendationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSavingsPlansPurchaseRecommendationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisSummary:
    boto3_raw_data: "type_defs.AnalysisSummaryTypeDef" = dataclasses.field()

    EstimatedCompletionTime = field("EstimatedCompletionTime")
    AnalysisCompletionTime = field("AnalysisCompletionTime")
    AnalysisStartedTime = field("AnalysisStartedTime")
    AnalysisStatus = field("AnalysisStatus")
    ErrorCode = field("ErrorCode")
    AnalysisId = field("AnalysisId")

    @cached_property
    def CommitmentPurchaseAnalysisConfiguration(self):  # pragma: no cover
        return CommitmentPurchaseAnalysisConfigurationOutput.make_one(
            self.boto3_raw_data["CommitmentPurchaseAnalysisConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalysisSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnalysisSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCommitmentPurchaseAnalysisResponse:
    boto3_raw_data: "type_defs.GetCommitmentPurchaseAnalysisResponseTypeDef" = (
        dataclasses.field()
    )

    EstimatedCompletionTime = field("EstimatedCompletionTime")
    AnalysisCompletionTime = field("AnalysisCompletionTime")
    AnalysisStartedTime = field("AnalysisStartedTime")
    AnalysisId = field("AnalysisId")
    AnalysisStatus = field("AnalysisStatus")
    ErrorCode = field("ErrorCode")

    @cached_property
    def AnalysisDetails(self):  # pragma: no cover
        return AnalysisDetails.make_one(self.boto3_raw_data["AnalysisDetails"])

    @cached_property
    def CommitmentPurchaseAnalysisConfiguration(self):  # pragma: no cover
        return CommitmentPurchaseAnalysisConfigurationOutput.make_one(
            self.boto3_raw_data["CommitmentPurchaseAnalysisConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCommitmentPurchaseAnalysisResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCommitmentPurchaseAnalysisResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReservationCoverageResponse:
    boto3_raw_data: "type_defs.GetReservationCoverageResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CoveragesByTime(self):  # pragma: no cover
        return CoverageByTime.make_many(self.boto3_raw_data["CoveragesByTime"])

    @cached_property
    def Total(self):  # pragma: no cover
        return Coverage.make_one(self.boto3_raw_data["Total"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetReservationCoverageResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReservationCoverageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCostCategoryDefinitionResponse:
    boto3_raw_data: "type_defs.DescribeCostCategoryDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CostCategory(self):  # pragma: no cover
        return CostCategory.make_one(self.boto3_raw_data["CostCategory"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCostCategoryDefinitionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCostCategoryDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyRecommendationDetail:
    boto3_raw_data: "type_defs.ModifyRecommendationDetailTypeDef" = dataclasses.field()

    @cached_property
    def TargetInstances(self):  # pragma: no cover
        return TargetInstance.make_many(self.boto3_raw_data["TargetInstances"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyRecommendationDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyRecommendationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostCategoryRule:
    boto3_raw_data: "type_defs.CostCategoryRuleTypeDef" = dataclasses.field()

    Value = field("Value")
    Rule = field("Rule")

    @cached_property
    def InheritedValue(self):  # pragma: no cover
        return CostCategoryInheritedValueDimension.make_one(
            self.boto3_raw_data["InheritedValue"]
        )

    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CostCategoryRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CostCategoryRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCostAndUsageComparisonsRequest:
    boto3_raw_data: "type_defs.GetCostAndUsageComparisonsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BaselineTimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["BaselineTimePeriod"])

    @cached_property
    def ComparisonTimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["ComparisonTimePeriod"])

    MetricForComparison = field("MetricForComparison")
    BillingViewArn = field("BillingViewArn")
    Filter = field("Filter")

    @cached_property
    def GroupBy(self):  # pragma: no cover
        return GroupDefinition.make_many(self.boto3_raw_data["GroupBy"])

    MaxResults = field("MaxResults")
    NextPageToken = field("NextPageToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCostAndUsageComparisonsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCostAndUsageComparisonsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCostAndUsageRequest:
    boto3_raw_data: "type_defs.GetCostAndUsageRequestTypeDef" = dataclasses.field()

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["TimePeriod"])

    Granularity = field("Granularity")
    Metrics = field("Metrics")
    Filter = field("Filter")

    @cached_property
    def GroupBy(self):  # pragma: no cover
        return GroupDefinition.make_many(self.boto3_raw_data["GroupBy"])

    BillingViewArn = field("BillingViewArn")
    NextPageToken = field("NextPageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCostAndUsageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCostAndUsageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCostAndUsageWithResourcesRequest:
    boto3_raw_data: "type_defs.GetCostAndUsageWithResourcesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["TimePeriod"])

    Granularity = field("Granularity")
    Filter = field("Filter")
    Metrics = field("Metrics")

    @cached_property
    def GroupBy(self):  # pragma: no cover
        return GroupDefinition.make_many(self.boto3_raw_data["GroupBy"])

    BillingViewArn = field("BillingViewArn")
    NextPageToken = field("NextPageToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCostAndUsageWithResourcesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCostAndUsageWithResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCostCategoriesRequest:
    boto3_raw_data: "type_defs.GetCostCategoriesRequestTypeDef" = dataclasses.field()

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["TimePeriod"])

    SearchString = field("SearchString")
    CostCategoryName = field("CostCategoryName")
    Filter = field("Filter")

    @cached_property
    def SortBy(self):  # pragma: no cover
        return SortDefinition.make_many(self.boto3_raw_data["SortBy"])

    BillingViewArn = field("BillingViewArn")
    MaxResults = field("MaxResults")
    NextPageToken = field("NextPageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCostCategoriesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCostCategoriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCostComparisonDriversRequest:
    boto3_raw_data: "type_defs.GetCostComparisonDriversRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BaselineTimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["BaselineTimePeriod"])

    @cached_property
    def ComparisonTimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["ComparisonTimePeriod"])

    MetricForComparison = field("MetricForComparison")
    BillingViewArn = field("BillingViewArn")
    Filter = field("Filter")

    @cached_property
    def GroupBy(self):  # pragma: no cover
        return GroupDefinition.make_many(self.boto3_raw_data["GroupBy"])

    MaxResults = field("MaxResults")
    NextPageToken = field("NextPageToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCostComparisonDriversRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCostComparisonDriversRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCostForecastRequest:
    boto3_raw_data: "type_defs.GetCostForecastRequestTypeDef" = dataclasses.field()

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["TimePeriod"])

    Metric = field("Metric")
    Granularity = field("Granularity")
    Filter = field("Filter")
    BillingViewArn = field("BillingViewArn")
    PredictionIntervalLevel = field("PredictionIntervalLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCostForecastRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCostForecastRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDimensionValuesRequest:
    boto3_raw_data: "type_defs.GetDimensionValuesRequestTypeDef" = dataclasses.field()

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["TimePeriod"])

    Dimension = field("Dimension")
    SearchString = field("SearchString")
    Context = field("Context")
    Filter = field("Filter")

    @cached_property
    def SortBy(self):  # pragma: no cover
        return SortDefinition.make_many(self.boto3_raw_data["SortBy"])

    BillingViewArn = field("BillingViewArn")
    MaxResults = field("MaxResults")
    NextPageToken = field("NextPageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDimensionValuesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDimensionValuesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReservationCoverageRequest:
    boto3_raw_data: "type_defs.GetReservationCoverageRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["TimePeriod"])

    @cached_property
    def GroupBy(self):  # pragma: no cover
        return GroupDefinition.make_many(self.boto3_raw_data["GroupBy"])

    Granularity = field("Granularity")
    Filter = field("Filter")
    Metrics = field("Metrics")
    NextPageToken = field("NextPageToken")

    @cached_property
    def SortBy(self):  # pragma: no cover
        return SortDefinition.make_one(self.boto3_raw_data["SortBy"])

    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetReservationCoverageRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReservationCoverageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReservationPurchaseRecommendationRequest:
    boto3_raw_data: "type_defs.GetReservationPurchaseRecommendationRequestTypeDef" = (
        dataclasses.field()
    )

    Service = field("Service")
    AccountId = field("AccountId")
    Filter = field("Filter")
    AccountScope = field("AccountScope")
    LookbackPeriodInDays = field("LookbackPeriodInDays")
    TermInYears = field("TermInYears")
    PaymentOption = field("PaymentOption")

    @cached_property
    def ServiceSpecification(self):  # pragma: no cover
        return ServiceSpecification.make_one(
            self.boto3_raw_data["ServiceSpecification"]
        )

    PageSize = field("PageSize")
    NextPageToken = field("NextPageToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetReservationPurchaseRecommendationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReservationPurchaseRecommendationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReservationUtilizationRequest:
    boto3_raw_data: "type_defs.GetReservationUtilizationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["TimePeriod"])

    @cached_property
    def GroupBy(self):  # pragma: no cover
        return GroupDefinition.make_many(self.boto3_raw_data["GroupBy"])

    Granularity = field("Granularity")
    Filter = field("Filter")

    @cached_property
    def SortBy(self):  # pragma: no cover
        return SortDefinition.make_one(self.boto3_raw_data["SortBy"])

    NextPageToken = field("NextPageToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetReservationUtilizationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReservationUtilizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRightsizingRecommendationRequest:
    boto3_raw_data: "type_defs.GetRightsizingRecommendationRequestTypeDef" = (
        dataclasses.field()
    )

    Service = field("Service")
    Filter = field("Filter")

    @cached_property
    def Configuration(self):  # pragma: no cover
        return RightsizingRecommendationConfiguration.make_one(
            self.boto3_raw_data["Configuration"]
        )

    PageSize = field("PageSize")
    NextPageToken = field("NextPageToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRightsizingRecommendationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRightsizingRecommendationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSavingsPlansCoverageRequest:
    boto3_raw_data: "type_defs.GetSavingsPlansCoverageRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["TimePeriod"])

    @cached_property
    def GroupBy(self):  # pragma: no cover
        return GroupDefinition.make_many(self.boto3_raw_data["GroupBy"])

    Granularity = field("Granularity")
    Filter = field("Filter")
    Metrics = field("Metrics")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def SortBy(self):  # pragma: no cover
        return SortDefinition.make_one(self.boto3_raw_data["SortBy"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSavingsPlansCoverageRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSavingsPlansCoverageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSavingsPlansPurchaseRecommendationRequest:
    boto3_raw_data: "type_defs.GetSavingsPlansPurchaseRecommendationRequestTypeDef" = (
        dataclasses.field()
    )

    SavingsPlansType = field("SavingsPlansType")
    TermInYears = field("TermInYears")
    PaymentOption = field("PaymentOption")
    LookbackPeriodInDays = field("LookbackPeriodInDays")
    AccountScope = field("AccountScope")
    NextPageToken = field("NextPageToken")
    PageSize = field("PageSize")
    Filter = field("Filter")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSavingsPlansPurchaseRecommendationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSavingsPlansPurchaseRecommendationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSavingsPlansUtilizationDetailsRequest:
    boto3_raw_data: "type_defs.GetSavingsPlansUtilizationDetailsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["TimePeriod"])

    Filter = field("Filter")
    DataType = field("DataType")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def SortBy(self):  # pragma: no cover
        return SortDefinition.make_one(self.boto3_raw_data["SortBy"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSavingsPlansUtilizationDetailsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSavingsPlansUtilizationDetailsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSavingsPlansUtilizationRequest:
    boto3_raw_data: "type_defs.GetSavingsPlansUtilizationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["TimePeriod"])

    Granularity = field("Granularity")
    Filter = field("Filter")

    @cached_property
    def SortBy(self):  # pragma: no cover
        return SortDefinition.make_one(self.boto3_raw_data["SortBy"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSavingsPlansUtilizationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSavingsPlansUtilizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTagsRequest:
    boto3_raw_data: "type_defs.GetTagsRequestTypeDef" = dataclasses.field()

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["TimePeriod"])

    SearchString = field("SearchString")
    TagKey = field("TagKey")
    Filter = field("Filter")

    @cached_property
    def SortBy(self):  # pragma: no cover
        return SortDefinition.make_many(self.boto3_raw_data["SortBy"])

    BillingViewArn = field("BillingViewArn")
    MaxResults = field("MaxResults")
    NextPageToken = field("NextPageToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTagsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetTagsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUsageForecastRequest:
    boto3_raw_data: "type_defs.GetUsageForecastRequestTypeDef" = dataclasses.field()

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return DateInterval.make_one(self.boto3_raw_data["TimePeriod"])

    Metric = field("Metric")
    Granularity = field("Granularity")
    Filter = field("Filter")
    BillingViewArn = field("BillingViewArn")
    PredictionIntervalLevel = field("PredictionIntervalLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUsageForecastRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUsageForecastRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAnomalySubscriptionRequest:
    boto3_raw_data: "type_defs.UpdateAnomalySubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    SubscriptionArn = field("SubscriptionArn")
    Threshold = field("Threshold")
    Frequency = field("Frequency")
    MonitorArnList = field("MonitorArnList")

    @cached_property
    def Subscribers(self):  # pragma: no cover
        return Subscriber.make_many(self.boto3_raw_data["Subscribers"])

    SubscriptionName = field("SubscriptionName")
    ThresholdExpression = field("ThresholdExpression")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAnomalySubscriptionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAnomalySubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReservationPurchaseRecommendationResponse:
    boto3_raw_data: "type_defs.GetReservationPurchaseRecommendationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Metadata(self):  # pragma: no cover
        return ReservationPurchaseRecommendationMetadata.make_one(
            self.boto3_raw_data["Metadata"]
        )

    @cached_property
    def Recommendations(self):  # pragma: no cover
        return ReservationPurchaseRecommendation.make_many(
            self.boto3_raw_data["Recommendations"]
        )

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetReservationPurchaseRecommendationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReservationPurchaseRecommendationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCommitmentPurchaseAnalysesResponse:
    boto3_raw_data: "type_defs.ListCommitmentPurchaseAnalysesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AnalysisSummaryList(self):  # pragma: no cover
        return AnalysisSummary.make_many(self.boto3_raw_data["AnalysisSummaryList"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCommitmentPurchaseAnalysesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCommitmentPurchaseAnalysesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCommitmentPurchaseAnalysisRequest:
    boto3_raw_data: "type_defs.StartCommitmentPurchaseAnalysisRequestTypeDef" = (
        dataclasses.field()
    )

    CommitmentPurchaseAnalysisConfiguration = field(
        "CommitmentPurchaseAnalysisConfiguration"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartCommitmentPurchaseAnalysisRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCommitmentPurchaseAnalysisRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RightsizingRecommendation:
    boto3_raw_data: "type_defs.RightsizingRecommendationTypeDef" = dataclasses.field()

    AccountId = field("AccountId")

    @cached_property
    def CurrentInstance(self):  # pragma: no cover
        return CurrentInstance.make_one(self.boto3_raw_data["CurrentInstance"])

    RightsizingType = field("RightsizingType")

    @cached_property
    def ModifyRecommendationDetail(self):  # pragma: no cover
        return ModifyRecommendationDetail.make_one(
            self.boto3_raw_data["ModifyRecommendationDetail"]
        )

    @cached_property
    def TerminateRecommendationDetail(self):  # pragma: no cover
        return TerminateRecommendationDetail.make_one(
            self.boto3_raw_data["TerminateRecommendationDetail"]
        )

    FindingReasonCodes = field("FindingReasonCodes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RightsizingRecommendationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RightsizingRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAnomalyMonitorRequest:
    boto3_raw_data: "type_defs.CreateAnomalyMonitorRequestTypeDef" = dataclasses.field()

    AnomalyMonitor = field("AnomalyMonitor")

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ResourceTags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAnomalyMonitorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAnomalyMonitorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAnomalySubscriptionRequest:
    boto3_raw_data: "type_defs.CreateAnomalySubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    AnomalySubscription = field("AnomalySubscription")

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ResourceTags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAnomalySubscriptionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAnomalySubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRightsizingRecommendationResponse:
    boto3_raw_data: "type_defs.GetRightsizingRecommendationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Metadata(self):  # pragma: no cover
        return RightsizingRecommendationMetadata.make_one(
            self.boto3_raw_data["Metadata"]
        )

    @cached_property
    def Summary(self):  # pragma: no cover
        return RightsizingRecommendationSummary.make_one(self.boto3_raw_data["Summary"])

    @cached_property
    def RightsizingRecommendations(self):  # pragma: no cover
        return RightsizingRecommendation.make_many(
            self.boto3_raw_data["RightsizingRecommendations"]
        )

    NextPageToken = field("NextPageToken")

    @cached_property
    def Configuration(self):  # pragma: no cover
        return RightsizingRecommendationConfiguration.make_one(
            self.boto3_raw_data["Configuration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRightsizingRecommendationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRightsizingRecommendationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCostCategoryDefinitionRequest:
    boto3_raw_data: "type_defs.CreateCostCategoryDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    RuleVersion = field("RuleVersion")
    Rules = field("Rules")
    EffectiveStart = field("EffectiveStart")
    DefaultValue = field("DefaultValue")
    SplitChargeRules = field("SplitChargeRules")

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ResourceTags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCostCategoryDefinitionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCostCategoryDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCostCategoryDefinitionRequest:
    boto3_raw_data: "type_defs.UpdateCostCategoryDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    CostCategoryArn = field("CostCategoryArn")
    RuleVersion = field("RuleVersion")
    Rules = field("Rules")
    EffectiveStart = field("EffectiveStart")
    DefaultValue = field("DefaultValue")
    SplitChargeRules = field("SplitChargeRules")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCostCategoryDefinitionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCostCategoryDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
