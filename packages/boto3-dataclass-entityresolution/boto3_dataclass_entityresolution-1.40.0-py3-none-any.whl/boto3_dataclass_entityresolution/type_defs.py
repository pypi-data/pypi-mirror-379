# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_entityresolution import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AddPolicyStatementInput:
    boto3_raw_data: "type_defs.AddPolicyStatementInputTypeDef" = dataclasses.field()

    arn = field("arn")
    statementId = field("statementId")
    effect = field("effect")
    action = field("action")
    principal = field("principal")
    condition = field("condition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddPolicyStatementInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddPolicyStatementInputTypeDef"]
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
class BatchDeleteUniqueIdInput:
    boto3_raw_data: "type_defs.BatchDeleteUniqueIdInputTypeDef" = dataclasses.field()

    workflowName = field("workflowName")
    uniqueIds = field("uniqueIds")
    inputSource = field("inputSource")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteUniqueIdInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteUniqueIdInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUniqueIdError:
    boto3_raw_data: "type_defs.DeleteUniqueIdErrorTypeDef" = dataclasses.field()

    uniqueId = field("uniqueId")
    errorType = field("errorType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteUniqueIdErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUniqueIdErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletedUniqueId:
    boto3_raw_data: "type_defs.DeletedUniqueIdTypeDef" = dataclasses.field()

    uniqueId = field("uniqueId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeletedUniqueIdTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeletedUniqueIdTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdMappingIncrementalRunConfig:
    boto3_raw_data: "type_defs.IdMappingIncrementalRunConfigTypeDef" = (
        dataclasses.field()
    )

    incrementalRunType = field("incrementalRunType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IdMappingIncrementalRunConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdMappingIncrementalRunConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdMappingWorkflowInputSource:
    boto3_raw_data: "type_defs.IdMappingWorkflowInputSourceTypeDef" = (
        dataclasses.field()
    )

    inputSourceARN = field("inputSourceARN")
    schemaName = field("schemaName")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdMappingWorkflowInputSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdMappingWorkflowInputSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdMappingWorkflowOutputSource:
    boto3_raw_data: "type_defs.IdMappingWorkflowOutputSourceTypeDef" = (
        dataclasses.field()
    )

    outputS3Path = field("outputS3Path")
    KMSArn = field("KMSArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IdMappingWorkflowOutputSourceTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdMappingWorkflowOutputSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdNamespaceInputSource:
    boto3_raw_data: "type_defs.IdNamespaceInputSourceTypeDef" = dataclasses.field()

    inputSourceARN = field("inputSourceARN")
    schemaName = field("schemaName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdNamespaceInputSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdNamespaceInputSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IncrementalRunConfig:
    boto3_raw_data: "type_defs.IncrementalRunConfigTypeDef" = dataclasses.field()

    incrementalRunType = field("incrementalRunType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IncrementalRunConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IncrementalRunConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputSource:
    boto3_raw_data: "type_defs.InputSourceTypeDef" = dataclasses.field()

    inputSourceARN = field("inputSourceARN")
    schemaName = field("schemaName")
    applyNormalization = field("applyNormalization")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaInputAttribute:
    boto3_raw_data: "type_defs.SchemaInputAttributeTypeDef" = dataclasses.field()

    fieldName = field("fieldName")
    type = field("type")
    groupName = field("groupName")
    matchKey = field("matchKey")
    subType = field("subType")
    hashed = field("hashed")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SchemaInputAttributeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchemaInputAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIdMappingWorkflowInput:
    boto3_raw_data: "type_defs.DeleteIdMappingWorkflowInputTypeDef" = (
        dataclasses.field()
    )

    workflowName = field("workflowName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIdMappingWorkflowInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIdMappingWorkflowInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIdNamespaceInput:
    boto3_raw_data: "type_defs.DeleteIdNamespaceInputTypeDef" = dataclasses.field()

    idNamespaceName = field("idNamespaceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIdNamespaceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIdNamespaceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMatchingWorkflowInput:
    boto3_raw_data: "type_defs.DeleteMatchingWorkflowInputTypeDef" = dataclasses.field()

    workflowName = field("workflowName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMatchingWorkflowInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMatchingWorkflowInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePolicyStatementInput:
    boto3_raw_data: "type_defs.DeletePolicyStatementInputTypeDef" = dataclasses.field()

    arn = field("arn")
    statementId = field("statementId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePolicyStatementInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePolicyStatementInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSchemaMappingInput:
    boto3_raw_data: "type_defs.DeleteSchemaMappingInputTypeDef" = dataclasses.field()

    schemaName = field("schemaName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSchemaMappingInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSchemaMappingInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorDetails:
    boto3_raw_data: "type_defs.ErrorDetailsTypeDef" = dataclasses.field()

    errorMessage = field("errorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedRecord:
    boto3_raw_data: "type_defs.FailedRecordTypeDef" = dataclasses.field()

    inputSourceARN = field("inputSourceARN")
    uniqueId = field("uniqueId")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailedRecordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FailedRecordTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Record:
    boto3_raw_data: "type_defs.RecordTypeDef" = dataclasses.field()

    inputSourceARN = field("inputSourceARN")
    uniqueId = field("uniqueId")
    recordAttributeMap = field("recordAttributeMap")

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
class GetIdMappingJobInput:
    boto3_raw_data: "type_defs.GetIdMappingJobInputTypeDef" = dataclasses.field()

    workflowName = field("workflowName")
    jobId = field("jobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIdMappingJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdMappingJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdMappingJobMetrics:
    boto3_raw_data: "type_defs.IdMappingJobMetricsTypeDef" = dataclasses.field()

    inputRecords = field("inputRecords")
    totalRecordsProcessed = field("totalRecordsProcessed")
    recordsNotProcessed = field("recordsNotProcessed")
    deleteRecordsProcessed = field("deleteRecordsProcessed")
    totalMappedRecords = field("totalMappedRecords")
    totalMappedSourceRecords = field("totalMappedSourceRecords")
    totalMappedTargetRecords = field("totalMappedTargetRecords")
    uniqueRecordsLoaded = field("uniqueRecordsLoaded")
    newMappedRecords = field("newMappedRecords")
    newMappedSourceRecords = field("newMappedSourceRecords")
    newMappedTargetRecords = field("newMappedTargetRecords")
    newUniqueRecordsLoaded = field("newUniqueRecordsLoaded")
    mappedRecordsRemoved = field("mappedRecordsRemoved")
    mappedSourceRecordsRemoved = field("mappedSourceRecordsRemoved")
    mappedTargetRecordsRemoved = field("mappedTargetRecordsRemoved")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdMappingJobMetricsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdMappingJobMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdMappingJobOutputSource:
    boto3_raw_data: "type_defs.IdMappingJobOutputSourceTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    outputS3Path = field("outputS3Path")
    KMSArn = field("KMSArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdMappingJobOutputSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdMappingJobOutputSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdMappingWorkflowInput:
    boto3_raw_data: "type_defs.GetIdMappingWorkflowInputTypeDef" = dataclasses.field()

    workflowName = field("workflowName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIdMappingWorkflowInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdMappingWorkflowInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdNamespaceInput:
    boto3_raw_data: "type_defs.GetIdNamespaceInputTypeDef" = dataclasses.field()

    idNamespaceName = field("idNamespaceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIdNamespaceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdNamespaceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMatchIdInput:
    boto3_raw_data: "type_defs.GetMatchIdInputTypeDef" = dataclasses.field()

    workflowName = field("workflowName")
    record = field("record")
    applyNormalization = field("applyNormalization")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMatchIdInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetMatchIdInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMatchingJobInput:
    boto3_raw_data: "type_defs.GetMatchingJobInputTypeDef" = dataclasses.field()

    workflowName = field("workflowName")
    jobId = field("jobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMatchingJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMatchingJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobMetrics:
    boto3_raw_data: "type_defs.JobMetricsTypeDef" = dataclasses.field()

    inputRecords = field("inputRecords")
    totalRecordsProcessed = field("totalRecordsProcessed")
    recordsNotProcessed = field("recordsNotProcessed")
    deleteRecordsProcessed = field("deleteRecordsProcessed")
    matchIDs = field("matchIDs")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobMetricsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobMetricsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobOutputSource:
    boto3_raw_data: "type_defs.JobOutputSourceTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    outputS3Path = field("outputS3Path")
    KMSArn = field("KMSArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobOutputSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobOutputSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMatchingWorkflowInput:
    boto3_raw_data: "type_defs.GetMatchingWorkflowInputTypeDef" = dataclasses.field()

    workflowName = field("workflowName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMatchingWorkflowInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMatchingWorkflowInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyInput:
    boto3_raw_data: "type_defs.GetPolicyInputTypeDef" = dataclasses.field()

    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPolicyInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetPolicyInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProviderServiceInput:
    boto3_raw_data: "type_defs.GetProviderServiceInputTypeDef" = dataclasses.field()

    providerName = field("providerName")
    providerServiceName = field("providerServiceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetProviderServiceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProviderServiceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProviderIdNameSpaceConfiguration:
    boto3_raw_data: "type_defs.ProviderIdNameSpaceConfigurationTypeDef" = (
        dataclasses.field()
    )

    description = field("description")
    providerTargetConfigurationDefinition = field(
        "providerTargetConfigurationDefinition"
    )
    providerSourceConfigurationDefinition = field(
        "providerSourceConfigurationDefinition"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProviderIdNameSpaceConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProviderIdNameSpaceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProviderIntermediateDataAccessConfiguration:
    boto3_raw_data: "type_defs.ProviderIntermediateDataAccessConfigurationTypeDef" = (
        dataclasses.field()
    )

    awsAccountIds = field("awsAccountIds")
    requiredBucketActions = field("requiredBucketActions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProviderIntermediateDataAccessConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProviderIntermediateDataAccessConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSchemaMappingInput:
    boto3_raw_data: "type_defs.GetSchemaMappingInputTypeDef" = dataclasses.field()

    schemaName = field("schemaName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSchemaMappingInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSchemaMappingInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleOutput:
    boto3_raw_data: "type_defs.RuleOutputTypeDef" = dataclasses.field()

    ruleName = field("ruleName")
    matchingKeys = field("matchingKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Rule:
    boto3_raw_data: "type_defs.RuleTypeDef" = dataclasses.field()

    ruleName = field("ruleName")
    matchingKeys = field("matchingKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdMappingWorkflowSummary:
    boto3_raw_data: "type_defs.IdMappingWorkflowSummaryTypeDef" = dataclasses.field()

    workflowName = field("workflowName")
    workflowArn = field("workflowArn")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdMappingWorkflowSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdMappingWorkflowSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdNamespaceIdMappingWorkflowMetadata:
    boto3_raw_data: "type_defs.IdNamespaceIdMappingWorkflowMetadataTypeDef" = (
        dataclasses.field()
    )

    idMappingType = field("idMappingType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IdNamespaceIdMappingWorkflowMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdNamespaceIdMappingWorkflowMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NamespaceProviderPropertiesOutput:
    boto3_raw_data: "type_defs.NamespaceProviderPropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    providerServiceArn = field("providerServiceArn")
    providerConfiguration = field("providerConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NamespaceProviderPropertiesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NamespaceProviderPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntermediateSourceConfiguration:
    boto3_raw_data: "type_defs.IntermediateSourceConfigurationTypeDef" = (
        dataclasses.field()
    )

    intermediateS3Path = field("intermediateS3Path")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IntermediateSourceConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntermediateSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobSummary:
    boto3_raw_data: "type_defs.JobSummaryTypeDef" = dataclasses.field()

    jobId = field("jobId")
    status = field("status")
    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobSummaryTypeDef"]]
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
class ListIdMappingJobsInput:
    boto3_raw_data: "type_defs.ListIdMappingJobsInputTypeDef" = dataclasses.field()

    workflowName = field("workflowName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdMappingJobsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdMappingJobsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdMappingWorkflowsInput:
    boto3_raw_data: "type_defs.ListIdMappingWorkflowsInputTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdMappingWorkflowsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdMappingWorkflowsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdNamespacesInput:
    boto3_raw_data: "type_defs.ListIdNamespacesInputTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdNamespacesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdNamespacesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMatchingJobsInput:
    boto3_raw_data: "type_defs.ListMatchingJobsInputTypeDef" = dataclasses.field()

    workflowName = field("workflowName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMatchingJobsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMatchingJobsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMatchingWorkflowsInput:
    boto3_raw_data: "type_defs.ListMatchingWorkflowsInputTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMatchingWorkflowsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMatchingWorkflowsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchingWorkflowSummary:
    boto3_raw_data: "type_defs.MatchingWorkflowSummaryTypeDef" = dataclasses.field()

    workflowName = field("workflowName")
    workflowArn = field("workflowArn")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    resolutionType = field("resolutionType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MatchingWorkflowSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MatchingWorkflowSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProviderServicesInput:
    boto3_raw_data: "type_defs.ListProviderServicesInputTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    providerName = field("providerName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProviderServicesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProviderServicesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProviderServiceSummary:
    boto3_raw_data: "type_defs.ProviderServiceSummaryTypeDef" = dataclasses.field()

    providerServiceArn = field("providerServiceArn")
    providerName = field("providerName")
    providerServiceDisplayName = field("providerServiceDisplayName")
    providerServiceName = field("providerServiceName")
    providerServiceType = field("providerServiceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProviderServiceSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProviderServiceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSchemaMappingsInput:
    boto3_raw_data: "type_defs.ListSchemaMappingsInputTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSchemaMappingsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchemaMappingsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaMappingSummary:
    boto3_raw_data: "type_defs.SchemaMappingSummaryTypeDef" = dataclasses.field()

    schemaName = field("schemaName")
    schemaArn = field("schemaArn")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    hasWorkflows = field("hasWorkflows")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SchemaMappingSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchemaMappingSummaryTypeDef"]
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

    resourceArn = field("resourceArn")

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
class MatchedRecord:
    boto3_raw_data: "type_defs.MatchedRecordTypeDef" = dataclasses.field()

    inputSourceARN = field("inputSourceARN")
    recordId = field("recordId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MatchedRecordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MatchedRecordTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NamespaceProviderProperties:
    boto3_raw_data: "type_defs.NamespaceProviderPropertiesTypeDef" = dataclasses.field()

    providerServiceArn = field("providerServiceArn")
    providerConfiguration = field("providerConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NamespaceProviderPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NamespaceProviderPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputAttribute:
    boto3_raw_data: "type_defs.OutputAttributeTypeDef" = dataclasses.field()

    name = field("name")
    hashed = field("hashed")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputAttributeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProviderSchemaAttribute:
    boto3_raw_data: "type_defs.ProviderSchemaAttributeTypeDef" = dataclasses.field()

    fieldName = field("fieldName")
    type = field("type")
    subType = field("subType")
    hashing = field("hashing")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProviderSchemaAttributeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProviderSchemaAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProviderMarketplaceConfiguration:
    boto3_raw_data: "type_defs.ProviderMarketplaceConfigurationTypeDef" = (
        dataclasses.field()
    )

    dataSetId = field("dataSetId")
    revisionId = field("revisionId")
    assetId = field("assetId")
    listingId = field("listingId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProviderMarketplaceConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProviderMarketplaceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPolicyInput:
    boto3_raw_data: "type_defs.PutPolicyInputTypeDef" = dataclasses.field()

    arn = field("arn")
    policy = field("policy")
    token = field("token")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutPolicyInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutPolicyInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleCondition:
    boto3_raw_data: "type_defs.RuleConditionTypeDef" = dataclasses.field()

    ruleName = field("ruleName")
    condition = field("condition")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMatchingJobInput:
    boto3_raw_data: "type_defs.StartMatchingJobInputTypeDef" = dataclasses.field()

    workflowName = field("workflowName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMatchingJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMatchingJobInputTypeDef"]
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

    resourceArn = field("resourceArn")
    tags = field("tags")

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
class UntagResourceInput:
    boto3_raw_data: "type_defs.UntagResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

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
class AddPolicyStatementOutput:
    boto3_raw_data: "type_defs.AddPolicyStatementOutputTypeDef" = dataclasses.field()

    arn = field("arn")
    token = field("token")
    policy = field("policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddPolicyStatementOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddPolicyStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIdMappingWorkflowOutput:
    boto3_raw_data: "type_defs.DeleteIdMappingWorkflowOutputTypeDef" = (
        dataclasses.field()
    )

    message = field("message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteIdMappingWorkflowOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIdMappingWorkflowOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIdNamespaceOutput:
    boto3_raw_data: "type_defs.DeleteIdNamespaceOutputTypeDef" = dataclasses.field()

    message = field("message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIdNamespaceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIdNamespaceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMatchingWorkflowOutput:
    boto3_raw_data: "type_defs.DeleteMatchingWorkflowOutputTypeDef" = (
        dataclasses.field()
    )

    message = field("message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMatchingWorkflowOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMatchingWorkflowOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePolicyStatementOutput:
    boto3_raw_data: "type_defs.DeletePolicyStatementOutputTypeDef" = dataclasses.field()

    arn = field("arn")
    token = field("token")
    policy = field("policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePolicyStatementOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePolicyStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSchemaMappingOutput:
    boto3_raw_data: "type_defs.DeleteSchemaMappingOutputTypeDef" = dataclasses.field()

    message = field("message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSchemaMappingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSchemaMappingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMatchIdOutput:
    boto3_raw_data: "type_defs.GetMatchIdOutputTypeDef" = dataclasses.field()

    matchId = field("matchId")
    matchRule = field("matchRule")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMatchIdOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMatchIdOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyOutput:
    boto3_raw_data: "type_defs.GetPolicyOutputTypeDef" = dataclasses.field()

    arn = field("arn")
    token = field("token")
    policy = field("policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPolicyOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetPolicyOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceOutput:
    boto3_raw_data: "type_defs.ListTagsForResourceOutputTypeDef" = dataclasses.field()

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

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
class PutPolicyOutput:
    boto3_raw_data: "type_defs.PutPolicyOutputTypeDef" = dataclasses.field()

    arn = field("arn")
    token = field("token")
    policy = field("policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutPolicyOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutPolicyOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMatchingJobOutput:
    boto3_raw_data: "type_defs.StartMatchingJobOutputTypeDef" = dataclasses.field()

    jobId = field("jobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMatchingJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMatchingJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteUniqueIdOutput:
    boto3_raw_data: "type_defs.BatchDeleteUniqueIdOutputTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def errors(self):  # pragma: no cover
        return DeleteUniqueIdError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def deleted(self):  # pragma: no cover
        return DeletedUniqueId.make_many(self.boto3_raw_data["deleted"])

    disconnectedUniqueIds = field("disconnectedUniqueIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteUniqueIdOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteUniqueIdOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSchemaMappingInput:
    boto3_raw_data: "type_defs.CreateSchemaMappingInputTypeDef" = dataclasses.field()

    schemaName = field("schemaName")

    @cached_property
    def mappedInputFields(self):  # pragma: no cover
        return SchemaInputAttribute.make_many(self.boto3_raw_data["mappedInputFields"])

    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSchemaMappingInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSchemaMappingInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSchemaMappingOutput:
    boto3_raw_data: "type_defs.CreateSchemaMappingOutputTypeDef" = dataclasses.field()

    schemaName = field("schemaName")
    schemaArn = field("schemaArn")
    description = field("description")

    @cached_property
    def mappedInputFields(self):  # pragma: no cover
        return SchemaInputAttribute.make_many(self.boto3_raw_data["mappedInputFields"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSchemaMappingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSchemaMappingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSchemaMappingOutput:
    boto3_raw_data: "type_defs.GetSchemaMappingOutputTypeDef" = dataclasses.field()

    schemaName = field("schemaName")
    schemaArn = field("schemaArn")
    description = field("description")

    @cached_property
    def mappedInputFields(self):  # pragma: no cover
        return SchemaInputAttribute.make_many(self.boto3_raw_data["mappedInputFields"])

    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    tags = field("tags")
    hasWorkflows = field("hasWorkflows")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSchemaMappingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSchemaMappingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSchemaMappingInput:
    boto3_raw_data: "type_defs.UpdateSchemaMappingInputTypeDef" = dataclasses.field()

    schemaName = field("schemaName")

    @cached_property
    def mappedInputFields(self):  # pragma: no cover
        return SchemaInputAttribute.make_many(self.boto3_raw_data["mappedInputFields"])

    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSchemaMappingInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSchemaMappingInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSchemaMappingOutput:
    boto3_raw_data: "type_defs.UpdateSchemaMappingOutputTypeDef" = dataclasses.field()

    schemaName = field("schemaName")
    schemaArn = field("schemaArn")
    description = field("description")

    @cached_property
    def mappedInputFields(self):  # pragma: no cover
        return SchemaInputAttribute.make_many(self.boto3_raw_data["mappedInputFields"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSchemaMappingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSchemaMappingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateMatchIdInput:
    boto3_raw_data: "type_defs.GenerateMatchIdInputTypeDef" = dataclasses.field()

    workflowName = field("workflowName")

    @cached_property
    def records(self):  # pragma: no cover
        return Record.make_many(self.boto3_raw_data["records"])

    processingType = field("processingType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateMatchIdInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateMatchIdInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdMappingJobOutput:
    boto3_raw_data: "type_defs.GetIdMappingJobOutputTypeDef" = dataclasses.field()

    jobId = field("jobId")
    status = field("status")
    startTime = field("startTime")
    endTime = field("endTime")

    @cached_property
    def metrics(self):  # pragma: no cover
        return IdMappingJobMetrics.make_one(self.boto3_raw_data["metrics"])

    @cached_property
    def errorDetails(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["errorDetails"])

    @cached_property
    def outputSourceConfig(self):  # pragma: no cover
        return IdMappingJobOutputSource.make_many(
            self.boto3_raw_data["outputSourceConfig"]
        )

    jobType = field("jobType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIdMappingJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdMappingJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartIdMappingJobInput:
    boto3_raw_data: "type_defs.StartIdMappingJobInputTypeDef" = dataclasses.field()

    workflowName = field("workflowName")

    @cached_property
    def outputSourceConfig(self):  # pragma: no cover
        return IdMappingJobOutputSource.make_many(
            self.boto3_raw_data["outputSourceConfig"]
        )

    jobType = field("jobType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartIdMappingJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartIdMappingJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartIdMappingJobOutput:
    boto3_raw_data: "type_defs.StartIdMappingJobOutputTypeDef" = dataclasses.field()

    jobId = field("jobId")

    @cached_property
    def outputSourceConfig(self):  # pragma: no cover
        return IdMappingJobOutputSource.make_many(
            self.boto3_raw_data["outputSourceConfig"]
        )

    jobType = field("jobType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartIdMappingJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartIdMappingJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMatchingJobOutput:
    boto3_raw_data: "type_defs.GetMatchingJobOutputTypeDef" = dataclasses.field()

    jobId = field("jobId")
    status = field("status")
    startTime = field("startTime")
    endTime = field("endTime")

    @cached_property
    def metrics(self):  # pragma: no cover
        return JobMetrics.make_one(self.boto3_raw_data["metrics"])

    @cached_property
    def errorDetails(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["errorDetails"])

    @cached_property
    def outputSourceConfig(self):  # pragma: no cover
        return JobOutputSource.make_many(self.boto3_raw_data["outputSourceConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMatchingJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMatchingJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdMappingRuleBasedPropertiesOutput:
    boto3_raw_data: "type_defs.IdMappingRuleBasedPropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    ruleDefinitionType = field("ruleDefinitionType")
    attributeMatchingModel = field("attributeMatchingModel")
    recordMatchingModel = field("recordMatchingModel")

    @cached_property
    def rules(self):  # pragma: no cover
        return RuleOutput.make_many(self.boto3_raw_data["rules"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IdMappingRuleBasedPropertiesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdMappingRuleBasedPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NamespaceRuleBasedPropertiesOutput:
    boto3_raw_data: "type_defs.NamespaceRuleBasedPropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def rules(self):  # pragma: no cover
        return RuleOutput.make_many(self.boto3_raw_data["rules"])

    ruleDefinitionTypes = field("ruleDefinitionTypes")
    attributeMatchingModel = field("attributeMatchingModel")
    recordMatchingModels = field("recordMatchingModels")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NamespaceRuleBasedPropertiesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NamespaceRuleBasedPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleBasedPropertiesOutput:
    boto3_raw_data: "type_defs.RuleBasedPropertiesOutputTypeDef" = dataclasses.field()

    @cached_property
    def rules(self):  # pragma: no cover
        return RuleOutput.make_many(self.boto3_raw_data["rules"])

    attributeMatchingModel = field("attributeMatchingModel")
    matchPurpose = field("matchPurpose")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleBasedPropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleBasedPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdMappingRuleBasedProperties:
    boto3_raw_data: "type_defs.IdMappingRuleBasedPropertiesTypeDef" = (
        dataclasses.field()
    )

    ruleDefinitionType = field("ruleDefinitionType")
    attributeMatchingModel = field("attributeMatchingModel")
    recordMatchingModel = field("recordMatchingModel")

    @cached_property
    def rules(self):  # pragma: no cover
        return Rule.make_many(self.boto3_raw_data["rules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdMappingRuleBasedPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdMappingRuleBasedPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleBasedProperties:
    boto3_raw_data: "type_defs.RuleBasedPropertiesTypeDef" = dataclasses.field()

    @cached_property
    def rules(self):  # pragma: no cover
        return Rule.make_many(self.boto3_raw_data["rules"])

    attributeMatchingModel = field("attributeMatchingModel")
    matchPurpose = field("matchPurpose")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleBasedPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleBasedPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdMappingWorkflowsOutput:
    boto3_raw_data: "type_defs.ListIdMappingWorkflowsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def workflowSummaries(self):  # pragma: no cover
        return IdMappingWorkflowSummary.make_many(
            self.boto3_raw_data["workflowSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdMappingWorkflowsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdMappingWorkflowsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdNamespaceSummary:
    boto3_raw_data: "type_defs.IdNamespaceSummaryTypeDef" = dataclasses.field()

    idNamespaceName = field("idNamespaceName")
    idNamespaceArn = field("idNamespaceArn")
    type = field("type")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    description = field("description")

    @cached_property
    def idMappingWorkflowProperties(self):  # pragma: no cover
        return IdNamespaceIdMappingWorkflowMetadata.make_many(
            self.boto3_raw_data["idMappingWorkflowProperties"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdNamespaceSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdNamespaceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProviderPropertiesOutput:
    boto3_raw_data: "type_defs.ProviderPropertiesOutputTypeDef" = dataclasses.field()

    providerServiceArn = field("providerServiceArn")
    providerConfiguration = field("providerConfiguration")

    @cached_property
    def intermediateSourceConfiguration(self):  # pragma: no cover
        return IntermediateSourceConfiguration.make_one(
            self.boto3_raw_data["intermediateSourceConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProviderPropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProviderPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProviderProperties:
    boto3_raw_data: "type_defs.ProviderPropertiesTypeDef" = dataclasses.field()

    providerServiceArn = field("providerServiceArn")
    providerConfiguration = field("providerConfiguration")

    @cached_property
    def intermediateSourceConfiguration(self):  # pragma: no cover
        return IntermediateSourceConfiguration.make_one(
            self.boto3_raw_data["intermediateSourceConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProviderPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProviderPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdMappingJobsOutput:
    boto3_raw_data: "type_defs.ListIdMappingJobsOutputTypeDef" = dataclasses.field()

    @cached_property
    def jobs(self):  # pragma: no cover
        return JobSummary.make_many(self.boto3_raw_data["jobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdMappingJobsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdMappingJobsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMatchingJobsOutput:
    boto3_raw_data: "type_defs.ListMatchingJobsOutputTypeDef" = dataclasses.field()

    @cached_property
    def jobs(self):  # pragma: no cover
        return JobSummary.make_many(self.boto3_raw_data["jobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMatchingJobsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMatchingJobsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdMappingJobsInputPaginate:
    boto3_raw_data: "type_defs.ListIdMappingJobsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    workflowName = field("workflowName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListIdMappingJobsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdMappingJobsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdMappingWorkflowsInputPaginate:
    boto3_raw_data: "type_defs.ListIdMappingWorkflowsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListIdMappingWorkflowsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdMappingWorkflowsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdNamespacesInputPaginate:
    boto3_raw_data: "type_defs.ListIdNamespacesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListIdNamespacesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdNamespacesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMatchingJobsInputPaginate:
    boto3_raw_data: "type_defs.ListMatchingJobsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    workflowName = field("workflowName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMatchingJobsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMatchingJobsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMatchingWorkflowsInputPaginate:
    boto3_raw_data: "type_defs.ListMatchingWorkflowsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMatchingWorkflowsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMatchingWorkflowsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProviderServicesInputPaginate:
    boto3_raw_data: "type_defs.ListProviderServicesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    providerName = field("providerName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProviderServicesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProviderServicesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSchemaMappingsInputPaginate:
    boto3_raw_data: "type_defs.ListSchemaMappingsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSchemaMappingsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchemaMappingsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMatchingWorkflowsOutput:
    boto3_raw_data: "type_defs.ListMatchingWorkflowsOutputTypeDef" = dataclasses.field()

    @cached_property
    def workflowSummaries(self):  # pragma: no cover
        return MatchingWorkflowSummary.make_many(
            self.boto3_raw_data["workflowSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMatchingWorkflowsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMatchingWorkflowsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProviderServicesOutput:
    boto3_raw_data: "type_defs.ListProviderServicesOutputTypeDef" = dataclasses.field()

    @cached_property
    def providerServiceSummaries(self):  # pragma: no cover
        return ProviderServiceSummary.make_many(
            self.boto3_raw_data["providerServiceSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProviderServicesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProviderServicesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSchemaMappingsOutput:
    boto3_raw_data: "type_defs.ListSchemaMappingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def schemaList(self):  # pragma: no cover
        return SchemaMappingSummary.make_many(self.boto3_raw_data["schemaList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSchemaMappingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchemaMappingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchGroup:
    boto3_raw_data: "type_defs.MatchGroupTypeDef" = dataclasses.field()

    @cached_property
    def records(self):  # pragma: no cover
        return MatchedRecord.make_many(self.boto3_raw_data["records"])

    matchId = field("matchId")
    matchRule = field("matchRule")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MatchGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MatchGroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputSourceOutput:
    boto3_raw_data: "type_defs.OutputSourceOutputTypeDef" = dataclasses.field()

    outputS3Path = field("outputS3Path")

    @cached_property
    def output(self):  # pragma: no cover
        return OutputAttribute.make_many(self.boto3_raw_data["output"])

    KMSArn = field("KMSArn")
    applyNormalization = field("applyNormalization")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutputSourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputSource:
    boto3_raw_data: "type_defs.OutputSourceTypeDef" = dataclasses.field()

    outputS3Path = field("outputS3Path")

    @cached_property
    def output(self):  # pragma: no cover
        return OutputAttribute.make_many(self.boto3_raw_data["output"])

    KMSArn = field("KMSArn")
    applyNormalization = field("applyNormalization")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProviderComponentSchema:
    boto3_raw_data: "type_defs.ProviderComponentSchemaTypeDef" = dataclasses.field()

    schemas = field("schemas")

    @cached_property
    def providerSchemaAttributes(self):  # pragma: no cover
        return ProviderSchemaAttribute.make_many(
            self.boto3_raw_data["providerSchemaAttributes"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProviderComponentSchemaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProviderComponentSchemaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProviderEndpointConfiguration:
    boto3_raw_data: "type_defs.ProviderEndpointConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def marketplaceConfiguration(self):  # pragma: no cover
        return ProviderMarketplaceConfiguration.make_one(
            self.boto3_raw_data["marketplaceConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProviderEndpointConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProviderEndpointConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleConditionPropertiesOutput:
    boto3_raw_data: "type_defs.RuleConditionPropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def rules(self):  # pragma: no cover
        return RuleCondition.make_many(self.boto3_raw_data["rules"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RuleConditionPropertiesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleConditionPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleConditionProperties:
    boto3_raw_data: "type_defs.RuleConditionPropertiesTypeDef" = dataclasses.field()

    @cached_property
    def rules(self):  # pragma: no cover
        return RuleCondition.make_many(self.boto3_raw_data["rules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleConditionPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleConditionPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdNamespaceIdMappingWorkflowPropertiesOutput:
    boto3_raw_data: "type_defs.IdNamespaceIdMappingWorkflowPropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    idMappingType = field("idMappingType")

    @cached_property
    def ruleBasedProperties(self):  # pragma: no cover
        return NamespaceRuleBasedPropertiesOutput.make_one(
            self.boto3_raw_data["ruleBasedProperties"]
        )

    @cached_property
    def providerProperties(self):  # pragma: no cover
        return NamespaceProviderPropertiesOutput.make_one(
            self.boto3_raw_data["providerProperties"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IdNamespaceIdMappingWorkflowPropertiesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdNamespaceIdMappingWorkflowPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NamespaceRuleBasedProperties:
    boto3_raw_data: "type_defs.NamespaceRuleBasedPropertiesTypeDef" = (
        dataclasses.field()
    )

    rules = field("rules")
    ruleDefinitionTypes = field("ruleDefinitionTypes")
    attributeMatchingModel = field("attributeMatchingModel")
    recordMatchingModels = field("recordMatchingModels")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NamespaceRuleBasedPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NamespaceRuleBasedPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdNamespacesOutput:
    boto3_raw_data: "type_defs.ListIdNamespacesOutputTypeDef" = dataclasses.field()

    @cached_property
    def idNamespaceSummaries(self):  # pragma: no cover
        return IdNamespaceSummary.make_many(self.boto3_raw_data["idNamespaceSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdNamespacesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdNamespacesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdMappingTechniquesOutput:
    boto3_raw_data: "type_defs.IdMappingTechniquesOutputTypeDef" = dataclasses.field()

    idMappingType = field("idMappingType")

    @cached_property
    def ruleBasedProperties(self):  # pragma: no cover
        return IdMappingRuleBasedPropertiesOutput.make_one(
            self.boto3_raw_data["ruleBasedProperties"]
        )

    @cached_property
    def providerProperties(self):  # pragma: no cover
        return ProviderPropertiesOutput.make_one(
            self.boto3_raw_data["providerProperties"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdMappingTechniquesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdMappingTechniquesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdMappingTechniques:
    boto3_raw_data: "type_defs.IdMappingTechniquesTypeDef" = dataclasses.field()

    idMappingType = field("idMappingType")

    @cached_property
    def ruleBasedProperties(self):  # pragma: no cover
        return IdMappingRuleBasedProperties.make_one(
            self.boto3_raw_data["ruleBasedProperties"]
        )

    @cached_property
    def providerProperties(self):  # pragma: no cover
        return ProviderProperties.make_one(self.boto3_raw_data["providerProperties"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdMappingTechniquesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdMappingTechniquesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateMatchIdOutput:
    boto3_raw_data: "type_defs.GenerateMatchIdOutputTypeDef" = dataclasses.field()

    @cached_property
    def matchGroups(self):  # pragma: no cover
        return MatchGroup.make_many(self.boto3_raw_data["matchGroups"])

    @cached_property
    def failedRecords(self):  # pragma: no cover
        return FailedRecord.make_many(self.boto3_raw_data["failedRecords"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateMatchIdOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateMatchIdOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProviderServiceOutput:
    boto3_raw_data: "type_defs.GetProviderServiceOutputTypeDef" = dataclasses.field()

    providerName = field("providerName")
    providerServiceName = field("providerServiceName")
    providerServiceDisplayName = field("providerServiceDisplayName")
    providerServiceType = field("providerServiceType")
    providerServiceArn = field("providerServiceArn")
    providerConfigurationDefinition = field("providerConfigurationDefinition")

    @cached_property
    def providerIdNameSpaceConfiguration(self):  # pragma: no cover
        return ProviderIdNameSpaceConfiguration.make_one(
            self.boto3_raw_data["providerIdNameSpaceConfiguration"]
        )

    providerJobConfiguration = field("providerJobConfiguration")

    @cached_property
    def providerEndpointConfiguration(self):  # pragma: no cover
        return ProviderEndpointConfiguration.make_one(
            self.boto3_raw_data["providerEndpointConfiguration"]
        )

    anonymizedOutput = field("anonymizedOutput")
    providerEntityOutputDefinition = field("providerEntityOutputDefinition")

    @cached_property
    def providerIntermediateDataAccessConfiguration(self):  # pragma: no cover
        return ProviderIntermediateDataAccessConfiguration.make_one(
            self.boto3_raw_data["providerIntermediateDataAccessConfiguration"]
        )

    @cached_property
    def providerComponentSchema(self):  # pragma: no cover
        return ProviderComponentSchema.make_one(
            self.boto3_raw_data["providerComponentSchema"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetProviderServiceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProviderServiceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolutionTechniquesOutput:
    boto3_raw_data: "type_defs.ResolutionTechniquesOutputTypeDef" = dataclasses.field()

    resolutionType = field("resolutionType")

    @cached_property
    def ruleBasedProperties(self):  # pragma: no cover
        return RuleBasedPropertiesOutput.make_one(
            self.boto3_raw_data["ruleBasedProperties"]
        )

    @cached_property
    def ruleConditionProperties(self):  # pragma: no cover
        return RuleConditionPropertiesOutput.make_one(
            self.boto3_raw_data["ruleConditionProperties"]
        )

    @cached_property
    def providerProperties(self):  # pragma: no cover
        return ProviderPropertiesOutput.make_one(
            self.boto3_raw_data["providerProperties"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResolutionTechniquesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResolutionTechniquesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolutionTechniques:
    boto3_raw_data: "type_defs.ResolutionTechniquesTypeDef" = dataclasses.field()

    resolutionType = field("resolutionType")

    @cached_property
    def ruleBasedProperties(self):  # pragma: no cover
        return RuleBasedProperties.make_one(self.boto3_raw_data["ruleBasedProperties"])

    @cached_property
    def ruleConditionProperties(self):  # pragma: no cover
        return RuleConditionProperties.make_one(
            self.boto3_raw_data["ruleConditionProperties"]
        )

    @cached_property
    def providerProperties(self):  # pragma: no cover
        return ProviderProperties.make_one(self.boto3_raw_data["providerProperties"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResolutionTechniquesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResolutionTechniquesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIdNamespaceOutput:
    boto3_raw_data: "type_defs.CreateIdNamespaceOutputTypeDef" = dataclasses.field()

    idNamespaceName = field("idNamespaceName")
    idNamespaceArn = field("idNamespaceArn")
    description = field("description")

    @cached_property
    def inputSourceConfig(self):  # pragma: no cover
        return IdNamespaceInputSource.make_many(
            self.boto3_raw_data["inputSourceConfig"]
        )

    @cached_property
    def idMappingWorkflowProperties(self):  # pragma: no cover
        return IdNamespaceIdMappingWorkflowPropertiesOutput.make_many(
            self.boto3_raw_data["idMappingWorkflowProperties"]
        )

    type = field("type")
    roleArn = field("roleArn")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIdNamespaceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIdNamespaceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdNamespaceOutput:
    boto3_raw_data: "type_defs.GetIdNamespaceOutputTypeDef" = dataclasses.field()

    idNamespaceName = field("idNamespaceName")
    idNamespaceArn = field("idNamespaceArn")
    description = field("description")

    @cached_property
    def inputSourceConfig(self):  # pragma: no cover
        return IdNamespaceInputSource.make_many(
            self.boto3_raw_data["inputSourceConfig"]
        )

    @cached_property
    def idMappingWorkflowProperties(self):  # pragma: no cover
        return IdNamespaceIdMappingWorkflowPropertiesOutput.make_many(
            self.boto3_raw_data["idMappingWorkflowProperties"]
        )

    type = field("type")
    roleArn = field("roleArn")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIdNamespaceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdNamespaceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIdNamespaceOutput:
    boto3_raw_data: "type_defs.UpdateIdNamespaceOutputTypeDef" = dataclasses.field()

    idNamespaceName = field("idNamespaceName")
    idNamespaceArn = field("idNamespaceArn")
    description = field("description")

    @cached_property
    def inputSourceConfig(self):  # pragma: no cover
        return IdNamespaceInputSource.make_many(
            self.boto3_raw_data["inputSourceConfig"]
        )

    @cached_property
    def idMappingWorkflowProperties(self):  # pragma: no cover
        return IdNamespaceIdMappingWorkflowPropertiesOutput.make_many(
            self.boto3_raw_data["idMappingWorkflowProperties"]
        )

    type = field("type")
    roleArn = field("roleArn")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIdNamespaceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIdNamespaceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIdMappingWorkflowOutput:
    boto3_raw_data: "type_defs.CreateIdMappingWorkflowOutputTypeDef" = (
        dataclasses.field()
    )

    workflowName = field("workflowName")
    workflowArn = field("workflowArn")
    description = field("description")

    @cached_property
    def inputSourceConfig(self):  # pragma: no cover
        return IdMappingWorkflowInputSource.make_many(
            self.boto3_raw_data["inputSourceConfig"]
        )

    @cached_property
    def outputSourceConfig(self):  # pragma: no cover
        return IdMappingWorkflowOutputSource.make_many(
            self.boto3_raw_data["outputSourceConfig"]
        )

    @cached_property
    def idMappingTechniques(self):  # pragma: no cover
        return IdMappingTechniquesOutput.make_one(
            self.boto3_raw_data["idMappingTechniques"]
        )

    @cached_property
    def incrementalRunConfig(self):  # pragma: no cover
        return IdMappingIncrementalRunConfig.make_one(
            self.boto3_raw_data["incrementalRunConfig"]
        )

    roleArn = field("roleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateIdMappingWorkflowOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIdMappingWorkflowOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdMappingWorkflowOutput:
    boto3_raw_data: "type_defs.GetIdMappingWorkflowOutputTypeDef" = dataclasses.field()

    workflowName = field("workflowName")
    workflowArn = field("workflowArn")
    description = field("description")

    @cached_property
    def inputSourceConfig(self):  # pragma: no cover
        return IdMappingWorkflowInputSource.make_many(
            self.boto3_raw_data["inputSourceConfig"]
        )

    @cached_property
    def outputSourceConfig(self):  # pragma: no cover
        return IdMappingWorkflowOutputSource.make_many(
            self.boto3_raw_data["outputSourceConfig"]
        )

    @cached_property
    def idMappingTechniques(self):  # pragma: no cover
        return IdMappingTechniquesOutput.make_one(
            self.boto3_raw_data["idMappingTechniques"]
        )

    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @cached_property
    def incrementalRunConfig(self):  # pragma: no cover
        return IdMappingIncrementalRunConfig.make_one(
            self.boto3_raw_data["incrementalRunConfig"]
        )

    roleArn = field("roleArn")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIdMappingWorkflowOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdMappingWorkflowOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIdMappingWorkflowOutput:
    boto3_raw_data: "type_defs.UpdateIdMappingWorkflowOutputTypeDef" = (
        dataclasses.field()
    )

    workflowName = field("workflowName")
    workflowArn = field("workflowArn")
    description = field("description")

    @cached_property
    def inputSourceConfig(self):  # pragma: no cover
        return IdMappingWorkflowInputSource.make_many(
            self.boto3_raw_data["inputSourceConfig"]
        )

    @cached_property
    def outputSourceConfig(self):  # pragma: no cover
        return IdMappingWorkflowOutputSource.make_many(
            self.boto3_raw_data["outputSourceConfig"]
        )

    @cached_property
    def idMappingTechniques(self):  # pragma: no cover
        return IdMappingTechniquesOutput.make_one(
            self.boto3_raw_data["idMappingTechniques"]
        )

    @cached_property
    def incrementalRunConfig(self):  # pragma: no cover
        return IdMappingIncrementalRunConfig.make_one(
            self.boto3_raw_data["incrementalRunConfig"]
        )

    roleArn = field("roleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateIdMappingWorkflowOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIdMappingWorkflowOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMatchingWorkflowOutput:
    boto3_raw_data: "type_defs.CreateMatchingWorkflowOutputTypeDef" = (
        dataclasses.field()
    )

    workflowName = field("workflowName")
    workflowArn = field("workflowArn")
    description = field("description")

    @cached_property
    def inputSourceConfig(self):  # pragma: no cover
        return InputSource.make_many(self.boto3_raw_data["inputSourceConfig"])

    @cached_property
    def outputSourceConfig(self):  # pragma: no cover
        return OutputSourceOutput.make_many(self.boto3_raw_data["outputSourceConfig"])

    @cached_property
    def resolutionTechniques(self):  # pragma: no cover
        return ResolutionTechniquesOutput.make_one(
            self.boto3_raw_data["resolutionTechniques"]
        )

    @cached_property
    def incrementalRunConfig(self):  # pragma: no cover
        return IncrementalRunConfig.make_one(
            self.boto3_raw_data["incrementalRunConfig"]
        )

    roleArn = field("roleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMatchingWorkflowOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMatchingWorkflowOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMatchingWorkflowOutput:
    boto3_raw_data: "type_defs.GetMatchingWorkflowOutputTypeDef" = dataclasses.field()

    workflowName = field("workflowName")
    workflowArn = field("workflowArn")
    description = field("description")

    @cached_property
    def inputSourceConfig(self):  # pragma: no cover
        return InputSource.make_many(self.boto3_raw_data["inputSourceConfig"])

    @cached_property
    def outputSourceConfig(self):  # pragma: no cover
        return OutputSourceOutput.make_many(self.boto3_raw_data["outputSourceConfig"])

    @cached_property
    def resolutionTechniques(self):  # pragma: no cover
        return ResolutionTechniquesOutput.make_one(
            self.boto3_raw_data["resolutionTechniques"]
        )

    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @cached_property
    def incrementalRunConfig(self):  # pragma: no cover
        return IncrementalRunConfig.make_one(
            self.boto3_raw_data["incrementalRunConfig"]
        )

    roleArn = field("roleArn")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMatchingWorkflowOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMatchingWorkflowOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMatchingWorkflowOutput:
    boto3_raw_data: "type_defs.UpdateMatchingWorkflowOutputTypeDef" = (
        dataclasses.field()
    )

    workflowName = field("workflowName")
    description = field("description")

    @cached_property
    def inputSourceConfig(self):  # pragma: no cover
        return InputSource.make_many(self.boto3_raw_data["inputSourceConfig"])

    @cached_property
    def outputSourceConfig(self):  # pragma: no cover
        return OutputSourceOutput.make_many(self.boto3_raw_data["outputSourceConfig"])

    @cached_property
    def resolutionTechniques(self):  # pragma: no cover
        return ResolutionTechniquesOutput.make_one(
            self.boto3_raw_data["resolutionTechniques"]
        )

    @cached_property
    def incrementalRunConfig(self):  # pragma: no cover
        return IncrementalRunConfig.make_one(
            self.boto3_raw_data["incrementalRunConfig"]
        )

    roleArn = field("roleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMatchingWorkflowOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMatchingWorkflowOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdNamespaceIdMappingWorkflowProperties:
    boto3_raw_data: "type_defs.IdNamespaceIdMappingWorkflowPropertiesTypeDef" = (
        dataclasses.field()
    )

    idMappingType = field("idMappingType")
    ruleBasedProperties = field("ruleBasedProperties")
    providerProperties = field("providerProperties")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IdNamespaceIdMappingWorkflowPropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdNamespaceIdMappingWorkflowPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIdMappingWorkflowInput:
    boto3_raw_data: "type_defs.CreateIdMappingWorkflowInputTypeDef" = (
        dataclasses.field()
    )

    workflowName = field("workflowName")

    @cached_property
    def inputSourceConfig(self):  # pragma: no cover
        return IdMappingWorkflowInputSource.make_many(
            self.boto3_raw_data["inputSourceConfig"]
        )

    idMappingTechniques = field("idMappingTechniques")
    description = field("description")

    @cached_property
    def outputSourceConfig(self):  # pragma: no cover
        return IdMappingWorkflowOutputSource.make_many(
            self.boto3_raw_data["outputSourceConfig"]
        )

    @cached_property
    def incrementalRunConfig(self):  # pragma: no cover
        return IdMappingIncrementalRunConfig.make_one(
            self.boto3_raw_data["incrementalRunConfig"]
        )

    roleArn = field("roleArn")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIdMappingWorkflowInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIdMappingWorkflowInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIdMappingWorkflowInput:
    boto3_raw_data: "type_defs.UpdateIdMappingWorkflowInputTypeDef" = (
        dataclasses.field()
    )

    workflowName = field("workflowName")

    @cached_property
    def inputSourceConfig(self):  # pragma: no cover
        return IdMappingWorkflowInputSource.make_many(
            self.boto3_raw_data["inputSourceConfig"]
        )

    idMappingTechniques = field("idMappingTechniques")
    description = field("description")

    @cached_property
    def outputSourceConfig(self):  # pragma: no cover
        return IdMappingWorkflowOutputSource.make_many(
            self.boto3_raw_data["outputSourceConfig"]
        )

    @cached_property
    def incrementalRunConfig(self):  # pragma: no cover
        return IdMappingIncrementalRunConfig.make_one(
            self.boto3_raw_data["incrementalRunConfig"]
        )

    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIdMappingWorkflowInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIdMappingWorkflowInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMatchingWorkflowInput:
    boto3_raw_data: "type_defs.CreateMatchingWorkflowInputTypeDef" = dataclasses.field()

    workflowName = field("workflowName")

    @cached_property
    def inputSourceConfig(self):  # pragma: no cover
        return InputSource.make_many(self.boto3_raw_data["inputSourceConfig"])

    outputSourceConfig = field("outputSourceConfig")
    resolutionTechniques = field("resolutionTechniques")
    roleArn = field("roleArn")
    description = field("description")

    @cached_property
    def incrementalRunConfig(self):  # pragma: no cover
        return IncrementalRunConfig.make_one(
            self.boto3_raw_data["incrementalRunConfig"]
        )

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMatchingWorkflowInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMatchingWorkflowInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMatchingWorkflowInput:
    boto3_raw_data: "type_defs.UpdateMatchingWorkflowInputTypeDef" = dataclasses.field()

    workflowName = field("workflowName")

    @cached_property
    def inputSourceConfig(self):  # pragma: no cover
        return InputSource.make_many(self.boto3_raw_data["inputSourceConfig"])

    outputSourceConfig = field("outputSourceConfig")
    resolutionTechniques = field("resolutionTechniques")
    roleArn = field("roleArn")
    description = field("description")

    @cached_property
    def incrementalRunConfig(self):  # pragma: no cover
        return IncrementalRunConfig.make_one(
            self.boto3_raw_data["incrementalRunConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMatchingWorkflowInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMatchingWorkflowInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIdNamespaceInput:
    boto3_raw_data: "type_defs.CreateIdNamespaceInputTypeDef" = dataclasses.field()

    idNamespaceName = field("idNamespaceName")
    type = field("type")
    description = field("description")

    @cached_property
    def inputSourceConfig(self):  # pragma: no cover
        return IdNamespaceInputSource.make_many(
            self.boto3_raw_data["inputSourceConfig"]
        )

    idMappingWorkflowProperties = field("idMappingWorkflowProperties")
    roleArn = field("roleArn")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIdNamespaceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIdNamespaceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIdNamespaceInput:
    boto3_raw_data: "type_defs.UpdateIdNamespaceInputTypeDef" = dataclasses.field()

    idNamespaceName = field("idNamespaceName")
    description = field("description")

    @cached_property
    def inputSourceConfig(self):  # pragma: no cover
        return IdNamespaceInputSource.make_many(
            self.boto3_raw_data["inputSourceConfig"]
        )

    idMappingWorkflowProperties = field("idMappingWorkflowProperties")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIdNamespaceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIdNamespaceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
