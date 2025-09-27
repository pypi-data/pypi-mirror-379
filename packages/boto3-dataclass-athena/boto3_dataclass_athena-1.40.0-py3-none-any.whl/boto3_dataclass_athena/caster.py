# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_athena import type_defs as bs_td


class ATHENACaster:

    def batch_get_named_query(
        self,
        res: "bs_td.BatchGetNamedQueryOutputTypeDef",
    ) -> "dc_td.BatchGetNamedQueryOutput":
        return dc_td.BatchGetNamedQueryOutput.make_one(res)

    def batch_get_prepared_statement(
        self,
        res: "bs_td.BatchGetPreparedStatementOutputTypeDef",
    ) -> "dc_td.BatchGetPreparedStatementOutput":
        return dc_td.BatchGetPreparedStatementOutput.make_one(res)

    def batch_get_query_execution(
        self,
        res: "bs_td.BatchGetQueryExecutionOutputTypeDef",
    ) -> "dc_td.BatchGetQueryExecutionOutput":
        return dc_td.BatchGetQueryExecutionOutput.make_one(res)

    def create_data_catalog(
        self,
        res: "bs_td.CreateDataCatalogOutputTypeDef",
    ) -> "dc_td.CreateDataCatalogOutput":
        return dc_td.CreateDataCatalogOutput.make_one(res)

    def create_named_query(
        self,
        res: "bs_td.CreateNamedQueryOutputTypeDef",
    ) -> "dc_td.CreateNamedQueryOutput":
        return dc_td.CreateNamedQueryOutput.make_one(res)

    def create_notebook(
        self,
        res: "bs_td.CreateNotebookOutputTypeDef",
    ) -> "dc_td.CreateNotebookOutput":
        return dc_td.CreateNotebookOutput.make_one(res)

    def create_presigned_notebook_url(
        self,
        res: "bs_td.CreatePresignedNotebookUrlResponseTypeDef",
    ) -> "dc_td.CreatePresignedNotebookUrlResponse":
        return dc_td.CreatePresignedNotebookUrlResponse.make_one(res)

    def delete_data_catalog(
        self,
        res: "bs_td.DeleteDataCatalogOutputTypeDef",
    ) -> "dc_td.DeleteDataCatalogOutput":
        return dc_td.DeleteDataCatalogOutput.make_one(res)

    def export_notebook(
        self,
        res: "bs_td.ExportNotebookOutputTypeDef",
    ) -> "dc_td.ExportNotebookOutput":
        return dc_td.ExportNotebookOutput.make_one(res)

    def get_calculation_execution(
        self,
        res: "bs_td.GetCalculationExecutionResponseTypeDef",
    ) -> "dc_td.GetCalculationExecutionResponse":
        return dc_td.GetCalculationExecutionResponse.make_one(res)

    def get_calculation_execution_code(
        self,
        res: "bs_td.GetCalculationExecutionCodeResponseTypeDef",
    ) -> "dc_td.GetCalculationExecutionCodeResponse":
        return dc_td.GetCalculationExecutionCodeResponse.make_one(res)

    def get_calculation_execution_status(
        self,
        res: "bs_td.GetCalculationExecutionStatusResponseTypeDef",
    ) -> "dc_td.GetCalculationExecutionStatusResponse":
        return dc_td.GetCalculationExecutionStatusResponse.make_one(res)

    def get_capacity_assignment_configuration(
        self,
        res: "bs_td.GetCapacityAssignmentConfigurationOutputTypeDef",
    ) -> "dc_td.GetCapacityAssignmentConfigurationOutput":
        return dc_td.GetCapacityAssignmentConfigurationOutput.make_one(res)

    def get_capacity_reservation(
        self,
        res: "bs_td.GetCapacityReservationOutputTypeDef",
    ) -> "dc_td.GetCapacityReservationOutput":
        return dc_td.GetCapacityReservationOutput.make_one(res)

    def get_data_catalog(
        self,
        res: "bs_td.GetDataCatalogOutputTypeDef",
    ) -> "dc_td.GetDataCatalogOutput":
        return dc_td.GetDataCatalogOutput.make_one(res)

    def get_database(
        self,
        res: "bs_td.GetDatabaseOutputTypeDef",
    ) -> "dc_td.GetDatabaseOutput":
        return dc_td.GetDatabaseOutput.make_one(res)

    def get_named_query(
        self,
        res: "bs_td.GetNamedQueryOutputTypeDef",
    ) -> "dc_td.GetNamedQueryOutput":
        return dc_td.GetNamedQueryOutput.make_one(res)

    def get_notebook_metadata(
        self,
        res: "bs_td.GetNotebookMetadataOutputTypeDef",
    ) -> "dc_td.GetNotebookMetadataOutput":
        return dc_td.GetNotebookMetadataOutput.make_one(res)

    def get_prepared_statement(
        self,
        res: "bs_td.GetPreparedStatementOutputTypeDef",
    ) -> "dc_td.GetPreparedStatementOutput":
        return dc_td.GetPreparedStatementOutput.make_one(res)

    def get_query_execution(
        self,
        res: "bs_td.GetQueryExecutionOutputTypeDef",
    ) -> "dc_td.GetQueryExecutionOutput":
        return dc_td.GetQueryExecutionOutput.make_one(res)

    def get_query_results(
        self,
        res: "bs_td.GetQueryResultsOutputTypeDef",
    ) -> "dc_td.GetQueryResultsOutput":
        return dc_td.GetQueryResultsOutput.make_one(res)

    def get_query_runtime_statistics(
        self,
        res: "bs_td.GetQueryRuntimeStatisticsOutputTypeDef",
    ) -> "dc_td.GetQueryRuntimeStatisticsOutput":
        return dc_td.GetQueryRuntimeStatisticsOutput.make_one(res)

    def get_session(
        self,
        res: "bs_td.GetSessionResponseTypeDef",
    ) -> "dc_td.GetSessionResponse":
        return dc_td.GetSessionResponse.make_one(res)

    def get_session_status(
        self,
        res: "bs_td.GetSessionStatusResponseTypeDef",
    ) -> "dc_td.GetSessionStatusResponse":
        return dc_td.GetSessionStatusResponse.make_one(res)

    def get_table_metadata(
        self,
        res: "bs_td.GetTableMetadataOutputTypeDef",
    ) -> "dc_td.GetTableMetadataOutput":
        return dc_td.GetTableMetadataOutput.make_one(res)

    def get_work_group(
        self,
        res: "bs_td.GetWorkGroupOutputTypeDef",
    ) -> "dc_td.GetWorkGroupOutput":
        return dc_td.GetWorkGroupOutput.make_one(res)

    def import_notebook(
        self,
        res: "bs_td.ImportNotebookOutputTypeDef",
    ) -> "dc_td.ImportNotebookOutput":
        return dc_td.ImportNotebookOutput.make_one(res)

    def list_application_dpu_sizes(
        self,
        res: "bs_td.ListApplicationDPUSizesOutputTypeDef",
    ) -> "dc_td.ListApplicationDPUSizesOutput":
        return dc_td.ListApplicationDPUSizesOutput.make_one(res)

    def list_calculation_executions(
        self,
        res: "bs_td.ListCalculationExecutionsResponseTypeDef",
    ) -> "dc_td.ListCalculationExecutionsResponse":
        return dc_td.ListCalculationExecutionsResponse.make_one(res)

    def list_capacity_reservations(
        self,
        res: "bs_td.ListCapacityReservationsOutputTypeDef",
    ) -> "dc_td.ListCapacityReservationsOutput":
        return dc_td.ListCapacityReservationsOutput.make_one(res)

    def list_data_catalogs(
        self,
        res: "bs_td.ListDataCatalogsOutputTypeDef",
    ) -> "dc_td.ListDataCatalogsOutput":
        return dc_td.ListDataCatalogsOutput.make_one(res)

    def list_databases(
        self,
        res: "bs_td.ListDatabasesOutputTypeDef",
    ) -> "dc_td.ListDatabasesOutput":
        return dc_td.ListDatabasesOutput.make_one(res)

    def list_engine_versions(
        self,
        res: "bs_td.ListEngineVersionsOutputTypeDef",
    ) -> "dc_td.ListEngineVersionsOutput":
        return dc_td.ListEngineVersionsOutput.make_one(res)

    def list_executors(
        self,
        res: "bs_td.ListExecutorsResponseTypeDef",
    ) -> "dc_td.ListExecutorsResponse":
        return dc_td.ListExecutorsResponse.make_one(res)

    def list_named_queries(
        self,
        res: "bs_td.ListNamedQueriesOutputTypeDef",
    ) -> "dc_td.ListNamedQueriesOutput":
        return dc_td.ListNamedQueriesOutput.make_one(res)

    def list_notebook_metadata(
        self,
        res: "bs_td.ListNotebookMetadataOutputTypeDef",
    ) -> "dc_td.ListNotebookMetadataOutput":
        return dc_td.ListNotebookMetadataOutput.make_one(res)

    def list_notebook_sessions(
        self,
        res: "bs_td.ListNotebookSessionsResponseTypeDef",
    ) -> "dc_td.ListNotebookSessionsResponse":
        return dc_td.ListNotebookSessionsResponse.make_one(res)

    def list_prepared_statements(
        self,
        res: "bs_td.ListPreparedStatementsOutputTypeDef",
    ) -> "dc_td.ListPreparedStatementsOutput":
        return dc_td.ListPreparedStatementsOutput.make_one(res)

    def list_query_executions(
        self,
        res: "bs_td.ListQueryExecutionsOutputTypeDef",
    ) -> "dc_td.ListQueryExecutionsOutput":
        return dc_td.ListQueryExecutionsOutput.make_one(res)

    def list_sessions(
        self,
        res: "bs_td.ListSessionsResponseTypeDef",
    ) -> "dc_td.ListSessionsResponse":
        return dc_td.ListSessionsResponse.make_one(res)

    def list_table_metadata(
        self,
        res: "bs_td.ListTableMetadataOutputTypeDef",
    ) -> "dc_td.ListTableMetadataOutput":
        return dc_td.ListTableMetadataOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def list_work_groups(
        self,
        res: "bs_td.ListWorkGroupsOutputTypeDef",
    ) -> "dc_td.ListWorkGroupsOutput":
        return dc_td.ListWorkGroupsOutput.make_one(res)

    def start_calculation_execution(
        self,
        res: "bs_td.StartCalculationExecutionResponseTypeDef",
    ) -> "dc_td.StartCalculationExecutionResponse":
        return dc_td.StartCalculationExecutionResponse.make_one(res)

    def start_query_execution(
        self,
        res: "bs_td.StartQueryExecutionOutputTypeDef",
    ) -> "dc_td.StartQueryExecutionOutput":
        return dc_td.StartQueryExecutionOutput.make_one(res)

    def start_session(
        self,
        res: "bs_td.StartSessionResponseTypeDef",
    ) -> "dc_td.StartSessionResponse":
        return dc_td.StartSessionResponse.make_one(res)

    def stop_calculation_execution(
        self,
        res: "bs_td.StopCalculationExecutionResponseTypeDef",
    ) -> "dc_td.StopCalculationExecutionResponse":
        return dc_td.StopCalculationExecutionResponse.make_one(res)

    def terminate_session(
        self,
        res: "bs_td.TerminateSessionResponseTypeDef",
    ) -> "dc_td.TerminateSessionResponse":
        return dc_td.TerminateSessionResponse.make_one(res)


athena_caster = ATHENACaster()
