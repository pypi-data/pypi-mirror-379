# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cur import type_defs as bs_td


class CURCaster:

    def delete_report_definition(
        self,
        res: "bs_td.DeleteReportDefinitionResponseTypeDef",
    ) -> "dc_td.DeleteReportDefinitionResponse":
        return dc_td.DeleteReportDefinitionResponse.make_one(res)

    def describe_report_definitions(
        self,
        res: "bs_td.DescribeReportDefinitionsResponseTypeDef",
    ) -> "dc_td.DescribeReportDefinitionsResponse":
        return dc_td.DescribeReportDefinitionsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)


cur_caster = CURCaster()
