# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_acm import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


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
class CertificateOptions:
    boto3_raw_data: "type_defs.CertificateOptionsTypeDef" = dataclasses.field()

    CertificateTransparencyLoggingPreference = field(
        "CertificateTransparencyLoggingPreference"
    )
    Export = field("Export")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CertificateOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CertificateOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtendedKeyUsage:
    boto3_raw_data: "type_defs.ExtendedKeyUsageTypeDef" = dataclasses.field()

    Name = field("Name")
    OID = field("OID")

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
class KeyUsage:
    boto3_raw_data: "type_defs.KeyUsageTypeDef" = dataclasses.field()

    Name = field("Name")

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
class CertificateSummary:
    boto3_raw_data: "type_defs.CertificateSummaryTypeDef" = dataclasses.field()

    CertificateArn = field("CertificateArn")
    DomainName = field("DomainName")
    SubjectAlternativeNameSummaries = field("SubjectAlternativeNameSummaries")
    HasAdditionalSubjectAlternativeNames = field("HasAdditionalSubjectAlternativeNames")
    Status = field("Status")
    Type = field("Type")
    KeyAlgorithm = field("KeyAlgorithm")
    KeyUsages = field("KeyUsages")
    ExtendedKeyUsages = field("ExtendedKeyUsages")
    ExportOption = field("ExportOption")
    InUse = field("InUse")
    Exported = field("Exported")
    RenewalEligibility = field("RenewalEligibility")
    NotBefore = field("NotBefore")
    NotAfter = field("NotAfter")
    CreatedAt = field("CreatedAt")
    IssuedAt = field("IssuedAt")
    ImportedAt = field("ImportedAt")
    RevokedAt = field("RevokedAt")
    ManagedBy = field("ManagedBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CertificateSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CertificateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCertificateRequest:
    boto3_raw_data: "type_defs.DeleteCertificateRequestTypeDef" = dataclasses.field()

    CertificateArn = field("CertificateArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCertificateRequest:
    boto3_raw_data: "type_defs.DescribeCertificateRequestTypeDef" = dataclasses.field()

    CertificateArn = field("CertificateArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCertificateRequestTypeDef"]
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
class DomainValidationOption:
    boto3_raw_data: "type_defs.DomainValidationOptionTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    ValidationDomain = field("ValidationDomain")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainValidationOptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainValidationOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpRedirect:
    boto3_raw_data: "type_defs.HttpRedirectTypeDef" = dataclasses.field()

    RedirectFrom = field("RedirectFrom")
    RedirectTo = field("RedirectTo")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HttpRedirectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HttpRedirectTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceRecord:
    boto3_raw_data: "type_defs.ResourceRecordTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceRecordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceRecordTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpiryEventsConfiguration:
    boto3_raw_data: "type_defs.ExpiryEventsConfigurationTypeDef" = dataclasses.field()

    DaysBeforeExpiry = field("DaysBeforeExpiry")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExpiryEventsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpiryEventsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filters:
    boto3_raw_data: "type_defs.FiltersTypeDef" = dataclasses.field()

    extendedKeyUsage = field("extendedKeyUsage")
    keyUsage = field("keyUsage")
    keyTypes = field("keyTypes")
    exportOption = field("exportOption")
    managedBy = field("managedBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FiltersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FiltersTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCertificateRequest:
    boto3_raw_data: "type_defs.GetCertificateRequestTypeDef" = dataclasses.field()

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
class ListTagsForCertificateRequest:
    boto3_raw_data: "type_defs.ListTagsForCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    CertificateArn = field("CertificateArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTagsForCertificateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RenewCertificateRequest:
    boto3_raw_data: "type_defs.RenewCertificateRequestTypeDef" = dataclasses.field()

    CertificateArn = field("CertificateArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RenewCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RenewCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResendValidationEmailRequest:
    boto3_raw_data: "type_defs.ResendValidationEmailRequestTypeDef" = (
        dataclasses.field()
    )

    CertificateArn = field("CertificateArn")
    Domain = field("Domain")
    ValidationDomain = field("ValidationDomain")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResendValidationEmailRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResendValidationEmailRequestTypeDef"]
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

    CertificateArn = field("CertificateArn")
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
class AddTagsToCertificateRequest:
    boto3_raw_data: "type_defs.AddTagsToCertificateRequestTypeDef" = dataclasses.field()

    CertificateArn = field("CertificateArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddTagsToCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddTagsToCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveTagsFromCertificateRequest:
    boto3_raw_data: "type_defs.RemoveTagsFromCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    CertificateArn = field("CertificateArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveTagsFromCertificateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveTagsFromCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportCertificateRequest:
    boto3_raw_data: "type_defs.ExportCertificateRequestTypeDef" = dataclasses.field()

    CertificateArn = field("CertificateArn")
    Passphrase = field("Passphrase")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportCertificateRequest:
    boto3_raw_data: "type_defs.ImportCertificateRequestTypeDef" = dataclasses.field()

    Certificate = field("Certificate")
    PrivateKey = field("PrivateKey")
    CertificateArn = field("CertificateArn")
    CertificateChain = field("CertificateChain")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCertificateOptionsRequest:
    boto3_raw_data: "type_defs.UpdateCertificateOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    CertificateArn = field("CertificateArn")

    @cached_property
    def Options(self):  # pragma: no cover
        return CertificateOptions.make_one(self.boto3_raw_data["Options"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateCertificateOptionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCertificateOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCertificateRequestWait:
    boto3_raw_data: "type_defs.DescribeCertificateRequestWaitTypeDef" = (
        dataclasses.field()
    )

    CertificateArn = field("CertificateArn")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCertificateRequestWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCertificateRequestWaitTypeDef"]
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
class ExportCertificateResponse:
    boto3_raw_data: "type_defs.ExportCertificateResponseTypeDef" = dataclasses.field()

    Certificate = field("Certificate")
    CertificateChain = field("CertificateChain")
    PrivateKey = field("PrivateKey")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportCertificateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportCertificateResponseTypeDef"]
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
class ImportCertificateResponse:
    boto3_raw_data: "type_defs.ImportCertificateResponseTypeDef" = dataclasses.field()

    CertificateArn = field("CertificateArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportCertificateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCertificatesResponse:
    boto3_raw_data: "type_defs.ListCertificatesResponseTypeDef" = dataclasses.field()

    @cached_property
    def CertificateSummaryList(self):  # pragma: no cover
        return CertificateSummary.make_many(
            self.boto3_raw_data["CertificateSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCertificatesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCertificatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForCertificateResponse:
    boto3_raw_data: "type_defs.ListTagsForCertificateResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTagsForCertificateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestCertificateResponse:
    boto3_raw_data: "type_defs.RequestCertificateResponseTypeDef" = dataclasses.field()

    CertificateArn = field("CertificateArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RequestCertificateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeCertificateResponse:
    boto3_raw_data: "type_defs.RevokeCertificateResponseTypeDef" = dataclasses.field()

    CertificateArn = field("CertificateArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RevokeCertificateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestCertificateRequest:
    boto3_raw_data: "type_defs.RequestCertificateRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    ValidationMethod = field("ValidationMethod")
    SubjectAlternativeNames = field("SubjectAlternativeNames")
    IdempotencyToken = field("IdempotencyToken")

    @cached_property
    def DomainValidationOptions(self):  # pragma: no cover
        return DomainValidationOption.make_many(
            self.boto3_raw_data["DomainValidationOptions"]
        )

    @cached_property
    def Options(self):  # pragma: no cover
        return CertificateOptions.make_one(self.boto3_raw_data["Options"])

    CertificateAuthorityArn = field("CertificateAuthorityArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    KeyAlgorithm = field("KeyAlgorithm")
    ManagedBy = field("ManagedBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RequestCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainValidation:
    boto3_raw_data: "type_defs.DomainValidationTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    ValidationEmails = field("ValidationEmails")
    ValidationDomain = field("ValidationDomain")
    ValidationStatus = field("ValidationStatus")

    @cached_property
    def ResourceRecord(self):  # pragma: no cover
        return ResourceRecord.make_one(self.boto3_raw_data["ResourceRecord"])

    @cached_property
    def HttpRedirect(self):  # pragma: no cover
        return HttpRedirect.make_one(self.boto3_raw_data["HttpRedirect"])

    ValidationMethod = field("ValidationMethod")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainValidationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainValidationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountConfigurationResponse:
    boto3_raw_data: "type_defs.GetAccountConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ExpiryEvents(self):  # pragma: no cover
        return ExpiryEventsConfiguration.make_one(self.boto3_raw_data["ExpiryEvents"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAccountConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAccountConfigurationRequest:
    boto3_raw_data: "type_defs.PutAccountConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    IdempotencyToken = field("IdempotencyToken")

    @cached_property
    def ExpiryEvents(self):  # pragma: no cover
        return ExpiryEventsConfiguration.make_one(self.boto3_raw_data["ExpiryEvents"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutAccountConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccountConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCertificatesRequest:
    boto3_raw_data: "type_defs.ListCertificatesRequestTypeDef" = dataclasses.field()

    CertificateStatuses = field("CertificateStatuses")

    @cached_property
    def Includes(self):  # pragma: no cover
        return Filters.make_one(self.boto3_raw_data["Includes"])

    NextToken = field("NextToken")
    MaxItems = field("MaxItems")
    SortBy = field("SortBy")
    SortOrder = field("SortOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCertificatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCertificatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCertificatesRequestPaginate:
    boto3_raw_data: "type_defs.ListCertificatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    CertificateStatuses = field("CertificateStatuses")

    @cached_property
    def Includes(self):  # pragma: no cover
        return Filters.make_one(self.boto3_raw_data["Includes"])

    SortBy = field("SortBy")
    SortOrder = field("SortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCertificatesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCertificatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RenewalSummary:
    boto3_raw_data: "type_defs.RenewalSummaryTypeDef" = dataclasses.field()

    RenewalStatus = field("RenewalStatus")

    @cached_property
    def DomainValidationOptions(self):  # pragma: no cover
        return DomainValidation.make_many(
            self.boto3_raw_data["DomainValidationOptions"]
        )

    UpdatedAt = field("UpdatedAt")
    RenewalStatusReason = field("RenewalStatusReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RenewalSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RenewalSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CertificateDetail:
    boto3_raw_data: "type_defs.CertificateDetailTypeDef" = dataclasses.field()

    CertificateArn = field("CertificateArn")
    DomainName = field("DomainName")
    SubjectAlternativeNames = field("SubjectAlternativeNames")
    ManagedBy = field("ManagedBy")

    @cached_property
    def DomainValidationOptions(self):  # pragma: no cover
        return DomainValidation.make_many(
            self.boto3_raw_data["DomainValidationOptions"]
        )

    Serial = field("Serial")
    Subject = field("Subject")
    Issuer = field("Issuer")
    CreatedAt = field("CreatedAt")
    IssuedAt = field("IssuedAt")
    ImportedAt = field("ImportedAt")
    Status = field("Status")
    RevokedAt = field("RevokedAt")
    RevocationReason = field("RevocationReason")
    NotBefore = field("NotBefore")
    NotAfter = field("NotAfter")
    KeyAlgorithm = field("KeyAlgorithm")
    SignatureAlgorithm = field("SignatureAlgorithm")
    InUseBy = field("InUseBy")
    FailureReason = field("FailureReason")
    Type = field("Type")

    @cached_property
    def RenewalSummary(self):  # pragma: no cover
        return RenewalSummary.make_one(self.boto3_raw_data["RenewalSummary"])

    @cached_property
    def KeyUsages(self):  # pragma: no cover
        return KeyUsage.make_many(self.boto3_raw_data["KeyUsages"])

    @cached_property
    def ExtendedKeyUsages(self):  # pragma: no cover
        return ExtendedKeyUsage.make_many(self.boto3_raw_data["ExtendedKeyUsages"])

    CertificateAuthorityArn = field("CertificateAuthorityArn")
    RenewalEligibility = field("RenewalEligibility")

    @cached_property
    def Options(self):  # pragma: no cover
        return CertificateOptions.make_one(self.boto3_raw_data["Options"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CertificateDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CertificateDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCertificateResponse:
    boto3_raw_data: "type_defs.DescribeCertificateResponseTypeDef" = dataclasses.field()

    @cached_property
    def Certificate(self):  # pragma: no cover
        return CertificateDetail.make_one(self.boto3_raw_data["Certificate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCertificateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
