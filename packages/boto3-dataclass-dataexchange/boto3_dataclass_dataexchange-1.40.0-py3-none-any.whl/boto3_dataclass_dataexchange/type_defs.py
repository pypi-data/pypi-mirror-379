# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_dataexchange import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcceptDataGrantRequest:
    boto3_raw_data: "type_defs.AcceptDataGrantRequestTypeDef" = dataclasses.field()

    DataGrantArn = field("DataGrantArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcceptDataGrantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptDataGrantRequestTypeDef"]
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
class ApiGatewayApiAsset:
    boto3_raw_data: "type_defs.ApiGatewayApiAssetTypeDef" = dataclasses.field()

    ApiDescription = field("ApiDescription")
    ApiEndpoint = field("ApiEndpoint")
    ApiId = field("ApiId")
    ApiKey = field("ApiKey")
    ApiName = field("ApiName")
    ApiSpecificationDownloadUrl = field("ApiSpecificationDownloadUrl")
    ApiSpecificationDownloadUrlExpiresAt = field("ApiSpecificationDownloadUrlExpiresAt")
    ProtocolType = field("ProtocolType")
    Stage = field("Stage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApiGatewayApiAssetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApiGatewayApiAssetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetDestinationEntry:
    boto3_raw_data: "type_defs.AssetDestinationEntryTypeDef" = dataclasses.field()

    AssetId = field("AssetId")
    Bucket = field("Bucket")
    Key = field("Key")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetDestinationEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetDestinationEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftDataShareAsset:
    boto3_raw_data: "type_defs.RedshiftDataShareAssetTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedshiftDataShareAssetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftDataShareAssetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3SnapshotAsset:
    boto3_raw_data: "type_defs.S3SnapshotAssetTypeDef" = dataclasses.field()

    Size = field("Size")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3SnapshotAssetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3SnapshotAssetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetSourceEntry:
    boto3_raw_data: "type_defs.AssetSourceEntryTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetSourceEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetSourceEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoExportRevisionDestinationEntry:
    boto3_raw_data: "type_defs.AutoExportRevisionDestinationEntryTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    KeyPattern = field("KeyPattern")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutoExportRevisionDestinationEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoExportRevisionDestinationEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportServerSideEncryption:
    boto3_raw_data: "type_defs.ExportServerSideEncryptionTypeDef" = dataclasses.field()

    Type = field("Type")
    KmsKeyArn = field("KmsKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportServerSideEncryptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportServerSideEncryptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelJobRequest:
    boto3_raw_data: "type_defs.CancelJobRequestTypeDef" = dataclasses.field()

    JobId = field("JobId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CancelJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataSetRequest:
    boto3_raw_data: "type_defs.CreateDataSetRequestTypeDef" = dataclasses.field()

    AssetType = field("AssetType")
    Description = field("Description")
    Name = field("Name")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginDetails:
    boto3_raw_data: "type_defs.OriginDetailsTypeDef" = dataclasses.field()

    ProductId = field("ProductId")
    DataGrantId = field("DataGrantId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OriginDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OriginDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRevisionRequest:
    boto3_raw_data: "type_defs.CreateRevisionRequestTypeDef" = dataclasses.field()

    DataSetId = field("DataSetId")
    Comment = field("Comment")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRevisionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRevisionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataGrantSummaryEntry:
    boto3_raw_data: "type_defs.DataGrantSummaryEntryTypeDef" = dataclasses.field()

    Name = field("Name")
    SenderPrincipal = field("SenderPrincipal")
    ReceiverPrincipal = field("ReceiverPrincipal")
    AcceptanceState = field("AcceptanceState")
    DataSetId = field("DataSetId")
    SourceDataSetId = field("SourceDataSetId")
    Id = field("Id")
    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")
    AcceptedAt = field("AcceptedAt")
    EndsAt = field("EndsAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataGrantSummaryEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataGrantSummaryEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LFTagOutput:
    boto3_raw_data: "type_defs.LFTagOutputTypeDef" = dataclasses.field()

    TagKey = field("TagKey")
    TagValues = field("TagValues")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LFTagOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LFTagOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LFTag:
    boto3_raw_data: "type_defs.LFTagTypeDef" = dataclasses.field()

    TagKey = field("TagKey")
    TagValues = field("TagValues")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LFTagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LFTagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAssetRequest:
    boto3_raw_data: "type_defs.DeleteAssetRequestTypeDef" = dataclasses.field()

    AssetId = field("AssetId")
    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAssetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataGrantRequest:
    boto3_raw_data: "type_defs.DeleteDataGrantRequestTypeDef" = dataclasses.field()

    DataGrantId = field("DataGrantId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataGrantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataGrantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataSetRequest:
    boto3_raw_data: "type_defs.DeleteDataSetRequestTypeDef" = dataclasses.field()

    DataSetId = field("DataSetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventActionRequest:
    boto3_raw_data: "type_defs.DeleteEventActionRequestTypeDef" = dataclasses.field()

    EventActionId = field("EventActionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEventActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRevisionRequest:
    boto3_raw_data: "type_defs.DeleteRevisionRequestTypeDef" = dataclasses.field()

    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRevisionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRevisionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportAssetFromSignedUrlJobErrorDetails:
    boto3_raw_data: "type_defs.ImportAssetFromSignedUrlJobErrorDetailsTypeDef" = (
        dataclasses.field()
    )

    AssetName = field("AssetName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ImportAssetFromSignedUrlJobErrorDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportAssetFromSignedUrlJobErrorDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevisionPublished:
    boto3_raw_data: "type_defs.RevisionPublishedTypeDef" = dataclasses.field()

    DataSetId = field("DataSetId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RevisionPublishedTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevisionPublishedTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportAssetToSignedUrlRequestDetails:
    boto3_raw_data: "type_defs.ExportAssetToSignedUrlRequestDetailsTypeDef" = (
        dataclasses.field()
    )

    AssetId = field("AssetId")
    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportAssetToSignedUrlRequestDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportAssetToSignedUrlRequestDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportAssetToSignedUrlResponseDetails:
    boto3_raw_data: "type_defs.ExportAssetToSignedUrlResponseDetailsTypeDef" = (
        dataclasses.field()
    )

    AssetId = field("AssetId")
    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")
    SignedUrl = field("SignedUrl")
    SignedUrlExpiresAt = field("SignedUrlExpiresAt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportAssetToSignedUrlResponseDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportAssetToSignedUrlResponseDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevisionDestinationEntry:
    boto3_raw_data: "type_defs.RevisionDestinationEntryTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    RevisionId = field("RevisionId")
    KeyPattern = field("KeyPattern")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RevisionDestinationEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevisionDestinationEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssetRequest:
    boto3_raw_data: "type_defs.GetAssetRequestTypeDef" = dataclasses.field()

    AssetId = field("AssetId")
    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAssetRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetAssetRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataGrantRequest:
    boto3_raw_data: "type_defs.GetDataGrantRequestTypeDef" = dataclasses.field()

    DataGrantId = field("DataGrantId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataGrantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataGrantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataSetRequest:
    boto3_raw_data: "type_defs.GetDataSetRequestTypeDef" = dataclasses.field()

    DataSetId = field("DataSetId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDataSetRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventActionRequest:
    boto3_raw_data: "type_defs.GetEventActionRequestTypeDef" = dataclasses.field()

    EventActionId = field("EventActionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEventActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobRequest:
    boto3_raw_data: "type_defs.GetJobRequestTypeDef" = dataclasses.field()

    JobId = field("JobId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetJobRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReceivedDataGrantRequest:
    boto3_raw_data: "type_defs.GetReceivedDataGrantRequestTypeDef" = dataclasses.field()

    DataGrantArn = field("DataGrantArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReceivedDataGrantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReceivedDataGrantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRevisionRequest:
    boto3_raw_data: "type_defs.GetRevisionRequestTypeDef" = dataclasses.field()

    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRevisionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRevisionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportAssetFromApiGatewayApiRequestDetails:
    boto3_raw_data: "type_defs.ImportAssetFromApiGatewayApiRequestDetailsTypeDef" = (
        dataclasses.field()
    )

    ApiId = field("ApiId")
    ApiName = field("ApiName")
    ApiSpecificationMd5Hash = field("ApiSpecificationMd5Hash")
    DataSetId = field("DataSetId")
    ProtocolType = field("ProtocolType")
    RevisionId = field("RevisionId")
    Stage = field("Stage")
    ApiDescription = field("ApiDescription")
    ApiKey = field("ApiKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ImportAssetFromApiGatewayApiRequestDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportAssetFromApiGatewayApiRequestDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportAssetFromApiGatewayApiResponseDetails:
    boto3_raw_data: "type_defs.ImportAssetFromApiGatewayApiResponseDetailsTypeDef" = (
        dataclasses.field()
    )

    ApiId = field("ApiId")
    ApiName = field("ApiName")
    ApiSpecificationMd5Hash = field("ApiSpecificationMd5Hash")
    ApiSpecificationUploadUrl = field("ApiSpecificationUploadUrl")
    ApiSpecificationUploadUrlExpiresAt = field("ApiSpecificationUploadUrlExpiresAt")
    DataSetId = field("DataSetId")
    ProtocolType = field("ProtocolType")
    RevisionId = field("RevisionId")
    Stage = field("Stage")
    ApiDescription = field("ApiDescription")
    ApiKey = field("ApiKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ImportAssetFromApiGatewayApiResponseDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportAssetFromApiGatewayApiResponseDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportAssetFromSignedUrlRequestDetails:
    boto3_raw_data: "type_defs.ImportAssetFromSignedUrlRequestDetailsTypeDef" = (
        dataclasses.field()
    )

    AssetName = field("AssetName")
    DataSetId = field("DataSetId")
    Md5Hash = field("Md5Hash")
    RevisionId = field("RevisionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ImportAssetFromSignedUrlRequestDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportAssetFromSignedUrlRequestDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportAssetFromSignedUrlResponseDetails:
    boto3_raw_data: "type_defs.ImportAssetFromSignedUrlResponseDetailsTypeDef" = (
        dataclasses.field()
    )

    AssetName = field("AssetName")
    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")
    Md5Hash = field("Md5Hash")
    SignedUrl = field("SignedUrl")
    SignedUrlExpiresAt = field("SignedUrlExpiresAt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ImportAssetFromSignedUrlResponseDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportAssetFromSignedUrlResponseDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftDataShareAssetSourceEntry:
    boto3_raw_data: "type_defs.RedshiftDataShareAssetSourceEntryTypeDef" = (
        dataclasses.field()
    )

    DataShareArn = field("DataShareArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RedshiftDataShareAssetSourceEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftDataShareAssetSourceEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KmsKeyToGrant:
    boto3_raw_data: "type_defs.KmsKeyToGrantTypeDef" = dataclasses.field()

    KmsKeyArn = field("KmsKeyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KmsKeyToGrantTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KmsKeyToGrantTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LakeFormationTagPolicyDetails:
    boto3_raw_data: "type_defs.LakeFormationTagPolicyDetailsTypeDef" = (
        dataclasses.field()
    )

    Database = field("Database")
    Table = field("Table")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LakeFormationTagPolicyDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LakeFormationTagPolicyDetailsTypeDef"]
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
class ListDataGrantsRequest:
    boto3_raw_data: "type_defs.ListDataGrantsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataGrantsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataGrantsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSetRevisionsRequest:
    boto3_raw_data: "type_defs.ListDataSetRevisionsRequestTypeDef" = dataclasses.field()

    DataSetId = field("DataSetId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataSetRevisionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSetRevisionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevisionEntry:
    boto3_raw_data: "type_defs.RevisionEntryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    DataSetId = field("DataSetId")
    Id = field("Id")
    UpdatedAt = field("UpdatedAt")
    Comment = field("Comment")
    Finalized = field("Finalized")
    SourceId = field("SourceId")
    RevocationComment = field("RevocationComment")
    Revoked = field("Revoked")
    RevokedAt = field("RevokedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RevisionEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RevisionEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSetsRequest:
    boto3_raw_data: "type_defs.ListDataSetsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    Origin = field("Origin")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataSetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventActionsRequest:
    boto3_raw_data: "type_defs.ListEventActionsRequestTypeDef" = dataclasses.field()

    EventSourceId = field("EventSourceId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEventActionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventActionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsRequest:
    boto3_raw_data: "type_defs.ListJobsRequestTypeDef" = dataclasses.field()

    DataSetId = field("DataSetId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    RevisionId = field("RevisionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListJobsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListJobsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReceivedDataGrantsRequest:
    boto3_raw_data: "type_defs.ListReceivedDataGrantsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    AcceptanceState = field("AcceptanceState")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReceivedDataGrantsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReceivedDataGrantsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReceivedDataGrantSummariesEntry:
    boto3_raw_data: "type_defs.ReceivedDataGrantSummariesEntryTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    SenderPrincipal = field("SenderPrincipal")
    ReceiverPrincipal = field("ReceiverPrincipal")
    AcceptanceState = field("AcceptanceState")
    DataSetId = field("DataSetId")
    Id = field("Id")
    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")
    AcceptedAt = field("AcceptedAt")
    EndsAt = field("EndsAt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReceivedDataGrantSummariesEntryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReceivedDataGrantSummariesEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRevisionAssetsRequest:
    boto3_raw_data: "type_defs.ListRevisionAssetsRequestTypeDef" = dataclasses.field()

    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRevisionAssetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRevisionAssetsRequestTypeDef"]
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

    ResourceArn = field("ResourceArn")

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
class RedshiftDataShareDetails:
    boto3_raw_data: "type_defs.RedshiftDataShareDetailsTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Database = field("Database")
    Function = field("Function")
    Table = field("Table")
    Schema = field("Schema")
    View = field("View")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedshiftDataShareDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftDataShareDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeRevisionRequest:
    boto3_raw_data: "type_defs.RevokeRevisionRequestTypeDef" = dataclasses.field()

    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")
    RevocationComment = field("RevocationComment")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RevokeRevisionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeRevisionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DataAccessDetails:
    boto3_raw_data: "type_defs.S3DataAccessDetailsTypeDef" = dataclasses.field()

    KeyPrefixes = field("KeyPrefixes")
    Keys = field("Keys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3DataAccessDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DataAccessDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaChangeDetails:
    boto3_raw_data: "type_defs.SchemaChangeDetailsTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SchemaChangeDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchemaChangeDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendApiAssetRequest:
    boto3_raw_data: "type_defs.SendApiAssetRequestTypeDef" = dataclasses.field()

    AssetId = field("AssetId")
    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")
    Body = field("Body")
    QueryStringParameters = field("QueryStringParameters")
    RequestHeaders = field("RequestHeaders")
    Method = field("Method")
    Path = field("Path")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendApiAssetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendApiAssetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartJobRequest:
    boto3_raw_data: "type_defs.StartJobRequestTypeDef" = dataclasses.field()

    JobId = field("JobId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StartJobRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
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
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")

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
class UpdateAssetRequest:
    boto3_raw_data: "type_defs.UpdateAssetRequestTypeDef" = dataclasses.field()

    AssetId = field("AssetId")
    DataSetId = field("DataSetId")
    Name = field("Name")
    RevisionId = field("RevisionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAssetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataSetRequest:
    boto3_raw_data: "type_defs.UpdateDataSetRequestTypeDef" = dataclasses.field()

    DataSetId = field("DataSetId")
    Description = field("Description")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDataSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRevisionRequest:
    boto3_raw_data: "type_defs.UpdateRevisionRequestTypeDef" = dataclasses.field()

    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")
    Comment = field("Comment")
    Finalized = field("Finalized")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRevisionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRevisionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptDataGrantResponse:
    boto3_raw_data: "type_defs.AcceptDataGrantResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    SenderPrincipal = field("SenderPrincipal")
    ReceiverPrincipal = field("ReceiverPrincipal")
    Description = field("Description")
    AcceptanceState = field("AcceptanceState")
    AcceptedAt = field("AcceptedAt")
    EndsAt = field("EndsAt")
    GrantDistributionScope = field("GrantDistributionScope")
    DataSetId = field("DataSetId")
    Id = field("Id")
    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcceptDataGrantResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptDataGrantResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataGrantResponse:
    boto3_raw_data: "type_defs.CreateDataGrantResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    SenderPrincipal = field("SenderPrincipal")
    ReceiverPrincipal = field("ReceiverPrincipal")
    Description = field("Description")
    AcceptanceState = field("AcceptanceState")
    AcceptedAt = field("AcceptedAt")
    EndsAt = field("EndsAt")
    GrantDistributionScope = field("GrantDistributionScope")
    DataSetId = field("DataSetId")
    SourceDataSetId = field("SourceDataSetId")
    Id = field("Id")
    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataGrantResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataGrantResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRevisionResponse:
    boto3_raw_data: "type_defs.CreateRevisionResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Comment = field("Comment")
    CreatedAt = field("CreatedAt")
    DataSetId = field("DataSetId")
    Finalized = field("Finalized")
    Id = field("Id")
    SourceId = field("SourceId")
    Tags = field("Tags")
    UpdatedAt = field("UpdatedAt")
    RevocationComment = field("RevocationComment")
    Revoked = field("Revoked")
    RevokedAt = field("RevokedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRevisionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRevisionResponseTypeDef"]
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
class GetDataGrantResponse:
    boto3_raw_data: "type_defs.GetDataGrantResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    SenderPrincipal = field("SenderPrincipal")
    ReceiverPrincipal = field("ReceiverPrincipal")
    Description = field("Description")
    AcceptanceState = field("AcceptanceState")
    AcceptedAt = field("AcceptedAt")
    EndsAt = field("EndsAt")
    GrantDistributionScope = field("GrantDistributionScope")
    DataSetId = field("DataSetId")
    SourceDataSetId = field("SourceDataSetId")
    Id = field("Id")
    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataGrantResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataGrantResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReceivedDataGrantResponse:
    boto3_raw_data: "type_defs.GetReceivedDataGrantResponseTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    SenderPrincipal = field("SenderPrincipal")
    ReceiverPrincipal = field("ReceiverPrincipal")
    Description = field("Description")
    AcceptanceState = field("AcceptanceState")
    AcceptedAt = field("AcceptedAt")
    EndsAt = field("EndsAt")
    GrantDistributionScope = field("GrantDistributionScope")
    DataSetId = field("DataSetId")
    Id = field("Id")
    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReceivedDataGrantResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReceivedDataGrantResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRevisionResponse:
    boto3_raw_data: "type_defs.GetRevisionResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Comment = field("Comment")
    CreatedAt = field("CreatedAt")
    DataSetId = field("DataSetId")
    Finalized = field("Finalized")
    Id = field("Id")
    SourceId = field("SourceId")
    Tags = field("Tags")
    UpdatedAt = field("UpdatedAt")
    RevocationComment = field("RevocationComment")
    Revoked = field("Revoked")
    RevokedAt = field("RevokedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRevisionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRevisionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeRevisionResponse:
    boto3_raw_data: "type_defs.RevokeRevisionResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Comment = field("Comment")
    CreatedAt = field("CreatedAt")
    DataSetId = field("DataSetId")
    Finalized = field("Finalized")
    Id = field("Id")
    SourceId = field("SourceId")
    UpdatedAt = field("UpdatedAt")
    RevocationComment = field("RevocationComment")
    Revoked = field("Revoked")
    RevokedAt = field("RevokedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RevokeRevisionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeRevisionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendApiAssetResponse:
    boto3_raw_data: "type_defs.SendApiAssetResponseTypeDef" = dataclasses.field()

    Body = field("Body")
    ResponseHeaders = field("ResponseHeaders")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendApiAssetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendApiAssetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRevisionResponse:
    boto3_raw_data: "type_defs.UpdateRevisionResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Comment = field("Comment")
    CreatedAt = field("CreatedAt")
    DataSetId = field("DataSetId")
    Finalized = field("Finalized")
    Id = field("Id")
    SourceId = field("SourceId")
    UpdatedAt = field("UpdatedAt")
    RevocationComment = field("RevocationComment")
    Revoked = field("Revoked")
    RevokedAt = field("RevokedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRevisionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRevisionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportAssetsFromS3RequestDetails:
    boto3_raw_data: "type_defs.ImportAssetsFromS3RequestDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AssetSources(self):  # pragma: no cover
        return AssetSourceEntry.make_many(self.boto3_raw_data["AssetSources"])

    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ImportAssetsFromS3RequestDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportAssetsFromS3RequestDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportAssetsFromS3ResponseDetails:
    boto3_raw_data: "type_defs.ImportAssetsFromS3ResponseDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AssetSources(self):  # pragma: no cover
        return AssetSourceEntry.make_many(self.boto3_raw_data["AssetSources"])

    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ImportAssetsFromS3ResponseDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportAssetsFromS3ResponseDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoExportRevisionToS3RequestDetails:
    boto3_raw_data: "type_defs.AutoExportRevisionToS3RequestDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RevisionDestination(self):  # pragma: no cover
        return AutoExportRevisionDestinationEntry.make_one(
            self.boto3_raw_data["RevisionDestination"]
        )

    @cached_property
    def Encryption(self):  # pragma: no cover
        return ExportServerSideEncryption.make_one(self.boto3_raw_data["Encryption"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutoExportRevisionToS3RequestDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoExportRevisionToS3RequestDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportAssetsToS3RequestDetails:
    boto3_raw_data: "type_defs.ExportAssetsToS3RequestDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AssetDestinations(self):  # pragma: no cover
        return AssetDestinationEntry.make_many(self.boto3_raw_data["AssetDestinations"])

    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return ExportServerSideEncryption.make_one(self.boto3_raw_data["Encryption"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExportAssetsToS3RequestDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportAssetsToS3RequestDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportAssetsToS3ResponseDetails:
    boto3_raw_data: "type_defs.ExportAssetsToS3ResponseDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AssetDestinations(self):  # pragma: no cover
        return AssetDestinationEntry.make_many(self.boto3_raw_data["AssetDestinations"])

    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return ExportServerSideEncryption.make_one(self.boto3_raw_data["Encryption"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExportAssetsToS3ResponseDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportAssetsToS3ResponseDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataGrantRequest:
    boto3_raw_data: "type_defs.CreateDataGrantRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    GrantDistributionScope = field("GrantDistributionScope")
    ReceiverPrincipal = field("ReceiverPrincipal")
    SourceDataSetId = field("SourceDataSetId")
    EndsAt = field("EndsAt")
    Description = field("Description")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataGrantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataGrantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataUpdateRequestDetails:
    boto3_raw_data: "type_defs.DataUpdateRequestDetailsTypeDef" = dataclasses.field()

    DataUpdatedAt = field("DataUpdatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataUpdateRequestDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataUpdateRequestDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeprecationRequestDetails:
    boto3_raw_data: "type_defs.DeprecationRequestDetailsTypeDef" = dataclasses.field()

    DeprecationAt = field("DeprecationAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeprecationRequestDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeprecationRequestDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataSetResponse:
    boto3_raw_data: "type_defs.CreateDataSetResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AssetType = field("AssetType")
    CreatedAt = field("CreatedAt")
    Description = field("Description")
    Id = field("Id")
    Name = field("Name")
    Origin = field("Origin")

    @cached_property
    def OriginDetails(self):  # pragma: no cover
        return OriginDetails.make_one(self.boto3_raw_data["OriginDetails"])

    SourceId = field("SourceId")
    Tags = field("Tags")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSetEntry:
    boto3_raw_data: "type_defs.DataSetEntryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AssetType = field("AssetType")
    CreatedAt = field("CreatedAt")
    Description = field("Description")
    Id = field("Id")
    Name = field("Name")
    Origin = field("Origin")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def OriginDetails(self):  # pragma: no cover
        return OriginDetails.make_one(self.boto3_raw_data["OriginDetails"])

    SourceId = field("SourceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSetEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataSetEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataSetResponse:
    boto3_raw_data: "type_defs.GetDataSetResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AssetType = field("AssetType")
    CreatedAt = field("CreatedAt")
    Description = field("Description")
    Id = field("Id")
    Name = field("Name")
    Origin = field("Origin")

    @cached_property
    def OriginDetails(self):  # pragma: no cover
        return OriginDetails.make_one(self.boto3_raw_data["OriginDetails"])

    SourceId = field("SourceId")
    Tags = field("Tags")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataSetResponse:
    boto3_raw_data: "type_defs.UpdateDataSetResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AssetType = field("AssetType")
    CreatedAt = field("CreatedAt")
    Description = field("Description")
    Id = field("Id")
    Name = field("Name")
    Origin = field("Origin")

    @cached_property
    def OriginDetails(self):  # pragma: no cover
        return OriginDetails.make_one(self.boto3_raw_data["OriginDetails"])

    SourceId = field("SourceId")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDataSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataGrantsResponse:
    boto3_raw_data: "type_defs.ListDataGrantsResponseTypeDef" = dataclasses.field()

    @cached_property
    def DataGrantSummaries(self):  # pragma: no cover
        return DataGrantSummaryEntry.make_many(
            self.boto3_raw_data["DataGrantSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataGrantsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataGrantsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseLFTagPolicyAndPermissionsOutput:
    boto3_raw_data: "type_defs.DatabaseLFTagPolicyAndPermissionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Expression(self):  # pragma: no cover
        return LFTagOutput.make_many(self.boto3_raw_data["Expression"])

    Permissions = field("Permissions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DatabaseLFTagPolicyAndPermissionsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseLFTagPolicyAndPermissionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseLFTagPolicy:
    boto3_raw_data: "type_defs.DatabaseLFTagPolicyTypeDef" = dataclasses.field()

    @cached_property
    def Expression(self):  # pragma: no cover
        return LFTagOutput.make_many(self.boto3_raw_data["Expression"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatabaseLFTagPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseLFTagPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableLFTagPolicyAndPermissionsOutput:
    boto3_raw_data: "type_defs.TableLFTagPolicyAndPermissionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Expression(self):  # pragma: no cover
        return LFTagOutput.make_many(self.boto3_raw_data["Expression"])

    Permissions = field("Permissions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TableLFTagPolicyAndPermissionsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableLFTagPolicyAndPermissionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableLFTagPolicy:
    boto3_raw_data: "type_defs.TableLFTagPolicyTypeDef" = dataclasses.field()

    @cached_property
    def Expression(self):  # pragma: no cover
        return LFTagOutput.make_many(self.boto3_raw_data["Expression"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TableLFTagPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableLFTagPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseLFTagPolicyAndPermissions:
    boto3_raw_data: "type_defs.DatabaseLFTagPolicyAndPermissionsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Expression(self):  # pragma: no cover
        return LFTag.make_many(self.boto3_raw_data["Expression"])

    Permissions = field("Permissions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DatabaseLFTagPolicyAndPermissionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseLFTagPolicyAndPermissionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Details:
    boto3_raw_data: "type_defs.DetailsTypeDef" = dataclasses.field()

    @cached_property
    def ImportAssetFromSignedUrlJobErrorDetails(self):  # pragma: no cover
        return ImportAssetFromSignedUrlJobErrorDetails.make_one(
            self.boto3_raw_data["ImportAssetFromSignedUrlJobErrorDetails"]
        )

    @cached_property
    def ImportAssetsFromS3JobErrorDetails(self):  # pragma: no cover
        return AssetSourceEntry.make_many(
            self.boto3_raw_data["ImportAssetsFromS3JobErrorDetails"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DetailsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Event:
    boto3_raw_data: "type_defs.EventTypeDef" = dataclasses.field()

    @cached_property
    def RevisionPublished(self):  # pragma: no cover
        return RevisionPublished.make_one(self.boto3_raw_data["RevisionPublished"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportRevisionsToS3RequestDetails:
    boto3_raw_data: "type_defs.ExportRevisionsToS3RequestDetailsTypeDef" = (
        dataclasses.field()
    )

    DataSetId = field("DataSetId")

    @cached_property
    def RevisionDestinations(self):  # pragma: no cover
        return RevisionDestinationEntry.make_many(
            self.boto3_raw_data["RevisionDestinations"]
        )

    @cached_property
    def Encryption(self):  # pragma: no cover
        return ExportServerSideEncryption.make_one(self.boto3_raw_data["Encryption"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportRevisionsToS3RequestDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportRevisionsToS3RequestDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportRevisionsToS3ResponseDetails:
    boto3_raw_data: "type_defs.ExportRevisionsToS3ResponseDetailsTypeDef" = (
        dataclasses.field()
    )

    DataSetId = field("DataSetId")

    @cached_property
    def RevisionDestinations(self):  # pragma: no cover
        return RevisionDestinationEntry.make_many(
            self.boto3_raw_data["RevisionDestinations"]
        )

    @cached_property
    def Encryption(self):  # pragma: no cover
        return ExportServerSideEncryption.make_one(self.boto3_raw_data["Encryption"])

    EventActionArn = field("EventActionArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportRevisionsToS3ResponseDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportRevisionsToS3ResponseDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportAssetsFromRedshiftDataSharesRequestDetails:
    boto3_raw_data: (
        "type_defs.ImportAssetsFromRedshiftDataSharesRequestDetailsTypeDef"
    ) = dataclasses.field()

    @cached_property
    def AssetSources(self):  # pragma: no cover
        return RedshiftDataShareAssetSourceEntry.make_many(
            self.boto3_raw_data["AssetSources"]
        )

    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ImportAssetsFromRedshiftDataSharesRequestDetailsTypeDef"
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
                "type_defs.ImportAssetsFromRedshiftDataSharesRequestDetailsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportAssetsFromRedshiftDataSharesResponseDetails:
    boto3_raw_data: (
        "type_defs.ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef"
    ) = dataclasses.field()

    @cached_property
    def AssetSources(self):  # pragma: no cover
        return RedshiftDataShareAssetSourceEntry.make_many(
            self.boto3_raw_data["AssetSources"]
        )

    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef"
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
                "type_defs.ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DataAccessAssetSourceEntryOutput:
    boto3_raw_data: "type_defs.S3DataAccessAssetSourceEntryOutputTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    KeyPrefixes = field("KeyPrefixes")
    Keys = field("Keys")

    @cached_property
    def KmsKeysToGrant(self):  # pragma: no cover
        return KmsKeyToGrant.make_many(self.boto3_raw_data["KmsKeysToGrant"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.S3DataAccessAssetSourceEntryOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DataAccessAssetSourceEntryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DataAccessAssetSourceEntry:
    boto3_raw_data: "type_defs.S3DataAccessAssetSourceEntryTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    KeyPrefixes = field("KeyPrefixes")
    Keys = field("Keys")

    @cached_property
    def KmsKeysToGrant(self):  # pragma: no cover
        return KmsKeyToGrant.make_many(self.boto3_raw_data["KmsKeysToGrant"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3DataAccessAssetSourceEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DataAccessAssetSourceEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DataAccessAsset:
    boto3_raw_data: "type_defs.S3DataAccessAssetTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    KeyPrefixes = field("KeyPrefixes")
    Keys = field("Keys")
    S3AccessPointAlias = field("S3AccessPointAlias")
    S3AccessPointArn = field("S3AccessPointArn")

    @cached_property
    def KmsKeysToGrant(self):  # pragma: no cover
        return KmsKeyToGrant.make_many(self.boto3_raw_data["KmsKeysToGrant"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3DataAccessAssetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DataAccessAssetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataGrantsRequestPaginate:
    boto3_raw_data: "type_defs.ListDataGrantsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataGrantsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataGrantsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSetRevisionsRequestPaginate:
    boto3_raw_data: "type_defs.ListDataSetRevisionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DataSetId = field("DataSetId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataSetRevisionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSetRevisionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSetsRequestPaginate:
    boto3_raw_data: "type_defs.ListDataSetsRequestPaginateTypeDef" = dataclasses.field()

    Origin = field("Origin")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataSetsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventActionsRequestPaginate:
    boto3_raw_data: "type_defs.ListEventActionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    EventSourceId = field("EventSourceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEventActionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventActionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListJobsRequestPaginateTypeDef" = dataclasses.field()

    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReceivedDataGrantsRequestPaginate:
    boto3_raw_data: "type_defs.ListReceivedDataGrantsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AcceptanceState = field("AcceptanceState")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListReceivedDataGrantsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReceivedDataGrantsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRevisionAssetsRequestPaginate:
    boto3_raw_data: "type_defs.ListRevisionAssetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRevisionAssetsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRevisionAssetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSetRevisionsResponse:
    boto3_raw_data: "type_defs.ListDataSetRevisionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Revisions(self):  # pragma: no cover
        return RevisionEntry.make_many(self.boto3_raw_data["Revisions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataSetRevisionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSetRevisionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReceivedDataGrantsResponse:
    boto3_raw_data: "type_defs.ListReceivedDataGrantsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DataGrantSummaries(self):  # pragma: no cover
        return ReceivedDataGrantSummariesEntry.make_many(
            self.boto3_raw_data["DataGrantSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReceivedDataGrantsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReceivedDataGrantsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScopeDetails:
    boto3_raw_data: "type_defs.ScopeDetailsTypeDef" = dataclasses.field()

    @cached_property
    def LakeFormationTagPolicies(self):  # pragma: no cover
        return LakeFormationTagPolicyDetails.make_many(
            self.boto3_raw_data["LakeFormationTagPolicies"]
        )

    @cached_property
    def RedshiftDataShares(self):  # pragma: no cover
        return RedshiftDataShareDetails.make_many(
            self.boto3_raw_data["RedshiftDataShares"]
        )

    @cached_property
    def S3DataAccesses(self):  # pragma: no cover
        return S3DataAccessDetails.make_many(self.boto3_raw_data["S3DataAccesses"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScopeDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScopeDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaChangeRequestDetails:
    boto3_raw_data: "type_defs.SchemaChangeRequestDetailsTypeDef" = dataclasses.field()

    SchemaChangeAt = field("SchemaChangeAt")

    @cached_property
    def Changes(self):  # pragma: no cover
        return SchemaChangeDetails.make_many(self.boto3_raw_data["Changes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SchemaChangeRequestDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchemaChangeRequestDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Action:
    boto3_raw_data: "type_defs.ActionTypeDef" = dataclasses.field()

    @cached_property
    def ExportRevisionToS3(self):  # pragma: no cover
        return AutoExportRevisionToS3RequestDetails.make_one(
            self.boto3_raw_data["ExportRevisionToS3"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSetsResponse:
    boto3_raw_data: "type_defs.ListDataSetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def DataSets(self):  # pragma: no cover
        return DataSetEntry.make_many(self.boto3_raw_data["DataSets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataSetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportAssetsFromLakeFormationTagPolicyResponseDetails:
    boto3_raw_data: (
        "type_defs.ImportAssetsFromLakeFormationTagPolicyResponseDetailsTypeDef"
    ) = dataclasses.field()

    CatalogId = field("CatalogId")
    RoleArn = field("RoleArn")
    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")

    @cached_property
    def Database(self):  # pragma: no cover
        return DatabaseLFTagPolicyAndPermissionsOutput.make_one(
            self.boto3_raw_data["Database"]
        )

    @cached_property
    def Table(self):  # pragma: no cover
        return TableLFTagPolicyAndPermissionsOutput.make_one(
            self.boto3_raw_data["Table"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ImportAssetsFromLakeFormationTagPolicyResponseDetailsTypeDef"
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
                "type_defs.ImportAssetsFromLakeFormationTagPolicyResponseDetailsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LFResourceDetails:
    boto3_raw_data: "type_defs.LFResourceDetailsTypeDef" = dataclasses.field()

    @cached_property
    def Database(self):  # pragma: no cover
        return DatabaseLFTagPolicy.make_one(self.boto3_raw_data["Database"])

    @cached_property
    def Table(self):  # pragma: no cover
        return TableLFTagPolicy.make_one(self.boto3_raw_data["Table"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LFResourceDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LFResourceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableLFTagPolicyAndPermissions:
    boto3_raw_data: "type_defs.TableLFTagPolicyAndPermissionsTypeDef" = (
        dataclasses.field()
    )

    Expression = field("Expression")
    Permissions = field("Permissions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TableLFTagPolicyAndPermissionsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableLFTagPolicyAndPermissionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobError:
    boto3_raw_data: "type_defs.JobErrorTypeDef" = dataclasses.field()

    Code = field("Code")
    Message = field("Message")

    @cached_property
    def Details(self):  # pragma: no cover
        return Details.make_one(self.boto3_raw_data["Details"])

    LimitName = field("LimitName")
    LimitValue = field("LimitValue")
    ResourceId = field("ResourceId")
    ResourceType = field("ResourceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobErrorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateS3DataAccessFromS3BucketResponseDetails:
    boto3_raw_data: "type_defs.CreateS3DataAccessFromS3BucketResponseDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AssetSource(self):  # pragma: no cover
        return S3DataAccessAssetSourceEntryOutput.make_one(
            self.boto3_raw_data["AssetSource"]
        )

    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateS3DataAccessFromS3BucketResponseDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateS3DataAccessFromS3BucketResponseDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationDetails:
    boto3_raw_data: "type_defs.NotificationDetailsTypeDef" = dataclasses.field()

    @cached_property
    def DataUpdate(self):  # pragma: no cover
        return DataUpdateRequestDetails.make_one(self.boto3_raw_data["DataUpdate"])

    @cached_property
    def Deprecation(self):  # pragma: no cover
        return DeprecationRequestDetails.make_one(self.boto3_raw_data["Deprecation"])

    @cached_property
    def SchemaChange(self):  # pragma: no cover
        return SchemaChangeRequestDetails.make_one(self.boto3_raw_data["SchemaChange"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventActionRequest:
    boto3_raw_data: "type_defs.CreateEventActionRequestTypeDef" = dataclasses.field()

    @cached_property
    def Action(self):  # pragma: no cover
        return Action.make_one(self.boto3_raw_data["Action"])

    @cached_property
    def Event(self):  # pragma: no cover
        return Event.make_one(self.boto3_raw_data["Event"])

    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEventActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventActionResponse:
    boto3_raw_data: "type_defs.CreateEventActionResponseTypeDef" = dataclasses.field()

    @cached_property
    def Action(self):  # pragma: no cover
        return Action.make_one(self.boto3_raw_data["Action"])

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")

    @cached_property
    def Event(self):  # pragma: no cover
        return Event.make_one(self.boto3_raw_data["Event"])

    Id = field("Id")
    Tags = field("Tags")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEventActionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventActionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventActionEntry:
    boto3_raw_data: "type_defs.EventActionEntryTypeDef" = dataclasses.field()

    @cached_property
    def Action(self):  # pragma: no cover
        return Action.make_one(self.boto3_raw_data["Action"])

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")

    @cached_property
    def Event(self):  # pragma: no cover
        return Event.make_one(self.boto3_raw_data["Event"])

    Id = field("Id")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventActionEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventActionEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventActionResponse:
    boto3_raw_data: "type_defs.GetEventActionResponseTypeDef" = dataclasses.field()

    @cached_property
    def Action(self):  # pragma: no cover
        return Action.make_one(self.boto3_raw_data["Action"])

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")

    @cached_property
    def Event(self):  # pragma: no cover
        return Event.make_one(self.boto3_raw_data["Event"])

    Id = field("Id")
    Tags = field("Tags")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEventActionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventActionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEventActionRequest:
    boto3_raw_data: "type_defs.UpdateEventActionRequestTypeDef" = dataclasses.field()

    EventActionId = field("EventActionId")

    @cached_property
    def Action(self):  # pragma: no cover
        return Action.make_one(self.boto3_raw_data["Action"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEventActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEventActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEventActionResponse:
    boto3_raw_data: "type_defs.UpdateEventActionResponseTypeDef" = dataclasses.field()

    @cached_property
    def Action(self):  # pragma: no cover
        return Action.make_one(self.boto3_raw_data["Action"])

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")

    @cached_property
    def Event(self):  # pragma: no cover
        return Event.make_one(self.boto3_raw_data["Event"])

    Id = field("Id")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEventActionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEventActionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LFTagPolicyDetails:
    boto3_raw_data: "type_defs.LFTagPolicyDetailsTypeDef" = dataclasses.field()

    CatalogId = field("CatalogId")
    ResourceType = field("ResourceType")

    @cached_property
    def ResourceDetails(self):  # pragma: no cover
        return LFResourceDetails.make_one(self.boto3_raw_data["ResourceDetails"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LFTagPolicyDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LFTagPolicyDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseDetails:
    boto3_raw_data: "type_defs.ResponseDetailsTypeDef" = dataclasses.field()

    @cached_property
    def ExportAssetToSignedUrl(self):  # pragma: no cover
        return ExportAssetToSignedUrlResponseDetails.make_one(
            self.boto3_raw_data["ExportAssetToSignedUrl"]
        )

    @cached_property
    def ExportAssetsToS3(self):  # pragma: no cover
        return ExportAssetsToS3ResponseDetails.make_one(
            self.boto3_raw_data["ExportAssetsToS3"]
        )

    @cached_property
    def ExportRevisionsToS3(self):  # pragma: no cover
        return ExportRevisionsToS3ResponseDetails.make_one(
            self.boto3_raw_data["ExportRevisionsToS3"]
        )

    @cached_property
    def ImportAssetFromSignedUrl(self):  # pragma: no cover
        return ImportAssetFromSignedUrlResponseDetails.make_one(
            self.boto3_raw_data["ImportAssetFromSignedUrl"]
        )

    @cached_property
    def ImportAssetsFromS3(self):  # pragma: no cover
        return ImportAssetsFromS3ResponseDetails.make_one(
            self.boto3_raw_data["ImportAssetsFromS3"]
        )

    @cached_property
    def ImportAssetsFromRedshiftDataShares(self):  # pragma: no cover
        return ImportAssetsFromRedshiftDataSharesResponseDetails.make_one(
            self.boto3_raw_data["ImportAssetsFromRedshiftDataShares"]
        )

    @cached_property
    def ImportAssetFromApiGatewayApi(self):  # pragma: no cover
        return ImportAssetFromApiGatewayApiResponseDetails.make_one(
            self.boto3_raw_data["ImportAssetFromApiGatewayApi"]
        )

    @cached_property
    def CreateS3DataAccessFromS3Bucket(self):  # pragma: no cover
        return CreateS3DataAccessFromS3BucketResponseDetails.make_one(
            self.boto3_raw_data["CreateS3DataAccessFromS3Bucket"]
        )

    @cached_property
    def ImportAssetsFromLakeFormationTagPolicy(self):  # pragma: no cover
        return ImportAssetsFromLakeFormationTagPolicyResponseDetails.make_one(
            self.boto3_raw_data["ImportAssetsFromLakeFormationTagPolicy"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResponseDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateS3DataAccessFromS3BucketRequestDetails:
    boto3_raw_data: "type_defs.CreateS3DataAccessFromS3BucketRequestDetailsTypeDef" = (
        dataclasses.field()
    )

    AssetSource = field("AssetSource")
    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateS3DataAccessFromS3BucketRequestDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateS3DataAccessFromS3BucketRequestDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendDataSetNotificationRequest:
    boto3_raw_data: "type_defs.SendDataSetNotificationRequestTypeDef" = (
        dataclasses.field()
    )

    DataSetId = field("DataSetId")
    Type = field("Type")

    @cached_property
    def Scope(self):  # pragma: no cover
        return ScopeDetails.make_one(self.boto3_raw_data["Scope"])

    ClientToken = field("ClientToken")
    Comment = field("Comment")

    @cached_property
    def Details(self):  # pragma: no cover
        return NotificationDetails.make_one(self.boto3_raw_data["Details"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SendDataSetNotificationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendDataSetNotificationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventActionsResponse:
    boto3_raw_data: "type_defs.ListEventActionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def EventActions(self):  # pragma: no cover
        return EventActionEntry.make_many(self.boto3_raw_data["EventActions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEventActionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventActionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LakeFormationDataPermissionDetails:
    boto3_raw_data: "type_defs.LakeFormationDataPermissionDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LFTagPolicy(self):  # pragma: no cover
        return LFTagPolicyDetails.make_one(self.boto3_raw_data["LFTagPolicy"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LakeFormationDataPermissionDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LakeFormationDataPermissionDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportAssetsFromLakeFormationTagPolicyRequestDetails:
    boto3_raw_data: (
        "type_defs.ImportAssetsFromLakeFormationTagPolicyRequestDetailsTypeDef"
    ) = dataclasses.field()

    CatalogId = field("CatalogId")
    RoleArn = field("RoleArn")
    DataSetId = field("DataSetId")
    RevisionId = field("RevisionId")
    Database = field("Database")
    Table = field("Table")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ImportAssetsFromLakeFormationTagPolicyRequestDetailsTypeDef"
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
                "type_defs.ImportAssetsFromLakeFormationTagPolicyRequestDetailsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobResponse:
    boto3_raw_data: "type_defs.CreateJobResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")

    @cached_property
    def Details(self):  # pragma: no cover
        return ResponseDetails.make_one(self.boto3_raw_data["Details"])

    @cached_property
    def Errors(self):  # pragma: no cover
        return JobError.make_many(self.boto3_raw_data["Errors"])

    Id = field("Id")
    State = field("State")
    Type = field("Type")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateJobResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobResponse:
    boto3_raw_data: "type_defs.GetJobResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")

    @cached_property
    def Details(self):  # pragma: no cover
        return ResponseDetails.make_one(self.boto3_raw_data["Details"])

    @cached_property
    def Errors(self):  # pragma: no cover
        return JobError.make_many(self.boto3_raw_data["Errors"])

    Id = field("Id")
    State = field("State")
    Type = field("Type")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetJobResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetJobResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobEntry:
    boto3_raw_data: "type_defs.JobEntryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")

    @cached_property
    def Details(self):  # pragma: no cover
        return ResponseDetails.make_one(self.boto3_raw_data["Details"])

    Id = field("Id")
    State = field("State")
    Type = field("Type")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def Errors(self):  # pragma: no cover
        return JobError.make_many(self.boto3_raw_data["Errors"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobEntryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LakeFormationDataPermissionAsset:
    boto3_raw_data: "type_defs.LakeFormationDataPermissionAssetTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LakeFormationDataPermissionDetails(self):  # pragma: no cover
        return LakeFormationDataPermissionDetails.make_one(
            self.boto3_raw_data["LakeFormationDataPermissionDetails"]
        )

    LakeFormationDataPermissionType = field("LakeFormationDataPermissionType")
    Permissions = field("Permissions")
    RoleArn = field("RoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LakeFormationDataPermissionAssetTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LakeFormationDataPermissionAssetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestDetails:
    boto3_raw_data: "type_defs.RequestDetailsTypeDef" = dataclasses.field()

    @cached_property
    def ExportAssetToSignedUrl(self):  # pragma: no cover
        return ExportAssetToSignedUrlRequestDetails.make_one(
            self.boto3_raw_data["ExportAssetToSignedUrl"]
        )

    @cached_property
    def ExportAssetsToS3(self):  # pragma: no cover
        return ExportAssetsToS3RequestDetails.make_one(
            self.boto3_raw_data["ExportAssetsToS3"]
        )

    @cached_property
    def ExportRevisionsToS3(self):  # pragma: no cover
        return ExportRevisionsToS3RequestDetails.make_one(
            self.boto3_raw_data["ExportRevisionsToS3"]
        )

    @cached_property
    def ImportAssetFromSignedUrl(self):  # pragma: no cover
        return ImportAssetFromSignedUrlRequestDetails.make_one(
            self.boto3_raw_data["ImportAssetFromSignedUrl"]
        )

    @cached_property
    def ImportAssetsFromS3(self):  # pragma: no cover
        return ImportAssetsFromS3RequestDetails.make_one(
            self.boto3_raw_data["ImportAssetsFromS3"]
        )

    @cached_property
    def ImportAssetsFromRedshiftDataShares(self):  # pragma: no cover
        return ImportAssetsFromRedshiftDataSharesRequestDetails.make_one(
            self.boto3_raw_data["ImportAssetsFromRedshiftDataShares"]
        )

    @cached_property
    def ImportAssetFromApiGatewayApi(self):  # pragma: no cover
        return ImportAssetFromApiGatewayApiRequestDetails.make_one(
            self.boto3_raw_data["ImportAssetFromApiGatewayApi"]
        )

    @cached_property
    def CreateS3DataAccessFromS3Bucket(self):  # pragma: no cover
        return CreateS3DataAccessFromS3BucketRequestDetails.make_one(
            self.boto3_raw_data["CreateS3DataAccessFromS3Bucket"]
        )

    @cached_property
    def ImportAssetsFromLakeFormationTagPolicy(self):  # pragma: no cover
        return ImportAssetsFromLakeFormationTagPolicyRequestDetails.make_one(
            self.boto3_raw_data["ImportAssetsFromLakeFormationTagPolicy"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RequestDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RequestDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsResponse:
    boto3_raw_data: "type_defs.ListJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Jobs(self):  # pragma: no cover
        return JobEntry.make_many(self.boto3_raw_data["Jobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListJobsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetDetails:
    boto3_raw_data: "type_defs.AssetDetailsTypeDef" = dataclasses.field()

    @cached_property
    def S3SnapshotAsset(self):  # pragma: no cover
        return S3SnapshotAsset.make_one(self.boto3_raw_data["S3SnapshotAsset"])

    @cached_property
    def RedshiftDataShareAsset(self):  # pragma: no cover
        return RedshiftDataShareAsset.make_one(
            self.boto3_raw_data["RedshiftDataShareAsset"]
        )

    @cached_property
    def ApiGatewayApiAsset(self):  # pragma: no cover
        return ApiGatewayApiAsset.make_one(self.boto3_raw_data["ApiGatewayApiAsset"])

    @cached_property
    def S3DataAccessAsset(self):  # pragma: no cover
        return S3DataAccessAsset.make_one(self.boto3_raw_data["S3DataAccessAsset"])

    @cached_property
    def LakeFormationDataPermissionAsset(self):  # pragma: no cover
        return LakeFormationDataPermissionAsset.make_one(
            self.boto3_raw_data["LakeFormationDataPermissionAsset"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssetDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobRequest:
    boto3_raw_data: "type_defs.CreateJobRequestTypeDef" = dataclasses.field()

    @cached_property
    def Details(self):  # pragma: no cover
        return RequestDetails.make_one(self.boto3_raw_data["Details"])

    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetEntry:
    boto3_raw_data: "type_defs.AssetEntryTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def AssetDetails(self):  # pragma: no cover
        return AssetDetails.make_one(self.boto3_raw_data["AssetDetails"])

    AssetType = field("AssetType")
    CreatedAt = field("CreatedAt")
    DataSetId = field("DataSetId")
    Id = field("Id")
    Name = field("Name")
    RevisionId = field("RevisionId")
    UpdatedAt = field("UpdatedAt")
    SourceId = field("SourceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssetEntryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssetResponse:
    boto3_raw_data: "type_defs.GetAssetResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def AssetDetails(self):  # pragma: no cover
        return AssetDetails.make_one(self.boto3_raw_data["AssetDetails"])

    AssetType = field("AssetType")
    CreatedAt = field("CreatedAt")
    DataSetId = field("DataSetId")
    Id = field("Id")
    Name = field("Name")
    RevisionId = field("RevisionId")
    SourceId = field("SourceId")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAssetResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssetResponse:
    boto3_raw_data: "type_defs.UpdateAssetResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def AssetDetails(self):  # pragma: no cover
        return AssetDetails.make_one(self.boto3_raw_data["AssetDetails"])

    AssetType = field("AssetType")
    CreatedAt = field("CreatedAt")
    DataSetId = field("DataSetId")
    Id = field("Id")
    Name = field("Name")
    RevisionId = field("RevisionId")
    SourceId = field("SourceId")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAssetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRevisionAssetsResponse:
    boto3_raw_data: "type_defs.ListRevisionAssetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Assets(self):  # pragma: no cover
        return AssetEntry.make_many(self.boto3_raw_data["Assets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRevisionAssetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRevisionAssetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
