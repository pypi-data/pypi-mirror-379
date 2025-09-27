# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_artifact import type_defs as bs_td


class ARTIFACTCaster:

    def get_account_settings(
        self,
        res: "bs_td.GetAccountSettingsResponseTypeDef",
    ) -> "dc_td.GetAccountSettingsResponse":
        return dc_td.GetAccountSettingsResponse.make_one(res)

    def get_report(
        self,
        res: "bs_td.GetReportResponseTypeDef",
    ) -> "dc_td.GetReportResponse":
        return dc_td.GetReportResponse.make_one(res)

    def get_report_metadata(
        self,
        res: "bs_td.GetReportMetadataResponseTypeDef",
    ) -> "dc_td.GetReportMetadataResponse":
        return dc_td.GetReportMetadataResponse.make_one(res)

    def get_term_for_report(
        self,
        res: "bs_td.GetTermForReportResponseTypeDef",
    ) -> "dc_td.GetTermForReportResponse":
        return dc_td.GetTermForReportResponse.make_one(res)

    def list_customer_agreements(
        self,
        res: "bs_td.ListCustomerAgreementsResponseTypeDef",
    ) -> "dc_td.ListCustomerAgreementsResponse":
        return dc_td.ListCustomerAgreementsResponse.make_one(res)

    def list_reports(
        self,
        res: "bs_td.ListReportsResponseTypeDef",
    ) -> "dc_td.ListReportsResponse":
        return dc_td.ListReportsResponse.make_one(res)

    def put_account_settings(
        self,
        res: "bs_td.PutAccountSettingsResponseTypeDef",
    ) -> "dc_td.PutAccountSettingsResponse":
        return dc_td.PutAccountSettingsResponse.make_one(res)


artifact_caster = ARTIFACTCaster()
