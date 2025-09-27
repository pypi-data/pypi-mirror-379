# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_docdb_elastic import type_defs as bs_td


class DOCDB_ELASTICCaster:

    def apply_pending_maintenance_action(
        self,
        res: "bs_td.ApplyPendingMaintenanceActionOutputTypeDef",
    ) -> "dc_td.ApplyPendingMaintenanceActionOutput":
        return dc_td.ApplyPendingMaintenanceActionOutput.make_one(res)

    def copy_cluster_snapshot(
        self,
        res: "bs_td.CopyClusterSnapshotOutputTypeDef",
    ) -> "dc_td.CopyClusterSnapshotOutput":
        return dc_td.CopyClusterSnapshotOutput.make_one(res)

    def create_cluster(
        self,
        res: "bs_td.CreateClusterOutputTypeDef",
    ) -> "dc_td.CreateClusterOutput":
        return dc_td.CreateClusterOutput.make_one(res)

    def create_cluster_snapshot(
        self,
        res: "bs_td.CreateClusterSnapshotOutputTypeDef",
    ) -> "dc_td.CreateClusterSnapshotOutput":
        return dc_td.CreateClusterSnapshotOutput.make_one(res)

    def delete_cluster(
        self,
        res: "bs_td.DeleteClusterOutputTypeDef",
    ) -> "dc_td.DeleteClusterOutput":
        return dc_td.DeleteClusterOutput.make_one(res)

    def delete_cluster_snapshot(
        self,
        res: "bs_td.DeleteClusterSnapshotOutputTypeDef",
    ) -> "dc_td.DeleteClusterSnapshotOutput":
        return dc_td.DeleteClusterSnapshotOutput.make_one(res)

    def get_cluster(
        self,
        res: "bs_td.GetClusterOutputTypeDef",
    ) -> "dc_td.GetClusterOutput":
        return dc_td.GetClusterOutput.make_one(res)

    def get_cluster_snapshot(
        self,
        res: "bs_td.GetClusterSnapshotOutputTypeDef",
    ) -> "dc_td.GetClusterSnapshotOutput":
        return dc_td.GetClusterSnapshotOutput.make_one(res)

    def get_pending_maintenance_action(
        self,
        res: "bs_td.GetPendingMaintenanceActionOutputTypeDef",
    ) -> "dc_td.GetPendingMaintenanceActionOutput":
        return dc_td.GetPendingMaintenanceActionOutput.make_one(res)

    def list_cluster_snapshots(
        self,
        res: "bs_td.ListClusterSnapshotsOutputTypeDef",
    ) -> "dc_td.ListClusterSnapshotsOutput":
        return dc_td.ListClusterSnapshotsOutput.make_one(res)

    def list_clusters(
        self,
        res: "bs_td.ListClustersOutputTypeDef",
    ) -> "dc_td.ListClustersOutput":
        return dc_td.ListClustersOutput.make_one(res)

    def list_pending_maintenance_actions(
        self,
        res: "bs_td.ListPendingMaintenanceActionsOutputTypeDef",
    ) -> "dc_td.ListPendingMaintenanceActionsOutput":
        return dc_td.ListPendingMaintenanceActionsOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def restore_cluster_from_snapshot(
        self,
        res: "bs_td.RestoreClusterFromSnapshotOutputTypeDef",
    ) -> "dc_td.RestoreClusterFromSnapshotOutput":
        return dc_td.RestoreClusterFromSnapshotOutput.make_one(res)

    def start_cluster(
        self,
        res: "bs_td.StartClusterOutputTypeDef",
    ) -> "dc_td.StartClusterOutput":
        return dc_td.StartClusterOutput.make_one(res)

    def stop_cluster(
        self,
        res: "bs_td.StopClusterOutputTypeDef",
    ) -> "dc_td.StopClusterOutput":
        return dc_td.StopClusterOutput.make_one(res)

    def update_cluster(
        self,
        res: "bs_td.UpdateClusterOutputTypeDef",
    ) -> "dc_td.UpdateClusterOutput":
        return dc_td.UpdateClusterOutput.make_one(res)


docdb_elastic_caster = DOCDB_ELASTICCaster()
