# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_datapipeline import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ParameterValue:
    boto3_raw_data: "type_defs.ParameterValueTypeDef" = dataclasses.field()

    id = field("id")
    stringValue = field("stringValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParameterValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParameterValueTypeDef"]],
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
class DeactivatePipelineInput:
    boto3_raw_data: "type_defs.DeactivatePipelineInputTypeDef" = dataclasses.field()

    pipelineId = field("pipelineId")
    cancelActive = field("cancelActive")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeactivatePipelineInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeactivatePipelineInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePipelineInput:
    boto3_raw_data: "type_defs.DeletePipelineInputTypeDef" = dataclasses.field()

    pipelineId = field("pipelineId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePipelineInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePipelineInputTypeDef"]
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
class DescribeObjectsInput:
    boto3_raw_data: "type_defs.DescribeObjectsInputTypeDef" = dataclasses.field()

    pipelineId = field("pipelineId")
    objectIds = field("objectIds")
    evaluateExpressions = field("evaluateExpressions")
    marker = field("marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeObjectsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeObjectsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePipelinesInput:
    boto3_raw_data: "type_defs.DescribePipelinesInputTypeDef" = dataclasses.field()

    pipelineIds = field("pipelineIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePipelinesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePipelinesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluateExpressionInput:
    boto3_raw_data: "type_defs.EvaluateExpressionInputTypeDef" = dataclasses.field()

    pipelineId = field("pipelineId")
    objectId = field("objectId")
    expression = field("expression")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluateExpressionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluateExpressionInputTypeDef"]
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

    key = field("key")
    stringValue = field("stringValue")
    refValue = field("refValue")

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
class GetPipelineDefinitionInput:
    boto3_raw_data: "type_defs.GetPipelineDefinitionInputTypeDef" = dataclasses.field()

    pipelineId = field("pipelineId")
    version = field("version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPipelineDefinitionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPipelineDefinitionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceIdentity:
    boto3_raw_data: "type_defs.InstanceIdentityTypeDef" = dataclasses.field()

    document = field("document")
    signature = field("signature")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceIdentityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceIdentityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelinesInput:
    boto3_raw_data: "type_defs.ListPipelinesInputTypeDef" = dataclasses.field()

    marker = field("marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPipelinesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelinesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineIdName:
    boto3_raw_data: "type_defs.PipelineIdNameTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PipelineIdNameTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PipelineIdNameTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Operator:
    boto3_raw_data: "type_defs.OperatorTypeDef" = dataclasses.field()

    type = field("type")
    values = field("values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OperatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OperatorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterAttribute:
    boto3_raw_data: "type_defs.ParameterAttributeTypeDef" = dataclasses.field()

    key = field("key")
    stringValue = field("stringValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParameterAttributeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParameterAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidationError:
    boto3_raw_data: "type_defs.ValidationErrorTypeDef" = dataclasses.field()

    id = field("id")
    errors = field("errors")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValidationErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ValidationErrorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidationWarning:
    boto3_raw_data: "type_defs.ValidationWarningTypeDef" = dataclasses.field()

    id = field("id")
    warnings = field("warnings")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValidationWarningTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidationWarningTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveTagsInput:
    boto3_raw_data: "type_defs.RemoveTagsInputTypeDef" = dataclasses.field()

    pipelineId = field("pipelineId")
    tagKeys = field("tagKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RemoveTagsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RemoveTagsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportTaskRunnerHeartbeatInput:
    boto3_raw_data: "type_defs.ReportTaskRunnerHeartbeatInputTypeDef" = (
        dataclasses.field()
    )

    taskrunnerId = field("taskrunnerId")
    workerGroup = field("workerGroup")
    hostname = field("hostname")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReportTaskRunnerHeartbeatInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReportTaskRunnerHeartbeatInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetStatusInput:
    boto3_raw_data: "type_defs.SetStatusInputTypeDef" = dataclasses.field()

    pipelineId = field("pipelineId")
    objectIds = field("objectIds")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SetStatusInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SetStatusInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetTaskStatusInput:
    boto3_raw_data: "type_defs.SetTaskStatusInputTypeDef" = dataclasses.field()

    taskId = field("taskId")
    taskStatus = field("taskStatus")
    errorId = field("errorId")
    errorMessage = field("errorMessage")
    errorStackTrace = field("errorStackTrace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetTaskStatusInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetTaskStatusInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivatePipelineInput:
    boto3_raw_data: "type_defs.ActivatePipelineInputTypeDef" = dataclasses.field()

    pipelineId = field("pipelineId")

    @cached_property
    def parameterValues(self):  # pragma: no cover
        return ParameterValue.make_many(self.boto3_raw_data["parameterValues"])

    startTimestamp = field("startTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActivatePipelineInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivatePipelineInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddTagsInput:
    boto3_raw_data: "type_defs.AddTagsInputTypeDef" = dataclasses.field()

    pipelineId = field("pipelineId")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddTagsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddTagsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePipelineInput:
    boto3_raw_data: "type_defs.CreatePipelineInputTypeDef" = dataclasses.field()

    name = field("name")
    uniqueId = field("uniqueId")
    description = field("description")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePipelineInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePipelineInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePipelineOutput:
    boto3_raw_data: "type_defs.CreatePipelineOutputTypeDef" = dataclasses.field()

    pipelineId = field("pipelineId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePipelineOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePipelineOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluateExpressionOutput:
    boto3_raw_data: "type_defs.EvaluateExpressionOutputTypeDef" = dataclasses.field()

    evaluatedExpression = field("evaluatedExpression")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluateExpressionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluateExpressionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryObjectsOutput:
    boto3_raw_data: "type_defs.QueryObjectsOutputTypeDef" = dataclasses.field()

    ids = field("ids")
    marker = field("marker")
    hasMoreResults = field("hasMoreResults")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryObjectsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryObjectsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportTaskProgressOutput:
    boto3_raw_data: "type_defs.ReportTaskProgressOutputTypeDef" = dataclasses.field()

    canceled = field("canceled")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReportTaskProgressOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReportTaskProgressOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportTaskRunnerHeartbeatOutput:
    boto3_raw_data: "type_defs.ReportTaskRunnerHeartbeatOutputTypeDef" = (
        dataclasses.field()
    )

    terminate = field("terminate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReportTaskRunnerHeartbeatOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReportTaskRunnerHeartbeatOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeObjectsInputPaginate:
    boto3_raw_data: "type_defs.DescribeObjectsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    pipelineId = field("pipelineId")
    objectIds = field("objectIds")
    evaluateExpressions = field("evaluateExpressions")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeObjectsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeObjectsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelinesInputPaginate:
    boto3_raw_data: "type_defs.ListPipelinesInputPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPipelinesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelinesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineDescription:
    boto3_raw_data: "type_defs.PipelineDescriptionTypeDef" = dataclasses.field()

    pipelineId = field("pipelineId")
    name = field("name")

    @cached_property
    def fields(self):  # pragma: no cover
        return Field.make_many(self.boto3_raw_data["fields"])

    description = field("description")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipelineDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineObjectOutput:
    boto3_raw_data: "type_defs.PipelineObjectOutputTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")

    @cached_property
    def fields(self):  # pragma: no cover
        return Field.make_many(self.boto3_raw_data["fields"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipelineObjectOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineObjectOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineObject:
    boto3_raw_data: "type_defs.PipelineObjectTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")

    @cached_property
    def fields(self):  # pragma: no cover
        return Field.make_many(self.boto3_raw_data["fields"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PipelineObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PipelineObjectTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportTaskProgressInput:
    boto3_raw_data: "type_defs.ReportTaskProgressInputTypeDef" = dataclasses.field()

    taskId = field("taskId")

    @cached_property
    def fields(self):  # pragma: no cover
        return Field.make_many(self.boto3_raw_data["fields"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReportTaskProgressInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReportTaskProgressInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PollForTaskInput:
    boto3_raw_data: "type_defs.PollForTaskInputTypeDef" = dataclasses.field()

    workerGroup = field("workerGroup")
    hostname = field("hostname")

    @cached_property
    def instanceIdentity(self):  # pragma: no cover
        return InstanceIdentity.make_one(self.boto3_raw_data["instanceIdentity"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PollForTaskInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PollForTaskInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelinesOutput:
    boto3_raw_data: "type_defs.ListPipelinesOutputTypeDef" = dataclasses.field()

    @cached_property
    def pipelineIdList(self):  # pragma: no cover
        return PipelineIdName.make_many(self.boto3_raw_data["pipelineIdList"])

    marker = field("marker")
    hasMoreResults = field("hasMoreResults")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPipelinesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelinesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Selector:
    boto3_raw_data: "type_defs.SelectorTypeDef" = dataclasses.field()

    fieldName = field("fieldName")

    @cached_property
    def operator(self):  # pragma: no cover
        return Operator.make_one(self.boto3_raw_data["operator"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SelectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SelectorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterObjectOutput:
    boto3_raw_data: "type_defs.ParameterObjectOutputTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def attributes(self):  # pragma: no cover
        return ParameterAttribute.make_many(self.boto3_raw_data["attributes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParameterObjectOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParameterObjectOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterObject:
    boto3_raw_data: "type_defs.ParameterObjectTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def attributes(self):  # pragma: no cover
        return ParameterAttribute.make_many(self.boto3_raw_data["attributes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParameterObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParameterObjectTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPipelineDefinitionOutput:
    boto3_raw_data: "type_defs.PutPipelineDefinitionOutputTypeDef" = dataclasses.field()

    @cached_property
    def validationErrors(self):  # pragma: no cover
        return ValidationError.make_many(self.boto3_raw_data["validationErrors"])

    @cached_property
    def validationWarnings(self):  # pragma: no cover
        return ValidationWarning.make_many(self.boto3_raw_data["validationWarnings"])

    errored = field("errored")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutPipelineDefinitionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPipelineDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidatePipelineDefinitionOutput:
    boto3_raw_data: "type_defs.ValidatePipelineDefinitionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def validationErrors(self):  # pragma: no cover
        return ValidationError.make_many(self.boto3_raw_data["validationErrors"])

    @cached_property
    def validationWarnings(self):  # pragma: no cover
        return ValidationWarning.make_many(self.boto3_raw_data["validationWarnings"])

    errored = field("errored")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ValidatePipelineDefinitionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidatePipelineDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePipelinesOutput:
    boto3_raw_data: "type_defs.DescribePipelinesOutputTypeDef" = dataclasses.field()

    @cached_property
    def pipelineDescriptionList(self):  # pragma: no cover
        return PipelineDescription.make_many(
            self.boto3_raw_data["pipelineDescriptionList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePipelinesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePipelinesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeObjectsOutput:
    boto3_raw_data: "type_defs.DescribeObjectsOutputTypeDef" = dataclasses.field()

    @cached_property
    def pipelineObjects(self):  # pragma: no cover
        return PipelineObjectOutput.make_many(self.boto3_raw_data["pipelineObjects"])

    marker = field("marker")
    hasMoreResults = field("hasMoreResults")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeObjectsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeObjectsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskObject:
    boto3_raw_data: "type_defs.TaskObjectTypeDef" = dataclasses.field()

    taskId = field("taskId")
    pipelineId = field("pipelineId")
    attemptId = field("attemptId")
    objects = field("objects")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaskObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaskObjectTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Query:
    boto3_raw_data: "type_defs.QueryTypeDef" = dataclasses.field()

    @cached_property
    def selectors(self):  # pragma: no cover
        return Selector.make_many(self.boto3_raw_data["selectors"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPipelineDefinitionOutput:
    boto3_raw_data: "type_defs.GetPipelineDefinitionOutputTypeDef" = dataclasses.field()

    @cached_property
    def pipelineObjects(self):  # pragma: no cover
        return PipelineObjectOutput.make_many(self.boto3_raw_data["pipelineObjects"])

    @cached_property
    def parameterObjects(self):  # pragma: no cover
        return ParameterObjectOutput.make_many(self.boto3_raw_data["parameterObjects"])

    @cached_property
    def parameterValues(self):  # pragma: no cover
        return ParameterValue.make_many(self.boto3_raw_data["parameterValues"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPipelineDefinitionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPipelineDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PollForTaskOutput:
    boto3_raw_data: "type_defs.PollForTaskOutputTypeDef" = dataclasses.field()

    @cached_property
    def taskObject(self):  # pragma: no cover
        return TaskObject.make_one(self.boto3_raw_data["taskObject"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PollForTaskOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PollForTaskOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryObjectsInputPaginate:
    boto3_raw_data: "type_defs.QueryObjectsInputPaginateTypeDef" = dataclasses.field()

    pipelineId = field("pipelineId")
    sphere = field("sphere")

    @cached_property
    def query(self):  # pragma: no cover
        return Query.make_one(self.boto3_raw_data["query"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryObjectsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryObjectsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryObjectsInput:
    boto3_raw_data: "type_defs.QueryObjectsInputTypeDef" = dataclasses.field()

    pipelineId = field("pipelineId")
    sphere = field("sphere")

    @cached_property
    def query(self):  # pragma: no cover
        return Query.make_one(self.boto3_raw_data["query"])

    marker = field("marker")
    limit = field("limit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryObjectsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryObjectsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPipelineDefinitionInput:
    boto3_raw_data: "type_defs.PutPipelineDefinitionInputTypeDef" = dataclasses.field()

    pipelineId = field("pipelineId")
    pipelineObjects = field("pipelineObjects")
    parameterObjects = field("parameterObjects")

    @cached_property
    def parameterValues(self):  # pragma: no cover
        return ParameterValue.make_many(self.boto3_raw_data["parameterValues"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutPipelineDefinitionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPipelineDefinitionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidatePipelineDefinitionInput:
    boto3_raw_data: "type_defs.ValidatePipelineDefinitionInputTypeDef" = (
        dataclasses.field()
    )

    pipelineId = field("pipelineId")
    pipelineObjects = field("pipelineObjects")
    parameterObjects = field("parameterObjects")

    @cached_property
    def parameterValues(self):  # pragma: no cover
        return ParameterValue.make_many(self.boto3_raw_data["parameterValues"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ValidatePipelineDefinitionInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidatePipelineDefinitionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
