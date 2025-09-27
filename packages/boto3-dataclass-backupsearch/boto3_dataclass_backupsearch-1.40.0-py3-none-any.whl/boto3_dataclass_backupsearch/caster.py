# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_backupsearch import type_defs as bs_td


class BACKUPSEARCHCaster:

    def get_search_job(
        self,
        res: "bs_td.GetSearchJobOutputTypeDef",
    ) -> "dc_td.GetSearchJobOutput":
        return dc_td.GetSearchJobOutput.make_one(res)

    def get_search_result_export_job(
        self,
        res: "bs_td.GetSearchResultExportJobOutputTypeDef",
    ) -> "dc_td.GetSearchResultExportJobOutput":
        return dc_td.GetSearchResultExportJobOutput.make_one(res)

    def list_search_job_backups(
        self,
        res: "bs_td.ListSearchJobBackupsOutputTypeDef",
    ) -> "dc_td.ListSearchJobBackupsOutput":
        return dc_td.ListSearchJobBackupsOutput.make_one(res)

    def list_search_job_results(
        self,
        res: "bs_td.ListSearchJobResultsOutputTypeDef",
    ) -> "dc_td.ListSearchJobResultsOutput":
        return dc_td.ListSearchJobResultsOutput.make_one(res)

    def list_search_jobs(
        self,
        res: "bs_td.ListSearchJobsOutputTypeDef",
    ) -> "dc_td.ListSearchJobsOutput":
        return dc_td.ListSearchJobsOutput.make_one(res)

    def list_search_result_export_jobs(
        self,
        res: "bs_td.ListSearchResultExportJobsOutputTypeDef",
    ) -> "dc_td.ListSearchResultExportJobsOutput":
        return dc_td.ListSearchResultExportJobsOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def start_search_job(
        self,
        res: "bs_td.StartSearchJobOutputTypeDef",
    ) -> "dc_td.StartSearchJobOutput":
        return dc_td.StartSearchJobOutput.make_one(res)

    def start_search_result_export_job(
        self,
        res: "bs_td.StartSearchResultExportJobOutputTypeDef",
    ) -> "dc_td.StartSearchResultExportJobOutput":
        return dc_td.StartSearchResultExportJobOutput.make_one(res)


backupsearch_caster = BACKUPSEARCHCaster()
