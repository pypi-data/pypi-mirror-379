# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_athena import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AclConfiguration:
    boto3_raw_data: "type_defs.AclConfigurationTypeDef" = dataclasses.field()

    S3AclOption = field("S3AclOption")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AclConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AclConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationDPUSizes:
    boto3_raw_data: "type_defs.ApplicationDPUSizesTypeDef" = dataclasses.field()

    ApplicationRuntimeId = field("ApplicationRuntimeId")
    SupportedDPUSizes = field("SupportedDPUSizes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationDPUSizesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationDPUSizesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AthenaError:
    boto3_raw_data: "type_defs.AthenaErrorTypeDef" = dataclasses.field()

    ErrorCategory = field("ErrorCategory")
    ErrorType = field("ErrorType")
    Retryable = field("Retryable")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AthenaErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AthenaErrorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetNamedQueryInput:
    boto3_raw_data: "type_defs.BatchGetNamedQueryInputTypeDef" = dataclasses.field()

    NamedQueryIds = field("NamedQueryIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetNamedQueryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetNamedQueryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NamedQuery:
    boto3_raw_data: "type_defs.NamedQueryTypeDef" = dataclasses.field()

    Name = field("Name")
    Database = field("Database")
    QueryString = field("QueryString")
    Description = field("Description")
    NamedQueryId = field("NamedQueryId")
    WorkGroup = field("WorkGroup")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NamedQueryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NamedQueryTypeDef"]]
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
class UnprocessedNamedQueryId:
    boto3_raw_data: "type_defs.UnprocessedNamedQueryIdTypeDef" = dataclasses.field()

    NamedQueryId = field("NamedQueryId")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnprocessedNamedQueryIdTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnprocessedNamedQueryIdTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetPreparedStatementInput:
    boto3_raw_data: "type_defs.BatchGetPreparedStatementInputTypeDef" = (
        dataclasses.field()
    )

    PreparedStatementNames = field("PreparedStatementNames")
    WorkGroup = field("WorkGroup")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetPreparedStatementInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetPreparedStatementInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PreparedStatement:
    boto3_raw_data: "type_defs.PreparedStatementTypeDef" = dataclasses.field()

    StatementName = field("StatementName")
    QueryStatement = field("QueryStatement")
    WorkGroupName = field("WorkGroupName")
    Description = field("Description")
    LastModifiedTime = field("LastModifiedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PreparedStatementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PreparedStatementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnprocessedPreparedStatementName:
    boto3_raw_data: "type_defs.UnprocessedPreparedStatementNameTypeDef" = (
        dataclasses.field()
    )

    StatementName = field("StatementName")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UnprocessedPreparedStatementNameTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnprocessedPreparedStatementNameTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetQueryExecutionInput:
    boto3_raw_data: "type_defs.BatchGetQueryExecutionInputTypeDef" = dataclasses.field()

    QueryExecutionIds = field("QueryExecutionIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetQueryExecutionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetQueryExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnprocessedQueryExecutionId:
    boto3_raw_data: "type_defs.UnprocessedQueryExecutionIdTypeDef" = dataclasses.field()

    QueryExecutionId = field("QueryExecutionId")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnprocessedQueryExecutionIdTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnprocessedQueryExecutionIdTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalculationConfiguration:
    boto3_raw_data: "type_defs.CalculationConfigurationTypeDef" = dataclasses.field()

    CodeBlock = field("CodeBlock")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CalculationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalculationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalculationResult:
    boto3_raw_data: "type_defs.CalculationResultTypeDef" = dataclasses.field()

    StdOutS3Uri = field("StdOutS3Uri")
    StdErrorS3Uri = field("StdErrorS3Uri")
    ResultS3Uri = field("ResultS3Uri")
    ResultType = field("ResultType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CalculationResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalculationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalculationStatistics:
    boto3_raw_data: "type_defs.CalculationStatisticsTypeDef" = dataclasses.field()

    DpuExecutionInMillis = field("DpuExecutionInMillis")
    Progress = field("Progress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CalculationStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalculationStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalculationStatus:
    boto3_raw_data: "type_defs.CalculationStatusTypeDef" = dataclasses.field()

    SubmissionDateTime = field("SubmissionDateTime")
    CompletionDateTime = field("CompletionDateTime")
    State = field("State")
    StateChangeReason = field("StateChangeReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CalculationStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalculationStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelCapacityReservationInput:
    boto3_raw_data: "type_defs.CancelCapacityReservationInputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelCapacityReservationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelCapacityReservationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityAllocation:
    boto3_raw_data: "type_defs.CapacityAllocationTypeDef" = dataclasses.field()

    Status = field("Status")
    RequestTime = field("RequestTime")
    StatusMessage = field("StatusMessage")
    RequestCompletionTime = field("RequestCompletionTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CapacityAllocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityAllocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityAssignmentOutput:
    boto3_raw_data: "type_defs.CapacityAssignmentOutputTypeDef" = dataclasses.field()

    WorkGroupNames = field("WorkGroupNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CapacityAssignmentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityAssignmentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityAssignment:
    boto3_raw_data: "type_defs.CapacityAssignmentTypeDef" = dataclasses.field()

    WorkGroupNames = field("WorkGroupNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CapacityAssignmentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityAssignmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColumnInfo:
    boto3_raw_data: "type_defs.ColumnInfoTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")
    CatalogName = field("CatalogName")
    SchemaName = field("SchemaName")
    TableName = field("TableName")
    Label = field("Label")
    Precision = field("Precision")
    Scale = field("Scale")
    Nullable = field("Nullable")
    CaseSensitive = field("CaseSensitive")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ColumnInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ColumnInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Column:
    boto3_raw_data: "type_defs.ColumnTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")
    Comment = field("Comment")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ColumnTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ColumnTypeDef"]]
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
class DataCatalog:
    boto3_raw_data: "type_defs.DataCatalogTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")
    Description = field("Description")
    Parameters = field("Parameters")
    Status = field("Status")
    ConnectionType = field("ConnectionType")
    Error = field("Error")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataCatalogTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataCatalogTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNamedQueryInput:
    boto3_raw_data: "type_defs.CreateNamedQueryInputTypeDef" = dataclasses.field()

    Name = field("Name")
    Database = field("Database")
    QueryString = field("QueryString")
    Description = field("Description")
    ClientRequestToken = field("ClientRequestToken")
    WorkGroup = field("WorkGroup")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateNamedQueryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNamedQueryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNotebookInput:
    boto3_raw_data: "type_defs.CreateNotebookInputTypeDef" = dataclasses.field()

    WorkGroup = field("WorkGroup")
    Name = field("Name")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateNotebookInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNotebookInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePreparedStatementInput:
    boto3_raw_data: "type_defs.CreatePreparedStatementInputTypeDef" = (
        dataclasses.field()
    )

    StatementName = field("StatementName")
    WorkGroup = field("WorkGroup")
    QueryStatement = field("QueryStatement")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePreparedStatementInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePreparedStatementInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePresignedNotebookUrlRequest:
    boto3_raw_data: "type_defs.CreatePresignedNotebookUrlRequestTypeDef" = (
        dataclasses.field()
    )

    SessionId = field("SessionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePresignedNotebookUrlRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePresignedNotebookUrlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerContentEncryptionConfiguration:
    boto3_raw_data: "type_defs.CustomerContentEncryptionConfigurationTypeDef" = (
        dataclasses.field()
    )

    KmsKey = field("KmsKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomerContentEncryptionConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerContentEncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataCatalogSummary:
    boto3_raw_data: "type_defs.DataCatalogSummaryTypeDef" = dataclasses.field()

    CatalogName = field("CatalogName")
    Type = field("Type")
    Status = field("Status")
    ConnectionType = field("ConnectionType")
    Error = field("Error")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataCatalogSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataCatalogSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Database:
    boto3_raw_data: "type_defs.DatabaseTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    Parameters = field("Parameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatabaseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatabaseTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Datum:
    boto3_raw_data: "type_defs.DatumTypeDef" = dataclasses.field()

    VarCharValue = field("VarCharValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatumTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatumTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCapacityReservationInput:
    boto3_raw_data: "type_defs.DeleteCapacityReservationInputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteCapacityReservationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCapacityReservationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataCatalogInput:
    boto3_raw_data: "type_defs.DeleteDataCatalogInputTypeDef" = dataclasses.field()

    Name = field("Name")
    DeleteCatalogOnly = field("DeleteCatalogOnly")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataCatalogInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataCatalogInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteNamedQueryInput:
    boto3_raw_data: "type_defs.DeleteNamedQueryInputTypeDef" = dataclasses.field()

    NamedQueryId = field("NamedQueryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteNamedQueryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteNamedQueryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteNotebookInput:
    boto3_raw_data: "type_defs.DeleteNotebookInputTypeDef" = dataclasses.field()

    NotebookId = field("NotebookId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteNotebookInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteNotebookInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePreparedStatementInput:
    boto3_raw_data: "type_defs.DeletePreparedStatementInputTypeDef" = (
        dataclasses.field()
    )

    StatementName = field("StatementName")
    WorkGroup = field("WorkGroup")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePreparedStatementInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePreparedStatementInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkGroupInput:
    boto3_raw_data: "type_defs.DeleteWorkGroupInputTypeDef" = dataclasses.field()

    WorkGroup = field("WorkGroup")
    RecursiveDeleteOption = field("RecursiveDeleteOption")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorkGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionConfiguration:
    boto3_raw_data: "type_defs.EncryptionConfigurationTypeDef" = dataclasses.field()

    EncryptionOption = field("EncryptionOption")
    KmsKey = field("KmsKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncryptionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngineConfigurationOutput:
    boto3_raw_data: "type_defs.EngineConfigurationOutputTypeDef" = dataclasses.field()

    MaxConcurrentDpus = field("MaxConcurrentDpus")
    CoordinatorDpuSize = field("CoordinatorDpuSize")
    DefaultExecutorDpuSize = field("DefaultExecutorDpuSize")
    AdditionalConfigs = field("AdditionalConfigs")
    SparkProperties = field("SparkProperties")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EngineConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EngineConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngineConfiguration:
    boto3_raw_data: "type_defs.EngineConfigurationTypeDef" = dataclasses.field()

    MaxConcurrentDpus = field("MaxConcurrentDpus")
    CoordinatorDpuSize = field("CoordinatorDpuSize")
    DefaultExecutorDpuSize = field("DefaultExecutorDpuSize")
    AdditionalConfigs = field("AdditionalConfigs")
    SparkProperties = field("SparkProperties")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EngineConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EngineConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngineVersion:
    boto3_raw_data: "type_defs.EngineVersionTypeDef" = dataclasses.field()

    SelectedEngineVersion = field("SelectedEngineVersion")
    EffectiveEngineVersion = field("EffectiveEngineVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EngineVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EngineVersionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutorsSummary:
    boto3_raw_data: "type_defs.ExecutorsSummaryTypeDef" = dataclasses.field()

    ExecutorId = field("ExecutorId")
    ExecutorType = field("ExecutorType")
    StartDateTime = field("StartDateTime")
    TerminationDateTime = field("TerminationDateTime")
    ExecutorState = field("ExecutorState")
    ExecutorSize = field("ExecutorSize")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExecutorsSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutorsSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportNotebookInput:
    boto3_raw_data: "type_defs.ExportNotebookInputTypeDef" = dataclasses.field()

    NotebookId = field("NotebookId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportNotebookInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportNotebookInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotebookMetadata:
    boto3_raw_data: "type_defs.NotebookMetadataTypeDef" = dataclasses.field()

    NotebookId = field("NotebookId")
    Name = field("Name")
    WorkGroup = field("WorkGroup")
    CreationTime = field("CreationTime")
    Type = field("Type")
    LastModifiedTime = field("LastModifiedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NotebookMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotebookMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterDefinition:
    boto3_raw_data: "type_defs.FilterDefinitionTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCalculationExecutionCodeRequest:
    boto3_raw_data: "type_defs.GetCalculationExecutionCodeRequestTypeDef" = (
        dataclasses.field()
    )

    CalculationExecutionId = field("CalculationExecutionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCalculationExecutionCodeRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCalculationExecutionCodeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCalculationExecutionRequest:
    boto3_raw_data: "type_defs.GetCalculationExecutionRequestTypeDef" = (
        dataclasses.field()
    )

    CalculationExecutionId = field("CalculationExecutionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCalculationExecutionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCalculationExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCalculationExecutionStatusRequest:
    boto3_raw_data: "type_defs.GetCalculationExecutionStatusRequestTypeDef" = (
        dataclasses.field()
    )

    CalculationExecutionId = field("CalculationExecutionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCalculationExecutionStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCalculationExecutionStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCapacityAssignmentConfigurationInput:
    boto3_raw_data: "type_defs.GetCapacityAssignmentConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    CapacityReservationName = field("CapacityReservationName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCapacityAssignmentConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCapacityAssignmentConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCapacityReservationInput:
    boto3_raw_data: "type_defs.GetCapacityReservationInputTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCapacityReservationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCapacityReservationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataCatalogInput:
    boto3_raw_data: "type_defs.GetDataCatalogInputTypeDef" = dataclasses.field()

    Name = field("Name")
    WorkGroup = field("WorkGroup")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataCatalogInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataCatalogInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDatabaseInput:
    boto3_raw_data: "type_defs.GetDatabaseInputTypeDef" = dataclasses.field()

    CatalogName = field("CatalogName")
    DatabaseName = field("DatabaseName")
    WorkGroup = field("WorkGroup")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDatabaseInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDatabaseInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNamedQueryInput:
    boto3_raw_data: "type_defs.GetNamedQueryInputTypeDef" = dataclasses.field()

    NamedQueryId = field("NamedQueryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetNamedQueryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNamedQueryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNotebookMetadataInput:
    boto3_raw_data: "type_defs.GetNotebookMetadataInputTypeDef" = dataclasses.field()

    NotebookId = field("NotebookId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetNotebookMetadataInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNotebookMetadataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPreparedStatementInput:
    boto3_raw_data: "type_defs.GetPreparedStatementInputTypeDef" = dataclasses.field()

    StatementName = field("StatementName")
    WorkGroup = field("WorkGroup")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPreparedStatementInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPreparedStatementInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryExecutionInput:
    boto3_raw_data: "type_defs.GetQueryExecutionInputTypeDef" = dataclasses.field()

    QueryExecutionId = field("QueryExecutionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueryExecutionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryExecutionInputTypeDef"]
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
class GetQueryResultsInput:
    boto3_raw_data: "type_defs.GetQueryResultsInputTypeDef" = dataclasses.field()

    QueryExecutionId = field("QueryExecutionId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    QueryResultType = field("QueryResultType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueryResultsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryResultsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryRuntimeStatisticsInput:
    boto3_raw_data: "type_defs.GetQueryRuntimeStatisticsInputTypeDef" = (
        dataclasses.field()
    )

    QueryExecutionId = field("QueryExecutionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetQueryRuntimeStatisticsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryRuntimeStatisticsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionRequest:
    boto3_raw_data: "type_defs.GetSessionRequestTypeDef" = dataclasses.field()

    SessionId = field("SessionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSessionRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionStatistics:
    boto3_raw_data: "type_defs.SessionStatisticsTypeDef" = dataclasses.field()

    DpuExecutionInMillis = field("DpuExecutionInMillis")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionStatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionStatus:
    boto3_raw_data: "type_defs.SessionStatusTypeDef" = dataclasses.field()

    StartDateTime = field("StartDateTime")
    LastModifiedDateTime = field("LastModifiedDateTime")
    EndDateTime = field("EndDateTime")
    IdleSinceDateTime = field("IdleSinceDateTime")
    State = field("State")
    StateChangeReason = field("StateChangeReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SessionStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionStatusRequest:
    boto3_raw_data: "type_defs.GetSessionStatusRequestTypeDef" = dataclasses.field()

    SessionId = field("SessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSessionStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableMetadataInput:
    boto3_raw_data: "type_defs.GetTableMetadataInputTypeDef" = dataclasses.field()

    CatalogName = field("CatalogName")
    DatabaseName = field("DatabaseName")
    TableName = field("TableName")
    WorkGroup = field("WorkGroup")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTableMetadataInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableMetadataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkGroupInput:
    boto3_raw_data: "type_defs.GetWorkGroupInputTypeDef" = dataclasses.field()

    WorkGroup = field("WorkGroup")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetWorkGroupInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityCenterConfiguration:
    boto3_raw_data: "type_defs.IdentityCenterConfigurationTypeDef" = dataclasses.field()

    EnableIdentityCenter = field("EnableIdentityCenter")
    IdentityCenterInstanceArn = field("IdentityCenterInstanceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentityCenterConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityCenterConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportNotebookInput:
    boto3_raw_data: "type_defs.ImportNotebookInputTypeDef" = dataclasses.field()

    WorkGroup = field("WorkGroup")
    Name = field("Name")
    Type = field("Type")
    Payload = field("Payload")
    NotebookS3LocationUri = field("NotebookS3LocationUri")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportNotebookInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportNotebookInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationDPUSizesInput:
    boto3_raw_data: "type_defs.ListApplicationDPUSizesInputTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApplicationDPUSizesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationDPUSizesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCalculationExecutionsRequest:
    boto3_raw_data: "type_defs.ListCalculationExecutionsRequestTypeDef" = (
        dataclasses.field()
    )

    SessionId = field("SessionId")
    StateFilter = field("StateFilter")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCalculationExecutionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCalculationExecutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCapacityReservationsInput:
    boto3_raw_data: "type_defs.ListCapacityReservationsInputTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCapacityReservationsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCapacityReservationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataCatalogsInput:
    boto3_raw_data: "type_defs.ListDataCatalogsInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    WorkGroup = field("WorkGroup")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataCatalogsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataCatalogsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatabasesInput:
    boto3_raw_data: "type_defs.ListDatabasesInputTypeDef" = dataclasses.field()

    CatalogName = field("CatalogName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    WorkGroup = field("WorkGroup")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatabasesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatabasesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngineVersionsInput:
    boto3_raw_data: "type_defs.ListEngineVersionsInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEngineVersionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEngineVersionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExecutorsRequest:
    boto3_raw_data: "type_defs.ListExecutorsRequestTypeDef" = dataclasses.field()

    SessionId = field("SessionId")
    ExecutorStateFilter = field("ExecutorStateFilter")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExecutorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExecutorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNamedQueriesInput:
    boto3_raw_data: "type_defs.ListNamedQueriesInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    WorkGroup = field("WorkGroup")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNamedQueriesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNamedQueriesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotebookSessionsRequest:
    boto3_raw_data: "type_defs.ListNotebookSessionsRequestTypeDef" = dataclasses.field()

    NotebookId = field("NotebookId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNotebookSessionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotebookSessionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotebookSessionSummary:
    boto3_raw_data: "type_defs.NotebookSessionSummaryTypeDef" = dataclasses.field()

    SessionId = field("SessionId")
    CreationTime = field("CreationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotebookSessionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotebookSessionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPreparedStatementsInput:
    boto3_raw_data: "type_defs.ListPreparedStatementsInputTypeDef" = dataclasses.field()

    WorkGroup = field("WorkGroup")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPreparedStatementsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPreparedStatementsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PreparedStatementSummary:
    boto3_raw_data: "type_defs.PreparedStatementSummaryTypeDef" = dataclasses.field()

    StatementName = field("StatementName")
    LastModifiedTime = field("LastModifiedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PreparedStatementSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PreparedStatementSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueryExecutionsInput:
    boto3_raw_data: "type_defs.ListQueryExecutionsInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    WorkGroup = field("WorkGroup")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQueryExecutionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueryExecutionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionsRequest:
    boto3_raw_data: "type_defs.ListSessionsRequestTypeDef" = dataclasses.field()

    WorkGroup = field("WorkGroup")
    StateFilter = field("StateFilter")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTableMetadataInput:
    boto3_raw_data: "type_defs.ListTableMetadataInputTypeDef" = dataclasses.field()

    CatalogName = field("CatalogName")
    DatabaseName = field("DatabaseName")
    Expression = field("Expression")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    WorkGroup = field("WorkGroup")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTableMetadataInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTableMetadataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInput:
    boto3_raw_data: "type_defs.ListTagsForResourceInputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkGroupsInput:
    boto3_raw_data: "type_defs.ListWorkGroupsInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkGroupsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkGroupsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedQueryResultsEncryptionConfiguration:
    boto3_raw_data: "type_defs.ManagedQueryResultsEncryptionConfigurationTypeDef" = (
        dataclasses.field()
    )

    KmsKey = field("KmsKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ManagedQueryResultsEncryptionConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedQueryResultsEncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryExecutionContext:
    boto3_raw_data: "type_defs.QueryExecutionContextTypeDef" = dataclasses.field()

    Database = field("Database")
    Catalog = field("Catalog")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryExecutionContextTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryExecutionContextTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResultReuseInformation:
    boto3_raw_data: "type_defs.ResultReuseInformationTypeDef" = dataclasses.field()

    ReusedPreviousResult = field("ReusedPreviousResult")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResultReuseInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResultReuseInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryResultsS3AccessGrantsConfiguration:
    boto3_raw_data: "type_defs.QueryResultsS3AccessGrantsConfigurationTypeDef" = (
        dataclasses.field()
    )

    EnableS3AccessGrants = field("EnableS3AccessGrants")
    AuthenticationType = field("AuthenticationType")
    CreateUserLevelPrefix = field("CreateUserLevelPrefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.QueryResultsS3AccessGrantsConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryResultsS3AccessGrantsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryRuntimeStatisticsRows:
    boto3_raw_data: "type_defs.QueryRuntimeStatisticsRowsTypeDef" = dataclasses.field()

    InputRows = field("InputRows")
    InputBytes = field("InputBytes")
    OutputBytes = field("OutputBytes")
    OutputRows = field("OutputRows")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryRuntimeStatisticsRowsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryRuntimeStatisticsRowsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryRuntimeStatisticsTimeline:
    boto3_raw_data: "type_defs.QueryRuntimeStatisticsTimelineTypeDef" = (
        dataclasses.field()
    )

    QueryQueueTimeInMillis = field("QueryQueueTimeInMillis")
    ServicePreProcessingTimeInMillis = field("ServicePreProcessingTimeInMillis")
    QueryPlanningTimeInMillis = field("QueryPlanningTimeInMillis")
    EngineExecutionTimeInMillis = field("EngineExecutionTimeInMillis")
    ServiceProcessingTimeInMillis = field("ServiceProcessingTimeInMillis")
    TotalExecutionTimeInMillis = field("TotalExecutionTimeInMillis")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.QueryRuntimeStatisticsTimelineTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryRuntimeStatisticsTimelineTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryStagePlanNode:
    boto3_raw_data: "type_defs.QueryStagePlanNodeTypeDef" = dataclasses.field()

    Name = field("Name")
    Identifier = field("Identifier")
    Children = field("Children")
    RemoteSources = field("RemoteSources")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryStagePlanNodeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryStagePlanNodeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResultReuseByAgeConfiguration:
    boto3_raw_data: "type_defs.ResultReuseByAgeConfigurationTypeDef" = (
        dataclasses.field()
    )

    Enabled = field("Enabled")
    MaxAgeInMinutes = field("MaxAgeInMinutes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ResultReuseByAgeConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResultReuseByAgeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopCalculationExecutionRequest:
    boto3_raw_data: "type_defs.StopCalculationExecutionRequestTypeDef" = (
        dataclasses.field()
    )

    CalculationExecutionId = field("CalculationExecutionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopCalculationExecutionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopCalculationExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopQueryExecutionInput:
    boto3_raw_data: "type_defs.StopQueryExecutionInputTypeDef" = dataclasses.field()

    QueryExecutionId = field("QueryExecutionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopQueryExecutionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopQueryExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateSessionRequest:
    boto3_raw_data: "type_defs.TerminateSessionRequestTypeDef" = dataclasses.field()

    SessionId = field("SessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TerminateSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceInput:
    boto3_raw_data: "type_defs.UntagResourceInputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCapacityReservationInput:
    boto3_raw_data: "type_defs.UpdateCapacityReservationInputTypeDef" = (
        dataclasses.field()
    )

    TargetDpus = field("TargetDpus")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateCapacityReservationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCapacityReservationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataCatalogInput:
    boto3_raw_data: "type_defs.UpdateDataCatalogInputTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")
    Description = field("Description")
    Parameters = field("Parameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDataCatalogInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataCatalogInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNamedQueryInput:
    boto3_raw_data: "type_defs.UpdateNamedQueryInputTypeDef" = dataclasses.field()

    NamedQueryId = field("NamedQueryId")
    Name = field("Name")
    QueryString = field("QueryString")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateNamedQueryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNamedQueryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNotebookInput:
    boto3_raw_data: "type_defs.UpdateNotebookInputTypeDef" = dataclasses.field()

    NotebookId = field("NotebookId")
    Payload = field("Payload")
    Type = field("Type")
    SessionId = field("SessionId")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateNotebookInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNotebookInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNotebookMetadataInput:
    boto3_raw_data: "type_defs.UpdateNotebookMetadataInputTypeDef" = dataclasses.field()

    NotebookId = field("NotebookId")
    Name = field("Name")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateNotebookMetadataInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNotebookMetadataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePreparedStatementInput:
    boto3_raw_data: "type_defs.UpdatePreparedStatementInputTypeDef" = (
        dataclasses.field()
    )

    StatementName = field("StatementName")
    WorkGroup = field("WorkGroup")
    QueryStatement = field("QueryStatement")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePreparedStatementInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePreparedStatementInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryExecutionStatus:
    boto3_raw_data: "type_defs.QueryExecutionStatusTypeDef" = dataclasses.field()

    State = field("State")
    StateChangeReason = field("StateChangeReason")
    SubmissionDateTime = field("SubmissionDateTime")
    CompletionDateTime = field("CompletionDateTime")

    @cached_property
    def AthenaError(self):  # pragma: no cover
        return AthenaError.make_one(self.boto3_raw_data["AthenaError"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryExecutionStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryExecutionStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNamedQueryOutput:
    boto3_raw_data: "type_defs.CreateNamedQueryOutputTypeDef" = dataclasses.field()

    NamedQueryId = field("NamedQueryId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateNamedQueryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNamedQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNotebookOutput:
    boto3_raw_data: "type_defs.CreateNotebookOutputTypeDef" = dataclasses.field()

    NotebookId = field("NotebookId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateNotebookOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNotebookOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePresignedNotebookUrlResponse:
    boto3_raw_data: "type_defs.CreatePresignedNotebookUrlResponseTypeDef" = (
        dataclasses.field()
    )

    NotebookUrl = field("NotebookUrl")
    AuthToken = field("AuthToken")
    AuthTokenExpirationTime = field("AuthTokenExpirationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePresignedNotebookUrlResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePresignedNotebookUrlResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCalculationExecutionCodeResponse:
    boto3_raw_data: "type_defs.GetCalculationExecutionCodeResponseTypeDef" = (
        dataclasses.field()
    )

    CodeBlock = field("CodeBlock")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCalculationExecutionCodeResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCalculationExecutionCodeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNamedQueryOutput:
    boto3_raw_data: "type_defs.GetNamedQueryOutputTypeDef" = dataclasses.field()

    @cached_property
    def NamedQuery(self):  # pragma: no cover
        return NamedQuery.make_one(self.boto3_raw_data["NamedQuery"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetNamedQueryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNamedQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportNotebookOutput:
    boto3_raw_data: "type_defs.ImportNotebookOutputTypeDef" = dataclasses.field()

    NotebookId = field("NotebookId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportNotebookOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportNotebookOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationDPUSizesOutput:
    boto3_raw_data: "type_defs.ListApplicationDPUSizesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ApplicationDPUSizes(self):  # pragma: no cover
        return ApplicationDPUSizes.make_many(self.boto3_raw_data["ApplicationDPUSizes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationDPUSizesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationDPUSizesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNamedQueriesOutput:
    boto3_raw_data: "type_defs.ListNamedQueriesOutputTypeDef" = dataclasses.field()

    NamedQueryIds = field("NamedQueryIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNamedQueriesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNamedQueriesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueryExecutionsOutput:
    boto3_raw_data: "type_defs.ListQueryExecutionsOutputTypeDef" = dataclasses.field()

    QueryExecutionIds = field("QueryExecutionIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQueryExecutionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueryExecutionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCalculationExecutionResponse:
    boto3_raw_data: "type_defs.StartCalculationExecutionResponseTypeDef" = (
        dataclasses.field()
    )

    CalculationExecutionId = field("CalculationExecutionId")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartCalculationExecutionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCalculationExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartQueryExecutionOutput:
    boto3_raw_data: "type_defs.StartQueryExecutionOutputTypeDef" = dataclasses.field()

    QueryExecutionId = field("QueryExecutionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartQueryExecutionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartQueryExecutionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSessionResponse:
    boto3_raw_data: "type_defs.StartSessionResponseTypeDef" = dataclasses.field()

    SessionId = field("SessionId")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopCalculationExecutionResponse:
    boto3_raw_data: "type_defs.StopCalculationExecutionResponseTypeDef" = (
        dataclasses.field()
    )

    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopCalculationExecutionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopCalculationExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateSessionResponse:
    boto3_raw_data: "type_defs.TerminateSessionResponseTypeDef" = dataclasses.field()

    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TerminateSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetNamedQueryOutput:
    boto3_raw_data: "type_defs.BatchGetNamedQueryOutputTypeDef" = dataclasses.field()

    @cached_property
    def NamedQueries(self):  # pragma: no cover
        return NamedQuery.make_many(self.boto3_raw_data["NamedQueries"])

    @cached_property
    def UnprocessedNamedQueryIds(self):  # pragma: no cover
        return UnprocessedNamedQueryId.make_many(
            self.boto3_raw_data["UnprocessedNamedQueryIds"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetNamedQueryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetNamedQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPreparedStatementOutput:
    boto3_raw_data: "type_defs.GetPreparedStatementOutputTypeDef" = dataclasses.field()

    @cached_property
    def PreparedStatement(self):  # pragma: no cover
        return PreparedStatement.make_one(self.boto3_raw_data["PreparedStatement"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPreparedStatementOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPreparedStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetPreparedStatementOutput:
    boto3_raw_data: "type_defs.BatchGetPreparedStatementOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PreparedStatements(self):  # pragma: no cover
        return PreparedStatement.make_many(self.boto3_raw_data["PreparedStatements"])

    @cached_property
    def UnprocessedPreparedStatementNames(self):  # pragma: no cover
        return UnprocessedPreparedStatementName.make_many(
            self.boto3_raw_data["UnprocessedPreparedStatementNames"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetPreparedStatementOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetPreparedStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCalculationExecutionRequest:
    boto3_raw_data: "type_defs.StartCalculationExecutionRequestTypeDef" = (
        dataclasses.field()
    )

    SessionId = field("SessionId")
    Description = field("Description")

    @cached_property
    def CalculationConfiguration(self):  # pragma: no cover
        return CalculationConfiguration.make_one(
            self.boto3_raw_data["CalculationConfiguration"]
        )

    CodeBlock = field("CodeBlock")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartCalculationExecutionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCalculationExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalculationSummary:
    boto3_raw_data: "type_defs.CalculationSummaryTypeDef" = dataclasses.field()

    CalculationExecutionId = field("CalculationExecutionId")
    Description = field("Description")

    @cached_property
    def Status(self):  # pragma: no cover
        return CalculationStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CalculationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalculationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCalculationExecutionResponse:
    boto3_raw_data: "type_defs.GetCalculationExecutionResponseTypeDef" = (
        dataclasses.field()
    )

    CalculationExecutionId = field("CalculationExecutionId")
    SessionId = field("SessionId")
    Description = field("Description")
    WorkingDirectory = field("WorkingDirectory")

    @cached_property
    def Status(self):  # pragma: no cover
        return CalculationStatus.make_one(self.boto3_raw_data["Status"])

    @cached_property
    def Statistics(self):  # pragma: no cover
        return CalculationStatistics.make_one(self.boto3_raw_data["Statistics"])

    @cached_property
    def Result(self):  # pragma: no cover
        return CalculationResult.make_one(self.boto3_raw_data["Result"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCalculationExecutionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCalculationExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCalculationExecutionStatusResponse:
    boto3_raw_data: "type_defs.GetCalculationExecutionStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Status(self):  # pragma: no cover
        return CalculationStatus.make_one(self.boto3_raw_data["Status"])

    @cached_property
    def Statistics(self):  # pragma: no cover
        return CalculationStatistics.make_one(self.boto3_raw_data["Statistics"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCalculationExecutionStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCalculationExecutionStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityReservation:
    boto3_raw_data: "type_defs.CapacityReservationTypeDef" = dataclasses.field()

    Name = field("Name")
    Status = field("Status")
    TargetDpus = field("TargetDpus")
    AllocatedDpus = field("AllocatedDpus")
    CreationTime = field("CreationTime")

    @cached_property
    def LastAllocation(self):  # pragma: no cover
        return CapacityAllocation.make_one(self.boto3_raw_data["LastAllocation"])

    LastSuccessfulAllocationTime = field("LastSuccessfulAllocationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CapacityReservationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityReservationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityAssignmentConfiguration:
    boto3_raw_data: "type_defs.CapacityAssignmentConfigurationTypeDef" = (
        dataclasses.field()
    )

    CapacityReservationName = field("CapacityReservationName")

    @cached_property
    def CapacityAssignments(self):  # pragma: no cover
        return CapacityAssignmentOutput.make_many(
            self.boto3_raw_data["CapacityAssignments"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CapacityAssignmentConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityAssignmentConfigurationTypeDef"]
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

    @cached_property
    def ColumnInfo(self):  # pragma: no cover
        return ColumnInfo.make_many(self.boto3_raw_data["ColumnInfo"])

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
class TableMetadata:
    boto3_raw_data: "type_defs.TableMetadataTypeDef" = dataclasses.field()

    Name = field("Name")
    CreateTime = field("CreateTime")
    LastAccessTime = field("LastAccessTime")
    TableType = field("TableType")

    @cached_property
    def Columns(self):  # pragma: no cover
        return Column.make_many(self.boto3_raw_data["Columns"])

    @cached_property
    def PartitionKeys(self):  # pragma: no cover
        return Column.make_many(self.boto3_raw_data["PartitionKeys"])

    Parameters = field("Parameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TableMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TableMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCapacityReservationInput:
    boto3_raw_data: "type_defs.CreateCapacityReservationInputTypeDef" = (
        dataclasses.field()
    )

    TargetDpus = field("TargetDpus")
    Name = field("Name")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateCapacityReservationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCapacityReservationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataCatalogInput:
    boto3_raw_data: "type_defs.CreateDataCatalogInputTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")
    Description = field("Description")
    Parameters = field("Parameters")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataCatalogInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataCatalogInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceOutput:
    boto3_raw_data: "type_defs.ListTagsForResourceOutputTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceInput:
    boto3_raw_data: "type_defs.TagResourceInputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagResourceInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataCatalogOutput:
    boto3_raw_data: "type_defs.CreateDataCatalogOutputTypeDef" = dataclasses.field()

    @cached_property
    def DataCatalog(self):  # pragma: no cover
        return DataCatalog.make_one(self.boto3_raw_data["DataCatalog"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataCatalogOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataCatalogOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataCatalogOutput:
    boto3_raw_data: "type_defs.DeleteDataCatalogOutputTypeDef" = dataclasses.field()

    @cached_property
    def DataCatalog(self):  # pragma: no cover
        return DataCatalog.make_one(self.boto3_raw_data["DataCatalog"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataCatalogOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataCatalogOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataCatalogOutput:
    boto3_raw_data: "type_defs.GetDataCatalogOutputTypeDef" = dataclasses.field()

    @cached_property
    def DataCatalog(self):  # pragma: no cover
        return DataCatalog.make_one(self.boto3_raw_data["DataCatalog"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataCatalogOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataCatalogOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataCatalogsOutput:
    boto3_raw_data: "type_defs.ListDataCatalogsOutputTypeDef" = dataclasses.field()

    @cached_property
    def DataCatalogsSummary(self):  # pragma: no cover
        return DataCatalogSummary.make_many(self.boto3_raw_data["DataCatalogsSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataCatalogsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataCatalogsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDatabaseOutput:
    boto3_raw_data: "type_defs.GetDatabaseOutputTypeDef" = dataclasses.field()

    @cached_property
    def Database(self):  # pragma: no cover
        return Database.make_one(self.boto3_raw_data["Database"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDatabaseOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDatabaseOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatabasesOutput:
    boto3_raw_data: "type_defs.ListDatabasesOutputTypeDef" = dataclasses.field()

    @cached_property
    def DatabaseList(self):  # pragma: no cover
        return Database.make_many(self.boto3_raw_data["DatabaseList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatabasesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatabasesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Row:
    boto3_raw_data: "type_defs.RowTypeDef" = dataclasses.field()

    @cached_property
    def Data(self):  # pragma: no cover
        return Datum.make_many(self.boto3_raw_data["Data"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RowTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResultConfiguration:
    boto3_raw_data: "type_defs.ResultConfigurationTypeDef" = dataclasses.field()

    OutputLocation = field("OutputLocation")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @cached_property
    def AclConfiguration(self):  # pragma: no cover
        return AclConfiguration.make_one(self.boto3_raw_data["AclConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResultConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResultConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResultConfigurationUpdates:
    boto3_raw_data: "type_defs.ResultConfigurationUpdatesTypeDef" = dataclasses.field()

    OutputLocation = field("OutputLocation")
    RemoveOutputLocation = field("RemoveOutputLocation")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    RemoveEncryptionConfiguration = field("RemoveEncryptionConfiguration")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    RemoveExpectedBucketOwner = field("RemoveExpectedBucketOwner")

    @cached_property
    def AclConfiguration(self):  # pragma: no cover
        return AclConfiguration.make_one(self.boto3_raw_data["AclConfiguration"])

    RemoveAclConfiguration = field("RemoveAclConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResultConfigurationUpdatesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResultConfigurationUpdatesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionConfiguration:
    boto3_raw_data: "type_defs.SessionConfigurationTypeDef" = dataclasses.field()

    ExecutionRole = field("ExecutionRole")
    WorkingDirectory = field("WorkingDirectory")
    IdleTimeoutSeconds = field("IdleTimeoutSeconds")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SessionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngineVersionsOutput:
    boto3_raw_data: "type_defs.ListEngineVersionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def EngineVersions(self):  # pragma: no cover
        return EngineVersion.make_many(self.boto3_raw_data["EngineVersions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEngineVersionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEngineVersionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkGroupSummary:
    boto3_raw_data: "type_defs.WorkGroupSummaryTypeDef" = dataclasses.field()

    Name = field("Name")
    State = field("State")
    Description = field("Description")
    CreationTime = field("CreationTime")

    @cached_property
    def EngineVersion(self):  # pragma: no cover
        return EngineVersion.make_one(self.boto3_raw_data["EngineVersion"])

    IdentityCenterApplicationArn = field("IdentityCenterApplicationArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkGroupSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkGroupSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExecutorsResponse:
    boto3_raw_data: "type_defs.ListExecutorsResponseTypeDef" = dataclasses.field()

    SessionId = field("SessionId")

    @cached_property
    def ExecutorsSummary(self):  # pragma: no cover
        return ExecutorsSummary.make_many(self.boto3_raw_data["ExecutorsSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExecutorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExecutorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportNotebookOutput:
    boto3_raw_data: "type_defs.ExportNotebookOutputTypeDef" = dataclasses.field()

    @cached_property
    def NotebookMetadata(self):  # pragma: no cover
        return NotebookMetadata.make_one(self.boto3_raw_data["NotebookMetadata"])

    Payload = field("Payload")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportNotebookOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportNotebookOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNotebookMetadataOutput:
    boto3_raw_data: "type_defs.GetNotebookMetadataOutputTypeDef" = dataclasses.field()

    @cached_property
    def NotebookMetadata(self):  # pragma: no cover
        return NotebookMetadata.make_one(self.boto3_raw_data["NotebookMetadata"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetNotebookMetadataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNotebookMetadataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotebookMetadataOutput:
    boto3_raw_data: "type_defs.ListNotebookMetadataOutputTypeDef" = dataclasses.field()

    @cached_property
    def NotebookMetadataList(self):  # pragma: no cover
        return NotebookMetadata.make_many(self.boto3_raw_data["NotebookMetadataList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNotebookMetadataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotebookMetadataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotebookMetadataInput:
    boto3_raw_data: "type_defs.ListNotebookMetadataInputTypeDef" = dataclasses.field()

    WorkGroup = field("WorkGroup")

    @cached_property
    def Filters(self):  # pragma: no cover
        return FilterDefinition.make_one(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNotebookMetadataInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotebookMetadataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryResultsInputPaginate:
    boto3_raw_data: "type_defs.GetQueryResultsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    QueryExecutionId = field("QueryExecutionId")
    QueryResultType = field("QueryResultType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueryResultsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryResultsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataCatalogsInputPaginate:
    boto3_raw_data: "type_defs.ListDataCatalogsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    WorkGroup = field("WorkGroup")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataCatalogsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataCatalogsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatabasesInputPaginate:
    boto3_raw_data: "type_defs.ListDatabasesInputPaginateTypeDef" = dataclasses.field()

    CatalogName = field("CatalogName")
    WorkGroup = field("WorkGroup")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatabasesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatabasesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNamedQueriesInputPaginate:
    boto3_raw_data: "type_defs.ListNamedQueriesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    WorkGroup = field("WorkGroup")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListNamedQueriesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNamedQueriesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueryExecutionsInputPaginate:
    boto3_raw_data: "type_defs.ListQueryExecutionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    WorkGroup = field("WorkGroup")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListQueryExecutionsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueryExecutionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTableMetadataInputPaginate:
    boto3_raw_data: "type_defs.ListTableMetadataInputPaginateTypeDef" = (
        dataclasses.field()
    )

    CatalogName = field("CatalogName")
    DatabaseName = field("DatabaseName")
    Expression = field("Expression")
    WorkGroup = field("WorkGroup")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTableMetadataInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTableMetadataInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInputPaginate:
    boto3_raw_data: "type_defs.ListTagsForResourceInputPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceARN = field("ResourceARN")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTagsForResourceInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionStatusResponse:
    boto3_raw_data: "type_defs.GetSessionStatusResponseTypeDef" = dataclasses.field()

    SessionId = field("SessionId")

    @cached_property
    def Status(self):  # pragma: no cover
        return SessionStatus.make_one(self.boto3_raw_data["Status"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSessionStatusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionSummary:
    boto3_raw_data: "type_defs.SessionSummaryTypeDef" = dataclasses.field()

    SessionId = field("SessionId")
    Description = field("Description")

    @cached_property
    def EngineVersion(self):  # pragma: no cover
        return EngineVersion.make_one(self.boto3_raw_data["EngineVersion"])

    NotebookVersion = field("NotebookVersion")

    @cached_property
    def Status(self):  # pragma: no cover
        return SessionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SessionSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotebookSessionsResponse:
    boto3_raw_data: "type_defs.ListNotebookSessionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def NotebookSessionsList(self):  # pragma: no cover
        return NotebookSessionSummary.make_many(
            self.boto3_raw_data["NotebookSessionsList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNotebookSessionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotebookSessionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPreparedStatementsOutput:
    boto3_raw_data: "type_defs.ListPreparedStatementsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PreparedStatements(self):  # pragma: no cover
        return PreparedStatementSummary.make_many(
            self.boto3_raw_data["PreparedStatements"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPreparedStatementsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPreparedStatementsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedQueryResultsConfiguration:
    boto3_raw_data: "type_defs.ManagedQueryResultsConfigurationTypeDef" = (
        dataclasses.field()
    )

    Enabled = field("Enabled")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return ManagedQueryResultsEncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ManagedQueryResultsConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedQueryResultsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedQueryResultsConfigurationUpdates:
    boto3_raw_data: "type_defs.ManagedQueryResultsConfigurationUpdatesTypeDef" = (
        dataclasses.field()
    )

    Enabled = field("Enabled")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return ManagedQueryResultsEncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    RemoveEncryptionConfiguration = field("RemoveEncryptionConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ManagedQueryResultsConfigurationUpdatesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedQueryResultsConfigurationUpdatesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryExecutionStatistics:
    boto3_raw_data: "type_defs.QueryExecutionStatisticsTypeDef" = dataclasses.field()

    EngineExecutionTimeInMillis = field("EngineExecutionTimeInMillis")
    DataScannedInBytes = field("DataScannedInBytes")
    DataManifestLocation = field("DataManifestLocation")
    TotalExecutionTimeInMillis = field("TotalExecutionTimeInMillis")
    QueryQueueTimeInMillis = field("QueryQueueTimeInMillis")
    ServicePreProcessingTimeInMillis = field("ServicePreProcessingTimeInMillis")
    QueryPlanningTimeInMillis = field("QueryPlanningTimeInMillis")
    ServiceProcessingTimeInMillis = field("ServiceProcessingTimeInMillis")

    @cached_property
    def ResultReuseInformation(self):  # pragma: no cover
        return ResultReuseInformation.make_one(
            self.boto3_raw_data["ResultReuseInformation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryExecutionStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryExecutionStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryStage:
    boto3_raw_data: "type_defs.QueryStageTypeDef" = dataclasses.field()

    StageId = field("StageId")
    State = field("State")
    OutputBytes = field("OutputBytes")
    OutputRows = field("OutputRows")
    InputBytes = field("InputBytes")
    InputRows = field("InputRows")
    ExecutionTime = field("ExecutionTime")

    @cached_property
    def QueryStagePlan(self):  # pragma: no cover
        return QueryStagePlanNode.make_one(self.boto3_raw_data["QueryStagePlan"])

    SubStages = field("SubStages")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryStageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryStageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResultReuseConfiguration:
    boto3_raw_data: "type_defs.ResultReuseConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def ResultReuseByAgeConfiguration(self):  # pragma: no cover
        return ResultReuseByAgeConfiguration.make_one(
            self.boto3_raw_data["ResultReuseByAgeConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResultReuseConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResultReuseConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCalculationExecutionsResponse:
    boto3_raw_data: "type_defs.ListCalculationExecutionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Calculations(self):  # pragma: no cover
        return CalculationSummary.make_many(self.boto3_raw_data["Calculations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCalculationExecutionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCalculationExecutionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCapacityReservationOutput:
    boto3_raw_data: "type_defs.GetCapacityReservationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CapacityReservation(self):  # pragma: no cover
        return CapacityReservation.make_one(self.boto3_raw_data["CapacityReservation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCapacityReservationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCapacityReservationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCapacityReservationsOutput:
    boto3_raw_data: "type_defs.ListCapacityReservationsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CapacityReservations(self):  # pragma: no cover
        return CapacityReservation.make_many(
            self.boto3_raw_data["CapacityReservations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCapacityReservationsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCapacityReservationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCapacityAssignmentConfigurationOutput:
    boto3_raw_data: "type_defs.GetCapacityAssignmentConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CapacityAssignmentConfiguration(self):  # pragma: no cover
        return CapacityAssignmentConfiguration.make_one(
            self.boto3_raw_data["CapacityAssignmentConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCapacityAssignmentConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCapacityAssignmentConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutCapacityAssignmentConfigurationInput:
    boto3_raw_data: "type_defs.PutCapacityAssignmentConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    CapacityReservationName = field("CapacityReservationName")
    CapacityAssignments = field("CapacityAssignments")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutCapacityAssignmentConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutCapacityAssignmentConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableMetadataOutput:
    boto3_raw_data: "type_defs.GetTableMetadataOutputTypeDef" = dataclasses.field()

    @cached_property
    def TableMetadata(self):  # pragma: no cover
        return TableMetadata.make_one(self.boto3_raw_data["TableMetadata"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTableMetadataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableMetadataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTableMetadataOutput:
    boto3_raw_data: "type_defs.ListTableMetadataOutputTypeDef" = dataclasses.field()

    @cached_property
    def TableMetadataList(self):  # pragma: no cover
        return TableMetadata.make_many(self.boto3_raw_data["TableMetadataList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTableMetadataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTableMetadataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResultSet:
    boto3_raw_data: "type_defs.ResultSetTypeDef" = dataclasses.field()

    @cached_property
    def Rows(self):  # pragma: no cover
        return Row.make_many(self.boto3_raw_data["Rows"])

    @cached_property
    def ResultSetMetadata(self):  # pragma: no cover
        return ResultSetMetadata.make_one(self.boto3_raw_data["ResultSetMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResultSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResultSetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionResponse:
    boto3_raw_data: "type_defs.GetSessionResponseTypeDef" = dataclasses.field()

    SessionId = field("SessionId")
    Description = field("Description")
    WorkGroup = field("WorkGroup")
    EngineVersion = field("EngineVersion")

    @cached_property
    def EngineConfiguration(self):  # pragma: no cover
        return EngineConfigurationOutput.make_one(
            self.boto3_raw_data["EngineConfiguration"]
        )

    NotebookVersion = field("NotebookVersion")

    @cached_property
    def SessionConfiguration(self):  # pragma: no cover
        return SessionConfiguration.make_one(
            self.boto3_raw_data["SessionConfiguration"]
        )

    @cached_property
    def Status(self):  # pragma: no cover
        return SessionStatus.make_one(self.boto3_raw_data["Status"])

    @cached_property
    def Statistics(self):  # pragma: no cover
        return SessionStatistics.make_one(self.boto3_raw_data["Statistics"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSessionRequest:
    boto3_raw_data: "type_defs.StartSessionRequestTypeDef" = dataclasses.field()

    WorkGroup = field("WorkGroup")
    EngineConfiguration = field("EngineConfiguration")
    Description = field("Description")
    NotebookVersion = field("NotebookVersion")
    SessionIdleTimeoutInMinutes = field("SessionIdleTimeoutInMinutes")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkGroupsOutput:
    boto3_raw_data: "type_defs.ListWorkGroupsOutputTypeDef" = dataclasses.field()

    @cached_property
    def WorkGroups(self):  # pragma: no cover
        return WorkGroupSummary.make_many(self.boto3_raw_data["WorkGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkGroupsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkGroupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionsResponse:
    boto3_raw_data: "type_defs.ListSessionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Sessions(self):  # pragma: no cover
        return SessionSummary.make_many(self.boto3_raw_data["Sessions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkGroupConfiguration:
    boto3_raw_data: "type_defs.WorkGroupConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def ResultConfiguration(self):  # pragma: no cover
        return ResultConfiguration.make_one(self.boto3_raw_data["ResultConfiguration"])

    @cached_property
    def ManagedQueryResultsConfiguration(self):  # pragma: no cover
        return ManagedQueryResultsConfiguration.make_one(
            self.boto3_raw_data["ManagedQueryResultsConfiguration"]
        )

    EnforceWorkGroupConfiguration = field("EnforceWorkGroupConfiguration")
    PublishCloudWatchMetricsEnabled = field("PublishCloudWatchMetricsEnabled")
    BytesScannedCutoffPerQuery = field("BytesScannedCutoffPerQuery")
    RequesterPaysEnabled = field("RequesterPaysEnabled")

    @cached_property
    def EngineVersion(self):  # pragma: no cover
        return EngineVersion.make_one(self.boto3_raw_data["EngineVersion"])

    AdditionalConfiguration = field("AdditionalConfiguration")
    ExecutionRole = field("ExecutionRole")

    @cached_property
    def CustomerContentEncryptionConfiguration(self):  # pragma: no cover
        return CustomerContentEncryptionConfiguration.make_one(
            self.boto3_raw_data["CustomerContentEncryptionConfiguration"]
        )

    EnableMinimumEncryptionConfiguration = field("EnableMinimumEncryptionConfiguration")

    @cached_property
    def IdentityCenterConfiguration(self):  # pragma: no cover
        return IdentityCenterConfiguration.make_one(
            self.boto3_raw_data["IdentityCenterConfiguration"]
        )

    @cached_property
    def QueryResultsS3AccessGrantsConfiguration(self):  # pragma: no cover
        return QueryResultsS3AccessGrantsConfiguration.make_one(
            self.boto3_raw_data["QueryResultsS3AccessGrantsConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkGroupConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkGroupConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkGroupConfigurationUpdates:
    boto3_raw_data: "type_defs.WorkGroupConfigurationUpdatesTypeDef" = (
        dataclasses.field()
    )

    EnforceWorkGroupConfiguration = field("EnforceWorkGroupConfiguration")

    @cached_property
    def ResultConfigurationUpdates(self):  # pragma: no cover
        return ResultConfigurationUpdates.make_one(
            self.boto3_raw_data["ResultConfigurationUpdates"]
        )

    @cached_property
    def ManagedQueryResultsConfigurationUpdates(self):  # pragma: no cover
        return ManagedQueryResultsConfigurationUpdates.make_one(
            self.boto3_raw_data["ManagedQueryResultsConfigurationUpdates"]
        )

    PublishCloudWatchMetricsEnabled = field("PublishCloudWatchMetricsEnabled")
    BytesScannedCutoffPerQuery = field("BytesScannedCutoffPerQuery")
    RemoveBytesScannedCutoffPerQuery = field("RemoveBytesScannedCutoffPerQuery")
    RequesterPaysEnabled = field("RequesterPaysEnabled")

    @cached_property
    def EngineVersion(self):  # pragma: no cover
        return EngineVersion.make_one(self.boto3_raw_data["EngineVersion"])

    RemoveCustomerContentEncryptionConfiguration = field(
        "RemoveCustomerContentEncryptionConfiguration"
    )
    AdditionalConfiguration = field("AdditionalConfiguration")
    ExecutionRole = field("ExecutionRole")

    @cached_property
    def CustomerContentEncryptionConfiguration(self):  # pragma: no cover
        return CustomerContentEncryptionConfiguration.make_one(
            self.boto3_raw_data["CustomerContentEncryptionConfiguration"]
        )

    EnableMinimumEncryptionConfiguration = field("EnableMinimumEncryptionConfiguration")

    @cached_property
    def QueryResultsS3AccessGrantsConfiguration(self):  # pragma: no cover
        return QueryResultsS3AccessGrantsConfiguration.make_one(
            self.boto3_raw_data["QueryResultsS3AccessGrantsConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WorkGroupConfigurationUpdatesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkGroupConfigurationUpdatesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryRuntimeStatistics:
    boto3_raw_data: "type_defs.QueryRuntimeStatisticsTypeDef" = dataclasses.field()

    @cached_property
    def Timeline(self):  # pragma: no cover
        return QueryRuntimeStatisticsTimeline.make_one(self.boto3_raw_data["Timeline"])

    @cached_property
    def Rows(self):  # pragma: no cover
        return QueryRuntimeStatisticsRows.make_one(self.boto3_raw_data["Rows"])

    @cached_property
    def OutputStage(self):  # pragma: no cover
        return QueryStage.make_one(self.boto3_raw_data["OutputStage"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryRuntimeStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryRuntimeStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryExecution:
    boto3_raw_data: "type_defs.QueryExecutionTypeDef" = dataclasses.field()

    QueryExecutionId = field("QueryExecutionId")
    Query = field("Query")
    StatementType = field("StatementType")

    @cached_property
    def ManagedQueryResultsConfiguration(self):  # pragma: no cover
        return ManagedQueryResultsConfiguration.make_one(
            self.boto3_raw_data["ManagedQueryResultsConfiguration"]
        )

    @cached_property
    def ResultConfiguration(self):  # pragma: no cover
        return ResultConfiguration.make_one(self.boto3_raw_data["ResultConfiguration"])

    @cached_property
    def ResultReuseConfiguration(self):  # pragma: no cover
        return ResultReuseConfiguration.make_one(
            self.boto3_raw_data["ResultReuseConfiguration"]
        )

    @cached_property
    def QueryExecutionContext(self):  # pragma: no cover
        return QueryExecutionContext.make_one(
            self.boto3_raw_data["QueryExecutionContext"]
        )

    @cached_property
    def Status(self):  # pragma: no cover
        return QueryExecutionStatus.make_one(self.boto3_raw_data["Status"])

    @cached_property
    def Statistics(self):  # pragma: no cover
        return QueryExecutionStatistics.make_one(self.boto3_raw_data["Statistics"])

    WorkGroup = field("WorkGroup")

    @cached_property
    def EngineVersion(self):  # pragma: no cover
        return EngineVersion.make_one(self.boto3_raw_data["EngineVersion"])

    ExecutionParameters = field("ExecutionParameters")
    SubstatementType = field("SubstatementType")

    @cached_property
    def QueryResultsS3AccessGrantsConfiguration(self):  # pragma: no cover
        return QueryResultsS3AccessGrantsConfiguration.make_one(
            self.boto3_raw_data["QueryResultsS3AccessGrantsConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryExecutionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryExecutionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartQueryExecutionInput:
    boto3_raw_data: "type_defs.StartQueryExecutionInputTypeDef" = dataclasses.field()

    QueryString = field("QueryString")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def QueryExecutionContext(self):  # pragma: no cover
        return QueryExecutionContext.make_one(
            self.boto3_raw_data["QueryExecutionContext"]
        )

    @cached_property
    def ResultConfiguration(self):  # pragma: no cover
        return ResultConfiguration.make_one(self.boto3_raw_data["ResultConfiguration"])

    WorkGroup = field("WorkGroup")
    ExecutionParameters = field("ExecutionParameters")

    @cached_property
    def ResultReuseConfiguration(self):  # pragma: no cover
        return ResultReuseConfiguration.make_one(
            self.boto3_raw_data["ResultReuseConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartQueryExecutionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartQueryExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryResultsOutput:
    boto3_raw_data: "type_defs.GetQueryResultsOutputTypeDef" = dataclasses.field()

    UpdateCount = field("UpdateCount")

    @cached_property
    def ResultSet(self):  # pragma: no cover
        return ResultSet.make_one(self.boto3_raw_data["ResultSet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueryResultsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryResultsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkGroupInput:
    boto3_raw_data: "type_defs.CreateWorkGroupInputTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Configuration(self):  # pragma: no cover
        return WorkGroupConfiguration.make_one(self.boto3_raw_data["Configuration"])

    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkGroup:
    boto3_raw_data: "type_defs.WorkGroupTypeDef" = dataclasses.field()

    Name = field("Name")
    State = field("State")

    @cached_property
    def Configuration(self):  # pragma: no cover
        return WorkGroupConfiguration.make_one(self.boto3_raw_data["Configuration"])

    Description = field("Description")
    CreationTime = field("CreationTime")
    IdentityCenterApplicationArn = field("IdentityCenterApplicationArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkGroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkGroupInput:
    boto3_raw_data: "type_defs.UpdateWorkGroupInputTypeDef" = dataclasses.field()

    WorkGroup = field("WorkGroup")
    Description = field("Description")

    @cached_property
    def ConfigurationUpdates(self):  # pragma: no cover
        return WorkGroupConfigurationUpdates.make_one(
            self.boto3_raw_data["ConfigurationUpdates"]
        )

    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryRuntimeStatisticsOutput:
    boto3_raw_data: "type_defs.GetQueryRuntimeStatisticsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def QueryRuntimeStatistics(self):  # pragma: no cover
        return QueryRuntimeStatistics.make_one(
            self.boto3_raw_data["QueryRuntimeStatistics"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetQueryRuntimeStatisticsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryRuntimeStatisticsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetQueryExecutionOutput:
    boto3_raw_data: "type_defs.BatchGetQueryExecutionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def QueryExecutions(self):  # pragma: no cover
        return QueryExecution.make_many(self.boto3_raw_data["QueryExecutions"])

    @cached_property
    def UnprocessedQueryExecutionIds(self):  # pragma: no cover
        return UnprocessedQueryExecutionId.make_many(
            self.boto3_raw_data["UnprocessedQueryExecutionIds"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetQueryExecutionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetQueryExecutionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryExecutionOutput:
    boto3_raw_data: "type_defs.GetQueryExecutionOutputTypeDef" = dataclasses.field()

    @cached_property
    def QueryExecution(self):  # pragma: no cover
        return QueryExecution.make_one(self.boto3_raw_data["QueryExecution"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueryExecutionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryExecutionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkGroupOutput:
    boto3_raw_data: "type_defs.GetWorkGroupOutputTypeDef" = dataclasses.field()

    @cached_property
    def WorkGroup(self):  # pragma: no cover
        return WorkGroup.make_one(self.boto3_raw_data["WorkGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
