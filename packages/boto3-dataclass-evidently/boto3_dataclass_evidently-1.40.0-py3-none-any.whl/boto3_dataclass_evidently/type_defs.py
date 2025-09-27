# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_evidently import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class EvaluationRequest:
    boto3_raw_data: "type_defs.EvaluationRequestTypeDef" = dataclasses.field()

    entityId = field("entityId")
    feature = field("feature")
    evaluationContext = field("evaluationContext")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluationRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationRequestTypeDef"]
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
class CloudWatchLogsDestinationConfig:
    boto3_raw_data: "type_defs.CloudWatchLogsDestinationConfigTypeDef" = (
        dataclasses.field()
    )

    logGroup = field("logGroup")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CloudWatchLogsDestinationConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLogsDestinationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchLogsDestination:
    boto3_raw_data: "type_defs.CloudWatchLogsDestinationTypeDef" = dataclasses.field()

    logGroup = field("logGroup")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchLogsDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLogsDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OnlineAbConfig:
    boto3_raw_data: "type_defs.OnlineAbConfigTypeDef" = dataclasses.field()

    controlTreatmentName = field("controlTreatmentName")
    treatmentWeights = field("treatmentWeights")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OnlineAbConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OnlineAbConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TreatmentConfig:
    boto3_raw_data: "type_defs.TreatmentConfigTypeDef" = dataclasses.field()

    feature = field("feature")
    name = field("name")
    variation = field("variation")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TreatmentConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TreatmentConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchGroupConfig:
    boto3_raw_data: "type_defs.LaunchGroupConfigTypeDef" = dataclasses.field()

    feature = field("feature")
    name = field("name")
    variation = field("variation")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LaunchGroupConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchGroupConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectAppConfigResourceConfig:
    boto3_raw_data: "type_defs.ProjectAppConfigResourceConfigTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    environmentId = field("environmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProjectAppConfigResourceConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectAppConfigResourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSegmentRequest:
    boto3_raw_data: "type_defs.CreateSegmentRequestTypeDef" = dataclasses.field()

    name = field("name")
    pattern = field("pattern")
    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSegmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSegmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Segment:
    boto3_raw_data: "type_defs.SegmentTypeDef" = dataclasses.field()

    arn = field("arn")
    createdTime = field("createdTime")
    lastUpdatedTime = field("lastUpdatedTime")
    name = field("name")
    pattern = field("pattern")
    description = field("description")
    experimentCount = field("experimentCount")
    launchCount = field("launchCount")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SegmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SegmentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteExperimentRequest:
    boto3_raw_data: "type_defs.DeleteExperimentRequestTypeDef" = dataclasses.field()

    experiment = field("experiment")
    project = field("project")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteExperimentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteExperimentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFeatureRequest:
    boto3_raw_data: "type_defs.DeleteFeatureRequestTypeDef" = dataclasses.field()

    feature = field("feature")
    project = field("project")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFeatureRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFeatureRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLaunchRequest:
    boto3_raw_data: "type_defs.DeleteLaunchRequestTypeDef" = dataclasses.field()

    launch = field("launch")
    project = field("project")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLaunchRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLaunchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProjectRequest:
    boto3_raw_data: "type_defs.DeleteProjectRequestTypeDef" = dataclasses.field()

    project = field("project")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSegmentRequest:
    boto3_raw_data: "type_defs.DeleteSegmentRequestTypeDef" = dataclasses.field()

    segment = field("segment")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSegmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSegmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluateFeatureRequest:
    boto3_raw_data: "type_defs.EvaluateFeatureRequestTypeDef" = dataclasses.field()

    entityId = field("entityId")
    feature = field("feature")
    project = field("project")
    evaluationContext = field("evaluationContext")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluateFeatureRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluateFeatureRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VariableValue:
    boto3_raw_data: "type_defs.VariableValueTypeDef" = dataclasses.field()

    boolValue = field("boolValue")
    doubleValue = field("doubleValue")
    longValue = field("longValue")
    stringValue = field("stringValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VariableValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VariableValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationRule:
    boto3_raw_data: "type_defs.EvaluationRuleTypeDef" = dataclasses.field()

    type = field("type")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluationRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EvaluationRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentExecution:
    boto3_raw_data: "type_defs.ExperimentExecutionTypeDef" = dataclasses.field()

    endedTime = field("endedTime")
    startedTime = field("startedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExperimentExecutionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentExecutionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentReport:
    boto3_raw_data: "type_defs.ExperimentReportTypeDef" = dataclasses.field()

    content = field("content")
    metricName = field("metricName")
    reportName = field("reportName")
    treatmentName = field("treatmentName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExperimentReportTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentReportTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentResultsData:
    boto3_raw_data: "type_defs.ExperimentResultsDataTypeDef" = dataclasses.field()

    metricName = field("metricName")
    resultStat = field("resultStat")
    treatmentName = field("treatmentName")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExperimentResultsDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentResultsDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentSchedule:
    boto3_raw_data: "type_defs.ExperimentScheduleTypeDef" = dataclasses.field()

    analysisCompleteTime = field("analysisCompleteTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExperimentScheduleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentScheduleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OnlineAbDefinition:
    boto3_raw_data: "type_defs.OnlineAbDefinitionTypeDef" = dataclasses.field()

    controlTreatmentName = field("controlTreatmentName")
    treatmentWeights = field("treatmentWeights")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OnlineAbDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OnlineAbDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Treatment:
    boto3_raw_data: "type_defs.TreatmentTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    featureVariations = field("featureVariations")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TreatmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TreatmentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExperimentRequest:
    boto3_raw_data: "type_defs.GetExperimentRequestTypeDef" = dataclasses.field()

    experiment = field("experiment")
    project = field("project")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExperimentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExperimentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFeatureRequest:
    boto3_raw_data: "type_defs.GetFeatureRequestTypeDef" = dataclasses.field()

    feature = field("feature")
    project = field("project")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFeatureRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFeatureRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLaunchRequest:
    boto3_raw_data: "type_defs.GetLaunchRequestTypeDef" = dataclasses.field()

    launch = field("launch")
    project = field("project")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetLaunchRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLaunchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProjectRequest:
    boto3_raw_data: "type_defs.GetProjectRequestTypeDef" = dataclasses.field()

    project = field("project")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetProjectRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentRequest:
    boto3_raw_data: "type_defs.GetSegmentRequestTypeDef" = dataclasses.field()

    segment = field("segment")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSegmentRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchExecution:
    boto3_raw_data: "type_defs.LaunchExecutionTypeDef" = dataclasses.field()

    endedTime = field("endedTime")
    startedTime = field("startedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LaunchExecutionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LaunchExecutionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchGroup:
    boto3_raw_data: "type_defs.LaunchGroupTypeDef" = dataclasses.field()

    featureVariations = field("featureVariations")
    name = field("name")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LaunchGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LaunchGroupTypeDef"]]
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
class ListExperimentsRequest:
    boto3_raw_data: "type_defs.ListExperimentsRequestTypeDef" = dataclasses.field()

    project = field("project")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExperimentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExperimentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFeaturesRequest:
    boto3_raw_data: "type_defs.ListFeaturesRequestTypeDef" = dataclasses.field()

    project = field("project")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFeaturesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFeaturesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLaunchesRequest:
    boto3_raw_data: "type_defs.ListLaunchesRequestTypeDef" = dataclasses.field()

    project = field("project")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLaunchesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLaunchesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectsRequest:
    boto3_raw_data: "type_defs.ListProjectsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProjectsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectSummary:
    boto3_raw_data: "type_defs.ProjectSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    createdTime = field("createdTime")
    lastUpdatedTime = field("lastUpdatedTime")
    name = field("name")
    status = field("status")
    activeExperimentCount = field("activeExperimentCount")
    activeLaunchCount = field("activeLaunchCount")
    description = field("description")
    experimentCount = field("experimentCount")
    featureCount = field("featureCount")
    launchCount = field("launchCount")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProjectSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProjectSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSegmentReferencesRequest:
    boto3_raw_data: "type_defs.ListSegmentReferencesRequestTypeDef" = (
        dataclasses.field()
    )

    segment = field("segment")
    type = field("type")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSegmentReferencesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSegmentReferencesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RefResource:
    boto3_raw_data: "type_defs.RefResourceTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")
    arn = field("arn")
    endTime = field("endTime")
    lastUpdatedOn = field("lastUpdatedOn")
    startTime = field("startTime")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RefResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RefResourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSegmentsRequest:
    boto3_raw_data: "type_defs.ListSegmentsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSegmentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSegmentsRequestTypeDef"]
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

    resourceArn = field("resourceArn")

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
class MetricDefinitionConfig:
    boto3_raw_data: "type_defs.MetricDefinitionConfigTypeDef" = dataclasses.field()

    entityIdKey = field("entityIdKey")
    name = field("name")
    valueKey = field("valueKey")
    eventPattern = field("eventPattern")
    unitLabel = field("unitLabel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricDefinitionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricDefinitionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDefinition:
    boto3_raw_data: "type_defs.MetricDefinitionTypeDef" = dataclasses.field()

    entityIdKey = field("entityIdKey")
    eventPattern = field("eventPattern")
    name = field("name")
    unitLabel = field("unitLabel")
    valueKey = field("valueKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectAppConfigResource:
    boto3_raw_data: "type_defs.ProjectAppConfigResourceTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    configurationProfileId = field("configurationProfileId")
    environmentId = field("environmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProjectAppConfigResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectAppConfigResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DestinationConfig:
    boto3_raw_data: "type_defs.S3DestinationConfigTypeDef" = dataclasses.field()

    bucket = field("bucket")
    prefix = field("prefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3DestinationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DestinationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Destination:
    boto3_raw_data: "type_defs.S3DestinationTypeDef" = dataclasses.field()

    bucket = field("bucket")
    prefix = field("prefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3DestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3DestinationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutProjectEventsResultEntry:
    boto3_raw_data: "type_defs.PutProjectEventsResultEntryTypeDef" = dataclasses.field()

    errorCode = field("errorCode")
    errorMessage = field("errorMessage")
    eventId = field("eventId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutProjectEventsResultEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutProjectEventsResultEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentOverrideOutput:
    boto3_raw_data: "type_defs.SegmentOverrideOutputTypeDef" = dataclasses.field()

    evaluationOrder = field("evaluationOrder")
    segment = field("segment")
    weights = field("weights")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SegmentOverrideOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SegmentOverrideOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentOverride:
    boto3_raw_data: "type_defs.SegmentOverrideTypeDef" = dataclasses.field()

    evaluationOrder = field("evaluationOrder")
    segment = field("segment")
    weights = field("weights")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SegmentOverrideTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SegmentOverrideTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartLaunchRequest:
    boto3_raw_data: "type_defs.StartLaunchRequestTypeDef" = dataclasses.field()

    launch = field("launch")
    project = field("project")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartLaunchRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartLaunchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopExperimentRequest:
    boto3_raw_data: "type_defs.StopExperimentRequestTypeDef" = dataclasses.field()

    experiment = field("experiment")
    project = field("project")
    desiredState = field("desiredState")
    reason = field("reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopExperimentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopExperimentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopLaunchRequest:
    boto3_raw_data: "type_defs.StopLaunchRequestTypeDef" = dataclasses.field()

    launch = field("launch")
    project = field("project")
    desiredState = field("desiredState")
    reason = field("reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopLaunchRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopLaunchRequestTypeDef"]
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

    resourceArn = field("resourceArn")
    tags = field("tags")

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
class TestSegmentPatternRequest:
    boto3_raw_data: "type_defs.TestSegmentPatternRequestTypeDef" = dataclasses.field()

    pattern = field("pattern")
    payload = field("payload")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestSegmentPatternRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestSegmentPatternRequestTypeDef"]
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

    resourceArn = field("resourceArn")
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
class BatchEvaluateFeatureRequest:
    boto3_raw_data: "type_defs.BatchEvaluateFeatureRequestTypeDef" = dataclasses.field()

    project = field("project")

    @cached_property
    def requests(self):  # pragma: no cover
        return EvaluationRequest.make_many(self.boto3_raw_data["requests"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchEvaluateFeatureRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchEvaluateFeatureRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartExperimentResponse:
    boto3_raw_data: "type_defs.StartExperimentResponseTypeDef" = dataclasses.field()

    startedTime = field("startedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartExperimentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartExperimentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopExperimentResponse:
    boto3_raw_data: "type_defs.StopExperimentResponseTypeDef" = dataclasses.field()

    endedTime = field("endedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopExperimentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopExperimentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopLaunchResponse:
    boto3_raw_data: "type_defs.StopLaunchResponseTypeDef" = dataclasses.field()

    endedTime = field("endedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopLaunchResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopLaunchResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestSegmentPatternResponse:
    boto3_raw_data: "type_defs.TestSegmentPatternResponseTypeDef" = dataclasses.field()

    match = field("match")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestSegmentPatternResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestSegmentPatternResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProjectRequest:
    boto3_raw_data: "type_defs.UpdateProjectRequestTypeDef" = dataclasses.field()

    project = field("project")

    @cached_property
    def appConfigResource(self):  # pragma: no cover
        return ProjectAppConfigResourceConfig.make_one(
            self.boto3_raw_data["appConfigResource"]
        )

    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSegmentResponse:
    boto3_raw_data: "type_defs.CreateSegmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def segment(self):  # pragma: no cover
        return Segment.make_one(self.boto3_raw_data["segment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSegmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSegmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentResponse:
    boto3_raw_data: "type_defs.GetSegmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def segment(self):  # pragma: no cover
        return Segment.make_one(self.boto3_raw_data["segment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSegmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSegmentsResponse:
    boto3_raw_data: "type_defs.ListSegmentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def segments(self):  # pragma: no cover
        return Segment.make_many(self.boto3_raw_data["segments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSegmentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSegmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluateFeatureResponse:
    boto3_raw_data: "type_defs.EvaluateFeatureResponseTypeDef" = dataclasses.field()

    details = field("details")
    reason = field("reason")

    @cached_property
    def value(self):  # pragma: no cover
        return VariableValue.make_one(self.boto3_raw_data["value"])

    variation = field("variation")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluateFeatureResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluateFeatureResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationResult:
    boto3_raw_data: "type_defs.EvaluationResultTypeDef" = dataclasses.field()

    entityId = field("entityId")
    feature = field("feature")
    details = field("details")
    project = field("project")
    reason = field("reason")

    @cached_property
    def value(self):  # pragma: no cover
        return VariableValue.make_one(self.boto3_raw_data["value"])

    variation = field("variation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluationResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VariationConfig:
    boto3_raw_data: "type_defs.VariationConfigTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def value(self):  # pragma: no cover
        return VariableValue.make_one(self.boto3_raw_data["value"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VariationConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VariationConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Variation:
    boto3_raw_data: "type_defs.VariationTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def value(self):  # pragma: no cover
        return VariableValue.make_one(self.boto3_raw_data["value"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VariationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VariationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FeatureSummary:
    boto3_raw_data: "type_defs.FeatureSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    createdTime = field("createdTime")
    evaluationStrategy = field("evaluationStrategy")
    lastUpdatedTime = field("lastUpdatedTime")
    name = field("name")
    status = field("status")
    defaultVariation = field("defaultVariation")

    @cached_property
    def evaluationRules(self):  # pragma: no cover
        return EvaluationRule.make_many(self.boto3_raw_data["evaluationRules"])

    project = field("project")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FeatureSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FeatureSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Event:
    boto3_raw_data: "type_defs.EventTypeDef" = dataclasses.field()

    data = field("data")
    timestamp = field("timestamp")
    type = field("type")

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
class GetExperimentResultsRequest:
    boto3_raw_data: "type_defs.GetExperimentResultsRequestTypeDef" = dataclasses.field()

    experiment = field("experiment")
    metricNames = field("metricNames")
    project = field("project")
    treatmentNames = field("treatmentNames")
    baseStat = field("baseStat")
    endTime = field("endTime")
    period = field("period")
    reportNames = field("reportNames")
    resultStats = field("resultStats")
    startTime = field("startTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExperimentResultsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExperimentResultsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartExperimentRequest:
    boto3_raw_data: "type_defs.StartExperimentRequestTypeDef" = dataclasses.field()

    analysisCompleteTime = field("analysisCompleteTime")
    experiment = field("experiment")
    project = field("project")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartExperimentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartExperimentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExperimentResultsResponse:
    boto3_raw_data: "type_defs.GetExperimentResultsResponseTypeDef" = (
        dataclasses.field()
    )

    details = field("details")

    @cached_property
    def reports(self):  # pragma: no cover
        return ExperimentReport.make_many(self.boto3_raw_data["reports"])

    @cached_property
    def resultsData(self):  # pragma: no cover
        return ExperimentResultsData.make_many(self.boto3_raw_data["resultsData"])

    timestamps = field("timestamps")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExperimentResultsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExperimentResultsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExperimentsRequestPaginate:
    boto3_raw_data: "type_defs.ListExperimentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    project = field("project")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListExperimentsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExperimentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFeaturesRequestPaginate:
    boto3_raw_data: "type_defs.ListFeaturesRequestPaginateTypeDef" = dataclasses.field()

    project = field("project")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFeaturesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFeaturesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLaunchesRequestPaginate:
    boto3_raw_data: "type_defs.ListLaunchesRequestPaginateTypeDef" = dataclasses.field()

    project = field("project")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLaunchesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLaunchesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectsRequestPaginate:
    boto3_raw_data: "type_defs.ListProjectsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProjectsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSegmentReferencesRequestPaginate:
    boto3_raw_data: "type_defs.ListSegmentReferencesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    segment = field("segment")
    type = field("type")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSegmentReferencesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSegmentReferencesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSegmentsRequestPaginate:
    boto3_raw_data: "type_defs.ListSegmentsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSegmentsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSegmentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectsResponse:
    boto3_raw_data: "type_defs.ListProjectsResponseTypeDef" = dataclasses.field()

    @cached_property
    def projects(self):  # pragma: no cover
        return ProjectSummary.make_many(self.boto3_raw_data["projects"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProjectsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSegmentReferencesResponse:
    boto3_raw_data: "type_defs.ListSegmentReferencesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def referencedBy(self):  # pragma: no cover
        return RefResource.make_many(self.boto3_raw_data["referencedBy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSegmentReferencesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSegmentReferencesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricGoalConfig:
    boto3_raw_data: "type_defs.MetricGoalConfigTypeDef" = dataclasses.field()

    @cached_property
    def metricDefinition(self):  # pragma: no cover
        return MetricDefinitionConfig.make_one(self.boto3_raw_data["metricDefinition"])

    desiredChange = field("desiredChange")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricGoalConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricGoalConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricMonitorConfig:
    boto3_raw_data: "type_defs.MetricMonitorConfigTypeDef" = dataclasses.field()

    @cached_property
    def metricDefinition(self):  # pragma: no cover
        return MetricDefinitionConfig.make_one(self.boto3_raw_data["metricDefinition"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricMonitorConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricMonitorConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricGoal:
    boto3_raw_data: "type_defs.MetricGoalTypeDef" = dataclasses.field()

    @cached_property
    def metricDefinition(self):  # pragma: no cover
        return MetricDefinition.make_one(self.boto3_raw_data["metricDefinition"])

    desiredChange = field("desiredChange")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricGoalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricGoalTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricMonitor:
    boto3_raw_data: "type_defs.MetricMonitorTypeDef" = dataclasses.field()

    @cached_property
    def metricDefinition(self):  # pragma: no cover
        return MetricDefinition.make_one(self.boto3_raw_data["metricDefinition"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricMonitorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricMonitorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectDataDeliveryConfig:
    boto3_raw_data: "type_defs.ProjectDataDeliveryConfigTypeDef" = dataclasses.field()

    @cached_property
    def cloudWatchLogs(self):  # pragma: no cover
        return CloudWatchLogsDestinationConfig.make_one(
            self.boto3_raw_data["cloudWatchLogs"]
        )

    @cached_property
    def s3Destination(self):  # pragma: no cover
        return S3DestinationConfig.make_one(self.boto3_raw_data["s3Destination"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProjectDataDeliveryConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectDataDeliveryConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProjectDataDeliveryRequest:
    boto3_raw_data: "type_defs.UpdateProjectDataDeliveryRequestTypeDef" = (
        dataclasses.field()
    )

    project = field("project")

    @cached_property
    def cloudWatchLogs(self):  # pragma: no cover
        return CloudWatchLogsDestinationConfig.make_one(
            self.boto3_raw_data["cloudWatchLogs"]
        )

    @cached_property
    def s3Destination(self):  # pragma: no cover
        return S3DestinationConfig.make_one(self.boto3_raw_data["s3Destination"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateProjectDataDeliveryRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProjectDataDeliveryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectDataDelivery:
    boto3_raw_data: "type_defs.ProjectDataDeliveryTypeDef" = dataclasses.field()

    @cached_property
    def cloudWatchLogs(self):  # pragma: no cover
        return CloudWatchLogsDestination.make_one(self.boto3_raw_data["cloudWatchLogs"])

    @cached_property
    def s3Destination(self):  # pragma: no cover
        return S3Destination.make_one(self.boto3_raw_data["s3Destination"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProjectDataDeliveryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectDataDeliveryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutProjectEventsResponse:
    boto3_raw_data: "type_defs.PutProjectEventsResponseTypeDef" = dataclasses.field()

    @cached_property
    def eventResults(self):  # pragma: no cover
        return PutProjectEventsResultEntry.make_many(
            self.boto3_raw_data["eventResults"]
        )

    failedEventCount = field("failedEventCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutProjectEventsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutProjectEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledSplit:
    boto3_raw_data: "type_defs.ScheduledSplitTypeDef" = dataclasses.field()

    startTime = field("startTime")
    groupWeights = field("groupWeights")

    @cached_property
    def segmentOverrides(self):  # pragma: no cover
        return SegmentOverrideOutput.make_many(self.boto3_raw_data["segmentOverrides"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduledSplitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduledSplitTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchEvaluateFeatureResponse:
    boto3_raw_data: "type_defs.BatchEvaluateFeatureResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def results(self):  # pragma: no cover
        return EvaluationResult.make_many(self.boto3_raw_data["results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchEvaluateFeatureResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchEvaluateFeatureResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFeatureRequest:
    boto3_raw_data: "type_defs.CreateFeatureRequestTypeDef" = dataclasses.field()

    name = field("name")
    project = field("project")

    @cached_property
    def variations(self):  # pragma: no cover
        return VariationConfig.make_many(self.boto3_raw_data["variations"])

    defaultVariation = field("defaultVariation")
    description = field("description")
    entityOverrides = field("entityOverrides")
    evaluationStrategy = field("evaluationStrategy")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFeatureRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFeatureRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFeatureRequest:
    boto3_raw_data: "type_defs.UpdateFeatureRequestTypeDef" = dataclasses.field()

    feature = field("feature")
    project = field("project")

    @cached_property
    def addOrUpdateVariations(self):  # pragma: no cover
        return VariationConfig.make_many(self.boto3_raw_data["addOrUpdateVariations"])

    defaultVariation = field("defaultVariation")
    description = field("description")
    entityOverrides = field("entityOverrides")
    evaluationStrategy = field("evaluationStrategy")
    removeVariations = field("removeVariations")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFeatureRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFeatureRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Feature:
    boto3_raw_data: "type_defs.FeatureTypeDef" = dataclasses.field()

    arn = field("arn")
    createdTime = field("createdTime")
    evaluationStrategy = field("evaluationStrategy")
    lastUpdatedTime = field("lastUpdatedTime")
    name = field("name")
    status = field("status")
    valueType = field("valueType")

    @cached_property
    def variations(self):  # pragma: no cover
        return Variation.make_many(self.boto3_raw_data["variations"])

    defaultVariation = field("defaultVariation")
    description = field("description")
    entityOverrides = field("entityOverrides")

    @cached_property
    def evaluationRules(self):  # pragma: no cover
        return EvaluationRule.make_many(self.boto3_raw_data["evaluationRules"])

    project = field("project")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FeatureTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FeatureTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFeaturesResponse:
    boto3_raw_data: "type_defs.ListFeaturesResponseTypeDef" = dataclasses.field()

    @cached_property
    def features(self):  # pragma: no cover
        return FeatureSummary.make_many(self.boto3_raw_data["features"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFeaturesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFeaturesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutProjectEventsRequest:
    boto3_raw_data: "type_defs.PutProjectEventsRequestTypeDef" = dataclasses.field()

    @cached_property
    def events(self):  # pragma: no cover
        return Event.make_many(self.boto3_raw_data["events"])

    project = field("project")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutProjectEventsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutProjectEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExperimentRequest:
    boto3_raw_data: "type_defs.CreateExperimentRequestTypeDef" = dataclasses.field()

    @cached_property
    def metricGoals(self):  # pragma: no cover
        return MetricGoalConfig.make_many(self.boto3_raw_data["metricGoals"])

    name = field("name")
    project = field("project")

    @cached_property
    def treatments(self):  # pragma: no cover
        return TreatmentConfig.make_many(self.boto3_raw_data["treatments"])

    description = field("description")

    @cached_property
    def onlineAbConfig(self):  # pragma: no cover
        return OnlineAbConfig.make_one(self.boto3_raw_data["onlineAbConfig"])

    randomizationSalt = field("randomizationSalt")
    samplingRate = field("samplingRate")
    segment = field("segment")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateExperimentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExperimentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateExperimentRequest:
    boto3_raw_data: "type_defs.UpdateExperimentRequestTypeDef" = dataclasses.field()

    experiment = field("experiment")
    project = field("project")
    description = field("description")

    @cached_property
    def metricGoals(self):  # pragma: no cover
        return MetricGoalConfig.make_many(self.boto3_raw_data["metricGoals"])

    @cached_property
    def onlineAbConfig(self):  # pragma: no cover
        return OnlineAbConfig.make_one(self.boto3_raw_data["onlineAbConfig"])

    randomizationSalt = field("randomizationSalt")
    removeSegment = field("removeSegment")
    samplingRate = field("samplingRate")
    segment = field("segment")

    @cached_property
    def treatments(self):  # pragma: no cover
        return TreatmentConfig.make_many(self.boto3_raw_data["treatments"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateExperimentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateExperimentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Experiment:
    boto3_raw_data: "type_defs.ExperimentTypeDef" = dataclasses.field()

    arn = field("arn")
    createdTime = field("createdTime")
    lastUpdatedTime = field("lastUpdatedTime")
    name = field("name")
    status = field("status")
    type = field("type")
    description = field("description")

    @cached_property
    def execution(self):  # pragma: no cover
        return ExperimentExecution.make_one(self.boto3_raw_data["execution"])

    @cached_property
    def metricGoals(self):  # pragma: no cover
        return MetricGoal.make_many(self.boto3_raw_data["metricGoals"])

    @cached_property
    def onlineAbDefinition(self):  # pragma: no cover
        return OnlineAbDefinition.make_one(self.boto3_raw_data["onlineAbDefinition"])

    project = field("project")
    randomizationSalt = field("randomizationSalt")
    samplingRate = field("samplingRate")

    @cached_property
    def schedule(self):  # pragma: no cover
        return ExperimentSchedule.make_one(self.boto3_raw_data["schedule"])

    segment = field("segment")
    statusReason = field("statusReason")
    tags = field("tags")

    @cached_property
    def treatments(self):  # pragma: no cover
        return Treatment.make_many(self.boto3_raw_data["treatments"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExperimentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExperimentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProjectRequest:
    boto3_raw_data: "type_defs.CreateProjectRequestTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def appConfigResource(self):  # pragma: no cover
        return ProjectAppConfigResourceConfig.make_one(
            self.boto3_raw_data["appConfigResource"]
        )

    @cached_property
    def dataDelivery(self):  # pragma: no cover
        return ProjectDataDeliveryConfig.make_one(self.boto3_raw_data["dataDelivery"])

    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Project:
    boto3_raw_data: "type_defs.ProjectTypeDef" = dataclasses.field()

    arn = field("arn")
    createdTime = field("createdTime")
    lastUpdatedTime = field("lastUpdatedTime")
    name = field("name")
    status = field("status")
    activeExperimentCount = field("activeExperimentCount")
    activeLaunchCount = field("activeLaunchCount")

    @cached_property
    def appConfigResource(self):  # pragma: no cover
        return ProjectAppConfigResource.make_one(
            self.boto3_raw_data["appConfigResource"]
        )

    @cached_property
    def dataDelivery(self):  # pragma: no cover
        return ProjectDataDelivery.make_one(self.boto3_raw_data["dataDelivery"])

    description = field("description")
    experimentCount = field("experimentCount")
    featureCount = field("featureCount")
    launchCount = field("launchCount")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProjectTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledSplitsLaunchDefinition:
    boto3_raw_data: "type_defs.ScheduledSplitsLaunchDefinitionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def steps(self):  # pragma: no cover
        return ScheduledSplit.make_many(self.boto3_raw_data["steps"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ScheduledSplitsLaunchDefinitionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduledSplitsLaunchDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledSplitConfig:
    boto3_raw_data: "type_defs.ScheduledSplitConfigTypeDef" = dataclasses.field()

    groupWeights = field("groupWeights")
    startTime = field("startTime")
    segmentOverrides = field("segmentOverrides")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduledSplitConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduledSplitConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFeatureResponse:
    boto3_raw_data: "type_defs.CreateFeatureResponseTypeDef" = dataclasses.field()

    @cached_property
    def feature(self):  # pragma: no cover
        return Feature.make_one(self.boto3_raw_data["feature"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFeatureResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFeatureResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFeatureResponse:
    boto3_raw_data: "type_defs.GetFeatureResponseTypeDef" = dataclasses.field()

    @cached_property
    def feature(self):  # pragma: no cover
        return Feature.make_one(self.boto3_raw_data["feature"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFeatureResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFeatureResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFeatureResponse:
    boto3_raw_data: "type_defs.UpdateFeatureResponseTypeDef" = dataclasses.field()

    @cached_property
    def feature(self):  # pragma: no cover
        return Feature.make_one(self.boto3_raw_data["feature"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFeatureResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFeatureResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExperimentResponse:
    boto3_raw_data: "type_defs.CreateExperimentResponseTypeDef" = dataclasses.field()

    @cached_property
    def experiment(self):  # pragma: no cover
        return Experiment.make_one(self.boto3_raw_data["experiment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateExperimentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExperimentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExperimentResponse:
    boto3_raw_data: "type_defs.GetExperimentResponseTypeDef" = dataclasses.field()

    @cached_property
    def experiment(self):  # pragma: no cover
        return Experiment.make_one(self.boto3_raw_data["experiment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExperimentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExperimentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExperimentsResponse:
    boto3_raw_data: "type_defs.ListExperimentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def experiments(self):  # pragma: no cover
        return Experiment.make_many(self.boto3_raw_data["experiments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExperimentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExperimentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateExperimentResponse:
    boto3_raw_data: "type_defs.UpdateExperimentResponseTypeDef" = dataclasses.field()

    @cached_property
    def experiment(self):  # pragma: no cover
        return Experiment.make_one(self.boto3_raw_data["experiment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateExperimentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateExperimentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProjectResponse:
    boto3_raw_data: "type_defs.CreateProjectResponseTypeDef" = dataclasses.field()

    @cached_property
    def project(self):  # pragma: no cover
        return Project.make_one(self.boto3_raw_data["project"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProjectResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProjectResponse:
    boto3_raw_data: "type_defs.GetProjectResponseTypeDef" = dataclasses.field()

    @cached_property
    def project(self):  # pragma: no cover
        return Project.make_one(self.boto3_raw_data["project"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetProjectResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProjectDataDeliveryResponse:
    boto3_raw_data: "type_defs.UpdateProjectDataDeliveryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def project(self):  # pragma: no cover
        return Project.make_one(self.boto3_raw_data["project"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateProjectDataDeliveryResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProjectDataDeliveryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProjectResponse:
    boto3_raw_data: "type_defs.UpdateProjectResponseTypeDef" = dataclasses.field()

    @cached_property
    def project(self):  # pragma: no cover
        return Project.make_one(self.boto3_raw_data["project"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProjectResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Launch:
    boto3_raw_data: "type_defs.LaunchTypeDef" = dataclasses.field()

    arn = field("arn")
    createdTime = field("createdTime")
    lastUpdatedTime = field("lastUpdatedTime")
    name = field("name")
    status = field("status")
    type = field("type")
    description = field("description")

    @cached_property
    def execution(self):  # pragma: no cover
        return LaunchExecution.make_one(self.boto3_raw_data["execution"])

    @cached_property
    def groups(self):  # pragma: no cover
        return LaunchGroup.make_many(self.boto3_raw_data["groups"])

    @cached_property
    def metricMonitors(self):  # pragma: no cover
        return MetricMonitor.make_many(self.boto3_raw_data["metricMonitors"])

    project = field("project")
    randomizationSalt = field("randomizationSalt")

    @cached_property
    def scheduledSplitsDefinition(self):  # pragma: no cover
        return ScheduledSplitsLaunchDefinition.make_one(
            self.boto3_raw_data["scheduledSplitsDefinition"]
        )

    statusReason = field("statusReason")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LaunchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LaunchTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledSplitsLaunchConfig:
    boto3_raw_data: "type_defs.ScheduledSplitsLaunchConfigTypeDef" = dataclasses.field()

    @cached_property
    def steps(self):  # pragma: no cover
        return ScheduledSplitConfig.make_many(self.boto3_raw_data["steps"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduledSplitsLaunchConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduledSplitsLaunchConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLaunchResponse:
    boto3_raw_data: "type_defs.CreateLaunchResponseTypeDef" = dataclasses.field()

    @cached_property
    def launch(self):  # pragma: no cover
        return Launch.make_one(self.boto3_raw_data["launch"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLaunchResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLaunchResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLaunchResponse:
    boto3_raw_data: "type_defs.GetLaunchResponseTypeDef" = dataclasses.field()

    @cached_property
    def launch(self):  # pragma: no cover
        return Launch.make_one(self.boto3_raw_data["launch"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetLaunchResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLaunchResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLaunchesResponse:
    boto3_raw_data: "type_defs.ListLaunchesResponseTypeDef" = dataclasses.field()

    @cached_property
    def launches(self):  # pragma: no cover
        return Launch.make_many(self.boto3_raw_data["launches"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLaunchesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLaunchesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartLaunchResponse:
    boto3_raw_data: "type_defs.StartLaunchResponseTypeDef" = dataclasses.field()

    @cached_property
    def launch(self):  # pragma: no cover
        return Launch.make_one(self.boto3_raw_data["launch"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartLaunchResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartLaunchResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLaunchResponse:
    boto3_raw_data: "type_defs.UpdateLaunchResponseTypeDef" = dataclasses.field()

    @cached_property
    def launch(self):  # pragma: no cover
        return Launch.make_one(self.boto3_raw_data["launch"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLaunchResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLaunchResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLaunchRequest:
    boto3_raw_data: "type_defs.CreateLaunchRequestTypeDef" = dataclasses.field()

    @cached_property
    def groups(self):  # pragma: no cover
        return LaunchGroupConfig.make_many(self.boto3_raw_data["groups"])

    name = field("name")
    project = field("project")
    description = field("description")

    @cached_property
    def metricMonitors(self):  # pragma: no cover
        return MetricMonitorConfig.make_many(self.boto3_raw_data["metricMonitors"])

    randomizationSalt = field("randomizationSalt")

    @cached_property
    def scheduledSplitsConfig(self):  # pragma: no cover
        return ScheduledSplitsLaunchConfig.make_one(
            self.boto3_raw_data["scheduledSplitsConfig"]
        )

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLaunchRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLaunchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLaunchRequest:
    boto3_raw_data: "type_defs.UpdateLaunchRequestTypeDef" = dataclasses.field()

    launch = field("launch")
    project = field("project")
    description = field("description")

    @cached_property
    def groups(self):  # pragma: no cover
        return LaunchGroupConfig.make_many(self.boto3_raw_data["groups"])

    @cached_property
    def metricMonitors(self):  # pragma: no cover
        return MetricMonitorConfig.make_many(self.boto3_raw_data["metricMonitors"])

    randomizationSalt = field("randomizationSalt")

    @cached_property
    def scheduledSplitsConfig(self):  # pragma: no cover
        return ScheduledSplitsLaunchConfig.make_one(
            self.boto3_raw_data["scheduledSplitsConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLaunchRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLaunchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
