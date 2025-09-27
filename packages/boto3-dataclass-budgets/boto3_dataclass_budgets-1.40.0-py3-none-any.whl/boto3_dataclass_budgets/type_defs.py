# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_budgets import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ActionThreshold:
    boto3_raw_data: "type_defs.ActionThresholdTypeDef" = dataclasses.field()

    ActionThresholdValue = field("ActionThresholdValue")
    ActionThresholdType = field("ActionThresholdType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionThresholdTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionThresholdTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Subscriber:
    boto3_raw_data: "type_defs.SubscriberTypeDef" = dataclasses.field()

    SubscriptionType = field("SubscriptionType")
    Address = field("Address")

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
class HistoricalOptions:
    boto3_raw_data: "type_defs.HistoricalOptionsTypeDef" = dataclasses.field()

    BudgetAdjustmentPeriod = field("BudgetAdjustmentPeriod")
    LookBackAvailablePeriods = field("LookBackAvailablePeriods")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HistoricalOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HistoricalOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Notification:
    boto3_raw_data: "type_defs.NotificationTypeDef" = dataclasses.field()

    NotificationType = field("NotificationType")
    ComparisonOperator = field("ComparisonOperator")
    Threshold = field("Threshold")
    ThresholdType = field("ThresholdType")
    NotificationState = field("NotificationState")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NotificationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NotificationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostTypes:
    boto3_raw_data: "type_defs.CostTypesTypeDef" = dataclasses.field()

    IncludeTax = field("IncludeTax")
    IncludeSubscription = field("IncludeSubscription")
    UseBlended = field("UseBlended")
    IncludeRefund = field("IncludeRefund")
    IncludeCredit = field("IncludeCredit")
    IncludeUpfront = field("IncludeUpfront")
    IncludeRecurring = field("IncludeRecurring")
    IncludeOtherSubscription = field("IncludeOtherSubscription")
    IncludeSupport = field("IncludeSupport")
    IncludeDiscount = field("IncludeDiscount")
    UseAmortized = field("UseAmortized")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CostTypesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CostTypesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HealthStatusOutput:
    boto3_raw_data: "type_defs.HealthStatusOutputTypeDef" = dataclasses.field()

    Status = field("Status")
    StatusReason = field("StatusReason")
    LastUpdatedTime = field("LastUpdatedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HealthStatusOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HealthStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Spend:
    boto3_raw_data: "type_defs.SpendTypeDef" = dataclasses.field()

    Amount = field("Amount")
    Unit = field("Unit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SpendTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SpendTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimePeriodOutput:
    boto3_raw_data: "type_defs.TimePeriodOutputTypeDef" = dataclasses.field()

    Start = field("Start")
    End = field("End")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimePeriodOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimePeriodOutputTypeDef"]
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
class IamActionDefinitionOutput:
    boto3_raw_data: "type_defs.IamActionDefinitionOutputTypeDef" = dataclasses.field()

    PolicyArn = field("PolicyArn")
    Roles = field("Roles")
    Groups = field("Groups")
    Users = field("Users")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IamActionDefinitionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IamActionDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScpActionDefinitionOutput:
    boto3_raw_data: "type_defs.ScpActionDefinitionOutputTypeDef" = dataclasses.field()

    PolicyId = field("PolicyId")
    TargetIds = field("TargetIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScpActionDefinitionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScpActionDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SsmActionDefinitionOutput:
    boto3_raw_data: "type_defs.SsmActionDefinitionOutputTypeDef" = dataclasses.field()

    ActionSubType = field("ActionSubType")
    Region = field("Region")
    InstanceIds = field("InstanceIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SsmActionDefinitionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SsmActionDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IamActionDefinition:
    boto3_raw_data: "type_defs.IamActionDefinitionTypeDef" = dataclasses.field()

    PolicyArn = field("PolicyArn")
    Roles = field("Roles")
    Groups = field("Groups")
    Users = field("Users")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IamActionDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IamActionDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScpActionDefinition:
    boto3_raw_data: "type_defs.ScpActionDefinitionTypeDef" = dataclasses.field()

    PolicyId = field("PolicyId")
    TargetIds = field("TargetIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScpActionDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScpActionDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SsmActionDefinition:
    boto3_raw_data: "type_defs.SsmActionDefinitionTypeDef" = dataclasses.field()

    ActionSubType = field("ActionSubType")
    Region = field("Region")
    InstanceIds = field("InstanceIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SsmActionDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SsmActionDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBudgetActionRequest:
    boto3_raw_data: "type_defs.DeleteBudgetActionRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")
    ActionId = field("ActionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBudgetActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBudgetActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBudgetRequest:
    boto3_raw_data: "type_defs.DeleteBudgetRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBudgetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBudgetRequestTypeDef"]
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
class DescribeBudgetActionRequest:
    boto3_raw_data: "type_defs.DescribeBudgetActionRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")
    ActionId = field("ActionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBudgetActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBudgetActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBudgetActionsForAccountRequest:
    boto3_raw_data: "type_defs.DescribeBudgetActionsForAccountRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBudgetActionsForAccountRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBudgetActionsForAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBudgetActionsForBudgetRequest:
    boto3_raw_data: "type_defs.DescribeBudgetActionsForBudgetRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBudgetActionsForBudgetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBudgetActionsForBudgetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBudgetNotificationsForAccountRequest:
    boto3_raw_data: "type_defs.DescribeBudgetNotificationsForAccountRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBudgetNotificationsForAccountRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBudgetNotificationsForAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBudgetRequest:
    boto3_raw_data: "type_defs.DescribeBudgetRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")
    ShowFilterExpression = field("ShowFilterExpression")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBudgetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBudgetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBudgetsRequest:
    boto3_raw_data: "type_defs.DescribeBudgetsRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    ShowFilterExpression = field("ShowFilterExpression")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBudgetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBudgetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNotificationsForBudgetRequest:
    boto3_raw_data: "type_defs.DescribeNotificationsForBudgetRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeNotificationsForBudgetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNotificationsForBudgetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteBudgetActionRequest:
    boto3_raw_data: "type_defs.ExecuteBudgetActionRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")
    ActionId = field("ActionId")
    ExecutionType = field("ExecutionType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteBudgetActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteBudgetActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpressionDimensionValuesOutput:
    boto3_raw_data: "type_defs.ExpressionDimensionValuesOutputTypeDef" = (
        dataclasses.field()
    )

    Key = field("Key")
    Values = field("Values")
    MatchOptions = field("MatchOptions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExpressionDimensionValuesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpressionDimensionValuesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpressionDimensionValues:
    boto3_raw_data: "type_defs.ExpressionDimensionValuesTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")
    MatchOptions = field("MatchOptions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExpressionDimensionValuesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpressionDimensionValuesTypeDef"]
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
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
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
class AutoAdjustDataOutput:
    boto3_raw_data: "type_defs.AutoAdjustDataOutputTypeDef" = dataclasses.field()

    AutoAdjustType = field("AutoAdjustType")

    @cached_property
    def HistoricalOptions(self):  # pragma: no cover
        return HistoricalOptions.make_one(self.boto3_raw_data["HistoricalOptions"])

    LastAutoAdjustTime = field("LastAutoAdjustTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoAdjustDataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoAdjustDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoAdjustData:
    boto3_raw_data: "type_defs.AutoAdjustDataTypeDef" = dataclasses.field()

    AutoAdjustType = field("AutoAdjustType")

    @cached_property
    def HistoricalOptions(self):  # pragma: no cover
        return HistoricalOptions.make_one(self.boto3_raw_data["HistoricalOptions"])

    LastAutoAdjustTime = field("LastAutoAdjustTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoAdjustDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AutoAdjustDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HealthStatus:
    boto3_raw_data: "type_defs.HealthStatusTypeDef" = dataclasses.field()

    Status = field("Status")
    StatusReason = field("StatusReason")
    LastUpdatedTime = field("LastUpdatedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HealthStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HealthStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimePeriod:
    boto3_raw_data: "type_defs.TimePeriodTypeDef" = dataclasses.field()

    Start = field("Start")
    End = field("End")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimePeriodTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimePeriodTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BudgetNotificationsForAccount:
    boto3_raw_data: "type_defs.BudgetNotificationsForAccountTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Notifications(self):  # pragma: no cover
        return Notification.make_many(self.boto3_raw_data["Notifications"])

    BudgetName = field("BudgetName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BudgetNotificationsForAccountTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BudgetNotificationsForAccountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNotificationRequest:
    boto3_raw_data: "type_defs.CreateNotificationRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")

    @cached_property
    def Notification(self):  # pragma: no cover
        return Notification.make_one(self.boto3_raw_data["Notification"])

    @cached_property
    def Subscribers(self):  # pragma: no cover
        return Subscriber.make_many(self.boto3_raw_data["Subscribers"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateNotificationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNotificationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSubscriberRequest:
    boto3_raw_data: "type_defs.CreateSubscriberRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")

    @cached_property
    def Notification(self):  # pragma: no cover
        return Notification.make_one(self.boto3_raw_data["Notification"])

    @cached_property
    def Subscriber(self):  # pragma: no cover
        return Subscriber.make_one(self.boto3_raw_data["Subscriber"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSubscriberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSubscriberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteNotificationRequest:
    boto3_raw_data: "type_defs.DeleteNotificationRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")

    @cached_property
    def Notification(self):  # pragma: no cover
        return Notification.make_one(self.boto3_raw_data["Notification"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteNotificationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteNotificationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSubscriberRequest:
    boto3_raw_data: "type_defs.DeleteSubscriberRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")

    @cached_property
    def Notification(self):  # pragma: no cover
        return Notification.make_one(self.boto3_raw_data["Notification"])

    @cached_property
    def Subscriber(self):  # pragma: no cover
        return Subscriber.make_one(self.boto3_raw_data["Subscriber"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSubscriberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSubscriberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSubscribersForNotificationRequest:
    boto3_raw_data: "type_defs.DescribeSubscribersForNotificationRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")

    @cached_property
    def Notification(self):  # pragma: no cover
        return Notification.make_one(self.boto3_raw_data["Notification"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSubscribersForNotificationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSubscribersForNotificationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationWithSubscribers:
    boto3_raw_data: "type_defs.NotificationWithSubscribersTypeDef" = dataclasses.field()

    @cached_property
    def Notification(self):  # pragma: no cover
        return Notification.make_one(self.boto3_raw_data["Notification"])

    @cached_property
    def Subscribers(self):  # pragma: no cover
        return Subscriber.make_many(self.boto3_raw_data["Subscribers"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationWithSubscribersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationWithSubscribersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNotificationRequest:
    boto3_raw_data: "type_defs.UpdateNotificationRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")

    @cached_property
    def OldNotification(self):  # pragma: no cover
        return Notification.make_one(self.boto3_raw_data["OldNotification"])

    @cached_property
    def NewNotification(self):  # pragma: no cover
        return Notification.make_one(self.boto3_raw_data["NewNotification"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateNotificationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNotificationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSubscriberRequest:
    boto3_raw_data: "type_defs.UpdateSubscriberRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")

    @cached_property
    def Notification(self):  # pragma: no cover
        return Notification.make_one(self.boto3_raw_data["Notification"])

    @cached_property
    def OldSubscriber(self):  # pragma: no cover
        return Subscriber.make_one(self.boto3_raw_data["OldSubscriber"])

    @cached_property
    def NewSubscriber(self):  # pragma: no cover
        return Subscriber.make_one(self.boto3_raw_data["NewSubscriber"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSubscriberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSubscriberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalculatedSpend:
    boto3_raw_data: "type_defs.CalculatedSpendTypeDef" = dataclasses.field()

    @cached_property
    def ActualSpend(self):  # pragma: no cover
        return Spend.make_one(self.boto3_raw_data["ActualSpend"])

    @cached_property
    def ForecastedSpend(self):  # pragma: no cover
        return Spend.make_one(self.boto3_raw_data["ForecastedSpend"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CalculatedSpendTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CalculatedSpendTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BudgetedAndActualAmounts:
    boto3_raw_data: "type_defs.BudgetedAndActualAmountsTypeDef" = dataclasses.field()

    @cached_property
    def BudgetedAmount(self):  # pragma: no cover
        return Spend.make_one(self.boto3_raw_data["BudgetedAmount"])

    @cached_property
    def ActualAmount(self):  # pragma: no cover
        return Spend.make_one(self.boto3_raw_data["ActualAmount"])

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return TimePeriodOutput.make_one(self.boto3_raw_data["TimePeriod"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BudgetedAndActualAmountsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BudgetedAndActualAmountsTypeDef"]
        ],
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
class CreateBudgetActionResponse:
    boto3_raw_data: "type_defs.CreateBudgetActionResponseTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")
    ActionId = field("ActionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBudgetActionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBudgetActionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNotificationsForBudgetResponse:
    boto3_raw_data: "type_defs.DescribeNotificationsForBudgetResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Notifications(self):  # pragma: no cover
        return Notification.make_many(self.boto3_raw_data["Notifications"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeNotificationsForBudgetResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNotificationsForBudgetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSubscribersForNotificationResponse:
    boto3_raw_data: "type_defs.DescribeSubscribersForNotificationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Subscribers(self):  # pragma: no cover
        return Subscriber.make_many(self.boto3_raw_data["Subscribers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSubscribersForNotificationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSubscribersForNotificationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteBudgetActionResponse:
    boto3_raw_data: "type_defs.ExecuteBudgetActionResponseTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")
    ActionId = field("ActionId")
    ExecutionType = field("ExecutionType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteBudgetActionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteBudgetActionResponseTypeDef"]
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
class DefinitionOutput:
    boto3_raw_data: "type_defs.DefinitionOutputTypeDef" = dataclasses.field()

    @cached_property
    def IamActionDefinition(self):  # pragma: no cover
        return IamActionDefinitionOutput.make_one(
            self.boto3_raw_data["IamActionDefinition"]
        )

    @cached_property
    def ScpActionDefinition(self):  # pragma: no cover
        return ScpActionDefinitionOutput.make_one(
            self.boto3_raw_data["ScpActionDefinition"]
        )

    @cached_property
    def SsmActionDefinition(self):  # pragma: no cover
        return SsmActionDefinitionOutput.make_one(
            self.boto3_raw_data["SsmActionDefinition"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DefinitionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Definition:
    boto3_raw_data: "type_defs.DefinitionTypeDef" = dataclasses.field()

    @cached_property
    def IamActionDefinition(self):  # pragma: no cover
        return IamActionDefinition.make_one(self.boto3_raw_data["IamActionDefinition"])

    @cached_property
    def ScpActionDefinition(self):  # pragma: no cover
        return ScpActionDefinition.make_one(self.boto3_raw_data["ScpActionDefinition"])

    @cached_property
    def SsmActionDefinition(self):  # pragma: no cover
        return SsmActionDefinition.make_one(self.boto3_raw_data["SsmActionDefinition"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DefinitionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBudgetActionsForAccountRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeBudgetActionsForAccountRequestPaginateTypeDef"
    ) = dataclasses.field()

    AccountId = field("AccountId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBudgetActionsForAccountRequestPaginateTypeDef"
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
                "type_defs.DescribeBudgetActionsForAccountRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBudgetActionsForBudgetRequestPaginate:
    boto3_raw_data: "type_defs.DescribeBudgetActionsForBudgetRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBudgetActionsForBudgetRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBudgetActionsForBudgetRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBudgetNotificationsForAccountRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeBudgetNotificationsForAccountRequestPaginateTypeDef"
    ) = dataclasses.field()

    AccountId = field("AccountId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBudgetNotificationsForAccountRequestPaginateTypeDef"
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
                "type_defs.DescribeBudgetNotificationsForAccountRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBudgetsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeBudgetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    ShowFilterExpression = field("ShowFilterExpression")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeBudgetsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBudgetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNotificationsForBudgetRequestPaginate:
    boto3_raw_data: "type_defs.DescribeNotificationsForBudgetRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeNotificationsForBudgetRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNotificationsForBudgetRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSubscribersForNotificationRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeSubscribersForNotificationRequestPaginateTypeDef"
    ) = dataclasses.field()

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")

    @cached_property
    def Notification(self):  # pragma: no cover
        return Notification.make_one(self.boto3_raw_data["Notification"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSubscribersForNotificationRequestPaginateTypeDef"
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
                "type_defs.DescribeSubscribersForNotificationRequestPaginateTypeDef"
            ]
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
        return ExpressionDimensionValuesOutput.make_one(
            self.boto3_raw_data["Dimensions"]
        )

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
class ExpressionPaginator:
    boto3_raw_data: "type_defs.ExpressionPaginatorTypeDef" = dataclasses.field()

    Or = field("Or")
    And = field("And")
    Not = field("Not")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return ExpressionDimensionValuesOutput.make_one(
            self.boto3_raw_data["Dimensions"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagValuesOutput.make_one(self.boto3_raw_data["Tags"])

    @cached_property
    def CostCategories(self):  # pragma: no cover
        return CostCategoryValuesOutput.make_one(self.boto3_raw_data["CostCategories"])

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
        return ExpressionDimensionValues.make_one(self.boto3_raw_data["Dimensions"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagValues.make_one(self.boto3_raw_data["Tags"])

    @cached_property
    def CostCategories(self):  # pragma: no cover
        return CostCategoryValues.make_one(self.boto3_raw_data["CostCategories"])

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
class DescribeBudgetNotificationsForAccountResponse:
    boto3_raw_data: "type_defs.DescribeBudgetNotificationsForAccountResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BudgetNotificationsForAccount(self):  # pragma: no cover
        return BudgetNotificationsForAccount.make_many(
            self.boto3_raw_data["BudgetNotificationsForAccount"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBudgetNotificationsForAccountResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBudgetNotificationsForAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BudgetPerformanceHistory:
    boto3_raw_data: "type_defs.BudgetPerformanceHistoryTypeDef" = dataclasses.field()

    BudgetName = field("BudgetName")
    BudgetType = field("BudgetType")
    CostFilters = field("CostFilters")

    @cached_property
    def CostTypes(self):  # pragma: no cover
        return CostTypes.make_one(self.boto3_raw_data["CostTypes"])

    TimeUnit = field("TimeUnit")
    BillingViewArn = field("BillingViewArn")

    @cached_property
    def BudgetedAndActualAmountsList(self):  # pragma: no cover
        return BudgetedAndActualAmounts.make_many(
            self.boto3_raw_data["BudgetedAndActualAmountsList"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BudgetPerformanceHistoryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BudgetPerformanceHistoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Action:
    boto3_raw_data: "type_defs.ActionTypeDef" = dataclasses.field()

    ActionId = field("ActionId")
    BudgetName = field("BudgetName")
    NotificationType = field("NotificationType")
    ActionType = field("ActionType")

    @cached_property
    def ActionThreshold(self):  # pragma: no cover
        return ActionThreshold.make_one(self.boto3_raw_data["ActionThreshold"])

    @cached_property
    def Definition(self):  # pragma: no cover
        return DefinitionOutput.make_one(self.boto3_raw_data["Definition"])

    ExecutionRoleArn = field("ExecutionRoleArn")
    ApprovalModel = field("ApprovalModel")
    Status = field("Status")

    @cached_property
    def Subscribers(self):  # pragma: no cover
        return Subscriber.make_many(self.boto3_raw_data["Subscribers"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BudgetOutput:
    boto3_raw_data: "type_defs.BudgetOutputTypeDef" = dataclasses.field()

    BudgetName = field("BudgetName")
    TimeUnit = field("TimeUnit")
    BudgetType = field("BudgetType")

    @cached_property
    def BudgetLimit(self):  # pragma: no cover
        return Spend.make_one(self.boto3_raw_data["BudgetLimit"])

    PlannedBudgetLimits = field("PlannedBudgetLimits")
    CostFilters = field("CostFilters")

    @cached_property
    def CostTypes(self):  # pragma: no cover
        return CostTypes.make_one(self.boto3_raw_data["CostTypes"])

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return TimePeriodOutput.make_one(self.boto3_raw_data["TimePeriod"])

    @cached_property
    def CalculatedSpend(self):  # pragma: no cover
        return CalculatedSpend.make_one(self.boto3_raw_data["CalculatedSpend"])

    LastUpdatedTime = field("LastUpdatedTime")

    @cached_property
    def AutoAdjustData(self):  # pragma: no cover
        return AutoAdjustDataOutput.make_one(self.boto3_raw_data["AutoAdjustData"])

    @cached_property
    def FilterExpression(self):  # pragma: no cover
        return ExpressionOutput.make_one(self.boto3_raw_data["FilterExpression"])

    Metrics = field("Metrics")
    BillingViewArn = field("BillingViewArn")

    @cached_property
    def HealthStatus(self):  # pragma: no cover
        return HealthStatusOutput.make_one(self.boto3_raw_data["HealthStatus"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BudgetOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BudgetOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BudgetPaginator:
    boto3_raw_data: "type_defs.BudgetPaginatorTypeDef" = dataclasses.field()

    BudgetName = field("BudgetName")
    TimeUnit = field("TimeUnit")
    BudgetType = field("BudgetType")

    @cached_property
    def BudgetLimit(self):  # pragma: no cover
        return Spend.make_one(self.boto3_raw_data["BudgetLimit"])

    PlannedBudgetLimits = field("PlannedBudgetLimits")
    CostFilters = field("CostFilters")

    @cached_property
    def CostTypes(self):  # pragma: no cover
        return CostTypes.make_one(self.boto3_raw_data["CostTypes"])

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return TimePeriodOutput.make_one(self.boto3_raw_data["TimePeriod"])

    @cached_property
    def CalculatedSpend(self):  # pragma: no cover
        return CalculatedSpend.make_one(self.boto3_raw_data["CalculatedSpend"])

    LastUpdatedTime = field("LastUpdatedTime")

    @cached_property
    def AutoAdjustData(self):  # pragma: no cover
        return AutoAdjustDataOutput.make_one(self.boto3_raw_data["AutoAdjustData"])

    @cached_property
    def FilterExpression(self):  # pragma: no cover
        return ExpressionPaginator.make_one(self.boto3_raw_data["FilterExpression"])

    Metrics = field("Metrics")
    BillingViewArn = field("BillingViewArn")

    @cached_property
    def HealthStatus(self):  # pragma: no cover
        return HealthStatusOutput.make_one(self.boto3_raw_data["HealthStatus"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BudgetPaginatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BudgetPaginatorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Budget:
    boto3_raw_data: "type_defs.BudgetTypeDef" = dataclasses.field()

    BudgetName = field("BudgetName")
    TimeUnit = field("TimeUnit")
    BudgetType = field("BudgetType")

    @cached_property
    def BudgetLimit(self):  # pragma: no cover
        return Spend.make_one(self.boto3_raw_data["BudgetLimit"])

    PlannedBudgetLimits = field("PlannedBudgetLimits")
    CostFilters = field("CostFilters")

    @cached_property
    def CostTypes(self):  # pragma: no cover
        return CostTypes.make_one(self.boto3_raw_data["CostTypes"])

    @cached_property
    def TimePeriod(self):  # pragma: no cover
        return TimePeriod.make_one(self.boto3_raw_data["TimePeriod"])

    @cached_property
    def CalculatedSpend(self):  # pragma: no cover
        return CalculatedSpend.make_one(self.boto3_raw_data["CalculatedSpend"])

    LastUpdatedTime = field("LastUpdatedTime")

    @cached_property
    def AutoAdjustData(self):  # pragma: no cover
        return AutoAdjustData.make_one(self.boto3_raw_data["AutoAdjustData"])

    @cached_property
    def FilterExpression(self):  # pragma: no cover
        return Expression.make_one(self.boto3_raw_data["FilterExpression"])

    Metrics = field("Metrics")
    BillingViewArn = field("BillingViewArn")

    @cached_property
    def HealthStatus(self):  # pragma: no cover
        return HealthStatus.make_one(self.boto3_raw_data["HealthStatus"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BudgetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BudgetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBudgetActionHistoriesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeBudgetActionHistoriesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")
    ActionId = field("ActionId")
    TimePeriod = field("TimePeriod")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBudgetActionHistoriesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBudgetActionHistoriesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBudgetActionHistoriesRequest:
    boto3_raw_data: "type_defs.DescribeBudgetActionHistoriesRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")
    ActionId = field("ActionId")
    TimePeriod = field("TimePeriod")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBudgetActionHistoriesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBudgetActionHistoriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBudgetPerformanceHistoryRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeBudgetPerformanceHistoryRequestPaginateTypeDef"
    ) = dataclasses.field()

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")
    TimePeriod = field("TimePeriod")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBudgetPerformanceHistoryRequestPaginateTypeDef"
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
                "type_defs.DescribeBudgetPerformanceHistoryRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBudgetPerformanceHistoryRequest:
    boto3_raw_data: "type_defs.DescribeBudgetPerformanceHistoryRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")
    TimePeriod = field("TimePeriod")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBudgetPerformanceHistoryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBudgetPerformanceHistoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBudgetPerformanceHistoryResponse:
    boto3_raw_data: "type_defs.DescribeBudgetPerformanceHistoryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BudgetPerformanceHistory(self):  # pragma: no cover
        return BudgetPerformanceHistory.make_one(
            self.boto3_raw_data["BudgetPerformanceHistory"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBudgetPerformanceHistoryResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBudgetPerformanceHistoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionHistoryDetails:
    boto3_raw_data: "type_defs.ActionHistoryDetailsTypeDef" = dataclasses.field()

    Message = field("Message")

    @cached_property
    def Action(self):  # pragma: no cover
        return Action.make_one(self.boto3_raw_data["Action"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionHistoryDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionHistoryDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBudgetActionResponse:
    boto3_raw_data: "type_defs.DeleteBudgetActionResponseTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")

    @cached_property
    def Action(self):  # pragma: no cover
        return Action.make_one(self.boto3_raw_data["Action"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBudgetActionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBudgetActionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBudgetActionResponse:
    boto3_raw_data: "type_defs.DescribeBudgetActionResponseTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")

    @cached_property
    def Action(self):  # pragma: no cover
        return Action.make_one(self.boto3_raw_data["Action"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBudgetActionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBudgetActionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBudgetActionsForAccountResponse:
    boto3_raw_data: "type_defs.DescribeBudgetActionsForAccountResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Actions(self):  # pragma: no cover
        return Action.make_many(self.boto3_raw_data["Actions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBudgetActionsForAccountResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBudgetActionsForAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBudgetActionsForBudgetResponse:
    boto3_raw_data: "type_defs.DescribeBudgetActionsForBudgetResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Actions(self):  # pragma: no cover
        return Action.make_many(self.boto3_raw_data["Actions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBudgetActionsForBudgetResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBudgetActionsForBudgetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBudgetActionResponse:
    boto3_raw_data: "type_defs.UpdateBudgetActionResponseTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")

    @cached_property
    def OldAction(self):  # pragma: no cover
        return Action.make_one(self.boto3_raw_data["OldAction"])

    @cached_property
    def NewAction(self):  # pragma: no cover
        return Action.make_one(self.boto3_raw_data["NewAction"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBudgetActionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBudgetActionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBudgetActionRequest:
    boto3_raw_data: "type_defs.CreateBudgetActionRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")
    NotificationType = field("NotificationType")
    ActionType = field("ActionType")

    @cached_property
    def ActionThreshold(self):  # pragma: no cover
        return ActionThreshold.make_one(self.boto3_raw_data["ActionThreshold"])

    Definition = field("Definition")
    ExecutionRoleArn = field("ExecutionRoleArn")
    ApprovalModel = field("ApprovalModel")

    @cached_property
    def Subscribers(self):  # pragma: no cover
        return Subscriber.make_many(self.boto3_raw_data["Subscribers"])

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ResourceTags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBudgetActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBudgetActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBudgetActionRequest:
    boto3_raw_data: "type_defs.UpdateBudgetActionRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    BudgetName = field("BudgetName")
    ActionId = field("ActionId")
    NotificationType = field("NotificationType")

    @cached_property
    def ActionThreshold(self):  # pragma: no cover
        return ActionThreshold.make_one(self.boto3_raw_data["ActionThreshold"])

    Definition = field("Definition")
    ExecutionRoleArn = field("ExecutionRoleArn")
    ApprovalModel = field("ApprovalModel")

    @cached_property
    def Subscribers(self):  # pragma: no cover
        return Subscriber.make_many(self.boto3_raw_data["Subscribers"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBudgetActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBudgetActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBudgetResponse:
    boto3_raw_data: "type_defs.DescribeBudgetResponseTypeDef" = dataclasses.field()

    @cached_property
    def Budget(self):  # pragma: no cover
        return BudgetOutput.make_one(self.boto3_raw_data["Budget"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBudgetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBudgetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBudgetsResponse:
    boto3_raw_data: "type_defs.DescribeBudgetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Budgets(self):  # pragma: no cover
        return BudgetOutput.make_many(self.boto3_raw_data["Budgets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBudgetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBudgetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBudgetsResponsePaginator:
    boto3_raw_data: "type_defs.DescribeBudgetsResponsePaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Budgets(self):  # pragma: no cover
        return BudgetPaginator.make_many(self.boto3_raw_data["Budgets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeBudgetsResponsePaginatorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBudgetsResponsePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionHistory:
    boto3_raw_data: "type_defs.ActionHistoryTypeDef" = dataclasses.field()

    Timestamp = field("Timestamp")
    Status = field("Status")
    EventType = field("EventType")

    @cached_property
    def ActionHistoryDetails(self):  # pragma: no cover
        return ActionHistoryDetails.make_one(
            self.boto3_raw_data["ActionHistoryDetails"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionHistoryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionHistoryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBudgetRequest:
    boto3_raw_data: "type_defs.CreateBudgetRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Budget = field("Budget")

    @cached_property
    def NotificationsWithSubscribers(self):  # pragma: no cover
        return NotificationWithSubscribers.make_many(
            self.boto3_raw_data["NotificationsWithSubscribers"]
        )

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ResourceTags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBudgetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBudgetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBudgetRequest:
    boto3_raw_data: "type_defs.UpdateBudgetRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    NewBudget = field("NewBudget")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBudgetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBudgetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBudgetActionHistoriesResponse:
    boto3_raw_data: "type_defs.DescribeBudgetActionHistoriesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ActionHistories(self):  # pragma: no cover
        return ActionHistory.make_many(self.boto3_raw_data["ActionHistories"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBudgetActionHistoriesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBudgetActionHistoriesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
