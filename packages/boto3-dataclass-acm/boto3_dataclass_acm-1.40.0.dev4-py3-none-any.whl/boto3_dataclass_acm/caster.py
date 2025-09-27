# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_acm import type_defs as bs_td


class ACMCaster:

    def add_tags_to_certificate(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_certificate(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_certificate(
        self,
        res: "bs_td.DescribeCertificateResponseTypeDef",
    ) -> "dc_td.DescribeCertificateResponse":
        return dc_td.DescribeCertificateResponse.make_one(res)

    def export_certificate(
        self,
        res: "bs_td.ExportCertificateResponseTypeDef",
    ) -> "dc_td.ExportCertificateResponse":
        return dc_td.ExportCertificateResponse.make_one(res)

    def get_account_configuration(
        self,
        res: "bs_td.GetAccountConfigurationResponseTypeDef",
    ) -> "dc_td.GetAccountConfigurationResponse":
        return dc_td.GetAccountConfigurationResponse.make_one(res)

    def get_certificate(
        self,
        res: "bs_td.GetCertificateResponseTypeDef",
    ) -> "dc_td.GetCertificateResponse":
        return dc_td.GetCertificateResponse.make_one(res)

    def import_certificate(
        self,
        res: "bs_td.ImportCertificateResponseTypeDef",
    ) -> "dc_td.ImportCertificateResponse":
        return dc_td.ImportCertificateResponse.make_one(res)

    def list_certificates(
        self,
        res: "bs_td.ListCertificatesResponseTypeDef",
    ) -> "dc_td.ListCertificatesResponse":
        return dc_td.ListCertificatesResponse.make_one(res)

    def list_tags_for_certificate(
        self,
        res: "bs_td.ListTagsForCertificateResponseTypeDef",
    ) -> "dc_td.ListTagsForCertificateResponse":
        return dc_td.ListTagsForCertificateResponse.make_one(res)

    def put_account_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def remove_tags_from_certificate(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def renew_certificate(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def request_certificate(
        self,
        res: "bs_td.RequestCertificateResponseTypeDef",
    ) -> "dc_td.RequestCertificateResponse":
        return dc_td.RequestCertificateResponse.make_one(res)

    def resend_validation_email(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def revoke_certificate(
        self,
        res: "bs_td.RevokeCertificateResponseTypeDef",
    ) -> "dc_td.RevokeCertificateResponse":
        return dc_td.RevokeCertificateResponse.make_one(res)

    def update_certificate_options(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


acm_caster = ACMCaster()
