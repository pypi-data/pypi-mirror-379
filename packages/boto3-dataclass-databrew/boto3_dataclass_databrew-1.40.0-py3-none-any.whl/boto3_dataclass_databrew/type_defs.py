# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_databrew import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AllowedStatisticsOutput:
    boto3_raw_data: "type_defs.AllowedStatisticsOutputTypeDef" = dataclasses.field()

    Statistics = field("Statistics")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AllowedStatisticsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AllowedStatisticsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllowedStatistics:
    boto3_raw_data: "type_defs.AllowedStatisticsTypeDef" = dataclasses.field()

    Statistics = field("Statistics")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AllowedStatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AllowedStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteRecipeVersionRequest:
    boto3_raw_data: "type_defs.BatchDeleteRecipeVersionRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    RecipeVersions = field("RecipeVersions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchDeleteRecipeVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteRecipeVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecipeVersionErrorDetail:
    boto3_raw_data: "type_defs.RecipeVersionErrorDetailTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")
    RecipeVersion = field("RecipeVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecipeVersionErrorDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecipeVersionErrorDetailTypeDef"]
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
class ColumnSelector:
    boto3_raw_data: "type_defs.ColumnSelectorTypeDef" = dataclasses.field()

    Regex = field("Regex")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ColumnSelectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ColumnSelectorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionExpression:
    boto3_raw_data: "type_defs.ConditionExpressionTypeDef" = dataclasses.field()

    Condition = field("Condition")
    TargetColumn = field("TargetColumn")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConditionExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConditionExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobSample:
    boto3_raw_data: "type_defs.JobSampleTypeDef" = dataclasses.field()

    Mode = field("Mode")
    Size = field("Size")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobSampleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobSampleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Location:
    boto3_raw_data: "type_defs.S3LocationTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    BucketOwner = field("BucketOwner")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3LocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3LocationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidationConfiguration:
    boto3_raw_data: "type_defs.ValidationConfigurationTypeDef" = dataclasses.field()

    RulesetArn = field("RulesetArn")
    ValidationMode = field("ValidationMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValidationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Sample:
    boto3_raw_data: "type_defs.SampleTypeDef" = dataclasses.field()

    Type = field("Type")
    Size = field("Size")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SampleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SampleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecipeReference:
    boto3_raw_data: "type_defs.RecipeReferenceTypeDef" = dataclasses.field()

    Name = field("Name")
    RecipeVersion = field("RecipeVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecipeReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecipeReferenceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateScheduleRequest:
    boto3_raw_data: "type_defs.CreateScheduleRequestTypeDef" = dataclasses.field()

    CronExpression = field("CronExpression")
    Name = field("Name")
    JobNames = field("JobNames")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateScheduleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateScheduleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CsvOptions:
    boto3_raw_data: "type_defs.CsvOptionsTypeDef" = dataclasses.field()

    Delimiter = field("Delimiter")
    HeaderRow = field("HeaderRow")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CsvOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CsvOptionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CsvOutputOptions:
    boto3_raw_data: "type_defs.CsvOutputOptionsTypeDef" = dataclasses.field()

    Delimiter = field("Delimiter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CsvOutputOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CsvOutputOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatetimeOptions:
    boto3_raw_data: "type_defs.DatetimeOptionsTypeDef" = dataclasses.field()

    Format = field("Format")
    TimezoneOffset = field("TimezoneOffset")
    LocaleCode = field("LocaleCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatetimeOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatetimeOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterExpressionOutput:
    boto3_raw_data: "type_defs.FilterExpressionOutputTypeDef" = dataclasses.field()

    Expression = field("Expression")
    ValuesMap = field("ValuesMap")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FilterExpressionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterExpressionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterExpression:
    boto3_raw_data: "type_defs.FilterExpressionTypeDef" = dataclasses.field()

    Expression = field("Expression")
    ValuesMap = field("ValuesMap")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterExpressionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterExpressionTypeDef"]
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

    Name = field("Name")

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
class DeleteJobRequest:
    boto3_raw_data: "type_defs.DeleteJobRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteJobRequestTypeDef"]
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

    Name = field("Name")

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
class DeleteRecipeVersionRequest:
    boto3_raw_data: "type_defs.DeleteRecipeVersionRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    RecipeVersion = field("RecipeVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRecipeVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRecipeVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRulesetRequest:
    boto3_raw_data: "type_defs.DeleteRulesetRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRulesetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRulesetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteScheduleRequest:
    boto3_raw_data: "type_defs.DeleteScheduleRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteScheduleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteScheduleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetRequest:
    boto3_raw_data: "type_defs.DescribeDatasetRequestTypeDef" = dataclasses.field()

    Name = field("Name")

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
class DescribeJobRequest:
    boto3_raw_data: "type_defs.DescribeJobRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobRunRequest:
    boto3_raw_data: "type_defs.DescribeJobRunRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    RunId = field("RunId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobRunRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobRunRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProjectRequest:
    boto3_raw_data: "type_defs.DescribeProjectRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeProjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecipeRequest:
    boto3_raw_data: "type_defs.DescribeRecipeRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    RecipeVersion = field("RecipeVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRecipeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecipeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRulesetRequest:
    boto3_raw_data: "type_defs.DescribeRulesetRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRulesetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRulesetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScheduleRequest:
    boto3_raw_data: "type_defs.DescribeScheduleRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeScheduleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScheduleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExcelOptionsOutput:
    boto3_raw_data: "type_defs.ExcelOptionsOutputTypeDef" = dataclasses.field()

    SheetNames = field("SheetNames")
    SheetIndexes = field("SheetIndexes")
    HeaderRow = field("HeaderRow")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExcelOptionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExcelOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExcelOptions:
    boto3_raw_data: "type_defs.ExcelOptionsTypeDef" = dataclasses.field()

    SheetNames = field("SheetNames")
    SheetIndexes = field("SheetIndexes")
    HeaderRow = field("HeaderRow")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExcelOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExcelOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilesLimit:
    boto3_raw_data: "type_defs.FilesLimitTypeDef" = dataclasses.field()

    MaxFiles = field("MaxFiles")
    OrderedBy = field("OrderedBy")
    Order = field("Order")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilesLimitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilesLimitTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JsonOptions:
    boto3_raw_data: "type_defs.JsonOptionsTypeDef" = dataclasses.field()

    MultiLine = field("MultiLine")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JsonOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JsonOptionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Metadata:
    boto3_raw_data: "type_defs.MetadataTypeDef" = dataclasses.field()

    SourceArn = field("SourceArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetadataTypeDef"]]
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
class ListDatasetsRequest:
    boto3_raw_data: "type_defs.ListDatasetsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

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
class ListJobRunsRequest:
    boto3_raw_data: "type_defs.ListJobRunsRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobRunsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobRunsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsRequest:
    boto3_raw_data: "type_defs.ListJobsRequestTypeDef" = dataclasses.field()

    DatasetName = field("DatasetName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    ProjectName = field("ProjectName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListJobsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListJobsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectsRequest:
    boto3_raw_data: "type_defs.ListProjectsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

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
class ListRecipeVersionsRequest:
    boto3_raw_data: "type_defs.ListRecipeVersionsRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecipeVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecipeVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecipesRequest:
    boto3_raw_data: "type_defs.ListRecipesRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    RecipeVersion = field("RecipeVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecipesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecipesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRulesetsRequest:
    boto3_raw_data: "type_defs.ListRulesetsRequestTypeDef" = dataclasses.field()

    TargetArn = field("TargetArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRulesetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRulesetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RulesetItem:
    boto3_raw_data: "type_defs.RulesetItemTypeDef" = dataclasses.field()

    Name = field("Name")
    TargetArn = field("TargetArn")
    AccountId = field("AccountId")
    CreatedBy = field("CreatedBy")
    CreateDate = field("CreateDate")
    Description = field("Description")
    LastModifiedBy = field("LastModifiedBy")
    LastModifiedDate = field("LastModifiedDate")
    ResourceArn = field("ResourceArn")
    RuleCount = field("RuleCount")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RulesetItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RulesetItemTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSchedulesRequest:
    boto3_raw_data: "type_defs.ListSchedulesRequestTypeDef" = dataclasses.field()

    JobName = field("JobName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSchedulesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchedulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Schedule:
    boto3_raw_data: "type_defs.ScheduleTypeDef" = dataclasses.field()

    Name = field("Name")
    AccountId = field("AccountId")
    CreatedBy = field("CreatedBy")
    CreateDate = field("CreateDate")
    JobNames = field("JobNames")
    LastModifiedBy = field("LastModifiedBy")
    LastModifiedDate = field("LastModifiedDate")
    ResourceArn = field("ResourceArn")
    CronExpression = field("CronExpression")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduleTypeDef"]]
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
class PublishRecipeRequest:
    boto3_raw_data: "type_defs.PublishRecipeRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PublishRecipeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublishRecipeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecipeActionOutput:
    boto3_raw_data: "type_defs.RecipeActionOutputTypeDef" = dataclasses.field()

    Operation = field("Operation")
    Parameters = field("Parameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecipeActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecipeActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecipeAction:
    boto3_raw_data: "type_defs.RecipeActionTypeDef" = dataclasses.field()

    Operation = field("Operation")
    Parameters = field("Parameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecipeActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecipeActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Threshold:
    boto3_raw_data: "type_defs.ThresholdTypeDef" = dataclasses.field()

    Value = field("Value")
    Type = field("Type")
    Unit = field("Unit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThresholdTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ThresholdTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ViewFrame:
    boto3_raw_data: "type_defs.ViewFrameTypeDef" = dataclasses.field()

    StartColumnIndex = field("StartColumnIndex")
    ColumnRange = field("ColumnRange")
    HiddenColumns = field("HiddenColumns")
    StartRowIndex = field("StartRowIndex")
    RowRange = field("RowRange")
    Analytics = field("Analytics")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ViewFrameTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ViewFrameTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartJobRunRequest:
    boto3_raw_data: "type_defs.StartJobRunRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartJobRunRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartJobRunRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartProjectSessionRequest:
    boto3_raw_data: "type_defs.StartProjectSessionRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    AssumeControl = field("AssumeControl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartProjectSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartProjectSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatisticOverrideOutput:
    boto3_raw_data: "type_defs.StatisticOverrideOutputTypeDef" = dataclasses.field()

    Statistic = field("Statistic")
    Parameters = field("Parameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StatisticOverrideOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StatisticOverrideOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatisticOverride:
    boto3_raw_data: "type_defs.StatisticOverrideTypeDef" = dataclasses.field()

    Statistic = field("Statistic")
    Parameters = field("Parameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatisticOverrideTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StatisticOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopJobRunRequest:
    boto3_raw_data: "type_defs.StopJobRunRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    RunId = field("RunId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopJobRunRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopJobRunRequestTypeDef"]
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
    Tags = field("Tags")

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
class UpdateScheduleRequest:
    boto3_raw_data: "type_defs.UpdateScheduleRequestTypeDef" = dataclasses.field()

    CronExpression = field("CronExpression")
    Name = field("Name")
    JobNames = field("JobNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateScheduleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateScheduleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityDetectorConfigurationOutput:
    boto3_raw_data: "type_defs.EntityDetectorConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    EntityTypes = field("EntityTypes")

    @cached_property
    def AllowedStatistics(self):  # pragma: no cover
        return AllowedStatisticsOutput.make_many(
            self.boto3_raw_data["AllowedStatistics"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EntityDetectorConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityDetectorConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityDetectorConfiguration:
    boto3_raw_data: "type_defs.EntityDetectorConfigurationTypeDef" = dataclasses.field()

    EntityTypes = field("EntityTypes")

    @cached_property
    def AllowedStatistics(self):  # pragma: no cover
        return AllowedStatistics.make_many(self.boto3_raw_data["AllowedStatistics"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EntityDetectorConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityDetectorConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteRecipeVersionResponse:
    boto3_raw_data: "type_defs.BatchDeleteRecipeVersionResponseTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @cached_property
    def Errors(self):  # pragma: no cover
        return RecipeVersionErrorDetail.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchDeleteRecipeVersionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteRecipeVersionResponseTypeDef"]
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

    Name = field("Name")

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
class CreateProfileJobResponse:
    boto3_raw_data: "type_defs.CreateProfileJobResponseTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProfileJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProfileJobResponseTypeDef"]
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

    Name = field("Name")

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
class CreateRecipeJobResponse:
    boto3_raw_data: "type_defs.CreateRecipeJobResponseTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRecipeJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRecipeJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRecipeResponse:
    boto3_raw_data: "type_defs.CreateRecipeResponseTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRecipeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRecipeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRulesetResponse:
    boto3_raw_data: "type_defs.CreateRulesetResponseTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRulesetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRulesetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateScheduleResponse:
    boto3_raw_data: "type_defs.CreateScheduleResponseTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateScheduleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateScheduleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDatasetResponse:
    boto3_raw_data: "type_defs.DeleteDatasetResponseTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDatasetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteJobResponse:
    boto3_raw_data: "type_defs.DeleteJobResponseTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteJobResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProjectResponse:
    boto3_raw_data: "type_defs.DeleteProjectResponseTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProjectResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRecipeVersionResponse:
    boto3_raw_data: "type_defs.DeleteRecipeVersionResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    RecipeVersion = field("RecipeVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRecipeVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRecipeVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRulesetResponse:
    boto3_raw_data: "type_defs.DeleteRulesetResponseTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRulesetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRulesetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteScheduleResponse:
    boto3_raw_data: "type_defs.DeleteScheduleResponseTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteScheduleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteScheduleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScheduleResponse:
    boto3_raw_data: "type_defs.DescribeScheduleResponseTypeDef" = dataclasses.field()

    CreateDate = field("CreateDate")
    CreatedBy = field("CreatedBy")
    JobNames = field("JobNames")
    LastModifiedBy = field("LastModifiedBy")
    LastModifiedDate = field("LastModifiedDate")
    ResourceArn = field("ResourceArn")
    CronExpression = field("CronExpression")
    Tags = field("Tags")
    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeScheduleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScheduleResponseTypeDef"]
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

    Tags = field("Tags")

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
class PublishRecipeResponse:
    boto3_raw_data: "type_defs.PublishRecipeResponseTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PublishRecipeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublishRecipeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendProjectSessionActionResponse:
    boto3_raw_data: "type_defs.SendProjectSessionActionResponseTypeDef" = (
        dataclasses.field()
    )

    Result = field("Result")
    Name = field("Name")
    ActionId = field("ActionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SendProjectSessionActionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendProjectSessionActionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartJobRunResponse:
    boto3_raw_data: "type_defs.StartJobRunResponseTypeDef" = dataclasses.field()

    RunId = field("RunId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartJobRunResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartJobRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartProjectSessionResponse:
    boto3_raw_data: "type_defs.StartProjectSessionResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    ClientSessionId = field("ClientSessionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartProjectSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartProjectSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopJobRunResponse:
    boto3_raw_data: "type_defs.StopJobRunResponseTypeDef" = dataclasses.field()

    RunId = field("RunId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopJobRunResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopJobRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDatasetResponse:
    boto3_raw_data: "type_defs.UpdateDatasetResponseTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDatasetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProfileJobResponse:
    boto3_raw_data: "type_defs.UpdateProfileJobResponseTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProfileJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProfileJobResponseTypeDef"]
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

    LastModifiedDate = field("LastModifiedDate")
    Name = field("Name")

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
class UpdateRecipeJobResponse:
    boto3_raw_data: "type_defs.UpdateRecipeJobResponseTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRecipeJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRecipeJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRecipeResponse:
    boto3_raw_data: "type_defs.UpdateRecipeResponseTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRecipeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRecipeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRulesetResponse:
    boto3_raw_data: "type_defs.UpdateRulesetResponseTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRulesetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRulesetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateScheduleResponse:
    boto3_raw_data: "type_defs.UpdateScheduleResponseTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateScheduleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateScheduleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataCatalogInputDefinition:
    boto3_raw_data: "type_defs.DataCatalogInputDefinitionTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")
    TableName = field("TableName")
    CatalogId = field("CatalogId")

    @cached_property
    def TempDirectory(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["TempDirectory"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataCatalogInputDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataCatalogInputDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseInputDefinition:
    boto3_raw_data: "type_defs.DatabaseInputDefinitionTypeDef" = dataclasses.field()

    GlueConnectionName = field("GlueConnectionName")
    DatabaseTableName = field("DatabaseTableName")

    @cached_property
    def TempDirectory(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["TempDirectory"])

    QueryString = field("QueryString")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatabaseInputDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseInputDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseTableOutputOptions:
    boto3_raw_data: "type_defs.DatabaseTableOutputOptionsTypeDef" = dataclasses.field()

    TableName = field("TableName")

    @cached_property
    def TempDirectory(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["TempDirectory"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatabaseTableOutputOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseTableOutputOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3TableOutputOptions:
    boto3_raw_data: "type_defs.S3TableOutputOptionsTypeDef" = dataclasses.field()

    @cached_property
    def Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["Location"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3TableOutputOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3TableOutputOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProjectRequest:
    boto3_raw_data: "type_defs.CreateProjectRequestTypeDef" = dataclasses.field()

    DatasetName = field("DatasetName")
    Name = field("Name")
    RecipeName = field("RecipeName")
    RoleArn = field("RoleArn")

    @cached_property
    def Sample(self):  # pragma: no cover
        return Sample.make_one(self.boto3_raw_data["Sample"])

    Tags = field("Tags")

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
class DescribeProjectResponse:
    boto3_raw_data: "type_defs.DescribeProjectResponseTypeDef" = dataclasses.field()

    CreateDate = field("CreateDate")
    CreatedBy = field("CreatedBy")
    DatasetName = field("DatasetName")
    LastModifiedDate = field("LastModifiedDate")
    LastModifiedBy = field("LastModifiedBy")
    Name = field("Name")
    RecipeName = field("RecipeName")
    ResourceArn = field("ResourceArn")

    @cached_property
    def Sample(self):  # pragma: no cover
        return Sample.make_one(self.boto3_raw_data["Sample"])

    RoleArn = field("RoleArn")
    Tags = field("Tags")
    SessionStatus = field("SessionStatus")
    OpenedBy = field("OpenedBy")
    OpenDate = field("OpenDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeProjectResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProjectResponseTypeDef"]
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

    Name = field("Name")
    RecipeName = field("RecipeName")
    AccountId = field("AccountId")
    CreateDate = field("CreateDate")
    CreatedBy = field("CreatedBy")
    DatasetName = field("DatasetName")
    LastModifiedDate = field("LastModifiedDate")
    LastModifiedBy = field("LastModifiedBy")
    ResourceArn = field("ResourceArn")

    @cached_property
    def Sample(self):  # pragma: no cover
        return Sample.make_one(self.boto3_raw_data["Sample"])

    Tags = field("Tags")
    RoleArn = field("RoleArn")
    OpenedBy = field("OpenedBy")
    OpenDate = field("OpenDate")

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
class UpdateProjectRequest:
    boto3_raw_data: "type_defs.UpdateProjectRequestTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")
    Name = field("Name")

    @cached_property
    def Sample(self):  # pragma: no cover
        return Sample.make_one(self.boto3_raw_data["Sample"])

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
class OutputFormatOptions:
    boto3_raw_data: "type_defs.OutputFormatOptionsTypeDef" = dataclasses.field()

    @cached_property
    def Csv(self):  # pragma: no cover
        return CsvOutputOptions.make_one(self.boto3_raw_data["Csv"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutputFormatOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputFormatOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetParameterOutput:
    boto3_raw_data: "type_defs.DatasetParameterOutputTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")

    @cached_property
    def DatetimeOptions(self):  # pragma: no cover
        return DatetimeOptions.make_one(self.boto3_raw_data["DatetimeOptions"])

    CreateColumn = field("CreateColumn")

    @cached_property
    def Filter(self):  # pragma: no cover
        return FilterExpressionOutput.make_one(self.boto3_raw_data["Filter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasetParameterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetParameterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetParameter:
    boto3_raw_data: "type_defs.DatasetParameterTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")

    @cached_property
    def DatetimeOptions(self):  # pragma: no cover
        return DatetimeOptions.make_one(self.boto3_raw_data["DatetimeOptions"])

    CreateColumn = field("CreateColumn")

    @cached_property
    def Filter(self):  # pragma: no cover
        return FilterExpression.make_one(self.boto3_raw_data["Filter"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormatOptionsOutput:
    boto3_raw_data: "type_defs.FormatOptionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Json(self):  # pragma: no cover
        return JsonOptions.make_one(self.boto3_raw_data["Json"])

    @cached_property
    def Excel(self):  # pragma: no cover
        return ExcelOptionsOutput.make_one(self.boto3_raw_data["Excel"])

    @cached_property
    def Csv(self):  # pragma: no cover
        return CsvOptions.make_one(self.boto3_raw_data["Csv"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FormatOptionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FormatOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormatOptions:
    boto3_raw_data: "type_defs.FormatOptionsTypeDef" = dataclasses.field()

    @cached_property
    def Json(self):  # pragma: no cover
        return JsonOptions.make_one(self.boto3_raw_data["Json"])

    @cached_property
    def Excel(self):  # pragma: no cover
        return ExcelOptions.make_one(self.boto3_raw_data["Excel"])

    @cached_property
    def Csv(self):  # pragma: no cover
        return CsvOptions.make_one(self.boto3_raw_data["Csv"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FormatOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FormatOptionsTypeDef"]],
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
class ListJobRunsRequestPaginate:
    boto3_raw_data: "type_defs.ListJobRunsRequestPaginateTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobRunsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobRunsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListJobsRequestPaginateTypeDef" = dataclasses.field()

    DatasetName = field("DatasetName")
    ProjectName = field("ProjectName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsRequestPaginateTypeDef"]
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
class ListRecipeVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListRecipeVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecipeVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecipeVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecipesRequestPaginate:
    boto3_raw_data: "type_defs.ListRecipesRequestPaginateTypeDef" = dataclasses.field()

    RecipeVersion = field("RecipeVersion")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecipesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecipesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRulesetsRequestPaginate:
    boto3_raw_data: "type_defs.ListRulesetsRequestPaginateTypeDef" = dataclasses.field()

    TargetArn = field("TargetArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRulesetsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRulesetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSchedulesRequestPaginate:
    boto3_raw_data: "type_defs.ListSchedulesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    JobName = field("JobName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSchedulesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchedulesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRulesetsResponse:
    boto3_raw_data: "type_defs.ListRulesetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Rulesets(self):  # pragma: no cover
        return RulesetItem.make_many(self.boto3_raw_data["Rulesets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRulesetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRulesetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSchedulesResponse:
    boto3_raw_data: "type_defs.ListSchedulesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Schedules(self):  # pragma: no cover
        return Schedule.make_many(self.boto3_raw_data["Schedules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSchedulesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchedulesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecipeStepOutput:
    boto3_raw_data: "type_defs.RecipeStepOutputTypeDef" = dataclasses.field()

    @cached_property
    def Action(self):  # pragma: no cover
        return RecipeActionOutput.make_one(self.boto3_raw_data["Action"])

    @cached_property
    def ConditionExpressions(self):  # pragma: no cover
        return ConditionExpression.make_many(
            self.boto3_raw_data["ConditionExpressions"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecipeStepOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecipeStepOutputTypeDef"]
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

    Name = field("Name")
    CheckExpression = field("CheckExpression")
    Disabled = field("Disabled")
    SubstitutionMap = field("SubstitutionMap")

    @cached_property
    def Threshold(self):  # pragma: no cover
        return Threshold.make_one(self.boto3_raw_data["Threshold"])

    @cached_property
    def ColumnSelectors(self):  # pragma: no cover
        return ColumnSelector.make_many(self.boto3_raw_data["ColumnSelectors"])

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

    Name = field("Name")
    CheckExpression = field("CheckExpression")
    Disabled = field("Disabled")
    SubstitutionMap = field("SubstitutionMap")

    @cached_property
    def Threshold(self):  # pragma: no cover
        return Threshold.make_one(self.boto3_raw_data["Threshold"])

    @cached_property
    def ColumnSelectors(self):  # pragma: no cover
        return ColumnSelector.make_many(self.boto3_raw_data["ColumnSelectors"])

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
class StatisticsConfigurationOutput:
    boto3_raw_data: "type_defs.StatisticsConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    IncludedStatistics = field("IncludedStatistics")

    @cached_property
    def Overrides(self):  # pragma: no cover
        return StatisticOverrideOutput.make_many(self.boto3_raw_data["Overrides"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StatisticsConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StatisticsConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatisticsConfiguration:
    boto3_raw_data: "type_defs.StatisticsConfigurationTypeDef" = dataclasses.field()

    IncludedStatistics = field("IncludedStatistics")

    @cached_property
    def Overrides(self):  # pragma: no cover
        return StatisticOverride.make_many(self.boto3_raw_data["Overrides"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StatisticsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StatisticsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Input:
    boto3_raw_data: "type_defs.InputTypeDef" = dataclasses.field()

    @cached_property
    def S3InputDefinition(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["S3InputDefinition"])

    @cached_property
    def DataCatalogInputDefinition(self):  # pragma: no cover
        return DataCatalogInputDefinition.make_one(
            self.boto3_raw_data["DataCatalogInputDefinition"]
        )

    @cached_property
    def DatabaseInputDefinition(self):  # pragma: no cover
        return DatabaseInputDefinition.make_one(
            self.boto3_raw_data["DatabaseInputDefinition"]
        )

    @cached_property
    def Metadata(self):  # pragma: no cover
        return Metadata.make_one(self.boto3_raw_data["Metadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseOutput:
    boto3_raw_data: "type_defs.DatabaseOutputTypeDef" = dataclasses.field()

    GlueConnectionName = field("GlueConnectionName")

    @cached_property
    def DatabaseOptions(self):  # pragma: no cover
        return DatabaseTableOutputOptions.make_one(
            self.boto3_raw_data["DatabaseOptions"]
        )

    DatabaseOutputMode = field("DatabaseOutputMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatabaseOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatabaseOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataCatalogOutput:
    boto3_raw_data: "type_defs.DataCatalogOutputTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")
    TableName = field("TableName")
    CatalogId = field("CatalogId")

    @cached_property
    def S3Options(self):  # pragma: no cover
        return S3TableOutputOptions.make_one(self.boto3_raw_data["S3Options"])

    @cached_property
    def DatabaseOptions(self):  # pragma: no cover
        return DatabaseTableOutputOptions.make_one(
            self.boto3_raw_data["DatabaseOptions"]
        )

    Overwrite = field("Overwrite")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataCatalogOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataCatalogOutputTypeDef"]
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
    def Projects(self):  # pragma: no cover
        return Project.make_many(self.boto3_raw_data["Projects"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

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
class Extra:
    boto3_raw_data: "type_defs.ExtraTypeDef" = dataclasses.field()

    @cached_property
    def Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["Location"])

    CompressionFormat = field("CompressionFormat")
    Format = field("Format")
    PartitionColumns = field("PartitionColumns")
    Overwrite = field("Overwrite")

    @cached_property
    def FormatOptions(self):  # pragma: no cover
        return OutputFormatOptions.make_one(self.boto3_raw_data["FormatOptions"])

    MaxOutputFiles = field("MaxOutputFiles")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExtraTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExtraTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Output:
    boto3_raw_data: "type_defs.OutputTypeDef" = dataclasses.field()

    @cached_property
    def Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["Location"])

    CompressionFormat = field("CompressionFormat")
    Format = field("Format")
    PartitionColumns = field("PartitionColumns")
    Overwrite = field("Overwrite")

    @cached_property
    def FormatOptions(self):  # pragma: no cover
        return OutputFormatOptions.make_one(self.boto3_raw_data["FormatOptions"])

    MaxOutputFiles = field("MaxOutputFiles")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PathOptionsOutput:
    boto3_raw_data: "type_defs.PathOptionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def LastModifiedDateCondition(self):  # pragma: no cover
        return FilterExpressionOutput.make_one(
            self.boto3_raw_data["LastModifiedDateCondition"]
        )

    @cached_property
    def FilesLimit(self):  # pragma: no cover
        return FilesLimit.make_one(self.boto3_raw_data["FilesLimit"])

    Parameters = field("Parameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PathOptionsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PathOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PathOptions:
    boto3_raw_data: "type_defs.PathOptionsTypeDef" = dataclasses.field()

    @cached_property
    def LastModifiedDateCondition(self):  # pragma: no cover
        return FilterExpression.make_one(
            self.boto3_raw_data["LastModifiedDateCondition"]
        )

    @cached_property
    def FilesLimit(self):  # pragma: no cover
        return FilesLimit.make_one(self.boto3_raw_data["FilesLimit"])

    Parameters = field("Parameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PathOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PathOptionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecipeResponse:
    boto3_raw_data: "type_defs.DescribeRecipeResponseTypeDef" = dataclasses.field()

    CreatedBy = field("CreatedBy")
    CreateDate = field("CreateDate")
    LastModifiedBy = field("LastModifiedBy")
    LastModifiedDate = field("LastModifiedDate")
    ProjectName = field("ProjectName")
    PublishedBy = field("PublishedBy")
    PublishedDate = field("PublishedDate")
    Description = field("Description")
    Name = field("Name")

    @cached_property
    def Steps(self):  # pragma: no cover
        return RecipeStepOutput.make_many(self.boto3_raw_data["Steps"])

    Tags = field("Tags")
    ResourceArn = field("ResourceArn")
    RecipeVersion = field("RecipeVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRecipeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecipeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Recipe:
    boto3_raw_data: "type_defs.RecipeTypeDef" = dataclasses.field()

    Name = field("Name")
    CreatedBy = field("CreatedBy")
    CreateDate = field("CreateDate")
    LastModifiedBy = field("LastModifiedBy")
    LastModifiedDate = field("LastModifiedDate")
    ProjectName = field("ProjectName")
    PublishedBy = field("PublishedBy")
    PublishedDate = field("PublishedDate")
    Description = field("Description")
    ResourceArn = field("ResourceArn")

    @cached_property
    def Steps(self):  # pragma: no cover
        return RecipeStepOutput.make_many(self.boto3_raw_data["Steps"])

    Tags = field("Tags")
    RecipeVersion = field("RecipeVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecipeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecipeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecipeStep:
    boto3_raw_data: "type_defs.RecipeStepTypeDef" = dataclasses.field()

    Action = field("Action")

    @cached_property
    def ConditionExpressions(self):  # pragma: no cover
        return ConditionExpression.make_many(
            self.boto3_raw_data["ConditionExpressions"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecipeStepTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecipeStepTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRulesetResponse:
    boto3_raw_data: "type_defs.DescribeRulesetResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    TargetArn = field("TargetArn")

    @cached_property
    def Rules(self):  # pragma: no cover
        return RuleOutput.make_many(self.boto3_raw_data["Rules"])

    CreateDate = field("CreateDate")
    CreatedBy = field("CreatedBy")
    LastModifiedBy = field("LastModifiedBy")
    LastModifiedDate = field("LastModifiedDate")
    ResourceArn = field("ResourceArn")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRulesetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRulesetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColumnStatisticsConfigurationOutput:
    boto3_raw_data: "type_defs.ColumnStatisticsConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Statistics(self):  # pragma: no cover
        return StatisticsConfigurationOutput.make_one(self.boto3_raw_data["Statistics"])

    @cached_property
    def Selectors(self):  # pragma: no cover
        return ColumnSelector.make_many(self.boto3_raw_data["Selectors"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ColumnStatisticsConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ColumnStatisticsConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColumnStatisticsConfiguration:
    boto3_raw_data: "type_defs.ColumnStatisticsConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Statistics(self):  # pragma: no cover
        return StatisticsConfiguration.make_one(self.boto3_raw_data["Statistics"])

    @cached_property
    def Selectors(self):  # pragma: no cover
        return ColumnSelector.make_many(self.boto3_raw_data["Selectors"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ColumnStatisticsConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ColumnStatisticsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobRun:
    boto3_raw_data: "type_defs.JobRunTypeDef" = dataclasses.field()

    Attempt = field("Attempt")
    CompletedOn = field("CompletedOn")
    DatasetName = field("DatasetName")
    ErrorMessage = field("ErrorMessage")
    ExecutionTime = field("ExecutionTime")
    JobName = field("JobName")
    RunId = field("RunId")
    State = field("State")
    LogSubscription = field("LogSubscription")
    LogGroupName = field("LogGroupName")

    @cached_property
    def Outputs(self):  # pragma: no cover
        return Extra.make_many(self.boto3_raw_data["Outputs"])

    @cached_property
    def DataCatalogOutputs(self):  # pragma: no cover
        return DataCatalogOutput.make_many(self.boto3_raw_data["DataCatalogOutputs"])

    @cached_property
    def DatabaseOutputs(self):  # pragma: no cover
        return DatabaseOutput.make_many(self.boto3_raw_data["DatabaseOutputs"])

    @cached_property
    def RecipeReference(self):  # pragma: no cover
        return RecipeReference.make_one(self.boto3_raw_data["RecipeReference"])

    StartedBy = field("StartedBy")
    StartedOn = field("StartedOn")

    @cached_property
    def JobSample(self):  # pragma: no cover
        return JobSample.make_one(self.boto3_raw_data["JobSample"])

    @cached_property
    def ValidationConfigurations(self):  # pragma: no cover
        return ValidationConfiguration.make_many(
            self.boto3_raw_data["ValidationConfigurations"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobRunTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobRunTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Job:
    boto3_raw_data: "type_defs.JobTypeDef" = dataclasses.field()

    Name = field("Name")
    AccountId = field("AccountId")
    CreatedBy = field("CreatedBy")
    CreateDate = field("CreateDate")
    DatasetName = field("DatasetName")
    EncryptionKeyArn = field("EncryptionKeyArn")
    EncryptionMode = field("EncryptionMode")
    Type = field("Type")
    LastModifiedBy = field("LastModifiedBy")
    LastModifiedDate = field("LastModifiedDate")
    LogSubscription = field("LogSubscription")
    MaxCapacity = field("MaxCapacity")
    MaxRetries = field("MaxRetries")

    @cached_property
    def Outputs(self):  # pragma: no cover
        return Extra.make_many(self.boto3_raw_data["Outputs"])

    @cached_property
    def DataCatalogOutputs(self):  # pragma: no cover
        return DataCatalogOutput.make_many(self.boto3_raw_data["DataCatalogOutputs"])

    @cached_property
    def DatabaseOutputs(self):  # pragma: no cover
        return DatabaseOutput.make_many(self.boto3_raw_data["DatabaseOutputs"])

    ProjectName = field("ProjectName")

    @cached_property
    def RecipeReference(self):  # pragma: no cover
        return RecipeReference.make_one(self.boto3_raw_data["RecipeReference"])

    ResourceArn = field("ResourceArn")
    RoleArn = field("RoleArn")
    Timeout = field("Timeout")
    Tags = field("Tags")

    @cached_property
    def JobSample(self):  # pragma: no cover
        return JobSample.make_one(self.boto3_raw_data["JobSample"])

    @cached_property
    def ValidationConfigurations(self):  # pragma: no cover
        return ValidationConfiguration.make_many(
            self.boto3_raw_data["ValidationConfigurations"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Dataset:
    boto3_raw_data: "type_defs.DatasetTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Input(self):  # pragma: no cover
        return Input.make_one(self.boto3_raw_data["Input"])

    AccountId = field("AccountId")
    CreatedBy = field("CreatedBy")
    CreateDate = field("CreateDate")
    Format = field("Format")

    @cached_property
    def FormatOptions(self):  # pragma: no cover
        return FormatOptionsOutput.make_one(self.boto3_raw_data["FormatOptions"])

    LastModifiedDate = field("LastModifiedDate")
    LastModifiedBy = field("LastModifiedBy")
    Source = field("Source")

    @cached_property
    def PathOptions(self):  # pragma: no cover
        return PathOptionsOutput.make_one(self.boto3_raw_data["PathOptions"])

    Tags = field("Tags")
    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetResponse:
    boto3_raw_data: "type_defs.DescribeDatasetResponseTypeDef" = dataclasses.field()

    CreatedBy = field("CreatedBy")
    CreateDate = field("CreateDate")
    Name = field("Name")
    Format = field("Format")

    @cached_property
    def FormatOptions(self):  # pragma: no cover
        return FormatOptionsOutput.make_one(self.boto3_raw_data["FormatOptions"])

    @cached_property
    def Input(self):  # pragma: no cover
        return Input.make_one(self.boto3_raw_data["Input"])

    LastModifiedDate = field("LastModifiedDate")
    LastModifiedBy = field("LastModifiedBy")
    Source = field("Source")

    @cached_property
    def PathOptions(self):  # pragma: no cover
        return PathOptionsOutput.make_one(self.boto3_raw_data["PathOptions"])

    Tags = field("Tags")
    ResourceArn = field("ResourceArn")

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
class ListRecipeVersionsResponse:
    boto3_raw_data: "type_defs.ListRecipeVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Recipes(self):  # pragma: no cover
        return Recipe.make_many(self.boto3_raw_data["Recipes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecipeVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecipeVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecipesResponse:
    boto3_raw_data: "type_defs.ListRecipesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Recipes(self):  # pragma: no cover
        return Recipe.make_many(self.boto3_raw_data["Recipes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecipesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecipesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRulesetRequest:
    boto3_raw_data: "type_defs.CreateRulesetRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    TargetArn = field("TargetArn")
    Rules = field("Rules")
    Description = field("Description")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRulesetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRulesetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRulesetRequest:
    boto3_raw_data: "type_defs.UpdateRulesetRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Rules = field("Rules")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRulesetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRulesetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileConfigurationOutput:
    boto3_raw_data: "type_defs.ProfileConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def DatasetStatisticsConfiguration(self):  # pragma: no cover
        return StatisticsConfigurationOutput.make_one(
            self.boto3_raw_data["DatasetStatisticsConfiguration"]
        )

    @cached_property
    def ProfileColumns(self):  # pragma: no cover
        return ColumnSelector.make_many(self.boto3_raw_data["ProfileColumns"])

    @cached_property
    def ColumnStatisticsConfigurations(self):  # pragma: no cover
        return ColumnStatisticsConfigurationOutput.make_many(
            self.boto3_raw_data["ColumnStatisticsConfigurations"]
        )

    @cached_property
    def EntityDetectorConfiguration(self):  # pragma: no cover
        return EntityDetectorConfigurationOutput.make_one(
            self.boto3_raw_data["EntityDetectorConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProfileConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProfileConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileConfiguration:
    boto3_raw_data: "type_defs.ProfileConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def DatasetStatisticsConfiguration(self):  # pragma: no cover
        return StatisticsConfiguration.make_one(
            self.boto3_raw_data["DatasetStatisticsConfiguration"]
        )

    @cached_property
    def ProfileColumns(self):  # pragma: no cover
        return ColumnSelector.make_many(self.boto3_raw_data["ProfileColumns"])

    @cached_property
    def ColumnStatisticsConfigurations(self):  # pragma: no cover
        return ColumnStatisticsConfiguration.make_many(
            self.boto3_raw_data["ColumnStatisticsConfigurations"]
        )

    @cached_property
    def EntityDetectorConfiguration(self):  # pragma: no cover
        return EntityDetectorConfiguration.make_one(
            self.boto3_raw_data["EntityDetectorConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProfileConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProfileConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobRunsResponse:
    boto3_raw_data: "type_defs.ListJobRunsResponseTypeDef" = dataclasses.field()

    @cached_property
    def JobRuns(self):  # pragma: no cover
        return JobRun.make_many(self.boto3_raw_data["JobRuns"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobRunsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobRunsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsResponse:
    boto3_raw_data: "type_defs.ListJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Jobs(self):  # pragma: no cover
        return Job.make_many(self.boto3_raw_data["Jobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListJobsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRecipeJobRequest:
    boto3_raw_data: "type_defs.CreateRecipeJobRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    RoleArn = field("RoleArn")
    DatasetName = field("DatasetName")
    EncryptionKeyArn = field("EncryptionKeyArn")
    EncryptionMode = field("EncryptionMode")
    LogSubscription = field("LogSubscription")
    MaxCapacity = field("MaxCapacity")
    MaxRetries = field("MaxRetries")
    Outputs = field("Outputs")

    @cached_property
    def DataCatalogOutputs(self):  # pragma: no cover
        return DataCatalogOutput.make_many(self.boto3_raw_data["DataCatalogOutputs"])

    @cached_property
    def DatabaseOutputs(self):  # pragma: no cover
        return DatabaseOutput.make_many(self.boto3_raw_data["DatabaseOutputs"])

    ProjectName = field("ProjectName")

    @cached_property
    def RecipeReference(self):  # pragma: no cover
        return RecipeReference.make_one(self.boto3_raw_data["RecipeReference"])

    Tags = field("Tags")
    Timeout = field("Timeout")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRecipeJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRecipeJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRecipeJobRequest:
    boto3_raw_data: "type_defs.UpdateRecipeJobRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    RoleArn = field("RoleArn")
    EncryptionKeyArn = field("EncryptionKeyArn")
    EncryptionMode = field("EncryptionMode")
    LogSubscription = field("LogSubscription")
    MaxCapacity = field("MaxCapacity")
    MaxRetries = field("MaxRetries")
    Outputs = field("Outputs")

    @cached_property
    def DataCatalogOutputs(self):  # pragma: no cover
        return DataCatalogOutput.make_many(self.boto3_raw_data["DataCatalogOutputs"])

    @cached_property
    def DatabaseOutputs(self):  # pragma: no cover
        return DatabaseOutput.make_many(self.boto3_raw_data["DatabaseOutputs"])

    Timeout = field("Timeout")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRecipeJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRecipeJobRequestTypeDef"]
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
        return Dataset.make_many(self.boto3_raw_data["Datasets"])

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
class CreateDatasetRequest:
    boto3_raw_data: "type_defs.CreateDatasetRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Input(self):  # pragma: no cover
        return Input.make_one(self.boto3_raw_data["Input"])

    Format = field("Format")
    FormatOptions = field("FormatOptions")
    PathOptions = field("PathOptions")
    Tags = field("Tags")

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
class UpdateDatasetRequest:
    boto3_raw_data: "type_defs.UpdateDatasetRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Input(self):  # pragma: no cover
        return Input.make_one(self.boto3_raw_data["Input"])

    Format = field("Format")
    FormatOptions = field("FormatOptions")
    PathOptions = field("PathOptions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRecipeRequest:
    boto3_raw_data: "type_defs.CreateRecipeRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Steps = field("Steps")
    Description = field("Description")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRecipeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRecipeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendProjectSessionActionRequest:
    boto3_raw_data: "type_defs.SendProjectSessionActionRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Preview = field("Preview")
    RecipeStep = field("RecipeStep")
    StepIndex = field("StepIndex")
    ClientSessionId = field("ClientSessionId")

    @cached_property
    def ViewFrame(self):  # pragma: no cover
        return ViewFrame.make_one(self.boto3_raw_data["ViewFrame"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SendProjectSessionActionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendProjectSessionActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRecipeRequest:
    boto3_raw_data: "type_defs.UpdateRecipeRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    Steps = field("Steps")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRecipeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRecipeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobResponse:
    boto3_raw_data: "type_defs.DescribeJobResponseTypeDef" = dataclasses.field()

    CreateDate = field("CreateDate")
    CreatedBy = field("CreatedBy")
    DatasetName = field("DatasetName")
    EncryptionKeyArn = field("EncryptionKeyArn")
    EncryptionMode = field("EncryptionMode")
    Name = field("Name")
    Type = field("Type")
    LastModifiedBy = field("LastModifiedBy")
    LastModifiedDate = field("LastModifiedDate")
    LogSubscription = field("LogSubscription")
    MaxCapacity = field("MaxCapacity")
    MaxRetries = field("MaxRetries")

    @cached_property
    def Outputs(self):  # pragma: no cover
        return Extra.make_many(self.boto3_raw_data["Outputs"])

    @cached_property
    def DataCatalogOutputs(self):  # pragma: no cover
        return DataCatalogOutput.make_many(self.boto3_raw_data["DataCatalogOutputs"])

    @cached_property
    def DatabaseOutputs(self):  # pragma: no cover
        return DatabaseOutput.make_many(self.boto3_raw_data["DatabaseOutputs"])

    ProjectName = field("ProjectName")

    @cached_property
    def ProfileConfiguration(self):  # pragma: no cover
        return ProfileConfigurationOutput.make_one(
            self.boto3_raw_data["ProfileConfiguration"]
        )

    @cached_property
    def ValidationConfigurations(self):  # pragma: no cover
        return ValidationConfiguration.make_many(
            self.boto3_raw_data["ValidationConfigurations"]
        )

    @cached_property
    def RecipeReference(self):  # pragma: no cover
        return RecipeReference.make_one(self.boto3_raw_data["RecipeReference"])

    ResourceArn = field("ResourceArn")
    RoleArn = field("RoleArn")
    Tags = field("Tags")
    Timeout = field("Timeout")

    @cached_property
    def JobSample(self):  # pragma: no cover
        return JobSample.make_one(self.boto3_raw_data["JobSample"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobRunResponse:
    boto3_raw_data: "type_defs.DescribeJobRunResponseTypeDef" = dataclasses.field()

    Attempt = field("Attempt")
    CompletedOn = field("CompletedOn")
    DatasetName = field("DatasetName")
    ErrorMessage = field("ErrorMessage")
    ExecutionTime = field("ExecutionTime")
    JobName = field("JobName")

    @cached_property
    def ProfileConfiguration(self):  # pragma: no cover
        return ProfileConfigurationOutput.make_one(
            self.boto3_raw_data["ProfileConfiguration"]
        )

    @cached_property
    def ValidationConfigurations(self):  # pragma: no cover
        return ValidationConfiguration.make_many(
            self.boto3_raw_data["ValidationConfigurations"]
        )

    RunId = field("RunId")
    State = field("State")
    LogSubscription = field("LogSubscription")
    LogGroupName = field("LogGroupName")

    @cached_property
    def Outputs(self):  # pragma: no cover
        return Extra.make_many(self.boto3_raw_data["Outputs"])

    @cached_property
    def DataCatalogOutputs(self):  # pragma: no cover
        return DataCatalogOutput.make_many(self.boto3_raw_data["DataCatalogOutputs"])

    @cached_property
    def DatabaseOutputs(self):  # pragma: no cover
        return DatabaseOutput.make_many(self.boto3_raw_data["DatabaseOutputs"])

    @cached_property
    def RecipeReference(self):  # pragma: no cover
        return RecipeReference.make_one(self.boto3_raw_data["RecipeReference"])

    StartedBy = field("StartedBy")
    StartedOn = field("StartedOn")

    @cached_property
    def JobSample(self):  # pragma: no cover
        return JobSample.make_one(self.boto3_raw_data["JobSample"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobRunResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProfileJobRequest:
    boto3_raw_data: "type_defs.CreateProfileJobRequestTypeDef" = dataclasses.field()

    DatasetName = field("DatasetName")
    Name = field("Name")

    @cached_property
    def OutputLocation(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["OutputLocation"])

    RoleArn = field("RoleArn")
    EncryptionKeyArn = field("EncryptionKeyArn")
    EncryptionMode = field("EncryptionMode")
    LogSubscription = field("LogSubscription")
    MaxCapacity = field("MaxCapacity")
    MaxRetries = field("MaxRetries")
    Configuration = field("Configuration")

    @cached_property
    def ValidationConfigurations(self):  # pragma: no cover
        return ValidationConfiguration.make_many(
            self.boto3_raw_data["ValidationConfigurations"]
        )

    Tags = field("Tags")
    Timeout = field("Timeout")

    @cached_property
    def JobSample(self):  # pragma: no cover
        return JobSample.make_one(self.boto3_raw_data["JobSample"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProfileJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProfileJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProfileJobRequest:
    boto3_raw_data: "type_defs.UpdateProfileJobRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def OutputLocation(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["OutputLocation"])

    RoleArn = field("RoleArn")
    Configuration = field("Configuration")
    EncryptionKeyArn = field("EncryptionKeyArn")
    EncryptionMode = field("EncryptionMode")
    LogSubscription = field("LogSubscription")
    MaxCapacity = field("MaxCapacity")
    MaxRetries = field("MaxRetries")

    @cached_property
    def ValidationConfigurations(self):  # pragma: no cover
        return ValidationConfiguration.make_many(
            self.boto3_raw_data["ValidationConfigurations"]
        )

    Timeout = field("Timeout")

    @cached_property
    def JobSample(self):  # pragma: no cover
        return JobSample.make_one(self.boto3_raw_data["JobSample"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProfileJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProfileJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
