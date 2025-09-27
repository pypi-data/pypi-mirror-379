# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cloudtrail_data import type_defs as bs_td


class CLOUDTRAIL_DATACaster:

    def put_audit_events(
        self,
        res: "bs_td.PutAuditEventsResponseTypeDef",
    ) -> "dc_td.PutAuditEventsResponse":
        return dc_td.PutAuditEventsResponse.make_one(res)


cloudtrail_data_caster = CLOUDTRAIL_DATACaster()
