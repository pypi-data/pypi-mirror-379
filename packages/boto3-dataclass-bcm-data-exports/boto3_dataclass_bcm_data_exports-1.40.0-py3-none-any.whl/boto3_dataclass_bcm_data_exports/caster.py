# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_bcm_data_exports import type_defs as bs_td


class BCM_DATA_EXPORTSCaster:

    def create_export(
        self,
        res: "bs_td.CreateExportResponseTypeDef",
    ) -> "dc_td.CreateExportResponse":
        return dc_td.CreateExportResponse.make_one(res)

    def delete_export(
        self,
        res: "bs_td.DeleteExportResponseTypeDef",
    ) -> "dc_td.DeleteExportResponse":
        return dc_td.DeleteExportResponse.make_one(res)

    def get_execution(
        self,
        res: "bs_td.GetExecutionResponseTypeDef",
    ) -> "dc_td.GetExecutionResponse":
        return dc_td.GetExecutionResponse.make_one(res)

    def get_export(
        self,
        res: "bs_td.GetExportResponseTypeDef",
    ) -> "dc_td.GetExportResponse":
        return dc_td.GetExportResponse.make_one(res)

    def get_table(
        self,
        res: "bs_td.GetTableResponseTypeDef",
    ) -> "dc_td.GetTableResponse":
        return dc_td.GetTableResponse.make_one(res)

    def list_executions(
        self,
        res: "bs_td.ListExecutionsResponseTypeDef",
    ) -> "dc_td.ListExecutionsResponse":
        return dc_td.ListExecutionsResponse.make_one(res)

    def list_exports(
        self,
        res: "bs_td.ListExportsResponseTypeDef",
    ) -> "dc_td.ListExportsResponse":
        return dc_td.ListExportsResponse.make_one(res)

    def list_tables(
        self,
        res: "bs_td.ListTablesResponseTypeDef",
    ) -> "dc_td.ListTablesResponse":
        return dc_td.ListTablesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def update_export(
        self,
        res: "bs_td.UpdateExportResponseTypeDef",
    ) -> "dc_td.UpdateExportResponse":
        return dc_td.UpdateExportResponse.make_one(res)


bcm_data_exports_caster = BCM_DATA_EXPORTSCaster()
