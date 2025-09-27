# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_dlm import type_defs as bs_td


class DLMCaster:

    def create_lifecycle_policy(
        self,
        res: "bs_td.CreateLifecyclePolicyResponseTypeDef",
    ) -> "dc_td.CreateLifecyclePolicyResponse":
        return dc_td.CreateLifecyclePolicyResponse.make_one(res)

    def get_lifecycle_policies(
        self,
        res: "bs_td.GetLifecyclePoliciesResponseTypeDef",
    ) -> "dc_td.GetLifecyclePoliciesResponse":
        return dc_td.GetLifecyclePoliciesResponse.make_one(res)

    def get_lifecycle_policy(
        self,
        res: "bs_td.GetLifecyclePolicyResponseTypeDef",
    ) -> "dc_td.GetLifecyclePolicyResponse":
        return dc_td.GetLifecyclePolicyResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)


dlm_caster = DLMCaster()
