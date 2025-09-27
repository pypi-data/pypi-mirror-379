# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_applicationcostprofiler import type_defs as bs_td


class APPLICATIONCOSTPROFILERCaster:

    def delete_report_definition(
        self,
        res: "bs_td.DeleteReportDefinitionResultTypeDef",
    ) -> "dc_td.DeleteReportDefinitionResult":
        return dc_td.DeleteReportDefinitionResult.make_one(res)

    def get_report_definition(
        self,
        res: "bs_td.GetReportDefinitionResultTypeDef",
    ) -> "dc_td.GetReportDefinitionResult":
        return dc_td.GetReportDefinitionResult.make_one(res)

    def import_application_usage(
        self,
        res: "bs_td.ImportApplicationUsageResultTypeDef",
    ) -> "dc_td.ImportApplicationUsageResult":
        return dc_td.ImportApplicationUsageResult.make_one(res)

    def list_report_definitions(
        self,
        res: "bs_td.ListReportDefinitionsResultTypeDef",
    ) -> "dc_td.ListReportDefinitionsResult":
        return dc_td.ListReportDefinitionsResult.make_one(res)

    def put_report_definition(
        self,
        res: "bs_td.PutReportDefinitionResultTypeDef",
    ) -> "dc_td.PutReportDefinitionResult":
        return dc_td.PutReportDefinitionResult.make_one(res)

    def update_report_definition(
        self,
        res: "bs_td.UpdateReportDefinitionResultTypeDef",
    ) -> "dc_td.UpdateReportDefinitionResult":
        return dc_td.UpdateReportDefinitionResult.make_one(res)


applicationcostprofiler_caster = APPLICATIONCOSTPROFILERCaster()
