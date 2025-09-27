# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_bedrock_data_automation_runtime import type_defs as bs_td


class BEDROCK_DATA_AUTOMATION_RUNTIMECaster:

    def get_data_automation_status(
        self,
        res: "bs_td.GetDataAutomationStatusResponseTypeDef",
    ) -> "dc_td.GetDataAutomationStatusResponse":
        return dc_td.GetDataAutomationStatusResponse.make_one(res)

    def invoke_data_automation_async(
        self,
        res: "bs_td.InvokeDataAutomationAsyncResponseTypeDef",
    ) -> "dc_td.InvokeDataAutomationAsyncResponse":
        return dc_td.InvokeDataAutomationAsyncResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)


bedrock_data_automation_runtime_caster = BEDROCK_DATA_AUTOMATION_RUNTIMECaster()
