# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cloudfront import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AliasICPRecordal:
    boto3_raw_data: "type_defs.AliasICPRecordalTypeDef" = dataclasses.field()

    CNAME = field("CNAME")
    ICPRecordalStatus = field("ICPRecordalStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AliasICPRecordalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AliasICPRecordalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AliasesOutput:
    boto3_raw_data: "type_defs.AliasesOutputTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AliasesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AliasesOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Aliases:
    boto3_raw_data: "type_defs.AliasesTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AliasesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AliasesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CachedMethodsOutput:
    boto3_raw_data: "type_defs.CachedMethodsOutputTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CachedMethodsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CachedMethodsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnycastIpListSummary:
    boto3_raw_data: "type_defs.AnycastIpListSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Status = field("Status")
    Arn = field("Arn")
    IpCount = field("IpCount")
    LastModifiedTime = field("LastModifiedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnycastIpListSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnycastIpListSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnycastIpList:
    boto3_raw_data: "type_defs.AnycastIpListTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Status = field("Status")
    Arn = field("Arn")
    AnycastIps = field("AnycastIps")
    IpCount = field("IpCount")
    LastModifiedTime = field("LastModifiedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnycastIpListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnycastIpListTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateAliasRequest:
    boto3_raw_data: "type_defs.AssociateAliasRequestTypeDef" = dataclasses.field()

    TargetDistributionId = field("TargetDistributionId")
    Alias = field("Alias")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateDistributionTenantWebACLRequest:
    boto3_raw_data: "type_defs.AssociateDistributionTenantWebACLRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    WebACLArn = field("WebACLArn")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateDistributionTenantWebACLRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateDistributionTenantWebACLRequestTypeDef"]
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
class AssociateDistributionWebACLRequest:
    boto3_raw_data: "type_defs.AssociateDistributionWebACLRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    WebACLArn = field("WebACLArn")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateDistributionWebACLRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateDistributionWebACLRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrpcConfig:
    boto3_raw_data: "type_defs.GrpcConfigTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GrpcConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GrpcConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrustedKeyGroupsOutput:
    boto3_raw_data: "type_defs.TrustedKeyGroupsOutputTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrustedKeyGroupsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrustedKeyGroupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrustedSignersOutput:
    boto3_raw_data: "type_defs.TrustedSignersOutputTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrustedSignersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrustedSignersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CookieNamesOutput:
    boto3_raw_data: "type_defs.CookieNamesOutputTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CookieNamesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CookieNamesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CookieNames:
    boto3_raw_data: "type_defs.CookieNamesTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CookieNamesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CookieNamesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HeadersOutput:
    boto3_raw_data: "type_defs.HeadersOutputTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HeadersOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HeadersOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Headers:
    boto3_raw_data: "type_defs.HeadersTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HeadersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HeadersTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryStringNamesOutput:
    boto3_raw_data: "type_defs.QueryStringNamesOutputTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryStringNamesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryStringNamesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryStringNames:
    boto3_raw_data: "type_defs.QueryStringNamesTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryStringNamesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryStringNamesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CachedMethods:
    boto3_raw_data: "type_defs.CachedMethodsTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CachedMethodsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CachedMethodsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Certificate:
    boto3_raw_data: "type_defs.CertificateTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CertificateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CertificateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudFrontOriginAccessIdentityConfig:
    boto3_raw_data: "type_defs.CloudFrontOriginAccessIdentityConfigTypeDef" = (
        dataclasses.field()
    )

    CallerReference = field("CallerReference")
    Comment = field("Comment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CloudFrontOriginAccessIdentityConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudFrontOriginAccessIdentityConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudFrontOriginAccessIdentitySummary:
    boto3_raw_data: "type_defs.CloudFrontOriginAccessIdentitySummaryTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    S3CanonicalUserId = field("S3CanonicalUserId")
    Comment = field("Comment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CloudFrontOriginAccessIdentitySummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudFrontOriginAccessIdentitySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConflictingAlias:
    boto3_raw_data: "type_defs.ConflictingAliasTypeDef" = dataclasses.field()

    Alias = field("Alias")
    DistributionId = field("DistributionId")
    AccountId = field("AccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConflictingAliasTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConflictingAliasTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionGroupAssociationFilter:
    boto3_raw_data: "type_defs.ConnectionGroupAssociationFilterTypeDef" = (
        dataclasses.field()
    )

    AnycastIpListId = field("AnycastIpListId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConnectionGroupAssociationFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionGroupAssociationFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionGroupSummary:
    boto3_raw_data: "type_defs.ConnectionGroupSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Arn = field("Arn")
    RoutingEndpoint = field("RoutingEndpoint")
    CreatedTime = field("CreatedTime")
    LastModifiedTime = field("LastModifiedTime")
    ETag = field("ETag")
    AnycastIpListId = field("AnycastIpListId")
    Enabled = field("Enabled")
    Status = field("Status")
    IsDefault = field("IsDefault")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectionGroupSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionGroupSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentTypeProfile:
    boto3_raw_data: "type_defs.ContentTypeProfileTypeDef" = dataclasses.field()

    Format = field("Format")
    ContentType = field("ContentType")
    ProfileId = field("ProfileId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContentTypeProfileTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentTypeProfileTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StagingDistributionDnsNamesOutput:
    boto3_raw_data: "type_defs.StagingDistributionDnsNamesOutputTypeDef" = (
        dataclasses.field()
    )

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StagingDistributionDnsNamesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StagingDistributionDnsNamesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StagingDistributionDnsNames:
    boto3_raw_data: "type_defs.StagingDistributionDnsNamesTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StagingDistributionDnsNamesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StagingDistributionDnsNamesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContinuousDeploymentSingleHeaderConfig:
    boto3_raw_data: "type_defs.ContinuousDeploymentSingleHeaderConfigTypeDef" = (
        dataclasses.field()
    )

    Header = field("Header")
    Value = field("Value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ContinuousDeploymentSingleHeaderConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContinuousDeploymentSingleHeaderConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionStickinessConfig:
    boto3_raw_data: "type_defs.SessionStickinessConfigTypeDef" = dataclasses.field()

    IdleTTL = field("IdleTTL")
    MaximumTTL = field("MaximumTTL")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SessionStickinessConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionStickinessConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyDistributionRequest:
    boto3_raw_data: "type_defs.CopyDistributionRequestTypeDef" = dataclasses.field()

    PrimaryDistributionId = field("PrimaryDistributionId")
    CallerReference = field("CallerReference")
    Staging = field("Staging")
    IfMatch = field("IfMatch")
    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyDistributionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyDistributionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainItem:
    boto3_raw_data: "type_defs.DomainItemTypeDef" = dataclasses.field()

    Domain = field("Domain")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainItemTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedCertificateRequest:
    boto3_raw_data: "type_defs.ManagedCertificateRequestTypeDef" = dataclasses.field()

    ValidationTokenHost = field("ValidationTokenHost")
    PrimaryDomainName = field("PrimaryDomainName")
    CertificateTransparencyLoggingPreference = field(
        "CertificateTransparencyLoggingPreference"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Parameter:
    boto3_raw_data: "type_defs.ParameterTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParameterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportSource:
    boto3_raw_data: "type_defs.ImportSourceTypeDef" = dataclasses.field()

    SourceType = field("SourceType")
    SourceARN = field("SourceARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImportSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyValueStore:
    boto3_raw_data: "type_defs.KeyValueStoreTypeDef" = dataclasses.field()

    Name = field("Name")
    Id = field("Id")
    Comment = field("Comment")
    ARN = field("ARN")
    LastModifiedTime = field("LastModifiedTime")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyValueStoreTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyValueStoreTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginAccessControlConfig:
    boto3_raw_data: "type_defs.OriginAccessControlConfigTypeDef" = dataclasses.field()

    Name = field("Name")
    SigningProtocol = field("SigningProtocol")
    SigningBehavior = field("SigningBehavior")
    OriginAccessControlOriginType = field("OriginAccessControlOriginType")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OriginAccessControlConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginAccessControlConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublicKeyConfig:
    boto3_raw_data: "type_defs.PublicKeyConfigTypeDef" = dataclasses.field()

    CallerReference = field("CallerReference")
    Name = field("Name")
    EncodedKey = field("EncodedKey")
    Comment = field("Comment")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PublicKeyConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PublicKeyConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomErrorResponse:
    boto3_raw_data: "type_defs.CustomErrorResponseTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    ResponsePagePath = field("ResponsePagePath")
    ResponseCode = field("ResponseCode")
    ErrorCachingMinTTL = field("ErrorCachingMinTTL")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomErrorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomErrorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginCustomHeader:
    boto3_raw_data: "type_defs.OriginCustomHeaderTypeDef" = dataclasses.field()

    HeaderName = field("HeaderName")
    HeaderValue = field("HeaderValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OriginCustomHeaderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginCustomHeaderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginSslProtocolsOutput:
    boto3_raw_data: "type_defs.OriginSslProtocolsOutputTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OriginSslProtocolsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginSslProtocolsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeoRestrictionCustomizationOutput:
    boto3_raw_data: "type_defs.GeoRestrictionCustomizationOutputTypeDef" = (
        dataclasses.field()
    )

    RestrictionType = field("RestrictionType")
    Locations = field("Locations")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GeoRestrictionCustomizationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeoRestrictionCustomizationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebAclCustomization:
    boto3_raw_data: "type_defs.WebAclCustomizationTypeDef" = dataclasses.field()

    Action = field("Action")
    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WebAclCustomizationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebAclCustomizationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeoRestrictionCustomization:
    boto3_raw_data: "type_defs.GeoRestrictionCustomizationTypeDef" = dataclasses.field()

    RestrictionType = field("RestrictionType")
    Locations = field("Locations")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GeoRestrictionCustomizationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeoRestrictionCustomizationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAnycastIpListRequest:
    boto3_raw_data: "type_defs.DeleteAnycastIpListRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAnycastIpListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAnycastIpListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCachePolicyRequest:
    boto3_raw_data: "type_defs.DeleteCachePolicyRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCachePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCachePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCloudFrontOriginAccessIdentityRequest:
    boto3_raw_data: "type_defs.DeleteCloudFrontOriginAccessIdentityRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCloudFrontOriginAccessIdentityRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCloudFrontOriginAccessIdentityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConnectionGroupRequest:
    boto3_raw_data: "type_defs.DeleteConnectionGroupRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConnectionGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectionGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteContinuousDeploymentPolicyRequest:
    boto3_raw_data: "type_defs.DeleteContinuousDeploymentPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteContinuousDeploymentPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteContinuousDeploymentPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDistributionRequest:
    boto3_raw_data: "type_defs.DeleteDistributionRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDistributionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDistributionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDistributionTenantRequest:
    boto3_raw_data: "type_defs.DeleteDistributionTenantRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDistributionTenantRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDistributionTenantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFieldLevelEncryptionConfigRequest:
    boto3_raw_data: "type_defs.DeleteFieldLevelEncryptionConfigRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteFieldLevelEncryptionConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFieldLevelEncryptionConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFieldLevelEncryptionProfileRequest:
    boto3_raw_data: "type_defs.DeleteFieldLevelEncryptionProfileRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteFieldLevelEncryptionProfileRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFieldLevelEncryptionProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFunctionRequest:
    boto3_raw_data: "type_defs.DeleteFunctionRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFunctionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFunctionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKeyGroupRequest:
    boto3_raw_data: "type_defs.DeleteKeyGroupRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteKeyGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKeyGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKeyValueStoreRequest:
    boto3_raw_data: "type_defs.DeleteKeyValueStoreRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteKeyValueStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKeyValueStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMonitoringSubscriptionRequest:
    boto3_raw_data: "type_defs.DeleteMonitoringSubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    DistributionId = field("DistributionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteMonitoringSubscriptionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMonitoringSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOriginAccessControlRequest:
    boto3_raw_data: "type_defs.DeleteOriginAccessControlRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteOriginAccessControlRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOriginAccessControlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOriginRequestPolicyRequest:
    boto3_raw_data: "type_defs.DeleteOriginRequestPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteOriginRequestPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOriginRequestPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePublicKeyRequest:
    boto3_raw_data: "type_defs.DeletePublicKeyRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePublicKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePublicKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRealtimeLogConfigRequest:
    boto3_raw_data: "type_defs.DeleteRealtimeLogConfigRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    ARN = field("ARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteRealtimeLogConfigRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRealtimeLogConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResponseHeadersPolicyRequest:
    boto3_raw_data: "type_defs.DeleteResponseHeadersPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteResponseHeadersPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResponseHeadersPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStreamingDistributionRequest:
    boto3_raw_data: "type_defs.DeleteStreamingDistributionRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteStreamingDistributionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStreamingDistributionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVpcOriginRequest:
    boto3_raw_data: "type_defs.DeleteVpcOriginRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVpcOriginRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVpcOriginRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFunctionRequest:
    boto3_raw_data: "type_defs.DescribeFunctionRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Stage = field("Stage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFunctionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFunctionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeKeyValueStoreRequest:
    boto3_raw_data: "type_defs.DescribeKeyValueStoreRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeKeyValueStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeKeyValueStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateDistributionTenantWebACLRequest:
    boto3_raw_data: "type_defs.DisassociateDistributionTenantWebACLRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateDistributionTenantWebACLRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateDistributionTenantWebACLRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateDistributionWebACLRequest:
    boto3_raw_data: "type_defs.DisassociateDistributionWebACLRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateDistributionWebACLRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateDistributionWebACLRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingConfig:
    boto3_raw_data: "type_defs.LoggingConfigTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    IncludeCookies = field("IncludeCookies")
    Bucket = field("Bucket")
    Prefix = field("Prefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoggingConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoggingConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ViewerCertificate:
    boto3_raw_data: "type_defs.ViewerCertificateTypeDef" = dataclasses.field()

    CloudFrontDefaultCertificate = field("CloudFrontDefaultCertificate")
    IAMCertificateId = field("IAMCertificateId")
    ACMCertificateArn = field("ACMCertificateArn")
    SSLSupportMethod = field("SSLSupportMethod")
    MinimumProtocolVersion = field("MinimumProtocolVersion")
    Certificate = field("Certificate")
    CertificateSource = field("CertificateSource")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ViewerCertificateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ViewerCertificateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DistributionIdList:
    boto3_raw_data: "type_defs.DistributionIdListTypeDef" = dataclasses.field()

    Marker = field("Marker")
    MaxItems = field("MaxItems")
    IsTruncated = field("IsTruncated")
    Quantity = field("Quantity")
    NextMarker = field("NextMarker")
    Items = field("Items")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DistributionIdListTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DistributionIdListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DistributionResourceId:
    boto3_raw_data: "type_defs.DistributionResourceIdTypeDef" = dataclasses.field()

    DistributionId = field("DistributionId")
    DistributionTenantId = field("DistributionTenantId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DistributionResourceIdTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DistributionResourceIdTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DistributionTenantAssociationFilter:
    boto3_raw_data: "type_defs.DistributionTenantAssociationFilterTypeDef" = (
        dataclasses.field()
    )

    DistributionId = field("DistributionId")
    ConnectionGroupId = field("ConnectionGroupId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DistributionTenantAssociationFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DistributionTenantAssociationFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainResult:
    boto3_raw_data: "type_defs.DomainResultTypeDef" = dataclasses.field()

    Domain = field("Domain")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DnsConfiguration:
    boto3_raw_data: "type_defs.DnsConfigurationTypeDef" = dataclasses.field()

    Domain = field("Domain")
    Status = field("Status")
    Reason = field("Reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DnsConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DnsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainConflict:
    boto3_raw_data: "type_defs.DomainConflictTypeDef" = dataclasses.field()

    Domain = field("Domain")
    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")
    AccountId = field("AccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainConflictTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainConflictTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldPatternsOutput:
    boto3_raw_data: "type_defs.FieldPatternsOutputTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FieldPatternsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldPatternsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldPatterns:
    boto3_raw_data: "type_defs.FieldPatternsTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldPatternsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldPatternsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisStreamConfig:
    boto3_raw_data: "type_defs.KinesisStreamConfigTypeDef" = dataclasses.field()

    RoleARN = field("RoleARN")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisStreamConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisStreamConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryStringCacheKeysOutput:
    boto3_raw_data: "type_defs.QueryStringCacheKeysOutputTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryStringCacheKeysOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryStringCacheKeysOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionAssociation:
    boto3_raw_data: "type_defs.FunctionAssociationTypeDef" = dataclasses.field()

    FunctionARN = field("FunctionARN")
    EventType = field("EventType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FunctionAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionMetadata:
    boto3_raw_data: "type_defs.FunctionMetadataTypeDef" = dataclasses.field()

    FunctionARN = field("FunctionARN")
    LastModifiedTime = field("LastModifiedTime")
    Stage = field("Stage")
    CreatedTime = field("CreatedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FunctionMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeoRestrictionOutput:
    boto3_raw_data: "type_defs.GeoRestrictionOutputTypeDef" = dataclasses.field()

    RestrictionType = field("RestrictionType")
    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GeoRestrictionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeoRestrictionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeoRestriction:
    boto3_raw_data: "type_defs.GeoRestrictionTypeDef" = dataclasses.field()

    RestrictionType = field("RestrictionType")
    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GeoRestrictionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GeoRestrictionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnycastIpListRequest:
    boto3_raw_data: "type_defs.GetAnycastIpListRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAnycastIpListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnycastIpListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCachePolicyConfigRequest:
    boto3_raw_data: "type_defs.GetCachePolicyConfigRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCachePolicyConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCachePolicyConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCachePolicyRequest:
    boto3_raw_data: "type_defs.GetCachePolicyRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCachePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCachePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCloudFrontOriginAccessIdentityConfigRequest:
    boto3_raw_data: (
        "type_defs.GetCloudFrontOriginAccessIdentityConfigRequestTypeDef"
    ) = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCloudFrontOriginAccessIdentityConfigRequestTypeDef"
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
                "type_defs.GetCloudFrontOriginAccessIdentityConfigRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCloudFrontOriginAccessIdentityRequest:
    boto3_raw_data: "type_defs.GetCloudFrontOriginAccessIdentityRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCloudFrontOriginAccessIdentityRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCloudFrontOriginAccessIdentityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectionGroupByRoutingEndpointRequest:
    boto3_raw_data: "type_defs.GetConnectionGroupByRoutingEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    RoutingEndpoint = field("RoutingEndpoint")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConnectionGroupByRoutingEndpointRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectionGroupByRoutingEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectionGroupRequest:
    boto3_raw_data: "type_defs.GetConnectionGroupRequestTypeDef" = dataclasses.field()

    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectionGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectionGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContinuousDeploymentPolicyConfigRequest:
    boto3_raw_data: "type_defs.GetContinuousDeploymentPolicyConfigRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetContinuousDeploymentPolicyConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContinuousDeploymentPolicyConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContinuousDeploymentPolicyRequest:
    boto3_raw_data: "type_defs.GetContinuousDeploymentPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetContinuousDeploymentPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContinuousDeploymentPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDistributionConfigRequest:
    boto3_raw_data: "type_defs.GetDistributionConfigRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDistributionConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDistributionConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDistributionRequest:
    boto3_raw_data: "type_defs.GetDistributionRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDistributionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDistributionRequestTypeDef"]
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
class GetDistributionTenantByDomainRequest:
    boto3_raw_data: "type_defs.GetDistributionTenantByDomainRequestTypeDef" = (
        dataclasses.field()
    )

    Domain = field("Domain")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDistributionTenantByDomainRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDistributionTenantByDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDistributionTenantRequest:
    boto3_raw_data: "type_defs.GetDistributionTenantRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDistributionTenantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDistributionTenantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFieldLevelEncryptionConfigRequest:
    boto3_raw_data: "type_defs.GetFieldLevelEncryptionConfigRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFieldLevelEncryptionConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFieldLevelEncryptionConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFieldLevelEncryptionProfileConfigRequest:
    boto3_raw_data: "type_defs.GetFieldLevelEncryptionProfileConfigRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFieldLevelEncryptionProfileConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFieldLevelEncryptionProfileConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFieldLevelEncryptionProfileRequest:
    boto3_raw_data: "type_defs.GetFieldLevelEncryptionProfileRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFieldLevelEncryptionProfileRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFieldLevelEncryptionProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFieldLevelEncryptionRequest:
    boto3_raw_data: "type_defs.GetFieldLevelEncryptionRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetFieldLevelEncryptionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFieldLevelEncryptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFunctionRequest:
    boto3_raw_data: "type_defs.GetFunctionRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Stage = field("Stage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFunctionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInvalidationForDistributionTenantRequest:
    boto3_raw_data: "type_defs.GetInvalidationForDistributionTenantRequestTypeDef" = (
        dataclasses.field()
    )

    DistributionTenantId = field("DistributionTenantId")
    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetInvalidationForDistributionTenantRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInvalidationForDistributionTenantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInvalidationRequest:
    boto3_raw_data: "type_defs.GetInvalidationRequestTypeDef" = dataclasses.field()

    DistributionId = field("DistributionId")
    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInvalidationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInvalidationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKeyGroupConfigRequest:
    boto3_raw_data: "type_defs.GetKeyGroupConfigRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKeyGroupConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKeyGroupConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyGroupConfigOutput:
    boto3_raw_data: "type_defs.KeyGroupConfigOutputTypeDef" = dataclasses.field()

    Name = field("Name")
    Items = field("Items")
    Comment = field("Comment")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KeyGroupConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeyGroupConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKeyGroupRequest:
    boto3_raw_data: "type_defs.GetKeyGroupRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKeyGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKeyGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetManagedCertificateDetailsRequest:
    boto3_raw_data: "type_defs.GetManagedCertificateDetailsRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetManagedCertificateDetailsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetManagedCertificateDetailsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMonitoringSubscriptionRequest:
    boto3_raw_data: "type_defs.GetMonitoringSubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    DistributionId = field("DistributionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMonitoringSubscriptionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMonitoringSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOriginAccessControlConfigRequest:
    boto3_raw_data: "type_defs.GetOriginAccessControlConfigRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOriginAccessControlConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOriginAccessControlConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOriginAccessControlRequest:
    boto3_raw_data: "type_defs.GetOriginAccessControlRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetOriginAccessControlRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOriginAccessControlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOriginRequestPolicyConfigRequest:
    boto3_raw_data: "type_defs.GetOriginRequestPolicyConfigRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOriginRequestPolicyConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOriginRequestPolicyConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOriginRequestPolicyRequest:
    boto3_raw_data: "type_defs.GetOriginRequestPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetOriginRequestPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOriginRequestPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPublicKeyConfigRequest:
    boto3_raw_data: "type_defs.GetPublicKeyConfigRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPublicKeyConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPublicKeyConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPublicKeyRequest:
    boto3_raw_data: "type_defs.GetPublicKeyRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPublicKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPublicKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRealtimeLogConfigRequest:
    boto3_raw_data: "type_defs.GetRealtimeLogConfigRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    ARN = field("ARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRealtimeLogConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRealtimeLogConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResponseHeadersPolicyConfigRequest:
    boto3_raw_data: "type_defs.GetResponseHeadersPolicyConfigRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetResponseHeadersPolicyConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResponseHeadersPolicyConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResponseHeadersPolicyRequest:
    boto3_raw_data: "type_defs.GetResponseHeadersPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetResponseHeadersPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResponseHeadersPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStreamingDistributionConfigRequest:
    boto3_raw_data: "type_defs.GetStreamingDistributionConfigRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetStreamingDistributionConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStreamingDistributionConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStreamingDistributionRequest:
    boto3_raw_data: "type_defs.GetStreamingDistributionRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetStreamingDistributionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStreamingDistributionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVpcOriginRequest:
    boto3_raw_data: "type_defs.GetVpcOriginRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVpcOriginRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVpcOriginRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PathsOutput:
    boto3_raw_data: "type_defs.PathsOutputTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PathsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PathsOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Paths:
    boto3_raw_data: "type_defs.PathsTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PathsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PathsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvalidationSummary:
    boto3_raw_data: "type_defs.InvalidationSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    CreateTime = field("CreateTime")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvalidationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvalidationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyPairIds:
    boto3_raw_data: "type_defs.KeyPairIdsTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyPairIdsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyPairIdsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyGroupConfig:
    boto3_raw_data: "type_defs.KeyGroupConfigTypeDef" = dataclasses.field()

    Name = field("Name")
    Items = field("Items")
    Comment = field("Comment")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyGroupConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyGroupConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyValueStoreAssociation:
    boto3_raw_data: "type_defs.KeyValueStoreAssociationTypeDef" = dataclasses.field()

    KeyValueStoreARN = field("KeyValueStoreARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KeyValueStoreAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeyValueStoreAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionAssociation:
    boto3_raw_data: "type_defs.LambdaFunctionAssociationTypeDef" = dataclasses.field()

    LambdaFunctionARN = field("LambdaFunctionARN")
    EventType = field("EventType")
    IncludeBody = field("IncludeBody")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaFunctionAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnycastIpListsRequest:
    boto3_raw_data: "type_defs.ListAnycastIpListsRequestTypeDef" = dataclasses.field()

    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAnycastIpListsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnycastIpListsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCachePoliciesRequest:
    boto3_raw_data: "type_defs.ListCachePoliciesRequestTypeDef" = dataclasses.field()

    Type = field("Type")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCachePoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCachePoliciesRequestTypeDef"]
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
class ListCloudFrontOriginAccessIdentitiesRequest:
    boto3_raw_data: "type_defs.ListCloudFrontOriginAccessIdentitiesRequestTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCloudFrontOriginAccessIdentitiesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCloudFrontOriginAccessIdentitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConflictingAliasesRequest:
    boto3_raw_data: "type_defs.ListConflictingAliasesRequestTypeDef" = (
        dataclasses.field()
    )

    DistributionId = field("DistributionId")
    Alias = field("Alias")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListConflictingAliasesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConflictingAliasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContinuousDeploymentPoliciesRequest:
    boto3_raw_data: "type_defs.ListContinuousDeploymentPoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListContinuousDeploymentPoliciesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContinuousDeploymentPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionTenantsByCustomizationRequest:
    boto3_raw_data: "type_defs.ListDistributionTenantsByCustomizationRequestTypeDef" = (
        dataclasses.field()
    )

    WebACLArn = field("WebACLArn")
    CertificateArn = field("CertificateArn")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionTenantsByCustomizationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionTenantsByCustomizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionsByAnycastIpListIdRequest:
    boto3_raw_data: "type_defs.ListDistributionsByAnycastIpListIdRequestTypeDef" = (
        dataclasses.field()
    )

    AnycastIpListId = field("AnycastIpListId")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionsByAnycastIpListIdRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionsByAnycastIpListIdRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionsByCachePolicyIdRequest:
    boto3_raw_data: "type_defs.ListDistributionsByCachePolicyIdRequestTypeDef" = (
        dataclasses.field()
    )

    CachePolicyId = field("CachePolicyId")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionsByCachePolicyIdRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionsByCachePolicyIdRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionsByConnectionModeRequest:
    boto3_raw_data: "type_defs.ListDistributionsByConnectionModeRequestTypeDef" = (
        dataclasses.field()
    )

    ConnectionMode = field("ConnectionMode")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionsByConnectionModeRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionsByConnectionModeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionsByKeyGroupRequest:
    boto3_raw_data: "type_defs.ListDistributionsByKeyGroupRequestTypeDef" = (
        dataclasses.field()
    )

    KeyGroupId = field("KeyGroupId")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionsByKeyGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionsByKeyGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionsByOriginRequestPolicyIdRequest:
    boto3_raw_data: (
        "type_defs.ListDistributionsByOriginRequestPolicyIdRequestTypeDef"
    ) = dataclasses.field()

    OriginRequestPolicyId = field("OriginRequestPolicyId")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionsByOriginRequestPolicyIdRequestTypeDef"
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
                "type_defs.ListDistributionsByOriginRequestPolicyIdRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionsByRealtimeLogConfigRequest:
    boto3_raw_data: "type_defs.ListDistributionsByRealtimeLogConfigRequestTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")
    MaxItems = field("MaxItems")
    RealtimeLogConfigName = field("RealtimeLogConfigName")
    RealtimeLogConfigArn = field("RealtimeLogConfigArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionsByRealtimeLogConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionsByRealtimeLogConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionsByResponseHeadersPolicyIdRequest:
    boto3_raw_data: (
        "type_defs.ListDistributionsByResponseHeadersPolicyIdRequestTypeDef"
    ) = dataclasses.field()

    ResponseHeadersPolicyId = field("ResponseHeadersPolicyId")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionsByResponseHeadersPolicyIdRequestTypeDef"
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
                "type_defs.ListDistributionsByResponseHeadersPolicyIdRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionsByVpcOriginIdRequest:
    boto3_raw_data: "type_defs.ListDistributionsByVpcOriginIdRequestTypeDef" = (
        dataclasses.field()
    )

    VpcOriginId = field("VpcOriginId")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionsByVpcOriginIdRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionsByVpcOriginIdRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionsByWebACLIdRequest:
    boto3_raw_data: "type_defs.ListDistributionsByWebACLIdRequestTypeDef" = (
        dataclasses.field()
    )

    WebACLId = field("WebACLId")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionsByWebACLIdRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionsByWebACLIdRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionsRequest:
    boto3_raw_data: "type_defs.ListDistributionsRequestTypeDef" = dataclasses.field()

    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDistributionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFieldLevelEncryptionConfigsRequest:
    boto3_raw_data: "type_defs.ListFieldLevelEncryptionConfigsRequestTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFieldLevelEncryptionConfigsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFieldLevelEncryptionConfigsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFieldLevelEncryptionProfilesRequest:
    boto3_raw_data: "type_defs.ListFieldLevelEncryptionProfilesRequestTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFieldLevelEncryptionProfilesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFieldLevelEncryptionProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFunctionsRequest:
    boto3_raw_data: "type_defs.ListFunctionsRequestTypeDef" = dataclasses.field()

    Marker = field("Marker")
    MaxItems = field("MaxItems")
    Stage = field("Stage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFunctionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFunctionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvalidationsForDistributionTenantRequest:
    boto3_raw_data: "type_defs.ListInvalidationsForDistributionTenantRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInvalidationsForDistributionTenantRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvalidationsForDistributionTenantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvalidationsRequest:
    boto3_raw_data: "type_defs.ListInvalidationsRequestTypeDef" = dataclasses.field()

    DistributionId = field("DistributionId")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInvalidationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvalidationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeyGroupsRequest:
    boto3_raw_data: "type_defs.ListKeyGroupsRequestTypeDef" = dataclasses.field()

    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKeyGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeyGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeyValueStoresRequest:
    boto3_raw_data: "type_defs.ListKeyValueStoresRequestTypeDef" = dataclasses.field()

    Marker = field("Marker")
    MaxItems = field("MaxItems")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKeyValueStoresRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeyValueStoresRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOriginAccessControlsRequest:
    boto3_raw_data: "type_defs.ListOriginAccessControlsRequestTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOriginAccessControlsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOriginAccessControlsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOriginRequestPoliciesRequest:
    boto3_raw_data: "type_defs.ListOriginRequestPoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOriginRequestPoliciesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOriginRequestPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPublicKeysRequest:
    boto3_raw_data: "type_defs.ListPublicKeysRequestTypeDef" = dataclasses.field()

    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPublicKeysRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPublicKeysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRealtimeLogConfigsRequest:
    boto3_raw_data: "type_defs.ListRealtimeLogConfigsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxItems = field("MaxItems")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRealtimeLogConfigsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRealtimeLogConfigsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResponseHeadersPoliciesRequest:
    boto3_raw_data: "type_defs.ListResponseHeadersPoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResponseHeadersPoliciesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResponseHeadersPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamingDistributionsRequest:
    boto3_raw_data: "type_defs.ListStreamingDistributionsRequestTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStreamingDistributionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamingDistributionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    Resource = field("Resource")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVpcOriginsRequest:
    boto3_raw_data: "type_defs.ListVpcOriginsRequestTypeDef" = dataclasses.field()

    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVpcOriginsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVpcOriginsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidationTokenDetail:
    boto3_raw_data: "type_defs.ValidationTokenDetailTypeDef" = dataclasses.field()

    Domain = field("Domain")
    RedirectTo = field("RedirectTo")
    RedirectFrom = field("RedirectFrom")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValidationTokenDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidationTokenDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealtimeMetricsSubscriptionConfig:
    boto3_raw_data: "type_defs.RealtimeMetricsSubscriptionConfigTypeDef" = (
        dataclasses.field()
    )

    RealtimeMetricsSubscriptionStatus = field("RealtimeMetricsSubscriptionStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RealtimeMetricsSubscriptionConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RealtimeMetricsSubscriptionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginAccessControlSummary:
    boto3_raw_data: "type_defs.OriginAccessControlSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Description = field("Description")
    Name = field("Name")
    SigningProtocol = field("SigningProtocol")
    SigningBehavior = field("SigningBehavior")
    OriginAccessControlOriginType = field("OriginAccessControlOriginType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OriginAccessControlSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginAccessControlSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatusCodesOutput:
    boto3_raw_data: "type_defs.StatusCodesOutputTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatusCodesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StatusCodesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginGroupMember:
    boto3_raw_data: "type_defs.OriginGroupMemberTypeDef" = dataclasses.field()

    OriginId = field("OriginId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OriginGroupMemberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginGroupMemberTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginShield:
    boto3_raw_data: "type_defs.OriginShieldTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    OriginShieldRegion = field("OriginShieldRegion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OriginShieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OriginShieldTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3OriginConfig:
    boto3_raw_data: "type_defs.S3OriginConfigTypeDef" = dataclasses.field()

    OriginAccessIdentity = field("OriginAccessIdentity")
    OriginReadTimeout = field("OriginReadTimeout")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3OriginConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3OriginConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcOriginConfig:
    boto3_raw_data: "type_defs.VpcOriginConfigTypeDef" = dataclasses.field()

    VpcOriginId = field("VpcOriginId")
    OriginReadTimeout = field("OriginReadTimeout")
    OriginKeepaliveTimeout = field("OriginKeepaliveTimeout")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcOriginConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcOriginConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginSslProtocols:
    boto3_raw_data: "type_defs.OriginSslProtocolsTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OriginSslProtocolsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginSslProtocolsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StringSchemaConfig:
    boto3_raw_data: "type_defs.StringSchemaConfigTypeDef" = dataclasses.field()

    Required = field("Required")
    Comment = field("Comment")
    DefaultValue = field("DefaultValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StringSchemaConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StringSchemaConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublicKeySummary:
    boto3_raw_data: "type_defs.PublicKeySummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    CreatedTime = field("CreatedTime")
    EncodedKey = field("EncodedKey")
    Comment = field("Comment")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PublicKeySummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublicKeySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublishFunctionRequest:
    boto3_raw_data: "type_defs.PublishFunctionRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PublishFunctionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublishFunctionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryArgProfile:
    boto3_raw_data: "type_defs.QueryArgProfileTypeDef" = dataclasses.field()

    QueryArg = field("QueryArg")
    ProfileId = field("ProfileId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryArgProfileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryArgProfileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryStringCacheKeys:
    boto3_raw_data: "type_defs.QueryStringCacheKeysTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryStringCacheKeysTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryStringCacheKeysTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyAccessControlAllowHeadersOutput:
    boto3_raw_data: (
        "type_defs.ResponseHeadersPolicyAccessControlAllowHeadersOutputTypeDef"
    ) = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyAccessControlAllowHeadersOutputTypeDef"
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
                "type_defs.ResponseHeadersPolicyAccessControlAllowHeadersOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyAccessControlAllowHeaders:
    boto3_raw_data: (
        "type_defs.ResponseHeadersPolicyAccessControlAllowHeadersTypeDef"
    ) = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyAccessControlAllowHeadersTypeDef"
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
                "type_defs.ResponseHeadersPolicyAccessControlAllowHeadersTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyAccessControlAllowMethodsOutput:
    boto3_raw_data: (
        "type_defs.ResponseHeadersPolicyAccessControlAllowMethodsOutputTypeDef"
    ) = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyAccessControlAllowMethodsOutputTypeDef"
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
                "type_defs.ResponseHeadersPolicyAccessControlAllowMethodsOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyAccessControlAllowMethods:
    boto3_raw_data: (
        "type_defs.ResponseHeadersPolicyAccessControlAllowMethodsTypeDef"
    ) = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyAccessControlAllowMethodsTypeDef"
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
                "type_defs.ResponseHeadersPolicyAccessControlAllowMethodsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyAccessControlAllowOriginsOutput:
    boto3_raw_data: (
        "type_defs.ResponseHeadersPolicyAccessControlAllowOriginsOutputTypeDef"
    ) = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyAccessControlAllowOriginsOutputTypeDef"
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
                "type_defs.ResponseHeadersPolicyAccessControlAllowOriginsOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyAccessControlAllowOrigins:
    boto3_raw_data: (
        "type_defs.ResponseHeadersPolicyAccessControlAllowOriginsTypeDef"
    ) = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyAccessControlAllowOriginsTypeDef"
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
                "type_defs.ResponseHeadersPolicyAccessControlAllowOriginsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyAccessControlExposeHeadersOutput:
    boto3_raw_data: (
        "type_defs.ResponseHeadersPolicyAccessControlExposeHeadersOutputTypeDef"
    ) = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyAccessControlExposeHeadersOutputTypeDef"
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
                "type_defs.ResponseHeadersPolicyAccessControlExposeHeadersOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyAccessControlExposeHeaders:
    boto3_raw_data: (
        "type_defs.ResponseHeadersPolicyAccessControlExposeHeadersTypeDef"
    ) = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyAccessControlExposeHeadersTypeDef"
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
                "type_defs.ResponseHeadersPolicyAccessControlExposeHeadersTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyServerTimingHeadersConfig:
    boto3_raw_data: (
        "type_defs.ResponseHeadersPolicyServerTimingHeadersConfigTypeDef"
    ) = dataclasses.field()

    Enabled = field("Enabled")
    SamplingRate = field("SamplingRate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyServerTimingHeadersConfigTypeDef"
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
                "type_defs.ResponseHeadersPolicyServerTimingHeadersConfigTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyContentSecurityPolicy:
    boto3_raw_data: "type_defs.ResponseHeadersPolicyContentSecurityPolicyTypeDef" = (
        dataclasses.field()
    )

    Override = field("Override")
    ContentSecurityPolicy = field("ContentSecurityPolicy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyContentSecurityPolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseHeadersPolicyContentSecurityPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyContentTypeOptions:
    boto3_raw_data: "type_defs.ResponseHeadersPolicyContentTypeOptionsTypeDef" = (
        dataclasses.field()
    )

    Override = field("Override")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyContentTypeOptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseHeadersPolicyContentTypeOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyCustomHeader:
    boto3_raw_data: "type_defs.ResponseHeadersPolicyCustomHeaderTypeDef" = (
        dataclasses.field()
    )

    Header = field("Header")
    Value = field("Value")
    Override = field("Override")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyCustomHeaderTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseHeadersPolicyCustomHeaderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyFrameOptions:
    boto3_raw_data: "type_defs.ResponseHeadersPolicyFrameOptionsTypeDef" = (
        dataclasses.field()
    )

    Override = field("Override")
    FrameOption = field("FrameOption")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyFrameOptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseHeadersPolicyFrameOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyReferrerPolicy:
    boto3_raw_data: "type_defs.ResponseHeadersPolicyReferrerPolicyTypeDef" = (
        dataclasses.field()
    )

    Override = field("Override")
    ReferrerPolicy = field("ReferrerPolicy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyReferrerPolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseHeadersPolicyReferrerPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyRemoveHeader:
    boto3_raw_data: "type_defs.ResponseHeadersPolicyRemoveHeaderTypeDef" = (
        dataclasses.field()
    )

    Header = field("Header")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyRemoveHeaderTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseHeadersPolicyRemoveHeaderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyStrictTransportSecurity:
    boto3_raw_data: "type_defs.ResponseHeadersPolicyStrictTransportSecurityTypeDef" = (
        dataclasses.field()
    )

    Override = field("Override")
    AccessControlMaxAgeSec = field("AccessControlMaxAgeSec")
    IncludeSubdomains = field("IncludeSubdomains")
    Preload = field("Preload")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyStrictTransportSecurityTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseHeadersPolicyStrictTransportSecurityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyXSSProtection:
    boto3_raw_data: "type_defs.ResponseHeadersPolicyXSSProtectionTypeDef" = (
        dataclasses.field()
    )

    Override = field("Override")
    Protection = field("Protection")
    ModeBlock = field("ModeBlock")
    ReportUri = field("ReportUri")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyXSSProtectionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseHeadersPolicyXSSProtectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Origin:
    boto3_raw_data: "type_defs.S3OriginTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    OriginAccessIdentity = field("OriginAccessIdentity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3OriginTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3OriginTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatusCodes:
    boto3_raw_data: "type_defs.StatusCodesTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatusCodesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatusCodesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamingLoggingConfig:
    boto3_raw_data: "type_defs.StreamingLoggingConfigTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    Bucket = field("Bucket")
    Prefix = field("Prefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamingLoggingConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamingLoggingConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagKeys:
    boto3_raw_data: "type_defs.TagKeysTypeDef" = dataclasses.field()

    Items = field("Items")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagKeysTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagKeysTypeDef"]]
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
class TrustedKeyGroups:
    boto3_raw_data: "type_defs.TrustedKeyGroupsTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrustedKeyGroupsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrustedKeyGroupsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrustedSigners:
    boto3_raw_data: "type_defs.TrustedSignersTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrustedSignersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TrustedSignersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectionGroupRequest:
    boto3_raw_data: "type_defs.UpdateConnectionGroupRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IfMatch = field("IfMatch")
    Ipv6Enabled = field("Ipv6Enabled")
    AnycastIpListId = field("AnycastIpListId")
    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConnectionGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectionGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDistributionWithStagingConfigRequest:
    boto3_raw_data: "type_defs.UpdateDistributionWithStagingConfigRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    StagingDistributionId = field("StagingDistributionId")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDistributionWithStagingConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDistributionWithStagingConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKeyValueStoreRequest:
    boto3_raw_data: "type_defs.UpdateKeyValueStoreRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Comment = field("Comment")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateKeyValueStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKeyValueStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyDnsConfigurationRequest:
    boto3_raw_data: "type_defs.VerifyDnsConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")
    Domain = field("Domain")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VerifyDnsConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyDnsConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcOriginSummary:
    boto3_raw_data: "type_defs.VpcOriginSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Status = field("Status")
    CreatedTime = field("CreatedTime")
    LastModifiedTime = field("LastModifiedTime")
    Arn = field("Arn")
    OriginEndpointArn = field("OriginEndpointArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcOriginSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcOriginSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllowedMethodsOutput:
    boto3_raw_data: "type_defs.AllowedMethodsOutputTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @cached_property
    def CachedMethods(self):  # pragma: no cover
        return CachedMethodsOutput.make_one(self.boto3_raw_data["CachedMethods"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AllowedMethodsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AllowedMethodsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnycastIpListCollection:
    boto3_raw_data: "type_defs.AnycastIpListCollectionTypeDef" = dataclasses.field()

    Marker = field("Marker")
    MaxItems = field("MaxItems")
    IsTruncated = field("IsTruncated")
    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return AnycastIpListSummary.make_many(self.boto3_raw_data["Items"])

    NextMarker = field("NextMarker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnycastIpListCollectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnycastIpListCollectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateDistributionTenantWebACLResult:
    boto3_raw_data: "type_defs.AssociateDistributionTenantWebACLResultTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    WebACLArn = field("WebACLArn")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateDistributionTenantWebACLResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateDistributionTenantWebACLResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateDistributionWebACLResult:
    boto3_raw_data: "type_defs.AssociateDistributionWebACLResultTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    WebACLArn = field("WebACLArn")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateDistributionWebACLResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateDistributionWebACLResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAnycastIpListResult:
    boto3_raw_data: "type_defs.CreateAnycastIpListResultTypeDef" = dataclasses.field()

    @cached_property
    def AnycastIpList(self):  # pragma: no cover
        return AnycastIpList.make_one(self.boto3_raw_data["AnycastIpList"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAnycastIpListResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAnycastIpListResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateDistributionTenantWebACLResult:
    boto3_raw_data: "type_defs.DisassociateDistributionTenantWebACLResultTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateDistributionTenantWebACLResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateDistributionTenantWebACLResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateDistributionWebACLResult:
    boto3_raw_data: "type_defs.DisassociateDistributionWebACLResultTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateDistributionWebACLResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateDistributionWebACLResultTypeDef"]
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
class GetAnycastIpListResult:
    boto3_raw_data: "type_defs.GetAnycastIpListResultTypeDef" = dataclasses.field()

    @cached_property
    def AnycastIpList(self):  # pragma: no cover
        return AnycastIpList.make_one(self.boto3_raw_data["AnycastIpList"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAnycastIpListResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnycastIpListResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFunctionResult:
    boto3_raw_data: "type_defs.GetFunctionResultTypeDef" = dataclasses.field()

    FunctionCode = field("FunctionCode")
    ETag = field("ETag")
    ContentType = field("ContentType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFunctionResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainAssociationResult:
    boto3_raw_data: "type_defs.UpdateDomainAssociationResultTypeDef" = (
        dataclasses.field()
    )

    Domain = field("Domain")
    ResourceId = field("ResourceId")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDomainAssociationResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainAssociationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestFunctionRequest:
    boto3_raw_data: "type_defs.TestFunctionRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    IfMatch = field("IfMatch")
    EventObject = field("EventObject")
    Stage = field("Stage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestFunctionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestFunctionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CachePolicyCookiesConfigOutput:
    boto3_raw_data: "type_defs.CachePolicyCookiesConfigOutputTypeDef" = (
        dataclasses.field()
    )

    CookieBehavior = field("CookieBehavior")

    @cached_property
    def Cookies(self):  # pragma: no cover
        return CookieNamesOutput.make_one(self.boto3_raw_data["Cookies"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CachePolicyCookiesConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CachePolicyCookiesConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CookiePreferenceOutput:
    boto3_raw_data: "type_defs.CookiePreferenceOutputTypeDef" = dataclasses.field()

    Forward = field("Forward")

    @cached_property
    def WhitelistedNames(self):  # pragma: no cover
        return CookieNamesOutput.make_one(self.boto3_raw_data["WhitelistedNames"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CookiePreferenceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CookiePreferenceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginRequestPolicyCookiesConfigOutput:
    boto3_raw_data: "type_defs.OriginRequestPolicyCookiesConfigOutputTypeDef" = (
        dataclasses.field()
    )

    CookieBehavior = field("CookieBehavior")

    @cached_property
    def Cookies(self):  # pragma: no cover
        return CookieNamesOutput.make_one(self.boto3_raw_data["Cookies"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OriginRequestPolicyCookiesConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginRequestPolicyCookiesConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CachePolicyCookiesConfig:
    boto3_raw_data: "type_defs.CachePolicyCookiesConfigTypeDef" = dataclasses.field()

    CookieBehavior = field("CookieBehavior")

    @cached_property
    def Cookies(self):  # pragma: no cover
        return CookieNames.make_one(self.boto3_raw_data["Cookies"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CachePolicyCookiesConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CachePolicyCookiesConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginRequestPolicyCookiesConfig:
    boto3_raw_data: "type_defs.OriginRequestPolicyCookiesConfigTypeDef" = (
        dataclasses.field()
    )

    CookieBehavior = field("CookieBehavior")

    @cached_property
    def Cookies(self):  # pragma: no cover
        return CookieNames.make_one(self.boto3_raw_data["Cookies"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OriginRequestPolicyCookiesConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginRequestPolicyCookiesConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CachePolicyHeadersConfigOutput:
    boto3_raw_data: "type_defs.CachePolicyHeadersConfigOutputTypeDef" = (
        dataclasses.field()
    )

    HeaderBehavior = field("HeaderBehavior")

    @cached_property
    def Headers(self):  # pragma: no cover
        return HeadersOutput.make_one(self.boto3_raw_data["Headers"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CachePolicyHeadersConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CachePolicyHeadersConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginRequestPolicyHeadersConfigOutput:
    boto3_raw_data: "type_defs.OriginRequestPolicyHeadersConfigOutputTypeDef" = (
        dataclasses.field()
    )

    HeaderBehavior = field("HeaderBehavior")

    @cached_property
    def Headers(self):  # pragma: no cover
        return HeadersOutput.make_one(self.boto3_raw_data["Headers"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OriginRequestPolicyHeadersConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginRequestPolicyHeadersConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CachePolicyHeadersConfig:
    boto3_raw_data: "type_defs.CachePolicyHeadersConfigTypeDef" = dataclasses.field()

    HeaderBehavior = field("HeaderBehavior")

    @cached_property
    def Headers(self):  # pragma: no cover
        return Headers.make_one(self.boto3_raw_data["Headers"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CachePolicyHeadersConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CachePolicyHeadersConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginRequestPolicyHeadersConfig:
    boto3_raw_data: "type_defs.OriginRequestPolicyHeadersConfigTypeDef" = (
        dataclasses.field()
    )

    HeaderBehavior = field("HeaderBehavior")

    @cached_property
    def Headers(self):  # pragma: no cover
        return Headers.make_one(self.boto3_raw_data["Headers"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OriginRequestPolicyHeadersConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginRequestPolicyHeadersConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CachePolicyQueryStringsConfigOutput:
    boto3_raw_data: "type_defs.CachePolicyQueryStringsConfigOutputTypeDef" = (
        dataclasses.field()
    )

    QueryStringBehavior = field("QueryStringBehavior")

    @cached_property
    def QueryStrings(self):  # pragma: no cover
        return QueryStringNamesOutput.make_one(self.boto3_raw_data["QueryStrings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CachePolicyQueryStringsConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CachePolicyQueryStringsConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginRequestPolicyQueryStringsConfigOutput:
    boto3_raw_data: "type_defs.OriginRequestPolicyQueryStringsConfigOutputTypeDef" = (
        dataclasses.field()
    )

    QueryStringBehavior = field("QueryStringBehavior")

    @cached_property
    def QueryStrings(self):  # pragma: no cover
        return QueryStringNamesOutput.make_one(self.boto3_raw_data["QueryStrings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OriginRequestPolicyQueryStringsConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginRequestPolicyQueryStringsConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CachePolicyQueryStringsConfig:
    boto3_raw_data: "type_defs.CachePolicyQueryStringsConfigTypeDef" = (
        dataclasses.field()
    )

    QueryStringBehavior = field("QueryStringBehavior")

    @cached_property
    def QueryStrings(self):  # pragma: no cover
        return QueryStringNames.make_one(self.boto3_raw_data["QueryStrings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CachePolicyQueryStringsConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CachePolicyQueryStringsConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginRequestPolicyQueryStringsConfig:
    boto3_raw_data: "type_defs.OriginRequestPolicyQueryStringsConfigTypeDef" = (
        dataclasses.field()
    )

    QueryStringBehavior = field("QueryStringBehavior")

    @cached_property
    def QueryStrings(self):  # pragma: no cover
        return QueryStringNames.make_one(self.boto3_raw_data["QueryStrings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OriginRequestPolicyQueryStringsConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginRequestPolicyQueryStringsConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudFrontOriginAccessIdentity:
    boto3_raw_data: "type_defs.CloudFrontOriginAccessIdentityTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    S3CanonicalUserId = field("S3CanonicalUserId")

    @cached_property
    def CloudFrontOriginAccessIdentityConfig(self):  # pragma: no cover
        return CloudFrontOriginAccessIdentityConfig.make_one(
            self.boto3_raw_data["CloudFrontOriginAccessIdentityConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CloudFrontOriginAccessIdentityTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudFrontOriginAccessIdentityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCloudFrontOriginAccessIdentityRequest:
    boto3_raw_data: "type_defs.CreateCloudFrontOriginAccessIdentityRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CloudFrontOriginAccessIdentityConfig(self):  # pragma: no cover
        return CloudFrontOriginAccessIdentityConfig.make_one(
            self.boto3_raw_data["CloudFrontOriginAccessIdentityConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCloudFrontOriginAccessIdentityRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCloudFrontOriginAccessIdentityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCloudFrontOriginAccessIdentityConfigResult:
    boto3_raw_data: "type_defs.GetCloudFrontOriginAccessIdentityConfigResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CloudFrontOriginAccessIdentityConfig(self):  # pragma: no cover
        return CloudFrontOriginAccessIdentityConfig.make_one(
            self.boto3_raw_data["CloudFrontOriginAccessIdentityConfig"]
        )

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCloudFrontOriginAccessIdentityConfigResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCloudFrontOriginAccessIdentityConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCloudFrontOriginAccessIdentityRequest:
    boto3_raw_data: "type_defs.UpdateCloudFrontOriginAccessIdentityRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CloudFrontOriginAccessIdentityConfig(self):  # pragma: no cover
        return CloudFrontOriginAccessIdentityConfig.make_one(
            self.boto3_raw_data["CloudFrontOriginAccessIdentityConfig"]
        )

    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCloudFrontOriginAccessIdentityRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCloudFrontOriginAccessIdentityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudFrontOriginAccessIdentityList:
    boto3_raw_data: "type_defs.CloudFrontOriginAccessIdentityListTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")
    MaxItems = field("MaxItems")
    IsTruncated = field("IsTruncated")
    Quantity = field("Quantity")
    NextMarker = field("NextMarker")

    @cached_property
    def Items(self):  # pragma: no cover
        return CloudFrontOriginAccessIdentitySummary.make_many(
            self.boto3_raw_data["Items"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CloudFrontOriginAccessIdentityListTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudFrontOriginAccessIdentityListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConflictingAliasesList:
    boto3_raw_data: "type_defs.ConflictingAliasesListTypeDef" = dataclasses.field()

    NextMarker = field("NextMarker")
    MaxItems = field("MaxItems")
    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return ConflictingAlias.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConflictingAliasesListTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConflictingAliasesListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectionGroupsRequest:
    boto3_raw_data: "type_defs.ListConnectionGroupsRequestTypeDef" = dataclasses.field()

    @cached_property
    def AssociationFilter(self):  # pragma: no cover
        return ConnectionGroupAssociationFilter.make_one(
            self.boto3_raw_data["AssociationFilter"]
        )

    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConnectionGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectionGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectionGroupsResult:
    boto3_raw_data: "type_defs.ListConnectionGroupsResultTypeDef" = dataclasses.field()

    NextMarker = field("NextMarker")

    @cached_property
    def ConnectionGroups(self):  # pragma: no cover
        return ConnectionGroupSummary.make_many(self.boto3_raw_data["ConnectionGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConnectionGroupsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectionGroupsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentTypeProfilesOutput:
    boto3_raw_data: "type_defs.ContentTypeProfilesOutputTypeDef" = dataclasses.field()

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return ContentTypeProfile.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContentTypeProfilesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentTypeProfilesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentTypeProfiles:
    boto3_raw_data: "type_defs.ContentTypeProfilesTypeDef" = dataclasses.field()

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return ContentTypeProfile.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContentTypeProfilesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentTypeProfilesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContinuousDeploymentSingleWeightConfig:
    boto3_raw_data: "type_defs.ContinuousDeploymentSingleWeightConfigTypeDef" = (
        dataclasses.field()
    )

    Weight = field("Weight")

    @cached_property
    def SessionStickinessConfig(self):  # pragma: no cover
        return SessionStickinessConfig.make_one(
            self.boto3_raw_data["SessionStickinessConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ContinuousDeploymentSingleWeightConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContinuousDeploymentSingleWeightConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKeyValueStoreRequest:
    boto3_raw_data: "type_defs.CreateKeyValueStoreRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Comment = field("Comment")

    @cached_property
    def ImportSource(self):  # pragma: no cover
        return ImportSource.make_one(self.boto3_raw_data["ImportSource"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKeyValueStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKeyValueStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKeyValueStoreResult:
    boto3_raw_data: "type_defs.CreateKeyValueStoreResultTypeDef" = dataclasses.field()

    @cached_property
    def KeyValueStore(self):  # pragma: no cover
        return KeyValueStore.make_one(self.boto3_raw_data["KeyValueStore"])

    ETag = field("ETag")
    Location = field("Location")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKeyValueStoreResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKeyValueStoreResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeKeyValueStoreResult:
    boto3_raw_data: "type_defs.DescribeKeyValueStoreResultTypeDef" = dataclasses.field()

    @cached_property
    def KeyValueStore(self):  # pragma: no cover
        return KeyValueStore.make_one(self.boto3_raw_data["KeyValueStore"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeKeyValueStoreResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeKeyValueStoreResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyValueStoreList:
    boto3_raw_data: "type_defs.KeyValueStoreListTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    Quantity = field("Quantity")
    NextMarker = field("NextMarker")

    @cached_property
    def Items(self):  # pragma: no cover
        return KeyValueStore.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyValueStoreListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeyValueStoreListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKeyValueStoreResult:
    boto3_raw_data: "type_defs.UpdateKeyValueStoreResultTypeDef" = dataclasses.field()

    @cached_property
    def KeyValueStore(self):  # pragma: no cover
        return KeyValueStore.make_one(self.boto3_raw_data["KeyValueStore"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateKeyValueStoreResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKeyValueStoreResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOriginAccessControlRequest:
    boto3_raw_data: "type_defs.CreateOriginAccessControlRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OriginAccessControlConfig(self):  # pragma: no cover
        return OriginAccessControlConfig.make_one(
            self.boto3_raw_data["OriginAccessControlConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateOriginAccessControlRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOriginAccessControlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOriginAccessControlConfigResult:
    boto3_raw_data: "type_defs.GetOriginAccessControlConfigResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OriginAccessControlConfig(self):  # pragma: no cover
        return OriginAccessControlConfig.make_one(
            self.boto3_raw_data["OriginAccessControlConfig"]
        )

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOriginAccessControlConfigResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOriginAccessControlConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginAccessControl:
    boto3_raw_data: "type_defs.OriginAccessControlTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def OriginAccessControlConfig(self):  # pragma: no cover
        return OriginAccessControlConfig.make_one(
            self.boto3_raw_data["OriginAccessControlConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OriginAccessControlTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginAccessControlTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOriginAccessControlRequest:
    boto3_raw_data: "type_defs.UpdateOriginAccessControlRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OriginAccessControlConfig(self):  # pragma: no cover
        return OriginAccessControlConfig.make_one(
            self.boto3_raw_data["OriginAccessControlConfig"]
        )

    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateOriginAccessControlRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOriginAccessControlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePublicKeyRequest:
    boto3_raw_data: "type_defs.CreatePublicKeyRequestTypeDef" = dataclasses.field()

    @cached_property
    def PublicKeyConfig(self):  # pragma: no cover
        return PublicKeyConfig.make_one(self.boto3_raw_data["PublicKeyConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePublicKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePublicKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPublicKeyConfigResult:
    boto3_raw_data: "type_defs.GetPublicKeyConfigResultTypeDef" = dataclasses.field()

    @cached_property
    def PublicKeyConfig(self):  # pragma: no cover
        return PublicKeyConfig.make_one(self.boto3_raw_data["PublicKeyConfig"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPublicKeyConfigResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPublicKeyConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublicKey:
    boto3_raw_data: "type_defs.PublicKeyTypeDef" = dataclasses.field()

    Id = field("Id")
    CreatedTime = field("CreatedTime")

    @cached_property
    def PublicKeyConfig(self):  # pragma: no cover
        return PublicKeyConfig.make_one(self.boto3_raw_data["PublicKeyConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PublicKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PublicKeyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePublicKeyRequest:
    boto3_raw_data: "type_defs.UpdatePublicKeyRequestTypeDef" = dataclasses.field()

    @cached_property
    def PublicKeyConfig(self):  # pragma: no cover
        return PublicKeyConfig.make_one(self.boto3_raw_data["PublicKeyConfig"])

    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePublicKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePublicKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomErrorResponsesOutput:
    boto3_raw_data: "type_defs.CustomErrorResponsesOutputTypeDef" = dataclasses.field()

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return CustomErrorResponse.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomErrorResponsesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomErrorResponsesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomErrorResponses:
    boto3_raw_data: "type_defs.CustomErrorResponsesTypeDef" = dataclasses.field()

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return CustomErrorResponse.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomErrorResponsesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomErrorResponsesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomHeadersOutput:
    boto3_raw_data: "type_defs.CustomHeadersOutputTypeDef" = dataclasses.field()

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return OriginCustomHeader.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomHeadersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomHeadersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomHeaders:
    boto3_raw_data: "type_defs.CustomHeadersTypeDef" = dataclasses.field()

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return OriginCustomHeader.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomHeadersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomHeadersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomOriginConfigOutput:
    boto3_raw_data: "type_defs.CustomOriginConfigOutputTypeDef" = dataclasses.field()

    HTTPPort = field("HTTPPort")
    HTTPSPort = field("HTTPSPort")
    OriginProtocolPolicy = field("OriginProtocolPolicy")

    @cached_property
    def OriginSslProtocols(self):  # pragma: no cover
        return OriginSslProtocolsOutput.make_one(
            self.boto3_raw_data["OriginSslProtocols"]
        )

    OriginReadTimeout = field("OriginReadTimeout")
    OriginKeepaliveTimeout = field("OriginKeepaliveTimeout")
    IpAddressType = field("IpAddressType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomOriginConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomOriginConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcOriginEndpointConfigOutput:
    boto3_raw_data: "type_defs.VpcOriginEndpointConfigOutputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Arn = field("Arn")
    HTTPPort = field("HTTPPort")
    HTTPSPort = field("HTTPSPort")
    OriginProtocolPolicy = field("OriginProtocolPolicy")

    @cached_property
    def OriginSslProtocols(self):  # pragma: no cover
        return OriginSslProtocolsOutput.make_one(
            self.boto3_raw_data["OriginSslProtocols"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VpcOriginEndpointConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcOriginEndpointConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomizationsOutput:
    boto3_raw_data: "type_defs.CustomizationsOutputTypeDef" = dataclasses.field()

    @cached_property
    def WebAcl(self):  # pragma: no cover
        return WebAclCustomization.make_one(self.boto3_raw_data["WebAcl"])

    @cached_property
    def Certificate(self):  # pragma: no cover
        return Certificate.make_one(self.boto3_raw_data["Certificate"])

    @cached_property
    def GeoRestrictions(self):  # pragma: no cover
        return GeoRestrictionCustomizationOutput.make_one(
            self.boto3_raw_data["GeoRestrictions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomizationsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomizationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Customizations:
    boto3_raw_data: "type_defs.CustomizationsTypeDef" = dataclasses.field()

    @cached_property
    def WebAcl(self):  # pragma: no cover
        return WebAclCustomization.make_one(self.boto3_raw_data["WebAcl"])

    @cached_property
    def Certificate(self):  # pragma: no cover
        return Certificate.make_one(self.boto3_raw_data["Certificate"])

    @cached_property
    def GeoRestrictions(self):  # pragma: no cover
        return GeoRestrictionCustomization.make_one(
            self.boto3_raw_data["GeoRestrictions"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomizationsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomizationsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionsByCachePolicyIdResult:
    boto3_raw_data: "type_defs.ListDistributionsByCachePolicyIdResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DistributionIdList(self):  # pragma: no cover
        return DistributionIdList.make_one(self.boto3_raw_data["DistributionIdList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionsByCachePolicyIdResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionsByCachePolicyIdResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionsByKeyGroupResult:
    boto3_raw_data: "type_defs.ListDistributionsByKeyGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DistributionIdList(self):  # pragma: no cover
        return DistributionIdList.make_one(self.boto3_raw_data["DistributionIdList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionsByKeyGroupResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionsByKeyGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionsByOriginRequestPolicyIdResult:
    boto3_raw_data: (
        "type_defs.ListDistributionsByOriginRequestPolicyIdResultTypeDef"
    ) = dataclasses.field()

    @cached_property
    def DistributionIdList(self):  # pragma: no cover
        return DistributionIdList.make_one(self.boto3_raw_data["DistributionIdList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionsByOriginRequestPolicyIdResultTypeDef"
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
                "type_defs.ListDistributionsByOriginRequestPolicyIdResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionsByResponseHeadersPolicyIdResult:
    boto3_raw_data: (
        "type_defs.ListDistributionsByResponseHeadersPolicyIdResultTypeDef"
    ) = dataclasses.field()

    @cached_property
    def DistributionIdList(self):  # pragma: no cover
        return DistributionIdList.make_one(self.boto3_raw_data["DistributionIdList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionsByResponseHeadersPolicyIdResultTypeDef"
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
                "type_defs.ListDistributionsByResponseHeadersPolicyIdResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionsByVpcOriginIdResult:
    boto3_raw_data: "type_defs.ListDistributionsByVpcOriginIdResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DistributionIdList(self):  # pragma: no cover
        return DistributionIdList.make_one(self.boto3_raw_data["DistributionIdList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionsByVpcOriginIdResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionsByVpcOriginIdResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainConflictsRequest:
    boto3_raw_data: "type_defs.ListDomainConflictsRequestTypeDef" = dataclasses.field()

    Domain = field("Domain")

    @cached_property
    def DomainControlValidationResource(self):  # pragma: no cover
        return DistributionResourceId.make_one(
            self.boto3_raw_data["DomainControlValidationResource"]
        )

    MaxItems = field("MaxItems")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainConflictsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainConflictsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainAssociationRequest:
    boto3_raw_data: "type_defs.UpdateDomainAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    Domain = field("Domain")

    @cached_property
    def TargetResource(self):  # pragma: no cover
        return DistributionResourceId.make_one(self.boto3_raw_data["TargetResource"])

    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDomainAssociationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionTenantsRequest:
    boto3_raw_data: "type_defs.ListDistributionTenantsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AssociationFilter(self):  # pragma: no cover
        return DistributionTenantAssociationFilter.make_one(
            self.boto3_raw_data["AssociationFilter"]
        )

    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDistributionTenantsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionTenantsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyDnsConfigurationResult:
    boto3_raw_data: "type_defs.VerifyDnsConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DnsConfigurationList(self):  # pragma: no cover
        return DnsConfiguration.make_many(self.boto3_raw_data["DnsConfigurationList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VerifyDnsConfigurationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyDnsConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainConflictsResult:
    boto3_raw_data: "type_defs.ListDomainConflictsResultTypeDef" = dataclasses.field()

    @cached_property
    def DomainConflicts(self):  # pragma: no cover
        return DomainConflict.make_many(self.boto3_raw_data["DomainConflicts"])

    NextMarker = field("NextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainConflictsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainConflictsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionEntityOutput:
    boto3_raw_data: "type_defs.EncryptionEntityOutputTypeDef" = dataclasses.field()

    PublicKeyId = field("PublicKeyId")
    ProviderId = field("ProviderId")

    @cached_property
    def FieldPatterns(self):  # pragma: no cover
        return FieldPatternsOutput.make_one(self.boto3_raw_data["FieldPatterns"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncryptionEntityOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionEntityOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionEntity:
    boto3_raw_data: "type_defs.EncryptionEntityTypeDef" = dataclasses.field()

    PublicKeyId = field("PublicKeyId")
    ProviderId = field("ProviderId")

    @cached_property
    def FieldPatterns(self):  # pragma: no cover
        return FieldPatterns.make_one(self.boto3_raw_data["FieldPatterns"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptionEntityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionEntityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndPoint:
    boto3_raw_data: "type_defs.EndPointTypeDef" = dataclasses.field()

    StreamType = field("StreamType")

    @cached_property
    def KinesisStreamConfig(self):  # pragma: no cover
        return KinesisStreamConfig.make_one(self.boto3_raw_data["KinesisStreamConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndPointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EndPointTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionAssociationsOutput:
    boto3_raw_data: "type_defs.FunctionAssociationsOutputTypeDef" = dataclasses.field()

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return FunctionAssociation.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FunctionAssociationsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionAssociationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionAssociations:
    boto3_raw_data: "type_defs.FunctionAssociationsTypeDef" = dataclasses.field()

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return FunctionAssociation.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FunctionAssociationsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionAssociationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestrictionsOutput:
    boto3_raw_data: "type_defs.RestrictionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def GeoRestriction(self):  # pragma: no cover
        return GeoRestrictionOutput.make_one(self.boto3_raw_data["GeoRestriction"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestrictionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestrictionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDistributionRequestWait:
    boto3_raw_data: "type_defs.GetDistributionRequestWaitTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDistributionRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDistributionRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInvalidationForDistributionTenantRequestWait:
    boto3_raw_data: (
        "type_defs.GetInvalidationForDistributionTenantRequestWaitTypeDef"
    ) = dataclasses.field()

    DistributionTenantId = field("DistributionTenantId")
    Id = field("Id")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetInvalidationForDistributionTenantRequestWaitTypeDef"
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
                "type_defs.GetInvalidationForDistributionTenantRequestWaitTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInvalidationRequestWait:
    boto3_raw_data: "type_defs.GetInvalidationRequestWaitTypeDef" = dataclasses.field()

    DistributionId = field("DistributionId")
    Id = field("Id")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInvalidationRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInvalidationRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStreamingDistributionRequestWait:
    boto3_raw_data: "type_defs.GetStreamingDistributionRequestWaitTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetStreamingDistributionRequestWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStreamingDistributionRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKeyGroupConfigResult:
    boto3_raw_data: "type_defs.GetKeyGroupConfigResultTypeDef" = dataclasses.field()

    @cached_property
    def KeyGroupConfig(self):  # pragma: no cover
        return KeyGroupConfigOutput.make_one(self.boto3_raw_data["KeyGroupConfig"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKeyGroupConfigResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKeyGroupConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyGroup:
    boto3_raw_data: "type_defs.KeyGroupTypeDef" = dataclasses.field()

    Id = field("Id")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def KeyGroupConfig(self):  # pragma: no cover
        return KeyGroupConfigOutput.make_one(self.boto3_raw_data["KeyGroupConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyGroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvalidationBatchOutput:
    boto3_raw_data: "type_defs.InvalidationBatchOutputTypeDef" = dataclasses.field()

    @cached_property
    def Paths(self):  # pragma: no cover
        return PathsOutput.make_one(self.boto3_raw_data["Paths"])

    CallerReference = field("CallerReference")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvalidationBatchOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvalidationBatchOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvalidationBatch:
    boto3_raw_data: "type_defs.InvalidationBatchTypeDef" = dataclasses.field()

    @cached_property
    def Paths(self):  # pragma: no cover
        return Paths.make_one(self.boto3_raw_data["Paths"])

    CallerReference = field("CallerReference")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InvalidationBatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvalidationBatchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvalidationList:
    boto3_raw_data: "type_defs.InvalidationListTypeDef" = dataclasses.field()

    Marker = field("Marker")
    MaxItems = field("MaxItems")
    IsTruncated = field("IsTruncated")
    Quantity = field("Quantity")
    NextMarker = field("NextMarker")

    @cached_property
    def Items(self):  # pragma: no cover
        return InvalidationSummary.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InvalidationListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvalidationListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KGKeyPairIds:
    boto3_raw_data: "type_defs.KGKeyPairIdsTypeDef" = dataclasses.field()

    KeyGroupId = field("KeyGroupId")

    @cached_property
    def KeyPairIds(self):  # pragma: no cover
        return KeyPairIds.make_one(self.boto3_raw_data["KeyPairIds"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KGKeyPairIdsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KGKeyPairIdsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Signer:
    boto3_raw_data: "type_defs.SignerTypeDef" = dataclasses.field()

    AwsAccountNumber = field("AwsAccountNumber")

    @cached_property
    def KeyPairIds(self):  # pragma: no cover
        return KeyPairIds.make_one(self.boto3_raw_data["KeyPairIds"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SignerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SignerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyValueStoreAssociationsOutput:
    boto3_raw_data: "type_defs.KeyValueStoreAssociationsOutputTypeDef" = (
        dataclasses.field()
    )

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return KeyValueStoreAssociation.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KeyValueStoreAssociationsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeyValueStoreAssociationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyValueStoreAssociations:
    boto3_raw_data: "type_defs.KeyValueStoreAssociationsTypeDef" = dataclasses.field()

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return KeyValueStoreAssociation.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KeyValueStoreAssociationsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeyValueStoreAssociationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionAssociationsOutput:
    boto3_raw_data: "type_defs.LambdaFunctionAssociationsOutputTypeDef" = (
        dataclasses.field()
    )

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return LambdaFunctionAssociation.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LambdaFunctionAssociationsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionAssociationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionAssociations:
    boto3_raw_data: "type_defs.LambdaFunctionAssociationsTypeDef" = dataclasses.field()

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return LambdaFunctionAssociation.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaFunctionAssociationsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionAssociationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCloudFrontOriginAccessIdentitiesRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListCloudFrontOriginAccessIdentitiesRequestPaginateTypeDef"
    ) = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCloudFrontOriginAccessIdentitiesRequestPaginateTypeDef"
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
                "type_defs.ListCloudFrontOriginAccessIdentitiesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectionGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListConnectionGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AssociationFilter(self):  # pragma: no cover
        return ConnectionGroupAssociationFilter.make_one(
            self.boto3_raw_data["AssociationFilter"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConnectionGroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectionGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionTenantsByCustomizationRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListDistributionTenantsByCustomizationRequestPaginateTypeDef"
    ) = dataclasses.field()

    WebACLArn = field("WebACLArn")
    CertificateArn = field("CertificateArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionTenantsByCustomizationRequestPaginateTypeDef"
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
                "type_defs.ListDistributionTenantsByCustomizationRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionTenantsRequestPaginate:
    boto3_raw_data: "type_defs.ListDistributionTenantsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AssociationFilter(self):  # pragma: no cover
        return DistributionTenantAssociationFilter.make_one(
            self.boto3_raw_data["AssociationFilter"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionTenantsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionTenantsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionsByConnectionModeRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListDistributionsByConnectionModeRequestPaginateTypeDef"
    ) = dataclasses.field()

    ConnectionMode = field("ConnectionMode")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionsByConnectionModeRequestPaginateTypeDef"
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
                "type_defs.ListDistributionsByConnectionModeRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionsRequestPaginate:
    boto3_raw_data: "type_defs.ListDistributionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDistributionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainConflictsRequestPaginate:
    boto3_raw_data: "type_defs.ListDomainConflictsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Domain = field("Domain")

    @cached_property
    def DomainControlValidationResource(self):  # pragma: no cover
        return DistributionResourceId.make_one(
            self.boto3_raw_data["DomainControlValidationResource"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDomainConflictsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainConflictsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvalidationsForDistributionTenantRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListInvalidationsForDistributionTenantRequestPaginateTypeDef"
    ) = dataclasses.field()

    Id = field("Id")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInvalidationsForDistributionTenantRequestPaginateTypeDef"
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
                "type_defs.ListInvalidationsForDistributionTenantRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvalidationsRequestPaginate:
    boto3_raw_data: "type_defs.ListInvalidationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DistributionId = field("DistributionId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInvalidationsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvalidationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeyValueStoresRequestPaginate:
    boto3_raw_data: "type_defs.ListKeyValueStoresRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListKeyValueStoresRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeyValueStoresRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOriginAccessControlsRequestPaginate:
    boto3_raw_data: "type_defs.ListOriginAccessControlsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOriginAccessControlsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOriginAccessControlsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPublicKeysRequestPaginate:
    boto3_raw_data: "type_defs.ListPublicKeysRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPublicKeysRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPublicKeysRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamingDistributionsRequestPaginate:
    boto3_raw_data: "type_defs.ListStreamingDistributionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStreamingDistributionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamingDistributionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedCertificateDetails:
    boto3_raw_data: "type_defs.ManagedCertificateDetailsTypeDef" = dataclasses.field()

    CertificateArn = field("CertificateArn")
    CertificateStatus = field("CertificateStatus")
    ValidationTokenHost = field("ValidationTokenHost")

    @cached_property
    def ValidationTokenDetails(self):  # pragma: no cover
        return ValidationTokenDetail.make_many(
            self.boto3_raw_data["ValidationTokenDetails"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedCertificateDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedCertificateDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitoringSubscription:
    boto3_raw_data: "type_defs.MonitoringSubscriptionTypeDef" = dataclasses.field()

    @cached_property
    def RealtimeMetricsSubscriptionConfig(self):  # pragma: no cover
        return RealtimeMetricsSubscriptionConfig.make_one(
            self.boto3_raw_data["RealtimeMetricsSubscriptionConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MonitoringSubscriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MonitoringSubscriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginAccessControlList:
    boto3_raw_data: "type_defs.OriginAccessControlListTypeDef" = dataclasses.field()

    Marker = field("Marker")
    MaxItems = field("MaxItems")
    IsTruncated = field("IsTruncated")
    Quantity = field("Quantity")
    NextMarker = field("NextMarker")

    @cached_property
    def Items(self):  # pragma: no cover
        return OriginAccessControlSummary.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OriginAccessControlListTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginAccessControlListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginGroupFailoverCriteriaOutput:
    boto3_raw_data: "type_defs.OriginGroupFailoverCriteriaOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StatusCodes(self):  # pragma: no cover
        return StatusCodesOutput.make_one(self.boto3_raw_data["StatusCodes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OriginGroupFailoverCriteriaOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginGroupFailoverCriteriaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginGroupMembersOutput:
    boto3_raw_data: "type_defs.OriginGroupMembersOutputTypeDef" = dataclasses.field()

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return OriginGroupMember.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OriginGroupMembersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginGroupMembersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginGroupMembers:
    boto3_raw_data: "type_defs.OriginGroupMembersTypeDef" = dataclasses.field()

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return OriginGroupMember.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OriginGroupMembersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginGroupMembersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcOriginEndpointConfig:
    boto3_raw_data: "type_defs.VpcOriginEndpointConfigTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")
    HTTPPort = field("HTTPPort")
    HTTPSPort = field("HTTPSPort")
    OriginProtocolPolicy = field("OriginProtocolPolicy")

    @cached_property
    def OriginSslProtocols(self):  # pragma: no cover
        return OriginSslProtocols.make_one(self.boto3_raw_data["OriginSslProtocols"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcOriginEndpointConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcOriginEndpointConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterDefinitionSchema:
    boto3_raw_data: "type_defs.ParameterDefinitionSchemaTypeDef" = dataclasses.field()

    @cached_property
    def StringSchema(self):  # pragma: no cover
        return StringSchemaConfig.make_one(self.boto3_raw_data["StringSchema"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParameterDefinitionSchemaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParameterDefinitionSchemaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublicKeyList:
    boto3_raw_data: "type_defs.PublicKeyListTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    Quantity = field("Quantity")
    NextMarker = field("NextMarker")

    @cached_property
    def Items(self):  # pragma: no cover
        return PublicKeySummary.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PublicKeyListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PublicKeyListTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryArgProfilesOutput:
    boto3_raw_data: "type_defs.QueryArgProfilesOutputTypeDef" = dataclasses.field()

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return QueryArgProfile.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryArgProfilesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryArgProfilesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryArgProfiles:
    boto3_raw_data: "type_defs.QueryArgProfilesTypeDef" = dataclasses.field()

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return QueryArgProfile.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryArgProfilesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryArgProfilesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyCorsConfigOutput:
    boto3_raw_data: "type_defs.ResponseHeadersPolicyCorsConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccessControlAllowOrigins(self):  # pragma: no cover
        return ResponseHeadersPolicyAccessControlAllowOriginsOutput.make_one(
            self.boto3_raw_data["AccessControlAllowOrigins"]
        )

    @cached_property
    def AccessControlAllowHeaders(self):  # pragma: no cover
        return ResponseHeadersPolicyAccessControlAllowHeadersOutput.make_one(
            self.boto3_raw_data["AccessControlAllowHeaders"]
        )

    @cached_property
    def AccessControlAllowMethods(self):  # pragma: no cover
        return ResponseHeadersPolicyAccessControlAllowMethodsOutput.make_one(
            self.boto3_raw_data["AccessControlAllowMethods"]
        )

    AccessControlAllowCredentials = field("AccessControlAllowCredentials")
    OriginOverride = field("OriginOverride")

    @cached_property
    def AccessControlExposeHeaders(self):  # pragma: no cover
        return ResponseHeadersPolicyAccessControlExposeHeadersOutput.make_one(
            self.boto3_raw_data["AccessControlExposeHeaders"]
        )

    AccessControlMaxAgeSec = field("AccessControlMaxAgeSec")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyCorsConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseHeadersPolicyCorsConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyCorsConfig:
    boto3_raw_data: "type_defs.ResponseHeadersPolicyCorsConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccessControlAllowOrigins(self):  # pragma: no cover
        return ResponseHeadersPolicyAccessControlAllowOrigins.make_one(
            self.boto3_raw_data["AccessControlAllowOrigins"]
        )

    @cached_property
    def AccessControlAllowHeaders(self):  # pragma: no cover
        return ResponseHeadersPolicyAccessControlAllowHeaders.make_one(
            self.boto3_raw_data["AccessControlAllowHeaders"]
        )

    @cached_property
    def AccessControlAllowMethods(self):  # pragma: no cover
        return ResponseHeadersPolicyAccessControlAllowMethods.make_one(
            self.boto3_raw_data["AccessControlAllowMethods"]
        )

    AccessControlAllowCredentials = field("AccessControlAllowCredentials")
    OriginOverride = field("OriginOverride")

    @cached_property
    def AccessControlExposeHeaders(self):  # pragma: no cover
        return ResponseHeadersPolicyAccessControlExposeHeaders.make_one(
            self.boto3_raw_data["AccessControlExposeHeaders"]
        )

    AccessControlMaxAgeSec = field("AccessControlMaxAgeSec")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ResponseHeadersPolicyCorsConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseHeadersPolicyCorsConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyCustomHeadersConfigOutput:
    boto3_raw_data: (
        "type_defs.ResponseHeadersPolicyCustomHeadersConfigOutputTypeDef"
    ) = dataclasses.field()

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return ResponseHeadersPolicyCustomHeader.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyCustomHeadersConfigOutputTypeDef"
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
                "type_defs.ResponseHeadersPolicyCustomHeadersConfigOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyCustomHeadersConfig:
    boto3_raw_data: "type_defs.ResponseHeadersPolicyCustomHeadersConfigTypeDef" = (
        dataclasses.field()
    )

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return ResponseHeadersPolicyCustomHeader.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyCustomHeadersConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseHeadersPolicyCustomHeadersConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyRemoveHeadersConfigOutput:
    boto3_raw_data: (
        "type_defs.ResponseHeadersPolicyRemoveHeadersConfigOutputTypeDef"
    ) = dataclasses.field()

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return ResponseHeadersPolicyRemoveHeader.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyRemoveHeadersConfigOutputTypeDef"
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
                "type_defs.ResponseHeadersPolicyRemoveHeadersConfigOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyRemoveHeadersConfig:
    boto3_raw_data: "type_defs.ResponseHeadersPolicyRemoveHeadersConfigTypeDef" = (
        dataclasses.field()
    )

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return ResponseHeadersPolicyRemoveHeader.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyRemoveHeadersConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseHeadersPolicyRemoveHeadersConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicySecurityHeadersConfig:
    boto3_raw_data: "type_defs.ResponseHeadersPolicySecurityHeadersConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def XSSProtection(self):  # pragma: no cover
        return ResponseHeadersPolicyXSSProtection.make_one(
            self.boto3_raw_data["XSSProtection"]
        )

    @cached_property
    def FrameOptions(self):  # pragma: no cover
        return ResponseHeadersPolicyFrameOptions.make_one(
            self.boto3_raw_data["FrameOptions"]
        )

    @cached_property
    def ReferrerPolicy(self):  # pragma: no cover
        return ResponseHeadersPolicyReferrerPolicy.make_one(
            self.boto3_raw_data["ReferrerPolicy"]
        )

    @cached_property
    def ContentSecurityPolicy(self):  # pragma: no cover
        return ResponseHeadersPolicyContentSecurityPolicy.make_one(
            self.boto3_raw_data["ContentSecurityPolicy"]
        )

    @cached_property
    def ContentTypeOptions(self):  # pragma: no cover
        return ResponseHeadersPolicyContentTypeOptions.make_one(
            self.boto3_raw_data["ContentTypeOptions"]
        )

    @cached_property
    def StrictTransportSecurity(self):  # pragma: no cover
        return ResponseHeadersPolicyStrictTransportSecurity.make_one(
            self.boto3_raw_data["StrictTransportSecurity"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicySecurityHeadersConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseHeadersPolicySecurityHeadersConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamingDistributionSummary:
    boto3_raw_data: "type_defs.StreamingDistributionSummaryTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    ARN = field("ARN")
    Status = field("Status")
    LastModifiedTime = field("LastModifiedTime")
    DomainName = field("DomainName")

    @cached_property
    def S3Origin(self):  # pragma: no cover
        return S3Origin.make_one(self.boto3_raw_data["S3Origin"])

    @cached_property
    def Aliases(self):  # pragma: no cover
        return AliasesOutput.make_one(self.boto3_raw_data["Aliases"])

    @cached_property
    def TrustedSigners(self):  # pragma: no cover
        return TrustedSignersOutput.make_one(self.boto3_raw_data["TrustedSigners"])

    Comment = field("Comment")
    PriceClass = field("PriceClass")
    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamingDistributionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamingDistributionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamingDistributionConfigOutput:
    boto3_raw_data: "type_defs.StreamingDistributionConfigOutputTypeDef" = (
        dataclasses.field()
    )

    CallerReference = field("CallerReference")

    @cached_property
    def S3Origin(self):  # pragma: no cover
        return S3Origin.make_one(self.boto3_raw_data["S3Origin"])

    Comment = field("Comment")

    @cached_property
    def TrustedSigners(self):  # pragma: no cover
        return TrustedSignersOutput.make_one(self.boto3_raw_data["TrustedSigners"])

    Enabled = field("Enabled")

    @cached_property
    def Aliases(self):  # pragma: no cover
        return AliasesOutput.make_one(self.boto3_raw_data["Aliases"])

    @cached_property
    def Logging(self):  # pragma: no cover
        return StreamingLoggingConfig.make_one(self.boto3_raw_data["Logging"])

    PriceClass = field("PriceClass")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StreamingDistributionConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamingDistributionConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    Resource = field("Resource")

    @cached_property
    def TagKeys(self):  # pragma: no cover
        return TagKeys.make_one(self.boto3_raw_data["TagKeys"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagsOutput:
    boto3_raw_data: "type_defs.TagsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagsOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tags:
    boto3_raw_data: "type_defs.TagsTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcOriginList:
    boto3_raw_data: "type_defs.VpcOriginListTypeDef" = dataclasses.field()

    Marker = field("Marker")
    MaxItems = field("MaxItems")
    IsTruncated = field("IsTruncated")
    Quantity = field("Quantity")
    NextMarker = field("NextMarker")

    @cached_property
    def Items(self):  # pragma: no cover
        return VpcOriginSummary.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcOriginListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcOriginListTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnycastIpListsResult:
    boto3_raw_data: "type_defs.ListAnycastIpListsResultTypeDef" = dataclasses.field()

    @cached_property
    def AnycastIpLists(self):  # pragma: no cover
        return AnycastIpListCollection.make_one(self.boto3_raw_data["AnycastIpLists"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAnycastIpListsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnycastIpListsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ForwardedValuesOutput:
    boto3_raw_data: "type_defs.ForwardedValuesOutputTypeDef" = dataclasses.field()

    QueryString = field("QueryString")

    @cached_property
    def Cookies(self):  # pragma: no cover
        return CookiePreferenceOutput.make_one(self.boto3_raw_data["Cookies"])

    @cached_property
    def Headers(self):  # pragma: no cover
        return HeadersOutput.make_one(self.boto3_raw_data["Headers"])

    @cached_property
    def QueryStringCacheKeys(self):  # pragma: no cover
        return QueryStringCacheKeysOutput.make_one(
            self.boto3_raw_data["QueryStringCacheKeys"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ForwardedValuesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ForwardedValuesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CookiePreference:
    boto3_raw_data: "type_defs.CookiePreferenceTypeDef" = dataclasses.field()

    Forward = field("Forward")
    WhitelistedNames = field("WhitelistedNames")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CookiePreferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CookiePreferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParametersInCacheKeyAndForwardedToOriginOutput:
    boto3_raw_data: (
        "type_defs.ParametersInCacheKeyAndForwardedToOriginOutputTypeDef"
    ) = dataclasses.field()

    EnableAcceptEncodingGzip = field("EnableAcceptEncodingGzip")

    @cached_property
    def HeadersConfig(self):  # pragma: no cover
        return CachePolicyHeadersConfigOutput.make_one(
            self.boto3_raw_data["HeadersConfig"]
        )

    @cached_property
    def CookiesConfig(self):  # pragma: no cover
        return CachePolicyCookiesConfigOutput.make_one(
            self.boto3_raw_data["CookiesConfig"]
        )

    @cached_property
    def QueryStringsConfig(self):  # pragma: no cover
        return CachePolicyQueryStringsConfigOutput.make_one(
            self.boto3_raw_data["QueryStringsConfig"]
        )

    EnableAcceptEncodingBrotli = field("EnableAcceptEncodingBrotli")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ParametersInCacheKeyAndForwardedToOriginOutputTypeDef"
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
                "type_defs.ParametersInCacheKeyAndForwardedToOriginOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginRequestPolicyConfigOutput:
    boto3_raw_data: "type_defs.OriginRequestPolicyConfigOutputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @cached_property
    def HeadersConfig(self):  # pragma: no cover
        return OriginRequestPolicyHeadersConfigOutput.make_one(
            self.boto3_raw_data["HeadersConfig"]
        )

    @cached_property
    def CookiesConfig(self):  # pragma: no cover
        return OriginRequestPolicyCookiesConfigOutput.make_one(
            self.boto3_raw_data["CookiesConfig"]
        )

    @cached_property
    def QueryStringsConfig(self):  # pragma: no cover
        return OriginRequestPolicyQueryStringsConfigOutput.make_one(
            self.boto3_raw_data["QueryStringsConfig"]
        )

    Comment = field("Comment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OriginRequestPolicyConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginRequestPolicyConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParametersInCacheKeyAndForwardedToOrigin:
    boto3_raw_data: "type_defs.ParametersInCacheKeyAndForwardedToOriginTypeDef" = (
        dataclasses.field()
    )

    EnableAcceptEncodingGzip = field("EnableAcceptEncodingGzip")

    @cached_property
    def HeadersConfig(self):  # pragma: no cover
        return CachePolicyHeadersConfig.make_one(self.boto3_raw_data["HeadersConfig"])

    @cached_property
    def CookiesConfig(self):  # pragma: no cover
        return CachePolicyCookiesConfig.make_one(self.boto3_raw_data["CookiesConfig"])

    @cached_property
    def QueryStringsConfig(self):  # pragma: no cover
        return CachePolicyQueryStringsConfig.make_one(
            self.boto3_raw_data["QueryStringsConfig"]
        )

    EnableAcceptEncodingBrotli = field("EnableAcceptEncodingBrotli")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ParametersInCacheKeyAndForwardedToOriginTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParametersInCacheKeyAndForwardedToOriginTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginRequestPolicyConfig:
    boto3_raw_data: "type_defs.OriginRequestPolicyConfigTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def HeadersConfig(self):  # pragma: no cover
        return OriginRequestPolicyHeadersConfig.make_one(
            self.boto3_raw_data["HeadersConfig"]
        )

    @cached_property
    def CookiesConfig(self):  # pragma: no cover
        return OriginRequestPolicyCookiesConfig.make_one(
            self.boto3_raw_data["CookiesConfig"]
        )

    @cached_property
    def QueryStringsConfig(self):  # pragma: no cover
        return OriginRequestPolicyQueryStringsConfig.make_one(
            self.boto3_raw_data["QueryStringsConfig"]
        )

    Comment = field("Comment")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OriginRequestPolicyConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginRequestPolicyConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllowedMethods:
    boto3_raw_data: "type_defs.AllowedMethodsTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")
    CachedMethods = field("CachedMethods")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AllowedMethodsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AllowedMethodsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCloudFrontOriginAccessIdentityResult:
    boto3_raw_data: "type_defs.CreateCloudFrontOriginAccessIdentityResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CloudFrontOriginAccessIdentity(self):  # pragma: no cover
        return CloudFrontOriginAccessIdentity.make_one(
            self.boto3_raw_data["CloudFrontOriginAccessIdentity"]
        )

    Location = field("Location")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCloudFrontOriginAccessIdentityResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCloudFrontOriginAccessIdentityResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCloudFrontOriginAccessIdentityResult:
    boto3_raw_data: "type_defs.GetCloudFrontOriginAccessIdentityResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CloudFrontOriginAccessIdentity(self):  # pragma: no cover
        return CloudFrontOriginAccessIdentity.make_one(
            self.boto3_raw_data["CloudFrontOriginAccessIdentity"]
        )

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCloudFrontOriginAccessIdentityResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCloudFrontOriginAccessIdentityResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCloudFrontOriginAccessIdentityResult:
    boto3_raw_data: "type_defs.UpdateCloudFrontOriginAccessIdentityResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CloudFrontOriginAccessIdentity(self):  # pragma: no cover
        return CloudFrontOriginAccessIdentity.make_one(
            self.boto3_raw_data["CloudFrontOriginAccessIdentity"]
        )

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCloudFrontOriginAccessIdentityResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCloudFrontOriginAccessIdentityResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCloudFrontOriginAccessIdentitiesResult:
    boto3_raw_data: "type_defs.ListCloudFrontOriginAccessIdentitiesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CloudFrontOriginAccessIdentityList(self):  # pragma: no cover
        return CloudFrontOriginAccessIdentityList.make_one(
            self.boto3_raw_data["CloudFrontOriginAccessIdentityList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCloudFrontOriginAccessIdentitiesResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCloudFrontOriginAccessIdentitiesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConflictingAliasesResult:
    boto3_raw_data: "type_defs.ListConflictingAliasesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConflictingAliasesList(self):  # pragma: no cover
        return ConflictingAliasesList.make_one(
            self.boto3_raw_data["ConflictingAliasesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConflictingAliasesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConflictingAliasesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentTypeProfileConfigOutput:
    boto3_raw_data: "type_defs.ContentTypeProfileConfigOutputTypeDef" = (
        dataclasses.field()
    )

    ForwardWhenContentTypeIsUnknown = field("ForwardWhenContentTypeIsUnknown")

    @cached_property
    def ContentTypeProfiles(self):  # pragma: no cover
        return ContentTypeProfilesOutput.make_one(
            self.boto3_raw_data["ContentTypeProfiles"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ContentTypeProfileConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentTypeProfileConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentTypeProfileConfig:
    boto3_raw_data: "type_defs.ContentTypeProfileConfigTypeDef" = dataclasses.field()

    ForwardWhenContentTypeIsUnknown = field("ForwardWhenContentTypeIsUnknown")

    @cached_property
    def ContentTypeProfiles(self):  # pragma: no cover
        return ContentTypeProfiles.make_one(self.boto3_raw_data["ContentTypeProfiles"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContentTypeProfileConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentTypeProfileConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrafficConfig:
    boto3_raw_data: "type_defs.TrafficConfigTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def SingleWeightConfig(self):  # pragma: no cover
        return ContinuousDeploymentSingleWeightConfig.make_one(
            self.boto3_raw_data["SingleWeightConfig"]
        )

    @cached_property
    def SingleHeaderConfig(self):  # pragma: no cover
        return ContinuousDeploymentSingleHeaderConfig.make_one(
            self.boto3_raw_data["SingleHeaderConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrafficConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TrafficConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeyValueStoresResult:
    boto3_raw_data: "type_defs.ListKeyValueStoresResultTypeDef" = dataclasses.field()

    @cached_property
    def KeyValueStoreList(self):  # pragma: no cover
        return KeyValueStoreList.make_one(self.boto3_raw_data["KeyValueStoreList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKeyValueStoresResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeyValueStoresResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOriginAccessControlResult:
    boto3_raw_data: "type_defs.CreateOriginAccessControlResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OriginAccessControl(self):  # pragma: no cover
        return OriginAccessControl.make_one(self.boto3_raw_data["OriginAccessControl"])

    Location = field("Location")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateOriginAccessControlResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOriginAccessControlResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOriginAccessControlResult:
    boto3_raw_data: "type_defs.GetOriginAccessControlResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OriginAccessControl(self):  # pragma: no cover
        return OriginAccessControl.make_one(self.boto3_raw_data["OriginAccessControl"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOriginAccessControlResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOriginAccessControlResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOriginAccessControlResult:
    boto3_raw_data: "type_defs.UpdateOriginAccessControlResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OriginAccessControl(self):  # pragma: no cover
        return OriginAccessControl.make_one(self.boto3_raw_data["OriginAccessControl"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateOriginAccessControlResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOriginAccessControlResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePublicKeyResult:
    boto3_raw_data: "type_defs.CreatePublicKeyResultTypeDef" = dataclasses.field()

    @cached_property
    def PublicKey(self):  # pragma: no cover
        return PublicKey.make_one(self.boto3_raw_data["PublicKey"])

    Location = field("Location")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePublicKeyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePublicKeyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPublicKeyResult:
    boto3_raw_data: "type_defs.GetPublicKeyResultTypeDef" = dataclasses.field()

    @cached_property
    def PublicKey(self):  # pragma: no cover
        return PublicKey.make_one(self.boto3_raw_data["PublicKey"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPublicKeyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPublicKeyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePublicKeyResult:
    boto3_raw_data: "type_defs.UpdatePublicKeyResultTypeDef" = dataclasses.field()

    @cached_property
    def PublicKey(self):  # pragma: no cover
        return PublicKey.make_one(self.boto3_raw_data["PublicKey"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePublicKeyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePublicKeyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginOutput:
    boto3_raw_data: "type_defs.OriginOutputTypeDef" = dataclasses.field()

    Id = field("Id")
    DomainName = field("DomainName")
    OriginPath = field("OriginPath")

    @cached_property
    def CustomHeaders(self):  # pragma: no cover
        return CustomHeadersOutput.make_one(self.boto3_raw_data["CustomHeaders"])

    @cached_property
    def S3OriginConfig(self):  # pragma: no cover
        return S3OriginConfig.make_one(self.boto3_raw_data["S3OriginConfig"])

    @cached_property
    def CustomOriginConfig(self):  # pragma: no cover
        return CustomOriginConfigOutput.make_one(
            self.boto3_raw_data["CustomOriginConfig"]
        )

    @cached_property
    def VpcOriginConfig(self):  # pragma: no cover
        return VpcOriginConfig.make_one(self.boto3_raw_data["VpcOriginConfig"])

    ConnectionAttempts = field("ConnectionAttempts")
    ConnectionTimeout = field("ConnectionTimeout")
    ResponseCompletionTimeout = field("ResponseCompletionTimeout")

    @cached_property
    def OriginShield(self):  # pragma: no cover
        return OriginShield.make_one(self.boto3_raw_data["OriginShield"])

    OriginAccessControlId = field("OriginAccessControlId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OriginOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OriginOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcOrigin:
    boto3_raw_data: "type_defs.VpcOriginTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Status = field("Status")
    CreatedTime = field("CreatedTime")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def VpcOriginEndpointConfig(self):  # pragma: no cover
        return VpcOriginEndpointConfigOutput.make_one(
            self.boto3_raw_data["VpcOriginEndpointConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcOriginTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcOriginTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DistributionTenantSummary:
    boto3_raw_data: "type_defs.DistributionTenantSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    DistributionId = field("DistributionId")
    Name = field("Name")
    Arn = field("Arn")

    @cached_property
    def Domains(self):  # pragma: no cover
        return DomainResult.make_many(self.boto3_raw_data["Domains"])

    CreatedTime = field("CreatedTime")
    LastModifiedTime = field("LastModifiedTime")
    ETag = field("ETag")
    ConnectionGroupId = field("ConnectionGroupId")

    @cached_property
    def Customizations(self):  # pragma: no cover
        return CustomizationsOutput.make_one(self.boto3_raw_data["Customizations"])

    Enabled = field("Enabled")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DistributionTenantSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DistributionTenantSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionEntitiesOutput:
    boto3_raw_data: "type_defs.EncryptionEntitiesOutputTypeDef" = dataclasses.field()

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return EncryptionEntityOutput.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncryptionEntitiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionEntitiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionEntities:
    boto3_raw_data: "type_defs.EncryptionEntitiesTypeDef" = dataclasses.field()

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return EncryptionEntity.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncryptionEntitiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionEntitiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRealtimeLogConfigRequest:
    boto3_raw_data: "type_defs.CreateRealtimeLogConfigRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EndPoints(self):  # pragma: no cover
        return EndPoint.make_many(self.boto3_raw_data["EndPoints"])

    Fields = field("Fields")
    Name = field("Name")
    SamplingRate = field("SamplingRate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateRealtimeLogConfigRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRealtimeLogConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealtimeLogConfig:
    boto3_raw_data: "type_defs.RealtimeLogConfigTypeDef" = dataclasses.field()

    ARN = field("ARN")
    Name = field("Name")
    SamplingRate = field("SamplingRate")

    @cached_property
    def EndPoints(self):  # pragma: no cover
        return EndPoint.make_many(self.boto3_raw_data["EndPoints"])

    Fields = field("Fields")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RealtimeLogConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RealtimeLogConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRealtimeLogConfigRequest:
    boto3_raw_data: "type_defs.UpdateRealtimeLogConfigRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EndPoints(self):  # pragma: no cover
        return EndPoint.make_many(self.boto3_raw_data["EndPoints"])

    Fields = field("Fields")
    Name = field("Name")
    ARN = field("ARN")
    SamplingRate = field("SamplingRate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateRealtimeLogConfigRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRealtimeLogConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Restrictions:
    boto3_raw_data: "type_defs.RestrictionsTypeDef" = dataclasses.field()

    GeoRestriction = field("GeoRestriction")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RestrictionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RestrictionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKeyGroupResult:
    boto3_raw_data: "type_defs.CreateKeyGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def KeyGroup(self):  # pragma: no cover
        return KeyGroup.make_one(self.boto3_raw_data["KeyGroup"])

    Location = field("Location")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKeyGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKeyGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKeyGroupResult:
    boto3_raw_data: "type_defs.GetKeyGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def KeyGroup(self):  # pragma: no cover
        return KeyGroup.make_one(self.boto3_raw_data["KeyGroup"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetKeyGroupResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKeyGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyGroupSummary:
    boto3_raw_data: "type_defs.KeyGroupSummaryTypeDef" = dataclasses.field()

    @cached_property
    def KeyGroup(self):  # pragma: no cover
        return KeyGroup.make_one(self.boto3_raw_data["KeyGroup"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyGroupSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyGroupSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKeyGroupResult:
    boto3_raw_data: "type_defs.UpdateKeyGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def KeyGroup(self):  # pragma: no cover
        return KeyGroup.make_one(self.boto3_raw_data["KeyGroup"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateKeyGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKeyGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Invalidation:
    boto3_raw_data: "type_defs.InvalidationTypeDef" = dataclasses.field()

    Id = field("Id")
    Status = field("Status")
    CreateTime = field("CreateTime")

    @cached_property
    def InvalidationBatch(self):  # pragma: no cover
        return InvalidationBatchOutput.make_one(
            self.boto3_raw_data["InvalidationBatch"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InvalidationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InvalidationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvalidationsForDistributionTenantResult:
    boto3_raw_data: "type_defs.ListInvalidationsForDistributionTenantResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InvalidationList(self):  # pragma: no cover
        return InvalidationList.make_one(self.boto3_raw_data["InvalidationList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInvalidationsForDistributionTenantResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvalidationsForDistributionTenantResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvalidationsResult:
    boto3_raw_data: "type_defs.ListInvalidationsResultTypeDef" = dataclasses.field()

    @cached_property
    def InvalidationList(self):  # pragma: no cover
        return InvalidationList.make_one(self.boto3_raw_data["InvalidationList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInvalidationsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvalidationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActiveTrustedKeyGroups:
    boto3_raw_data: "type_defs.ActiveTrustedKeyGroupsTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return KGKeyPairIds.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActiveTrustedKeyGroupsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActiveTrustedKeyGroupsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActiveTrustedSigners:
    boto3_raw_data: "type_defs.ActiveTrustedSignersTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return Signer.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActiveTrustedSignersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActiveTrustedSignersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKeyGroupRequest:
    boto3_raw_data: "type_defs.CreateKeyGroupRequestTypeDef" = dataclasses.field()

    KeyGroupConfig = field("KeyGroupConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKeyGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKeyGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKeyGroupRequest:
    boto3_raw_data: "type_defs.UpdateKeyGroupRequestTypeDef" = dataclasses.field()

    KeyGroupConfig = field("KeyGroupConfig")
    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateKeyGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKeyGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionConfigOutput:
    boto3_raw_data: "type_defs.FunctionConfigOutputTypeDef" = dataclasses.field()

    Comment = field("Comment")
    Runtime = field("Runtime")

    @cached_property
    def KeyValueStoreAssociations(self):  # pragma: no cover
        return KeyValueStoreAssociationsOutput.make_one(
            self.boto3_raw_data["KeyValueStoreAssociations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FunctionConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionConfig:
    boto3_raw_data: "type_defs.FunctionConfigTypeDef" = dataclasses.field()

    Comment = field("Comment")
    Runtime = field("Runtime")

    @cached_property
    def KeyValueStoreAssociations(self):  # pragma: no cover
        return KeyValueStoreAssociations.make_one(
            self.boto3_raw_data["KeyValueStoreAssociations"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FunctionConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FunctionConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetManagedCertificateDetailsResult:
    boto3_raw_data: "type_defs.GetManagedCertificateDetailsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ManagedCertificateDetails(self):  # pragma: no cover
        return ManagedCertificateDetails.make_one(
            self.boto3_raw_data["ManagedCertificateDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetManagedCertificateDetailsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetManagedCertificateDetailsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMonitoringSubscriptionRequest:
    boto3_raw_data: "type_defs.CreateMonitoringSubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    DistributionId = field("DistributionId")

    @cached_property
    def MonitoringSubscription(self):  # pragma: no cover
        return MonitoringSubscription.make_one(
            self.boto3_raw_data["MonitoringSubscription"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMonitoringSubscriptionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMonitoringSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMonitoringSubscriptionResult:
    boto3_raw_data: "type_defs.CreateMonitoringSubscriptionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MonitoringSubscription(self):  # pragma: no cover
        return MonitoringSubscription.make_one(
            self.boto3_raw_data["MonitoringSubscription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMonitoringSubscriptionResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMonitoringSubscriptionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMonitoringSubscriptionResult:
    boto3_raw_data: "type_defs.GetMonitoringSubscriptionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MonitoringSubscription(self):  # pragma: no cover
        return MonitoringSubscription.make_one(
            self.boto3_raw_data["MonitoringSubscription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMonitoringSubscriptionResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMonitoringSubscriptionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOriginAccessControlsResult:
    boto3_raw_data: "type_defs.ListOriginAccessControlsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OriginAccessControlList(self):  # pragma: no cover
        return OriginAccessControlList.make_one(
            self.boto3_raw_data["OriginAccessControlList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOriginAccessControlsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOriginAccessControlsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginGroupOutput:
    boto3_raw_data: "type_defs.OriginGroupOutputTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def FailoverCriteria(self):  # pragma: no cover
        return OriginGroupFailoverCriteriaOutput.make_one(
            self.boto3_raw_data["FailoverCriteria"]
        )

    @cached_property
    def Members(self):  # pragma: no cover
        return OriginGroupMembersOutput.make_one(self.boto3_raw_data["Members"])

    SelectionCriteria = field("SelectionCriteria")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OriginGroupOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomOriginConfig:
    boto3_raw_data: "type_defs.CustomOriginConfigTypeDef" = dataclasses.field()

    HTTPPort = field("HTTPPort")
    HTTPSPort = field("HTTPSPort")
    OriginProtocolPolicy = field("OriginProtocolPolicy")
    OriginSslProtocols = field("OriginSslProtocols")
    OriginReadTimeout = field("OriginReadTimeout")
    OriginKeepaliveTimeout = field("OriginKeepaliveTimeout")
    IpAddressType = field("IpAddressType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomOriginConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomOriginConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterDefinition:
    boto3_raw_data: "type_defs.ParameterDefinitionTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Definition(self):  # pragma: no cover
        return ParameterDefinitionSchema.make_one(self.boto3_raw_data["Definition"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParameterDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParameterDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPublicKeysResult:
    boto3_raw_data: "type_defs.ListPublicKeysResultTypeDef" = dataclasses.field()

    @cached_property
    def PublicKeyList(self):  # pragma: no cover
        return PublicKeyList.make_one(self.boto3_raw_data["PublicKeyList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPublicKeysResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPublicKeysResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryArgProfileConfigOutput:
    boto3_raw_data: "type_defs.QueryArgProfileConfigOutputTypeDef" = dataclasses.field()

    ForwardWhenQueryArgProfileIsUnknown = field("ForwardWhenQueryArgProfileIsUnknown")

    @cached_property
    def QueryArgProfiles(self):  # pragma: no cover
        return QueryArgProfilesOutput.make_one(self.boto3_raw_data["QueryArgProfiles"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryArgProfileConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryArgProfileConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryArgProfileConfig:
    boto3_raw_data: "type_defs.QueryArgProfileConfigTypeDef" = dataclasses.field()

    ForwardWhenQueryArgProfileIsUnknown = field("ForwardWhenQueryArgProfileIsUnknown")

    @cached_property
    def QueryArgProfiles(self):  # pragma: no cover
        return QueryArgProfiles.make_one(self.boto3_raw_data["QueryArgProfiles"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryArgProfileConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryArgProfileConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyConfigOutput:
    boto3_raw_data: "type_defs.ResponseHeadersPolicyConfigOutputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Comment = field("Comment")

    @cached_property
    def CorsConfig(self):  # pragma: no cover
        return ResponseHeadersPolicyCorsConfigOutput.make_one(
            self.boto3_raw_data["CorsConfig"]
        )

    @cached_property
    def SecurityHeadersConfig(self):  # pragma: no cover
        return ResponseHeadersPolicySecurityHeadersConfig.make_one(
            self.boto3_raw_data["SecurityHeadersConfig"]
        )

    @cached_property
    def ServerTimingHeadersConfig(self):  # pragma: no cover
        return ResponseHeadersPolicyServerTimingHeadersConfig.make_one(
            self.boto3_raw_data["ServerTimingHeadersConfig"]
        )

    @cached_property
    def CustomHeadersConfig(self):  # pragma: no cover
        return ResponseHeadersPolicyCustomHeadersConfigOutput.make_one(
            self.boto3_raw_data["CustomHeadersConfig"]
        )

    @cached_property
    def RemoveHeadersConfig(self):  # pragma: no cover
        return ResponseHeadersPolicyRemoveHeadersConfigOutput.make_one(
            self.boto3_raw_data["RemoveHeadersConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResponseHeadersPolicyConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseHeadersPolicyConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyConfig:
    boto3_raw_data: "type_defs.ResponseHeadersPolicyConfigTypeDef" = dataclasses.field()

    Name = field("Name")
    Comment = field("Comment")

    @cached_property
    def CorsConfig(self):  # pragma: no cover
        return ResponseHeadersPolicyCorsConfig.make_one(
            self.boto3_raw_data["CorsConfig"]
        )

    @cached_property
    def SecurityHeadersConfig(self):  # pragma: no cover
        return ResponseHeadersPolicySecurityHeadersConfig.make_one(
            self.boto3_raw_data["SecurityHeadersConfig"]
        )

    @cached_property
    def ServerTimingHeadersConfig(self):  # pragma: no cover
        return ResponseHeadersPolicyServerTimingHeadersConfig.make_one(
            self.boto3_raw_data["ServerTimingHeadersConfig"]
        )

    @cached_property
    def CustomHeadersConfig(self):  # pragma: no cover
        return ResponseHeadersPolicyCustomHeadersConfig.make_one(
            self.boto3_raw_data["CustomHeadersConfig"]
        )

    @cached_property
    def RemoveHeadersConfig(self):  # pragma: no cover
        return ResponseHeadersPolicyRemoveHeadersConfig.make_one(
            self.boto3_raw_data["RemoveHeadersConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResponseHeadersPolicyConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseHeadersPolicyConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamingDistributionList:
    boto3_raw_data: "type_defs.StreamingDistributionListTypeDef" = dataclasses.field()

    Marker = field("Marker")
    MaxItems = field("MaxItems")
    IsTruncated = field("IsTruncated")
    Quantity = field("Quantity")
    NextMarker = field("NextMarker")

    @cached_property
    def Items(self):  # pragma: no cover
        return StreamingDistributionSummary.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamingDistributionListTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamingDistributionListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginGroupFailoverCriteria:
    boto3_raw_data: "type_defs.OriginGroupFailoverCriteriaTypeDef" = dataclasses.field()

    StatusCodes = field("StatusCodes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OriginGroupFailoverCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginGroupFailoverCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStreamingDistributionConfigResult:
    boto3_raw_data: "type_defs.GetStreamingDistributionConfigResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StreamingDistributionConfig(self):  # pragma: no cover
        return StreamingDistributionConfigOutput.make_one(
            self.boto3_raw_data["StreamingDistributionConfig"]
        )

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetStreamingDistributionConfigResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStreamingDistributionConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionGroup:
    boto3_raw_data: "type_defs.ConnectionGroupTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Arn = field("Arn")
    CreatedTime = field("CreatedTime")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagsOutput.make_one(self.boto3_raw_data["Tags"])

    Ipv6Enabled = field("Ipv6Enabled")
    RoutingEndpoint = field("RoutingEndpoint")
    AnycastIpListId = field("AnycastIpListId")
    Status = field("Status")
    Enabled = field("Enabled")
    IsDefault = field("IsDefault")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectionGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConnectionGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DistributionTenant:
    boto3_raw_data: "type_defs.DistributionTenantTypeDef" = dataclasses.field()

    Id = field("Id")
    DistributionId = field("DistributionId")
    Name = field("Name")
    Arn = field("Arn")

    @cached_property
    def Domains(self):  # pragma: no cover
        return DomainResult.make_many(self.boto3_raw_data["Domains"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagsOutput.make_one(self.boto3_raw_data["Tags"])

    @cached_property
    def Customizations(self):  # pragma: no cover
        return CustomizationsOutput.make_one(self.boto3_raw_data["Customizations"])

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    ConnectionGroupId = field("ConnectionGroupId")
    CreatedTime = field("CreatedTime")
    LastModifiedTime = field("LastModifiedTime")
    Enabled = field("Enabled")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DistributionTenantTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DistributionTenantTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResult:
    boto3_raw_data: "type_defs.ListTagsForResourceResultTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagsOutput.make_one(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamingDistributionConfig:
    boto3_raw_data: "type_defs.StreamingDistributionConfigTypeDef" = dataclasses.field()

    CallerReference = field("CallerReference")

    @cached_property
    def S3Origin(self):  # pragma: no cover
        return S3Origin.make_one(self.boto3_raw_data["S3Origin"])

    Comment = field("Comment")
    TrustedSigners = field("TrustedSigners")
    Enabled = field("Enabled")
    Aliases = field("Aliases")

    @cached_property
    def Logging(self):  # pragma: no cover
        return StreamingLoggingConfig.make_one(self.boto3_raw_data["Logging"])

    PriceClass = field("PriceClass")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamingDistributionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamingDistributionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVpcOriginsResult:
    boto3_raw_data: "type_defs.ListVpcOriginsResultTypeDef" = dataclasses.field()

    @cached_property
    def VpcOriginList(self):  # pragma: no cover
        return VpcOriginList.make_one(self.boto3_raw_data["VpcOriginList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVpcOriginsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVpcOriginsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheBehaviorOutput:
    boto3_raw_data: "type_defs.CacheBehaviorOutputTypeDef" = dataclasses.field()

    PathPattern = field("PathPattern")
    TargetOriginId = field("TargetOriginId")
    ViewerProtocolPolicy = field("ViewerProtocolPolicy")

    @cached_property
    def TrustedSigners(self):  # pragma: no cover
        return TrustedSignersOutput.make_one(self.boto3_raw_data["TrustedSigners"])

    @cached_property
    def TrustedKeyGroups(self):  # pragma: no cover
        return TrustedKeyGroupsOutput.make_one(self.boto3_raw_data["TrustedKeyGroups"])

    @cached_property
    def AllowedMethods(self):  # pragma: no cover
        return AllowedMethodsOutput.make_one(self.boto3_raw_data["AllowedMethods"])

    SmoothStreaming = field("SmoothStreaming")
    Compress = field("Compress")

    @cached_property
    def LambdaFunctionAssociations(self):  # pragma: no cover
        return LambdaFunctionAssociationsOutput.make_one(
            self.boto3_raw_data["LambdaFunctionAssociations"]
        )

    @cached_property
    def FunctionAssociations(self):  # pragma: no cover
        return FunctionAssociationsOutput.make_one(
            self.boto3_raw_data["FunctionAssociations"]
        )

    FieldLevelEncryptionId = field("FieldLevelEncryptionId")
    RealtimeLogConfigArn = field("RealtimeLogConfigArn")
    CachePolicyId = field("CachePolicyId")
    OriginRequestPolicyId = field("OriginRequestPolicyId")
    ResponseHeadersPolicyId = field("ResponseHeadersPolicyId")

    @cached_property
    def GrpcConfig(self):  # pragma: no cover
        return GrpcConfig.make_one(self.boto3_raw_data["GrpcConfig"])

    @cached_property
    def ForwardedValues(self):  # pragma: no cover
        return ForwardedValuesOutput.make_one(self.boto3_raw_data["ForwardedValues"])

    MinTTL = field("MinTTL")
    DefaultTTL = field("DefaultTTL")
    MaxTTL = field("MaxTTL")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CacheBehaviorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheBehaviorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultCacheBehaviorOutput:
    boto3_raw_data: "type_defs.DefaultCacheBehaviorOutputTypeDef" = dataclasses.field()

    TargetOriginId = field("TargetOriginId")
    ViewerProtocolPolicy = field("ViewerProtocolPolicy")

    @cached_property
    def TrustedSigners(self):  # pragma: no cover
        return TrustedSignersOutput.make_one(self.boto3_raw_data["TrustedSigners"])

    @cached_property
    def TrustedKeyGroups(self):  # pragma: no cover
        return TrustedKeyGroupsOutput.make_one(self.boto3_raw_data["TrustedKeyGroups"])

    @cached_property
    def AllowedMethods(self):  # pragma: no cover
        return AllowedMethodsOutput.make_one(self.boto3_raw_data["AllowedMethods"])

    SmoothStreaming = field("SmoothStreaming")
    Compress = field("Compress")

    @cached_property
    def LambdaFunctionAssociations(self):  # pragma: no cover
        return LambdaFunctionAssociationsOutput.make_one(
            self.boto3_raw_data["LambdaFunctionAssociations"]
        )

    @cached_property
    def FunctionAssociations(self):  # pragma: no cover
        return FunctionAssociationsOutput.make_one(
            self.boto3_raw_data["FunctionAssociations"]
        )

    FieldLevelEncryptionId = field("FieldLevelEncryptionId")
    RealtimeLogConfigArn = field("RealtimeLogConfigArn")
    CachePolicyId = field("CachePolicyId")
    OriginRequestPolicyId = field("OriginRequestPolicyId")
    ResponseHeadersPolicyId = field("ResponseHeadersPolicyId")

    @cached_property
    def GrpcConfig(self):  # pragma: no cover
        return GrpcConfig.make_one(self.boto3_raw_data["GrpcConfig"])

    @cached_property
    def ForwardedValues(self):  # pragma: no cover
        return ForwardedValuesOutput.make_one(self.boto3_raw_data["ForwardedValues"])

    MinTTL = field("MinTTL")
    DefaultTTL = field("DefaultTTL")
    MaxTTL = field("MaxTTL")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DefaultCacheBehaviorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultCacheBehaviorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CachePolicyConfigOutput:
    boto3_raw_data: "type_defs.CachePolicyConfigOutputTypeDef" = dataclasses.field()

    Name = field("Name")
    MinTTL = field("MinTTL")
    Comment = field("Comment")
    DefaultTTL = field("DefaultTTL")
    MaxTTL = field("MaxTTL")

    @cached_property
    def ParametersInCacheKeyAndForwardedToOrigin(self):  # pragma: no cover
        return ParametersInCacheKeyAndForwardedToOriginOutput.make_one(
            self.boto3_raw_data["ParametersInCacheKeyAndForwardedToOrigin"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CachePolicyConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CachePolicyConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOriginRequestPolicyConfigResult:
    boto3_raw_data: "type_defs.GetOriginRequestPolicyConfigResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OriginRequestPolicyConfig(self):  # pragma: no cover
        return OriginRequestPolicyConfigOutput.make_one(
            self.boto3_raw_data["OriginRequestPolicyConfig"]
        )

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOriginRequestPolicyConfigResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOriginRequestPolicyConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginRequestPolicy:
    boto3_raw_data: "type_defs.OriginRequestPolicyTypeDef" = dataclasses.field()

    Id = field("Id")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def OriginRequestPolicyConfig(self):  # pragma: no cover
        return OriginRequestPolicyConfigOutput.make_one(
            self.boto3_raw_data["OriginRequestPolicyConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OriginRequestPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginRequestPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CachePolicyConfig:
    boto3_raw_data: "type_defs.CachePolicyConfigTypeDef" = dataclasses.field()

    Name = field("Name")
    MinTTL = field("MinTTL")
    Comment = field("Comment")
    DefaultTTL = field("DefaultTTL")
    MaxTTL = field("MaxTTL")

    @cached_property
    def ParametersInCacheKeyAndForwardedToOrigin(self):  # pragma: no cover
        return ParametersInCacheKeyAndForwardedToOrigin.make_one(
            self.boto3_raw_data["ParametersInCacheKeyAndForwardedToOrigin"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CachePolicyConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CachePolicyConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContinuousDeploymentPolicyConfigOutput:
    boto3_raw_data: "type_defs.ContinuousDeploymentPolicyConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StagingDistributionDnsNames(self):  # pragma: no cover
        return StagingDistributionDnsNamesOutput.make_one(
            self.boto3_raw_data["StagingDistributionDnsNames"]
        )

    Enabled = field("Enabled")

    @cached_property
    def TrafficConfig(self):  # pragma: no cover
        return TrafficConfig.make_one(self.boto3_raw_data["TrafficConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ContinuousDeploymentPolicyConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContinuousDeploymentPolicyConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContinuousDeploymentPolicyConfig:
    boto3_raw_data: "type_defs.ContinuousDeploymentPolicyConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StagingDistributionDnsNames(self):  # pragma: no cover
        return StagingDistributionDnsNames.make_one(
            self.boto3_raw_data["StagingDistributionDnsNames"]
        )

    Enabled = field("Enabled")

    @cached_property
    def TrafficConfig(self):  # pragma: no cover
        return TrafficConfig.make_one(self.boto3_raw_data["TrafficConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ContinuousDeploymentPolicyConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContinuousDeploymentPolicyConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginsOutput:
    boto3_raw_data: "type_defs.OriginsOutputTypeDef" = dataclasses.field()

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return OriginOutput.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OriginsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OriginsOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVpcOriginResult:
    boto3_raw_data: "type_defs.CreateVpcOriginResultTypeDef" = dataclasses.field()

    @cached_property
    def VpcOrigin(self):  # pragma: no cover
        return VpcOrigin.make_one(self.boto3_raw_data["VpcOrigin"])

    Location = field("Location")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVpcOriginResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcOriginResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVpcOriginResult:
    boto3_raw_data: "type_defs.DeleteVpcOriginResultTypeDef" = dataclasses.field()

    @cached_property
    def VpcOrigin(self):  # pragma: no cover
        return VpcOrigin.make_one(self.boto3_raw_data["VpcOrigin"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVpcOriginResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVpcOriginResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVpcOriginResult:
    boto3_raw_data: "type_defs.GetVpcOriginResultTypeDef" = dataclasses.field()

    @cached_property
    def VpcOrigin(self):  # pragma: no cover
        return VpcOrigin.make_one(self.boto3_raw_data["VpcOrigin"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVpcOriginResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVpcOriginResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVpcOriginResult:
    boto3_raw_data: "type_defs.UpdateVpcOriginResultTypeDef" = dataclasses.field()

    @cached_property
    def VpcOrigin(self):  # pragma: no cover
        return VpcOrigin.make_one(self.boto3_raw_data["VpcOrigin"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVpcOriginResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVpcOriginResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionTenantsByCustomizationResult:
    boto3_raw_data: "type_defs.ListDistributionTenantsByCustomizationResultTypeDef" = (
        dataclasses.field()
    )

    NextMarker = field("NextMarker")

    @cached_property
    def DistributionTenantList(self):  # pragma: no cover
        return DistributionTenantSummary.make_many(
            self.boto3_raw_data["DistributionTenantList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionTenantsByCustomizationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionTenantsByCustomizationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionTenantsResult:
    boto3_raw_data: "type_defs.ListDistributionTenantsResultTypeDef" = (
        dataclasses.field()
    )

    NextMarker = field("NextMarker")

    @cached_property
    def DistributionTenantList(self):  # pragma: no cover
        return DistributionTenantSummary.make_many(
            self.boto3_raw_data["DistributionTenantList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDistributionTenantsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionTenantsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDistributionTenantRequest:
    boto3_raw_data: "type_defs.UpdateDistributionTenantRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IfMatch = field("IfMatch")
    DistributionId = field("DistributionId")

    @cached_property
    def Domains(self):  # pragma: no cover
        return DomainItem.make_many(self.boto3_raw_data["Domains"])

    Customizations = field("Customizations")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    ConnectionGroupId = field("ConnectionGroupId")

    @cached_property
    def ManagedCertificateRequest(self):  # pragma: no cover
        return ManagedCertificateRequest.make_one(
            self.boto3_raw_data["ManagedCertificateRequest"]
        )

    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDistributionTenantRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDistributionTenantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldLevelEncryptionProfileConfigOutput:
    boto3_raw_data: "type_defs.FieldLevelEncryptionProfileConfigOutputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    CallerReference = field("CallerReference")

    @cached_property
    def EncryptionEntities(self):  # pragma: no cover
        return EncryptionEntitiesOutput.make_one(
            self.boto3_raw_data["EncryptionEntities"]
        )

    Comment = field("Comment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FieldLevelEncryptionProfileConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldLevelEncryptionProfileConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldLevelEncryptionProfileSummary:
    boto3_raw_data: "type_defs.FieldLevelEncryptionProfileSummaryTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    LastModifiedTime = field("LastModifiedTime")
    Name = field("Name")

    @cached_property
    def EncryptionEntities(self):  # pragma: no cover
        return EncryptionEntitiesOutput.make_one(
            self.boto3_raw_data["EncryptionEntities"]
        )

    Comment = field("Comment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FieldLevelEncryptionProfileSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldLevelEncryptionProfileSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldLevelEncryptionProfileConfig:
    boto3_raw_data: "type_defs.FieldLevelEncryptionProfileConfigTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    CallerReference = field("CallerReference")

    @cached_property
    def EncryptionEntities(self):  # pragma: no cover
        return EncryptionEntities.make_one(self.boto3_raw_data["EncryptionEntities"])

    Comment = field("Comment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FieldLevelEncryptionProfileConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldLevelEncryptionProfileConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRealtimeLogConfigResult:
    boto3_raw_data: "type_defs.CreateRealtimeLogConfigResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RealtimeLogConfig(self):  # pragma: no cover
        return RealtimeLogConfig.make_one(self.boto3_raw_data["RealtimeLogConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateRealtimeLogConfigResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRealtimeLogConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRealtimeLogConfigResult:
    boto3_raw_data: "type_defs.GetRealtimeLogConfigResultTypeDef" = dataclasses.field()

    @cached_property
    def RealtimeLogConfig(self):  # pragma: no cover
        return RealtimeLogConfig.make_one(self.boto3_raw_data["RealtimeLogConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRealtimeLogConfigResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRealtimeLogConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealtimeLogConfigs:
    boto3_raw_data: "type_defs.RealtimeLogConfigsTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def Items(self):  # pragma: no cover
        return RealtimeLogConfig.make_many(self.boto3_raw_data["Items"])

    NextMarker = field("NextMarker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RealtimeLogConfigsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RealtimeLogConfigsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRealtimeLogConfigResult:
    boto3_raw_data: "type_defs.UpdateRealtimeLogConfigResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RealtimeLogConfig(self):  # pragma: no cover
        return RealtimeLogConfig.make_one(self.boto3_raw_data["RealtimeLogConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateRealtimeLogConfigResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRealtimeLogConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyGroupList:
    boto3_raw_data: "type_defs.KeyGroupListTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    Quantity = field("Quantity")
    NextMarker = field("NextMarker")

    @cached_property
    def Items(self):  # pragma: no cover
        return KeyGroupSummary.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyGroupListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyGroupListTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInvalidationForDistributionTenantResult:
    boto3_raw_data: "type_defs.CreateInvalidationForDistributionTenantResultTypeDef" = (
        dataclasses.field()
    )

    Location = field("Location")

    @cached_property
    def Invalidation(self):  # pragma: no cover
        return Invalidation.make_one(self.boto3_raw_data["Invalidation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateInvalidationForDistributionTenantResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInvalidationForDistributionTenantResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInvalidationResult:
    boto3_raw_data: "type_defs.CreateInvalidationResultTypeDef" = dataclasses.field()

    Location = field("Location")

    @cached_property
    def Invalidation(self):  # pragma: no cover
        return Invalidation.make_one(self.boto3_raw_data["Invalidation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInvalidationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInvalidationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInvalidationForDistributionTenantResult:
    boto3_raw_data: "type_defs.GetInvalidationForDistributionTenantResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Invalidation(self):  # pragma: no cover
        return Invalidation.make_one(self.boto3_raw_data["Invalidation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetInvalidationForDistributionTenantResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInvalidationForDistributionTenantResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInvalidationResult:
    boto3_raw_data: "type_defs.GetInvalidationResultTypeDef" = dataclasses.field()

    @cached_property
    def Invalidation(self):  # pragma: no cover
        return Invalidation.make_one(self.boto3_raw_data["Invalidation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInvalidationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInvalidationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInvalidationForDistributionTenantRequest:
    boto3_raw_data: (
        "type_defs.CreateInvalidationForDistributionTenantRequestTypeDef"
    ) = dataclasses.field()

    Id = field("Id")
    InvalidationBatch = field("InvalidationBatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateInvalidationForDistributionTenantRequestTypeDef"
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
                "type_defs.CreateInvalidationForDistributionTenantRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInvalidationRequest:
    boto3_raw_data: "type_defs.CreateInvalidationRequestTypeDef" = dataclasses.field()

    DistributionId = field("DistributionId")
    InvalidationBatch = field("InvalidationBatch")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInvalidationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInvalidationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamingDistribution:
    boto3_raw_data: "type_defs.StreamingDistributionTypeDef" = dataclasses.field()

    Id = field("Id")
    ARN = field("ARN")
    Status = field("Status")
    DomainName = field("DomainName")

    @cached_property
    def ActiveTrustedSigners(self):  # pragma: no cover
        return ActiveTrustedSigners.make_one(
            self.boto3_raw_data["ActiveTrustedSigners"]
        )

    @cached_property
    def StreamingDistributionConfig(self):  # pragma: no cover
        return StreamingDistributionConfigOutput.make_one(
            self.boto3_raw_data["StreamingDistributionConfig"]
        )

    LastModifiedTime = field("LastModifiedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamingDistributionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamingDistributionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionSummary:
    boto3_raw_data: "type_defs.FunctionSummaryTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def FunctionConfig(self):  # pragma: no cover
        return FunctionConfigOutput.make_one(self.boto3_raw_data["FunctionConfig"])

    @cached_property
    def FunctionMetadata(self):  # pragma: no cover
        return FunctionMetadata.make_one(self.boto3_raw_data["FunctionMetadata"])

    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FunctionSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FunctionSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginGroupsOutput:
    boto3_raw_data: "type_defs.OriginGroupsOutputTypeDef" = dataclasses.field()

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return OriginGroupOutput.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OriginGroupsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginGroupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVpcOriginRequest:
    boto3_raw_data: "type_defs.UpdateVpcOriginRequestTypeDef" = dataclasses.field()

    VpcOriginEndpointConfig = field("VpcOriginEndpointConfig")
    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVpcOriginRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVpcOriginRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TenantConfigOutput:
    boto3_raw_data: "type_defs.TenantConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def ParameterDefinitions(self):  # pragma: no cover
        return ParameterDefinition.make_many(
            self.boto3_raw_data["ParameterDefinitions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TenantConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TenantConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TenantConfig:
    boto3_raw_data: "type_defs.TenantConfigTypeDef" = dataclasses.field()

    @cached_property
    def ParameterDefinitions(self):  # pragma: no cover
        return ParameterDefinition.make_many(
            self.boto3_raw_data["ParameterDefinitions"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TenantConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TenantConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldLevelEncryptionConfigOutput:
    boto3_raw_data: "type_defs.FieldLevelEncryptionConfigOutputTypeDef" = (
        dataclasses.field()
    )

    CallerReference = field("CallerReference")
    Comment = field("Comment")

    @cached_property
    def QueryArgProfileConfig(self):  # pragma: no cover
        return QueryArgProfileConfigOutput.make_one(
            self.boto3_raw_data["QueryArgProfileConfig"]
        )

    @cached_property
    def ContentTypeProfileConfig(self):  # pragma: no cover
        return ContentTypeProfileConfigOutput.make_one(
            self.boto3_raw_data["ContentTypeProfileConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FieldLevelEncryptionConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldLevelEncryptionConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldLevelEncryptionSummary:
    boto3_raw_data: "type_defs.FieldLevelEncryptionSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    LastModifiedTime = field("LastModifiedTime")
    Comment = field("Comment")

    @cached_property
    def QueryArgProfileConfig(self):  # pragma: no cover
        return QueryArgProfileConfigOutput.make_one(
            self.boto3_raw_data["QueryArgProfileConfig"]
        )

    @cached_property
    def ContentTypeProfileConfig(self):  # pragma: no cover
        return ContentTypeProfileConfigOutput.make_one(
            self.boto3_raw_data["ContentTypeProfileConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FieldLevelEncryptionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldLevelEncryptionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldLevelEncryptionConfig:
    boto3_raw_data: "type_defs.FieldLevelEncryptionConfigTypeDef" = dataclasses.field()

    CallerReference = field("CallerReference")
    Comment = field("Comment")

    @cached_property
    def QueryArgProfileConfig(self):  # pragma: no cover
        return QueryArgProfileConfig.make_one(
            self.boto3_raw_data["QueryArgProfileConfig"]
        )

    @cached_property
    def ContentTypeProfileConfig(self):  # pragma: no cover
        return ContentTypeProfileConfig.make_one(
            self.boto3_raw_data["ContentTypeProfileConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FieldLevelEncryptionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldLevelEncryptionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResponseHeadersPolicyConfigResult:
    boto3_raw_data: "type_defs.GetResponseHeadersPolicyConfigResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResponseHeadersPolicyConfig(self):  # pragma: no cover
        return ResponseHeadersPolicyConfigOutput.make_one(
            self.boto3_raw_data["ResponseHeadersPolicyConfig"]
        )

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetResponseHeadersPolicyConfigResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResponseHeadersPolicyConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicy:
    boto3_raw_data: "type_defs.ResponseHeadersPolicyTypeDef" = dataclasses.field()

    Id = field("Id")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def ResponseHeadersPolicyConfig(self):  # pragma: no cover
        return ResponseHeadersPolicyConfigOutput.make_one(
            self.boto3_raw_data["ResponseHeadersPolicyConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResponseHeadersPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseHeadersPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamingDistributionsResult:
    boto3_raw_data: "type_defs.ListStreamingDistributionsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StreamingDistributionList(self):  # pragma: no cover
        return StreamingDistributionList.make_one(
            self.boto3_raw_data["StreamingDistributionList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListStreamingDistributionsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamingDistributionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectionGroupResult:
    boto3_raw_data: "type_defs.CreateConnectionGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def ConnectionGroup(self):  # pragma: no cover
        return ConnectionGroup.make_one(self.boto3_raw_data["ConnectionGroup"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConnectionGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectionGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectionGroupByRoutingEndpointResult:
    boto3_raw_data: "type_defs.GetConnectionGroupByRoutingEndpointResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConnectionGroup(self):  # pragma: no cover
        return ConnectionGroup.make_one(self.boto3_raw_data["ConnectionGroup"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConnectionGroupByRoutingEndpointResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectionGroupByRoutingEndpointResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectionGroupResult:
    boto3_raw_data: "type_defs.GetConnectionGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def ConnectionGroup(self):  # pragma: no cover
        return ConnectionGroup.make_one(self.boto3_raw_data["ConnectionGroup"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectionGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectionGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectionGroupResult:
    boto3_raw_data: "type_defs.UpdateConnectionGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def ConnectionGroup(self):  # pragma: no cover
        return ConnectionGroup.make_one(self.boto3_raw_data["ConnectionGroup"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConnectionGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectionGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDistributionTenantResult:
    boto3_raw_data: "type_defs.CreateDistributionTenantResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DistributionTenant(self):  # pragma: no cover
        return DistributionTenant.make_one(self.boto3_raw_data["DistributionTenant"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDistributionTenantResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDistributionTenantResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDistributionTenantByDomainResult:
    boto3_raw_data: "type_defs.GetDistributionTenantByDomainResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DistributionTenant(self):  # pragma: no cover
        return DistributionTenant.make_one(self.boto3_raw_data["DistributionTenant"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDistributionTenantByDomainResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDistributionTenantByDomainResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDistributionTenantResult:
    boto3_raw_data: "type_defs.GetDistributionTenantResultTypeDef" = dataclasses.field()

    @cached_property
    def DistributionTenant(self):  # pragma: no cover
        return DistributionTenant.make_one(self.boto3_raw_data["DistributionTenant"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDistributionTenantResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDistributionTenantResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDistributionTenantResult:
    boto3_raw_data: "type_defs.UpdateDistributionTenantResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DistributionTenant(self):  # pragma: no cover
        return DistributionTenant.make_one(self.boto3_raw_data["DistributionTenant"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDistributionTenantResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDistributionTenantResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAnycastIpListRequest:
    boto3_raw_data: "type_defs.CreateAnycastIpListRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    IpCount = field("IpCount")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAnycastIpListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAnycastIpListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectionGroupRequest:
    boto3_raw_data: "type_defs.CreateConnectionGroupRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Ipv6Enabled = field("Ipv6Enabled")
    Tags = field("Tags")
    AnycastIpListId = field("AnycastIpListId")
    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConnectionGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectionGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDistributionTenantRequest:
    boto3_raw_data: "type_defs.CreateDistributionTenantRequestTypeDef" = (
        dataclasses.field()
    )

    DistributionId = field("DistributionId")
    Name = field("Name")

    @cached_property
    def Domains(self):  # pragma: no cover
        return DomainItem.make_many(self.boto3_raw_data["Domains"])

    Tags = field("Tags")
    Customizations = field("Customizations")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    ConnectionGroupId = field("ConnectionGroupId")

    @cached_property
    def ManagedCertificateRequest(self):  # pragma: no cover
        return ManagedCertificateRequest.make_one(
            self.boto3_raw_data["ManagedCertificateRequest"]
        )

    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDistributionTenantRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDistributionTenantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVpcOriginRequest:
    boto3_raw_data: "type_defs.CreateVpcOriginRequestTypeDef" = dataclasses.field()

    VpcOriginEndpointConfig = field("VpcOriginEndpointConfig")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVpcOriginRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcOriginRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    Resource = field("Resource")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheBehaviorsOutput:
    boto3_raw_data: "type_defs.CacheBehaviorsOutputTypeDef" = dataclasses.field()

    Quantity = field("Quantity")

    @cached_property
    def Items(self):  # pragma: no cover
        return CacheBehaviorOutput.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CacheBehaviorsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheBehaviorsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ForwardedValues:
    boto3_raw_data: "type_defs.ForwardedValuesTypeDef" = dataclasses.field()

    QueryString = field("QueryString")
    Cookies = field("Cookies")
    Headers = field("Headers")
    QueryStringCacheKeys = field("QueryStringCacheKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ForwardedValuesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ForwardedValuesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CachePolicy:
    boto3_raw_data: "type_defs.CachePolicyTypeDef" = dataclasses.field()

    Id = field("Id")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def CachePolicyConfig(self):  # pragma: no cover
        return CachePolicyConfigOutput.make_one(
            self.boto3_raw_data["CachePolicyConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CachePolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CachePolicyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCachePolicyConfigResult:
    boto3_raw_data: "type_defs.GetCachePolicyConfigResultTypeDef" = dataclasses.field()

    @cached_property
    def CachePolicyConfig(self):  # pragma: no cover
        return CachePolicyConfigOutput.make_one(
            self.boto3_raw_data["CachePolicyConfig"]
        )

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCachePolicyConfigResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCachePolicyConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOriginRequestPolicyResult:
    boto3_raw_data: "type_defs.CreateOriginRequestPolicyResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OriginRequestPolicy(self):  # pragma: no cover
        return OriginRequestPolicy.make_one(self.boto3_raw_data["OriginRequestPolicy"])

    Location = field("Location")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateOriginRequestPolicyResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOriginRequestPolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOriginRequestPolicyResult:
    boto3_raw_data: "type_defs.GetOriginRequestPolicyResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OriginRequestPolicy(self):  # pragma: no cover
        return OriginRequestPolicy.make_one(self.boto3_raw_data["OriginRequestPolicy"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOriginRequestPolicyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOriginRequestPolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginRequestPolicySummary:
    boto3_raw_data: "type_defs.OriginRequestPolicySummaryTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def OriginRequestPolicy(self):  # pragma: no cover
        return OriginRequestPolicy.make_one(self.boto3_raw_data["OriginRequestPolicy"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OriginRequestPolicySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginRequestPolicySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOriginRequestPolicyResult:
    boto3_raw_data: "type_defs.UpdateOriginRequestPolicyResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OriginRequestPolicy(self):  # pragma: no cover
        return OriginRequestPolicy.make_one(self.boto3_raw_data["OriginRequestPolicy"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateOriginRequestPolicyResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOriginRequestPolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOriginRequestPolicyRequest:
    boto3_raw_data: "type_defs.CreateOriginRequestPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    OriginRequestPolicyConfig = field("OriginRequestPolicyConfig")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateOriginRequestPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOriginRequestPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOriginRequestPolicyRequest:
    boto3_raw_data: "type_defs.UpdateOriginRequestPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    OriginRequestPolicyConfig = field("OriginRequestPolicyConfig")
    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateOriginRequestPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOriginRequestPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContinuousDeploymentPolicy:
    boto3_raw_data: "type_defs.ContinuousDeploymentPolicyTypeDef" = dataclasses.field()

    Id = field("Id")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def ContinuousDeploymentPolicyConfig(self):  # pragma: no cover
        return ContinuousDeploymentPolicyConfigOutput.make_one(
            self.boto3_raw_data["ContinuousDeploymentPolicyConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContinuousDeploymentPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContinuousDeploymentPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContinuousDeploymentPolicyConfigResult:
    boto3_raw_data: "type_defs.GetContinuousDeploymentPolicyConfigResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ContinuousDeploymentPolicyConfig(self):  # pragma: no cover
        return ContinuousDeploymentPolicyConfigOutput.make_one(
            self.boto3_raw_data["ContinuousDeploymentPolicyConfig"]
        )

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetContinuousDeploymentPolicyConfigResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContinuousDeploymentPolicyConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldLevelEncryptionProfile:
    boto3_raw_data: "type_defs.FieldLevelEncryptionProfileTypeDef" = dataclasses.field()

    Id = field("Id")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def FieldLevelEncryptionProfileConfig(self):  # pragma: no cover
        return FieldLevelEncryptionProfileConfigOutput.make_one(
            self.boto3_raw_data["FieldLevelEncryptionProfileConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FieldLevelEncryptionProfileTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldLevelEncryptionProfileTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFieldLevelEncryptionProfileConfigResult:
    boto3_raw_data: "type_defs.GetFieldLevelEncryptionProfileConfigResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FieldLevelEncryptionProfileConfig(self):  # pragma: no cover
        return FieldLevelEncryptionProfileConfigOutput.make_one(
            self.boto3_raw_data["FieldLevelEncryptionProfileConfig"]
        )

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFieldLevelEncryptionProfileConfigResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFieldLevelEncryptionProfileConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldLevelEncryptionProfileList:
    boto3_raw_data: "type_defs.FieldLevelEncryptionProfileListTypeDef" = (
        dataclasses.field()
    )

    MaxItems = field("MaxItems")
    Quantity = field("Quantity")
    NextMarker = field("NextMarker")

    @cached_property
    def Items(self):  # pragma: no cover
        return FieldLevelEncryptionProfileSummary.make_many(
            self.boto3_raw_data["Items"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FieldLevelEncryptionProfileListTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldLevelEncryptionProfileListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRealtimeLogConfigsResult:
    boto3_raw_data: "type_defs.ListRealtimeLogConfigsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RealtimeLogConfigs(self):  # pragma: no cover
        return RealtimeLogConfigs.make_one(self.boto3_raw_data["RealtimeLogConfigs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRealtimeLogConfigsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRealtimeLogConfigsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeyGroupsResult:
    boto3_raw_data: "type_defs.ListKeyGroupsResultTypeDef" = dataclasses.field()

    @cached_property
    def KeyGroupList(self):  # pragma: no cover
        return KeyGroupList.make_one(self.boto3_raw_data["KeyGroupList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKeyGroupsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeyGroupsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStreamingDistributionResult:
    boto3_raw_data: "type_defs.CreateStreamingDistributionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StreamingDistribution(self):  # pragma: no cover
        return StreamingDistribution.make_one(
            self.boto3_raw_data["StreamingDistribution"]
        )

    Location = field("Location")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateStreamingDistributionResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStreamingDistributionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStreamingDistributionWithTagsResult:
    boto3_raw_data: "type_defs.CreateStreamingDistributionWithTagsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StreamingDistribution(self):  # pragma: no cover
        return StreamingDistribution.make_one(
            self.boto3_raw_data["StreamingDistribution"]
        )

    Location = field("Location")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateStreamingDistributionWithTagsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStreamingDistributionWithTagsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStreamingDistributionResult:
    boto3_raw_data: "type_defs.GetStreamingDistributionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StreamingDistribution(self):  # pragma: no cover
        return StreamingDistribution.make_one(
            self.boto3_raw_data["StreamingDistribution"]
        )

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetStreamingDistributionResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStreamingDistributionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStreamingDistributionResult:
    boto3_raw_data: "type_defs.UpdateStreamingDistributionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StreamingDistribution(self):  # pragma: no cover
        return StreamingDistribution.make_one(
            self.boto3_raw_data["StreamingDistribution"]
        )

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateStreamingDistributionResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStreamingDistributionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFunctionResult:
    boto3_raw_data: "type_defs.CreateFunctionResultTypeDef" = dataclasses.field()

    @cached_property
    def FunctionSummary(self):  # pragma: no cover
        return FunctionSummary.make_one(self.boto3_raw_data["FunctionSummary"])

    Location = field("Location")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFunctionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFunctionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFunctionResult:
    boto3_raw_data: "type_defs.DescribeFunctionResultTypeDef" = dataclasses.field()

    @cached_property
    def FunctionSummary(self):  # pragma: no cover
        return FunctionSummary.make_one(self.boto3_raw_data["FunctionSummary"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFunctionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFunctionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionList:
    boto3_raw_data: "type_defs.FunctionListTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    Quantity = field("Quantity")
    NextMarker = field("NextMarker")

    @cached_property
    def Items(self):  # pragma: no cover
        return FunctionSummary.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FunctionListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FunctionListTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublishFunctionResult:
    boto3_raw_data: "type_defs.PublishFunctionResultTypeDef" = dataclasses.field()

    @cached_property
    def FunctionSummary(self):  # pragma: no cover
        return FunctionSummary.make_one(self.boto3_raw_data["FunctionSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PublishFunctionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublishFunctionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestResult:
    boto3_raw_data: "type_defs.TestResultTypeDef" = dataclasses.field()

    @cached_property
    def FunctionSummary(self):  # pragma: no cover
        return FunctionSummary.make_one(self.boto3_raw_data["FunctionSummary"])

    ComputeUtilization = field("ComputeUtilization")
    FunctionExecutionLogs = field("FunctionExecutionLogs")
    FunctionErrorMessage = field("FunctionErrorMessage")
    FunctionOutput = field("FunctionOutput")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TestResultTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFunctionResult:
    boto3_raw_data: "type_defs.UpdateFunctionResultTypeDef" = dataclasses.field()

    @cached_property
    def FunctionSummary(self):  # pragma: no cover
        return FunctionSummary.make_one(self.boto3_raw_data["FunctionSummary"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFunctionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFunctionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFunctionRequest:
    boto3_raw_data: "type_defs.CreateFunctionRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    FunctionConfig = field("FunctionConfig")
    FunctionCode = field("FunctionCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFunctionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFunctionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFunctionRequest:
    boto3_raw_data: "type_defs.UpdateFunctionRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    IfMatch = field("IfMatch")
    FunctionConfig = field("FunctionConfig")
    FunctionCode = field("FunctionCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFunctionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFunctionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Origin:
    boto3_raw_data: "type_defs.OriginTypeDef" = dataclasses.field()

    Id = field("Id")
    DomainName = field("DomainName")
    OriginPath = field("OriginPath")
    CustomHeaders = field("CustomHeaders")

    @cached_property
    def S3OriginConfig(self):  # pragma: no cover
        return S3OriginConfig.make_one(self.boto3_raw_data["S3OriginConfig"])

    CustomOriginConfig = field("CustomOriginConfig")

    @cached_property
    def VpcOriginConfig(self):  # pragma: no cover
        return VpcOriginConfig.make_one(self.boto3_raw_data["VpcOriginConfig"])

    ConnectionAttempts = field("ConnectionAttempts")
    ConnectionTimeout = field("ConnectionTimeout")
    ResponseCompletionTimeout = field("ResponseCompletionTimeout")

    @cached_property
    def OriginShield(self):  # pragma: no cover
        return OriginShield.make_one(self.boto3_raw_data["OriginShield"])

    OriginAccessControlId = field("OriginAccessControlId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OriginTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OriginTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldLevelEncryption:
    boto3_raw_data: "type_defs.FieldLevelEncryptionTypeDef" = dataclasses.field()

    Id = field("Id")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def FieldLevelEncryptionConfig(self):  # pragma: no cover
        return FieldLevelEncryptionConfigOutput.make_one(
            self.boto3_raw_data["FieldLevelEncryptionConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FieldLevelEncryptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldLevelEncryptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFieldLevelEncryptionConfigResult:
    boto3_raw_data: "type_defs.GetFieldLevelEncryptionConfigResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FieldLevelEncryptionConfig(self):  # pragma: no cover
        return FieldLevelEncryptionConfigOutput.make_one(
            self.boto3_raw_data["FieldLevelEncryptionConfig"]
        )

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFieldLevelEncryptionConfigResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFieldLevelEncryptionConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldLevelEncryptionList:
    boto3_raw_data: "type_defs.FieldLevelEncryptionListTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    Quantity = field("Quantity")
    NextMarker = field("NextMarker")

    @cached_property
    def Items(self):  # pragma: no cover
        return FieldLevelEncryptionSummary.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FieldLevelEncryptionListTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldLevelEncryptionListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResponseHeadersPolicyResult:
    boto3_raw_data: "type_defs.CreateResponseHeadersPolicyResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResponseHeadersPolicy(self):  # pragma: no cover
        return ResponseHeadersPolicy.make_one(
            self.boto3_raw_data["ResponseHeadersPolicy"]
        )

    Location = field("Location")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateResponseHeadersPolicyResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResponseHeadersPolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResponseHeadersPolicyResult:
    boto3_raw_data: "type_defs.GetResponseHeadersPolicyResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResponseHeadersPolicy(self):  # pragma: no cover
        return ResponseHeadersPolicy.make_one(
            self.boto3_raw_data["ResponseHeadersPolicy"]
        )

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetResponseHeadersPolicyResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResponseHeadersPolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicySummary:
    boto3_raw_data: "type_defs.ResponseHeadersPolicySummaryTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")

    @cached_property
    def ResponseHeadersPolicy(self):  # pragma: no cover
        return ResponseHeadersPolicy.make_one(
            self.boto3_raw_data["ResponseHeadersPolicy"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResponseHeadersPolicySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseHeadersPolicySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResponseHeadersPolicyResult:
    boto3_raw_data: "type_defs.UpdateResponseHeadersPolicyResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResponseHeadersPolicy(self):  # pragma: no cover
        return ResponseHeadersPolicy.make_one(
            self.boto3_raw_data["ResponseHeadersPolicy"]
        )

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateResponseHeadersPolicyResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResponseHeadersPolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResponseHeadersPolicyRequest:
    boto3_raw_data: "type_defs.CreateResponseHeadersPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    ResponseHeadersPolicyConfig = field("ResponseHeadersPolicyConfig")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateResponseHeadersPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResponseHeadersPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResponseHeadersPolicyRequest:
    boto3_raw_data: "type_defs.UpdateResponseHeadersPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    ResponseHeadersPolicyConfig = field("ResponseHeadersPolicyConfig")
    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateResponseHeadersPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResponseHeadersPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginGroup:
    boto3_raw_data: "type_defs.OriginGroupTypeDef" = dataclasses.field()

    Id = field("Id")
    FailoverCriteria = field("FailoverCriteria")
    Members = field("Members")
    SelectionCriteria = field("SelectionCriteria")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OriginGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OriginGroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStreamingDistributionRequest:
    boto3_raw_data: "type_defs.CreateStreamingDistributionRequestTypeDef" = (
        dataclasses.field()
    )

    StreamingDistributionConfig = field("StreamingDistributionConfig")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateStreamingDistributionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStreamingDistributionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamingDistributionConfigWithTags:
    boto3_raw_data: "type_defs.StreamingDistributionConfigWithTagsTypeDef" = (
        dataclasses.field()
    )

    StreamingDistributionConfig = field("StreamingDistributionConfig")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StreamingDistributionConfigWithTagsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamingDistributionConfigWithTagsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStreamingDistributionRequest:
    boto3_raw_data: "type_defs.UpdateStreamingDistributionRequestTypeDef" = (
        dataclasses.field()
    )

    StreamingDistributionConfig = field("StreamingDistributionConfig")
    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateStreamingDistributionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStreamingDistributionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DistributionConfigOutput:
    boto3_raw_data: "type_defs.DistributionConfigOutputTypeDef" = dataclasses.field()

    CallerReference = field("CallerReference")

    @cached_property
    def Origins(self):  # pragma: no cover
        return OriginsOutput.make_one(self.boto3_raw_data["Origins"])

    @cached_property
    def DefaultCacheBehavior(self):  # pragma: no cover
        return DefaultCacheBehaviorOutput.make_one(
            self.boto3_raw_data["DefaultCacheBehavior"]
        )

    Comment = field("Comment")
    Enabled = field("Enabled")

    @cached_property
    def Aliases(self):  # pragma: no cover
        return AliasesOutput.make_one(self.boto3_raw_data["Aliases"])

    DefaultRootObject = field("DefaultRootObject")

    @cached_property
    def OriginGroups(self):  # pragma: no cover
        return OriginGroupsOutput.make_one(self.boto3_raw_data["OriginGroups"])

    @cached_property
    def CacheBehaviors(self):  # pragma: no cover
        return CacheBehaviorsOutput.make_one(self.boto3_raw_data["CacheBehaviors"])

    @cached_property
    def CustomErrorResponses(self):  # pragma: no cover
        return CustomErrorResponsesOutput.make_one(
            self.boto3_raw_data["CustomErrorResponses"]
        )

    @cached_property
    def Logging(self):  # pragma: no cover
        return LoggingConfig.make_one(self.boto3_raw_data["Logging"])

    PriceClass = field("PriceClass")

    @cached_property
    def ViewerCertificate(self):  # pragma: no cover
        return ViewerCertificate.make_one(self.boto3_raw_data["ViewerCertificate"])

    @cached_property
    def Restrictions(self):  # pragma: no cover
        return RestrictionsOutput.make_one(self.boto3_raw_data["Restrictions"])

    WebACLId = field("WebACLId")
    HttpVersion = field("HttpVersion")
    IsIPV6Enabled = field("IsIPV6Enabled")
    ContinuousDeploymentPolicyId = field("ContinuousDeploymentPolicyId")
    Staging = field("Staging")
    AnycastIpListId = field("AnycastIpListId")

    @cached_property
    def TenantConfig(self):  # pragma: no cover
        return TenantConfigOutput.make_one(self.boto3_raw_data["TenantConfig"])

    ConnectionMode = field("ConnectionMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DistributionConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DistributionConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DistributionSummary:
    boto3_raw_data: "type_defs.DistributionSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    ARN = field("ARN")
    Status = field("Status")
    LastModifiedTime = field("LastModifiedTime")
    DomainName = field("DomainName")

    @cached_property
    def Aliases(self):  # pragma: no cover
        return AliasesOutput.make_one(self.boto3_raw_data["Aliases"])

    @cached_property
    def Origins(self):  # pragma: no cover
        return OriginsOutput.make_one(self.boto3_raw_data["Origins"])

    @cached_property
    def DefaultCacheBehavior(self):  # pragma: no cover
        return DefaultCacheBehaviorOutput.make_one(
            self.boto3_raw_data["DefaultCacheBehavior"]
        )

    @cached_property
    def CacheBehaviors(self):  # pragma: no cover
        return CacheBehaviorsOutput.make_one(self.boto3_raw_data["CacheBehaviors"])

    @cached_property
    def CustomErrorResponses(self):  # pragma: no cover
        return CustomErrorResponsesOutput.make_one(
            self.boto3_raw_data["CustomErrorResponses"]
        )

    Comment = field("Comment")
    PriceClass = field("PriceClass")
    Enabled = field("Enabled")

    @cached_property
    def ViewerCertificate(self):  # pragma: no cover
        return ViewerCertificate.make_one(self.boto3_raw_data["ViewerCertificate"])

    @cached_property
    def Restrictions(self):  # pragma: no cover
        return RestrictionsOutput.make_one(self.boto3_raw_data["Restrictions"])

    WebACLId = field("WebACLId")
    HttpVersion = field("HttpVersion")
    IsIPV6Enabled = field("IsIPV6Enabled")
    Staging = field("Staging")
    ETag = field("ETag")

    @cached_property
    def OriginGroups(self):  # pragma: no cover
        return OriginGroupsOutput.make_one(self.boto3_raw_data["OriginGroups"])

    @cached_property
    def AliasICPRecordals(self):  # pragma: no cover
        return AliasICPRecordal.make_many(self.boto3_raw_data["AliasICPRecordals"])

    ConnectionMode = field("ConnectionMode")
    AnycastIpListId = field("AnycastIpListId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DistributionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DistributionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CachePolicySummary:
    boto3_raw_data: "type_defs.CachePolicySummaryTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def CachePolicy(self):  # pragma: no cover
        return CachePolicy.make_one(self.boto3_raw_data["CachePolicy"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CachePolicySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CachePolicySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCachePolicyResult:
    boto3_raw_data: "type_defs.CreateCachePolicyResultTypeDef" = dataclasses.field()

    @cached_property
    def CachePolicy(self):  # pragma: no cover
        return CachePolicy.make_one(self.boto3_raw_data["CachePolicy"])

    Location = field("Location")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCachePolicyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCachePolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCachePolicyResult:
    boto3_raw_data: "type_defs.GetCachePolicyResultTypeDef" = dataclasses.field()

    @cached_property
    def CachePolicy(self):  # pragma: no cover
        return CachePolicy.make_one(self.boto3_raw_data["CachePolicy"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCachePolicyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCachePolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCachePolicyResult:
    boto3_raw_data: "type_defs.UpdateCachePolicyResultTypeDef" = dataclasses.field()

    @cached_property
    def CachePolicy(self):  # pragma: no cover
        return CachePolicy.make_one(self.boto3_raw_data["CachePolicy"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCachePolicyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCachePolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginRequestPolicyList:
    boto3_raw_data: "type_defs.OriginRequestPolicyListTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    Quantity = field("Quantity")
    NextMarker = field("NextMarker")

    @cached_property
    def Items(self):  # pragma: no cover
        return OriginRequestPolicySummary.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OriginRequestPolicyListTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginRequestPolicyListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCachePolicyRequest:
    boto3_raw_data: "type_defs.CreateCachePolicyRequestTypeDef" = dataclasses.field()

    CachePolicyConfig = field("CachePolicyConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCachePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCachePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCachePolicyRequest:
    boto3_raw_data: "type_defs.UpdateCachePolicyRequestTypeDef" = dataclasses.field()

    CachePolicyConfig = field("CachePolicyConfig")
    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCachePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCachePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContinuousDeploymentPolicySummary:
    boto3_raw_data: "type_defs.ContinuousDeploymentPolicySummaryTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ContinuousDeploymentPolicy(self):  # pragma: no cover
        return ContinuousDeploymentPolicy.make_one(
            self.boto3_raw_data["ContinuousDeploymentPolicy"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ContinuousDeploymentPolicySummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContinuousDeploymentPolicySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContinuousDeploymentPolicyResult:
    boto3_raw_data: "type_defs.CreateContinuousDeploymentPolicyResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ContinuousDeploymentPolicy(self):  # pragma: no cover
        return ContinuousDeploymentPolicy.make_one(
            self.boto3_raw_data["ContinuousDeploymentPolicy"]
        )

    Location = field("Location")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateContinuousDeploymentPolicyResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContinuousDeploymentPolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContinuousDeploymentPolicyResult:
    boto3_raw_data: "type_defs.GetContinuousDeploymentPolicyResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ContinuousDeploymentPolicy(self):  # pragma: no cover
        return ContinuousDeploymentPolicy.make_one(
            self.boto3_raw_data["ContinuousDeploymentPolicy"]
        )

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetContinuousDeploymentPolicyResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContinuousDeploymentPolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContinuousDeploymentPolicyResult:
    boto3_raw_data: "type_defs.UpdateContinuousDeploymentPolicyResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ContinuousDeploymentPolicy(self):  # pragma: no cover
        return ContinuousDeploymentPolicy.make_one(
            self.boto3_raw_data["ContinuousDeploymentPolicy"]
        )

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateContinuousDeploymentPolicyResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContinuousDeploymentPolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContinuousDeploymentPolicyRequest:
    boto3_raw_data: "type_defs.CreateContinuousDeploymentPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    ContinuousDeploymentPolicyConfig = field("ContinuousDeploymentPolicyConfig")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateContinuousDeploymentPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContinuousDeploymentPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContinuousDeploymentPolicyRequest:
    boto3_raw_data: "type_defs.UpdateContinuousDeploymentPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    ContinuousDeploymentPolicyConfig = field("ContinuousDeploymentPolicyConfig")
    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateContinuousDeploymentPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContinuousDeploymentPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFieldLevelEncryptionProfileResult:
    boto3_raw_data: "type_defs.CreateFieldLevelEncryptionProfileResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FieldLevelEncryptionProfile(self):  # pragma: no cover
        return FieldLevelEncryptionProfile.make_one(
            self.boto3_raw_data["FieldLevelEncryptionProfile"]
        )

    Location = field("Location")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateFieldLevelEncryptionProfileResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFieldLevelEncryptionProfileResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFieldLevelEncryptionProfileResult:
    boto3_raw_data: "type_defs.GetFieldLevelEncryptionProfileResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FieldLevelEncryptionProfile(self):  # pragma: no cover
        return FieldLevelEncryptionProfile.make_one(
            self.boto3_raw_data["FieldLevelEncryptionProfile"]
        )

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFieldLevelEncryptionProfileResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFieldLevelEncryptionProfileResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFieldLevelEncryptionProfileResult:
    boto3_raw_data: "type_defs.UpdateFieldLevelEncryptionProfileResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FieldLevelEncryptionProfile(self):  # pragma: no cover
        return FieldLevelEncryptionProfile.make_one(
            self.boto3_raw_data["FieldLevelEncryptionProfile"]
        )

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFieldLevelEncryptionProfileResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFieldLevelEncryptionProfileResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFieldLevelEncryptionProfilesResult:
    boto3_raw_data: "type_defs.ListFieldLevelEncryptionProfilesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FieldLevelEncryptionProfileList(self):  # pragma: no cover
        return FieldLevelEncryptionProfileList.make_one(
            self.boto3_raw_data["FieldLevelEncryptionProfileList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFieldLevelEncryptionProfilesResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFieldLevelEncryptionProfilesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFieldLevelEncryptionProfileRequest:
    boto3_raw_data: "type_defs.CreateFieldLevelEncryptionProfileRequestTypeDef" = (
        dataclasses.field()
    )

    FieldLevelEncryptionProfileConfig = field("FieldLevelEncryptionProfileConfig")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateFieldLevelEncryptionProfileRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFieldLevelEncryptionProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFieldLevelEncryptionProfileRequest:
    boto3_raw_data: "type_defs.UpdateFieldLevelEncryptionProfileRequestTypeDef" = (
        dataclasses.field()
    )

    FieldLevelEncryptionProfileConfig = field("FieldLevelEncryptionProfileConfig")
    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFieldLevelEncryptionProfileRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFieldLevelEncryptionProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFunctionsResult:
    boto3_raw_data: "type_defs.ListFunctionsResultTypeDef" = dataclasses.field()

    @cached_property
    def FunctionList(self):  # pragma: no cover
        return FunctionList.make_one(self.boto3_raw_data["FunctionList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFunctionsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFunctionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestFunctionResult:
    boto3_raw_data: "type_defs.TestFunctionResultTypeDef" = dataclasses.field()

    @cached_property
    def TestResult(self):  # pragma: no cover
        return TestResult.make_one(self.boto3_raw_data["TestResult"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestFunctionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestFunctionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFieldLevelEncryptionConfigResult:
    boto3_raw_data: "type_defs.CreateFieldLevelEncryptionConfigResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FieldLevelEncryption(self):  # pragma: no cover
        return FieldLevelEncryption.make_one(
            self.boto3_raw_data["FieldLevelEncryption"]
        )

    Location = field("Location")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateFieldLevelEncryptionConfigResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFieldLevelEncryptionConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFieldLevelEncryptionResult:
    boto3_raw_data: "type_defs.GetFieldLevelEncryptionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FieldLevelEncryption(self):  # pragma: no cover
        return FieldLevelEncryption.make_one(
            self.boto3_raw_data["FieldLevelEncryption"]
        )

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetFieldLevelEncryptionResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFieldLevelEncryptionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFieldLevelEncryptionConfigResult:
    boto3_raw_data: "type_defs.UpdateFieldLevelEncryptionConfigResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FieldLevelEncryption(self):  # pragma: no cover
        return FieldLevelEncryption.make_one(
            self.boto3_raw_data["FieldLevelEncryption"]
        )

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFieldLevelEncryptionConfigResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFieldLevelEncryptionConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFieldLevelEncryptionConfigsResult:
    boto3_raw_data: "type_defs.ListFieldLevelEncryptionConfigsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FieldLevelEncryptionList(self):  # pragma: no cover
        return FieldLevelEncryptionList.make_one(
            self.boto3_raw_data["FieldLevelEncryptionList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFieldLevelEncryptionConfigsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFieldLevelEncryptionConfigsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFieldLevelEncryptionConfigRequest:
    boto3_raw_data: "type_defs.CreateFieldLevelEncryptionConfigRequestTypeDef" = (
        dataclasses.field()
    )

    FieldLevelEncryptionConfig = field("FieldLevelEncryptionConfig")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateFieldLevelEncryptionConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFieldLevelEncryptionConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFieldLevelEncryptionConfigRequest:
    boto3_raw_data: "type_defs.UpdateFieldLevelEncryptionConfigRequestTypeDef" = (
        dataclasses.field()
    )

    FieldLevelEncryptionConfig = field("FieldLevelEncryptionConfig")
    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFieldLevelEncryptionConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFieldLevelEncryptionConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseHeadersPolicyList:
    boto3_raw_data: "type_defs.ResponseHeadersPolicyListTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    Quantity = field("Quantity")
    NextMarker = field("NextMarker")

    @cached_property
    def Items(self):  # pragma: no cover
        return ResponseHeadersPolicySummary.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResponseHeadersPolicyListTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseHeadersPolicyListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStreamingDistributionWithTagsRequest:
    boto3_raw_data: "type_defs.CreateStreamingDistributionWithTagsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StreamingDistributionConfigWithTags(self):  # pragma: no cover
        return StreamingDistributionConfigWithTags.make_one(
            self.boto3_raw_data["StreamingDistributionConfigWithTags"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateStreamingDistributionWithTagsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStreamingDistributionWithTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Distribution:
    boto3_raw_data: "type_defs.DistributionTypeDef" = dataclasses.field()

    Id = field("Id")
    ARN = field("ARN")
    Status = field("Status")
    LastModifiedTime = field("LastModifiedTime")
    InProgressInvalidationBatches = field("InProgressInvalidationBatches")
    DomainName = field("DomainName")

    @cached_property
    def DistributionConfig(self):  # pragma: no cover
        return DistributionConfigOutput.make_one(
            self.boto3_raw_data["DistributionConfig"]
        )

    @cached_property
    def ActiveTrustedSigners(self):  # pragma: no cover
        return ActiveTrustedSigners.make_one(
            self.boto3_raw_data["ActiveTrustedSigners"]
        )

    @cached_property
    def ActiveTrustedKeyGroups(self):  # pragma: no cover
        return ActiveTrustedKeyGroups.make_one(
            self.boto3_raw_data["ActiveTrustedKeyGroups"]
        )

    @cached_property
    def AliasICPRecordals(self):  # pragma: no cover
        return AliasICPRecordal.make_many(self.boto3_raw_data["AliasICPRecordals"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DistributionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DistributionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDistributionConfigResult:
    boto3_raw_data: "type_defs.GetDistributionConfigResultTypeDef" = dataclasses.field()

    @cached_property
    def DistributionConfig(self):  # pragma: no cover
        return DistributionConfigOutput.make_one(
            self.boto3_raw_data["DistributionConfig"]
        )

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDistributionConfigResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDistributionConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DistributionList:
    boto3_raw_data: "type_defs.DistributionListTypeDef" = dataclasses.field()

    Marker = field("Marker")
    MaxItems = field("MaxItems")
    IsTruncated = field("IsTruncated")
    Quantity = field("Quantity")
    NextMarker = field("NextMarker")

    @cached_property
    def Items(self):  # pragma: no cover
        return DistributionSummary.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DistributionListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DistributionListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheBehavior:
    boto3_raw_data: "type_defs.CacheBehaviorTypeDef" = dataclasses.field()

    PathPattern = field("PathPattern")
    TargetOriginId = field("TargetOriginId")
    ViewerProtocolPolicy = field("ViewerProtocolPolicy")
    TrustedSigners = field("TrustedSigners")
    TrustedKeyGroups = field("TrustedKeyGroups")
    AllowedMethods = field("AllowedMethods")
    SmoothStreaming = field("SmoothStreaming")
    Compress = field("Compress")
    LambdaFunctionAssociations = field("LambdaFunctionAssociations")
    FunctionAssociations = field("FunctionAssociations")
    FieldLevelEncryptionId = field("FieldLevelEncryptionId")
    RealtimeLogConfigArn = field("RealtimeLogConfigArn")
    CachePolicyId = field("CachePolicyId")
    OriginRequestPolicyId = field("OriginRequestPolicyId")
    ResponseHeadersPolicyId = field("ResponseHeadersPolicyId")

    @cached_property
    def GrpcConfig(self):  # pragma: no cover
        return GrpcConfig.make_one(self.boto3_raw_data["GrpcConfig"])

    ForwardedValues = field("ForwardedValues")
    MinTTL = field("MinTTL")
    DefaultTTL = field("DefaultTTL")
    MaxTTL = field("MaxTTL")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CacheBehaviorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CacheBehaviorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultCacheBehavior:
    boto3_raw_data: "type_defs.DefaultCacheBehaviorTypeDef" = dataclasses.field()

    TargetOriginId = field("TargetOriginId")
    ViewerProtocolPolicy = field("ViewerProtocolPolicy")
    TrustedSigners = field("TrustedSigners")
    TrustedKeyGroups = field("TrustedKeyGroups")
    AllowedMethods = field("AllowedMethods")
    SmoothStreaming = field("SmoothStreaming")
    Compress = field("Compress")
    LambdaFunctionAssociations = field("LambdaFunctionAssociations")
    FunctionAssociations = field("FunctionAssociations")
    FieldLevelEncryptionId = field("FieldLevelEncryptionId")
    RealtimeLogConfigArn = field("RealtimeLogConfigArn")
    CachePolicyId = field("CachePolicyId")
    OriginRequestPolicyId = field("OriginRequestPolicyId")
    ResponseHeadersPolicyId = field("ResponseHeadersPolicyId")

    @cached_property
    def GrpcConfig(self):  # pragma: no cover
        return GrpcConfig.make_one(self.boto3_raw_data["GrpcConfig"])

    ForwardedValues = field("ForwardedValues")
    MinTTL = field("MinTTL")
    DefaultTTL = field("DefaultTTL")
    MaxTTL = field("MaxTTL")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DefaultCacheBehaviorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultCacheBehaviorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CachePolicyList:
    boto3_raw_data: "type_defs.CachePolicyListTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    Quantity = field("Quantity")
    NextMarker = field("NextMarker")

    @cached_property
    def Items(self):  # pragma: no cover
        return CachePolicySummary.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CachePolicyListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CachePolicyListTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOriginRequestPoliciesResult:
    boto3_raw_data: "type_defs.ListOriginRequestPoliciesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OriginRequestPolicyList(self):  # pragma: no cover
        return OriginRequestPolicyList.make_one(
            self.boto3_raw_data["OriginRequestPolicyList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOriginRequestPoliciesResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOriginRequestPoliciesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContinuousDeploymentPolicyList:
    boto3_raw_data: "type_defs.ContinuousDeploymentPolicyListTypeDef" = (
        dataclasses.field()
    )

    MaxItems = field("MaxItems")
    Quantity = field("Quantity")
    NextMarker = field("NextMarker")

    @cached_property
    def Items(self):  # pragma: no cover
        return ContinuousDeploymentPolicySummary.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ContinuousDeploymentPolicyListTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContinuousDeploymentPolicyListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Origins:
    boto3_raw_data: "type_defs.OriginsTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OriginsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OriginsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResponseHeadersPoliciesResult:
    boto3_raw_data: "type_defs.ListResponseHeadersPoliciesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResponseHeadersPolicyList(self):  # pragma: no cover
        return ResponseHeadersPolicyList.make_one(
            self.boto3_raw_data["ResponseHeadersPolicyList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResponseHeadersPoliciesResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResponseHeadersPoliciesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginGroups:
    boto3_raw_data: "type_defs.OriginGroupsTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OriginGroupsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OriginGroupsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyDistributionResult:
    boto3_raw_data: "type_defs.CopyDistributionResultTypeDef" = dataclasses.field()

    @cached_property
    def Distribution(self):  # pragma: no cover
        return Distribution.make_one(self.boto3_raw_data["Distribution"])

    Location = field("Location")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyDistributionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyDistributionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDistributionResult:
    boto3_raw_data: "type_defs.CreateDistributionResultTypeDef" = dataclasses.field()

    @cached_property
    def Distribution(self):  # pragma: no cover
        return Distribution.make_one(self.boto3_raw_data["Distribution"])

    Location = field("Location")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDistributionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDistributionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDistributionWithTagsResult:
    boto3_raw_data: "type_defs.CreateDistributionWithTagsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Distribution(self):  # pragma: no cover
        return Distribution.make_one(self.boto3_raw_data["Distribution"])

    Location = field("Location")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDistributionWithTagsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDistributionWithTagsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDistributionResult:
    boto3_raw_data: "type_defs.GetDistributionResultTypeDef" = dataclasses.field()

    @cached_property
    def Distribution(self):  # pragma: no cover
        return Distribution.make_one(self.boto3_raw_data["Distribution"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDistributionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDistributionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDistributionResult:
    boto3_raw_data: "type_defs.UpdateDistributionResultTypeDef" = dataclasses.field()

    @cached_property
    def Distribution(self):  # pragma: no cover
        return Distribution.make_one(self.boto3_raw_data["Distribution"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDistributionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDistributionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDistributionWithStagingConfigResult:
    boto3_raw_data: "type_defs.UpdateDistributionWithStagingConfigResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Distribution(self):  # pragma: no cover
        return Distribution.make_one(self.boto3_raw_data["Distribution"])

    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDistributionWithStagingConfigResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDistributionWithStagingConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionsByAnycastIpListIdResult:
    boto3_raw_data: "type_defs.ListDistributionsByAnycastIpListIdResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DistributionList(self):  # pragma: no cover
        return DistributionList.make_one(self.boto3_raw_data["DistributionList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionsByAnycastIpListIdResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionsByAnycastIpListIdResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionsByConnectionModeResult:
    boto3_raw_data: "type_defs.ListDistributionsByConnectionModeResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DistributionList(self):  # pragma: no cover
        return DistributionList.make_one(self.boto3_raw_data["DistributionList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionsByConnectionModeResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionsByConnectionModeResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionsByRealtimeLogConfigResult:
    boto3_raw_data: "type_defs.ListDistributionsByRealtimeLogConfigResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DistributionList(self):  # pragma: no cover
        return DistributionList.make_one(self.boto3_raw_data["DistributionList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionsByRealtimeLogConfigResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionsByRealtimeLogConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionsByWebACLIdResult:
    boto3_raw_data: "type_defs.ListDistributionsByWebACLIdResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DistributionList(self):  # pragma: no cover
        return DistributionList.make_one(self.boto3_raw_data["DistributionList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDistributionsByWebACLIdResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionsByWebACLIdResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDistributionsResult:
    boto3_raw_data: "type_defs.ListDistributionsResultTypeDef" = dataclasses.field()

    @cached_property
    def DistributionList(self):  # pragma: no cover
        return DistributionList.make_one(self.boto3_raw_data["DistributionList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDistributionsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDistributionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCachePoliciesResult:
    boto3_raw_data: "type_defs.ListCachePoliciesResultTypeDef" = dataclasses.field()

    @cached_property
    def CachePolicyList(self):  # pragma: no cover
        return CachePolicyList.make_one(self.boto3_raw_data["CachePolicyList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCachePoliciesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCachePoliciesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContinuousDeploymentPoliciesResult:
    boto3_raw_data: "type_defs.ListContinuousDeploymentPoliciesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ContinuousDeploymentPolicyList(self):  # pragma: no cover
        return ContinuousDeploymentPolicyList.make_one(
            self.boto3_raw_data["ContinuousDeploymentPolicyList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListContinuousDeploymentPoliciesResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContinuousDeploymentPoliciesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheBehaviors:
    boto3_raw_data: "type_defs.CacheBehaviorsTypeDef" = dataclasses.field()

    Quantity = field("Quantity")
    Items = field("Items")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CacheBehaviorsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CacheBehaviorsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DistributionConfig:
    boto3_raw_data: "type_defs.DistributionConfigTypeDef" = dataclasses.field()

    CallerReference = field("CallerReference")
    Origins = field("Origins")
    DefaultCacheBehavior = field("DefaultCacheBehavior")
    Comment = field("Comment")
    Enabled = field("Enabled")
    Aliases = field("Aliases")
    DefaultRootObject = field("DefaultRootObject")
    OriginGroups = field("OriginGroups")
    CacheBehaviors = field("CacheBehaviors")
    CustomErrorResponses = field("CustomErrorResponses")

    @cached_property
    def Logging(self):  # pragma: no cover
        return LoggingConfig.make_one(self.boto3_raw_data["Logging"])

    PriceClass = field("PriceClass")

    @cached_property
    def ViewerCertificate(self):  # pragma: no cover
        return ViewerCertificate.make_one(self.boto3_raw_data["ViewerCertificate"])

    Restrictions = field("Restrictions")
    WebACLId = field("WebACLId")
    HttpVersion = field("HttpVersion")
    IsIPV6Enabled = field("IsIPV6Enabled")
    ContinuousDeploymentPolicyId = field("ContinuousDeploymentPolicyId")
    Staging = field("Staging")
    AnycastIpListId = field("AnycastIpListId")
    TenantConfig = field("TenantConfig")
    ConnectionMode = field("ConnectionMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DistributionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DistributionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDistributionRequest:
    boto3_raw_data: "type_defs.CreateDistributionRequestTypeDef" = dataclasses.field()

    DistributionConfig = field("DistributionConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDistributionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDistributionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DistributionConfigWithTags:
    boto3_raw_data: "type_defs.DistributionConfigWithTagsTypeDef" = dataclasses.field()

    DistributionConfig = field("DistributionConfig")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DistributionConfigWithTagsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DistributionConfigWithTagsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDistributionRequest:
    boto3_raw_data: "type_defs.UpdateDistributionRequestTypeDef" = dataclasses.field()

    DistributionConfig = field("DistributionConfig")
    Id = field("Id")
    IfMatch = field("IfMatch")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDistributionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDistributionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDistributionWithTagsRequest:
    boto3_raw_data: "type_defs.CreateDistributionWithTagsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DistributionConfigWithTags(self):  # pragma: no cover
        return DistributionConfigWithTags.make_one(
            self.boto3_raw_data["DistributionConfigWithTags"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDistributionWithTagsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDistributionWithTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
