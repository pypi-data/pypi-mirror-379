# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_acm_pca import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class CustomAttribute:
    boto3_raw_data: "type_defs.CustomAttributeTypeDef" = dataclasses.field()

    ObjectIdentifier = field("ObjectIdentifier")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomAttributeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessMethod:
    boto3_raw_data: "type_defs.AccessMethodTypeDef" = dataclasses.field()

    CustomObjectIdentifier = field("CustomObjectIdentifier")
    AccessMethodType = field("AccessMethodType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessMethodTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccessMethodTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCertificateAuthorityAuditReportRequest:
    boto3_raw_data: "type_defs.CreateCertificateAuthorityAuditReportRequestTypeDef" = (
        dataclasses.field()
    )

    CertificateAuthorityArn = field("CertificateAuthorityArn")
    S3BucketName = field("S3BucketName")
    AuditReportResponseFormat = field("AuditReportResponseFormat")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCertificateAuthorityAuditReportRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCertificateAuthorityAuditReportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseMetadata:
    boto3_raw_data: "type_defs.ResponseMetadataTypeDef" = dataclasses.field()

    RequestId = field("RequestId")
    HTTPStatusCode = field("HTTPStatusCode")
    HTTPHeaders = field("HTTPHeaders")
    RetryAttempts = field("RetryAttempts")
    HostId = field("HostId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePermissionRequest:
    boto3_raw_data: "type_defs.CreatePermissionRequestTypeDef" = dataclasses.field()

    CertificateAuthorityArn = field("CertificateAuthorityArn")
    Principal = field("Principal")
    Actions = field("Actions")
    SourceAccount = field("SourceAccount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePermissionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePermissionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CrlDistributionPointExtensionConfiguration:
    boto3_raw_data: "type_defs.CrlDistributionPointExtensionConfigurationTypeDef" = (
        dataclasses.field()
    )

    OmitExtension = field("OmitExtension")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CrlDistributionPointExtensionConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CrlDistributionPointExtensionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyUsage:
    boto3_raw_data: "type_defs.KeyUsageTypeDef" = dataclasses.field()

    DigitalSignature = field("DigitalSignature")
    NonRepudiation = field("NonRepudiation")
    KeyEncipherment = field("KeyEncipherment")
    DataEncipherment = field("DataEncipherment")
    KeyAgreement = field("KeyAgreement")
    KeyCertSign = field("KeyCertSign")
    CRLSign = field("CRLSign")
    EncipherOnly = field("EncipherOnly")
    DecipherOnly = field("DecipherOnly")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyUsageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyUsageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomExtension:
    boto3_raw_data: "type_defs.CustomExtensionTypeDef" = dataclasses.field()

    ObjectIdentifier = field("ObjectIdentifier")
    Value = field("Value")
    Critical = field("Critical")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomExtensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomExtensionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCertificateAuthorityRequest:
    boto3_raw_data: "type_defs.DeleteCertificateAuthorityRequestTypeDef" = (
        dataclasses.field()
    )

    CertificateAuthorityArn = field("CertificateAuthorityArn")
    PermanentDeletionTimeInDays = field("PermanentDeletionTimeInDays")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCertificateAuthorityRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCertificateAuthorityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePermissionRequest:
    boto3_raw_data: "type_defs.DeletePermissionRequestTypeDef" = dataclasses.field()

    CertificateAuthorityArn = field("CertificateAuthorityArn")
    Principal = field("Principal")
    SourceAccount = field("SourceAccount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePermissionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePermissionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePolicyRequest:
    boto3_raw_data: "type_defs.DeletePolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCertificateAuthorityAuditReportRequest:
    boto3_raw_data: (
        "type_defs.DescribeCertificateAuthorityAuditReportRequestTypeDef"
    ) = dataclasses.field()

    CertificateAuthorityArn = field("CertificateAuthorityArn")
    AuditReportId = field("AuditReportId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCertificateAuthorityAuditReportRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeCertificateAuthorityAuditReportRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaiterConfig:
    boto3_raw_data: "type_defs.WaiterConfigTypeDef" = dataclasses.field()

    Delay = field("Delay")
    MaxAttempts = field("MaxAttempts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaiterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaiterConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCertificateAuthorityRequest:
    boto3_raw_data: "type_defs.DescribeCertificateAuthorityRequestTypeDef" = (
        dataclasses.field()
    )

    CertificateAuthorityArn = field("CertificateAuthorityArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCertificateAuthorityRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCertificateAuthorityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EdiPartyName:
    boto3_raw_data: "type_defs.EdiPartyNameTypeDef" = dataclasses.field()

    PartyName = field("PartyName")
    NameAssigner = field("NameAssigner")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EdiPartyNameTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EdiPartyNameTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtendedKeyUsage:
    boto3_raw_data: "type_defs.ExtendedKeyUsageTypeDef" = dataclasses.field()

    ExtendedKeyUsageType = field("ExtendedKeyUsageType")
    ExtendedKeyUsageObjectIdentifier = field("ExtendedKeyUsageObjectIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExtendedKeyUsageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExtendedKeyUsageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OtherName:
    boto3_raw_data: "type_defs.OtherNameTypeDef" = dataclasses.field()

    TypeId = field("TypeId")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OtherNameTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OtherNameTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCertificateAuthorityCertificateRequest:
    boto3_raw_data: "type_defs.GetCertificateAuthorityCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    CertificateAuthorityArn = field("CertificateAuthorityArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCertificateAuthorityCertificateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCertificateAuthorityCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCertificateAuthorityCsrRequest:
    boto3_raw_data: "type_defs.GetCertificateAuthorityCsrRequestTypeDef" = (
        dataclasses.field()
    )

    CertificateAuthorityArn = field("CertificateAuthorityArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCertificateAuthorityCsrRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCertificateAuthorityCsrRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCertificateRequest:
    boto3_raw_data: "type_defs.GetCertificateRequestTypeDef" = dataclasses.field()

    CertificateAuthorityArn = field("CertificateAuthorityArn")
    CertificateArn = field("CertificateArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyRequest:
    boto3_raw_data: "type_defs.GetPolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPolicyRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Validity:
    boto3_raw_data: "type_defs.ValidityTypeDef" = dataclasses.field()

    Value = field("Value")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValidityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ValidityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PaginatorConfig:
    boto3_raw_data: "type_defs.PaginatorConfigTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    PageSize = field("PageSize")
    StartingToken = field("StartingToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PaginatorConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PaginatorConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCertificateAuthoritiesRequest:
    boto3_raw_data: "type_defs.ListCertificateAuthoritiesRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    ResourceOwner = field("ResourceOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCertificateAuthoritiesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCertificateAuthoritiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPermissionsRequest:
    boto3_raw_data: "type_defs.ListPermissionsRequestTypeDef" = dataclasses.field()

    CertificateAuthorityArn = field("CertificateAuthorityArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPermissionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPermissionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Permission:
    boto3_raw_data: "type_defs.PermissionTypeDef" = dataclasses.field()

    CertificateAuthorityArn = field("CertificateAuthorityArn")
    CreatedAt = field("CreatedAt")
    Principal = field("Principal")
    SourceAccount = field("SourceAccount")
    Actions = field("Actions")
    Policy = field("Policy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PermissionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PermissionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsRequest:
    boto3_raw_data: "type_defs.ListTagsRequestTypeDef" = dataclasses.field()

    CertificateAuthorityArn = field("CertificateAuthorityArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTagsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListTagsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OcspConfiguration:
    boto3_raw_data: "type_defs.OcspConfigurationTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    OcspCustomCname = field("OcspCustomCname")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OcspConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OcspConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Qualifier:
    boto3_raw_data: "type_defs.QualifierTypeDef" = dataclasses.field()

    CpsUri = field("CpsUri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QualifierTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QualifierTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPolicyRequest:
    boto3_raw_data: "type_defs.PutPolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Policy = field("Policy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutPolicyRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreCertificateAuthorityRequest:
    boto3_raw_data: "type_defs.RestoreCertificateAuthorityRequestTypeDef" = (
        dataclasses.field()
    )

    CertificateAuthorityArn = field("CertificateAuthorityArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreCertificateAuthorityRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreCertificateAuthorityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeCertificateRequest:
    boto3_raw_data: "type_defs.RevokeCertificateRequestTypeDef" = dataclasses.field()

    CertificateAuthorityArn = field("CertificateAuthorityArn")
    CertificateSerial = field("CertificateSerial")
    RevocationReason = field("RevocationReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RevokeCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ASN1SubjectOutput:
    boto3_raw_data: "type_defs.ASN1SubjectOutputTypeDef" = dataclasses.field()

    Country = field("Country")
    Organization = field("Organization")
    OrganizationalUnit = field("OrganizationalUnit")
    DistinguishedNameQualifier = field("DistinguishedNameQualifier")
    State = field("State")
    CommonName = field("CommonName")
    SerialNumber = field("SerialNumber")
    Locality = field("Locality")
    Title = field("Title")
    Surname = field("Surname")
    GivenName = field("GivenName")
    Initials = field("Initials")
    Pseudonym = field("Pseudonym")
    GenerationQualifier = field("GenerationQualifier")

    @cached_property
    def CustomAttributes(self):  # pragma: no cover
        return CustomAttribute.make_many(self.boto3_raw_data["CustomAttributes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ASN1SubjectOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ASN1SubjectOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ASN1Subject:
    boto3_raw_data: "type_defs.ASN1SubjectTypeDef" = dataclasses.field()

    Country = field("Country")
    Organization = field("Organization")
    OrganizationalUnit = field("OrganizationalUnit")
    DistinguishedNameQualifier = field("DistinguishedNameQualifier")
    State = field("State")
    CommonName = field("CommonName")
    SerialNumber = field("SerialNumber")
    Locality = field("Locality")
    Title = field("Title")
    Surname = field("Surname")
    GivenName = field("GivenName")
    Initials = field("Initials")
    Pseudonym = field("Pseudonym")
    GenerationQualifier = field("GenerationQualifier")

    @cached_property
    def CustomAttributes(self):  # pragma: no cover
        return CustomAttribute.make_many(self.boto3_raw_data["CustomAttributes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ASN1SubjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ASN1SubjectTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportCertificateAuthorityCertificateRequest:
    boto3_raw_data: "type_defs.ImportCertificateAuthorityCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    CertificateAuthorityArn = field("CertificateAuthorityArn")
    Certificate = field("Certificate")
    CertificateChain = field("CertificateChain")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ImportCertificateAuthorityCertificateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportCertificateAuthorityCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCertificateAuthorityAuditReportResponse:
    boto3_raw_data: "type_defs.CreateCertificateAuthorityAuditReportResponseTypeDef" = (
        dataclasses.field()
    )

    AuditReportId = field("AuditReportId")
    S3Key = field("S3Key")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCertificateAuthorityAuditReportResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCertificateAuthorityAuditReportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCertificateAuthorityResponse:
    boto3_raw_data: "type_defs.CreateCertificateAuthorityResponseTypeDef" = (
        dataclasses.field()
    )

    CertificateAuthorityArn = field("CertificateAuthorityArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCertificateAuthorityResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCertificateAuthorityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCertificateAuthorityAuditReportResponse:
    boto3_raw_data: (
        "type_defs.DescribeCertificateAuthorityAuditReportResponseTypeDef"
    ) = dataclasses.field()

    AuditReportStatus = field("AuditReportStatus")
    S3BucketName = field("S3BucketName")
    S3Key = field("S3Key")
    CreatedAt = field("CreatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCertificateAuthorityAuditReportResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeCertificateAuthorityAuditReportResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCertificateAuthorityCertificateResponse:
    boto3_raw_data: "type_defs.GetCertificateAuthorityCertificateResponseTypeDef" = (
        dataclasses.field()
    )

    Certificate = field("Certificate")
    CertificateChain = field("CertificateChain")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCertificateAuthorityCertificateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCertificateAuthorityCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCertificateAuthorityCsrResponse:
    boto3_raw_data: "type_defs.GetCertificateAuthorityCsrResponseTypeDef" = (
        dataclasses.field()
    )

    Csr = field("Csr")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCertificateAuthorityCsrResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCertificateAuthorityCsrResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCertificateResponse:
    boto3_raw_data: "type_defs.GetCertificateResponseTypeDef" = dataclasses.field()

    Certificate = field("Certificate")
    CertificateChain = field("CertificateChain")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCertificateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyResponse:
    boto3_raw_data: "type_defs.GetPolicyResponseTypeDef" = dataclasses.field()

    Policy = field("Policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPolicyResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IssueCertificateResponse:
    boto3_raw_data: "type_defs.IssueCertificateResponseTypeDef" = dataclasses.field()

    CertificateArn = field("CertificateArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IssueCertificateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IssueCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsResponse:
    boto3_raw_data: "type_defs.ListTagsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTagsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagCertificateAuthorityRequest:
    boto3_raw_data: "type_defs.TagCertificateAuthorityRequestTypeDef" = (
        dataclasses.field()
    )

    CertificateAuthorityArn = field("CertificateAuthorityArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TagCertificateAuthorityRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagCertificateAuthorityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagCertificateAuthorityRequest:
    boto3_raw_data: "type_defs.UntagCertificateAuthorityRequestTypeDef" = (
        dataclasses.field()
    )

    CertificateAuthorityArn = field("CertificateAuthorityArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UntagCertificateAuthorityRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagCertificateAuthorityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CrlConfiguration:
    boto3_raw_data: "type_defs.CrlConfigurationTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    ExpirationInDays = field("ExpirationInDays")
    CustomCname = field("CustomCname")
    S3BucketName = field("S3BucketName")
    S3ObjectAcl = field("S3ObjectAcl")

    @cached_property
    def CrlDistributionPointExtensionConfiguration(self):  # pragma: no cover
        return CrlDistributionPointExtensionConfiguration.make_one(
            self.boto3_raw_data["CrlDistributionPointExtensionConfiguration"]
        )

    CrlType = field("CrlType")
    CustomPath = field("CustomPath")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CrlConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CrlConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCertificateAuthorityAuditReportRequestWait:
    boto3_raw_data: (
        "type_defs.DescribeCertificateAuthorityAuditReportRequestWaitTypeDef"
    ) = dataclasses.field()

    CertificateAuthorityArn = field("CertificateAuthorityArn")
    AuditReportId = field("AuditReportId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCertificateAuthorityAuditReportRequestWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeCertificateAuthorityAuditReportRequestWaitTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCertificateAuthorityCsrRequestWait:
    boto3_raw_data: "type_defs.GetCertificateAuthorityCsrRequestWaitTypeDef" = (
        dataclasses.field()
    )

    CertificateAuthorityArn = field("CertificateAuthorityArn")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCertificateAuthorityCsrRequestWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCertificateAuthorityCsrRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCertificateRequestWait:
    boto3_raw_data: "type_defs.GetCertificateRequestWaitTypeDef" = dataclasses.field()

    CertificateAuthorityArn = field("CertificateAuthorityArn")
    CertificateArn = field("CertificateArn")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCertificateRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCertificateRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCertificateAuthoritiesRequestPaginate:
    boto3_raw_data: "type_defs.ListCertificateAuthoritiesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceOwner = field("ResourceOwner")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCertificateAuthoritiesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCertificateAuthoritiesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPermissionsRequestPaginate:
    boto3_raw_data: "type_defs.ListPermissionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    CertificateAuthorityArn = field("CertificateAuthorityArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPermissionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPermissionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsRequestPaginate:
    boto3_raw_data: "type_defs.ListTagsRequestPaginateTypeDef" = dataclasses.field()

    CertificateAuthorityArn = field("CertificateAuthorityArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPermissionsResponse:
    boto3_raw_data: "type_defs.ListPermissionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Permissions(self):  # pragma: no cover
        return Permission.make_many(self.boto3_raw_data["Permissions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPermissionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPermissionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyQualifierInfo:
    boto3_raw_data: "type_defs.PolicyQualifierInfoTypeDef" = dataclasses.field()

    PolicyQualifierId = field("PolicyQualifierId")

    @cached_property
    def Qualifier(self):  # pragma: no cover
        return Qualifier.make_one(self.boto3_raw_data["Qualifier"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyQualifierInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyQualifierInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeneralNameOutput:
    boto3_raw_data: "type_defs.GeneralNameOutputTypeDef" = dataclasses.field()

    @cached_property
    def OtherName(self):  # pragma: no cover
        return OtherName.make_one(self.boto3_raw_data["OtherName"])

    Rfc822Name = field("Rfc822Name")
    DnsName = field("DnsName")

    @cached_property
    def DirectoryName(self):  # pragma: no cover
        return ASN1SubjectOutput.make_one(self.boto3_raw_data["DirectoryName"])

    @cached_property
    def EdiPartyName(self):  # pragma: no cover
        return EdiPartyName.make_one(self.boto3_raw_data["EdiPartyName"])

    UniformResourceIdentifier = field("UniformResourceIdentifier")
    IpAddress = field("IpAddress")
    RegisteredId = field("RegisteredId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GeneralNameOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeneralNameOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevocationConfiguration:
    boto3_raw_data: "type_defs.RevocationConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def CrlConfiguration(self):  # pragma: no cover
        return CrlConfiguration.make_one(self.boto3_raw_data["CrlConfiguration"])

    @cached_property
    def OcspConfiguration(self):  # pragma: no cover
        return OcspConfiguration.make_one(self.boto3_raw_data["OcspConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RevocationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevocationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyInformation:
    boto3_raw_data: "type_defs.PolicyInformationTypeDef" = dataclasses.field()

    CertPolicyId = field("CertPolicyId")

    @cached_property
    def PolicyQualifiers(self):  # pragma: no cover
        return PolicyQualifierInfo.make_many(self.boto3_raw_data["PolicyQualifiers"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyInformationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessDescriptionOutput:
    boto3_raw_data: "type_defs.AccessDescriptionOutputTypeDef" = dataclasses.field()

    @cached_property
    def AccessMethod(self):  # pragma: no cover
        return AccessMethod.make_one(self.boto3_raw_data["AccessMethod"])

    @cached_property
    def AccessLocation(self):  # pragma: no cover
        return GeneralNameOutput.make_one(self.boto3_raw_data["AccessLocation"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessDescriptionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessDescriptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeneralName:
    boto3_raw_data: "type_defs.GeneralNameTypeDef" = dataclasses.field()

    @cached_property
    def OtherName(self):  # pragma: no cover
        return OtherName.make_one(self.boto3_raw_data["OtherName"])

    Rfc822Name = field("Rfc822Name")
    DnsName = field("DnsName")
    DirectoryName = field("DirectoryName")

    @cached_property
    def EdiPartyName(self):  # pragma: no cover
        return EdiPartyName.make_one(self.boto3_raw_data["EdiPartyName"])

    UniformResourceIdentifier = field("UniformResourceIdentifier")
    IpAddress = field("IpAddress")
    RegisteredId = field("RegisteredId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GeneralNameTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GeneralNameTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCertificateAuthorityRequest:
    boto3_raw_data: "type_defs.UpdateCertificateAuthorityRequestTypeDef" = (
        dataclasses.field()
    )

    CertificateAuthorityArn = field("CertificateAuthorityArn")

    @cached_property
    def RevocationConfiguration(self):  # pragma: no cover
        return RevocationConfiguration.make_one(
            self.boto3_raw_data["RevocationConfiguration"]
        )

    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCertificateAuthorityRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCertificateAuthorityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CsrExtensionsOutput:
    boto3_raw_data: "type_defs.CsrExtensionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def KeyUsage(self):  # pragma: no cover
        return KeyUsage.make_one(self.boto3_raw_data["KeyUsage"])

    @cached_property
    def SubjectInformationAccess(self):  # pragma: no cover
        return AccessDescriptionOutput.make_many(
            self.boto3_raw_data["SubjectInformationAccess"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CsrExtensionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CsrExtensionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessDescription:
    boto3_raw_data: "type_defs.AccessDescriptionTypeDef" = dataclasses.field()

    @cached_property
    def AccessMethod(self):  # pragma: no cover
        return AccessMethod.make_one(self.boto3_raw_data["AccessMethod"])

    @cached_property
    def AccessLocation(self):  # pragma: no cover
        return GeneralName.make_one(self.boto3_raw_data["AccessLocation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CertificateAuthorityConfigurationOutput:
    boto3_raw_data: "type_defs.CertificateAuthorityConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    KeyAlgorithm = field("KeyAlgorithm")
    SigningAlgorithm = field("SigningAlgorithm")

    @cached_property
    def Subject(self):  # pragma: no cover
        return ASN1SubjectOutput.make_one(self.boto3_raw_data["Subject"])

    @cached_property
    def CsrExtensions(self):  # pragma: no cover
        return CsrExtensionsOutput.make_one(self.boto3_raw_data["CsrExtensions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CertificateAuthorityConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CertificateAuthorityConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CsrExtensions:
    boto3_raw_data: "type_defs.CsrExtensionsTypeDef" = dataclasses.field()

    @cached_property
    def KeyUsage(self):  # pragma: no cover
        return KeyUsage.make_one(self.boto3_raw_data["KeyUsage"])

    @cached_property
    def SubjectInformationAccess(self):  # pragma: no cover
        return AccessDescription.make_many(
            self.boto3_raw_data["SubjectInformationAccess"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CsrExtensionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CsrExtensionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Extensions:
    boto3_raw_data: "type_defs.ExtensionsTypeDef" = dataclasses.field()

    @cached_property
    def CertificatePolicies(self):  # pragma: no cover
        return PolicyInformation.make_many(self.boto3_raw_data["CertificatePolicies"])

    @cached_property
    def ExtendedKeyUsage(self):  # pragma: no cover
        return ExtendedKeyUsage.make_many(self.boto3_raw_data["ExtendedKeyUsage"])

    @cached_property
    def KeyUsage(self):  # pragma: no cover
        return KeyUsage.make_one(self.boto3_raw_data["KeyUsage"])

    SubjectAlternativeNames = field("SubjectAlternativeNames")

    @cached_property
    def CustomExtensions(self):  # pragma: no cover
        return CustomExtension.make_many(self.boto3_raw_data["CustomExtensions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExtensionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExtensionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CertificateAuthority:
    boto3_raw_data: "type_defs.CertificateAuthorityTypeDef" = dataclasses.field()

    Arn = field("Arn")
    OwnerAccount = field("OwnerAccount")
    CreatedAt = field("CreatedAt")
    LastStateChangeAt = field("LastStateChangeAt")
    Type = field("Type")
    Serial = field("Serial")
    Status = field("Status")
    NotBefore = field("NotBefore")
    NotAfter = field("NotAfter")
    FailureReason = field("FailureReason")

    @cached_property
    def CertificateAuthorityConfiguration(self):  # pragma: no cover
        return CertificateAuthorityConfigurationOutput.make_one(
            self.boto3_raw_data["CertificateAuthorityConfiguration"]
        )

    @cached_property
    def RevocationConfiguration(self):  # pragma: no cover
        return RevocationConfiguration.make_one(
            self.boto3_raw_data["RevocationConfiguration"]
        )

    RestorableUntil = field("RestorableUntil")
    KeyStorageSecurityStandard = field("KeyStorageSecurityStandard")
    UsageMode = field("UsageMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CertificateAuthorityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CertificateAuthorityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CertificateAuthorityConfiguration:
    boto3_raw_data: "type_defs.CertificateAuthorityConfigurationTypeDef" = (
        dataclasses.field()
    )

    KeyAlgorithm = field("KeyAlgorithm")
    SigningAlgorithm = field("SigningAlgorithm")

    @cached_property
    def Subject(self):  # pragma: no cover
        return ASN1Subject.make_one(self.boto3_raw_data["Subject"])

    @cached_property
    def CsrExtensions(self):  # pragma: no cover
        return CsrExtensions.make_one(self.boto3_raw_data["CsrExtensions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CertificateAuthorityConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CertificateAuthorityConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiPassthrough:
    boto3_raw_data: "type_defs.ApiPassthroughTypeDef" = dataclasses.field()

    @cached_property
    def Extensions(self):  # pragma: no cover
        return Extensions.make_one(self.boto3_raw_data["Extensions"])

    Subject = field("Subject")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApiPassthroughTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApiPassthroughTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCertificateAuthorityResponse:
    boto3_raw_data: "type_defs.DescribeCertificateAuthorityResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CertificateAuthority(self):  # pragma: no cover
        return CertificateAuthority.make_one(
            self.boto3_raw_data["CertificateAuthority"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCertificateAuthorityResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCertificateAuthorityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCertificateAuthoritiesResponse:
    boto3_raw_data: "type_defs.ListCertificateAuthoritiesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CertificateAuthorities(self):  # pragma: no cover
        return CertificateAuthority.make_many(
            self.boto3_raw_data["CertificateAuthorities"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCertificateAuthoritiesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCertificateAuthoritiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IssueCertificateRequest:
    boto3_raw_data: "type_defs.IssueCertificateRequestTypeDef" = dataclasses.field()

    CertificateAuthorityArn = field("CertificateAuthorityArn")
    Csr = field("Csr")
    SigningAlgorithm = field("SigningAlgorithm")

    @cached_property
    def Validity(self):  # pragma: no cover
        return Validity.make_one(self.boto3_raw_data["Validity"])

    @cached_property
    def ApiPassthrough(self):  # pragma: no cover
        return ApiPassthrough.make_one(self.boto3_raw_data["ApiPassthrough"])

    TemplateArn = field("TemplateArn")

    @cached_property
    def ValidityNotBefore(self):  # pragma: no cover
        return Validity.make_one(self.boto3_raw_data["ValidityNotBefore"])

    IdempotencyToken = field("IdempotencyToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IssueCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IssueCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCertificateAuthorityRequest:
    boto3_raw_data: "type_defs.CreateCertificateAuthorityRequestTypeDef" = (
        dataclasses.field()
    )

    CertificateAuthorityConfiguration = field("CertificateAuthorityConfiguration")
    CertificateAuthorityType = field("CertificateAuthorityType")

    @cached_property
    def RevocationConfiguration(self):  # pragma: no cover
        return RevocationConfiguration.make_one(
            self.boto3_raw_data["RevocationConfiguration"]
        )

    IdempotencyToken = field("IdempotencyToken")
    KeyStorageSecurityStandard = field("KeyStorageSecurityStandard")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    UsageMode = field("UsageMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCertificateAuthorityRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCertificateAuthorityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
