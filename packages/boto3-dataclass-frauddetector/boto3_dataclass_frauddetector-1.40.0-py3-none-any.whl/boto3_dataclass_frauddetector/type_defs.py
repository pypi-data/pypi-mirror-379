# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_frauddetector import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ATIMetricDataPoint:
    boto3_raw_data: "type_defs.ATIMetricDataPointTypeDef" = dataclasses.field()

    cr = field("cr")
    adr = field("adr")
    threshold = field("threshold")
    atodr = field("atodr")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ATIMetricDataPointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ATIMetricDataPointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ATIModelPerformance:
    boto3_raw_data: "type_defs.ATIModelPerformanceTypeDef" = dataclasses.field()

    asi = field("asi")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ATIModelPerformanceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ATIModelPerformanceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregatedLogOddsMetric:
    boto3_raw_data: "type_defs.AggregatedLogOddsMetricTypeDef" = dataclasses.field()

    variableNames = field("variableNames")
    aggregatedVariablesImportance = field("aggregatedVariablesImportance")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AggregatedLogOddsMetricTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregatedLogOddsMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregatedVariablesImpactExplanation:
    boto3_raw_data: "type_defs.AggregatedVariablesImpactExplanationTypeDef" = (
        dataclasses.field()
    )

    eventVariableNames = field("eventVariableNames")
    relativeImpact = field("relativeImpact")
    logOddsImpact = field("logOddsImpact")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AggregatedVariablesImpactExplanationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregatedVariablesImpactExplanationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllowDenyList:
    boto3_raw_data: "type_defs.AllowDenyListTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    variableType = field("variableType")
    createdTime = field("createdTime")
    updatedTime = field("updatedTime")
    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AllowDenyListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AllowDenyListTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateVariableError:
    boto3_raw_data: "type_defs.BatchCreateVariableErrorTypeDef" = dataclasses.field()

    name = field("name")
    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchCreateVariableErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateVariableErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

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
class VariableEntry:
    boto3_raw_data: "type_defs.VariableEntryTypeDef" = dataclasses.field()

    name = field("name")
    dataType = field("dataType")
    dataSource = field("dataSource")
    defaultValue = field("defaultValue")
    description = field("description")
    variableType = field("variableType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VariableEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VariableEntryTypeDef"]],
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
class BatchGetVariableError:
    boto3_raw_data: "type_defs.BatchGetVariableErrorTypeDef" = dataclasses.field()

    name = field("name")
    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetVariableErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetVariableErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetVariableRequest:
    boto3_raw_data: "type_defs.BatchGetVariableRequestTypeDef" = dataclasses.field()

    names = field("names")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetVariableRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetVariableRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Variable:
    boto3_raw_data: "type_defs.VariableTypeDef" = dataclasses.field()

    name = field("name")
    dataType = field("dataType")
    dataSource = field("dataSource")
    defaultValue = field("defaultValue")
    description = field("description")
    variableType = field("variableType")
    lastUpdatedTime = field("lastUpdatedTime")
    createdTime = field("createdTime")
    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VariableTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VariableTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchImport:
    boto3_raw_data: "type_defs.BatchImportTypeDef" = dataclasses.field()

    jobId = field("jobId")
    status = field("status")
    failureReason = field("failureReason")
    startTime = field("startTime")
    completionTime = field("completionTime")
    inputPath = field("inputPath")
    outputPath = field("outputPath")
    eventTypeName = field("eventTypeName")
    iamRoleArn = field("iamRoleArn")
    arn = field("arn")
    processedRecordsCount = field("processedRecordsCount")
    failedRecordsCount = field("failedRecordsCount")
    totalRecordsCount = field("totalRecordsCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchImportTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BatchImportTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPrediction:
    boto3_raw_data: "type_defs.BatchPredictionTypeDef" = dataclasses.field()

    jobId = field("jobId")
    status = field("status")
    failureReason = field("failureReason")
    startTime = field("startTime")
    completionTime = field("completionTime")
    lastHeartbeatTime = field("lastHeartbeatTime")
    inputPath = field("inputPath")
    outputPath = field("outputPath")
    eventTypeName = field("eventTypeName")
    detectorName = field("detectorName")
    detectorVersion = field("detectorVersion")
    iamRoleArn = field("iamRoleArn")
    arn = field("arn")
    processedRecordsCount = field("processedRecordsCount")
    totalRecordsCount = field("totalRecordsCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchPredictionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BatchPredictionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelBatchImportJobRequest:
    boto3_raw_data: "type_defs.CancelBatchImportJobRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelBatchImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelBatchImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelBatchPredictionJobRequest:
    boto3_raw_data: "type_defs.CancelBatchPredictionJobRequestTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelBatchPredictionJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelBatchPredictionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelVersion:
    boto3_raw_data: "type_defs.ModelVersionTypeDef" = dataclasses.field()

    modelId = field("modelId")
    modelType = field("modelType")
    modelVersionNumber = field("modelVersionNumber")
    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ModelVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ModelVersionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Rule:
    boto3_raw_data: "type_defs.RuleTypeDef" = dataclasses.field()

    detectorId = field("detectorId")
    ruleId = field("ruleId")
    ruleVersion = field("ruleVersion")

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
class ExternalEventsDetail:
    boto3_raw_data: "type_defs.ExternalEventsDetailTypeDef" = dataclasses.field()

    dataLocation = field("dataLocation")
    dataAccessRoleArn = field("dataAccessRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExternalEventsDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExternalEventsDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldValidationMessage:
    boto3_raw_data: "type_defs.FieldValidationMessageTypeDef" = dataclasses.field()

    fieldName = field("fieldName")
    identifier = field("identifier")
    title = field("title")
    content = field("content")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FieldValidationMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldValidationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileValidationMessage:
    boto3_raw_data: "type_defs.FileValidationMessageTypeDef" = dataclasses.field()

    title = field("title")
    content = field("content")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileValidationMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileValidationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBatchImportJobRequest:
    boto3_raw_data: "type_defs.DeleteBatchImportJobRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBatchImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBatchImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBatchPredictionJobRequest:
    boto3_raw_data: "type_defs.DeleteBatchPredictionJobRequestTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteBatchPredictionJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBatchPredictionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDetectorRequest:
    boto3_raw_data: "type_defs.DeleteDetectorRequestTypeDef" = dataclasses.field()

    detectorId = field("detectorId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDetectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDetectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDetectorVersionRequest:
    boto3_raw_data: "type_defs.DeleteDetectorVersionRequestTypeDef" = (
        dataclasses.field()
    )

    detectorId = field("detectorId")
    detectorVersionId = field("detectorVersionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDetectorVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDetectorVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEntityTypeRequest:
    boto3_raw_data: "type_defs.DeleteEntityTypeRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEntityTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEntityTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventRequest:
    boto3_raw_data: "type_defs.DeleteEventRequestTypeDef" = dataclasses.field()

    eventId = field("eventId")
    eventTypeName = field("eventTypeName")
    deleteAuditHistory = field("deleteAuditHistory")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEventRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventTypeRequest:
    boto3_raw_data: "type_defs.DeleteEventTypeRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEventTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventsByEventTypeRequest:
    boto3_raw_data: "type_defs.DeleteEventsByEventTypeRequestTypeDef" = (
        dataclasses.field()
    )

    eventTypeName = field("eventTypeName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteEventsByEventTypeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventsByEventTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteExternalModelRequest:
    boto3_raw_data: "type_defs.DeleteExternalModelRequestTypeDef" = dataclasses.field()

    modelEndpoint = field("modelEndpoint")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteExternalModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteExternalModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLabelRequest:
    boto3_raw_data: "type_defs.DeleteLabelRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLabelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLabelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteListRequest:
    boto3_raw_data: "type_defs.DeleteListRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteListRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteModelRequest:
    boto3_raw_data: "type_defs.DeleteModelRequestTypeDef" = dataclasses.field()

    modelId = field("modelId")
    modelType = field("modelType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteModelVersionRequest:
    boto3_raw_data: "type_defs.DeleteModelVersionRequestTypeDef" = dataclasses.field()

    modelId = field("modelId")
    modelType = field("modelType")
    modelVersionNumber = field("modelVersionNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteModelVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteModelVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOutcomeRequest:
    boto3_raw_data: "type_defs.DeleteOutcomeRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteOutcomeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOutcomeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVariableRequest:
    boto3_raw_data: "type_defs.DeleteVariableRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVariableRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVariableRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDetectorRequest:
    boto3_raw_data: "type_defs.DescribeDetectorRequestTypeDef" = dataclasses.field()

    detectorId = field("detectorId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDetectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDetectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectorVersionSummary:
    boto3_raw_data: "type_defs.DetectorVersionSummaryTypeDef" = dataclasses.field()

    detectorVersionId = field("detectorVersionId")
    status = field("status")
    description = field("description")
    lastUpdatedTime = field("lastUpdatedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectorVersionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectorVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeModelVersionsRequest:
    boto3_raw_data: "type_defs.DescribeModelVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    modelId = field("modelId")
    modelVersionNumber = field("modelVersionNumber")
    modelType = field("modelType")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeModelVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeModelVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Detector:
    boto3_raw_data: "type_defs.DetectorTypeDef" = dataclasses.field()

    detectorId = field("detectorId")
    description = field("description")
    eventTypeName = field("eventTypeName")
    lastUpdatedTime = field("lastUpdatedTime")
    createdTime = field("createdTime")
    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DetectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DetectorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Entity:
    boto3_raw_data: "type_defs.EntityTypeDef" = dataclasses.field()

    entityType = field("entityType")
    entityId = field("entityId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityType:
    boto3_raw_data: "type_defs.EntityTypeTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    lastUpdatedTime = field("lastUpdatedTime")
    createdTime = field("createdTime")
    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntityTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntityTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluatedExternalModel:
    boto3_raw_data: "type_defs.EvaluatedExternalModelTypeDef" = dataclasses.field()

    modelEndpoint = field("modelEndpoint")
    useEventVariables = field("useEventVariables")
    inputVariables = field("inputVariables")
    outputVariables = field("outputVariables")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluatedExternalModelTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluatedExternalModelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluatedRule:
    boto3_raw_data: "type_defs.EvaluatedRuleTypeDef" = dataclasses.field()

    ruleId = field("ruleId")
    ruleVersion = field("ruleVersion")
    expression = field("expression")
    expressionWithValues = field("expressionWithValues")
    outcomes = field("outcomes")
    evaluated = field("evaluated")
    matched = field("matched")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluatedRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EvaluatedRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventOrchestration:
    boto3_raw_data: "type_defs.EventOrchestrationTypeDef" = dataclasses.field()

    eventBridgeEnabled = field("eventBridgeEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventOrchestrationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventOrchestrationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventPredictionSummary:
    boto3_raw_data: "type_defs.EventPredictionSummaryTypeDef" = dataclasses.field()

    eventId = field("eventId")
    eventTypeName = field("eventTypeName")
    eventTimestamp = field("eventTimestamp")
    predictionTimestamp = field("predictionTimestamp")
    detectorId = field("detectorId")
    detectorVersionId = field("detectorVersionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventPredictionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventPredictionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngestedEventStatistics:
    boto3_raw_data: "type_defs.IngestedEventStatisticsTypeDef" = dataclasses.field()

    numberOfEvents = field("numberOfEvents")
    eventDataSizeInBytes = field("eventDataSizeInBytes")
    leastRecentEvent = field("leastRecentEvent")
    mostRecentEvent = field("mostRecentEvent")
    lastUpdatedTime = field("lastUpdatedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngestedEventStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngestedEventStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventVariableSummary:
    boto3_raw_data: "type_defs.EventVariableSummaryTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")
    source = field("source")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventVariableSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventVariableSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalModelSummary:
    boto3_raw_data: "type_defs.ExternalModelSummaryTypeDef" = dataclasses.field()

    modelEndpoint = field("modelEndpoint")
    modelSource = field("modelSource")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExternalModelSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExternalModelSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelInputConfiguration:
    boto3_raw_data: "type_defs.ModelInputConfigurationTypeDef" = dataclasses.field()

    useEventVariables = field("useEventVariables")
    eventTypeName = field("eventTypeName")
    format = field("format")
    jsonInputTemplate = field("jsonInputTemplate")
    csvInputTemplate = field("csvInputTemplate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModelInputConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelInputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelOutputConfigurationOutput:
    boto3_raw_data: "type_defs.ModelOutputConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    format = field("format")
    jsonKeyToVariableMap = field("jsonKeyToVariableMap")
    csvIndexToVariableMap = field("csvIndexToVariableMap")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModelOutputConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelOutputConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterCondition:
    boto3_raw_data: "type_defs.FilterConditionTypeDef" = dataclasses.field()

    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBatchImportJobsRequest:
    boto3_raw_data: "type_defs.GetBatchImportJobsRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBatchImportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBatchImportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBatchPredictionJobsRequest:
    boto3_raw_data: "type_defs.GetBatchPredictionJobsRequestTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetBatchPredictionJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBatchPredictionJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeleteEventsByEventTypeStatusRequest:
    boto3_raw_data: "type_defs.GetDeleteEventsByEventTypeStatusRequestTypeDef" = (
        dataclasses.field()
    )

    eventTypeName = field("eventTypeName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDeleteEventsByEventTypeStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeleteEventsByEventTypeStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDetectorVersionRequest:
    boto3_raw_data: "type_defs.GetDetectorVersionRequestTypeDef" = dataclasses.field()

    detectorId = field("detectorId")
    detectorVersionId = field("detectorVersionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDetectorVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDetectorVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDetectorsRequest:
    boto3_raw_data: "type_defs.GetDetectorsRequestTypeDef" = dataclasses.field()

    detectorId = field("detectorId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDetectorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDetectorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEntityTypesRequest:
    boto3_raw_data: "type_defs.GetEntityTypesRequestTypeDef" = dataclasses.field()

    name = field("name")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEntityTypesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEntityTypesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventPredictionMetadataRequest:
    boto3_raw_data: "type_defs.GetEventPredictionMetadataRequestTypeDef" = (
        dataclasses.field()
    )

    eventId = field("eventId")
    eventTypeName = field("eventTypeName")
    detectorId = field("detectorId")
    detectorVersionId = field("detectorVersionId")
    predictionTimestamp = field("predictionTimestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEventPredictionMetadataRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventPredictionMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleResult:
    boto3_raw_data: "type_defs.RuleResultTypeDef" = dataclasses.field()

    ruleId = field("ruleId")
    outcomes = field("outcomes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleResultTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventRequest:
    boto3_raw_data: "type_defs.GetEventRequestTypeDef" = dataclasses.field()

    eventId = field("eventId")
    eventTypeName = field("eventTypeName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetEventRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetEventRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventTypesRequest:
    boto3_raw_data: "type_defs.GetEventTypesRequestTypeDef" = dataclasses.field()

    name = field("name")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEventTypesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventTypesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExternalModelsRequest:
    boto3_raw_data: "type_defs.GetExternalModelsRequestTypeDef" = dataclasses.field()

    modelEndpoint = field("modelEndpoint")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExternalModelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExternalModelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KMSKey:
    boto3_raw_data: "type_defs.KMSKeyTypeDef" = dataclasses.field()

    kmsEncryptionKeyArn = field("kmsEncryptionKeyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KMSKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KMSKeyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLabelsRequest:
    boto3_raw_data: "type_defs.GetLabelsRequestTypeDef" = dataclasses.field()

    name = field("name")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetLabelsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLabelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Label:
    boto3_raw_data: "type_defs.LabelTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    lastUpdatedTime = field("lastUpdatedTime")
    createdTime = field("createdTime")
    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LabelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LabelTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetListElementsRequest:
    boto3_raw_data: "type_defs.GetListElementsRequestTypeDef" = dataclasses.field()

    name = field("name")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetListElementsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetListElementsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetListsMetadataRequest:
    boto3_raw_data: "type_defs.GetListsMetadataRequestTypeDef" = dataclasses.field()

    name = field("name")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetListsMetadataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetListsMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelVersionRequest:
    boto3_raw_data: "type_defs.GetModelVersionRequestTypeDef" = dataclasses.field()

    modelId = field("modelId")
    modelType = field("modelType")
    modelVersionNumber = field("modelVersionNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetModelVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetModelVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelsRequest:
    boto3_raw_data: "type_defs.GetModelsRequestTypeDef" = dataclasses.field()

    modelId = field("modelId")
    modelType = field("modelType")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetModelsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetModelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Model:
    boto3_raw_data: "type_defs.ModelTypeDef" = dataclasses.field()

    modelId = field("modelId")
    modelType = field("modelType")
    description = field("description")
    eventTypeName = field("eventTypeName")
    createdTime = field("createdTime")
    lastUpdatedTime = field("lastUpdatedTime")
    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ModelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ModelTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOutcomesRequest:
    boto3_raw_data: "type_defs.GetOutcomesRequestTypeDef" = dataclasses.field()

    name = field("name")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOutcomesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOutcomesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Outcome:
    boto3_raw_data: "type_defs.OutcomeTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    lastUpdatedTime = field("lastUpdatedTime")
    createdTime = field("createdTime")
    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutcomeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutcomeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRulesRequest:
    boto3_raw_data: "type_defs.GetRulesRequestTypeDef" = dataclasses.field()

    detectorId = field("detectorId")
    ruleId = field("ruleId")
    ruleVersion = field("ruleVersion")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRulesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetRulesRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleDetail:
    boto3_raw_data: "type_defs.RuleDetailTypeDef" = dataclasses.field()

    ruleId = field("ruleId")
    description = field("description")
    detectorId = field("detectorId")
    ruleVersion = field("ruleVersion")
    expression = field("expression")
    language = field("language")
    outcomes = field("outcomes")
    lastUpdatedTime = field("lastUpdatedTime")
    createdTime = field("createdTime")
    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleDetailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVariablesRequest:
    boto3_raw_data: "type_defs.GetVariablesRequestTypeDef" = dataclasses.field()

    name = field("name")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVariablesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVariablesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngestedEventsTimeWindow:
    boto3_raw_data: "type_defs.IngestedEventsTimeWindowTypeDef" = dataclasses.field()

    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngestedEventsTimeWindowTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngestedEventsTimeWindowTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LabelSchemaOutput:
    boto3_raw_data: "type_defs.LabelSchemaOutputTypeDef" = dataclasses.field()

    labelMapper = field("labelMapper")
    unlabeledEventsTreatment = field("unlabeledEventsTreatment")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LabelSchemaOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LabelSchemaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LabelSchema:
    boto3_raw_data: "type_defs.LabelSchemaTypeDef" = dataclasses.field()

    labelMapper = field("labelMapper")
    unlabeledEventsTreatment = field("unlabeledEventsTreatment")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LabelSchemaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LabelSchemaTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictionTimeRange:
    boto3_raw_data: "type_defs.PredictionTimeRangeTypeDef" = dataclasses.field()

    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PredictionTimeRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictionTimeRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    resourceARN = field("resourceARN")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogOddsMetric:
    boto3_raw_data: "type_defs.LogOddsMetricTypeDef" = dataclasses.field()

    variableName = field("variableName")
    variableType = field("variableType")
    variableImportance = field("variableImportance")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogOddsMetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogOddsMetricTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDataPoint:
    boto3_raw_data: "type_defs.MetricDataPointTypeDef" = dataclasses.field()

    fpr = field("fpr")
    precision = field("precision")
    tpr = field("tpr")
    threshold = field("threshold")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricDataPointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricDataPointTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelOutputConfiguration:
    boto3_raw_data: "type_defs.ModelOutputConfigurationTypeDef" = dataclasses.field()

    format = field("format")
    jsonKeyToVariableMap = field("jsonKeyToVariableMap")
    csvIndexToVariableMap = field("csvIndexToVariableMap")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModelOutputConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelOutputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OFIMetricDataPoint:
    boto3_raw_data: "type_defs.OFIMetricDataPointTypeDef" = dataclasses.field()

    fpr = field("fpr")
    precision = field("precision")
    tpr = field("tpr")
    threshold = field("threshold")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OFIMetricDataPointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OFIMetricDataPointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UncertaintyRange:
    boto3_raw_data: "type_defs.UncertaintyRangeTypeDef" = dataclasses.field()

    lowerBoundValue = field("lowerBoundValue")
    upperBoundValue = field("upperBoundValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UncertaintyRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UncertaintyRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VariableImpactExplanation:
    boto3_raw_data: "type_defs.VariableImpactExplanationTypeDef" = dataclasses.field()

    eventVariableName = field("eventVariableName")
    relativeImpact = field("relativeImpact")
    logOddsImpact = field("logOddsImpact")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VariableImpactExplanationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VariableImpactExplanationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutKMSEncryptionKeyRequest:
    boto3_raw_data: "type_defs.PutKMSEncryptionKeyRequestTypeDef" = dataclasses.field()

    kmsEncryptionKeyArn = field("kmsEncryptionKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutKMSEncryptionKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutKMSEncryptionKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TFIMetricDataPoint:
    boto3_raw_data: "type_defs.TFIMetricDataPointTypeDef" = dataclasses.field()

    fpr = field("fpr")
    precision = field("precision")
    tpr = field("tpr")
    threshold = field("threshold")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TFIMetricDataPointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TFIMetricDataPointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    resourceARN = field("resourceARN")
    tagKeys = field("tagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDetectorVersionMetadataRequest:
    boto3_raw_data: "type_defs.UpdateDetectorVersionMetadataRequestTypeDef" = (
        dataclasses.field()
    )

    detectorId = field("detectorId")
    detectorVersionId = field("detectorVersionId")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDetectorVersionMetadataRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDetectorVersionMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDetectorVersionStatusRequest:
    boto3_raw_data: "type_defs.UpdateDetectorVersionStatusRequestTypeDef" = (
        dataclasses.field()
    )

    detectorId = field("detectorId")
    detectorVersionId = field("detectorVersionId")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDetectorVersionStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDetectorVersionStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEventLabelRequest:
    boto3_raw_data: "type_defs.UpdateEventLabelRequestTypeDef" = dataclasses.field()

    eventId = field("eventId")
    eventTypeName = field("eventTypeName")
    assignedLabel = field("assignedLabel")
    labelTimestamp = field("labelTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEventLabelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEventLabelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateListRequest:
    boto3_raw_data: "type_defs.UpdateListRequestTypeDef" = dataclasses.field()

    name = field("name")
    elements = field("elements")
    description = field("description")
    updateMode = field("updateMode")
    variableType = field("variableType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateListRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateModelRequest:
    boto3_raw_data: "type_defs.UpdateModelRequestTypeDef" = dataclasses.field()

    modelId = field("modelId")
    modelType = field("modelType")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateModelVersionStatusRequest:
    boto3_raw_data: "type_defs.UpdateModelVersionStatusRequestTypeDef" = (
        dataclasses.field()
    )

    modelId = field("modelId")
    modelType = field("modelType")
    modelVersionNumber = field("modelVersionNumber")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateModelVersionStatusRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateModelVersionStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVariableRequest:
    boto3_raw_data: "type_defs.UpdateVariableRequestTypeDef" = dataclasses.field()

    name = field("name")
    defaultValue = field("defaultValue")
    description = field("description")
    variableType = field("variableType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVariableRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVariableRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ATITrainingMetricsValue:
    boto3_raw_data: "type_defs.ATITrainingMetricsValueTypeDef" = dataclasses.field()

    @cached_property
    def metricDataPoints(self):  # pragma: no cover
        return ATIMetricDataPoint.make_many(self.boto3_raw_data["metricDataPoints"])

    @cached_property
    def modelPerformance(self):  # pragma: no cover
        return ATIModelPerformance.make_one(self.boto3_raw_data["modelPerformance"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ATITrainingMetricsValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ATITrainingMetricsValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregatedVariablesImportanceMetrics:
    boto3_raw_data: "type_defs.AggregatedVariablesImportanceMetricsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def logOddsMetrics(self):  # pragma: no cover
        return AggregatedLogOddsMetric.make_many(self.boto3_raw_data["logOddsMetrics"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AggregatedVariablesImportanceMetricsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregatedVariablesImportanceMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBatchImportJobRequest:
    boto3_raw_data: "type_defs.CreateBatchImportJobRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")
    inputPath = field("inputPath")
    outputPath = field("outputPath")
    eventTypeName = field("eventTypeName")
    iamRoleArn = field("iamRoleArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBatchImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBatchImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBatchPredictionJobRequest:
    boto3_raw_data: "type_defs.CreateBatchPredictionJobRequestTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")
    inputPath = field("inputPath")
    outputPath = field("outputPath")
    eventTypeName = field("eventTypeName")
    detectorName = field("detectorName")
    iamRoleArn = field("iamRoleArn")
    detectorVersion = field("detectorVersion")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateBatchPredictionJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBatchPredictionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateListRequest:
    boto3_raw_data: "type_defs.CreateListRequestTypeDef" = dataclasses.field()

    name = field("name")
    elements = field("elements")
    variableType = field("variableType")
    description = field("description")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateListRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateModelRequest:
    boto3_raw_data: "type_defs.CreateModelRequestTypeDef" = dataclasses.field()

    modelId = field("modelId")
    modelType = field("modelType")
    eventTypeName = field("eventTypeName")
    description = field("description")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRuleRequest:
    boto3_raw_data: "type_defs.CreateRuleRequestTypeDef" = dataclasses.field()

    ruleId = field("ruleId")
    detectorId = field("detectorId")
    expression = field("expression")
    language = field("language")
    outcomes = field("outcomes")
    description = field("description")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateRuleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVariableRequest:
    boto3_raw_data: "type_defs.CreateVariableRequestTypeDef" = dataclasses.field()

    name = field("name")
    dataType = field("dataType")
    dataSource = field("dataSource")
    defaultValue = field("defaultValue")
    description = field("description")
    variableType = field("variableType")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVariableRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVariableRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDetectorRequest:
    boto3_raw_data: "type_defs.PutDetectorRequestTypeDef" = dataclasses.field()

    detectorId = field("detectorId")
    eventTypeName = field("eventTypeName")
    description = field("description")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutDetectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDetectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEntityTypeRequest:
    boto3_raw_data: "type_defs.PutEntityTypeRequestTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutEntityTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEntityTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutLabelRequest:
    boto3_raw_data: "type_defs.PutLabelRequestTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutLabelRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutLabelRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutOutcomeRequest:
    boto3_raw_data: "type_defs.PutOutcomeRequestTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutOutcomeRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutOutcomeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    resourceARN = field("resourceARN")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateVariableRequest:
    boto3_raw_data: "type_defs.BatchCreateVariableRequestTypeDef" = dataclasses.field()

    @cached_property
    def variableEntries(self):  # pragma: no cover
        return VariableEntry.make_many(self.boto3_raw_data["variableEntries"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchCreateVariableRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateVariableRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateVariableResult:
    boto3_raw_data: "type_defs.BatchCreateVariableResultTypeDef" = dataclasses.field()

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchCreateVariableError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchCreateVariableResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateVariableResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDetectorVersionResult:
    boto3_raw_data: "type_defs.CreateDetectorVersionResultTypeDef" = dataclasses.field()

    detectorId = field("detectorId")
    detectorVersionId = field("detectorVersionId")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDetectorVersionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDetectorVersionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateModelVersionResult:
    boto3_raw_data: "type_defs.CreateModelVersionResultTypeDef" = dataclasses.field()

    modelId = field("modelId")
    modelType = field("modelType")
    modelVersionNumber = field("modelVersionNumber")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateModelVersionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateModelVersionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventsByEventTypeResult:
    boto3_raw_data: "type_defs.DeleteEventsByEventTypeResultTypeDef" = (
        dataclasses.field()
    )

    eventTypeName = field("eventTypeName")
    eventsDeletionStatus = field("eventsDeletionStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteEventsByEventTypeResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventsByEventTypeResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeleteEventsByEventTypeStatusResult:
    boto3_raw_data: "type_defs.GetDeleteEventsByEventTypeStatusResultTypeDef" = (
        dataclasses.field()
    )

    eventTypeName = field("eventTypeName")
    eventsDeletionStatus = field("eventsDeletionStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDeleteEventsByEventTypeStatusResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeleteEventsByEventTypeStatusResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetListElementsResult:
    boto3_raw_data: "type_defs.GetListElementsResultTypeDef" = dataclasses.field()

    elements = field("elements")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetListElementsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetListElementsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetListsMetadataResult:
    boto3_raw_data: "type_defs.GetListsMetadataResultTypeDef" = dataclasses.field()

    @cached_property
    def lists(self):  # pragma: no cover
        return AllowDenyList.make_many(self.boto3_raw_data["lists"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetListsMetadataResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetListsMetadataResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResult:
    boto3_raw_data: "type_defs.ListTagsForResourceResultTypeDef" = dataclasses.field()

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateModelVersionResult:
    boto3_raw_data: "type_defs.UpdateModelVersionResultTypeDef" = dataclasses.field()

    modelId = field("modelId")
    modelType = field("modelType")
    modelVersionNumber = field("modelVersionNumber")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateModelVersionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateModelVersionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetVariableResult:
    boto3_raw_data: "type_defs.BatchGetVariableResultTypeDef" = dataclasses.field()

    @cached_property
    def variables(self):  # pragma: no cover
        return Variable.make_many(self.boto3_raw_data["variables"])

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchGetVariableError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetVariableResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetVariableResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVariablesResult:
    boto3_raw_data: "type_defs.GetVariablesResultTypeDef" = dataclasses.field()

    @cached_property
    def variables(self):  # pragma: no cover
        return Variable.make_many(self.boto3_raw_data["variables"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVariablesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVariablesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBatchImportJobsResult:
    boto3_raw_data: "type_defs.GetBatchImportJobsResultTypeDef" = dataclasses.field()

    @cached_property
    def batchImports(self):  # pragma: no cover
        return BatchImport.make_many(self.boto3_raw_data["batchImports"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBatchImportJobsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBatchImportJobsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBatchPredictionJobsResult:
    boto3_raw_data: "type_defs.GetBatchPredictionJobsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def batchPredictions(self):  # pragma: no cover
        return BatchPrediction.make_many(self.boto3_raw_data["batchPredictions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBatchPredictionJobsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBatchPredictionJobsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelEndpointDataBlob:
    boto3_raw_data: "type_defs.ModelEndpointDataBlobTypeDef" = dataclasses.field()

    byteBuffer = field("byteBuffer")
    contentType = field("contentType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModelEndpointDataBlobTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelEndpointDataBlobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelScores:
    boto3_raw_data: "type_defs.ModelScoresTypeDef" = dataclasses.field()

    @cached_property
    def modelVersion(self):  # pragma: no cover
        return ModelVersion.make_one(self.boto3_raw_data["modelVersion"])

    scores = field("scores")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ModelScoresTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ModelScoresTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDetectorVersionRequest:
    boto3_raw_data: "type_defs.CreateDetectorVersionRequestTypeDef" = (
        dataclasses.field()
    )

    detectorId = field("detectorId")

    @cached_property
    def rules(self):  # pragma: no cover
        return Rule.make_many(self.boto3_raw_data["rules"])

    description = field("description")
    externalModelEndpoints = field("externalModelEndpoints")

    @cached_property
    def modelVersions(self):  # pragma: no cover
        return ModelVersion.make_many(self.boto3_raw_data["modelVersions"])

    ruleExecutionMode = field("ruleExecutionMode")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDetectorVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDetectorVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRuleResult:
    boto3_raw_data: "type_defs.CreateRuleResultTypeDef" = dataclasses.field()

    @cached_property
    def rule(self):  # pragma: no cover
        return Rule.make_one(self.boto3_raw_data["rule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateRuleResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRuleResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRuleRequest:
    boto3_raw_data: "type_defs.DeleteRuleRequestTypeDef" = dataclasses.field()

    @cached_property
    def rule(self):  # pragma: no cover
        return Rule.make_one(self.boto3_raw_data["rule"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteRuleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDetectorVersionResult:
    boto3_raw_data: "type_defs.GetDetectorVersionResultTypeDef" = dataclasses.field()

    detectorId = field("detectorId")
    detectorVersionId = field("detectorVersionId")
    description = field("description")
    externalModelEndpoints = field("externalModelEndpoints")

    @cached_property
    def modelVersions(self):  # pragma: no cover
        return ModelVersion.make_many(self.boto3_raw_data["modelVersions"])

    @cached_property
    def rules(self):  # pragma: no cover
        return Rule.make_many(self.boto3_raw_data["rules"])

    status = field("status")
    lastUpdatedTime = field("lastUpdatedTime")
    createdTime = field("createdTime")
    ruleExecutionMode = field("ruleExecutionMode")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDetectorVersionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDetectorVersionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDetectorVersionRequest:
    boto3_raw_data: "type_defs.UpdateDetectorVersionRequestTypeDef" = (
        dataclasses.field()
    )

    detectorId = field("detectorId")
    detectorVersionId = field("detectorVersionId")
    externalModelEndpoints = field("externalModelEndpoints")

    @cached_property
    def rules(self):  # pragma: no cover
        return Rule.make_many(self.boto3_raw_data["rules"])

    description = field("description")

    @cached_property
    def modelVersions(self):  # pragma: no cover
        return ModelVersion.make_many(self.boto3_raw_data["modelVersions"])

    ruleExecutionMode = field("ruleExecutionMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDetectorVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDetectorVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRuleMetadataRequest:
    boto3_raw_data: "type_defs.UpdateRuleMetadataRequestTypeDef" = dataclasses.field()

    @cached_property
    def rule(self):  # pragma: no cover
        return Rule.make_one(self.boto3_raw_data["rule"])

    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRuleMetadataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRuleMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRuleVersionRequest:
    boto3_raw_data: "type_defs.UpdateRuleVersionRequestTypeDef" = dataclasses.field()

    @cached_property
    def rule(self):  # pragma: no cover
        return Rule.make_one(self.boto3_raw_data["rule"])

    expression = field("expression")
    language = field("language")
    outcomes = field("outcomes")
    description = field("description")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRuleVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRuleVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRuleVersionResult:
    boto3_raw_data: "type_defs.UpdateRuleVersionResultTypeDef" = dataclasses.field()

    @cached_property
    def rule(self):  # pragma: no cover
        return Rule.make_one(self.boto3_raw_data["rule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRuleVersionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRuleVersionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataValidationMetrics:
    boto3_raw_data: "type_defs.DataValidationMetricsTypeDef" = dataclasses.field()

    @cached_property
    def fileLevelMessages(self):  # pragma: no cover
        return FileValidationMessage.make_many(self.boto3_raw_data["fileLevelMessages"])

    @cached_property
    def fieldLevelMessages(self):  # pragma: no cover
        return FieldValidationMessage.make_many(
            self.boto3_raw_data["fieldLevelMessages"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataValidationMetricsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataValidationMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDetectorResult:
    boto3_raw_data: "type_defs.DescribeDetectorResultTypeDef" = dataclasses.field()

    detectorId = field("detectorId")

    @cached_property
    def detectorVersionSummaries(self):  # pragma: no cover
        return DetectorVersionSummary.make_many(
            self.boto3_raw_data["detectorVersionSummaries"]
        )

    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDetectorResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDetectorResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDetectorsResult:
    boto3_raw_data: "type_defs.GetDetectorsResultTypeDef" = dataclasses.field()

    @cached_property
    def detectors(self):  # pragma: no cover
        return Detector.make_many(self.boto3_raw_data["detectors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDetectorsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDetectorsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Event:
    boto3_raw_data: "type_defs.EventTypeDef" = dataclasses.field()

    eventId = field("eventId")
    eventTypeName = field("eventTypeName")
    eventTimestamp = field("eventTimestamp")
    eventVariables = field("eventVariables")
    currentLabel = field("currentLabel")
    labelTimestamp = field("labelTimestamp")

    @cached_property
    def entities(self):  # pragma: no cover
        return Entity.make_many(self.boto3_raw_data["entities"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendEventRequest:
    boto3_raw_data: "type_defs.SendEventRequestTypeDef" = dataclasses.field()

    eventId = field("eventId")
    eventTypeName = field("eventTypeName")
    eventTimestamp = field("eventTimestamp")
    eventVariables = field("eventVariables")

    @cached_property
    def entities(self):  # pragma: no cover
        return Entity.make_many(self.boto3_raw_data["entities"])

    assignedLabel = field("assignedLabel")
    labelTimestamp = field("labelTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SendEventRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendEventRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEntityTypesResult:
    boto3_raw_data: "type_defs.GetEntityTypesResultTypeDef" = dataclasses.field()

    @cached_property
    def entityTypes(self):  # pragma: no cover
        return EntityType.make_many(self.boto3_raw_data["entityTypes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEntityTypesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEntityTypesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEventTypeRequest:
    boto3_raw_data: "type_defs.PutEventTypeRequestTypeDef" = dataclasses.field()

    name = field("name")
    eventVariables = field("eventVariables")
    entityTypes = field("entityTypes")
    description = field("description")
    labels = field("labels")
    eventIngestion = field("eventIngestion")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def eventOrchestration(self):  # pragma: no cover
        return EventOrchestration.make_one(self.boto3_raw_data["eventOrchestration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutEventTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEventTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventPredictionsResult:
    boto3_raw_data: "type_defs.ListEventPredictionsResultTypeDef" = dataclasses.field()

    @cached_property
    def eventPredictionSummaries(self):  # pragma: no cover
        return EventPredictionSummary.make_many(
            self.boto3_raw_data["eventPredictionSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEventPredictionsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventPredictionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventType:
    boto3_raw_data: "type_defs.EventTypeTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    eventVariables = field("eventVariables")
    labels = field("labels")
    entityTypes = field("entityTypes")
    eventIngestion = field("eventIngestion")

    @cached_property
    def ingestedEventStatistics(self):  # pragma: no cover
        return IngestedEventStatistics.make_one(
            self.boto3_raw_data["ingestedEventStatistics"]
        )

    lastUpdatedTime = field("lastUpdatedTime")
    createdTime = field("createdTime")
    arn = field("arn")

    @cached_property
    def eventOrchestration(self):  # pragma: no cover
        return EventOrchestration.make_one(self.boto3_raw_data["eventOrchestration"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalModelOutputs:
    boto3_raw_data: "type_defs.ExternalModelOutputsTypeDef" = dataclasses.field()

    @cached_property
    def externalModel(self):  # pragma: no cover
        return ExternalModelSummary.make_one(self.boto3_raw_data["externalModel"])

    outputs = field("outputs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExternalModelOutputsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExternalModelOutputsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalModel:
    boto3_raw_data: "type_defs.ExternalModelTypeDef" = dataclasses.field()

    modelEndpoint = field("modelEndpoint")
    modelSource = field("modelSource")
    invokeModelEndpointRoleArn = field("invokeModelEndpointRoleArn")

    @cached_property
    def inputConfiguration(self):  # pragma: no cover
        return ModelInputConfiguration.make_one(
            self.boto3_raw_data["inputConfiguration"]
        )

    @cached_property
    def outputConfiguration(self):  # pragma: no cover
        return ModelOutputConfigurationOutput.make_one(
            self.boto3_raw_data["outputConfiguration"]
        )

    modelEndpointStatus = field("modelEndpointStatus")
    lastUpdatedTime = field("lastUpdatedTime")
    createdTime = field("createdTime")
    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExternalModelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExternalModelTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKMSEncryptionKeyResult:
    boto3_raw_data: "type_defs.GetKMSEncryptionKeyResultTypeDef" = dataclasses.field()

    @cached_property
    def kmsKey(self):  # pragma: no cover
        return KMSKey.make_one(self.boto3_raw_data["kmsKey"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKMSEncryptionKeyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKMSEncryptionKeyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLabelsResult:
    boto3_raw_data: "type_defs.GetLabelsResultTypeDef" = dataclasses.field()

    @cached_property
    def labels(self):  # pragma: no cover
        return Label.make_many(self.boto3_raw_data["labels"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetLabelsResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetLabelsResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelsResult:
    boto3_raw_data: "type_defs.GetModelsResultTypeDef" = dataclasses.field()

    @cached_property
    def models(self):  # pragma: no cover
        return Model.make_many(self.boto3_raw_data["models"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetModelsResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetModelsResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOutcomesResult:
    boto3_raw_data: "type_defs.GetOutcomesResultTypeDef" = dataclasses.field()

    @cached_property
    def outcomes(self):  # pragma: no cover
        return Outcome.make_many(self.boto3_raw_data["outcomes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetOutcomesResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOutcomesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRulesResult:
    boto3_raw_data: "type_defs.GetRulesResultTypeDef" = dataclasses.field()

    @cached_property
    def ruleDetails(self):  # pragma: no cover
        return RuleDetail.make_many(self.boto3_raw_data["ruleDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRulesResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetRulesResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngestedEventsDetail:
    boto3_raw_data: "type_defs.IngestedEventsDetailTypeDef" = dataclasses.field()

    @cached_property
    def ingestedEventsTimeWindow(self):  # pragma: no cover
        return IngestedEventsTimeWindow.make_one(
            self.boto3_raw_data["ingestedEventsTimeWindow"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngestedEventsDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngestedEventsDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainingDataSchemaOutput:
    boto3_raw_data: "type_defs.TrainingDataSchemaOutputTypeDef" = dataclasses.field()

    modelVariables = field("modelVariables")

    @cached_property
    def labelSchema(self):  # pragma: no cover
        return LabelSchemaOutput.make_one(self.boto3_raw_data["labelSchema"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrainingDataSchemaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainingDataSchemaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainingDataSchema:
    boto3_raw_data: "type_defs.TrainingDataSchemaTypeDef" = dataclasses.field()

    modelVariables = field("modelVariables")

    @cached_property
    def labelSchema(self):  # pragma: no cover
        return LabelSchema.make_one(self.boto3_raw_data["labelSchema"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrainingDataSchemaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainingDataSchemaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventPredictionsRequest:
    boto3_raw_data: "type_defs.ListEventPredictionsRequestTypeDef" = dataclasses.field()

    @cached_property
    def eventId(self):  # pragma: no cover
        return FilterCondition.make_one(self.boto3_raw_data["eventId"])

    @cached_property
    def eventType(self):  # pragma: no cover
        return FilterCondition.make_one(self.boto3_raw_data["eventType"])

    @cached_property
    def detectorId(self):  # pragma: no cover
        return FilterCondition.make_one(self.boto3_raw_data["detectorId"])

    @cached_property
    def detectorVersionId(self):  # pragma: no cover
        return FilterCondition.make_one(self.boto3_raw_data["detectorVersionId"])

    @cached_property
    def predictionTimeRange(self):  # pragma: no cover
        return PredictionTimeRange.make_one(self.boto3_raw_data["predictionTimeRange"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEventPredictionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventPredictionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VariableImportanceMetrics:
    boto3_raw_data: "type_defs.VariableImportanceMetricsTypeDef" = dataclasses.field()

    @cached_property
    def logOddsMetrics(self):  # pragma: no cover
        return LogOddsMetric.make_many(self.boto3_raw_data["logOddsMetrics"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VariableImportanceMetricsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VariableImportanceMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainingMetrics:
    boto3_raw_data: "type_defs.TrainingMetricsTypeDef" = dataclasses.field()

    auc = field("auc")

    @cached_property
    def metricDataPoints(self):  # pragma: no cover
        return MetricDataPoint.make_many(self.boto3_raw_data["metricDataPoints"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrainingMetricsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TrainingMetricsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OFIModelPerformance:
    boto3_raw_data: "type_defs.OFIModelPerformanceTypeDef" = dataclasses.field()

    auc = field("auc")

    @cached_property
    def uncertaintyRange(self):  # pragma: no cover
        return UncertaintyRange.make_one(self.boto3_raw_data["uncertaintyRange"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OFIModelPerformanceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OFIModelPerformanceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TFIModelPerformance:
    boto3_raw_data: "type_defs.TFIModelPerformanceTypeDef" = dataclasses.field()

    auc = field("auc")

    @cached_property
    def uncertaintyRange(self):  # pragma: no cover
        return UncertaintyRange.make_one(self.boto3_raw_data["uncertaintyRange"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TFIModelPerformanceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TFIModelPerformanceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictionExplanations:
    boto3_raw_data: "type_defs.PredictionExplanationsTypeDef" = dataclasses.field()

    @cached_property
    def variableImpactExplanations(self):  # pragma: no cover
        return VariableImpactExplanation.make_many(
            self.boto3_raw_data["variableImpactExplanations"]
        )

    @cached_property
    def aggregatedVariablesImpactExplanations(self):  # pragma: no cover
        return AggregatedVariablesImpactExplanation.make_many(
            self.boto3_raw_data["aggregatedVariablesImpactExplanations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PredictionExplanationsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictionExplanationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventPredictionRequest:
    boto3_raw_data: "type_defs.GetEventPredictionRequestTypeDef" = dataclasses.field()

    detectorId = field("detectorId")
    eventId = field("eventId")
    eventTypeName = field("eventTypeName")

    @cached_property
    def entities(self):  # pragma: no cover
        return Entity.make_many(self.boto3_raw_data["entities"])

    eventTimestamp = field("eventTimestamp")
    eventVariables = field("eventVariables")
    detectorVersionId = field("detectorVersionId")
    externalModelEndpointDataBlobs = field("externalModelEndpointDataBlobs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEventPredictionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventPredictionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventResult:
    boto3_raw_data: "type_defs.GetEventResultTypeDef" = dataclasses.field()

    @cached_property
    def event(self):  # pragma: no cover
        return Event.make_one(self.boto3_raw_data["event"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetEventResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetEventResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventTypesResult:
    boto3_raw_data: "type_defs.GetEventTypesResultTypeDef" = dataclasses.field()

    @cached_property
    def eventTypes(self):  # pragma: no cover
        return EventType.make_many(self.boto3_raw_data["eventTypes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEventTypesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventTypesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventPredictionResult:
    boto3_raw_data: "type_defs.GetEventPredictionResultTypeDef" = dataclasses.field()

    @cached_property
    def modelScores(self):  # pragma: no cover
        return ModelScores.make_many(self.boto3_raw_data["modelScores"])

    @cached_property
    def ruleResults(self):  # pragma: no cover
        return RuleResult.make_many(self.boto3_raw_data["ruleResults"])

    @cached_property
    def externalModelOutputs(self):  # pragma: no cover
        return ExternalModelOutputs.make_many(
            self.boto3_raw_data["externalModelOutputs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEventPredictionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventPredictionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExternalModelsResult:
    boto3_raw_data: "type_defs.GetExternalModelsResultTypeDef" = dataclasses.field()

    @cached_property
    def externalModels(self):  # pragma: no cover
        return ExternalModel.make_many(self.boto3_raw_data["externalModels"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExternalModelsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExternalModelsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateModelVersionRequest:
    boto3_raw_data: "type_defs.UpdateModelVersionRequestTypeDef" = dataclasses.field()

    modelId = field("modelId")
    modelType = field("modelType")
    majorVersionNumber = field("majorVersionNumber")

    @cached_property
    def externalEventsDetail(self):  # pragma: no cover
        return ExternalEventsDetail.make_one(
            self.boto3_raw_data["externalEventsDetail"]
        )

    @cached_property
    def ingestedEventsDetail(self):  # pragma: no cover
        return IngestedEventsDetail.make_one(
            self.boto3_raw_data["ingestedEventsDetail"]
        )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateModelVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateModelVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelVersionResult:
    boto3_raw_data: "type_defs.GetModelVersionResultTypeDef" = dataclasses.field()

    modelId = field("modelId")
    modelType = field("modelType")
    modelVersionNumber = field("modelVersionNumber")
    trainingDataSource = field("trainingDataSource")

    @cached_property
    def trainingDataSchema(self):  # pragma: no cover
        return TrainingDataSchemaOutput.make_one(
            self.boto3_raw_data["trainingDataSchema"]
        )

    @cached_property
    def externalEventsDetail(self):  # pragma: no cover
        return ExternalEventsDetail.make_one(
            self.boto3_raw_data["externalEventsDetail"]
        )

    @cached_property
    def ingestedEventsDetail(self):  # pragma: no cover
        return IngestedEventsDetail.make_one(
            self.boto3_raw_data["ingestedEventsDetail"]
        )

    status = field("status")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetModelVersionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetModelVersionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainingResult:
    boto3_raw_data: "type_defs.TrainingResultTypeDef" = dataclasses.field()

    @cached_property
    def dataValidationMetrics(self):  # pragma: no cover
        return DataValidationMetrics.make_one(
            self.boto3_raw_data["dataValidationMetrics"]
        )

    @cached_property
    def trainingMetrics(self):  # pragma: no cover
        return TrainingMetrics.make_one(self.boto3_raw_data["trainingMetrics"])

    @cached_property
    def variableImportanceMetrics(self):  # pragma: no cover
        return VariableImportanceMetrics.make_one(
            self.boto3_raw_data["variableImportanceMetrics"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrainingResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TrainingResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutExternalModelRequest:
    boto3_raw_data: "type_defs.PutExternalModelRequestTypeDef" = dataclasses.field()

    modelEndpoint = field("modelEndpoint")
    modelSource = field("modelSource")
    invokeModelEndpointRoleArn = field("invokeModelEndpointRoleArn")

    @cached_property
    def inputConfiguration(self):  # pragma: no cover
        return ModelInputConfiguration.make_one(
            self.boto3_raw_data["inputConfiguration"]
        )

    outputConfiguration = field("outputConfiguration")
    modelEndpointStatus = field("modelEndpointStatus")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutExternalModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutExternalModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OFITrainingMetricsValue:
    boto3_raw_data: "type_defs.OFITrainingMetricsValueTypeDef" = dataclasses.field()

    @cached_property
    def metricDataPoints(self):  # pragma: no cover
        return OFIMetricDataPoint.make_many(self.boto3_raw_data["metricDataPoints"])

    @cached_property
    def modelPerformance(self):  # pragma: no cover
        return OFIModelPerformance.make_one(self.boto3_raw_data["modelPerformance"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OFITrainingMetricsValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OFITrainingMetricsValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TFITrainingMetricsValue:
    boto3_raw_data: "type_defs.TFITrainingMetricsValueTypeDef" = dataclasses.field()

    @cached_property
    def metricDataPoints(self):  # pragma: no cover
        return TFIMetricDataPoint.make_many(self.boto3_raw_data["metricDataPoints"])

    @cached_property
    def modelPerformance(self):  # pragma: no cover
        return TFIModelPerformance.make_one(self.boto3_raw_data["modelPerformance"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TFITrainingMetricsValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TFITrainingMetricsValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelVersionEvaluation:
    boto3_raw_data: "type_defs.ModelVersionEvaluationTypeDef" = dataclasses.field()

    outputVariableName = field("outputVariableName")
    evaluationScore = field("evaluationScore")

    @cached_property
    def predictionExplanations(self):  # pragma: no cover
        return PredictionExplanations.make_one(
            self.boto3_raw_data["predictionExplanations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModelVersionEvaluationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelVersionEvaluationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateModelVersionRequest:
    boto3_raw_data: "type_defs.CreateModelVersionRequestTypeDef" = dataclasses.field()

    modelId = field("modelId")
    modelType = field("modelType")
    trainingDataSource = field("trainingDataSource")
    trainingDataSchema = field("trainingDataSchema")

    @cached_property
    def externalEventsDetail(self):  # pragma: no cover
        return ExternalEventsDetail.make_one(
            self.boto3_raw_data["externalEventsDetail"]
        )

    @cached_property
    def ingestedEventsDetail(self):  # pragma: no cover
        return IngestedEventsDetail.make_one(
            self.boto3_raw_data["ingestedEventsDetail"]
        )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateModelVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateModelVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainingMetricsV2:
    boto3_raw_data: "type_defs.TrainingMetricsV2TypeDef" = dataclasses.field()

    @cached_property
    def ofi(self):  # pragma: no cover
        return OFITrainingMetricsValue.make_one(self.boto3_raw_data["ofi"])

    @cached_property
    def tfi(self):  # pragma: no cover
        return TFITrainingMetricsValue.make_one(self.boto3_raw_data["tfi"])

    @cached_property
    def ati(self):  # pragma: no cover
        return ATITrainingMetricsValue.make_one(self.boto3_raw_data["ati"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrainingMetricsV2TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainingMetricsV2TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluatedModelVersion:
    boto3_raw_data: "type_defs.EvaluatedModelVersionTypeDef" = dataclasses.field()

    modelId = field("modelId")
    modelVersion = field("modelVersion")
    modelType = field("modelType")

    @cached_property
    def evaluations(self):  # pragma: no cover
        return ModelVersionEvaluation.make_many(self.boto3_raw_data["evaluations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluatedModelVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluatedModelVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainingResultV2:
    boto3_raw_data: "type_defs.TrainingResultV2TypeDef" = dataclasses.field()

    @cached_property
    def dataValidationMetrics(self):  # pragma: no cover
        return DataValidationMetrics.make_one(
            self.boto3_raw_data["dataValidationMetrics"]
        )

    @cached_property
    def trainingMetricsV2(self):  # pragma: no cover
        return TrainingMetricsV2.make_one(self.boto3_raw_data["trainingMetricsV2"])

    @cached_property
    def variableImportanceMetrics(self):  # pragma: no cover
        return VariableImportanceMetrics.make_one(
            self.boto3_raw_data["variableImportanceMetrics"]
        )

    @cached_property
    def aggregatedVariablesImportanceMetrics(self):  # pragma: no cover
        return AggregatedVariablesImportanceMetrics.make_one(
            self.boto3_raw_data["aggregatedVariablesImportanceMetrics"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrainingResultV2TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainingResultV2TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventPredictionMetadataResult:
    boto3_raw_data: "type_defs.GetEventPredictionMetadataResultTypeDef" = (
        dataclasses.field()
    )

    eventId = field("eventId")
    eventTypeName = field("eventTypeName")
    entityId = field("entityId")
    entityType = field("entityType")
    eventTimestamp = field("eventTimestamp")
    detectorId = field("detectorId")
    detectorVersionId = field("detectorVersionId")
    detectorVersionStatus = field("detectorVersionStatus")

    @cached_property
    def eventVariables(self):  # pragma: no cover
        return EventVariableSummary.make_many(self.boto3_raw_data["eventVariables"])

    @cached_property
    def rules(self):  # pragma: no cover
        return EvaluatedRule.make_many(self.boto3_raw_data["rules"])

    ruleExecutionMode = field("ruleExecutionMode")
    outcomes = field("outcomes")

    @cached_property
    def evaluatedModelVersions(self):  # pragma: no cover
        return EvaluatedModelVersion.make_many(
            self.boto3_raw_data["evaluatedModelVersions"]
        )

    @cached_property
    def evaluatedExternalModels(self):  # pragma: no cover
        return EvaluatedExternalModel.make_many(
            self.boto3_raw_data["evaluatedExternalModels"]
        )

    predictionTimestamp = field("predictionTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetEventPredictionMetadataResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventPredictionMetadataResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelVersionDetail:
    boto3_raw_data: "type_defs.ModelVersionDetailTypeDef" = dataclasses.field()

    modelId = field("modelId")
    modelType = field("modelType")
    modelVersionNumber = field("modelVersionNumber")
    status = field("status")
    trainingDataSource = field("trainingDataSource")

    @cached_property
    def trainingDataSchema(self):  # pragma: no cover
        return TrainingDataSchemaOutput.make_one(
            self.boto3_raw_data["trainingDataSchema"]
        )

    @cached_property
    def externalEventsDetail(self):  # pragma: no cover
        return ExternalEventsDetail.make_one(
            self.boto3_raw_data["externalEventsDetail"]
        )

    @cached_property
    def ingestedEventsDetail(self):  # pragma: no cover
        return IngestedEventsDetail.make_one(
            self.boto3_raw_data["ingestedEventsDetail"]
        )

    @cached_property
    def trainingResult(self):  # pragma: no cover
        return TrainingResult.make_one(self.boto3_raw_data["trainingResult"])

    lastUpdatedTime = field("lastUpdatedTime")
    createdTime = field("createdTime")
    arn = field("arn")

    @cached_property
    def trainingResultV2(self):  # pragma: no cover
        return TrainingResultV2.make_one(self.boto3_raw_data["trainingResultV2"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModelVersionDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelVersionDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeModelVersionsResult:
    boto3_raw_data: "type_defs.DescribeModelVersionsResultTypeDef" = dataclasses.field()

    @cached_property
    def modelVersionDetails(self):  # pragma: no cover
        return ModelVersionDetail.make_many(self.boto3_raw_data["modelVersionDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeModelVersionsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeModelVersionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
