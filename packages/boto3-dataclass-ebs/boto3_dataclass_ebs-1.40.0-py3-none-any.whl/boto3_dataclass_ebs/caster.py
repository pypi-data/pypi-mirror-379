# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ebs import type_defs as bs_td


class EBSCaster:

    def complete_snapshot(
        self,
        res: "bs_td.CompleteSnapshotResponseTypeDef",
    ) -> "dc_td.CompleteSnapshotResponse":
        return dc_td.CompleteSnapshotResponse.make_one(res)

    def get_snapshot_block(
        self,
        res: "bs_td.GetSnapshotBlockResponseTypeDef",
    ) -> "dc_td.GetSnapshotBlockResponse":
        return dc_td.GetSnapshotBlockResponse.make_one(res)

    def list_changed_blocks(
        self,
        res: "bs_td.ListChangedBlocksResponseTypeDef",
    ) -> "dc_td.ListChangedBlocksResponse":
        return dc_td.ListChangedBlocksResponse.make_one(res)

    def list_snapshot_blocks(
        self,
        res: "bs_td.ListSnapshotBlocksResponseTypeDef",
    ) -> "dc_td.ListSnapshotBlocksResponse":
        return dc_td.ListSnapshotBlocksResponse.make_one(res)

    def put_snapshot_block(
        self,
        res: "bs_td.PutSnapshotBlockResponseTypeDef",
    ) -> "dc_td.PutSnapshotBlockResponse":
        return dc_td.PutSnapshotBlockResponse.make_one(res)

    def start_snapshot(
        self,
        res: "bs_td.StartSnapshotResponseTypeDef",
    ) -> "dc_td.StartSnapshotResponse":
        return dc_td.StartSnapshotResponse.make_one(res)


ebs_caster = EBSCaster()
