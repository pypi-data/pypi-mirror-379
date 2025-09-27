# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_forecastquery import type_defs as bs_td


class FORECASTQUERYCaster:

    def query_forecast(
        self,
        res: "bs_td.QueryForecastResponseTypeDef",
    ) -> "dc_td.QueryForecastResponse":
        return dc_td.QueryForecastResponse.make_one(res)

    def query_what_if_forecast(
        self,
        res: "bs_td.QueryWhatIfForecastResponseTypeDef",
    ) -> "dc_td.QueryWhatIfForecastResponse":
        return dc_td.QueryWhatIfForecastResponse.make_one(res)


forecastquery_caster = FORECASTQUERYCaster()
