# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_redshift_data import type_defs as bs_td


class REDSHIFT_DATACaster:

    def batch_execute_statement(
        self,
        res: "bs_td.BatchExecuteStatementOutputTypeDef",
    ) -> "dc_td.BatchExecuteStatementOutput":
        return dc_td.BatchExecuteStatementOutput.make_one(res)

    def cancel_statement(
        self,
        res: "bs_td.CancelStatementResponseTypeDef",
    ) -> "dc_td.CancelStatementResponse":
        return dc_td.CancelStatementResponse.make_one(res)

    def describe_statement(
        self,
        res: "bs_td.DescribeStatementResponseTypeDef",
    ) -> "dc_td.DescribeStatementResponse":
        return dc_td.DescribeStatementResponse.make_one(res)

    def describe_table(
        self,
        res: "bs_td.DescribeTableResponseTypeDef",
    ) -> "dc_td.DescribeTableResponse":
        return dc_td.DescribeTableResponse.make_one(res)

    def execute_statement(
        self,
        res: "bs_td.ExecuteStatementOutputTypeDef",
    ) -> "dc_td.ExecuteStatementOutput":
        return dc_td.ExecuteStatementOutput.make_one(res)

    def get_statement_result(
        self,
        res: "bs_td.GetStatementResultResponseTypeDef",
    ) -> "dc_td.GetStatementResultResponse":
        return dc_td.GetStatementResultResponse.make_one(res)

    def get_statement_result_v2(
        self,
        res: "bs_td.GetStatementResultV2ResponseTypeDef",
    ) -> "dc_td.GetStatementResultV2Response":
        return dc_td.GetStatementResultV2Response.make_one(res)

    def list_databases(
        self,
        res: "bs_td.ListDatabasesResponseTypeDef",
    ) -> "dc_td.ListDatabasesResponse":
        return dc_td.ListDatabasesResponse.make_one(res)

    def list_schemas(
        self,
        res: "bs_td.ListSchemasResponseTypeDef",
    ) -> "dc_td.ListSchemasResponse":
        return dc_td.ListSchemasResponse.make_one(res)

    def list_statements(
        self,
        res: "bs_td.ListStatementsResponseTypeDef",
    ) -> "dc_td.ListStatementsResponse":
        return dc_td.ListStatementsResponse.make_one(res)

    def list_tables(
        self,
        res: "bs_td.ListTablesResponseTypeDef",
    ) -> "dc_td.ListTablesResponse":
        return dc_td.ListTablesResponse.make_one(res)


redshift_data_caster = REDSHIFT_DATACaster()
