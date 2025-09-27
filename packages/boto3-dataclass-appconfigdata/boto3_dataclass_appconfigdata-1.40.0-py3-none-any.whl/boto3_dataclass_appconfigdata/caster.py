# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_appconfigdata import type_defs as bs_td


class APPCONFIGDATACaster:

    def get_latest_configuration(
        self,
        res: "bs_td.GetLatestConfigurationResponseTypeDef",
    ) -> "dc_td.GetLatestConfigurationResponse":
        return dc_td.GetLatestConfigurationResponse.make_one(res)

    def start_configuration_session(
        self,
        res: "bs_td.StartConfigurationSessionResponseTypeDef",
    ) -> "dc_td.StartConfigurationSessionResponse":
        return dc_td.StartConfigurationSessionResponse.make_one(res)


appconfigdata_caster = APPCONFIGDATACaster()
