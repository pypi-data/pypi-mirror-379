# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_freetier import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class MonetaryAmount:
    boto3_raw_data: "type_defs.MonetaryAmountTypeDef" = dataclasses.field()

    amount = field("amount")
    unit = field("unit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MonetaryAmountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MonetaryAmountTypeDef"]],
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
class FreeTierUsage:
    boto3_raw_data: "type_defs.FreeTierUsageTypeDef" = dataclasses.field()

    service = field("service")
    operation = field("operation")
    usageType = field("usageType")
    region = field("region")
    actualUsageAmount = field("actualUsageAmount")
    forecastedUsageAmount = field("forecastedUsageAmount")
    limit = field("limit")
    unit = field("unit")
    description = field("description")
    freeTierType = field("freeTierType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FreeTierUsageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FreeTierUsageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountActivityRequest:
    boto3_raw_data: "type_defs.GetAccountActivityRequestTypeDef" = dataclasses.field()

    activityId = field("activityId")
    languageCode = field("languageCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccountActivityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountActivityRequestTypeDef"]
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
class ListAccountActivitiesRequest:
    boto3_raw_data: "type_defs.ListAccountActivitiesRequestTypeDef" = (
        dataclasses.field()
    )

    filterActivityStatuses = field("filterActivityStatuses")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    languageCode = field("languageCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccountActivitiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountActivitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpgradeAccountPlanRequest:
    boto3_raw_data: "type_defs.UpgradeAccountPlanRequestTypeDef" = dataclasses.field()

    accountPlanType = field("accountPlanType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpgradeAccountPlanRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpgradeAccountPlanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivityReward:
    boto3_raw_data: "type_defs.ActivityRewardTypeDef" = dataclasses.field()

    @cached_property
    def credit(self):  # pragma: no cover
        return MonetaryAmount.make_one(self.boto3_raw_data["credit"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActivityRewardTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActivityRewardTypeDef"]],
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
class Expression:
    boto3_raw_data: "type_defs.ExpressionTypeDef" = dataclasses.field()

    Or = field("Or")
    And = field("And")
    Not = field("Not")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return DimensionValues.make_one(self.boto3_raw_data["Dimensions"])

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
class GetAccountPlanStateResponse:
    boto3_raw_data: "type_defs.GetAccountPlanStateResponseTypeDef" = dataclasses.field()

    accountId = field("accountId")
    accountPlanType = field("accountPlanType")
    accountPlanStatus = field("accountPlanStatus")

    @cached_property
    def accountPlanRemainingCredits(self):  # pragma: no cover
        return MonetaryAmount.make_one(
            self.boto3_raw_data["accountPlanRemainingCredits"]
        )

    accountPlanExpirationDate = field("accountPlanExpirationDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccountPlanStateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountPlanStateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFreeTierUsageResponse:
    boto3_raw_data: "type_defs.GetFreeTierUsageResponseTypeDef" = dataclasses.field()

    @cached_property
    def freeTierUsages(self):  # pragma: no cover
        return FreeTierUsage.make_many(self.boto3_raw_data["freeTierUsages"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFreeTierUsageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFreeTierUsageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpgradeAccountPlanResponse:
    boto3_raw_data: "type_defs.UpgradeAccountPlanResponseTypeDef" = dataclasses.field()

    accountId = field("accountId")
    accountPlanType = field("accountPlanType")
    accountPlanStatus = field("accountPlanStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpgradeAccountPlanResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpgradeAccountPlanResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountActivitiesRequestPaginate:
    boto3_raw_data: "type_defs.ListAccountActivitiesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    filterActivityStatuses = field("filterActivityStatuses")
    languageCode = field("languageCode")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccountActivitiesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountActivitiesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivitySummary:
    boto3_raw_data: "type_defs.ActivitySummaryTypeDef" = dataclasses.field()

    activityId = field("activityId")
    title = field("title")

    @cached_property
    def reward(self):  # pragma: no cover
        return ActivityReward.make_one(self.boto3_raw_data["reward"])

    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActivitySummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActivitySummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountActivityResponse:
    boto3_raw_data: "type_defs.GetAccountActivityResponseTypeDef" = dataclasses.field()

    activityId = field("activityId")
    title = field("title")
    description = field("description")
    status = field("status")
    instructionsUrl = field("instructionsUrl")

    @cached_property
    def reward(self):  # pragma: no cover
        return ActivityReward.make_one(self.boto3_raw_data["reward"])

    estimatedTimeToCompleteInMinutes = field("estimatedTimeToCompleteInMinutes")
    expiresAt = field("expiresAt")
    startedAt = field("startedAt")
    completedAt = field("completedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccountActivityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountActivityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFreeTierUsageRequestPaginate:
    boto3_raw_data: "type_defs.GetFreeTierUsageRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filter(self):  # pragma: no cover
        return ExpressionPaginator.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetFreeTierUsageRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFreeTierUsageRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFreeTierUsageRequest:
    boto3_raw_data: "type_defs.GetFreeTierUsageRequestTypeDef" = dataclasses.field()

    @cached_property
    def filter(self):  # pragma: no cover
        return Expression.make_one(self.boto3_raw_data["filter"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFreeTierUsageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFreeTierUsageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountActivitiesResponse:
    boto3_raw_data: "type_defs.ListAccountActivitiesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def activities(self):  # pragma: no cover
        return ActivitySummary.make_many(self.boto3_raw_data["activities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccountActivitiesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountActivitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
