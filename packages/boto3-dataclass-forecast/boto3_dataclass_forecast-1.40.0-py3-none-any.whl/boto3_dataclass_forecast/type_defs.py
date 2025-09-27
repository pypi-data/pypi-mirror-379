# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_forecast import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Action:
    boto3_raw_data: "type_defs.ActionTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")
    Operation = field("Operation")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdditionalDatasetOutput:
    boto3_raw_data: "type_defs.AdditionalDatasetOutputTypeDef" = dataclasses.field()

    Name = field("Name")
    Configuration = field("Configuration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdditionalDatasetOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdditionalDatasetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdditionalDataset:
    boto3_raw_data: "type_defs.AdditionalDatasetTypeDef" = dataclasses.field()

    Name = field("Name")
    Configuration = field("Configuration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AdditionalDatasetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdditionalDatasetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeConfigOutput:
    boto3_raw_data: "type_defs.AttributeConfigOutputTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")
    Transformations = field("Transformations")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeConfig:
    boto3_raw_data: "type_defs.AttributeConfigTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")
    Transformations = field("Transformations")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributeConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BaselineMetric:
    boto3_raw_data: "type_defs.BaselineMetricTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BaselineMetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BaselineMetricTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CategoricalParameterRangeOutput:
    boto3_raw_data: "type_defs.CategoricalParameterRangeOutputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CategoricalParameterRangeOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CategoricalParameterRangeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CategoricalParameterRange:
    boto3_raw_data: "type_defs.CategoricalParameterRangeTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CategoricalParameterRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CategoricalParameterRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContinuousParameterRange:
    boto3_raw_data: "type_defs.ContinuousParameterRangeTypeDef" = dataclasses.field()

    Name = field("Name")
    MaxValue = field("MaxValue")
    MinValue = field("MinValue")
    ScalingType = field("ScalingType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContinuousParameterRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContinuousParameterRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionConfig:
    boto3_raw_data: "type_defs.EncryptionConfigTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")
    KMSKeyArn = field("KMSKeyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptionConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitorConfig:
    boto3_raw_data: "type_defs.MonitorConfigTypeDef" = dataclasses.field()

    MonitorName = field("MonitorName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MonitorConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MonitorConfigTypeDef"]],
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
class TimeAlignmentBoundary:
    boto3_raw_data: "type_defs.TimeAlignmentBoundaryTypeDef" = dataclasses.field()

    Month = field("Month")
    DayOfMonth = field("DayOfMonth")
    DayOfWeek = field("DayOfWeek")
    Hour = field("Hour")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimeAlignmentBoundaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeAlignmentBoundaryTypeDef"]
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
class ExplainabilityConfig:
    boto3_raw_data: "type_defs.ExplainabilityConfigTypeDef" = dataclasses.field()

    TimeSeriesGranularity = field("TimeSeriesGranularity")
    TimePointGranularity = field("TimePointGranularity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExplainabilityConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExplainabilityConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationParameters:
    boto3_raw_data: "type_defs.EvaluationParametersTypeDef" = dataclasses.field()

    NumberOfBacktestWindows = field("NumberOfBacktestWindows")
    BackTestWindowOffset = field("BackTestWindowOffset")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Config:
    boto3_raw_data: "type_defs.S3ConfigTypeDef" = dataclasses.field()

    Path = field("Path")
    RoleArn = field("RoleArn")
    KMSKeyArn = field("KMSKeyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetGroupSummary:
    boto3_raw_data: "type_defs.DatasetGroupSummaryTypeDef" = dataclasses.field()

    DatasetGroupArn = field("DatasetGroupArn")
    DatasetGroupName = field("DatasetGroupName")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasetGroupSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetGroupSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetSummary:
    boto3_raw_data: "type_defs.DatasetSummaryTypeDef" = dataclasses.field()

    DatasetArn = field("DatasetArn")
    DatasetName = field("DatasetName")
    DatasetType = field("DatasetType")
    Domain = field("Domain")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDatasetGroupRequest:
    boto3_raw_data: "type_defs.DeleteDatasetGroupRequestTypeDef" = dataclasses.field()

    DatasetGroupArn = field("DatasetGroupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDatasetGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDatasetGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDatasetImportJobRequest:
    boto3_raw_data: "type_defs.DeleteDatasetImportJobRequestTypeDef" = (
        dataclasses.field()
    )

    DatasetImportJobArn = field("DatasetImportJobArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDatasetImportJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDatasetImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDatasetRequest:
    boto3_raw_data: "type_defs.DeleteDatasetRequestTypeDef" = dataclasses.field()

    DatasetArn = field("DatasetArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteExplainabilityExportRequest:
    boto3_raw_data: "type_defs.DeleteExplainabilityExportRequestTypeDef" = (
        dataclasses.field()
    )

    ExplainabilityExportArn = field("ExplainabilityExportArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteExplainabilityExportRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteExplainabilityExportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteExplainabilityRequest:
    boto3_raw_data: "type_defs.DeleteExplainabilityRequestTypeDef" = dataclasses.field()

    ExplainabilityArn = field("ExplainabilityArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteExplainabilityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteExplainabilityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteForecastExportJobRequest:
    boto3_raw_data: "type_defs.DeleteForecastExportJobRequestTypeDef" = (
        dataclasses.field()
    )

    ForecastExportJobArn = field("ForecastExportJobArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteForecastExportJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteForecastExportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteForecastRequest:
    boto3_raw_data: "type_defs.DeleteForecastRequestTypeDef" = dataclasses.field()

    ForecastArn = field("ForecastArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteForecastRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteForecastRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMonitorRequest:
    boto3_raw_data: "type_defs.DeleteMonitorRequestTypeDef" = dataclasses.field()

    MonitorArn = field("MonitorArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMonitorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMonitorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePredictorBacktestExportJobRequest:
    boto3_raw_data: "type_defs.DeletePredictorBacktestExportJobRequestTypeDef" = (
        dataclasses.field()
    )

    PredictorBacktestExportJobArn = field("PredictorBacktestExportJobArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeletePredictorBacktestExportJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePredictorBacktestExportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePredictorRequest:
    boto3_raw_data: "type_defs.DeletePredictorRequestTypeDef" = dataclasses.field()

    PredictorArn = field("PredictorArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePredictorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePredictorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourceTreeRequest:
    boto3_raw_data: "type_defs.DeleteResourceTreeRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourceTreeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourceTreeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWhatIfAnalysisRequest:
    boto3_raw_data: "type_defs.DeleteWhatIfAnalysisRequestTypeDef" = dataclasses.field()

    WhatIfAnalysisArn = field("WhatIfAnalysisArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWhatIfAnalysisRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWhatIfAnalysisRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWhatIfForecastExportRequest:
    boto3_raw_data: "type_defs.DeleteWhatIfForecastExportRequestTypeDef" = (
        dataclasses.field()
    )

    WhatIfForecastExportArn = field("WhatIfForecastExportArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteWhatIfForecastExportRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWhatIfForecastExportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWhatIfForecastRequest:
    boto3_raw_data: "type_defs.DeleteWhatIfForecastRequestTypeDef" = dataclasses.field()

    WhatIfForecastArn = field("WhatIfForecastArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWhatIfForecastRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWhatIfForecastRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAutoPredictorRequest:
    boto3_raw_data: "type_defs.DescribeAutoPredictorRequestTypeDef" = (
        dataclasses.field()
    )

    PredictorArn = field("PredictorArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAutoPredictorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAutoPredictorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExplainabilityInfo:
    boto3_raw_data: "type_defs.ExplainabilityInfoTypeDef" = dataclasses.field()

    ExplainabilityArn = field("ExplainabilityArn")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExplainabilityInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExplainabilityInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitorInfo:
    boto3_raw_data: "type_defs.MonitorInfoTypeDef" = dataclasses.field()

    MonitorArn = field("MonitorArn")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MonitorInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MonitorInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReferencePredictorSummary:
    boto3_raw_data: "type_defs.ReferencePredictorSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReferencePredictorSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReferencePredictorSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetGroupRequest:
    boto3_raw_data: "type_defs.DescribeDatasetGroupRequestTypeDef" = dataclasses.field()

    DatasetGroupArn = field("DatasetGroupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDatasetGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetImportJobRequest:
    boto3_raw_data: "type_defs.DescribeDatasetImportJobRequestTypeDef" = (
        dataclasses.field()
    )

    DatasetImportJobArn = field("DatasetImportJobArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDatasetImportJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Statistics:
    boto3_raw_data: "type_defs.StatisticsTypeDef" = dataclasses.field()

    Count = field("Count")
    CountDistinct = field("CountDistinct")
    CountNull = field("CountNull")
    CountNan = field("CountNan")
    Min = field("Min")
    Max = field("Max")
    Avg = field("Avg")
    Stddev = field("Stddev")
    CountLong = field("CountLong")
    CountDistinctLong = field("CountDistinctLong")
    CountNullLong = field("CountNullLong")
    CountNanLong = field("CountNanLong")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatisticsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetRequest:
    boto3_raw_data: "type_defs.DescribeDatasetRequestTypeDef" = dataclasses.field()

    DatasetArn = field("DatasetArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExplainabilityExportRequest:
    boto3_raw_data: "type_defs.DescribeExplainabilityExportRequestTypeDef" = (
        dataclasses.field()
    )

    ExplainabilityExportArn = field("ExplainabilityExportArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeExplainabilityExportRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExplainabilityExportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExplainabilityRequest:
    boto3_raw_data: "type_defs.DescribeExplainabilityRequestTypeDef" = (
        dataclasses.field()
    )

    ExplainabilityArn = field("ExplainabilityArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeExplainabilityRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExplainabilityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeForecastExportJobRequest:
    boto3_raw_data: "type_defs.DescribeForecastExportJobRequestTypeDef" = (
        dataclasses.field()
    )

    ForecastExportJobArn = field("ForecastExportJobArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeForecastExportJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeForecastExportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeForecastRequest:
    boto3_raw_data: "type_defs.DescribeForecastRequestTypeDef" = dataclasses.field()

    ForecastArn = field("ForecastArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeForecastRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeForecastRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMonitorRequest:
    boto3_raw_data: "type_defs.DescribeMonitorRequestTypeDef" = dataclasses.field()

    MonitorArn = field("MonitorArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMonitorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMonitorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePredictorBacktestExportJobRequest:
    boto3_raw_data: "type_defs.DescribePredictorBacktestExportJobRequestTypeDef" = (
        dataclasses.field()
    )

    PredictorBacktestExportJobArn = field("PredictorBacktestExportJobArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePredictorBacktestExportJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePredictorBacktestExportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePredictorRequest:
    boto3_raw_data: "type_defs.DescribePredictorRequestTypeDef" = dataclasses.field()

    PredictorArn = field("PredictorArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePredictorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePredictorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWhatIfAnalysisRequest:
    boto3_raw_data: "type_defs.DescribeWhatIfAnalysisRequestTypeDef" = (
        dataclasses.field()
    )

    WhatIfAnalysisArn = field("WhatIfAnalysisArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeWhatIfAnalysisRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWhatIfAnalysisRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWhatIfForecastExportRequest:
    boto3_raw_data: "type_defs.DescribeWhatIfForecastExportRequestTypeDef" = (
        dataclasses.field()
    )

    WhatIfForecastExportArn = field("WhatIfForecastExportArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWhatIfForecastExportRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWhatIfForecastExportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWhatIfForecastRequest:
    boto3_raw_data: "type_defs.DescribeWhatIfForecastRequestTypeDef" = (
        dataclasses.field()
    )

    WhatIfForecastArn = field("WhatIfForecastArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeWhatIfForecastRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWhatIfForecastRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorMetric:
    boto3_raw_data: "type_defs.ErrorMetricTypeDef" = dataclasses.field()

    ForecastType = field("ForecastType")
    WAPE = field("WAPE")
    RMSE = field("RMSE")
    MASE = field("MASE")
    MAPE = field("MAPE")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorMetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorMetricTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FeaturizationMethodOutput:
    boto3_raw_data: "type_defs.FeaturizationMethodOutputTypeDef" = dataclasses.field()

    FeaturizationMethodName = field("FeaturizationMethodName")
    FeaturizationMethodParameters = field("FeaturizationMethodParameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FeaturizationMethodOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FeaturizationMethodOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FeaturizationMethod:
    boto3_raw_data: "type_defs.FeaturizationMethodTypeDef" = dataclasses.field()

    FeaturizationMethodName = field("FeaturizationMethodName")
    FeaturizationMethodParameters = field("FeaturizationMethodParameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FeaturizationMethodTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FeaturizationMethodTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filter:
    boto3_raw_data: "type_defs.FilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")
    Condition = field("Condition")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ForecastSummary:
    boto3_raw_data: "type_defs.ForecastSummaryTypeDef" = dataclasses.field()

    ForecastArn = field("ForecastArn")
    ForecastName = field("ForecastName")
    PredictorArn = field("PredictorArn")
    CreatedUsingAutoPredictor = field("CreatedUsingAutoPredictor")
    DatasetGroupArn = field("DatasetGroupArn")
    Status = field("Status")
    Message = field("Message")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ForecastSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ForecastSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccuracyMetricsRequest:
    boto3_raw_data: "type_defs.GetAccuracyMetricsRequestTypeDef" = dataclasses.field()

    PredictorArn = field("PredictorArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccuracyMetricsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccuracyMetricsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SupplementaryFeature:
    boto3_raw_data: "type_defs.SupplementaryFeatureTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SupplementaryFeatureTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SupplementaryFeatureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntegerParameterRange:
    boto3_raw_data: "type_defs.IntegerParameterRangeTypeDef" = dataclasses.field()

    Name = field("Name")
    MaxValue = field("MaxValue")
    MinValue = field("MinValue")
    ScalingType = field("ScalingType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IntegerParameterRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntegerParameterRangeTypeDef"]
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
class ListDatasetGroupsRequest:
    boto3_raw_data: "type_defs.ListDatasetGroupsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetsRequest:
    boto3_raw_data: "type_defs.ListDatasetsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitorSummary:
    boto3_raw_data: "type_defs.MonitorSummaryTypeDef" = dataclasses.field()

    MonitorArn = field("MonitorArn")
    MonitorName = field("MonitorName")
    ResourceArn = field("ResourceArn")
    Status = field("Status")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MonitorSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MonitorSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

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
class WhatIfAnalysisSummary:
    boto3_raw_data: "type_defs.WhatIfAnalysisSummaryTypeDef" = dataclasses.field()

    WhatIfAnalysisArn = field("WhatIfAnalysisArn")
    WhatIfAnalysisName = field("WhatIfAnalysisName")
    ForecastArn = field("ForecastArn")
    Status = field("Status")
    Message = field("Message")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WhatIfAnalysisSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WhatIfAnalysisSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WhatIfForecastSummary:
    boto3_raw_data: "type_defs.WhatIfForecastSummaryTypeDef" = dataclasses.field()

    WhatIfForecastArn = field("WhatIfForecastArn")
    WhatIfForecastName = field("WhatIfForecastName")
    WhatIfAnalysisArn = field("WhatIfAnalysisArn")
    Status = field("Status")
    Message = field("Message")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WhatIfForecastSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WhatIfForecastSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricResult:
    boto3_raw_data: "type_defs.MetricResultTypeDef" = dataclasses.field()

    MetricName = field("MetricName")
    MetricValue = field("MetricValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WeightedQuantileLoss:
    boto3_raw_data: "type_defs.WeightedQuantileLossTypeDef" = dataclasses.field()

    Quantile = field("Quantile")
    LossValue = field("LossValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WeightedQuantileLossTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WeightedQuantileLossTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitorDataSource:
    boto3_raw_data: "type_defs.MonitorDataSourceTypeDef" = dataclasses.field()

    DatasetImportJobArn = field("DatasetImportJobArn")
    ForecastArn = field("ForecastArn")
    PredictorArn = field("PredictorArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MonitorDataSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MonitorDataSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictorEvent:
    boto3_raw_data: "type_defs.PredictorEventTypeDef" = dataclasses.field()

    Detail = field("Detail")
    Datetime = field("Datetime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PredictorEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PredictorEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestWindowSummary:
    boto3_raw_data: "type_defs.TestWindowSummaryTypeDef" = dataclasses.field()

    TestWindowStart = field("TestWindowStart")
    TestWindowEnd = field("TestWindowEnd")
    Status = field("Status")
    Message = field("Message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestWindowSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestWindowSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResumeResourceRequest:
    boto3_raw_data: "type_defs.ResumeResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResumeResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResumeResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaAttribute:
    boto3_raw_data: "type_defs.SchemaAttributeTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")
    AttributeType = field("AttributeType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SchemaAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SchemaAttributeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopResourceRequest:
    boto3_raw_data: "type_defs.StopResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeSeriesCondition:
    boto3_raw_data: "type_defs.TimeSeriesConditionTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")
    AttributeValue = field("AttributeValue")
    Condition = field("Condition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimeSeriesConditionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeSeriesConditionTypeDef"]
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

    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")

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
class UpdateDatasetGroupRequest:
    boto3_raw_data: "type_defs.UpdateDatasetGroupRequestTypeDef" = dataclasses.field()

    DatasetGroupArn = field("DatasetGroupArn")
    DatasetArns = field("DatasetArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDatasetGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDatasetGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataConfigOutput:
    boto3_raw_data: "type_defs.DataConfigOutputTypeDef" = dataclasses.field()

    DatasetGroupArn = field("DatasetGroupArn")

    @cached_property
    def AttributeConfigs(self):  # pragma: no cover
        return AttributeConfigOutput.make_many(self.boto3_raw_data["AttributeConfigs"])

    @cached_property
    def AdditionalDatasets(self):  # pragma: no cover
        return AdditionalDatasetOutput.make_many(
            self.boto3_raw_data["AdditionalDatasets"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataConfigOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataConfig:
    boto3_raw_data: "type_defs.DataConfigTypeDef" = dataclasses.field()

    DatasetGroupArn = field("DatasetGroupArn")

    @cached_property
    def AttributeConfigs(self):  # pragma: no cover
        return AttributeConfig.make_many(self.boto3_raw_data["AttributeConfigs"])

    @cached_property
    def AdditionalDatasets(self):  # pragma: no cover
        return AdditionalDataset.make_many(self.boto3_raw_data["AdditionalDatasets"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictorBaseline:
    boto3_raw_data: "type_defs.PredictorBaselineTypeDef" = dataclasses.field()

    @cached_property
    def BaselineMetrics(self):  # pragma: no cover
        return BaselineMetric.make_many(self.boto3_raw_data["BaselineMetrics"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PredictorBaselineTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictorBaselineTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatasetGroupRequest:
    boto3_raw_data: "type_defs.CreateDatasetGroupRequestTypeDef" = dataclasses.field()

    DatasetGroupName = field("DatasetGroupName")
    Domain = field("Domain")
    DatasetArns = field("DatasetArns")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatasetGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMonitorRequest:
    boto3_raw_data: "type_defs.CreateMonitorRequestTypeDef" = dataclasses.field()

    MonitorName = field("MonitorName")
    ResourceArn = field("ResourceArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMonitorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMonitorRequestTypeDef"]
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

    ResourceArn = field("ResourceArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class CreateAutoPredictorResponse:
    boto3_raw_data: "type_defs.CreateAutoPredictorResponseTypeDef" = dataclasses.field()

    PredictorArn = field("PredictorArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAutoPredictorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAutoPredictorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatasetGroupResponse:
    boto3_raw_data: "type_defs.CreateDatasetGroupResponseTypeDef" = dataclasses.field()

    DatasetGroupArn = field("DatasetGroupArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatasetGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatasetImportJobResponse:
    boto3_raw_data: "type_defs.CreateDatasetImportJobResponseTypeDef" = (
        dataclasses.field()
    )

    DatasetImportJobArn = field("DatasetImportJobArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDatasetImportJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatasetResponse:
    boto3_raw_data: "type_defs.CreateDatasetResponseTypeDef" = dataclasses.field()

    DatasetArn = field("DatasetArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatasetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExplainabilityExportResponse:
    boto3_raw_data: "type_defs.CreateExplainabilityExportResponseTypeDef" = (
        dataclasses.field()
    )

    ExplainabilityExportArn = field("ExplainabilityExportArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateExplainabilityExportResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExplainabilityExportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExplainabilityResponse:
    boto3_raw_data: "type_defs.CreateExplainabilityResponseTypeDef" = (
        dataclasses.field()
    )

    ExplainabilityArn = field("ExplainabilityArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateExplainabilityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExplainabilityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateForecastExportJobResponse:
    boto3_raw_data: "type_defs.CreateForecastExportJobResponseTypeDef" = (
        dataclasses.field()
    )

    ForecastExportJobArn = field("ForecastExportJobArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateForecastExportJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateForecastExportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateForecastResponse:
    boto3_raw_data: "type_defs.CreateForecastResponseTypeDef" = dataclasses.field()

    ForecastArn = field("ForecastArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateForecastResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateForecastResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMonitorResponse:
    boto3_raw_data: "type_defs.CreateMonitorResponseTypeDef" = dataclasses.field()

    MonitorArn = field("MonitorArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMonitorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMonitorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePredictorBacktestExportJobResponse:
    boto3_raw_data: "type_defs.CreatePredictorBacktestExportJobResponseTypeDef" = (
        dataclasses.field()
    )

    PredictorBacktestExportJobArn = field("PredictorBacktestExportJobArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePredictorBacktestExportJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePredictorBacktestExportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePredictorResponse:
    boto3_raw_data: "type_defs.CreatePredictorResponseTypeDef" = dataclasses.field()

    PredictorArn = field("PredictorArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePredictorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePredictorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWhatIfAnalysisResponse:
    boto3_raw_data: "type_defs.CreateWhatIfAnalysisResponseTypeDef" = (
        dataclasses.field()
    )

    WhatIfAnalysisArn = field("WhatIfAnalysisArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWhatIfAnalysisResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWhatIfAnalysisResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWhatIfForecastExportResponse:
    boto3_raw_data: "type_defs.CreateWhatIfForecastExportResponseTypeDef" = (
        dataclasses.field()
    )

    WhatIfForecastExportArn = field("WhatIfForecastExportArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateWhatIfForecastExportResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWhatIfForecastExportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWhatIfForecastResponse:
    boto3_raw_data: "type_defs.CreateWhatIfForecastResponseTypeDef" = (
        dataclasses.field()
    )

    WhatIfForecastArn = field("WhatIfForecastArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWhatIfForecastResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWhatIfForecastResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetGroupResponse:
    boto3_raw_data: "type_defs.DescribeDatasetGroupResponseTypeDef" = (
        dataclasses.field()
    )

    DatasetGroupName = field("DatasetGroupName")
    DatasetGroupArn = field("DatasetGroupArn")
    DatasetArns = field("DatasetArns")
    Domain = field("Domain")
    Status = field("Status")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDatasetGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetGroupResponseTypeDef"]
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
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class ExplainabilitySummary:
    boto3_raw_data: "type_defs.ExplainabilitySummaryTypeDef" = dataclasses.field()

    ExplainabilityArn = field("ExplainabilityArn")
    ExplainabilityName = field("ExplainabilityName")
    ResourceArn = field("ResourceArn")

    @cached_property
    def ExplainabilityConfig(self):  # pragma: no cover
        return ExplainabilityConfig.make_one(
            self.boto3_raw_data["ExplainabilityConfig"]
        )

    Status = field("Status")
    Message = field("Message")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExplainabilitySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExplainabilitySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataDestination:
    boto3_raw_data: "type_defs.DataDestinationTypeDef" = dataclasses.field()

    @cached_property
    def S3Config(self):  # pragma: no cover
        return S3Config.make_one(self.boto3_raw_data["S3Config"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataDestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataDestinationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSource:
    boto3_raw_data: "type_defs.DataSourceTypeDef" = dataclasses.field()

    @cached_property
    def S3Config(self):  # pragma: no cover
        return S3Config.make_one(self.boto3_raw_data["S3Config"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetGroupsResponse:
    boto3_raw_data: "type_defs.ListDatasetGroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def DatasetGroups(self):  # pragma: no cover
        return DatasetGroupSummary.make_many(self.boto3_raw_data["DatasetGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetsResponse:
    boto3_raw_data: "type_defs.ListDatasetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Datasets(self):  # pragma: no cover
        return DatasetSummary.make_many(self.boto3_raw_data["Datasets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictorSummary:
    boto3_raw_data: "type_defs.PredictorSummaryTypeDef" = dataclasses.field()

    PredictorArn = field("PredictorArn")
    PredictorName = field("PredictorName")
    DatasetGroupArn = field("DatasetGroupArn")
    IsAutoPredictor = field("IsAutoPredictor")

    @cached_property
    def ReferencePredictorSummary(self):  # pragma: no cover
        return ReferencePredictorSummary.make_one(
            self.boto3_raw_data["ReferencePredictorSummary"]
        )

    Status = field("Status")
    Message = field("Message")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PredictorSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictorSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FeaturizationOutput:
    boto3_raw_data: "type_defs.FeaturizationOutputTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")

    @cached_property
    def FeaturizationPipeline(self):  # pragma: no cover
        return FeaturizationMethodOutput.make_many(
            self.boto3_raw_data["FeaturizationPipeline"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FeaturizationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FeaturizationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Featurization:
    boto3_raw_data: "type_defs.FeaturizationTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")

    @cached_property
    def FeaturizationPipeline(self):  # pragma: no cover
        return FeaturizationMethod.make_many(
            self.boto3_raw_data["FeaturizationPipeline"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FeaturizationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FeaturizationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetImportJobsRequest:
    boto3_raw_data: "type_defs.ListDatasetImportJobsRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetImportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetImportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExplainabilitiesRequest:
    boto3_raw_data: "type_defs.ListExplainabilitiesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExplainabilitiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExplainabilitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExplainabilityExportsRequest:
    boto3_raw_data: "type_defs.ListExplainabilityExportsRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListExplainabilityExportsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExplainabilityExportsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListForecastExportJobsRequest:
    boto3_raw_data: "type_defs.ListForecastExportJobsRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListForecastExportJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListForecastExportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListForecastsRequest:
    boto3_raw_data: "type_defs.ListForecastsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListForecastsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListForecastsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMonitorEvaluationsRequest:
    boto3_raw_data: "type_defs.ListMonitorEvaluationsRequestTypeDef" = (
        dataclasses.field()
    )

    MonitorArn = field("MonitorArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMonitorEvaluationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMonitorEvaluationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMonitorsRequest:
    boto3_raw_data: "type_defs.ListMonitorsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMonitorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMonitorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPredictorBacktestExportJobsRequest:
    boto3_raw_data: "type_defs.ListPredictorBacktestExportJobsRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPredictorBacktestExportJobsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPredictorBacktestExportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPredictorsRequest:
    boto3_raw_data: "type_defs.ListPredictorsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPredictorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPredictorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWhatIfAnalysesRequest:
    boto3_raw_data: "type_defs.ListWhatIfAnalysesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWhatIfAnalysesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWhatIfAnalysesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWhatIfForecastExportsRequest:
    boto3_raw_data: "type_defs.ListWhatIfForecastExportsRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWhatIfForecastExportsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWhatIfForecastExportsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWhatIfForecastsRequest:
    boto3_raw_data: "type_defs.ListWhatIfForecastsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWhatIfForecastsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWhatIfForecastsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListForecastsResponse:
    boto3_raw_data: "type_defs.ListForecastsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Forecasts(self):  # pragma: no cover
        return ForecastSummary.make_many(self.boto3_raw_data["Forecasts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListForecastsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListForecastsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDataConfigOutput:
    boto3_raw_data: "type_defs.InputDataConfigOutputTypeDef" = dataclasses.field()

    DatasetGroupArn = field("DatasetGroupArn")

    @cached_property
    def SupplementaryFeatures(self):  # pragma: no cover
        return SupplementaryFeature.make_many(
            self.boto3_raw_data["SupplementaryFeatures"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputDataConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputDataConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDataConfig:
    boto3_raw_data: "type_defs.InputDataConfigTypeDef" = dataclasses.field()

    DatasetGroupArn = field("DatasetGroupArn")

    @cached_property
    def SupplementaryFeatures(self):  # pragma: no cover
        return SupplementaryFeature.make_many(
            self.boto3_raw_data["SupplementaryFeatures"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputDataConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputDataConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterRangesOutput:
    boto3_raw_data: "type_defs.ParameterRangesOutputTypeDef" = dataclasses.field()

    @cached_property
    def CategoricalParameterRanges(self):  # pragma: no cover
        return CategoricalParameterRangeOutput.make_many(
            self.boto3_raw_data["CategoricalParameterRanges"]
        )

    @cached_property
    def ContinuousParameterRanges(self):  # pragma: no cover
        return ContinuousParameterRange.make_many(
            self.boto3_raw_data["ContinuousParameterRanges"]
        )

    @cached_property
    def IntegerParameterRanges(self):  # pragma: no cover
        return IntegerParameterRange.make_many(
            self.boto3_raw_data["IntegerParameterRanges"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParameterRangesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParameterRangesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterRanges:
    boto3_raw_data: "type_defs.ParameterRangesTypeDef" = dataclasses.field()

    @cached_property
    def CategoricalParameterRanges(self):  # pragma: no cover
        return CategoricalParameterRange.make_many(
            self.boto3_raw_data["CategoricalParameterRanges"]
        )

    @cached_property
    def ContinuousParameterRanges(self):  # pragma: no cover
        return ContinuousParameterRange.make_many(
            self.boto3_raw_data["ContinuousParameterRanges"]
        )

    @cached_property
    def IntegerParameterRanges(self):  # pragma: no cover
        return IntegerParameterRange.make_many(
            self.boto3_raw_data["IntegerParameterRanges"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParameterRangesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParameterRangesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListDatasetGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDatasetGroupsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetImportJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListDatasetImportJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDatasetImportJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetImportJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetsRequestPaginate:
    boto3_raw_data: "type_defs.ListDatasetsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExplainabilitiesRequestPaginate:
    boto3_raw_data: "type_defs.ListExplainabilitiesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListExplainabilitiesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExplainabilitiesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExplainabilityExportsRequestPaginate:
    boto3_raw_data: "type_defs.ListExplainabilityExportsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListExplainabilityExportsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExplainabilityExportsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListForecastExportJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListForecastExportJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListForecastExportJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListForecastExportJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListForecastsRequestPaginate:
    boto3_raw_data: "type_defs.ListForecastsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListForecastsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListForecastsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMonitorEvaluationsRequestPaginate:
    boto3_raw_data: "type_defs.ListMonitorEvaluationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    MonitorArn = field("MonitorArn")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMonitorEvaluationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMonitorEvaluationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMonitorsRequestPaginate:
    boto3_raw_data: "type_defs.ListMonitorsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMonitorsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMonitorsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPredictorBacktestExportJobsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListPredictorBacktestExportJobsRequestPaginateTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPredictorBacktestExportJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListPredictorBacktestExportJobsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPredictorsRequestPaginate:
    boto3_raw_data: "type_defs.ListPredictorsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPredictorsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPredictorsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWhatIfAnalysesRequestPaginate:
    boto3_raw_data: "type_defs.ListWhatIfAnalysesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWhatIfAnalysesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWhatIfAnalysesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWhatIfForecastExportsRequestPaginate:
    boto3_raw_data: "type_defs.ListWhatIfForecastExportsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWhatIfForecastExportsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWhatIfForecastExportsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWhatIfForecastsRequestPaginate:
    boto3_raw_data: "type_defs.ListWhatIfForecastsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWhatIfForecastsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWhatIfForecastsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMonitorsResponse:
    boto3_raw_data: "type_defs.ListMonitorsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Monitors(self):  # pragma: no cover
        return MonitorSummary.make_many(self.boto3_raw_data["Monitors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMonitorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMonitorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWhatIfAnalysesResponse:
    boto3_raw_data: "type_defs.ListWhatIfAnalysesResponseTypeDef" = dataclasses.field()

    @cached_property
    def WhatIfAnalyses(self):  # pragma: no cover
        return WhatIfAnalysisSummary.make_many(self.boto3_raw_data["WhatIfAnalyses"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWhatIfAnalysesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWhatIfAnalysesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWhatIfForecastsResponse:
    boto3_raw_data: "type_defs.ListWhatIfForecastsResponseTypeDef" = dataclasses.field()

    @cached_property
    def WhatIfForecasts(self):  # pragma: no cover
        return WhatIfForecastSummary.make_many(self.boto3_raw_data["WhatIfForecasts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWhatIfForecastsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWhatIfForecastsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Metrics:
    boto3_raw_data: "type_defs.MetricsTypeDef" = dataclasses.field()

    RMSE = field("RMSE")

    @cached_property
    def WeightedQuantileLosses(self):  # pragma: no cover
        return WeightedQuantileLoss.make_many(
            self.boto3_raw_data["WeightedQuantileLosses"]
        )

    @cached_property
    def ErrorMetrics(self):  # pragma: no cover
        return ErrorMetric.make_many(self.boto3_raw_data["ErrorMetrics"])

    AverageWeightedQuantileLoss = field("AverageWeightedQuantileLoss")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictorMonitorEvaluation:
    boto3_raw_data: "type_defs.PredictorMonitorEvaluationTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    MonitorArn = field("MonitorArn")
    EvaluationTime = field("EvaluationTime")
    EvaluationState = field("EvaluationState")
    WindowStartDatetime = field("WindowStartDatetime")
    WindowEndDatetime = field("WindowEndDatetime")

    @cached_property
    def PredictorEvent(self):  # pragma: no cover
        return PredictorEvent.make_one(self.boto3_raw_data["PredictorEvent"])

    @cached_property
    def MonitorDataSource(self):  # pragma: no cover
        return MonitorDataSource.make_one(self.boto3_raw_data["MonitorDataSource"])

    @cached_property
    def MetricResults(self):  # pragma: no cover
        return MetricResult.make_many(self.boto3_raw_data["MetricResults"])

    NumItemsEvaluated = field("NumItemsEvaluated")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PredictorMonitorEvaluationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictorMonitorEvaluationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictorExecution:
    boto3_raw_data: "type_defs.PredictorExecutionTypeDef" = dataclasses.field()

    AlgorithmArn = field("AlgorithmArn")

    @cached_property
    def TestWindows(self):  # pragma: no cover
        return TestWindowSummary.make_many(self.boto3_raw_data["TestWindows"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PredictorExecutionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictorExecutionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaOutput:
    boto3_raw_data: "type_defs.SchemaOutputTypeDef" = dataclasses.field()

    @cached_property
    def Attributes(self):  # pragma: no cover
        return SchemaAttribute.make_many(self.boto3_raw_data["Attributes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SchemaOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SchemaOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Schema:
    boto3_raw_data: "type_defs.SchemaTypeDef" = dataclasses.field()

    @cached_property
    def Attributes(self):  # pragma: no cover
        return SchemaAttribute.make_many(self.boto3_raw_data["Attributes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SchemaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SchemaTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeSeriesTransformationOutput:
    boto3_raw_data: "type_defs.TimeSeriesTransformationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Action(self):  # pragma: no cover
        return Action.make_one(self.boto3_raw_data["Action"])

    @cached_property
    def TimeSeriesConditions(self):  # pragma: no cover
        return TimeSeriesCondition.make_many(
            self.boto3_raw_data["TimeSeriesConditions"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TimeSeriesTransformationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeSeriesTransformationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeSeriesTransformation:
    boto3_raw_data: "type_defs.TimeSeriesTransformationTypeDef" = dataclasses.field()

    @cached_property
    def Action(self):  # pragma: no cover
        return Action.make_one(self.boto3_raw_data["Action"])

    @cached_property
    def TimeSeriesConditions(self):  # pragma: no cover
        return TimeSeriesCondition.make_many(
            self.boto3_raw_data["TimeSeriesConditions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimeSeriesTransformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeSeriesTransformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAutoPredictorResponse:
    boto3_raw_data: "type_defs.DescribeAutoPredictorResponseTypeDef" = (
        dataclasses.field()
    )

    PredictorArn = field("PredictorArn")
    PredictorName = field("PredictorName")
    ForecastHorizon = field("ForecastHorizon")
    ForecastTypes = field("ForecastTypes")
    ForecastFrequency = field("ForecastFrequency")
    ForecastDimensions = field("ForecastDimensions")
    DatasetImportJobArns = field("DatasetImportJobArns")

    @cached_property
    def DataConfig(self):  # pragma: no cover
        return DataConfigOutput.make_one(self.boto3_raw_data["DataConfig"])

    @cached_property
    def EncryptionConfig(self):  # pragma: no cover
        return EncryptionConfig.make_one(self.boto3_raw_data["EncryptionConfig"])

    @cached_property
    def ReferencePredictorSummary(self):  # pragma: no cover
        return ReferencePredictorSummary.make_one(
            self.boto3_raw_data["ReferencePredictorSummary"]
        )

    EstimatedTimeRemainingInMinutes = field("EstimatedTimeRemainingInMinutes")
    Status = field("Status")
    Message = field("Message")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")
    OptimizationMetric = field("OptimizationMetric")

    @cached_property
    def ExplainabilityInfo(self):  # pragma: no cover
        return ExplainabilityInfo.make_one(self.boto3_raw_data["ExplainabilityInfo"])

    @cached_property
    def MonitorInfo(self):  # pragma: no cover
        return MonitorInfo.make_one(self.boto3_raw_data["MonitorInfo"])

    @cached_property
    def TimeAlignmentBoundary(self):  # pragma: no cover
        return TimeAlignmentBoundary.make_one(
            self.boto3_raw_data["TimeAlignmentBoundary"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAutoPredictorResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAutoPredictorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Baseline:
    boto3_raw_data: "type_defs.BaselineTypeDef" = dataclasses.field()

    @cached_property
    def PredictorBaseline(self):  # pragma: no cover
        return PredictorBaseline.make_one(self.boto3_raw_data["PredictorBaseline"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BaselineTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BaselineTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExplainabilitiesResponse:
    boto3_raw_data: "type_defs.ListExplainabilitiesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Explainabilities(self):  # pragma: no cover
        return ExplainabilitySummary.make_many(self.boto3_raw_data["Explainabilities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExplainabilitiesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExplainabilitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExplainabilityExportRequest:
    boto3_raw_data: "type_defs.CreateExplainabilityExportRequestTypeDef" = (
        dataclasses.field()
    )

    ExplainabilityExportName = field("ExplainabilityExportName")
    ExplainabilityArn = field("ExplainabilityArn")

    @cached_property
    def Destination(self):  # pragma: no cover
        return DataDestination.make_one(self.boto3_raw_data["Destination"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    Format = field("Format")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateExplainabilityExportRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExplainabilityExportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateForecastExportJobRequest:
    boto3_raw_data: "type_defs.CreateForecastExportJobRequestTypeDef" = (
        dataclasses.field()
    )

    ForecastExportJobName = field("ForecastExportJobName")
    ForecastArn = field("ForecastArn")

    @cached_property
    def Destination(self):  # pragma: no cover
        return DataDestination.make_one(self.boto3_raw_data["Destination"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    Format = field("Format")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateForecastExportJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateForecastExportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePredictorBacktestExportJobRequest:
    boto3_raw_data: "type_defs.CreatePredictorBacktestExportJobRequestTypeDef" = (
        dataclasses.field()
    )

    PredictorBacktestExportJobName = field("PredictorBacktestExportJobName")
    PredictorArn = field("PredictorArn")

    @cached_property
    def Destination(self):  # pragma: no cover
        return DataDestination.make_one(self.boto3_raw_data["Destination"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    Format = field("Format")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePredictorBacktestExportJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePredictorBacktestExportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWhatIfForecastExportRequest:
    boto3_raw_data: "type_defs.CreateWhatIfForecastExportRequestTypeDef" = (
        dataclasses.field()
    )

    WhatIfForecastExportName = field("WhatIfForecastExportName")
    WhatIfForecastArns = field("WhatIfForecastArns")

    @cached_property
    def Destination(self):  # pragma: no cover
        return DataDestination.make_one(self.boto3_raw_data["Destination"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    Format = field("Format")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateWhatIfForecastExportRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWhatIfForecastExportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExplainabilityExportResponse:
    boto3_raw_data: "type_defs.DescribeExplainabilityExportResponseTypeDef" = (
        dataclasses.field()
    )

    ExplainabilityExportArn = field("ExplainabilityExportArn")
    ExplainabilityExportName = field("ExplainabilityExportName")
    ExplainabilityArn = field("ExplainabilityArn")

    @cached_property
    def Destination(self):  # pragma: no cover
        return DataDestination.make_one(self.boto3_raw_data["Destination"])

    Message = field("Message")
    Status = field("Status")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")
    Format = field("Format")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeExplainabilityExportResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExplainabilityExportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeForecastExportJobResponse:
    boto3_raw_data: "type_defs.DescribeForecastExportJobResponseTypeDef" = (
        dataclasses.field()
    )

    ForecastExportJobArn = field("ForecastExportJobArn")
    ForecastExportJobName = field("ForecastExportJobName")
    ForecastArn = field("ForecastArn")

    @cached_property
    def Destination(self):  # pragma: no cover
        return DataDestination.make_one(self.boto3_raw_data["Destination"])

    Message = field("Message")
    Status = field("Status")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")
    Format = field("Format")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeForecastExportJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeForecastExportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePredictorBacktestExportJobResponse:
    boto3_raw_data: "type_defs.DescribePredictorBacktestExportJobResponseTypeDef" = (
        dataclasses.field()
    )

    PredictorBacktestExportJobArn = field("PredictorBacktestExportJobArn")
    PredictorBacktestExportJobName = field("PredictorBacktestExportJobName")
    PredictorArn = field("PredictorArn")

    @cached_property
    def Destination(self):  # pragma: no cover
        return DataDestination.make_one(self.boto3_raw_data["Destination"])

    Message = field("Message")
    Status = field("Status")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")
    Format = field("Format")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePredictorBacktestExportJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePredictorBacktestExportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWhatIfForecastExportResponse:
    boto3_raw_data: "type_defs.DescribeWhatIfForecastExportResponseTypeDef" = (
        dataclasses.field()
    )

    WhatIfForecastExportArn = field("WhatIfForecastExportArn")
    WhatIfForecastExportName = field("WhatIfForecastExportName")
    WhatIfForecastArns = field("WhatIfForecastArns")

    @cached_property
    def Destination(self):  # pragma: no cover
        return DataDestination.make_one(self.boto3_raw_data["Destination"])

    Message = field("Message")
    Status = field("Status")
    CreationTime = field("CreationTime")
    EstimatedTimeRemainingInMinutes = field("EstimatedTimeRemainingInMinutes")
    LastModificationTime = field("LastModificationTime")
    Format = field("Format")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWhatIfForecastExportResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWhatIfForecastExportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExplainabilityExportSummary:
    boto3_raw_data: "type_defs.ExplainabilityExportSummaryTypeDef" = dataclasses.field()

    ExplainabilityExportArn = field("ExplainabilityExportArn")
    ExplainabilityExportName = field("ExplainabilityExportName")

    @cached_property
    def Destination(self):  # pragma: no cover
        return DataDestination.make_one(self.boto3_raw_data["Destination"])

    Status = field("Status")
    Message = field("Message")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExplainabilityExportSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExplainabilityExportSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ForecastExportJobSummary:
    boto3_raw_data: "type_defs.ForecastExportJobSummaryTypeDef" = dataclasses.field()

    ForecastExportJobArn = field("ForecastExportJobArn")
    ForecastExportJobName = field("ForecastExportJobName")

    @cached_property
    def Destination(self):  # pragma: no cover
        return DataDestination.make_one(self.boto3_raw_data["Destination"])

    Status = field("Status")
    Message = field("Message")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ForecastExportJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ForecastExportJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictorBacktestExportJobSummary:
    boto3_raw_data: "type_defs.PredictorBacktestExportJobSummaryTypeDef" = (
        dataclasses.field()
    )

    PredictorBacktestExportJobArn = field("PredictorBacktestExportJobArn")
    PredictorBacktestExportJobName = field("PredictorBacktestExportJobName")

    @cached_property
    def Destination(self):  # pragma: no cover
        return DataDestination.make_one(self.boto3_raw_data["Destination"])

    Status = field("Status")
    Message = field("Message")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictorBacktestExportJobSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictorBacktestExportJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WhatIfForecastExportSummary:
    boto3_raw_data: "type_defs.WhatIfForecastExportSummaryTypeDef" = dataclasses.field()

    WhatIfForecastExportArn = field("WhatIfForecastExportArn")
    WhatIfForecastArns = field("WhatIfForecastArns")
    WhatIfForecastExportName = field("WhatIfForecastExportName")

    @cached_property
    def Destination(self):  # pragma: no cover
        return DataDestination.make_one(self.boto3_raw_data["Destination"])

    Status = field("Status")
    Message = field("Message")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WhatIfForecastExportSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WhatIfForecastExportSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatasetImportJobRequest:
    boto3_raw_data: "type_defs.CreateDatasetImportJobRequestTypeDef" = (
        dataclasses.field()
    )

    DatasetImportJobName = field("DatasetImportJobName")
    DatasetArn = field("DatasetArn")

    @cached_property
    def DataSource(self):  # pragma: no cover
        return DataSource.make_one(self.boto3_raw_data["DataSource"])

    TimestampFormat = field("TimestampFormat")
    TimeZone = field("TimeZone")
    UseGeolocationForTimeZone = field("UseGeolocationForTimeZone")
    GeolocationFormat = field("GeolocationFormat")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    Format = field("Format")
    ImportMode = field("ImportMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDatasetImportJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetImportJobSummary:
    boto3_raw_data: "type_defs.DatasetImportJobSummaryTypeDef" = dataclasses.field()

    DatasetImportJobArn = field("DatasetImportJobArn")
    DatasetImportJobName = field("DatasetImportJobName")

    @cached_property
    def DataSource(self):  # pragma: no cover
        return DataSource.make_one(self.boto3_raw_data["DataSource"])

    Status = field("Status")
    Message = field("Message")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")
    ImportMode = field("ImportMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasetImportJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetImportJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetImportJobResponse:
    boto3_raw_data: "type_defs.DescribeDatasetImportJobResponseTypeDef" = (
        dataclasses.field()
    )

    DatasetImportJobName = field("DatasetImportJobName")
    DatasetImportJobArn = field("DatasetImportJobArn")
    DatasetArn = field("DatasetArn")
    TimestampFormat = field("TimestampFormat")
    TimeZone = field("TimeZone")
    UseGeolocationForTimeZone = field("UseGeolocationForTimeZone")
    GeolocationFormat = field("GeolocationFormat")

    @cached_property
    def DataSource(self):  # pragma: no cover
        return DataSource.make_one(self.boto3_raw_data["DataSource"])

    EstimatedTimeRemainingInMinutes = field("EstimatedTimeRemainingInMinutes")
    FieldStatistics = field("FieldStatistics")
    DataSize = field("DataSize")
    Status = field("Status")
    Message = field("Message")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")
    Format = field("Format")
    ImportMode = field("ImportMode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDatasetImportJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPredictorsResponse:
    boto3_raw_data: "type_defs.ListPredictorsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Predictors(self):  # pragma: no cover
        return PredictorSummary.make_many(self.boto3_raw_data["Predictors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPredictorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPredictorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FeaturizationConfigOutput:
    boto3_raw_data: "type_defs.FeaturizationConfigOutputTypeDef" = dataclasses.field()

    ForecastFrequency = field("ForecastFrequency")
    ForecastDimensions = field("ForecastDimensions")

    @cached_property
    def Featurizations(self):  # pragma: no cover
        return FeaturizationOutput.make_many(self.boto3_raw_data["Featurizations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FeaturizationConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FeaturizationConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FeaturizationConfig:
    boto3_raw_data: "type_defs.FeaturizationConfigTypeDef" = dataclasses.field()

    ForecastFrequency = field("ForecastFrequency")
    ForecastDimensions = field("ForecastDimensions")

    @cached_property
    def Featurizations(self):  # pragma: no cover
        return Featurization.make_many(self.boto3_raw_data["Featurizations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FeaturizationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FeaturizationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HyperParameterTuningJobConfigOutput:
    boto3_raw_data: "type_defs.HyperParameterTuningJobConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ParameterRanges(self):  # pragma: no cover
        return ParameterRangesOutput.make_one(self.boto3_raw_data["ParameterRanges"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.HyperParameterTuningJobConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HyperParameterTuningJobConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HyperParameterTuningJobConfig:
    boto3_raw_data: "type_defs.HyperParameterTuningJobConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ParameterRanges(self):  # pragma: no cover
        return ParameterRanges.make_one(self.boto3_raw_data["ParameterRanges"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.HyperParameterTuningJobConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HyperParameterTuningJobConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WindowSummary:
    boto3_raw_data: "type_defs.WindowSummaryTypeDef" = dataclasses.field()

    TestWindowStart = field("TestWindowStart")
    TestWindowEnd = field("TestWindowEnd")
    ItemCount = field("ItemCount")
    EvaluationType = field("EvaluationType")

    @cached_property
    def Metrics(self):  # pragma: no cover
        return Metrics.make_one(self.boto3_raw_data["Metrics"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WindowSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WindowSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMonitorEvaluationsResponse:
    boto3_raw_data: "type_defs.ListMonitorEvaluationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PredictorMonitorEvaluations(self):  # pragma: no cover
        return PredictorMonitorEvaluation.make_many(
            self.boto3_raw_data["PredictorMonitorEvaluations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMonitorEvaluationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMonitorEvaluationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictorExecutionDetails:
    boto3_raw_data: "type_defs.PredictorExecutionDetailsTypeDef" = dataclasses.field()

    @cached_property
    def PredictorExecutions(self):  # pragma: no cover
        return PredictorExecution.make_many(self.boto3_raw_data["PredictorExecutions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PredictorExecutionDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictorExecutionDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetResponse:
    boto3_raw_data: "type_defs.DescribeDatasetResponseTypeDef" = dataclasses.field()

    DatasetArn = field("DatasetArn")
    DatasetName = field("DatasetName")
    Domain = field("Domain")
    DatasetType = field("DatasetType")
    DataFrequency = field("DataFrequency")

    @cached_property
    def Schema(self):  # pragma: no cover
        return SchemaOutput.make_one(self.boto3_raw_data["Schema"])

    @cached_property
    def EncryptionConfig(self):  # pragma: no cover
        return EncryptionConfig.make_one(self.boto3_raw_data["EncryptionConfig"])

    Status = field("Status")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDatasetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExplainabilityResponse:
    boto3_raw_data: "type_defs.DescribeExplainabilityResponseTypeDef" = (
        dataclasses.field()
    )

    ExplainabilityArn = field("ExplainabilityArn")
    ExplainabilityName = field("ExplainabilityName")
    ResourceArn = field("ResourceArn")

    @cached_property
    def ExplainabilityConfig(self):  # pragma: no cover
        return ExplainabilityConfig.make_one(
            self.boto3_raw_data["ExplainabilityConfig"]
        )

    EnableVisualization = field("EnableVisualization")

    @cached_property
    def DataSource(self):  # pragma: no cover
        return DataSource.make_one(self.boto3_raw_data["DataSource"])

    @cached_property
    def Schema(self):  # pragma: no cover
        return SchemaOutput.make_one(self.boto3_raw_data["Schema"])

    StartDateTime = field("StartDateTime")
    EndDateTime = field("EndDateTime")
    EstimatedTimeRemainingInMinutes = field("EstimatedTimeRemainingInMinutes")
    Message = field("Message")
    Status = field("Status")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeExplainabilityResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExplainabilityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeSeriesIdentifiersOutput:
    boto3_raw_data: "type_defs.TimeSeriesIdentifiersOutputTypeDef" = dataclasses.field()

    @cached_property
    def DataSource(self):  # pragma: no cover
        return DataSource.make_one(self.boto3_raw_data["DataSource"])

    @cached_property
    def Schema(self):  # pragma: no cover
        return SchemaOutput.make_one(self.boto3_raw_data["Schema"])

    Format = field("Format")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimeSeriesIdentifiersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeSeriesIdentifiersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeSeriesReplacementsDataSourceOutput:
    boto3_raw_data: "type_defs.TimeSeriesReplacementsDataSourceOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def S3Config(self):  # pragma: no cover
        return S3Config.make_one(self.boto3_raw_data["S3Config"])

    @cached_property
    def Schema(self):  # pragma: no cover
        return SchemaOutput.make_one(self.boto3_raw_data["Schema"])

    Format = field("Format")
    TimestampFormat = field("TimestampFormat")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TimeSeriesReplacementsDataSourceOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeSeriesReplacementsDataSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeSeriesIdentifiers:
    boto3_raw_data: "type_defs.TimeSeriesIdentifiersTypeDef" = dataclasses.field()

    @cached_property
    def DataSource(self):  # pragma: no cover
        return DataSource.make_one(self.boto3_raw_data["DataSource"])

    @cached_property
    def Schema(self):  # pragma: no cover
        return Schema.make_one(self.boto3_raw_data["Schema"])

    Format = field("Format")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimeSeriesIdentifiersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeSeriesIdentifiersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeSeriesReplacementsDataSource:
    boto3_raw_data: "type_defs.TimeSeriesReplacementsDataSourceTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def S3Config(self):  # pragma: no cover
        return S3Config.make_one(self.boto3_raw_data["S3Config"])

    @cached_property
    def Schema(self):  # pragma: no cover
        return Schema.make_one(self.boto3_raw_data["Schema"])

    Format = field("Format")
    TimestampFormat = field("TimestampFormat")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TimeSeriesReplacementsDataSourceTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeSeriesReplacementsDataSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAutoPredictorRequest:
    boto3_raw_data: "type_defs.CreateAutoPredictorRequestTypeDef" = dataclasses.field()

    PredictorName = field("PredictorName")
    ForecastHorizon = field("ForecastHorizon")
    ForecastTypes = field("ForecastTypes")
    ForecastDimensions = field("ForecastDimensions")
    ForecastFrequency = field("ForecastFrequency")
    DataConfig = field("DataConfig")

    @cached_property
    def EncryptionConfig(self):  # pragma: no cover
        return EncryptionConfig.make_one(self.boto3_raw_data["EncryptionConfig"])

    ReferencePredictorArn = field("ReferencePredictorArn")
    OptimizationMetric = field("OptimizationMetric")
    ExplainPredictor = field("ExplainPredictor")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def MonitorConfig(self):  # pragma: no cover
        return MonitorConfig.make_one(self.boto3_raw_data["MonitorConfig"])

    @cached_property
    def TimeAlignmentBoundary(self):  # pragma: no cover
        return TimeAlignmentBoundary.make_one(
            self.boto3_raw_data["TimeAlignmentBoundary"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAutoPredictorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAutoPredictorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMonitorResponse:
    boto3_raw_data: "type_defs.DescribeMonitorResponseTypeDef" = dataclasses.field()

    MonitorName = field("MonitorName")
    MonitorArn = field("MonitorArn")
    ResourceArn = field("ResourceArn")
    Status = field("Status")
    LastEvaluationTime = field("LastEvaluationTime")
    LastEvaluationState = field("LastEvaluationState")

    @cached_property
    def Baseline(self):  # pragma: no cover
        return Baseline.make_one(self.boto3_raw_data["Baseline"])

    Message = field("Message")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")
    EstimatedEvaluationTimeRemainingInMinutes = field(
        "EstimatedEvaluationTimeRemainingInMinutes"
    )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMonitorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMonitorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExplainabilityExportsResponse:
    boto3_raw_data: "type_defs.ListExplainabilityExportsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ExplainabilityExports(self):  # pragma: no cover
        return ExplainabilityExportSummary.make_many(
            self.boto3_raw_data["ExplainabilityExports"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListExplainabilityExportsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExplainabilityExportsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListForecastExportJobsResponse:
    boto3_raw_data: "type_defs.ListForecastExportJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ForecastExportJobs(self):  # pragma: no cover
        return ForecastExportJobSummary.make_many(
            self.boto3_raw_data["ForecastExportJobs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListForecastExportJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListForecastExportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPredictorBacktestExportJobsResponse:
    boto3_raw_data: "type_defs.ListPredictorBacktestExportJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PredictorBacktestExportJobs(self):  # pragma: no cover
        return PredictorBacktestExportJobSummary.make_many(
            self.boto3_raw_data["PredictorBacktestExportJobs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPredictorBacktestExportJobsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPredictorBacktestExportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWhatIfForecastExportsResponse:
    boto3_raw_data: "type_defs.ListWhatIfForecastExportsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def WhatIfForecastExports(self):  # pragma: no cover
        return WhatIfForecastExportSummary.make_many(
            self.boto3_raw_data["WhatIfForecastExports"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWhatIfForecastExportsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWhatIfForecastExportsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetImportJobsResponse:
    boto3_raw_data: "type_defs.ListDatasetImportJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DatasetImportJobs(self):  # pragma: no cover
        return DatasetImportJobSummary.make_many(
            self.boto3_raw_data["DatasetImportJobs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDatasetImportJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetImportJobsResponseTypeDef"]
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

    AlgorithmArn = field("AlgorithmArn")

    @cached_property
    def TestWindows(self):  # pragma: no cover
        return WindowSummary.make_many(self.boto3_raw_data["TestWindows"])

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
class DescribePredictorResponse:
    boto3_raw_data: "type_defs.DescribePredictorResponseTypeDef" = dataclasses.field()

    PredictorArn = field("PredictorArn")
    PredictorName = field("PredictorName")
    AlgorithmArn = field("AlgorithmArn")
    AutoMLAlgorithmArns = field("AutoMLAlgorithmArns")
    ForecastHorizon = field("ForecastHorizon")
    ForecastTypes = field("ForecastTypes")
    PerformAutoML = field("PerformAutoML")
    AutoMLOverrideStrategy = field("AutoMLOverrideStrategy")
    PerformHPO = field("PerformHPO")
    TrainingParameters = field("TrainingParameters")

    @cached_property
    def EvaluationParameters(self):  # pragma: no cover
        return EvaluationParameters.make_one(
            self.boto3_raw_data["EvaluationParameters"]
        )

    @cached_property
    def HPOConfig(self):  # pragma: no cover
        return HyperParameterTuningJobConfigOutput.make_one(
            self.boto3_raw_data["HPOConfig"]
        )

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfigOutput.make_one(self.boto3_raw_data["InputDataConfig"])

    @cached_property
    def FeaturizationConfig(self):  # pragma: no cover
        return FeaturizationConfigOutput.make_one(
            self.boto3_raw_data["FeaturizationConfig"]
        )

    @cached_property
    def EncryptionConfig(self):  # pragma: no cover
        return EncryptionConfig.make_one(self.boto3_raw_data["EncryptionConfig"])

    @cached_property
    def PredictorExecutionDetails(self):  # pragma: no cover
        return PredictorExecutionDetails.make_one(
            self.boto3_raw_data["PredictorExecutionDetails"]
        )

    EstimatedTimeRemainingInMinutes = field("EstimatedTimeRemainingInMinutes")
    IsAutoPredictor = field("IsAutoPredictor")
    DatasetImportJobArns = field("DatasetImportJobArns")
    Status = field("Status")
    Message = field("Message")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")
    OptimizationMetric = field("OptimizationMetric")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePredictorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePredictorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeSeriesSelectorOutput:
    boto3_raw_data: "type_defs.TimeSeriesSelectorOutputTypeDef" = dataclasses.field()

    @cached_property
    def TimeSeriesIdentifiers(self):  # pragma: no cover
        return TimeSeriesIdentifiersOutput.make_one(
            self.boto3_raw_data["TimeSeriesIdentifiers"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimeSeriesSelectorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeSeriesSelectorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWhatIfForecastResponse:
    boto3_raw_data: "type_defs.DescribeWhatIfForecastResponseTypeDef" = (
        dataclasses.field()
    )

    WhatIfForecastName = field("WhatIfForecastName")
    WhatIfForecastArn = field("WhatIfForecastArn")
    WhatIfAnalysisArn = field("WhatIfAnalysisArn")
    EstimatedTimeRemainingInMinutes = field("EstimatedTimeRemainingInMinutes")
    Status = field("Status")
    Message = field("Message")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")

    @cached_property
    def TimeSeriesTransformations(self):  # pragma: no cover
        return TimeSeriesTransformationOutput.make_many(
            self.boto3_raw_data["TimeSeriesTransformations"]
        )

    @cached_property
    def TimeSeriesReplacementsDataSource(self):  # pragma: no cover
        return TimeSeriesReplacementsDataSourceOutput.make_one(
            self.boto3_raw_data["TimeSeriesReplacementsDataSource"]
        )

    ForecastTypes = field("ForecastTypes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeWhatIfForecastResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWhatIfForecastResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatasetRequest:
    boto3_raw_data: "type_defs.CreateDatasetRequestTypeDef" = dataclasses.field()

    DatasetName = field("DatasetName")
    Domain = field("Domain")
    DatasetType = field("DatasetType")
    Schema = field("Schema")
    DataFrequency = field("DataFrequency")

    @cached_property
    def EncryptionConfig(self):  # pragma: no cover
        return EncryptionConfig.make_one(self.boto3_raw_data["EncryptionConfig"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExplainabilityRequest:
    boto3_raw_data: "type_defs.CreateExplainabilityRequestTypeDef" = dataclasses.field()

    ExplainabilityName = field("ExplainabilityName")
    ResourceArn = field("ResourceArn")

    @cached_property
    def ExplainabilityConfig(self):  # pragma: no cover
        return ExplainabilityConfig.make_one(
            self.boto3_raw_data["ExplainabilityConfig"]
        )

    @cached_property
    def DataSource(self):  # pragma: no cover
        return DataSource.make_one(self.boto3_raw_data["DataSource"])

    Schema = field("Schema")
    EnableVisualization = field("EnableVisualization")
    StartDateTime = field("StartDateTime")
    EndDateTime = field("EndDateTime")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateExplainabilityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExplainabilityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeSeriesSelector:
    boto3_raw_data: "type_defs.TimeSeriesSelectorTypeDef" = dataclasses.field()

    @cached_property
    def TimeSeriesIdentifiers(self):  # pragma: no cover
        return TimeSeriesIdentifiers.make_one(
            self.boto3_raw_data["TimeSeriesIdentifiers"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimeSeriesSelectorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeSeriesSelectorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePredictorRequest:
    boto3_raw_data: "type_defs.CreatePredictorRequestTypeDef" = dataclasses.field()

    PredictorName = field("PredictorName")
    ForecastHorizon = field("ForecastHorizon")
    InputDataConfig = field("InputDataConfig")
    FeaturizationConfig = field("FeaturizationConfig")
    AlgorithmArn = field("AlgorithmArn")
    ForecastTypes = field("ForecastTypes")
    PerformAutoML = field("PerformAutoML")
    AutoMLOverrideStrategy = field("AutoMLOverrideStrategy")
    PerformHPO = field("PerformHPO")
    TrainingParameters = field("TrainingParameters")

    @cached_property
    def EvaluationParameters(self):  # pragma: no cover
        return EvaluationParameters.make_one(
            self.boto3_raw_data["EvaluationParameters"]
        )

    HPOConfig = field("HPOConfig")

    @cached_property
    def EncryptionConfig(self):  # pragma: no cover
        return EncryptionConfig.make_one(self.boto3_raw_data["EncryptionConfig"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    OptimizationMetric = field("OptimizationMetric")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePredictorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePredictorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccuracyMetricsResponse:
    boto3_raw_data: "type_defs.GetAccuracyMetricsResponseTypeDef" = dataclasses.field()

    @cached_property
    def PredictorEvaluationResults(self):  # pragma: no cover
        return EvaluationResult.make_many(
            self.boto3_raw_data["PredictorEvaluationResults"]
        )

    IsAutoPredictor = field("IsAutoPredictor")
    AutoMLOverrideStrategy = field("AutoMLOverrideStrategy")
    OptimizationMetric = field("OptimizationMetric")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccuracyMetricsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccuracyMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeForecastResponse:
    boto3_raw_data: "type_defs.DescribeForecastResponseTypeDef" = dataclasses.field()

    ForecastArn = field("ForecastArn")
    ForecastName = field("ForecastName")
    ForecastTypes = field("ForecastTypes")
    PredictorArn = field("PredictorArn")
    DatasetGroupArn = field("DatasetGroupArn")
    EstimatedTimeRemainingInMinutes = field("EstimatedTimeRemainingInMinutes")
    Status = field("Status")
    Message = field("Message")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")

    @cached_property
    def TimeSeriesSelector(self):  # pragma: no cover
        return TimeSeriesSelectorOutput.make_one(
            self.boto3_raw_data["TimeSeriesSelector"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeForecastResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeForecastResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWhatIfAnalysisResponse:
    boto3_raw_data: "type_defs.DescribeWhatIfAnalysisResponseTypeDef" = (
        dataclasses.field()
    )

    WhatIfAnalysisName = field("WhatIfAnalysisName")
    WhatIfAnalysisArn = field("WhatIfAnalysisArn")
    ForecastArn = field("ForecastArn")
    EstimatedTimeRemainingInMinutes = field("EstimatedTimeRemainingInMinutes")
    Status = field("Status")
    Message = field("Message")
    CreationTime = field("CreationTime")
    LastModificationTime = field("LastModificationTime")

    @cached_property
    def TimeSeriesSelector(self):  # pragma: no cover
        return TimeSeriesSelectorOutput.make_one(
            self.boto3_raw_data["TimeSeriesSelector"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeWhatIfAnalysisResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWhatIfAnalysisResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWhatIfForecastRequest:
    boto3_raw_data: "type_defs.CreateWhatIfForecastRequestTypeDef" = dataclasses.field()

    WhatIfForecastName = field("WhatIfForecastName")
    WhatIfAnalysisArn = field("WhatIfAnalysisArn")
    TimeSeriesTransformations = field("TimeSeriesTransformations")
    TimeSeriesReplacementsDataSource = field("TimeSeriesReplacementsDataSource")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWhatIfForecastRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWhatIfForecastRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateForecastRequest:
    boto3_raw_data: "type_defs.CreateForecastRequestTypeDef" = dataclasses.field()

    ForecastName = field("ForecastName")
    PredictorArn = field("PredictorArn")
    ForecastTypes = field("ForecastTypes")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    TimeSeriesSelector = field("TimeSeriesSelector")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateForecastRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateForecastRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWhatIfAnalysisRequest:
    boto3_raw_data: "type_defs.CreateWhatIfAnalysisRequestTypeDef" = dataclasses.field()

    WhatIfAnalysisName = field("WhatIfAnalysisName")
    ForecastArn = field("ForecastArn")
    TimeSeriesSelector = field("TimeSeriesSelector")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWhatIfAnalysisRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWhatIfAnalysisRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
