# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_acm_pca import type_defs as bs_td


class ACM_PCACaster:

    def create_certificate_authority(
        self,
        res: "bs_td.CreateCertificateAuthorityResponseTypeDef",
    ) -> "dc_td.CreateCertificateAuthorityResponse":
        return dc_td.CreateCertificateAuthorityResponse.make_one(res)

    def create_certificate_authority_audit_report(
        self,
        res: "bs_td.CreateCertificateAuthorityAuditReportResponseTypeDef",
    ) -> "dc_td.CreateCertificateAuthorityAuditReportResponse":
        return dc_td.CreateCertificateAuthorityAuditReportResponse.make_one(res)

    def create_permission(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_certificate_authority(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_permission(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_certificate_authority(
        self,
        res: "bs_td.DescribeCertificateAuthorityResponseTypeDef",
    ) -> "dc_td.DescribeCertificateAuthorityResponse":
        return dc_td.DescribeCertificateAuthorityResponse.make_one(res)

    def describe_certificate_authority_audit_report(
        self,
        res: "bs_td.DescribeCertificateAuthorityAuditReportResponseTypeDef",
    ) -> "dc_td.DescribeCertificateAuthorityAuditReportResponse":
        return dc_td.DescribeCertificateAuthorityAuditReportResponse.make_one(res)

    def get_certificate(
        self,
        res: "bs_td.GetCertificateResponseTypeDef",
    ) -> "dc_td.GetCertificateResponse":
        return dc_td.GetCertificateResponse.make_one(res)

    def get_certificate_authority_certificate(
        self,
        res: "bs_td.GetCertificateAuthorityCertificateResponseTypeDef",
    ) -> "dc_td.GetCertificateAuthorityCertificateResponse":
        return dc_td.GetCertificateAuthorityCertificateResponse.make_one(res)

    def get_certificate_authority_csr(
        self,
        res: "bs_td.GetCertificateAuthorityCsrResponseTypeDef",
    ) -> "dc_td.GetCertificateAuthorityCsrResponse":
        return dc_td.GetCertificateAuthorityCsrResponse.make_one(res)

    def get_policy(
        self,
        res: "bs_td.GetPolicyResponseTypeDef",
    ) -> "dc_td.GetPolicyResponse":
        return dc_td.GetPolicyResponse.make_one(res)

    def import_certificate_authority_certificate(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def issue_certificate(
        self,
        res: "bs_td.IssueCertificateResponseTypeDef",
    ) -> "dc_td.IssueCertificateResponse":
        return dc_td.IssueCertificateResponse.make_one(res)

    def list_certificate_authorities(
        self,
        res: "bs_td.ListCertificateAuthoritiesResponseTypeDef",
    ) -> "dc_td.ListCertificateAuthoritiesResponse":
        return dc_td.ListCertificateAuthoritiesResponse.make_one(res)

    def list_permissions(
        self,
        res: "bs_td.ListPermissionsResponseTypeDef",
    ) -> "dc_td.ListPermissionsResponse":
        return dc_td.ListPermissionsResponse.make_one(res)

    def list_tags(
        self,
        res: "bs_td.ListTagsResponseTypeDef",
    ) -> "dc_td.ListTagsResponse":
        return dc_td.ListTagsResponse.make_one(res)

    def put_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def restore_certificate_authority(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def revoke_certificate(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def tag_certificate_authority(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_certificate_authority(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_certificate_authority(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


acm_pca_caster = ACM_PCACaster()
