# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_connect_contact_lens import type_defs as bs_td


class CONNECT_CONTACT_LENSCaster:

    def list_realtime_contact_analysis_segments(
        self,
        res: "bs_td.ListRealtimeContactAnalysisSegmentsResponseTypeDef",
    ) -> "dc_td.ListRealtimeContactAnalysisSegmentsResponse":
        return dc_td.ListRealtimeContactAnalysisSegmentsResponse.make_one(res)


connect_contact_lens_caster = CONNECT_CONTACT_LENSCaster()
