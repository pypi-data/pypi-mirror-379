# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_application_signals import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


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
class ServiceLevelObjectiveBudgetReportError:
    boto3_raw_data: "type_defs.ServiceLevelObjectiveBudgetReportErrorTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Arn = field("Arn")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceLevelObjectiveBudgetReportErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceLevelObjectiveBudgetReportErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateExclusionWindowsError:
    boto3_raw_data: "type_defs.BatchUpdateExclusionWindowsErrorTypeDef" = (
        dataclasses.field()
    )

    SloId = field("SloId")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchUpdateExclusionWindowsErrorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateExclusionWindowsErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BurnRateConfiguration:
    boto3_raw_data: "type_defs.BurnRateConfigurationTypeDef" = dataclasses.field()

    LookBackWindowMinutes = field("LookBackWindowMinutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BurnRateConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BurnRateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalendarIntervalOutput:
    boto3_raw_data: "type_defs.CalendarIntervalOutputTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    DurationUnit = field("DurationUnit")
    Duration = field("Duration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CalendarIntervalOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalendarIntervalOutputTypeDef"]
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
class DeleteServiceLevelObjectiveInput:
    boto3_raw_data: "type_defs.DeleteServiceLevelObjectiveInputTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteServiceLevelObjectiveInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceLevelObjectiveInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DependencyConfigOutput:
    boto3_raw_data: "type_defs.DependencyConfigOutputTypeDef" = dataclasses.field()

    DependencyKeyAttributes = field("DependencyKeyAttributes")
    DependencyOperationName = field("DependencyOperationName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DependencyConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DependencyConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DependencyConfig:
    boto3_raw_data: "type_defs.DependencyConfigTypeDef" = dataclasses.field()

    DependencyKeyAttributes = field("DependencyKeyAttributes")
    DependencyOperationName = field("DependencyOperationName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DependencyConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DependencyConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Dimension:
    boto3_raw_data: "type_defs.DimensionTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DimensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DimensionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecurrenceRule:
    boto3_raw_data: "type_defs.RecurrenceRuleTypeDef" = dataclasses.field()

    Expression = field("Expression")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecurrenceRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecurrenceRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Window:
    boto3_raw_data: "type_defs.WindowTypeDef" = dataclasses.field()

    DurationUnit = field("DurationUnit")
    Duration = field("Duration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WindowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WindowTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceLevelObjectiveInput:
    boto3_raw_data: "type_defs.GetServiceLevelObjectiveInputTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetServiceLevelObjectiveInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceLevelObjectiveInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RollingInterval:
    boto3_raw_data: "type_defs.RollingIntervalTypeDef" = dataclasses.field()

    DurationUnit = field("DurationUnit")
    Duration = field("Duration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RollingIntervalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RollingIntervalTypeDef"]],
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
class ListServiceLevelObjectiveExclusionWindowsInput:
    boto3_raw_data: (
        "type_defs.ListServiceLevelObjectiveExclusionWindowsInputTypeDef"
    ) = dataclasses.field()

    Id = field("Id")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceLevelObjectiveExclusionWindowsInputTypeDef"
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
                "type_defs.ListServiceLevelObjectiveExclusionWindowsInputTypeDef"
            ]
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
class BatchGetServiceLevelObjectiveBudgetReportInput:
    boto3_raw_data: (
        "type_defs.BatchGetServiceLevelObjectiveBudgetReportInputTypeDef"
    ) = dataclasses.field()

    Timestamp = field("Timestamp")
    SloIds = field("SloIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetServiceLevelObjectiveBudgetReportInputTypeDef"
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
                "type_defs.BatchGetServiceLevelObjectiveBudgetReportInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalendarInterval:
    boto3_raw_data: "type_defs.CalendarIntervalTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    DurationUnit = field("DurationUnit")
    Duration = field("Duration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CalendarIntervalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalendarIntervalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceInput:
    boto3_raw_data: "type_defs.GetServiceInputTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    KeyAttributes = field("KeyAttributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetServiceInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetServiceInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceDependenciesInput:
    boto3_raw_data: "type_defs.ListServiceDependenciesInputTypeDef" = (
        dataclasses.field()
    )

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    KeyAttributes = field("KeyAttributes")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServiceDependenciesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceDependenciesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceDependentsInput:
    boto3_raw_data: "type_defs.ListServiceDependentsInputTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    KeyAttributes = field("KeyAttributes")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServiceDependentsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceDependentsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceOperationsInput:
    boto3_raw_data: "type_defs.ListServiceOperationsInputTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    KeyAttributes = field("KeyAttributes")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServiceOperationsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceOperationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesInput:
    boto3_raw_data: "type_defs.ListServicesInputTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    IncludeLinkedAccounts = field("IncludeLinkedAccounts")
    AwsAccountId = field("AwsAccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListServicesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateExclusionWindowsOutput:
    boto3_raw_data: "type_defs.BatchUpdateExclusionWindowsOutputTypeDef" = (
        dataclasses.field()
    )

    SloIds = field("SloIds")

    @cached_property
    def Errors(self):  # pragma: no cover
        return BatchUpdateExclusionWindowsError.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateExclusionWindowsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateExclusionWindowsOutputTypeDef"]
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
class ServiceLevelObjectiveSummary:
    boto3_raw_data: "type_defs.ServiceLevelObjectiveSummaryTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Name = field("Name")
    KeyAttributes = field("KeyAttributes")
    OperationName = field("OperationName")

    @cached_property
    def DependencyConfig(self):  # pragma: no cover
        return DependencyConfigOutput.make_one(self.boto3_raw_data["DependencyConfig"])

    CreatedTime = field("CreatedTime")
    EvaluationType = field("EvaluationType")
    MetricSourceType = field("MetricSourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceLevelObjectiveSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceLevelObjectiveSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricOutput:
    boto3_raw_data: "type_defs.MetricOutputTypeDef" = dataclasses.field()

    Namespace = field("Namespace")
    MetricName = field("MetricName")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricReference:
    boto3_raw_data: "type_defs.MetricReferenceTypeDef" = dataclasses.field()

    Namespace = field("Namespace")
    MetricType = field("MetricType")
    MetricName = field("MetricName")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    AccountId = field("AccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricReferenceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Metric:
    boto3_raw_data: "type_defs.MetricTypeDef" = dataclasses.field()

    Namespace = field("Namespace")
    MetricName = field("MetricName")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExclusionWindowOutput:
    boto3_raw_data: "type_defs.ExclusionWindowOutputTypeDef" = dataclasses.field()

    @cached_property
    def Window(self):  # pragma: no cover
        return Window.make_one(self.boto3_raw_data["Window"])

    StartTime = field("StartTime")

    @cached_property
    def RecurrenceRule(self):  # pragma: no cover
        return RecurrenceRule.make_one(self.boto3_raw_data["RecurrenceRule"])

    Reason = field("Reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExclusionWindowOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExclusionWindowOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExclusionWindow:
    boto3_raw_data: "type_defs.ExclusionWindowTypeDef" = dataclasses.field()

    @cached_property
    def Window(self):  # pragma: no cover
        return Window.make_one(self.boto3_raw_data["Window"])

    StartTime = field("StartTime")

    @cached_property
    def RecurrenceRule(self):  # pragma: no cover
        return RecurrenceRule.make_one(self.boto3_raw_data["RecurrenceRule"])

    Reason = field("Reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExclusionWindowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExclusionWindowTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntervalOutput:
    boto3_raw_data: "type_defs.IntervalOutputTypeDef" = dataclasses.field()

    @cached_property
    def RollingInterval(self):  # pragma: no cover
        return RollingInterval.make_one(self.boto3_raw_data["RollingInterval"])

    @cached_property
    def CalendarInterval(self):  # pragma: no cover
        return CalendarIntervalOutput.make_one(self.boto3_raw_data["CalendarInterval"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntervalOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IntervalOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceDependenciesInputPaginate:
    boto3_raw_data: "type_defs.ListServiceDependenciesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    KeyAttributes = field("KeyAttributes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceDependenciesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceDependenciesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceDependentsInputPaginate:
    boto3_raw_data: "type_defs.ListServiceDependentsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    KeyAttributes = field("KeyAttributes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceDependentsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceDependentsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceLevelObjectiveExclusionWindowsInputPaginate:
    boto3_raw_data: (
        "type_defs.ListServiceLevelObjectiveExclusionWindowsInputPaginateTypeDef"
    ) = dataclasses.field()

    Id = field("Id")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceLevelObjectiveExclusionWindowsInputPaginateTypeDef"
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
                "type_defs.ListServiceLevelObjectiveExclusionWindowsInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceOperationsInputPaginate:
    boto3_raw_data: "type_defs.ListServiceOperationsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    KeyAttributes = field("KeyAttributes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceOperationsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceOperationsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesInputPaginate:
    boto3_raw_data: "type_defs.ListServicesInputPaginateTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    IncludeLinkedAccounts = field("IncludeLinkedAccounts")
    AwsAccountId = field("AwsAccountId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServicesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Interval:
    boto3_raw_data: "type_defs.IntervalTypeDef" = dataclasses.field()

    @cached_property
    def RollingInterval(self):  # pragma: no cover
        return RollingInterval.make_one(self.boto3_raw_data["RollingInterval"])

    @cached_property
    def CalendarInterval(self):  # pragma: no cover
        return CalendarInterval.make_one(self.boto3_raw_data["CalendarInterval"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntervalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IntervalTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceLevelObjectivesOutput:
    boto3_raw_data: "type_defs.ListServiceLevelObjectivesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SloSummaries(self):  # pragma: no cover
        return ServiceLevelObjectiveSummary.make_many(
            self.boto3_raw_data["SloSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListServiceLevelObjectivesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceLevelObjectivesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceLevelObjectivesInputPaginate:
    boto3_raw_data: "type_defs.ListServiceLevelObjectivesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    KeyAttributes = field("KeyAttributes")
    OperationName = field("OperationName")
    DependencyConfig = field("DependencyConfig")
    MetricSourceTypes = field("MetricSourceTypes")
    IncludeLinkedAccounts = field("IncludeLinkedAccounts")
    SloOwnerAwsAccountId = field("SloOwnerAwsAccountId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceLevelObjectivesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceLevelObjectivesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceLevelObjectivesInput:
    boto3_raw_data: "type_defs.ListServiceLevelObjectivesInputTypeDef" = (
        dataclasses.field()
    )

    KeyAttributes = field("KeyAttributes")
    OperationName = field("OperationName")
    DependencyConfig = field("DependencyConfig")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    MetricSourceTypes = field("MetricSourceTypes")
    IncludeLinkedAccounts = field("IncludeLinkedAccounts")
    SloOwnerAwsAccountId = field("SloOwnerAwsAccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListServiceLevelObjectivesInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceLevelObjectivesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricStatOutput:
    boto3_raw_data: "type_defs.MetricStatOutputTypeDef" = dataclasses.field()

    @cached_property
    def Metric(self):  # pragma: no cover
        return MetricOutput.make_one(self.boto3_raw_data["Metric"])

    Period = field("Period")
    Stat = field("Stat")
    Unit = field("Unit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricStatOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricStatOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceDependency:
    boto3_raw_data: "type_defs.ServiceDependencyTypeDef" = dataclasses.field()

    OperationName = field("OperationName")
    DependencyKeyAttributes = field("DependencyKeyAttributes")
    DependencyOperationName = field("DependencyOperationName")

    @cached_property
    def MetricReferences(self):  # pragma: no cover
        return MetricReference.make_many(self.boto3_raw_data["MetricReferences"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceDependencyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceDependencyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceDependent:
    boto3_raw_data: "type_defs.ServiceDependentTypeDef" = dataclasses.field()

    DependentKeyAttributes = field("DependentKeyAttributes")

    @cached_property
    def MetricReferences(self):  # pragma: no cover
        return MetricReference.make_many(self.boto3_raw_data["MetricReferences"])

    OperationName = field("OperationName")
    DependentOperationName = field("DependentOperationName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceDependentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceDependentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceOperation:
    boto3_raw_data: "type_defs.ServiceOperationTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def MetricReferences(self):  # pragma: no cover
        return MetricReference.make_many(self.boto3_raw_data["MetricReferences"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceOperationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceOperationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceSummary:
    boto3_raw_data: "type_defs.ServiceSummaryTypeDef" = dataclasses.field()

    KeyAttributes = field("KeyAttributes")

    @cached_property
    def MetricReferences(self):  # pragma: no cover
        return MetricReference.make_many(self.boto3_raw_data["MetricReferences"])

    AttributeMaps = field("AttributeMaps")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Service:
    boto3_raw_data: "type_defs.ServiceTypeDef" = dataclasses.field()

    KeyAttributes = field("KeyAttributes")

    @cached_property
    def MetricReferences(self):  # pragma: no cover
        return MetricReference.make_many(self.boto3_raw_data["MetricReferences"])

    AttributeMaps = field("AttributeMaps")
    LogGroupReferences = field("LogGroupReferences")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceLevelObjectiveExclusionWindowsOutput:
    boto3_raw_data: (
        "type_defs.ListServiceLevelObjectiveExclusionWindowsOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def ExclusionWindows(self):  # pragma: no cover
        return ExclusionWindowOutput.make_many(self.boto3_raw_data["ExclusionWindows"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceLevelObjectiveExclusionWindowsOutputTypeDef"
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
                "type_defs.ListServiceLevelObjectiveExclusionWindowsOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GoalOutput:
    boto3_raw_data: "type_defs.GoalOutputTypeDef" = dataclasses.field()

    @cached_property
    def Interval(self):  # pragma: no cover
        return IntervalOutput.make_one(self.boto3_raw_data["Interval"])

    AttainmentGoal = field("AttainmentGoal")
    WarningThreshold = field("WarningThreshold")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GoalOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GoalOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Goal:
    boto3_raw_data: "type_defs.GoalTypeDef" = dataclasses.field()

    @cached_property
    def Interval(self):  # pragma: no cover
        return Interval.make_one(self.boto3_raw_data["Interval"])

    AttainmentGoal = field("AttainmentGoal")
    WarningThreshold = field("WarningThreshold")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GoalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GoalTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDataQueryOutput:
    boto3_raw_data: "type_defs.MetricDataQueryOutputTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def MetricStat(self):  # pragma: no cover
        return MetricStatOutput.make_one(self.boto3_raw_data["MetricStat"])

    Expression = field("Expression")
    Label = field("Label")
    ReturnData = field("ReturnData")
    Period = field("Period")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricDataQueryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricDataQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceDependenciesOutput:
    boto3_raw_data: "type_defs.ListServiceDependenciesOutputTypeDef" = (
        dataclasses.field()
    )

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def ServiceDependencies(self):  # pragma: no cover
        return ServiceDependency.make_many(self.boto3_raw_data["ServiceDependencies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListServiceDependenciesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceDependenciesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceDependentsOutput:
    boto3_raw_data: "type_defs.ListServiceDependentsOutputTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def ServiceDependents(self):  # pragma: no cover
        return ServiceDependent.make_many(self.boto3_raw_data["ServiceDependents"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServiceDependentsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceDependentsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceOperationsOutput:
    boto3_raw_data: "type_defs.ListServiceOperationsOutputTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def ServiceOperations(self):  # pragma: no cover
        return ServiceOperation.make_many(self.boto3_raw_data["ServiceOperations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServiceOperationsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceOperationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesOutput:
    boto3_raw_data: "type_defs.ListServicesOutputTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def ServiceSummaries(self):  # pragma: no cover
        return ServiceSummary.make_many(self.boto3_raw_data["ServiceSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServicesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceOutput:
    boto3_raw_data: "type_defs.GetServiceOutputTypeDef" = dataclasses.field()

    @cached_property
    def Service(self):  # pragma: no cover
        return Service.make_one(self.boto3_raw_data["Service"])

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    LogGroupReferences = field("LogGroupReferences")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetServiceOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricStat:
    boto3_raw_data: "type_defs.MetricStatTypeDef" = dataclasses.field()

    Metric = field("Metric")
    Period = field("Period")
    Stat = field("Stat")
    Unit = field("Unit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricStatTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricStatTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateExclusionWindowsInput:
    boto3_raw_data: "type_defs.BatchUpdateExclusionWindowsInputTypeDef" = (
        dataclasses.field()
    )

    SloIds = field("SloIds")
    AddExclusionWindows = field("AddExclusionWindows")
    RemoveExclusionWindows = field("RemoveExclusionWindows")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchUpdateExclusionWindowsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateExclusionWindowsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitoredRequestCountMetricDataQueriesOutput:
    boto3_raw_data: "type_defs.MonitoredRequestCountMetricDataQueriesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GoodCountMetric(self):  # pragma: no cover
        return MetricDataQueryOutput.make_many(self.boto3_raw_data["GoodCountMetric"])

    @cached_property
    def BadCountMetric(self):  # pragma: no cover
        return MetricDataQueryOutput.make_many(self.boto3_raw_data["BadCountMetric"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MonitoredRequestCountMetricDataQueriesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MonitoredRequestCountMetricDataQueriesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceLevelIndicatorMetric:
    boto3_raw_data: "type_defs.ServiceLevelIndicatorMetricTypeDef" = dataclasses.field()

    @cached_property
    def MetricDataQueries(self):  # pragma: no cover
        return MetricDataQueryOutput.make_many(self.boto3_raw_data["MetricDataQueries"])

    KeyAttributes = field("KeyAttributes")
    OperationName = field("OperationName")
    MetricType = field("MetricType")

    @cached_property
    def DependencyConfig(self):  # pragma: no cover
        return DependencyConfigOutput.make_one(self.boto3_raw_data["DependencyConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceLevelIndicatorMetricTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceLevelIndicatorMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestBasedServiceLevelIndicatorMetric:
    boto3_raw_data: "type_defs.RequestBasedServiceLevelIndicatorMetricTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TotalRequestCountMetric(self):  # pragma: no cover
        return MetricDataQueryOutput.make_many(
            self.boto3_raw_data["TotalRequestCountMetric"]
        )

    @cached_property
    def MonitoredRequestCountMetric(self):  # pragma: no cover
        return MonitoredRequestCountMetricDataQueriesOutput.make_one(
            self.boto3_raw_data["MonitoredRequestCountMetric"]
        )

    KeyAttributes = field("KeyAttributes")
    OperationName = field("OperationName")
    MetricType = field("MetricType")

    @cached_property
    def DependencyConfig(self):  # pragma: no cover
        return DependencyConfigOutput.make_one(self.boto3_raw_data["DependencyConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RequestBasedServiceLevelIndicatorMetricTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestBasedServiceLevelIndicatorMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceLevelIndicator:
    boto3_raw_data: "type_defs.ServiceLevelIndicatorTypeDef" = dataclasses.field()

    @cached_property
    def SliMetric(self):  # pragma: no cover
        return ServiceLevelIndicatorMetric.make_one(self.boto3_raw_data["SliMetric"])

    MetricThreshold = field("MetricThreshold")
    ComparisonOperator = field("ComparisonOperator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceLevelIndicatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceLevelIndicatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDataQuery:
    boto3_raw_data: "type_defs.MetricDataQueryTypeDef" = dataclasses.field()

    Id = field("Id")
    MetricStat = field("MetricStat")
    Expression = field("Expression")
    Label = field("Label")
    ReturnData = field("ReturnData")
    Period = field("Period")
    AccountId = field("AccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricDataQueryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricDataQueryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestBasedServiceLevelIndicator:
    boto3_raw_data: "type_defs.RequestBasedServiceLevelIndicatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RequestBasedSliMetric(self):  # pragma: no cover
        return RequestBasedServiceLevelIndicatorMetric.make_one(
            self.boto3_raw_data["RequestBasedSliMetric"]
        )

    MetricThreshold = field("MetricThreshold")
    ComparisonOperator = field("ComparisonOperator")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RequestBasedServiceLevelIndicatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestBasedServiceLevelIndicatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceLevelObjectiveBudgetReport:
    boto3_raw_data: "type_defs.ServiceLevelObjectiveBudgetReportTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Name = field("Name")
    BudgetStatus = field("BudgetStatus")
    EvaluationType = field("EvaluationType")
    Attainment = field("Attainment")
    TotalBudgetSeconds = field("TotalBudgetSeconds")
    BudgetSecondsRemaining = field("BudgetSecondsRemaining")
    TotalBudgetRequests = field("TotalBudgetRequests")
    BudgetRequestsRemaining = field("BudgetRequestsRemaining")

    @cached_property
    def Sli(self):  # pragma: no cover
        return ServiceLevelIndicator.make_one(self.boto3_raw_data["Sli"])

    @cached_property
    def RequestBasedSli(self):  # pragma: no cover
        return RequestBasedServiceLevelIndicator.make_one(
            self.boto3_raw_data["RequestBasedSli"]
        )

    @cached_property
    def Goal(self):  # pragma: no cover
        return GoalOutput.make_one(self.boto3_raw_data["Goal"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceLevelObjectiveBudgetReportTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceLevelObjectiveBudgetReportTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceLevelObjective:
    boto3_raw_data: "type_defs.ServiceLevelObjectiveTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    CreatedTime = field("CreatedTime")
    LastUpdatedTime = field("LastUpdatedTime")

    @cached_property
    def Goal(self):  # pragma: no cover
        return GoalOutput.make_one(self.boto3_raw_data["Goal"])

    Description = field("Description")

    @cached_property
    def Sli(self):  # pragma: no cover
        return ServiceLevelIndicator.make_one(self.boto3_raw_data["Sli"])

    @cached_property
    def RequestBasedSli(self):  # pragma: no cover
        return RequestBasedServiceLevelIndicator.make_one(
            self.boto3_raw_data["RequestBasedSli"]
        )

    EvaluationType = field("EvaluationType")

    @cached_property
    def BurnRateConfigurations(self):  # pragma: no cover
        return BurnRateConfiguration.make_many(
            self.boto3_raw_data["BurnRateConfigurations"]
        )

    MetricSourceType = field("MetricSourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceLevelObjectiveTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceLevelObjectiveTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitoredRequestCountMetricDataQueries:
    boto3_raw_data: "type_defs.MonitoredRequestCountMetricDataQueriesTypeDef" = (
        dataclasses.field()
    )

    GoodCountMetric = field("GoodCountMetric")

    @cached_property
    def BadCountMetric(self):  # pragma: no cover
        return MetricDataQuery.make_many(self.boto3_raw_data["BadCountMetric"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MonitoredRequestCountMetricDataQueriesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MonitoredRequestCountMetricDataQueriesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceLevelIndicatorMetricConfig:
    boto3_raw_data: "type_defs.ServiceLevelIndicatorMetricConfigTypeDef" = (
        dataclasses.field()
    )

    KeyAttributes = field("KeyAttributes")
    OperationName = field("OperationName")
    MetricType = field("MetricType")
    Statistic = field("Statistic")
    PeriodSeconds = field("PeriodSeconds")
    MetricDataQueries = field("MetricDataQueries")
    DependencyConfig = field("DependencyConfig")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceLevelIndicatorMetricConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceLevelIndicatorMetricConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetServiceLevelObjectiveBudgetReportOutput:
    boto3_raw_data: (
        "type_defs.BatchGetServiceLevelObjectiveBudgetReportOutputTypeDef"
    ) = dataclasses.field()

    Timestamp = field("Timestamp")

    @cached_property
    def Reports(self):  # pragma: no cover
        return ServiceLevelObjectiveBudgetReport.make_many(
            self.boto3_raw_data["Reports"]
        )

    @cached_property
    def Errors(self):  # pragma: no cover
        return ServiceLevelObjectiveBudgetReportError.make_many(
            self.boto3_raw_data["Errors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetServiceLevelObjectiveBudgetReportOutputTypeDef"
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
                "type_defs.BatchGetServiceLevelObjectiveBudgetReportOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceLevelObjectiveOutput:
    boto3_raw_data: "type_defs.CreateServiceLevelObjectiveOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Slo(self):  # pragma: no cover
        return ServiceLevelObjective.make_one(self.boto3_raw_data["Slo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateServiceLevelObjectiveOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceLevelObjectiveOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceLevelObjectiveOutput:
    boto3_raw_data: "type_defs.GetServiceLevelObjectiveOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Slo(self):  # pragma: no cover
        return ServiceLevelObjective.make_one(self.boto3_raw_data["Slo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetServiceLevelObjectiveOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceLevelObjectiveOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceLevelObjectiveOutput:
    boto3_raw_data: "type_defs.UpdateServiceLevelObjectiveOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Slo(self):  # pragma: no cover
        return ServiceLevelObjective.make_one(self.boto3_raw_data["Slo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateServiceLevelObjectiveOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceLevelObjectiveOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceLevelIndicatorConfig:
    boto3_raw_data: "type_defs.ServiceLevelIndicatorConfigTypeDef" = dataclasses.field()

    @cached_property
    def SliMetricConfig(self):  # pragma: no cover
        return ServiceLevelIndicatorMetricConfig.make_one(
            self.boto3_raw_data["SliMetricConfig"]
        )

    MetricThreshold = field("MetricThreshold")
    ComparisonOperator = field("ComparisonOperator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceLevelIndicatorConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceLevelIndicatorConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestBasedServiceLevelIndicatorMetricConfig:
    boto3_raw_data: "type_defs.RequestBasedServiceLevelIndicatorMetricConfigTypeDef" = (
        dataclasses.field()
    )

    KeyAttributes = field("KeyAttributes")
    OperationName = field("OperationName")
    MetricType = field("MetricType")
    TotalRequestCountMetric = field("TotalRequestCountMetric")
    MonitoredRequestCountMetric = field("MonitoredRequestCountMetric")
    DependencyConfig = field("DependencyConfig")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RequestBasedServiceLevelIndicatorMetricConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestBasedServiceLevelIndicatorMetricConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestBasedServiceLevelIndicatorConfig:
    boto3_raw_data: "type_defs.RequestBasedServiceLevelIndicatorConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RequestBasedSliMetricConfig(self):  # pragma: no cover
        return RequestBasedServiceLevelIndicatorMetricConfig.make_one(
            self.boto3_raw_data["RequestBasedSliMetricConfig"]
        )

    MetricThreshold = field("MetricThreshold")
    ComparisonOperator = field("ComparisonOperator")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RequestBasedServiceLevelIndicatorConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestBasedServiceLevelIndicatorConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceLevelObjectiveInput:
    boto3_raw_data: "type_defs.CreateServiceLevelObjectiveInputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Description = field("Description")

    @cached_property
    def SliConfig(self):  # pragma: no cover
        return ServiceLevelIndicatorConfig.make_one(self.boto3_raw_data["SliConfig"])

    @cached_property
    def RequestBasedSliConfig(self):  # pragma: no cover
        return RequestBasedServiceLevelIndicatorConfig.make_one(
            self.boto3_raw_data["RequestBasedSliConfig"]
        )

    Goal = field("Goal")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def BurnRateConfigurations(self):  # pragma: no cover
        return BurnRateConfiguration.make_many(
            self.boto3_raw_data["BurnRateConfigurations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateServiceLevelObjectiveInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceLevelObjectiveInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceLevelObjectiveInput:
    boto3_raw_data: "type_defs.UpdateServiceLevelObjectiveInputTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Description = field("Description")

    @cached_property
    def SliConfig(self):  # pragma: no cover
        return ServiceLevelIndicatorConfig.make_one(self.boto3_raw_data["SliConfig"])

    @cached_property
    def RequestBasedSliConfig(self):  # pragma: no cover
        return RequestBasedServiceLevelIndicatorConfig.make_one(
            self.boto3_raw_data["RequestBasedSliConfig"]
        )

    Goal = field("Goal")

    @cached_property
    def BurnRateConfigurations(self):  # pragma: no cover
        return BurnRateConfiguration.make_many(
            self.boto3_raw_data["BurnRateConfigurations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateServiceLevelObjectiveInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceLevelObjectiveInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
