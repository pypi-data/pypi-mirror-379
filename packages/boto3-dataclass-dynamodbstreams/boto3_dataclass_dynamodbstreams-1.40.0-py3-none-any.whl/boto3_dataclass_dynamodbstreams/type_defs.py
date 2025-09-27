# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_dynamodbstreams import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AttributeValue:
    boto3_raw_data: "type_defs.AttributeValueTypeDef" = dataclasses.field()

    S = field("S")
    N = field("N")
    B = field("B")
    SS = field("SS")
    NS = field("NS")
    BS = field("BS")
    M = field("M")
    L = field("L")
    NULL = field("NULL")
    BOOL = field("BOOL")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributeValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShardFilter:
    boto3_raw_data: "type_defs.ShardFilterTypeDef" = dataclasses.field()

    Type = field("Type")
    ShardId = field("ShardId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ShardFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ShardFilterTypeDef"]]
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
class GetRecordsInput:
    boto3_raw_data: "type_defs.GetRecordsInputTypeDef" = dataclasses.field()

    ShardIterator = field("ShardIterator")
    Limit = field("Limit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRecordsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetRecordsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetShardIteratorInput:
    boto3_raw_data: "type_defs.GetShardIteratorInputTypeDef" = dataclasses.field()

    StreamArn = field("StreamArn")
    ShardId = field("ShardId")
    ShardIteratorType = field("ShardIteratorType")
    SequenceNumber = field("SequenceNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetShardIteratorInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetShardIteratorInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Identity:
    boto3_raw_data: "type_defs.IdentityTypeDef" = dataclasses.field()

    PrincipalId = field("PrincipalId")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IdentityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IdentityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeySchemaElement:
    boto3_raw_data: "type_defs.KeySchemaElementTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")
    KeyType = field("KeyType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeySchemaElementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeySchemaElementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamsInput:
    boto3_raw_data: "type_defs.ListStreamsInputTypeDef" = dataclasses.field()

    TableName = field("TableName")
    Limit = field("Limit")
    ExclusiveStartStreamArn = field("ExclusiveStartStreamArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListStreamsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Stream:
    boto3_raw_data: "type_defs.StreamTypeDef" = dataclasses.field()

    StreamArn = field("StreamArn")
    TableName = field("TableName")
    StreamLabel = field("StreamLabel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StreamTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StreamTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SequenceNumberRange:
    boto3_raw_data: "type_defs.SequenceNumberRangeTypeDef" = dataclasses.field()

    StartingSequenceNumber = field("StartingSequenceNumber")
    EndingSequenceNumber = field("EndingSequenceNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SequenceNumberRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SequenceNumberRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamRecord:
    boto3_raw_data: "type_defs.StreamRecordTypeDef" = dataclasses.field()

    ApproximateCreationDateTime = field("ApproximateCreationDateTime")
    Keys = field("Keys")
    NewImage = field("NewImage")
    OldImage = field("OldImage")
    SequenceNumber = field("SequenceNumber")
    SizeBytes = field("SizeBytes")
    StreamViewType = field("StreamViewType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StreamRecordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StreamRecordTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStreamInput:
    boto3_raw_data: "type_defs.DescribeStreamInputTypeDef" = dataclasses.field()

    StreamArn = field("StreamArn")
    Limit = field("Limit")
    ExclusiveStartShardId = field("ExclusiveStartShardId")

    @cached_property
    def ShardFilter(self):  # pragma: no cover
        return ShardFilter.make_one(self.boto3_raw_data["ShardFilter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStreamInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetShardIteratorOutput:
    boto3_raw_data: "type_defs.GetShardIteratorOutputTypeDef" = dataclasses.field()

    ShardIterator = field("ShardIterator")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetShardIteratorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetShardIteratorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamsOutput:
    boto3_raw_data: "type_defs.ListStreamsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Streams(self):  # pragma: no cover
        return Stream.make_many(self.boto3_raw_data["Streams"])

    LastEvaluatedStreamArn = field("LastEvaluatedStreamArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListStreamsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Shard:
    boto3_raw_data: "type_defs.ShardTypeDef" = dataclasses.field()

    ShardId = field("ShardId")

    @cached_property
    def SequenceNumberRange(self):  # pragma: no cover
        return SequenceNumberRange.make_one(self.boto3_raw_data["SequenceNumberRange"])

    ParentShardId = field("ParentShardId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ShardTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ShardTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Record:
    boto3_raw_data: "type_defs.RecordTypeDef" = dataclasses.field()

    eventID = field("eventID")
    eventName = field("eventName")
    eventVersion = field("eventVersion")
    eventSource = field("eventSource")
    awsRegion = field("awsRegion")

    @cached_property
    def dynamodb(self):  # pragma: no cover
        return StreamRecord.make_one(self.boto3_raw_data["dynamodb"])

    @cached_property
    def userIdentity(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["userIdentity"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecordTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamDescription:
    boto3_raw_data: "type_defs.StreamDescriptionTypeDef" = dataclasses.field()

    StreamArn = field("StreamArn")
    StreamLabel = field("StreamLabel")
    StreamStatus = field("StreamStatus")
    StreamViewType = field("StreamViewType")
    CreationRequestDateTime = field("CreationRequestDateTime")
    TableName = field("TableName")

    @cached_property
    def KeySchema(self):  # pragma: no cover
        return KeySchemaElement.make_many(self.boto3_raw_data["KeySchema"])

    @cached_property
    def Shards(self):  # pragma: no cover
        return Shard.make_many(self.boto3_raw_data["Shards"])

    LastEvaluatedShardId = field("LastEvaluatedShardId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StreamDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecordsOutput:
    boto3_raw_data: "type_defs.GetRecordsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Records(self):  # pragma: no cover
        return Record.make_many(self.boto3_raw_data["Records"])

    NextShardIterator = field("NextShardIterator")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRecordsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecordsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStreamOutput:
    boto3_raw_data: "type_defs.DescribeStreamOutputTypeDef" = dataclasses.field()

    @cached_property
    def StreamDescription(self):  # pragma: no cover
        return StreamDescription.make_one(self.boto3_raw_data["StreamDescription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStreamOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStreamOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
