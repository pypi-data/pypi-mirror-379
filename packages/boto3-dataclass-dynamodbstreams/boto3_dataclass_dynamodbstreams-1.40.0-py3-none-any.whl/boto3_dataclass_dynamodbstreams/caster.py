# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_dynamodbstreams import type_defs as bs_td


class DYNAMODBSTREAMSCaster:

    def describe_stream(
        self,
        res: "bs_td.DescribeStreamOutputTypeDef",
    ) -> "dc_td.DescribeStreamOutput":
        return dc_td.DescribeStreamOutput.make_one(res)

    def get_records(
        self,
        res: "bs_td.GetRecordsOutputTypeDef",
    ) -> "dc_td.GetRecordsOutput":
        return dc_td.GetRecordsOutput.make_one(res)

    def get_shard_iterator(
        self,
        res: "bs_td.GetShardIteratorOutputTypeDef",
    ) -> "dc_td.GetShardIteratorOutput":
        return dc_td.GetShardIteratorOutput.make_one(res)

    def list_streams(
        self,
        res: "bs_td.ListStreamsOutputTypeDef",
    ) -> "dc_td.ListStreamsOutput":
        return dc_td.ListStreamsOutput.make_one(res)


dynamodbstreams_caster = DYNAMODBSTREAMSCaster()
