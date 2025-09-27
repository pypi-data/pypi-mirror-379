# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_codeguru_security import type_defs as bs_td


class CODEGURU_SECURITYCaster:

    def batch_get_findings(
        self,
        res: "bs_td.BatchGetFindingsResponseTypeDef",
    ) -> "dc_td.BatchGetFindingsResponse":
        return dc_td.BatchGetFindingsResponse.make_one(res)

    def create_scan(
        self,
        res: "bs_td.CreateScanResponseTypeDef",
    ) -> "dc_td.CreateScanResponse":
        return dc_td.CreateScanResponse.make_one(res)

    def create_upload_url(
        self,
        res: "bs_td.CreateUploadUrlResponseTypeDef",
    ) -> "dc_td.CreateUploadUrlResponse":
        return dc_td.CreateUploadUrlResponse.make_one(res)

    def get_account_configuration(
        self,
        res: "bs_td.GetAccountConfigurationResponseTypeDef",
    ) -> "dc_td.GetAccountConfigurationResponse":
        return dc_td.GetAccountConfigurationResponse.make_one(res)

    def get_findings(
        self,
        res: "bs_td.GetFindingsResponseTypeDef",
    ) -> "dc_td.GetFindingsResponse":
        return dc_td.GetFindingsResponse.make_one(res)

    def get_metrics_summary(
        self,
        res: "bs_td.GetMetricsSummaryResponseTypeDef",
    ) -> "dc_td.GetMetricsSummaryResponse":
        return dc_td.GetMetricsSummaryResponse.make_one(res)

    def get_scan(
        self,
        res: "bs_td.GetScanResponseTypeDef",
    ) -> "dc_td.GetScanResponse":
        return dc_td.GetScanResponse.make_one(res)

    def list_findings_metrics(
        self,
        res: "bs_td.ListFindingsMetricsResponseTypeDef",
    ) -> "dc_td.ListFindingsMetricsResponse":
        return dc_td.ListFindingsMetricsResponse.make_one(res)

    def list_scans(
        self,
        res: "bs_td.ListScansResponseTypeDef",
    ) -> "dc_td.ListScansResponse":
        return dc_td.ListScansResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def update_account_configuration(
        self,
        res: "bs_td.UpdateAccountConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateAccountConfigurationResponse":
        return dc_td.UpdateAccountConfigurationResponse.make_one(res)


codeguru_security_caster = CODEGURU_SECURITYCaster()
