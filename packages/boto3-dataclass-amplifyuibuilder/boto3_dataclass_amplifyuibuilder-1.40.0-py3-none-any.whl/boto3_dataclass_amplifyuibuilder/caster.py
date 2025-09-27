# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_amplifyuibuilder import type_defs as bs_td


class AMPLIFYUIBUILDERCaster:

    def create_component(
        self,
        res: "bs_td.CreateComponentResponseTypeDef",
    ) -> "dc_td.CreateComponentResponse":
        return dc_td.CreateComponentResponse.make_one(res)

    def create_form(
        self,
        res: "bs_td.CreateFormResponseTypeDef",
    ) -> "dc_td.CreateFormResponse":
        return dc_td.CreateFormResponse.make_one(res)

    def create_theme(
        self,
        res: "bs_td.CreateThemeResponseTypeDef",
    ) -> "dc_td.CreateThemeResponse":
        return dc_td.CreateThemeResponse.make_one(res)

    def delete_component(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_form(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_theme(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def exchange_code_for_token(
        self,
        res: "bs_td.ExchangeCodeForTokenResponseTypeDef",
    ) -> "dc_td.ExchangeCodeForTokenResponse":
        return dc_td.ExchangeCodeForTokenResponse.make_one(res)

    def export_components(
        self,
        res: "bs_td.ExportComponentsResponseTypeDef",
    ) -> "dc_td.ExportComponentsResponse":
        return dc_td.ExportComponentsResponse.make_one(res)

    def export_forms(
        self,
        res: "bs_td.ExportFormsResponseTypeDef",
    ) -> "dc_td.ExportFormsResponse":
        return dc_td.ExportFormsResponse.make_one(res)

    def export_themes(
        self,
        res: "bs_td.ExportThemesResponseTypeDef",
    ) -> "dc_td.ExportThemesResponse":
        return dc_td.ExportThemesResponse.make_one(res)

    def get_codegen_job(
        self,
        res: "bs_td.GetCodegenJobResponseTypeDef",
    ) -> "dc_td.GetCodegenJobResponse":
        return dc_td.GetCodegenJobResponse.make_one(res)

    def get_component(
        self,
        res: "bs_td.GetComponentResponseTypeDef",
    ) -> "dc_td.GetComponentResponse":
        return dc_td.GetComponentResponse.make_one(res)

    def get_form(
        self,
        res: "bs_td.GetFormResponseTypeDef",
    ) -> "dc_td.GetFormResponse":
        return dc_td.GetFormResponse.make_one(res)

    def get_metadata(
        self,
        res: "bs_td.GetMetadataResponseTypeDef",
    ) -> "dc_td.GetMetadataResponse":
        return dc_td.GetMetadataResponse.make_one(res)

    def get_theme(
        self,
        res: "bs_td.GetThemeResponseTypeDef",
    ) -> "dc_td.GetThemeResponse":
        return dc_td.GetThemeResponse.make_one(res)

    def list_codegen_jobs(
        self,
        res: "bs_td.ListCodegenJobsResponseTypeDef",
    ) -> "dc_td.ListCodegenJobsResponse":
        return dc_td.ListCodegenJobsResponse.make_one(res)

    def list_components(
        self,
        res: "bs_td.ListComponentsResponseTypeDef",
    ) -> "dc_td.ListComponentsResponse":
        return dc_td.ListComponentsResponse.make_one(res)

    def list_forms(
        self,
        res: "bs_td.ListFormsResponseTypeDef",
    ) -> "dc_td.ListFormsResponse":
        return dc_td.ListFormsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_themes(
        self,
        res: "bs_td.ListThemesResponseTypeDef",
    ) -> "dc_td.ListThemesResponse":
        return dc_td.ListThemesResponse.make_one(res)

    def put_metadata_flag(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def refresh_token(
        self,
        res: "bs_td.RefreshTokenResponseTypeDef",
    ) -> "dc_td.RefreshTokenResponse":
        return dc_td.RefreshTokenResponse.make_one(res)

    def start_codegen_job(
        self,
        res: "bs_td.StartCodegenJobResponseTypeDef",
    ) -> "dc_td.StartCodegenJobResponse":
        return dc_td.StartCodegenJobResponse.make_one(res)

    def update_component(
        self,
        res: "bs_td.UpdateComponentResponseTypeDef",
    ) -> "dc_td.UpdateComponentResponse":
        return dc_td.UpdateComponentResponse.make_one(res)

    def update_form(
        self,
        res: "bs_td.UpdateFormResponseTypeDef",
    ) -> "dc_td.UpdateFormResponse":
        return dc_td.UpdateFormResponse.make_one(res)

    def update_theme(
        self,
        res: "bs_td.UpdateThemeResponseTypeDef",
    ) -> "dc_td.UpdateThemeResponse":
        return dc_td.UpdateThemeResponse.make_one(res)


amplifyuibuilder_caster = AMPLIFYUIBUILDERCaster()
