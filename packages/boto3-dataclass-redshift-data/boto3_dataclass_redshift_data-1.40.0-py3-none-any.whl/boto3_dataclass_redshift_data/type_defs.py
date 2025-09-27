# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_redshift_data import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class BatchExecuteStatementInput:
    boto3_raw_data: "type_defs.BatchExecuteStatementInputTypeDef" = dataclasses.field()

    Sqls = field("Sqls")
    ClientToken = field("ClientToken")
    ClusterIdentifier = field("ClusterIdentifier")
    Database = field("Database")
    DbUser = field("DbUser")
    ResultFormat = field("ResultFormat")
    SecretArn = field("SecretArn")
    SessionId = field("SessionId")
    SessionKeepAliveSeconds = field("SessionKeepAliveSeconds")
    StatementName = field("StatementName")
    WithEvent = field("WithEvent")
    WorkgroupName = field("WorkgroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchExecuteStatementInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchExecuteStatementInputTypeDef"]
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
class CancelStatementRequest:
    boto3_raw_data: "type_defs.CancelStatementRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelStatementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelStatementRequestTypeDef"]
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

    columnDefault = field("columnDefault")
    isCaseSensitive = field("isCaseSensitive")
    isCurrency = field("isCurrency")
    isSigned = field("isSigned")
    label = field("label")
    length = field("length")
    name = field("name")
    nullable = field("nullable")
    precision = field("precision")
    scale = field("scale")
    schemaName = field("schemaName")
    tableName = field("tableName")
    typeName = field("typeName")

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
class DescribeStatementRequest:
    boto3_raw_data: "type_defs.DescribeStatementRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStatementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStatementRequestTypeDef"]
        ],
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
class SubStatementData:
    boto3_raw_data: "type_defs.SubStatementDataTypeDef" = dataclasses.field()

    Id = field("Id")
    CreatedAt = field("CreatedAt")
    Duration = field("Duration")
    Error = field("Error")
    HasResultSet = field("HasResultSet")
    QueryString = field("QueryString")
    RedshiftQueryId = field("RedshiftQueryId")
    ResultRows = field("ResultRows")
    ResultSize = field("ResultSize")
    Status = field("Status")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubStatementDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubStatementDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PaginatorConfig:
    boto3_raw_data: "type_defs.PaginatorConfigTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    PageSize = field("PageSize")
    StartingToken = field("StartingToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PaginatorConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PaginatorConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTableRequest:
    boto3_raw_data: "type_defs.DescribeTableRequestTypeDef" = dataclasses.field()

    Database = field("Database")
    ClusterIdentifier = field("ClusterIdentifier")
    ConnectedDatabase = field("ConnectedDatabase")
    DbUser = field("DbUser")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    Schema = field("Schema")
    SecretArn = field("SecretArn")
    Table = field("Table")
    WorkgroupName = field("WorkgroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTableRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTableRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Field:
    boto3_raw_data: "type_defs.FieldTypeDef" = dataclasses.field()

    blobValue = field("blobValue")
    booleanValue = field("booleanValue")
    doubleValue = field("doubleValue")
    isNull = field("isNull")
    longValue = field("longValue")
    stringValue = field("stringValue")

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
class GetStatementResultRequest:
    boto3_raw_data: "type_defs.GetStatementResultRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStatementResultRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStatementResultRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStatementResultV2Request:
    boto3_raw_data: "type_defs.GetStatementResultV2RequestTypeDef" = dataclasses.field()

    Id = field("Id")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStatementResultV2RequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStatementResultV2RequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryRecords:
    boto3_raw_data: "type_defs.QueryRecordsTypeDef" = dataclasses.field()

    CSVRecords = field("CSVRecords")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryRecordsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryRecordsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatabasesRequest:
    boto3_raw_data: "type_defs.ListDatabasesRequestTypeDef" = dataclasses.field()

    Database = field("Database")
    ClusterIdentifier = field("ClusterIdentifier")
    DbUser = field("DbUser")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    SecretArn = field("SecretArn")
    WorkgroupName = field("WorkgroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatabasesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatabasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSchemasRequest:
    boto3_raw_data: "type_defs.ListSchemasRequestTypeDef" = dataclasses.field()

    Database = field("Database")
    ClusterIdentifier = field("ClusterIdentifier")
    ConnectedDatabase = field("ConnectedDatabase")
    DbUser = field("DbUser")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    SchemaPattern = field("SchemaPattern")
    SecretArn = field("SecretArn")
    WorkgroupName = field("WorkgroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSchemasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchemasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStatementsRequest:
    boto3_raw_data: "type_defs.ListStatementsRequestTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    Database = field("Database")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    RoleLevel = field("RoleLevel")
    StatementName = field("StatementName")
    Status = field("Status")
    WorkgroupName = field("WorkgroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStatementsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStatementsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTablesRequest:
    boto3_raw_data: "type_defs.ListTablesRequestTypeDef" = dataclasses.field()

    Database = field("Database")
    ClusterIdentifier = field("ClusterIdentifier")
    ConnectedDatabase = field("ConnectedDatabase")
    DbUser = field("DbUser")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    SchemaPattern = field("SchemaPattern")
    SecretArn = field("SecretArn")
    TablePattern = field("TablePattern")
    WorkgroupName = field("WorkgroupName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTablesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTablesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableMember:
    boto3_raw_data: "type_defs.TableMemberTypeDef" = dataclasses.field()

    name = field("name")
    schema = field("schema")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TableMemberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TableMemberTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchExecuteStatementOutput:
    boto3_raw_data: "type_defs.BatchExecuteStatementOutputTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    CreatedAt = field("CreatedAt")
    Database = field("Database")
    DbGroups = field("DbGroups")
    DbUser = field("DbUser")
    Id = field("Id")
    SecretArn = field("SecretArn")
    SessionId = field("SessionId")
    WorkgroupName = field("WorkgroupName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchExecuteStatementOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchExecuteStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelStatementResponse:
    boto3_raw_data: "type_defs.CancelStatementResponseTypeDef" = dataclasses.field()

    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelStatementResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelStatementResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteStatementOutput:
    boto3_raw_data: "type_defs.ExecuteStatementOutputTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    CreatedAt = field("CreatedAt")
    Database = field("Database")
    DbGroups = field("DbGroups")
    DbUser = field("DbUser")
    Id = field("Id")
    SecretArn = field("SecretArn")
    SessionId = field("SessionId")
    WorkgroupName = field("WorkgroupName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteStatementOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatabasesResponse:
    boto3_raw_data: "type_defs.ListDatabasesResponseTypeDef" = dataclasses.field()

    Databases = field("Databases")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatabasesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatabasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSchemasResponse:
    boto3_raw_data: "type_defs.ListSchemasResponseTypeDef" = dataclasses.field()

    Schemas = field("Schemas")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSchemasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchemasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTableResponse:
    boto3_raw_data: "type_defs.DescribeTableResponseTypeDef" = dataclasses.field()

    @cached_property
    def ColumnList(self):  # pragma: no cover
        return ColumnMetadata.make_many(self.boto3_raw_data["ColumnList"])

    TableName = field("TableName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTableResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTableResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteStatementInput:
    boto3_raw_data: "type_defs.ExecuteStatementInputTypeDef" = dataclasses.field()

    Sql = field("Sql")
    ClientToken = field("ClientToken")
    ClusterIdentifier = field("ClusterIdentifier")
    Database = field("Database")
    DbUser = field("DbUser")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return SqlParameter.make_many(self.boto3_raw_data["Parameters"])

    ResultFormat = field("ResultFormat")
    SecretArn = field("SecretArn")
    SessionId = field("SessionId")
    SessionKeepAliveSeconds = field("SessionKeepAliveSeconds")
    StatementName = field("StatementName")
    WithEvent = field("WithEvent")
    WorkgroupName = field("WorkgroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteStatementInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteStatementInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatementData:
    boto3_raw_data: "type_defs.StatementDataTypeDef" = dataclasses.field()

    Id = field("Id")
    CreatedAt = field("CreatedAt")
    IsBatchStatement = field("IsBatchStatement")

    @cached_property
    def QueryParameters(self):  # pragma: no cover
        return SqlParameter.make_many(self.boto3_raw_data["QueryParameters"])

    QueryString = field("QueryString")
    QueryStrings = field("QueryStrings")
    ResultFormat = field("ResultFormat")
    SecretArn = field("SecretArn")
    SessionId = field("SessionId")
    StatementName = field("StatementName")
    Status = field("Status")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatementDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatementDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStatementResponse:
    boto3_raw_data: "type_defs.DescribeStatementResponseTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    CreatedAt = field("CreatedAt")
    Database = field("Database")
    DbUser = field("DbUser")
    Duration = field("Duration")
    Error = field("Error")
    HasResultSet = field("HasResultSet")
    Id = field("Id")

    @cached_property
    def QueryParameters(self):  # pragma: no cover
        return SqlParameter.make_many(self.boto3_raw_data["QueryParameters"])

    QueryString = field("QueryString")
    RedshiftPid = field("RedshiftPid")
    RedshiftQueryId = field("RedshiftQueryId")
    ResultFormat = field("ResultFormat")
    ResultRows = field("ResultRows")
    ResultSize = field("ResultSize")
    SecretArn = field("SecretArn")
    SessionId = field("SessionId")
    Status = field("Status")

    @cached_property
    def SubStatements(self):  # pragma: no cover
        return SubStatementData.make_many(self.boto3_raw_data["SubStatements"])

    UpdatedAt = field("UpdatedAt")
    WorkgroupName = field("WorkgroupName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStatementResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStatementResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTableRequestPaginate:
    boto3_raw_data: "type_defs.DescribeTableRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Database = field("Database")
    ClusterIdentifier = field("ClusterIdentifier")
    ConnectedDatabase = field("ConnectedDatabase")
    DbUser = field("DbUser")
    Schema = field("Schema")
    SecretArn = field("SecretArn")
    Table = field("Table")
    WorkgroupName = field("WorkgroupName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTableRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTableRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStatementResultRequestPaginate:
    boto3_raw_data: "type_defs.GetStatementResultRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetStatementResultRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStatementResultRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStatementResultV2RequestPaginate:
    boto3_raw_data: "type_defs.GetStatementResultV2RequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetStatementResultV2RequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStatementResultV2RequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatabasesRequestPaginate:
    boto3_raw_data: "type_defs.ListDatabasesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Database = field("Database")
    ClusterIdentifier = field("ClusterIdentifier")
    DbUser = field("DbUser")
    SecretArn = field("SecretArn")
    WorkgroupName = field("WorkgroupName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatabasesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatabasesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSchemasRequestPaginate:
    boto3_raw_data: "type_defs.ListSchemasRequestPaginateTypeDef" = dataclasses.field()

    Database = field("Database")
    ClusterIdentifier = field("ClusterIdentifier")
    ConnectedDatabase = field("ConnectedDatabase")
    DbUser = field("DbUser")
    SchemaPattern = field("SchemaPattern")
    SecretArn = field("SecretArn")
    WorkgroupName = field("WorkgroupName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSchemasRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchemasRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStatementsRequestPaginate:
    boto3_raw_data: "type_defs.ListStatementsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    Database = field("Database")
    RoleLevel = field("RoleLevel")
    StatementName = field("StatementName")
    Status = field("Status")
    WorkgroupName = field("WorkgroupName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListStatementsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStatementsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTablesRequestPaginate:
    boto3_raw_data: "type_defs.ListTablesRequestPaginateTypeDef" = dataclasses.field()

    Database = field("Database")
    ClusterIdentifier = field("ClusterIdentifier")
    ConnectedDatabase = field("ConnectedDatabase")
    DbUser = field("DbUser")
    SchemaPattern = field("SchemaPattern")
    SecretArn = field("SecretArn")
    TablePattern = field("TablePattern")
    WorkgroupName = field("WorkgroupName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTablesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTablesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStatementResultResponse:
    boto3_raw_data: "type_defs.GetStatementResultResponseTypeDef" = dataclasses.field()

    @cached_property
    def ColumnMetadata(self):  # pragma: no cover
        return ColumnMetadata.make_many(self.boto3_raw_data["ColumnMetadata"])

    @cached_property
    def Records(self):  # pragma: no cover
        return Field.make_many(self.boto3_raw_data["Records"])

    TotalNumRows = field("TotalNumRows")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStatementResultResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStatementResultResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStatementResultV2Response:
    boto3_raw_data: "type_defs.GetStatementResultV2ResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ColumnMetadata(self):  # pragma: no cover
        return ColumnMetadata.make_many(self.boto3_raw_data["ColumnMetadata"])

    @cached_property
    def Records(self):  # pragma: no cover
        return QueryRecords.make_many(self.boto3_raw_data["Records"])

    ResultFormat = field("ResultFormat")
    TotalNumRows = field("TotalNumRows")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStatementResultV2ResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStatementResultV2ResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTablesResponse:
    boto3_raw_data: "type_defs.ListTablesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Tables(self):  # pragma: no cover
        return TableMember.make_many(self.boto3_raw_data["Tables"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTablesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTablesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStatementsResponse:
    boto3_raw_data: "type_defs.ListStatementsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Statements(self):  # pragma: no cover
        return StatementData.make_many(self.boto3_raw_data["Statements"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStatementsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStatementsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
