# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_discovery import type_defs as bs_td


class DISCOVERYCaster:

    def batch_delete_agents(
        self,
        res: "bs_td.BatchDeleteAgentsResponseTypeDef",
    ) -> "dc_td.BatchDeleteAgentsResponse":
        return dc_td.BatchDeleteAgentsResponse.make_one(res)

    def batch_delete_import_data(
        self,
        res: "bs_td.BatchDeleteImportDataResponseTypeDef",
    ) -> "dc_td.BatchDeleteImportDataResponse":
        return dc_td.BatchDeleteImportDataResponse.make_one(res)

    def create_application(
        self,
        res: "bs_td.CreateApplicationResponseTypeDef",
    ) -> "dc_td.CreateApplicationResponse":
        return dc_td.CreateApplicationResponse.make_one(res)

    def describe_agents(
        self,
        res: "bs_td.DescribeAgentsResponseTypeDef",
    ) -> "dc_td.DescribeAgentsResponse":
        return dc_td.DescribeAgentsResponse.make_one(res)

    def describe_batch_delete_configuration_task(
        self,
        res: "bs_td.DescribeBatchDeleteConfigurationTaskResponseTypeDef",
    ) -> "dc_td.DescribeBatchDeleteConfigurationTaskResponse":
        return dc_td.DescribeBatchDeleteConfigurationTaskResponse.make_one(res)

    def describe_configurations(
        self,
        res: "bs_td.DescribeConfigurationsResponseTypeDef",
    ) -> "dc_td.DescribeConfigurationsResponse":
        return dc_td.DescribeConfigurationsResponse.make_one(res)

    def describe_continuous_exports(
        self,
        res: "bs_td.DescribeContinuousExportsResponseTypeDef",
    ) -> "dc_td.DescribeContinuousExportsResponse":
        return dc_td.DescribeContinuousExportsResponse.make_one(res)

    def describe_export_configurations(
        self,
        res: "bs_td.DescribeExportConfigurationsResponseTypeDef",
    ) -> "dc_td.DescribeExportConfigurationsResponse":
        return dc_td.DescribeExportConfigurationsResponse.make_one(res)

    def describe_export_tasks(
        self,
        res: "bs_td.DescribeExportTasksResponseTypeDef",
    ) -> "dc_td.DescribeExportTasksResponse":
        return dc_td.DescribeExportTasksResponse.make_one(res)

    def describe_import_tasks(
        self,
        res: "bs_td.DescribeImportTasksResponseTypeDef",
    ) -> "dc_td.DescribeImportTasksResponse":
        return dc_td.DescribeImportTasksResponse.make_one(res)

    def describe_tags(
        self,
        res: "bs_td.DescribeTagsResponseTypeDef",
    ) -> "dc_td.DescribeTagsResponse":
        return dc_td.DescribeTagsResponse.make_one(res)

    def export_configurations(
        self,
        res: "bs_td.ExportConfigurationsResponseTypeDef",
    ) -> "dc_td.ExportConfigurationsResponse":
        return dc_td.ExportConfigurationsResponse.make_one(res)

    def get_discovery_summary(
        self,
        res: "bs_td.GetDiscoverySummaryResponseTypeDef",
    ) -> "dc_td.GetDiscoverySummaryResponse":
        return dc_td.GetDiscoverySummaryResponse.make_one(res)

    def list_configurations(
        self,
        res: "bs_td.ListConfigurationsResponseTypeDef",
    ) -> "dc_td.ListConfigurationsResponse":
        return dc_td.ListConfigurationsResponse.make_one(res)

    def list_server_neighbors(
        self,
        res: "bs_td.ListServerNeighborsResponseTypeDef",
    ) -> "dc_td.ListServerNeighborsResponse":
        return dc_td.ListServerNeighborsResponse.make_one(res)

    def start_batch_delete_configuration_task(
        self,
        res: "bs_td.StartBatchDeleteConfigurationTaskResponseTypeDef",
    ) -> "dc_td.StartBatchDeleteConfigurationTaskResponse":
        return dc_td.StartBatchDeleteConfigurationTaskResponse.make_one(res)

    def start_continuous_export(
        self,
        res: "bs_td.StartContinuousExportResponseTypeDef",
    ) -> "dc_td.StartContinuousExportResponse":
        return dc_td.StartContinuousExportResponse.make_one(res)

    def start_data_collection_by_agent_ids(
        self,
        res: "bs_td.StartDataCollectionByAgentIdsResponseTypeDef",
    ) -> "dc_td.StartDataCollectionByAgentIdsResponse":
        return dc_td.StartDataCollectionByAgentIdsResponse.make_one(res)

    def start_export_task(
        self,
        res: "bs_td.StartExportTaskResponseTypeDef",
    ) -> "dc_td.StartExportTaskResponse":
        return dc_td.StartExportTaskResponse.make_one(res)

    def start_import_task(
        self,
        res: "bs_td.StartImportTaskResponseTypeDef",
    ) -> "dc_td.StartImportTaskResponse":
        return dc_td.StartImportTaskResponse.make_one(res)

    def stop_continuous_export(
        self,
        res: "bs_td.StopContinuousExportResponseTypeDef",
    ) -> "dc_td.StopContinuousExportResponse":
        return dc_td.StopContinuousExportResponse.make_one(res)

    def stop_data_collection_by_agent_ids(
        self,
        res: "bs_td.StopDataCollectionByAgentIdsResponseTypeDef",
    ) -> "dc_td.StopDataCollectionByAgentIdsResponse":
        return dc_td.StopDataCollectionByAgentIdsResponse.make_one(res)


discovery_caster = DISCOVERYCaster()
