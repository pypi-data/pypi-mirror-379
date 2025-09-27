# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_dynamodb import type_defs as bs_td


class DYNAMODBCaster:

    def batch_execute_statement(
        self,
        res: "bs_td.BatchExecuteStatementOutputTypeDef",
    ) -> "dc_td.BatchExecuteStatementOutput":
        return dc_td.BatchExecuteStatementOutput.make_one(res)

    def batch_get_item(
        self,
        res: "bs_td.BatchGetItemOutputTypeDef",
    ) -> "dc_td.BatchGetItemOutput":
        return dc_td.BatchGetItemOutput.make_one(res)

    def batch_write_item(
        self,
        res: "bs_td.BatchWriteItemOutputTypeDef",
    ) -> "dc_td.BatchWriteItemOutput":
        return dc_td.BatchWriteItemOutput.make_one(res)

    def create_backup(
        self,
        res: "bs_td.CreateBackupOutputTypeDef",
    ) -> "dc_td.CreateBackupOutput":
        return dc_td.CreateBackupOutput.make_one(res)

    def create_global_table(
        self,
        res: "bs_td.CreateGlobalTableOutputTypeDef",
    ) -> "dc_td.CreateGlobalTableOutput":
        return dc_td.CreateGlobalTableOutput.make_one(res)

    def create_table(
        self,
        res: "bs_td.CreateTableOutputTypeDef",
    ) -> "dc_td.CreateTableOutput":
        return dc_td.CreateTableOutput.make_one(res)

    def delete_backup(
        self,
        res: "bs_td.DeleteBackupOutputTypeDef",
    ) -> "dc_td.DeleteBackupOutput":
        return dc_td.DeleteBackupOutput.make_one(res)

    def delete_item(
        self,
        res: "bs_td.DeleteItemOutputTypeDef",
    ) -> "dc_td.DeleteItemOutput":
        return dc_td.DeleteItemOutput.make_one(res)

    def delete_resource_policy(
        self,
        res: "bs_td.DeleteResourcePolicyOutputTypeDef",
    ) -> "dc_td.DeleteResourcePolicyOutput":
        return dc_td.DeleteResourcePolicyOutput.make_one(res)

    def delete_table(
        self,
        res: "bs_td.DeleteTableOutputTypeDef",
    ) -> "dc_td.DeleteTableOutput":
        return dc_td.DeleteTableOutput.make_one(res)

    def describe_backup(
        self,
        res: "bs_td.DescribeBackupOutputTypeDef",
    ) -> "dc_td.DescribeBackupOutput":
        return dc_td.DescribeBackupOutput.make_one(res)

    def describe_continuous_backups(
        self,
        res: "bs_td.DescribeContinuousBackupsOutputTypeDef",
    ) -> "dc_td.DescribeContinuousBackupsOutput":
        return dc_td.DescribeContinuousBackupsOutput.make_one(res)

    def describe_contributor_insights(
        self,
        res: "bs_td.DescribeContributorInsightsOutputTypeDef",
    ) -> "dc_td.DescribeContributorInsightsOutput":
        return dc_td.DescribeContributorInsightsOutput.make_one(res)

    def describe_endpoints(
        self,
        res: "bs_td.DescribeEndpointsResponseTypeDef",
    ) -> "dc_td.DescribeEndpointsResponse":
        return dc_td.DescribeEndpointsResponse.make_one(res)

    def describe_export(
        self,
        res: "bs_td.DescribeExportOutputTypeDef",
    ) -> "dc_td.DescribeExportOutput":
        return dc_td.DescribeExportOutput.make_one(res)

    def describe_global_table(
        self,
        res: "bs_td.DescribeGlobalTableOutputTypeDef",
    ) -> "dc_td.DescribeGlobalTableOutput":
        return dc_td.DescribeGlobalTableOutput.make_one(res)

    def describe_global_table_settings(
        self,
        res: "bs_td.DescribeGlobalTableSettingsOutputTypeDef",
    ) -> "dc_td.DescribeGlobalTableSettingsOutput":
        return dc_td.DescribeGlobalTableSettingsOutput.make_one(res)

    def describe_import(
        self,
        res: "bs_td.DescribeImportOutputTypeDef",
    ) -> "dc_td.DescribeImportOutput":
        return dc_td.DescribeImportOutput.make_one(res)

    def describe_kinesis_streaming_destination(
        self,
        res: "bs_td.DescribeKinesisStreamingDestinationOutputTypeDef",
    ) -> "dc_td.DescribeKinesisStreamingDestinationOutput":
        return dc_td.DescribeKinesisStreamingDestinationOutput.make_one(res)

    def describe_limits(
        self,
        res: "bs_td.DescribeLimitsOutputTypeDef",
    ) -> "dc_td.DescribeLimitsOutput":
        return dc_td.DescribeLimitsOutput.make_one(res)

    def describe_table(
        self,
        res: "bs_td.DescribeTableOutputTypeDef",
    ) -> "dc_td.DescribeTableOutput":
        return dc_td.DescribeTableOutput.make_one(res)

    def describe_table_replica_auto_scaling(
        self,
        res: "bs_td.DescribeTableReplicaAutoScalingOutputTypeDef",
    ) -> "dc_td.DescribeTableReplicaAutoScalingOutput":
        return dc_td.DescribeTableReplicaAutoScalingOutput.make_one(res)

    def describe_time_to_live(
        self,
        res: "bs_td.DescribeTimeToLiveOutputTypeDef",
    ) -> "dc_td.DescribeTimeToLiveOutput":
        return dc_td.DescribeTimeToLiveOutput.make_one(res)

    def disable_kinesis_streaming_destination(
        self,
        res: "bs_td.KinesisStreamingDestinationOutputTypeDef",
    ) -> "dc_td.KinesisStreamingDestinationOutput":
        return dc_td.KinesisStreamingDestinationOutput.make_one(res)

    def enable_kinesis_streaming_destination(
        self,
        res: "bs_td.KinesisStreamingDestinationOutputTypeDef",
    ) -> "dc_td.KinesisStreamingDestinationOutput":
        return dc_td.KinesisStreamingDestinationOutput.make_one(res)

    def execute_statement(
        self,
        res: "bs_td.ExecuteStatementOutputTypeDef",
    ) -> "dc_td.ExecuteStatementOutput":
        return dc_td.ExecuteStatementOutput.make_one(res)

    def execute_transaction(
        self,
        res: "bs_td.ExecuteTransactionOutputTypeDef",
    ) -> "dc_td.ExecuteTransactionOutput":
        return dc_td.ExecuteTransactionOutput.make_one(res)

    def export_table_to_point_in_time(
        self,
        res: "bs_td.ExportTableToPointInTimeOutputTypeDef",
    ) -> "dc_td.ExportTableToPointInTimeOutput":
        return dc_td.ExportTableToPointInTimeOutput.make_one(res)

    def get_item(
        self,
        res: "bs_td.GetItemOutputTypeDef",
    ) -> "dc_td.GetItemOutput":
        return dc_td.GetItemOutput.make_one(res)

    def get_resource_policy(
        self,
        res: "bs_td.GetResourcePolicyOutputTypeDef",
    ) -> "dc_td.GetResourcePolicyOutput":
        return dc_td.GetResourcePolicyOutput.make_one(res)

    def import_table(
        self,
        res: "bs_td.ImportTableOutputTypeDef",
    ) -> "dc_td.ImportTableOutput":
        return dc_td.ImportTableOutput.make_one(res)

    def list_backups(
        self,
        res: "bs_td.ListBackupsOutputTypeDef",
    ) -> "dc_td.ListBackupsOutput":
        return dc_td.ListBackupsOutput.make_one(res)

    def list_contributor_insights(
        self,
        res: "bs_td.ListContributorInsightsOutputTypeDef",
    ) -> "dc_td.ListContributorInsightsOutput":
        return dc_td.ListContributorInsightsOutput.make_one(res)

    def list_exports(
        self,
        res: "bs_td.ListExportsOutputTypeDef",
    ) -> "dc_td.ListExportsOutput":
        return dc_td.ListExportsOutput.make_one(res)

    def list_global_tables(
        self,
        res: "bs_td.ListGlobalTablesOutputTypeDef",
    ) -> "dc_td.ListGlobalTablesOutput":
        return dc_td.ListGlobalTablesOutput.make_one(res)

    def list_imports(
        self,
        res: "bs_td.ListImportsOutputTypeDef",
    ) -> "dc_td.ListImportsOutput":
        return dc_td.ListImportsOutput.make_one(res)

    def list_tables(
        self,
        res: "bs_td.ListTablesOutputTypeDef",
    ) -> "dc_td.ListTablesOutput":
        return dc_td.ListTablesOutput.make_one(res)

    def list_tags_of_resource(
        self,
        res: "bs_td.ListTagsOfResourceOutputTypeDef",
    ) -> "dc_td.ListTagsOfResourceOutput":
        return dc_td.ListTagsOfResourceOutput.make_one(res)

    def put_item(
        self,
        res: "bs_td.PutItemOutputTypeDef",
    ) -> "dc_td.PutItemOutput":
        return dc_td.PutItemOutput.make_one(res)

    def put_resource_policy(
        self,
        res: "bs_td.PutResourcePolicyOutputTypeDef",
    ) -> "dc_td.PutResourcePolicyOutput":
        return dc_td.PutResourcePolicyOutput.make_one(res)

    def query(
        self,
        res: "bs_td.QueryOutputTypeDef",
    ) -> "dc_td.QueryOutput":
        return dc_td.QueryOutput.make_one(res)

    def restore_table_from_backup(
        self,
        res: "bs_td.RestoreTableFromBackupOutputTypeDef",
    ) -> "dc_td.RestoreTableFromBackupOutput":
        return dc_td.RestoreTableFromBackupOutput.make_one(res)

    def restore_table_to_point_in_time(
        self,
        res: "bs_td.RestoreTableToPointInTimeOutputTypeDef",
    ) -> "dc_td.RestoreTableToPointInTimeOutput":
        return dc_td.RestoreTableToPointInTimeOutput.make_one(res)

    def scan(
        self,
        res: "bs_td.ScanOutputTypeDef",
    ) -> "dc_td.ScanOutput":
        return dc_td.ScanOutput.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def transact_get_items(
        self,
        res: "bs_td.TransactGetItemsOutputTypeDef",
    ) -> "dc_td.TransactGetItemsOutput":
        return dc_td.TransactGetItemsOutput.make_one(res)

    def transact_write_items(
        self,
        res: "bs_td.TransactWriteItemsOutputTypeDef",
    ) -> "dc_td.TransactWriteItemsOutput":
        return dc_td.TransactWriteItemsOutput.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_continuous_backups(
        self,
        res: "bs_td.UpdateContinuousBackupsOutputTypeDef",
    ) -> "dc_td.UpdateContinuousBackupsOutput":
        return dc_td.UpdateContinuousBackupsOutput.make_one(res)

    def update_contributor_insights(
        self,
        res: "bs_td.UpdateContributorInsightsOutputTypeDef",
    ) -> "dc_td.UpdateContributorInsightsOutput":
        return dc_td.UpdateContributorInsightsOutput.make_one(res)

    def update_global_table(
        self,
        res: "bs_td.UpdateGlobalTableOutputTypeDef",
    ) -> "dc_td.UpdateGlobalTableOutput":
        return dc_td.UpdateGlobalTableOutput.make_one(res)

    def update_global_table_settings(
        self,
        res: "bs_td.UpdateGlobalTableSettingsOutputTypeDef",
    ) -> "dc_td.UpdateGlobalTableSettingsOutput":
        return dc_td.UpdateGlobalTableSettingsOutput.make_one(res)

    def update_item(
        self,
        res: "bs_td.UpdateItemOutputTypeDef",
    ) -> "dc_td.UpdateItemOutput":
        return dc_td.UpdateItemOutput.make_one(res)

    def update_kinesis_streaming_destination(
        self,
        res: "bs_td.UpdateKinesisStreamingDestinationOutputTypeDef",
    ) -> "dc_td.UpdateKinesisStreamingDestinationOutput":
        return dc_td.UpdateKinesisStreamingDestinationOutput.make_one(res)

    def update_table(
        self,
        res: "bs_td.UpdateTableOutputTypeDef",
    ) -> "dc_td.UpdateTableOutput":
        return dc_td.UpdateTableOutput.make_one(res)

    def update_table_replica_auto_scaling(
        self,
        res: "bs_td.UpdateTableReplicaAutoScalingOutputTypeDef",
    ) -> "dc_td.UpdateTableReplicaAutoScalingOutput":
        return dc_td.UpdateTableReplicaAutoScalingOutput.make_one(res)

    def update_time_to_live(
        self,
        res: "bs_td.UpdateTimeToLiveOutputTypeDef",
    ) -> "dc_td.UpdateTimeToLiveOutput":
        return dc_td.UpdateTimeToLiveOutput.make_one(res)


dynamodb_caster = DYNAMODBCaster()
