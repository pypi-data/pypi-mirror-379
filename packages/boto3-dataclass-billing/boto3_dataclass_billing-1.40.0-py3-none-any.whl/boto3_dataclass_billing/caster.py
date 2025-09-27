# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_billing import type_defs as bs_td


class BILLINGCaster:

    def create_billing_view(
        self,
        res: "bs_td.CreateBillingViewResponseTypeDef",
    ) -> "dc_td.CreateBillingViewResponse":
        return dc_td.CreateBillingViewResponse.make_one(res)

    def delete_billing_view(
        self,
        res: "bs_td.DeleteBillingViewResponseTypeDef",
    ) -> "dc_td.DeleteBillingViewResponse":
        return dc_td.DeleteBillingViewResponse.make_one(res)

    def get_billing_view(
        self,
        res: "bs_td.GetBillingViewResponseTypeDef",
    ) -> "dc_td.GetBillingViewResponse":
        return dc_td.GetBillingViewResponse.make_one(res)

    def get_resource_policy(
        self,
        res: "bs_td.GetResourcePolicyResponseTypeDef",
    ) -> "dc_td.GetResourcePolicyResponse":
        return dc_td.GetResourcePolicyResponse.make_one(res)

    def list_billing_views(
        self,
        res: "bs_td.ListBillingViewsResponseTypeDef",
    ) -> "dc_td.ListBillingViewsResponse":
        return dc_td.ListBillingViewsResponse.make_one(res)

    def list_source_views_for_billing_view(
        self,
        res: "bs_td.ListSourceViewsForBillingViewResponseTypeDef",
    ) -> "dc_td.ListSourceViewsForBillingViewResponse":
        return dc_td.ListSourceViewsForBillingViewResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def update_billing_view(
        self,
        res: "bs_td.UpdateBillingViewResponseTypeDef",
    ) -> "dc_td.UpdateBillingViewResponse":
        return dc_td.UpdateBillingViewResponse.make_one(res)


billing_caster = BILLINGCaster()
