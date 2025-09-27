# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_firehose import type_defs as bs_td


class FIREHOSECaster:

    def create_delivery_stream(
        self,
        res: "bs_td.CreateDeliveryStreamOutputTypeDef",
    ) -> "dc_td.CreateDeliveryStreamOutput":
        return dc_td.CreateDeliveryStreamOutput.make_one(res)

    def describe_delivery_stream(
        self,
        res: "bs_td.DescribeDeliveryStreamOutputTypeDef",
    ) -> "dc_td.DescribeDeliveryStreamOutput":
        return dc_td.DescribeDeliveryStreamOutput.make_one(res)

    def list_delivery_streams(
        self,
        res: "bs_td.ListDeliveryStreamsOutputTypeDef",
    ) -> "dc_td.ListDeliveryStreamsOutput":
        return dc_td.ListDeliveryStreamsOutput.make_one(res)

    def list_tags_for_delivery_stream(
        self,
        res: "bs_td.ListTagsForDeliveryStreamOutputTypeDef",
    ) -> "dc_td.ListTagsForDeliveryStreamOutput":
        return dc_td.ListTagsForDeliveryStreamOutput.make_one(res)

    def put_record(
        self,
        res: "bs_td.PutRecordOutputTypeDef",
    ) -> "dc_td.PutRecordOutput":
        return dc_td.PutRecordOutput.make_one(res)

    def put_record_batch(
        self,
        res: "bs_td.PutRecordBatchOutputTypeDef",
    ) -> "dc_td.PutRecordBatchOutput":
        return dc_td.PutRecordBatchOutput.make_one(res)


firehose_caster = FIREHOSECaster()
