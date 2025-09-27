# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ebs import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Block:
    boto3_raw_data: "type_defs.BlockTypeDef" = dataclasses.field()

    BlockIndex = field("BlockIndex")
    BlockToken = field("BlockToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BlockTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BlockTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangedBlock:
    boto3_raw_data: "type_defs.ChangedBlockTypeDef" = dataclasses.field()

    BlockIndex = field("BlockIndex")
    FirstBlockToken = field("FirstBlockToken")
    SecondBlockToken = field("SecondBlockToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChangedBlockTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChangedBlockTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompleteSnapshotRequest:
    boto3_raw_data: "type_defs.CompleteSnapshotRequestTypeDef" = dataclasses.field()

    SnapshotId = field("SnapshotId")
    ChangedBlocksCount = field("ChangedBlocksCount")
    Checksum = field("Checksum")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ChecksumAggregationMethod = field("ChecksumAggregationMethod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompleteSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompleteSnapshotRequestTypeDef"]
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
class GetSnapshotBlockRequest:
    boto3_raw_data: "type_defs.GetSnapshotBlockRequestTypeDef" = dataclasses.field()

    SnapshotId = field("SnapshotId")
    BlockIndex = field("BlockIndex")
    BlockToken = field("BlockToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSnapshotBlockRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSnapshotBlockRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChangedBlocksRequest:
    boto3_raw_data: "type_defs.ListChangedBlocksRequestTypeDef" = dataclasses.field()

    SecondSnapshotId = field("SecondSnapshotId")
    FirstSnapshotId = field("FirstSnapshotId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    StartingBlockIndex = field("StartingBlockIndex")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChangedBlocksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChangedBlocksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSnapshotBlocksRequest:
    boto3_raw_data: "type_defs.ListSnapshotBlocksRequestTypeDef" = dataclasses.field()

    SnapshotId = field("SnapshotId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    StartingBlockIndex = field("StartingBlockIndex")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSnapshotBlocksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSnapshotBlocksRequestTypeDef"]
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
class PutSnapshotBlockRequest:
    boto3_raw_data: "type_defs.PutSnapshotBlockRequestTypeDef" = dataclasses.field()

    SnapshotId = field("SnapshotId")
    BlockIndex = field("BlockIndex")
    BlockData = field("BlockData")
    DataLength = field("DataLength")
    Checksum = field("Checksum")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    Progress = field("Progress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutSnapshotBlockRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSnapshotBlockRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompleteSnapshotResponse:
    boto3_raw_data: "type_defs.CompleteSnapshotResponseTypeDef" = dataclasses.field()

    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompleteSnapshotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompleteSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSnapshotBlockResponse:
    boto3_raw_data: "type_defs.GetSnapshotBlockResponseTypeDef" = dataclasses.field()

    DataLength = field("DataLength")
    BlockData = field("BlockData")
    Checksum = field("Checksum")
    ChecksumAlgorithm = field("ChecksumAlgorithm")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSnapshotBlockResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSnapshotBlockResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChangedBlocksResponse:
    boto3_raw_data: "type_defs.ListChangedBlocksResponseTypeDef" = dataclasses.field()

    @cached_property
    def ChangedBlocks(self):  # pragma: no cover
        return ChangedBlock.make_many(self.boto3_raw_data["ChangedBlocks"])

    ExpiryTime = field("ExpiryTime")
    VolumeSize = field("VolumeSize")
    BlockSize = field("BlockSize")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChangedBlocksResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChangedBlocksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSnapshotBlocksResponse:
    boto3_raw_data: "type_defs.ListSnapshotBlocksResponseTypeDef" = dataclasses.field()

    @cached_property
    def Blocks(self):  # pragma: no cover
        return Block.make_many(self.boto3_raw_data["Blocks"])

    ExpiryTime = field("ExpiryTime")
    VolumeSize = field("VolumeSize")
    BlockSize = field("BlockSize")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSnapshotBlocksResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSnapshotBlocksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSnapshotBlockResponse:
    boto3_raw_data: "type_defs.PutSnapshotBlockResponseTypeDef" = dataclasses.field()

    Checksum = field("Checksum")
    ChecksumAlgorithm = field("ChecksumAlgorithm")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutSnapshotBlockResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSnapshotBlockResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSnapshotRequest:
    boto3_raw_data: "type_defs.StartSnapshotRequestTypeDef" = dataclasses.field()

    VolumeSize = field("VolumeSize")
    ParentSnapshotId = field("ParentSnapshotId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    Description = field("Description")
    ClientToken = field("ClientToken")
    Encrypted = field("Encrypted")
    KmsKeyArn = field("KmsKeyArn")
    Timeout = field("Timeout")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSnapshotResponse:
    boto3_raw_data: "type_defs.StartSnapshotResponseTypeDef" = dataclasses.field()

    Description = field("Description")
    SnapshotId = field("SnapshotId")
    OwnerId = field("OwnerId")
    Status = field("Status")
    StartTime = field("StartTime")
    VolumeSize = field("VolumeSize")
    BlockSize = field("BlockSize")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ParentSnapshotId = field("ParentSnapshotId")
    KmsKeyArn = field("KmsKeyArn")
    SseType = field("SseType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSnapshotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
