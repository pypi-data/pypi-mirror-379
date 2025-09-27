# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_aiops import type_defs as bs_td


class AIOPSCaster:

    def create_investigation_group(
        self,
        res: "bs_td.CreateInvestigationGroupOutputTypeDef",
    ) -> "dc_td.CreateInvestigationGroupOutput":
        return dc_td.CreateInvestigationGroupOutput.make_one(res)

    def delete_investigation_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_investigation_group(
        self,
        res: "bs_td.GetInvestigationGroupResponseTypeDef",
    ) -> "dc_td.GetInvestigationGroupResponse":
        return dc_td.GetInvestigationGroupResponse.make_one(res)

    def get_investigation_group_policy(
        self,
        res: "bs_td.GetInvestigationGroupPolicyResponseTypeDef",
    ) -> "dc_td.GetInvestigationGroupPolicyResponse":
        return dc_td.GetInvestigationGroupPolicyResponse.make_one(res)

    def list_investigation_groups(
        self,
        res: "bs_td.ListInvestigationGroupsOutputTypeDef",
    ) -> "dc_td.ListInvestigationGroupsOutput":
        return dc_td.ListInvestigationGroupsOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def put_investigation_group_policy(
        self,
        res: "bs_td.PutInvestigationGroupPolicyResponseTypeDef",
    ) -> "dc_td.PutInvestigationGroupPolicyResponse":
        return dc_td.PutInvestigationGroupPolicyResponse.make_one(res)


aiops_caster = AIOPSCaster()
