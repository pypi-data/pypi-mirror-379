# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_s3vectors import type_defs as bs_td


class S3VECTORSCaster:

    def get_index(
        self,
        res: "bs_td.GetIndexOutputTypeDef",
    ) -> "dc_td.GetIndexOutput":
        return dc_td.GetIndexOutput.make_one(res)

    def get_vector_bucket(
        self,
        res: "bs_td.GetVectorBucketOutputTypeDef",
    ) -> "dc_td.GetVectorBucketOutput":
        return dc_td.GetVectorBucketOutput.make_one(res)

    def get_vector_bucket_policy(
        self,
        res: "bs_td.GetVectorBucketPolicyOutputTypeDef",
    ) -> "dc_td.GetVectorBucketPolicyOutput":
        return dc_td.GetVectorBucketPolicyOutput.make_one(res)

    def get_vectors(
        self,
        res: "bs_td.GetVectorsOutputTypeDef",
    ) -> "dc_td.GetVectorsOutput":
        return dc_td.GetVectorsOutput.make_one(res)

    def list_indexes(
        self,
        res: "bs_td.ListIndexesOutputTypeDef",
    ) -> "dc_td.ListIndexesOutput":
        return dc_td.ListIndexesOutput.make_one(res)

    def list_vector_buckets(
        self,
        res: "bs_td.ListVectorBucketsOutputTypeDef",
    ) -> "dc_td.ListVectorBucketsOutput":
        return dc_td.ListVectorBucketsOutput.make_one(res)

    def list_vectors(
        self,
        res: "bs_td.ListVectorsOutputTypeDef",
    ) -> "dc_td.ListVectorsOutput":
        return dc_td.ListVectorsOutput.make_one(res)

    def query_vectors(
        self,
        res: "bs_td.QueryVectorsOutputTypeDef",
    ) -> "dc_td.QueryVectorsOutput":
        return dc_td.QueryVectorsOutput.make_one(res)


s3vectors_caster = S3VECTORSCaster()
