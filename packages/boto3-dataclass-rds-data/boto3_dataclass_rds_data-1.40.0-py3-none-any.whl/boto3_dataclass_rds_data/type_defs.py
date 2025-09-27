# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_rds_data import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ArrayValueOutput:
    boto3_raw_data: "type_defs.ArrayValueOutputTypeDef" = dataclasses.field()

    booleanValues = field("booleanValues")
    longValues = field("longValues")
    doubleValues = field("doubleValues")
    stringValues = field("stringValues")
    arrayValues = field("arrayValues")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ArrayValueOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArrayValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArrayValue:
    boto3_raw_data: "type_defs.ArrayValueTypeDef" = dataclasses.field()

    booleanValues = field("booleanValues")
    longValues = field("longValues")
    doubleValues = field("doubleValues")
    stringValues = field("stringValues")
    arrayValues = field("arrayValues")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ArrayValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ArrayValueTypeDef"]]
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
class BeginTransactionRequest:
    boto3_raw_data: "type_defs.BeginTransactionRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    secretArn = field("secretArn")
    database = field("database")
    schema = field("schema")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BeginTransactionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BeginTransactionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColumnMetadata:
    boto3_raw_data: "type_defs.ColumnMetadataTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")
    typeName = field("typeName")
    label = field("label")
    schemaName = field("schemaName")
    tableName = field("tableName")
    isAutoIncrement = field("isAutoIncrement")
    isSigned = field("isSigned")
    isCurrency = field("isCurrency")
    isCaseSensitive = field("isCaseSensitive")
    nullable = field("nullable")
    precision = field("precision")
    scale = field("scale")
    arrayBaseColumnType = field("arrayBaseColumnType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ColumnMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ColumnMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommitTransactionRequest:
    boto3_raw_data: "type_defs.CommitTransactionRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    secretArn = field("secretArn")
    transactionId = field("transactionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommitTransactionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommitTransactionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteSqlRequest:
    boto3_raw_data: "type_defs.ExecuteSqlRequestTypeDef" = dataclasses.field()

    dbClusterOrInstanceArn = field("dbClusterOrInstanceArn")
    awsSecretStoreArn = field("awsSecretStoreArn")
    sqlStatements = field("sqlStatements")
    database = field("database")
    schema = field("schema")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExecuteSqlRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteSqlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResultSetOptions:
    boto3_raw_data: "type_defs.ResultSetOptionsTypeDef" = dataclasses.field()

    decimalReturnType = field("decimalReturnType")
    longReturnType = field("longReturnType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResultSetOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResultSetOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RollbackTransactionRequest:
    boto3_raw_data: "type_defs.RollbackTransactionRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    secretArn = field("secretArn")
    transactionId = field("transactionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RollbackTransactionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RollbackTransactionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StructValue:
    boto3_raw_data: "type_defs.StructValueTypeDef" = dataclasses.field()

    attributes = field("attributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StructValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StructValueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldOutput:
    boto3_raw_data: "type_defs.FieldOutputTypeDef" = dataclasses.field()

    isNull = field("isNull")
    booleanValue = field("booleanValue")
    longValue = field("longValue")
    doubleValue = field("doubleValue")
    stringValue = field("stringValue")
    blobValue = field("blobValue")

    @cached_property
    def arrayValue(self):  # pragma: no cover
        return ArrayValueOutput.make_one(self.boto3_raw_data["arrayValue"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BeginTransactionResponse:
    boto3_raw_data: "type_defs.BeginTransactionResponseTypeDef" = dataclasses.field()

    transactionId = field("transactionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BeginTransactionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BeginTransactionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommitTransactionResponse:
    boto3_raw_data: "type_defs.CommitTransactionResponseTypeDef" = dataclasses.field()

    transactionStatus = field("transactionStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommitTransactionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommitTransactionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RollbackTransactionResponse:
    boto3_raw_data: "type_defs.RollbackTransactionResponseTypeDef" = dataclasses.field()

    transactionStatus = field("transactionStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RollbackTransactionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RollbackTransactionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResultSetMetadata:
    boto3_raw_data: "type_defs.ResultSetMetadataTypeDef" = dataclasses.field()

    columnCount = field("columnCount")

    @cached_property
    def columnMetadata(self):  # pragma: no cover
        return ColumnMetadata.make_many(self.boto3_raw_data["columnMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResultSetMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResultSetMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Value:
    boto3_raw_data: "type_defs.ValueTypeDef" = dataclasses.field()

    isNull = field("isNull")
    bitValue = field("bitValue")
    bigIntValue = field("bigIntValue")
    intValue = field("intValue")
    doubleValue = field("doubleValue")
    realValue = field("realValue")
    stringValue = field("stringValue")
    blobValue = field("blobValue")
    arrayValues = field("arrayValues")

    @cached_property
    def structValue(self):  # pragma: no cover
        return StructValue.make_one(self.boto3_raw_data["structValue"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ValueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteStatementResponse:
    boto3_raw_data: "type_defs.ExecuteStatementResponseTypeDef" = dataclasses.field()

    @cached_property
    def records(self):  # pragma: no cover
        return FieldOutput.make_many(self.boto3_raw_data["records"])

    @cached_property
    def columnMetadata(self):  # pragma: no cover
        return ColumnMetadata.make_many(self.boto3_raw_data["columnMetadata"])

    numberOfRecordsUpdated = field("numberOfRecordsUpdated")

    @cached_property
    def generatedFields(self):  # pragma: no cover
        return FieldOutput.make_many(self.boto3_raw_data["generatedFields"])

    formattedRecords = field("formattedRecords")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteStatementResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteStatementResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResult:
    boto3_raw_data: "type_defs.UpdateResultTypeDef" = dataclasses.field()

    @cached_property
    def generatedFields(self):  # pragma: no cover
        return FieldOutput.make_many(self.boto3_raw_data["generatedFields"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Field:
    boto3_raw_data: "type_defs.FieldTypeDef" = dataclasses.field()

    isNull = field("isNull")
    booleanValue = field("booleanValue")
    longValue = field("longValue")
    doubleValue = field("doubleValue")
    stringValue = field("stringValue")
    blobValue = field("blobValue")
    arrayValue = field("arrayValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Record:
    boto3_raw_data: "type_defs.RecordTypeDef" = dataclasses.field()

    @cached_property
    def values(self):  # pragma: no cover
        return Value.make_many(self.boto3_raw_data["values"])

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
class BatchExecuteStatementResponse:
    boto3_raw_data: "type_defs.BatchExecuteStatementResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def updateResults(self):  # pragma: no cover
        return UpdateResult.make_many(self.boto3_raw_data["updateResults"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchExecuteStatementResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchExecuteStatementResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResultFrame:
    boto3_raw_data: "type_defs.ResultFrameTypeDef" = dataclasses.field()

    @cached_property
    def resultSetMetadata(self):  # pragma: no cover
        return ResultSetMetadata.make_one(self.boto3_raw_data["resultSetMetadata"])

    @cached_property
    def records(self):  # pragma: no cover
        return Record.make_many(self.boto3_raw_data["records"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResultFrameTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResultFrameTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SqlParameter:
    boto3_raw_data: "type_defs.SqlParameterTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")
    typeHint = field("typeHint")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SqlParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SqlParameterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SqlStatementResult:
    boto3_raw_data: "type_defs.SqlStatementResultTypeDef" = dataclasses.field()

    @cached_property
    def resultFrame(self):  # pragma: no cover
        return ResultFrame.make_one(self.boto3_raw_data["resultFrame"])

    numberOfRecordsUpdated = field("numberOfRecordsUpdated")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SqlStatementResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SqlStatementResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchExecuteStatementRequest:
    boto3_raw_data: "type_defs.BatchExecuteStatementRequestTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")
    secretArn = field("secretArn")
    sql = field("sql")
    database = field("database")
    schema = field("schema")

    @cached_property
    def parameterSets(self):  # pragma: no cover
        return SqlParameter.make_many(self.boto3_raw_data["parameterSets"])

    transactionId = field("transactionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchExecuteStatementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchExecuteStatementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteStatementRequest:
    boto3_raw_data: "type_defs.ExecuteStatementRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    secretArn = field("secretArn")
    sql = field("sql")
    database = field("database")
    schema = field("schema")

    @cached_property
    def parameters(self):  # pragma: no cover
        return SqlParameter.make_many(self.boto3_raw_data["parameters"])

    transactionId = field("transactionId")
    includeResultMetadata = field("includeResultMetadata")
    continueAfterTimeout = field("continueAfterTimeout")

    @cached_property
    def resultSetOptions(self):  # pragma: no cover
        return ResultSetOptions.make_one(self.boto3_raw_data["resultSetOptions"])

    formatRecordsAs = field("formatRecordsAs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteStatementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteStatementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteSqlResponse:
    boto3_raw_data: "type_defs.ExecuteSqlResponseTypeDef" = dataclasses.field()

    @cached_property
    def sqlStatementResults(self):  # pragma: no cover
        return SqlStatementResult.make_many(self.boto3_raw_data["sqlStatementResults"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteSqlResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteSqlResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
