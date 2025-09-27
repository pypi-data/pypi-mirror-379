# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_rds_data import type_defs as bs_td


class RDS_DATACaster:

    def batch_execute_statement(
        self,
        res: "bs_td.BatchExecuteStatementResponseTypeDef",
    ) -> "dc_td.BatchExecuteStatementResponse":
        return dc_td.BatchExecuteStatementResponse.make_one(res)

    def begin_transaction(
        self,
        res: "bs_td.BeginTransactionResponseTypeDef",
    ) -> "dc_td.BeginTransactionResponse":
        return dc_td.BeginTransactionResponse.make_one(res)

    def commit_transaction(
        self,
        res: "bs_td.CommitTransactionResponseTypeDef",
    ) -> "dc_td.CommitTransactionResponse":
        return dc_td.CommitTransactionResponse.make_one(res)

    def execute_sql(
        self,
        res: "bs_td.ExecuteSqlResponseTypeDef",
    ) -> "dc_td.ExecuteSqlResponse":
        return dc_td.ExecuteSqlResponse.make_one(res)

    def execute_statement(
        self,
        res: "bs_td.ExecuteStatementResponseTypeDef",
    ) -> "dc_td.ExecuteStatementResponse":
        return dc_td.ExecuteStatementResponse.make_one(res)

    def rollback_transaction(
        self,
        res: "bs_td.RollbackTransactionResponseTypeDef",
    ) -> "dc_td.RollbackTransactionResponse":
        return dc_td.RollbackTransactionResponse.make_one(res)


rds_data_caster = RDS_DATACaster()
