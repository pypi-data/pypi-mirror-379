# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_controlcatalog import type_defs as bs_td


class CONTROLCATALOGCaster:

    def get_control(
        self,
        res: "bs_td.GetControlResponseTypeDef",
    ) -> "dc_td.GetControlResponse":
        return dc_td.GetControlResponse.make_one(res)

    def list_common_controls(
        self,
        res: "bs_td.ListCommonControlsResponseTypeDef",
    ) -> "dc_td.ListCommonControlsResponse":
        return dc_td.ListCommonControlsResponse.make_one(res)

    def list_control_mappings(
        self,
        res: "bs_td.ListControlMappingsResponseTypeDef",
    ) -> "dc_td.ListControlMappingsResponse":
        return dc_td.ListControlMappingsResponse.make_one(res)

    def list_controls(
        self,
        res: "bs_td.ListControlsResponseTypeDef",
    ) -> "dc_td.ListControlsResponse":
        return dc_td.ListControlsResponse.make_one(res)

    def list_domains(
        self,
        res: "bs_td.ListDomainsResponseTypeDef",
    ) -> "dc_td.ListDomainsResponse":
        return dc_td.ListDomainsResponse.make_one(res)

    def list_objectives(
        self,
        res: "bs_td.ListObjectivesResponseTypeDef",
    ) -> "dc_td.ListObjectivesResponse":
        return dc_td.ListObjectivesResponse.make_one(res)


controlcatalog_caster = CONTROLCATALOGCaster()
