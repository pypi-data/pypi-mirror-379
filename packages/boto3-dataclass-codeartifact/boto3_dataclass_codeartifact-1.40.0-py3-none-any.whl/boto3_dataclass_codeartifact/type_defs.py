# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_codeartifact import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AssetSummary:
    boto3_raw_data: "type_defs.AssetSummaryTypeDef" = dataclasses.field()

    name = field("name")
    size = field("size")
    hashes = field("hashes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssetSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateExternalConnectionRequest:
    boto3_raw_data: "type_defs.AssociateExternalConnectionRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    repository = field("repository")
    externalConnection = field("externalConnection")
    domainOwner = field("domainOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateExternalConnectionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateExternalConnectionRequestTypeDef"]
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
class AssociatedPackage:
    boto3_raw_data: "type_defs.AssociatedPackageTypeDef" = dataclasses.field()

    format = field("format")
    namespace = field("namespace")
    package = field("package")
    associationType = field("associationType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssociatedPackageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatedPackageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyPackageVersionsRequest:
    boto3_raw_data: "type_defs.CopyPackageVersionsRequestTypeDef" = dataclasses.field()

    domain = field("domain")
    sourceRepository = field("sourceRepository")
    destinationRepository = field("destinationRepository")
    format = field("format")
    package = field("package")
    domainOwner = field("domainOwner")
    namespace = field("namespace")
    versions = field("versions")
    versionRevisions = field("versionRevisions")
    allowOverwrite = field("allowOverwrite")
    includeFromUpstream = field("includeFromUpstream")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyPackageVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyPackageVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageVersionError:
    boto3_raw_data: "type_defs.PackageVersionErrorTypeDef" = dataclasses.field()

    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageVersionErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageVersionErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuccessfulPackageVersionInfo:
    boto3_raw_data: "type_defs.SuccessfulPackageVersionInfoTypeDef" = (
        dataclasses.field()
    )

    revision = field("revision")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuccessfulPackageVersionInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuccessfulPackageVersionInfoTypeDef"]
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

    key = field("key")
    value = field("value")

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
class DomainDescription:
    boto3_raw_data: "type_defs.DomainDescriptionTypeDef" = dataclasses.field()

    name = field("name")
    owner = field("owner")
    arn = field("arn")
    status = field("status")
    createdTime = field("createdTime")
    encryptionKey = field("encryptionKey")
    repositoryCount = field("repositoryCount")
    assetSizeBytes = field("assetSizeBytes")
    s3BucketArn = field("s3BucketArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpstreamRepository:
    boto3_raw_data: "type_defs.UpstreamRepositoryTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpstreamRepositoryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpstreamRepositoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainPermissionsPolicyRequest:
    boto3_raw_data: "type_defs.DeleteDomainPermissionsPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    domainOwner = field("domainOwner")
    policyRevision = field("policyRevision")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDomainPermissionsPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainPermissionsPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourcePolicy:
    boto3_raw_data: "type_defs.ResourcePolicyTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    revision = field("revision")
    document = field("document")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourcePolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourcePolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainRequest:
    boto3_raw_data: "type_defs.DeleteDomainRequestTypeDef" = dataclasses.field()

    domain = field("domain")
    domainOwner = field("domainOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePackageGroupRequest:
    boto3_raw_data: "type_defs.DeletePackageGroupRequestTypeDef" = dataclasses.field()

    domain = field("domain")
    packageGroup = field("packageGroup")
    domainOwner = field("domainOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePackageGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePackageGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePackageRequest:
    boto3_raw_data: "type_defs.DeletePackageRequestTypeDef" = dataclasses.field()

    domain = field("domain")
    repository = field("repository")
    format = field("format")
    package = field("package")
    domainOwner = field("domainOwner")
    namespace = field("namespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePackageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePackageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePackageVersionsRequest:
    boto3_raw_data: "type_defs.DeletePackageVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    repository = field("repository")
    format = field("format")
    package = field("package")
    versions = field("versions")
    domainOwner = field("domainOwner")
    namespace = field("namespace")
    expectedStatus = field("expectedStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePackageVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePackageVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRepositoryPermissionsPolicyRequest:
    boto3_raw_data: "type_defs.DeleteRepositoryPermissionsPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    repository = field("repository")
    domainOwner = field("domainOwner")
    policyRevision = field("policyRevision")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRepositoryPermissionsPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRepositoryPermissionsPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRepositoryRequest:
    boto3_raw_data: "type_defs.DeleteRepositoryRequestTypeDef" = dataclasses.field()

    domain = field("domain")
    repository = field("repository")
    domainOwner = field("domainOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRepositoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRepositoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainRequest:
    boto3_raw_data: "type_defs.DescribeDomainRequestTypeDef" = dataclasses.field()

    domain = field("domain")
    domainOwner = field("domainOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePackageGroupRequest:
    boto3_raw_data: "type_defs.DescribePackageGroupRequestTypeDef" = dataclasses.field()

    domain = field("domain")
    packageGroup = field("packageGroup")
    domainOwner = field("domainOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePackageGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePackageGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePackageRequest:
    boto3_raw_data: "type_defs.DescribePackageRequestTypeDef" = dataclasses.field()

    domain = field("domain")
    repository = field("repository")
    format = field("format")
    package = field("package")
    domainOwner = field("domainOwner")
    namespace = field("namespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePackageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePackageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePackageVersionRequest:
    boto3_raw_data: "type_defs.DescribePackageVersionRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    repository = field("repository")
    format = field("format")
    package = field("package")
    packageVersion = field("packageVersion")
    domainOwner = field("domainOwner")
    namespace = field("namespace")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePackageVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePackageVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRepositoryRequest:
    boto3_raw_data: "type_defs.DescribeRepositoryRequestTypeDef" = dataclasses.field()

    domain = field("domain")
    repository = field("repository")
    domainOwner = field("domainOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRepositoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRepositoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateExternalConnectionRequest:
    boto3_raw_data: "type_defs.DisassociateExternalConnectionRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    repository = field("repository")
    externalConnection = field("externalConnection")
    domainOwner = field("domainOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateExternalConnectionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateExternalConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisposePackageVersionsRequest:
    boto3_raw_data: "type_defs.DisposePackageVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    repository = field("repository")
    format = field("format")
    package = field("package")
    versions = field("versions")
    domainOwner = field("domainOwner")
    namespace = field("namespace")
    versionRevisions = field("versionRevisions")
    expectedStatus = field("expectedStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisposePackageVersionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisposePackageVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainEntryPoint:
    boto3_raw_data: "type_defs.DomainEntryPointTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    externalConnectionName = field("externalConnectionName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainEntryPointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainEntryPointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainSummary:
    boto3_raw_data: "type_defs.DomainSummaryTypeDef" = dataclasses.field()

    name = field("name")
    owner = field("owner")
    arn = field("arn")
    status = field("status")
    createdTime = field("createdTime")
    encryptionKey = field("encryptionKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssociatedPackageGroupRequest:
    boto3_raw_data: "type_defs.GetAssociatedPackageGroupRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    format = field("format")
    package = field("package")
    domainOwner = field("domainOwner")
    namespace = field("namespace")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAssociatedPackageGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssociatedPackageGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAuthorizationTokenRequest:
    boto3_raw_data: "type_defs.GetAuthorizationTokenRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    domainOwner = field("domainOwner")
    durationSeconds = field("durationSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAuthorizationTokenRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAuthorizationTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainPermissionsPolicyRequest:
    boto3_raw_data: "type_defs.GetDomainPermissionsPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    domainOwner = field("domainOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDomainPermissionsPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainPermissionsPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPackageVersionAssetRequest:
    boto3_raw_data: "type_defs.GetPackageVersionAssetRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    repository = field("repository")
    format = field("format")
    package = field("package")
    packageVersion = field("packageVersion")
    asset = field("asset")
    domainOwner = field("domainOwner")
    namespace = field("namespace")
    packageVersionRevision = field("packageVersionRevision")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPackageVersionAssetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPackageVersionAssetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPackageVersionReadmeRequest:
    boto3_raw_data: "type_defs.GetPackageVersionReadmeRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    repository = field("repository")
    format = field("format")
    package = field("package")
    packageVersion = field("packageVersion")
    domainOwner = field("domainOwner")
    namespace = field("namespace")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPackageVersionReadmeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPackageVersionReadmeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRepositoryEndpointRequest:
    boto3_raw_data: "type_defs.GetRepositoryEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    repository = field("repository")
    format = field("format")
    domainOwner = field("domainOwner")
    endpointType = field("endpointType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRepositoryEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRepositoryEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRepositoryPermissionsPolicyRequest:
    boto3_raw_data: "type_defs.GetRepositoryPermissionsPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    repository = field("repository")
    domainOwner = field("domainOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRepositoryPermissionsPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRepositoryPermissionsPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LicenseInfo:
    boto3_raw_data: "type_defs.LicenseInfoTypeDef" = dataclasses.field()

    name = field("name")
    url = field("url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LicenseInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LicenseInfoTypeDef"]]
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
class ListAllowedRepositoriesForGroupRequest:
    boto3_raw_data: "type_defs.ListAllowedRepositoriesForGroupRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    packageGroup = field("packageGroup")
    originRestrictionType = field("originRestrictionType")
    domainOwner = field("domainOwner")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAllowedRepositoriesForGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAllowedRepositoriesForGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociatedPackagesRequest:
    boto3_raw_data: "type_defs.ListAssociatedPackagesRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    packageGroup = field("packageGroup")
    domainOwner = field("domainOwner")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    preview = field("preview")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssociatedPackagesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociatedPackagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainsRequest:
    boto3_raw_data: "type_defs.ListDomainsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackageGroupsRequest:
    boto3_raw_data: "type_defs.ListPackageGroupsRequestTypeDef" = dataclasses.field()

    domain = field("domain")
    domainOwner = field("domainOwner")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    prefix = field("prefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPackageGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackageGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackageVersionAssetsRequest:
    boto3_raw_data: "type_defs.ListPackageVersionAssetsRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    repository = field("repository")
    format = field("format")
    package = field("package")
    packageVersion = field("packageVersion")
    domainOwner = field("domainOwner")
    namespace = field("namespace")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPackageVersionAssetsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackageVersionAssetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackageVersionDependenciesRequest:
    boto3_raw_data: "type_defs.ListPackageVersionDependenciesRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    repository = field("repository")
    format = field("format")
    package = field("package")
    packageVersion = field("packageVersion")
    domainOwner = field("domainOwner")
    namespace = field("namespace")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPackageVersionDependenciesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackageVersionDependenciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageDependency:
    boto3_raw_data: "type_defs.PackageDependencyTypeDef" = dataclasses.field()

    namespace = field("namespace")
    package = field("package")
    dependencyType = field("dependencyType")
    versionRequirement = field("versionRequirement")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PackageDependencyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageDependencyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackageVersionsRequest:
    boto3_raw_data: "type_defs.ListPackageVersionsRequestTypeDef" = dataclasses.field()

    domain = field("domain")
    repository = field("repository")
    format = field("format")
    package = field("package")
    domainOwner = field("domainOwner")
    namespace = field("namespace")
    status = field("status")
    sortBy = field("sortBy")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    originType = field("originType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPackageVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackageVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackagesRequest:
    boto3_raw_data: "type_defs.ListPackagesRequestTypeDef" = dataclasses.field()

    domain = field("domain")
    repository = field("repository")
    domainOwner = field("domainOwner")
    format = field("format")
    namespace = field("namespace")
    packagePrefix = field("packagePrefix")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    publish = field("publish")
    upstream = field("upstream")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPackagesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositoriesInDomainRequest:
    boto3_raw_data: "type_defs.ListRepositoriesInDomainRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    domainOwner = field("domainOwner")
    administratorAccount = field("administratorAccount")
    repositoryPrefix = field("repositoryPrefix")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRepositoriesInDomainRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositoriesInDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositorySummary:
    boto3_raw_data: "type_defs.RepositorySummaryTypeDef" = dataclasses.field()

    name = field("name")
    administratorAccount = field("administratorAccount")
    domainName = field("domainName")
    domainOwner = field("domainOwner")
    arn = field("arn")
    description = field("description")
    createdTime = field("createdTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RepositorySummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositorySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositoriesRequest:
    boto3_raw_data: "type_defs.ListRepositoriesRequestTypeDef" = dataclasses.field()

    repositoryPrefix = field("repositoryPrefix")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRepositoriesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositoriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubPackageGroupsRequest:
    boto3_raw_data: "type_defs.ListSubPackageGroupsRequestTypeDef" = dataclasses.field()

    domain = field("domain")
    packageGroup = field("packageGroup")
    domainOwner = field("domainOwner")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSubPackageGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubPackageGroupsRequestTypeDef"]
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

    resourceArn = field("resourceArn")

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
class PackageGroupAllowedRepository:
    boto3_raw_data: "type_defs.PackageGroupAllowedRepositoryTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    originRestrictionType = field("originRestrictionType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PackageGroupAllowedRepositoryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageGroupAllowedRepositoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageGroupReference:
    boto3_raw_data: "type_defs.PackageGroupReferenceTypeDef" = dataclasses.field()

    arn = field("arn")
    pattern = field("pattern")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageGroupReferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageGroupReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageOriginRestrictions:
    boto3_raw_data: "type_defs.PackageOriginRestrictionsTypeDef" = dataclasses.field()

    publish = field("publish")
    upstream = field("upstream")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageOriginRestrictionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageOriginRestrictionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDomainPermissionsPolicyRequest:
    boto3_raw_data: "type_defs.PutDomainPermissionsPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    policyDocument = field("policyDocument")
    domainOwner = field("domainOwner")
    policyRevision = field("policyRevision")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutDomainPermissionsPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDomainPermissionsPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRepositoryPermissionsPolicyRequest:
    boto3_raw_data: "type_defs.PutRepositoryPermissionsPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    repository = field("repository")
    policyDocument = field("policyDocument")
    domainOwner = field("domainOwner")
    policyRevision = field("policyRevision")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutRepositoryPermissionsPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRepositoryPermissionsPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositoryExternalConnectionInfo:
    boto3_raw_data: "type_defs.RepositoryExternalConnectionInfoTypeDef" = (
        dataclasses.field()
    )

    externalConnectionName = field("externalConnectionName")
    packageFormat = field("packageFormat")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RepositoryExternalConnectionInfoTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositoryExternalConnectionInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpstreamRepositoryInfo:
    boto3_raw_data: "type_defs.UpstreamRepositoryInfoTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpstreamRepositoryInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpstreamRepositoryInfoTypeDef"]
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

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

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
class UpdatePackageGroupRequest:
    boto3_raw_data: "type_defs.UpdatePackageGroupRequestTypeDef" = dataclasses.field()

    domain = field("domain")
    packageGroup = field("packageGroup")
    domainOwner = field("domainOwner")
    contactInfo = field("contactInfo")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePackageGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePackageGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePackageVersionsStatusRequest:
    boto3_raw_data: "type_defs.UpdatePackageVersionsStatusRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    repository = field("repository")
    format = field("format")
    package = field("package")
    versions = field("versions")
    targetStatus = field("targetStatus")
    domainOwner = field("domainOwner")
    namespace = field("namespace")
    versionRevisions = field("versionRevisions")
    expectedStatus = field("expectedStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePackageVersionsStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePackageVersionsStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAuthorizationTokenResult:
    boto3_raw_data: "type_defs.GetAuthorizationTokenResultTypeDef" = dataclasses.field()

    authorizationToken = field("authorizationToken")
    expiration = field("expiration")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAuthorizationTokenResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAuthorizationTokenResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPackageVersionAssetResult:
    boto3_raw_data: "type_defs.GetPackageVersionAssetResultTypeDef" = (
        dataclasses.field()
    )

    asset = field("asset")
    assetName = field("assetName")
    packageVersion = field("packageVersion")
    packageVersionRevision = field("packageVersionRevision")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPackageVersionAssetResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPackageVersionAssetResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPackageVersionReadmeResult:
    boto3_raw_data: "type_defs.GetPackageVersionReadmeResultTypeDef" = (
        dataclasses.field()
    )

    format = field("format")
    namespace = field("namespace")
    package = field("package")
    version = field("version")
    versionRevision = field("versionRevision")
    readme = field("readme")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPackageVersionReadmeResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPackageVersionReadmeResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRepositoryEndpointResult:
    boto3_raw_data: "type_defs.GetRepositoryEndpointResultTypeDef" = dataclasses.field()

    repositoryEndpoint = field("repositoryEndpoint")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRepositoryEndpointResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRepositoryEndpointResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAllowedRepositoriesForGroupResult:
    boto3_raw_data: "type_defs.ListAllowedRepositoriesForGroupResultTypeDef" = (
        dataclasses.field()
    )

    allowedRepositories = field("allowedRepositories")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAllowedRepositoriesForGroupResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAllowedRepositoriesForGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackageVersionAssetsResult:
    boto3_raw_data: "type_defs.ListPackageVersionAssetsResultTypeDef" = (
        dataclasses.field()
    )

    format = field("format")
    namespace = field("namespace")
    package = field("package")
    version = field("version")
    versionRevision = field("versionRevision")

    @cached_property
    def assets(self):  # pragma: no cover
        return AssetSummary.make_many(self.boto3_raw_data["assets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPackageVersionAssetsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackageVersionAssetsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublishPackageVersionResult:
    boto3_raw_data: "type_defs.PublishPackageVersionResultTypeDef" = dataclasses.field()

    format = field("format")
    namespace = field("namespace")
    package = field("package")
    version = field("version")
    versionRevision = field("versionRevision")
    status = field("status")

    @cached_property
    def asset(self):  # pragma: no cover
        return AssetSummary.make_one(self.boto3_raw_data["asset"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PublishPackageVersionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublishPackageVersionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociatedPackagesResult:
    boto3_raw_data: "type_defs.ListAssociatedPackagesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def packages(self):  # pragma: no cover
        return AssociatedPackage.make_many(self.boto3_raw_data["packages"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssociatedPackagesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociatedPackagesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublishPackageVersionRequest:
    boto3_raw_data: "type_defs.PublishPackageVersionRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    repository = field("repository")
    format = field("format")
    package = field("package")
    packageVersion = field("packageVersion")
    assetContent = field("assetContent")
    assetName = field("assetName")
    assetSHA256 = field("assetSHA256")
    domainOwner = field("domainOwner")
    namespace = field("namespace")
    unfinished = field("unfinished")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PublishPackageVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublishPackageVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyPackageVersionsResult:
    boto3_raw_data: "type_defs.CopyPackageVersionsResultTypeDef" = dataclasses.field()

    successfulVersions = field("successfulVersions")
    failedVersions = field("failedVersions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyPackageVersionsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyPackageVersionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePackageVersionsResult:
    boto3_raw_data: "type_defs.DeletePackageVersionsResultTypeDef" = dataclasses.field()

    successfulVersions = field("successfulVersions")
    failedVersions = field("failedVersions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePackageVersionsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePackageVersionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisposePackageVersionsResult:
    boto3_raw_data: "type_defs.DisposePackageVersionsResultTypeDef" = (
        dataclasses.field()
    )

    successfulVersions = field("successfulVersions")
    failedVersions = field("failedVersions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisposePackageVersionsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisposePackageVersionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePackageVersionsStatusResult:
    boto3_raw_data: "type_defs.UpdatePackageVersionsStatusResultTypeDef" = (
        dataclasses.field()
    )

    successfulVersions = field("successfulVersions")
    failedVersions = field("failedVersions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePackageVersionsStatusResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePackageVersionsStatusResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainRequest:
    boto3_raw_data: "type_defs.CreateDomainRequestTypeDef" = dataclasses.field()

    domain = field("domain")
    encryptionKey = field("encryptionKey")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePackageGroupRequest:
    boto3_raw_data: "type_defs.CreatePackageGroupRequestTypeDef" = dataclasses.field()

    domain = field("domain")
    packageGroup = field("packageGroup")
    domainOwner = field("domainOwner")
    contactInfo = field("contactInfo")
    description = field("description")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePackageGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePackageGroupRequestTypeDef"]
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
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class CreateDomainResult:
    boto3_raw_data: "type_defs.CreateDomainResultTypeDef" = dataclasses.field()

    @cached_property
    def domain(self):  # pragma: no cover
        return DomainDescription.make_one(self.boto3_raw_data["domain"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainResult:
    boto3_raw_data: "type_defs.DeleteDomainResultTypeDef" = dataclasses.field()

    @cached_property
    def domain(self):  # pragma: no cover
        return DomainDescription.make_one(self.boto3_raw_data["domain"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDomainResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainResult:
    boto3_raw_data: "type_defs.DescribeDomainResultTypeDef" = dataclasses.field()

    @cached_property
    def domain(self):  # pragma: no cover
        return DomainDescription.make_one(self.boto3_raw_data["domain"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDomainResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRepositoryRequest:
    boto3_raw_data: "type_defs.CreateRepositoryRequestTypeDef" = dataclasses.field()

    domain = field("domain")
    repository = field("repository")
    domainOwner = field("domainOwner")
    description = field("description")

    @cached_property
    def upstreams(self):  # pragma: no cover
        return UpstreamRepository.make_many(self.boto3_raw_data["upstreams"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRepositoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRepositoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRepositoryRequest:
    boto3_raw_data: "type_defs.UpdateRepositoryRequestTypeDef" = dataclasses.field()

    domain = field("domain")
    repository = field("repository")
    domainOwner = field("domainOwner")
    description = field("description")

    @cached_property
    def upstreams(self):  # pragma: no cover
        return UpstreamRepository.make_many(self.boto3_raw_data["upstreams"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRepositoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRepositoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainPermissionsPolicyResult:
    boto3_raw_data: "type_defs.DeleteDomainPermissionsPolicyResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def policy(self):  # pragma: no cover
        return ResourcePolicy.make_one(self.boto3_raw_data["policy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDomainPermissionsPolicyResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainPermissionsPolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRepositoryPermissionsPolicyResult:
    boto3_raw_data: "type_defs.DeleteRepositoryPermissionsPolicyResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def policy(self):  # pragma: no cover
        return ResourcePolicy.make_one(self.boto3_raw_data["policy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRepositoryPermissionsPolicyResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRepositoryPermissionsPolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainPermissionsPolicyResult:
    boto3_raw_data: "type_defs.GetDomainPermissionsPolicyResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def policy(self):  # pragma: no cover
        return ResourcePolicy.make_one(self.boto3_raw_data["policy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDomainPermissionsPolicyResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainPermissionsPolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRepositoryPermissionsPolicyResult:
    boto3_raw_data: "type_defs.GetRepositoryPermissionsPolicyResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def policy(self):  # pragma: no cover
        return ResourcePolicy.make_one(self.boto3_raw_data["policy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRepositoryPermissionsPolicyResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRepositoryPermissionsPolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDomainPermissionsPolicyResult:
    boto3_raw_data: "type_defs.PutDomainPermissionsPolicyResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def policy(self):  # pragma: no cover
        return ResourcePolicy.make_one(self.boto3_raw_data["policy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutDomainPermissionsPolicyResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDomainPermissionsPolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRepositoryPermissionsPolicyResult:
    boto3_raw_data: "type_defs.PutRepositoryPermissionsPolicyResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def policy(self):  # pragma: no cover
        return ResourcePolicy.make_one(self.boto3_raw_data["policy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutRepositoryPermissionsPolicyResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRepositoryPermissionsPolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageVersionOrigin:
    boto3_raw_data: "type_defs.PackageVersionOriginTypeDef" = dataclasses.field()

    @cached_property
    def domainEntryPoint(self):  # pragma: no cover
        return DomainEntryPoint.make_one(self.boto3_raw_data["domainEntryPoint"])

    originType = field("originType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageVersionOriginTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageVersionOriginTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainsResult:
    boto3_raw_data: "type_defs.ListDomainsResultTypeDef" = dataclasses.field()

    @cached_property
    def domains(self):  # pragma: no cover
        return DomainSummary.make_many(self.boto3_raw_data["domains"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListDomainsResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAllowedRepositoriesForGroupRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListAllowedRepositoriesForGroupRequestPaginateTypeDef"
    ) = dataclasses.field()

    domain = field("domain")
    packageGroup = field("packageGroup")
    originRestrictionType = field("originRestrictionType")
    domainOwner = field("domainOwner")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAllowedRepositoriesForGroupRequestPaginateTypeDef"
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
                "type_defs.ListAllowedRepositoriesForGroupRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociatedPackagesRequestPaginate:
    boto3_raw_data: "type_defs.ListAssociatedPackagesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    packageGroup = field("packageGroup")
    domainOwner = field("domainOwner")
    preview = field("preview")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssociatedPackagesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociatedPackagesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainsRequestPaginate:
    boto3_raw_data: "type_defs.ListDomainsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackageGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListPackageGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    domainOwner = field("domainOwner")
    prefix = field("prefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPackageGroupsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackageGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackageVersionAssetsRequestPaginate:
    boto3_raw_data: "type_defs.ListPackageVersionAssetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    repository = field("repository")
    format = field("format")
    package = field("package")
    packageVersion = field("packageVersion")
    domainOwner = field("domainOwner")
    namespace = field("namespace")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPackageVersionAssetsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackageVersionAssetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackageVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListPackageVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    repository = field("repository")
    format = field("format")
    package = field("package")
    domainOwner = field("domainOwner")
    namespace = field("namespace")
    status = field("status")
    sortBy = field("sortBy")
    originType = field("originType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPackageVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackageVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackagesRequestPaginate:
    boto3_raw_data: "type_defs.ListPackagesRequestPaginateTypeDef" = dataclasses.field()

    domain = field("domain")
    repository = field("repository")
    domainOwner = field("domainOwner")
    format = field("format")
    namespace = field("namespace")
    packagePrefix = field("packagePrefix")
    publish = field("publish")
    upstream = field("upstream")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPackagesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackagesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositoriesInDomainRequestPaginate:
    boto3_raw_data: "type_defs.ListRepositoriesInDomainRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    domainOwner = field("domainOwner")
    administratorAccount = field("administratorAccount")
    repositoryPrefix = field("repositoryPrefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRepositoriesInDomainRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositoriesInDomainRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositoriesRequestPaginate:
    boto3_raw_data: "type_defs.ListRepositoriesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    repositoryPrefix = field("repositoryPrefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRepositoriesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositoriesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubPackageGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListSubPackageGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    packageGroup = field("packageGroup")
    domainOwner = field("domainOwner")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSubPackageGroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubPackageGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackageVersionDependenciesResult:
    boto3_raw_data: "type_defs.ListPackageVersionDependenciesResultTypeDef" = (
        dataclasses.field()
    )

    format = field("format")
    namespace = field("namespace")
    package = field("package")
    version = field("version")
    versionRevision = field("versionRevision")

    @cached_property
    def dependencies(self):  # pragma: no cover
        return PackageDependency.make_many(self.boto3_raw_data["dependencies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPackageVersionDependenciesResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackageVersionDependenciesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositoriesInDomainResult:
    boto3_raw_data: "type_defs.ListRepositoriesInDomainResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def repositories(self):  # pragma: no cover
        return RepositorySummary.make_many(self.boto3_raw_data["repositories"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRepositoriesInDomainResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositoriesInDomainResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositoriesResult:
    boto3_raw_data: "type_defs.ListRepositoriesResultTypeDef" = dataclasses.field()

    @cached_property
    def repositories(self):  # pragma: no cover
        return RepositorySummary.make_many(self.boto3_raw_data["repositories"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRepositoriesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositoriesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePackageGroupOriginConfigurationRequest:
    boto3_raw_data: "type_defs.UpdatePackageGroupOriginConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    packageGroup = field("packageGroup")
    domainOwner = field("domainOwner")
    restrictions = field("restrictions")

    @cached_property
    def addAllowedRepositories(self):  # pragma: no cover
        return PackageGroupAllowedRepository.make_many(
            self.boto3_raw_data["addAllowedRepositories"]
        )

    @cached_property
    def removeAllowedRepositories(self):  # pragma: no cover
        return PackageGroupAllowedRepository.make_many(
            self.boto3_raw_data["removeAllowedRepositories"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePackageGroupOriginConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePackageGroupOriginConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageGroupOriginRestriction:
    boto3_raw_data: "type_defs.PackageGroupOriginRestrictionTypeDef" = (
        dataclasses.field()
    )

    mode = field("mode")
    effectiveMode = field("effectiveMode")

    @cached_property
    def inheritedFrom(self):  # pragma: no cover
        return PackageGroupReference.make_one(self.boto3_raw_data["inheritedFrom"])

    repositoriesCount = field("repositoriesCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PackageGroupOriginRestrictionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageGroupOriginRestrictionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageOriginConfiguration:
    boto3_raw_data: "type_defs.PackageOriginConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def restrictions(self):  # pragma: no cover
        return PackageOriginRestrictions.make_one(self.boto3_raw_data["restrictions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageOriginConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageOriginConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPackageOriginConfigurationRequest:
    boto3_raw_data: "type_defs.PutPackageOriginConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    repository = field("repository")
    format = field("format")
    package = field("package")

    @cached_property
    def restrictions(self):  # pragma: no cover
        return PackageOriginRestrictions.make_one(self.boto3_raw_data["restrictions"])

    domainOwner = field("domainOwner")
    namespace = field("namespace")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutPackageOriginConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPackageOriginConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositoryDescription:
    boto3_raw_data: "type_defs.RepositoryDescriptionTypeDef" = dataclasses.field()

    name = field("name")
    administratorAccount = field("administratorAccount")
    domainName = field("domainName")
    domainOwner = field("domainOwner")
    arn = field("arn")
    description = field("description")

    @cached_property
    def upstreams(self):  # pragma: no cover
        return UpstreamRepositoryInfo.make_many(self.boto3_raw_data["upstreams"])

    @cached_property
    def externalConnections(self):  # pragma: no cover
        return RepositoryExternalConnectionInfo.make_many(
            self.boto3_raw_data["externalConnections"]
        )

    createdTime = field("createdTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RepositoryDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositoryDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageVersionDescription:
    boto3_raw_data: "type_defs.PackageVersionDescriptionTypeDef" = dataclasses.field()

    format = field("format")
    namespace = field("namespace")
    packageName = field("packageName")
    displayName = field("displayName")
    version = field("version")
    summary = field("summary")
    homePage = field("homePage")
    sourceCodeRepository = field("sourceCodeRepository")
    publishedTime = field("publishedTime")

    @cached_property
    def licenses(self):  # pragma: no cover
        return LicenseInfo.make_many(self.boto3_raw_data["licenses"])

    revision = field("revision")
    status = field("status")

    @cached_property
    def origin(self):  # pragma: no cover
        return PackageVersionOrigin.make_one(self.boto3_raw_data["origin"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageVersionDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageVersionDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageVersionSummary:
    boto3_raw_data: "type_defs.PackageVersionSummaryTypeDef" = dataclasses.field()

    version = field("version")
    status = field("status")
    revision = field("revision")

    @cached_property
    def origin(self):  # pragma: no cover
        return PackageVersionOrigin.make_one(self.boto3_raw_data["origin"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageVersionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageGroupOriginConfiguration:
    boto3_raw_data: "type_defs.PackageGroupOriginConfigurationTypeDef" = (
        dataclasses.field()
    )

    restrictions = field("restrictions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PackageGroupOriginConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageGroupOriginConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageDescription:
    boto3_raw_data: "type_defs.PackageDescriptionTypeDef" = dataclasses.field()

    format = field("format")
    namespace = field("namespace")
    name = field("name")

    @cached_property
    def originConfiguration(self):  # pragma: no cover
        return PackageOriginConfiguration.make_one(
            self.boto3_raw_data["originConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageSummary:
    boto3_raw_data: "type_defs.PackageSummaryTypeDef" = dataclasses.field()

    format = field("format")
    namespace = field("namespace")
    package = field("package")

    @cached_property
    def originConfiguration(self):  # pragma: no cover
        return PackageOriginConfiguration.make_one(
            self.boto3_raw_data["originConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PackageSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PackageSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPackageOriginConfigurationResult:
    boto3_raw_data: "type_defs.PutPackageOriginConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def originConfiguration(self):  # pragma: no cover
        return PackageOriginConfiguration.make_one(
            self.boto3_raw_data["originConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutPackageOriginConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPackageOriginConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateExternalConnectionResult:
    boto3_raw_data: "type_defs.AssociateExternalConnectionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def repository(self):  # pragma: no cover
        return RepositoryDescription.make_one(self.boto3_raw_data["repository"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateExternalConnectionResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateExternalConnectionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRepositoryResult:
    boto3_raw_data: "type_defs.CreateRepositoryResultTypeDef" = dataclasses.field()

    @cached_property
    def repository(self):  # pragma: no cover
        return RepositoryDescription.make_one(self.boto3_raw_data["repository"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRepositoryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRepositoryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRepositoryResult:
    boto3_raw_data: "type_defs.DeleteRepositoryResultTypeDef" = dataclasses.field()

    @cached_property
    def repository(self):  # pragma: no cover
        return RepositoryDescription.make_one(self.boto3_raw_data["repository"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRepositoryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRepositoryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRepositoryResult:
    boto3_raw_data: "type_defs.DescribeRepositoryResultTypeDef" = dataclasses.field()

    @cached_property
    def repository(self):  # pragma: no cover
        return RepositoryDescription.make_one(self.boto3_raw_data["repository"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRepositoryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRepositoryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateExternalConnectionResult:
    boto3_raw_data: "type_defs.DisassociateExternalConnectionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def repository(self):  # pragma: no cover
        return RepositoryDescription.make_one(self.boto3_raw_data["repository"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateExternalConnectionResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateExternalConnectionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRepositoryResult:
    boto3_raw_data: "type_defs.UpdateRepositoryResultTypeDef" = dataclasses.field()

    @cached_property
    def repository(self):  # pragma: no cover
        return RepositoryDescription.make_one(self.boto3_raw_data["repository"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRepositoryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRepositoryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePackageVersionResult:
    boto3_raw_data: "type_defs.DescribePackageVersionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def packageVersion(self):  # pragma: no cover
        return PackageVersionDescription.make_one(self.boto3_raw_data["packageVersion"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePackageVersionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePackageVersionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackageVersionsResult:
    boto3_raw_data: "type_defs.ListPackageVersionsResultTypeDef" = dataclasses.field()

    defaultDisplayVersion = field("defaultDisplayVersion")
    format = field("format")
    namespace = field("namespace")
    package = field("package")

    @cached_property
    def versions(self):  # pragma: no cover
        return PackageVersionSummary.make_many(self.boto3_raw_data["versions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPackageVersionsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackageVersionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageGroupDescription:
    boto3_raw_data: "type_defs.PackageGroupDescriptionTypeDef" = dataclasses.field()

    arn = field("arn")
    pattern = field("pattern")
    domainName = field("domainName")
    domainOwner = field("domainOwner")
    createdTime = field("createdTime")
    contactInfo = field("contactInfo")
    description = field("description")

    @cached_property
    def originConfiguration(self):  # pragma: no cover
        return PackageGroupOriginConfiguration.make_one(
            self.boto3_raw_data["originConfiguration"]
        )

    @cached_property
    def parent(self):  # pragma: no cover
        return PackageGroupReference.make_one(self.boto3_raw_data["parent"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageGroupDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageGroupDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageGroupSummary:
    boto3_raw_data: "type_defs.PackageGroupSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    pattern = field("pattern")
    domainName = field("domainName")
    domainOwner = field("domainOwner")
    createdTime = field("createdTime")
    contactInfo = field("contactInfo")
    description = field("description")

    @cached_property
    def originConfiguration(self):  # pragma: no cover
        return PackageGroupOriginConfiguration.make_one(
            self.boto3_raw_data["originConfiguration"]
        )

    @cached_property
    def parent(self):  # pragma: no cover
        return PackageGroupReference.make_one(self.boto3_raw_data["parent"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageGroupSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageGroupSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePackageResult:
    boto3_raw_data: "type_defs.DescribePackageResultTypeDef" = dataclasses.field()

    @cached_property
    def package(self):  # pragma: no cover
        return PackageDescription.make_one(self.boto3_raw_data["package"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePackageResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePackageResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePackageResult:
    boto3_raw_data: "type_defs.DeletePackageResultTypeDef" = dataclasses.field()

    @cached_property
    def deletedPackage(self):  # pragma: no cover
        return PackageSummary.make_one(self.boto3_raw_data["deletedPackage"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePackageResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePackageResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackagesResult:
    boto3_raw_data: "type_defs.ListPackagesResultTypeDef" = dataclasses.field()

    @cached_property
    def packages(self):  # pragma: no cover
        return PackageSummary.make_many(self.boto3_raw_data["packages"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPackagesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackagesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePackageGroupResult:
    boto3_raw_data: "type_defs.CreatePackageGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def packageGroup(self):  # pragma: no cover
        return PackageGroupDescription.make_one(self.boto3_raw_data["packageGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePackageGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePackageGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePackageGroupResult:
    boto3_raw_data: "type_defs.DeletePackageGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def packageGroup(self):  # pragma: no cover
        return PackageGroupDescription.make_one(self.boto3_raw_data["packageGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePackageGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePackageGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePackageGroupResult:
    boto3_raw_data: "type_defs.DescribePackageGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def packageGroup(self):  # pragma: no cover
        return PackageGroupDescription.make_one(self.boto3_raw_data["packageGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePackageGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePackageGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssociatedPackageGroupResult:
    boto3_raw_data: "type_defs.GetAssociatedPackageGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def packageGroup(self):  # pragma: no cover
        return PackageGroupDescription.make_one(self.boto3_raw_data["packageGroup"])

    associationType = field("associationType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAssociatedPackageGroupResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssociatedPackageGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePackageGroupOriginConfigurationResult:
    boto3_raw_data: "type_defs.UpdatePackageGroupOriginConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def packageGroup(self):  # pragma: no cover
        return PackageGroupDescription.make_one(self.boto3_raw_data["packageGroup"])

    allowedRepositoryUpdates = field("allowedRepositoryUpdates")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePackageGroupOriginConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePackageGroupOriginConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePackageGroupResult:
    boto3_raw_data: "type_defs.UpdatePackageGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def packageGroup(self):  # pragma: no cover
        return PackageGroupDescription.make_one(self.boto3_raw_data["packageGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePackageGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePackageGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackageGroupsResult:
    boto3_raw_data: "type_defs.ListPackageGroupsResultTypeDef" = dataclasses.field()

    @cached_property
    def packageGroups(self):  # pragma: no cover
        return PackageGroupSummary.make_many(self.boto3_raw_data["packageGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPackageGroupsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackageGroupsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubPackageGroupsResult:
    boto3_raw_data: "type_defs.ListSubPackageGroupsResultTypeDef" = dataclasses.field()

    @cached_property
    def packageGroups(self):  # pragma: no cover
        return PackageGroupSummary.make_many(self.boto3_raw_data["packageGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSubPackageGroupsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubPackageGroupsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
