# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_budgets import type_defs as bs_td


class BUDGETSCaster:

    def create_budget_action(
        self,
        res: "bs_td.CreateBudgetActionResponseTypeDef",
    ) -> "dc_td.CreateBudgetActionResponse":
        return dc_td.CreateBudgetActionResponse.make_one(res)

    def delete_budget_action(
        self,
        res: "bs_td.DeleteBudgetActionResponseTypeDef",
    ) -> "dc_td.DeleteBudgetActionResponse":
        return dc_td.DeleteBudgetActionResponse.make_one(res)

    def describe_budget(
        self,
        res: "bs_td.DescribeBudgetResponseTypeDef",
    ) -> "dc_td.DescribeBudgetResponse":
        return dc_td.DescribeBudgetResponse.make_one(res)

    def describe_budget_action(
        self,
        res: "bs_td.DescribeBudgetActionResponseTypeDef",
    ) -> "dc_td.DescribeBudgetActionResponse":
        return dc_td.DescribeBudgetActionResponse.make_one(res)

    def describe_budget_action_histories(
        self,
        res: "bs_td.DescribeBudgetActionHistoriesResponseTypeDef",
    ) -> "dc_td.DescribeBudgetActionHistoriesResponse":
        return dc_td.DescribeBudgetActionHistoriesResponse.make_one(res)

    def describe_budget_actions_for_account(
        self,
        res: "bs_td.DescribeBudgetActionsForAccountResponseTypeDef",
    ) -> "dc_td.DescribeBudgetActionsForAccountResponse":
        return dc_td.DescribeBudgetActionsForAccountResponse.make_one(res)

    def describe_budget_actions_for_budget(
        self,
        res: "bs_td.DescribeBudgetActionsForBudgetResponseTypeDef",
    ) -> "dc_td.DescribeBudgetActionsForBudgetResponse":
        return dc_td.DescribeBudgetActionsForBudgetResponse.make_one(res)

    def describe_budget_notifications_for_account(
        self,
        res: "bs_td.DescribeBudgetNotificationsForAccountResponseTypeDef",
    ) -> "dc_td.DescribeBudgetNotificationsForAccountResponse":
        return dc_td.DescribeBudgetNotificationsForAccountResponse.make_one(res)

    def describe_budget_performance_history(
        self,
        res: "bs_td.DescribeBudgetPerformanceHistoryResponseTypeDef",
    ) -> "dc_td.DescribeBudgetPerformanceHistoryResponse":
        return dc_td.DescribeBudgetPerformanceHistoryResponse.make_one(res)

    def describe_budgets(
        self,
        res: "bs_td.DescribeBudgetsResponseTypeDef",
    ) -> "dc_td.DescribeBudgetsResponse":
        return dc_td.DescribeBudgetsResponse.make_one(res)

    def describe_notifications_for_budget(
        self,
        res: "bs_td.DescribeNotificationsForBudgetResponseTypeDef",
    ) -> "dc_td.DescribeNotificationsForBudgetResponse":
        return dc_td.DescribeNotificationsForBudgetResponse.make_one(res)

    def describe_subscribers_for_notification(
        self,
        res: "bs_td.DescribeSubscribersForNotificationResponseTypeDef",
    ) -> "dc_td.DescribeSubscribersForNotificationResponse":
        return dc_td.DescribeSubscribersForNotificationResponse.make_one(res)

    def execute_budget_action(
        self,
        res: "bs_td.ExecuteBudgetActionResponseTypeDef",
    ) -> "dc_td.ExecuteBudgetActionResponse":
        return dc_td.ExecuteBudgetActionResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def update_budget_action(
        self,
        res: "bs_td.UpdateBudgetActionResponseTypeDef",
    ) -> "dc_td.UpdateBudgetActionResponse":
        return dc_td.UpdateBudgetActionResponse.make_one(res)


budgets_caster = BUDGETSCaster()
