# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_s3vectors import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class EncryptionConfiguration:
    boto3_raw_data: "type_defs.EncryptionConfigurationTypeDef" = dataclasses.field()

    sseType = field("sseType")
    kmsKeyArn = field("kmsKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncryptionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIndexInput:
    boto3_raw_data: "type_defs.DeleteIndexInputTypeDef" = dataclasses.field()

    vectorBucketName = field("vectorBucketName")
    indexName = field("indexName")
    indexArn = field("indexArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteIndexInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIndexInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVectorBucketInput:
    boto3_raw_data: "type_defs.DeleteVectorBucketInputTypeDef" = dataclasses.field()

    vectorBucketName = field("vectorBucketName")
    vectorBucketArn = field("vectorBucketArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVectorBucketInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVectorBucketInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVectorBucketPolicyInput:
    boto3_raw_data: "type_defs.DeleteVectorBucketPolicyInputTypeDef" = (
        dataclasses.field()
    )

    vectorBucketName = field("vectorBucketName")
    vectorBucketArn = field("vectorBucketArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteVectorBucketPolicyInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVectorBucketPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVectorsInput:
    boto3_raw_data: "type_defs.DeleteVectorsInputTypeDef" = dataclasses.field()

    keys = field("keys")
    vectorBucketName = field("vectorBucketName")
    indexName = field("indexName")
    indexArn = field("indexArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVectorsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVectorsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIndexInput:
    boto3_raw_data: "type_defs.GetIndexInputTypeDef" = dataclasses.field()

    vectorBucketName = field("vectorBucketName")
    indexName = field("indexName")
    indexArn = field("indexArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetIndexInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetIndexInputTypeDef"]],
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
class VectorDataOutput:
    boto3_raw_data: "type_defs.VectorDataOutputTypeDef" = dataclasses.field()

    float32 = field("float32")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VectorDataOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VectorDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVectorBucketInput:
    boto3_raw_data: "type_defs.GetVectorBucketInputTypeDef" = dataclasses.field()

    vectorBucketName = field("vectorBucketName")
    vectorBucketArn = field("vectorBucketArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVectorBucketInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVectorBucketInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVectorBucketPolicyInput:
    boto3_raw_data: "type_defs.GetVectorBucketPolicyInputTypeDef" = dataclasses.field()

    vectorBucketName = field("vectorBucketName")
    vectorBucketArn = field("vectorBucketArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVectorBucketPolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVectorBucketPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVectorsInput:
    boto3_raw_data: "type_defs.GetVectorsInputTypeDef" = dataclasses.field()

    keys = field("keys")
    vectorBucketName = field("vectorBucketName")
    indexName = field("indexName")
    indexArn = field("indexArn")
    returnData = field("returnData")
    returnMetadata = field("returnMetadata")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetVectorsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetVectorsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndexSummary:
    boto3_raw_data: "type_defs.IndexSummaryTypeDef" = dataclasses.field()

    vectorBucketName = field("vectorBucketName")
    indexName = field("indexName")
    indexArn = field("indexArn")
    creationTime = field("creationTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IndexSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IndexSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataConfigurationOutput:
    boto3_raw_data: "type_defs.MetadataConfigurationOutputTypeDef" = dataclasses.field()

    nonFilterableMetadataKeys = field("nonFilterableMetadataKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetadataConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataConfigurationOutputTypeDef"]
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
class ListIndexesInput:
    boto3_raw_data: "type_defs.ListIndexesInputTypeDef" = dataclasses.field()

    vectorBucketName = field("vectorBucketName")
    vectorBucketArn = field("vectorBucketArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    prefix = field("prefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListIndexesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIndexesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVectorBucketsInput:
    boto3_raw_data: "type_defs.ListVectorBucketsInputTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    prefix = field("prefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVectorBucketsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVectorBucketsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorBucketSummary:
    boto3_raw_data: "type_defs.VectorBucketSummaryTypeDef" = dataclasses.field()

    vectorBucketName = field("vectorBucketName")
    vectorBucketArn = field("vectorBucketArn")
    creationTime = field("creationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VectorBucketSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VectorBucketSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVectorsInput:
    boto3_raw_data: "type_defs.ListVectorsInputTypeDef" = dataclasses.field()

    vectorBucketName = field("vectorBucketName")
    indexName = field("indexName")
    indexArn = field("indexArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    segmentCount = field("segmentCount")
    segmentIndex = field("segmentIndex")
    returnData = field("returnData")
    returnMetadata = field("returnMetadata")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListVectorsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVectorsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataConfiguration:
    boto3_raw_data: "type_defs.MetadataConfigurationTypeDef" = dataclasses.field()

    nonFilterableMetadataKeys = field("nonFilterableMetadataKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetadataConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutVectorBucketPolicyInput:
    boto3_raw_data: "type_defs.PutVectorBucketPolicyInputTypeDef" = dataclasses.field()

    policy = field("policy")
    vectorBucketName = field("vectorBucketName")
    vectorBucketArn = field("vectorBucketArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutVectorBucketPolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutVectorBucketPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorData:
    boto3_raw_data: "type_defs.VectorDataTypeDef" = dataclasses.field()

    float32 = field("float32")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VectorDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VectorDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVectorBucketInput:
    boto3_raw_data: "type_defs.CreateVectorBucketInputTypeDef" = dataclasses.field()

    vectorBucketName = field("vectorBucketName")

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVectorBucketInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVectorBucketInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorBucket:
    boto3_raw_data: "type_defs.VectorBucketTypeDef" = dataclasses.field()

    vectorBucketName = field("vectorBucketName")
    vectorBucketArn = field("vectorBucketArn")
    creationTime = field("creationTime")

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VectorBucketTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VectorBucketTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVectorBucketPolicyOutput:
    boto3_raw_data: "type_defs.GetVectorBucketPolicyOutputTypeDef" = dataclasses.field()

    policy = field("policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVectorBucketPolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVectorBucketPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOutputVector:
    boto3_raw_data: "type_defs.GetOutputVectorTypeDef" = dataclasses.field()

    key = field("key")

    @cached_property
    def data(self):  # pragma: no cover
        return VectorDataOutput.make_one(self.boto3_raw_data["data"])

    metadata = field("metadata")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetOutputVectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetOutputVectorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOutputVector:
    boto3_raw_data: "type_defs.ListOutputVectorTypeDef" = dataclasses.field()

    key = field("key")

    @cached_property
    def data(self):  # pragma: no cover
        return VectorDataOutput.make_one(self.boto3_raw_data["data"])

    metadata = field("metadata")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListOutputVectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOutputVectorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryOutputVector:
    boto3_raw_data: "type_defs.QueryOutputVectorTypeDef" = dataclasses.field()

    key = field("key")

    @cached_property
    def data(self):  # pragma: no cover
        return VectorDataOutput.make_one(self.boto3_raw_data["data"])

    metadata = field("metadata")
    distance = field("distance")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryOutputVectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryOutputVectorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIndexesOutput:
    boto3_raw_data: "type_defs.ListIndexesOutputTypeDef" = dataclasses.field()

    @cached_property
    def indexes(self):  # pragma: no cover
        return IndexSummary.make_many(self.boto3_raw_data["indexes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListIndexesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIndexesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Index:
    boto3_raw_data: "type_defs.IndexTypeDef" = dataclasses.field()

    vectorBucketName = field("vectorBucketName")
    indexName = field("indexName")
    indexArn = field("indexArn")
    creationTime = field("creationTime")
    dataType = field("dataType")
    dimension = field("dimension")
    distanceMetric = field("distanceMetric")

    @cached_property
    def metadataConfiguration(self):  # pragma: no cover
        return MetadataConfigurationOutput.make_one(
            self.boto3_raw_data["metadataConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IndexTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IndexTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIndexesInputPaginate:
    boto3_raw_data: "type_defs.ListIndexesInputPaginateTypeDef" = dataclasses.field()

    vectorBucketName = field("vectorBucketName")
    vectorBucketArn = field("vectorBucketArn")
    prefix = field("prefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIndexesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIndexesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVectorBucketsInputPaginate:
    boto3_raw_data: "type_defs.ListVectorBucketsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    prefix = field("prefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVectorBucketsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVectorBucketsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVectorsInputPaginate:
    boto3_raw_data: "type_defs.ListVectorsInputPaginateTypeDef" = dataclasses.field()

    vectorBucketName = field("vectorBucketName")
    indexName = field("indexName")
    indexArn = field("indexArn")
    segmentCount = field("segmentCount")
    segmentIndex = field("segmentIndex")
    returnData = field("returnData")
    returnMetadata = field("returnMetadata")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVectorsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVectorsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVectorBucketsOutput:
    boto3_raw_data: "type_defs.ListVectorBucketsOutputTypeDef" = dataclasses.field()

    @cached_property
    def vectorBuckets(self):  # pragma: no cover
        return VectorBucketSummary.make_many(self.boto3_raw_data["vectorBuckets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVectorBucketsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVectorBucketsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVectorBucketOutput:
    boto3_raw_data: "type_defs.GetVectorBucketOutputTypeDef" = dataclasses.field()

    @cached_property
    def vectorBucket(self):  # pragma: no cover
        return VectorBucket.make_one(self.boto3_raw_data["vectorBucket"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVectorBucketOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVectorBucketOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVectorsOutput:
    boto3_raw_data: "type_defs.GetVectorsOutputTypeDef" = dataclasses.field()

    @cached_property
    def vectors(self):  # pragma: no cover
        return GetOutputVector.make_many(self.boto3_raw_data["vectors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetVectorsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVectorsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVectorsOutput:
    boto3_raw_data: "type_defs.ListVectorsOutputTypeDef" = dataclasses.field()

    @cached_property
    def vectors(self):  # pragma: no cover
        return ListOutputVector.make_many(self.boto3_raw_data["vectors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListVectorsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVectorsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryVectorsOutput:
    boto3_raw_data: "type_defs.QueryVectorsOutputTypeDef" = dataclasses.field()

    @cached_property
    def vectors(self):  # pragma: no cover
        return QueryOutputVector.make_many(self.boto3_raw_data["vectors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryVectorsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryVectorsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIndexOutput:
    boto3_raw_data: "type_defs.GetIndexOutputTypeDef" = dataclasses.field()

    @cached_property
    def index(self):  # pragma: no cover
        return Index.make_one(self.boto3_raw_data["index"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetIndexOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetIndexOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIndexInput:
    boto3_raw_data: "type_defs.CreateIndexInputTypeDef" = dataclasses.field()

    indexName = field("indexName")
    dataType = field("dataType")
    dimension = field("dimension")
    distanceMetric = field("distanceMetric")
    vectorBucketName = field("vectorBucketName")
    vectorBucketArn = field("vectorBucketArn")
    metadataConfiguration = field("metadataConfiguration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateIndexInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIndexInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutInputVector:
    boto3_raw_data: "type_defs.PutInputVectorTypeDef" = dataclasses.field()

    key = field("key")
    data = field("data")
    metadata = field("metadata")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutInputVectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutInputVectorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryVectorsInput:
    boto3_raw_data: "type_defs.QueryVectorsInputTypeDef" = dataclasses.field()

    topK = field("topK")
    queryVector = field("queryVector")
    vectorBucketName = field("vectorBucketName")
    indexName = field("indexName")
    indexArn = field("indexArn")
    filter = field("filter")
    returnMetadata = field("returnMetadata")
    returnDistance = field("returnDistance")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryVectorsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryVectorsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutVectorsInput:
    boto3_raw_data: "type_defs.PutVectorsInputTypeDef" = dataclasses.field()

    @cached_property
    def vectors(self):  # pragma: no cover
        return PutInputVector.make_many(self.boto3_raw_data["vectors"])

    vectorBucketName = field("vectorBucketName")
    indexName = field("indexName")
    indexArn = field("indexArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutVectorsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutVectorsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
