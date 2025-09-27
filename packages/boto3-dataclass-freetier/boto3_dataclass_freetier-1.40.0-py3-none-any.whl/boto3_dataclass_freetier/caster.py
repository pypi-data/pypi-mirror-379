# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_freetier import type_defs as bs_td


class FREETIERCaster:

    def get_account_activity(
        self,
        res: "bs_td.GetAccountActivityResponseTypeDef",
    ) -> "dc_td.GetAccountActivityResponse":
        return dc_td.GetAccountActivityResponse.make_one(res)

    def get_account_plan_state(
        self,
        res: "bs_td.GetAccountPlanStateResponseTypeDef",
    ) -> "dc_td.GetAccountPlanStateResponse":
        return dc_td.GetAccountPlanStateResponse.make_one(res)

    def get_free_tier_usage(
        self,
        res: "bs_td.GetFreeTierUsageResponseTypeDef",
    ) -> "dc_td.GetFreeTierUsageResponse":
        return dc_td.GetFreeTierUsageResponse.make_one(res)

    def list_account_activities(
        self,
        res: "bs_td.ListAccountActivitiesResponseTypeDef",
    ) -> "dc_td.ListAccountActivitiesResponse":
        return dc_td.ListAccountActivitiesResponse.make_one(res)

    def upgrade_account_plan(
        self,
        res: "bs_td.UpgradeAccountPlanResponseTypeDef",
    ) -> "dc_td.UpgradeAccountPlanResponse":
        return dc_td.UpgradeAccountPlanResponse.make_one(res)


freetier_caster = FREETIERCaster()
