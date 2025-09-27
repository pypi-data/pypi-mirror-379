# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cost_optimization_hub import type_defs as bs_td


class COST_OPTIMIZATION_HUBCaster:

    def get_preferences(
        self,
        res: "bs_td.GetPreferencesResponseTypeDef",
    ) -> "dc_td.GetPreferencesResponse":
        return dc_td.GetPreferencesResponse.make_one(res)

    def get_recommendation(
        self,
        res: "bs_td.GetRecommendationResponseTypeDef",
    ) -> "dc_td.GetRecommendationResponse":
        return dc_td.GetRecommendationResponse.make_one(res)

    def list_enrollment_statuses(
        self,
        res: "bs_td.ListEnrollmentStatusesResponseTypeDef",
    ) -> "dc_td.ListEnrollmentStatusesResponse":
        return dc_td.ListEnrollmentStatusesResponse.make_one(res)

    def list_recommendation_summaries(
        self,
        res: "bs_td.ListRecommendationSummariesResponseTypeDef",
    ) -> "dc_td.ListRecommendationSummariesResponse":
        return dc_td.ListRecommendationSummariesResponse.make_one(res)

    def list_recommendations(
        self,
        res: "bs_td.ListRecommendationsResponseTypeDef",
    ) -> "dc_td.ListRecommendationsResponse":
        return dc_td.ListRecommendationsResponse.make_one(res)

    def update_enrollment_status(
        self,
        res: "bs_td.UpdateEnrollmentStatusResponseTypeDef",
    ) -> "dc_td.UpdateEnrollmentStatusResponse":
        return dc_td.UpdateEnrollmentStatusResponse.make_one(res)

    def update_preferences(
        self,
        res: "bs_td.UpdatePreferencesResponseTypeDef",
    ) -> "dc_td.UpdatePreferencesResponse":
        return dc_td.UpdatePreferencesResponse.make_one(res)


cost_optimization_hub_caster = COST_OPTIMIZATION_HUBCaster()
