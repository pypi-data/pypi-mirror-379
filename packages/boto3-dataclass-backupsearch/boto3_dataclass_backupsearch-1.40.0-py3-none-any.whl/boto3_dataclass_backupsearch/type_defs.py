# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_backupsearch import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class BackupCreationTimeFilterOutput:
    boto3_raw_data: "type_defs.BackupCreationTimeFilterOutputTypeDef" = (
        dataclasses.field()
    )

    CreatedAfter = field("CreatedAfter")
    CreatedBefore = field("CreatedBefore")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BackupCreationTimeFilterOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackupCreationTimeFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CurrentSearchProgress:
    boto3_raw_data: "type_defs.CurrentSearchProgressTypeDef" = dataclasses.field()

    RecoveryPointsScannedCount = field("RecoveryPointsScannedCount")
    ItemsScannedCount = field("ItemsScannedCount")
    ItemsMatchedCount = field("ItemsMatchedCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CurrentSearchProgressTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CurrentSearchProgressTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LongCondition:
    boto3_raw_data: "type_defs.LongConditionTypeDef" = dataclasses.field()

    Value = field("Value")
    Operator = field("Operator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LongConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LongConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StringCondition:
    boto3_raw_data: "type_defs.StringConditionTypeDef" = dataclasses.field()

    Value = field("Value")
    Operator = field("Operator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StringConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StringConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeConditionOutput:
    boto3_raw_data: "type_defs.TimeConditionOutputTypeDef" = dataclasses.field()

    Value = field("Value")
    Operator = field("Operator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimeConditionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeConditionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EBSResultItem:
    boto3_raw_data: "type_defs.EBSResultItemTypeDef" = dataclasses.field()

    BackupResourceArn = field("BackupResourceArn")
    SourceResourceArn = field("SourceResourceArn")
    BackupVaultName = field("BackupVaultName")
    FileSystemIdentifier = field("FileSystemIdentifier")
    FilePath = field("FilePath")
    FileSize = field("FileSize")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EBSResultItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EBSResultItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportJobSummary:
    boto3_raw_data: "type_defs.ExportJobSummaryTypeDef" = dataclasses.field()

    ExportJobIdentifier = field("ExportJobIdentifier")
    ExportJobArn = field("ExportJobArn")
    Status = field("Status")
    CreationTime = field("CreationTime")
    CompletionTime = field("CompletionTime")
    StatusMessage = field("StatusMessage")
    SearchJobArn = field("SearchJobArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportJobSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ExportSpecification:
    boto3_raw_data: "type_defs.S3ExportSpecificationTypeDef" = dataclasses.field()

    DestinationBucket = field("DestinationBucket")
    DestinationPrefix = field("DestinationPrefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3ExportSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ExportSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSearchJobInput:
    boto3_raw_data: "type_defs.GetSearchJobInputTypeDef" = dataclasses.field()

    SearchJobIdentifier = field("SearchJobIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSearchJobInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSearchJobInputTypeDef"]
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
class SearchScopeSummary:
    boto3_raw_data: "type_defs.SearchScopeSummaryTypeDef" = dataclasses.field()

    TotalRecoveryPointsToScanCount = field("TotalRecoveryPointsToScanCount")
    TotalItemsToScanCount = field("TotalItemsToScanCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchScopeSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchScopeSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSearchResultExportJobInput:
    boto3_raw_data: "type_defs.GetSearchResultExportJobInputTypeDef" = (
        dataclasses.field()
    )

    ExportJobIdentifier = field("ExportJobIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSearchResultExportJobInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSearchResultExportJobInputTypeDef"]
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
class ListSearchJobBackupsInput:
    boto3_raw_data: "type_defs.ListSearchJobBackupsInputTypeDef" = dataclasses.field()

    SearchJobIdentifier = field("SearchJobIdentifier")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSearchJobBackupsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSearchJobBackupsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchJobBackupsResult:
    boto3_raw_data: "type_defs.SearchJobBackupsResultTypeDef" = dataclasses.field()

    Status = field("Status")
    StatusMessage = field("StatusMessage")
    ResourceType = field("ResourceType")
    BackupResourceArn = field("BackupResourceArn")
    SourceResourceArn = field("SourceResourceArn")
    IndexCreationTime = field("IndexCreationTime")
    BackupCreationTime = field("BackupCreationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchJobBackupsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchJobBackupsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSearchJobResultsInput:
    boto3_raw_data: "type_defs.ListSearchJobResultsInputTypeDef" = dataclasses.field()

    SearchJobIdentifier = field("SearchJobIdentifier")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSearchJobResultsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSearchJobResultsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSearchJobsInput:
    boto3_raw_data: "type_defs.ListSearchJobsInputTypeDef" = dataclasses.field()

    ByStatus = field("ByStatus")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSearchJobsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSearchJobsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSearchResultExportJobsInput:
    boto3_raw_data: "type_defs.ListSearchResultExportJobsInputTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    SearchJobIdentifier = field("SearchJobIdentifier")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSearchResultExportJobsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSearchResultExportJobsInputTypeDef"]
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
class S3ResultItem:
    boto3_raw_data: "type_defs.S3ResultItemTypeDef" = dataclasses.field()

    BackupResourceArn = field("BackupResourceArn")
    SourceResourceArn = field("SourceResourceArn")
    BackupVaultName = field("BackupVaultName")
    ObjectKey = field("ObjectKey")
    ObjectSize = field("ObjectSize")
    CreationTime = field("CreationTime")
    ETag = field("ETag")
    VersionId = field("VersionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ResultItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ResultItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopSearchJobInput:
    boto3_raw_data: "type_defs.StopSearchJobInputTypeDef" = dataclasses.field()

    SearchJobIdentifier = field("SearchJobIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopSearchJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopSearchJobInputTypeDef"]
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
class SearchScopeOutput:
    boto3_raw_data: "type_defs.SearchScopeOutputTypeDef" = dataclasses.field()

    BackupResourceTypes = field("BackupResourceTypes")

    @cached_property
    def BackupResourceCreationTime(self):  # pragma: no cover
        return BackupCreationTimeFilterOutput.make_one(
            self.boto3_raw_data["BackupResourceCreationTime"]
        )

    SourceResourceArns = field("SourceResourceArns")
    BackupResourceArns = field("BackupResourceArns")
    BackupResourceTags = field("BackupResourceTags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchScopeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchScopeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackupCreationTimeFilter:
    boto3_raw_data: "type_defs.BackupCreationTimeFilterTypeDef" = dataclasses.field()

    CreatedAfter = field("CreatedAfter")
    CreatedBefore = field("CreatedBefore")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BackupCreationTimeFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackupCreationTimeFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeCondition:
    boto3_raw_data: "type_defs.TimeConditionTypeDef" = dataclasses.field()

    Value = field("Value")
    Operator = field("Operator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EBSItemFilterOutput:
    boto3_raw_data: "type_defs.EBSItemFilterOutputTypeDef" = dataclasses.field()

    @cached_property
    def FilePaths(self):  # pragma: no cover
        return StringCondition.make_many(self.boto3_raw_data["FilePaths"])

    @cached_property
    def Sizes(self):  # pragma: no cover
        return LongCondition.make_many(self.boto3_raw_data["Sizes"])

    @cached_property
    def CreationTimes(self):  # pragma: no cover
        return TimeConditionOutput.make_many(self.boto3_raw_data["CreationTimes"])

    @cached_property
    def LastModificationTimes(self):  # pragma: no cover
        return TimeConditionOutput.make_many(
            self.boto3_raw_data["LastModificationTimes"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EBSItemFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EBSItemFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ItemFilterOutput:
    boto3_raw_data: "type_defs.S3ItemFilterOutputTypeDef" = dataclasses.field()

    @cached_property
    def ObjectKeys(self):  # pragma: no cover
        return StringCondition.make_many(self.boto3_raw_data["ObjectKeys"])

    @cached_property
    def Sizes(self):  # pragma: no cover
        return LongCondition.make_many(self.boto3_raw_data["Sizes"])

    @cached_property
    def CreationTimes(self):  # pragma: no cover
        return TimeConditionOutput.make_many(self.boto3_raw_data["CreationTimes"])

    @cached_property
    def VersionIds(self):  # pragma: no cover
        return StringCondition.make_many(self.boto3_raw_data["VersionIds"])

    @cached_property
    def ETags(self):  # pragma: no cover
        return StringCondition.make_many(self.boto3_raw_data["ETags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3ItemFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ItemFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportSpecification:
    boto3_raw_data: "type_defs.ExportSpecificationTypeDef" = dataclasses.field()

    @cached_property
    def s3ExportSpecification(self):  # pragma: no cover
        return S3ExportSpecification.make_one(
            self.boto3_raw_data["s3ExportSpecification"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSearchResultExportJobsOutput:
    boto3_raw_data: "type_defs.ListSearchResultExportJobsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ExportJobs(self):  # pragma: no cover
        return ExportJobSummary.make_many(self.boto3_raw_data["ExportJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSearchResultExportJobsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSearchResultExportJobsOutputTypeDef"]
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
class StartSearchJobOutput:
    boto3_raw_data: "type_defs.StartSearchJobOutputTypeDef" = dataclasses.field()

    SearchJobArn = field("SearchJobArn")
    CreationTime = field("CreationTime")
    SearchJobIdentifier = field("SearchJobIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSearchJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSearchJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSearchResultExportJobOutput:
    boto3_raw_data: "type_defs.StartSearchResultExportJobOutputTypeDef" = (
        dataclasses.field()
    )

    ExportJobArn = field("ExportJobArn")
    ExportJobIdentifier = field("ExportJobIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartSearchResultExportJobOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSearchResultExportJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchJobSummary:
    boto3_raw_data: "type_defs.SearchJobSummaryTypeDef" = dataclasses.field()

    SearchJobIdentifier = field("SearchJobIdentifier")
    SearchJobArn = field("SearchJobArn")
    Name = field("Name")
    Status = field("Status")
    CreationTime = field("CreationTime")
    CompletionTime = field("CompletionTime")

    @cached_property
    def SearchScopeSummary(self):  # pragma: no cover
        return SearchScopeSummary.make_one(self.boto3_raw_data["SearchScopeSummary"])

    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchJobSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSearchJobBackupsInputPaginate:
    boto3_raw_data: "type_defs.ListSearchJobBackupsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    SearchJobIdentifier = field("SearchJobIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSearchJobBackupsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSearchJobBackupsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSearchJobResultsInputPaginate:
    boto3_raw_data: "type_defs.ListSearchJobResultsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    SearchJobIdentifier = field("SearchJobIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSearchJobResultsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSearchJobResultsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSearchJobsInputPaginate:
    boto3_raw_data: "type_defs.ListSearchJobsInputPaginateTypeDef" = dataclasses.field()

    ByStatus = field("ByStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSearchJobsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSearchJobsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSearchResultExportJobsInputPaginate:
    boto3_raw_data: "type_defs.ListSearchResultExportJobsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    SearchJobIdentifier = field("SearchJobIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSearchResultExportJobsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSearchResultExportJobsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSearchJobBackupsOutput:
    boto3_raw_data: "type_defs.ListSearchJobBackupsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Results(self):  # pragma: no cover
        return SearchJobBackupsResult.make_many(self.boto3_raw_data["Results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSearchJobBackupsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSearchJobBackupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResultItem:
    boto3_raw_data: "type_defs.ResultItemTypeDef" = dataclasses.field()

    @cached_property
    def S3ResultItem(self):  # pragma: no cover
        return S3ResultItem.make_one(self.boto3_raw_data["S3ResultItem"])

    @cached_property
    def EBSResultItem(self):  # pragma: no cover
        return EBSResultItem.make_one(self.boto3_raw_data["EBSResultItem"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResultItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResultItemTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchScope:
    boto3_raw_data: "type_defs.SearchScopeTypeDef" = dataclasses.field()

    BackupResourceTypes = field("BackupResourceTypes")

    @cached_property
    def BackupResourceCreationTime(self):  # pragma: no cover
        return BackupCreationTimeFilter.make_one(
            self.boto3_raw_data["BackupResourceCreationTime"]
        )

    SourceResourceArns = field("SourceResourceArns")
    BackupResourceArns = field("BackupResourceArns")
    BackupResourceTags = field("BackupResourceTags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchScopeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SearchScopeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EBSItemFilter:
    boto3_raw_data: "type_defs.EBSItemFilterTypeDef" = dataclasses.field()

    @cached_property
    def FilePaths(self):  # pragma: no cover
        return StringCondition.make_many(self.boto3_raw_data["FilePaths"])

    @cached_property
    def Sizes(self):  # pragma: no cover
        return LongCondition.make_many(self.boto3_raw_data["Sizes"])

    @cached_property
    def CreationTimes(self):  # pragma: no cover
        return TimeCondition.make_many(self.boto3_raw_data["CreationTimes"])

    @cached_property
    def LastModificationTimes(self):  # pragma: no cover
        return TimeCondition.make_many(self.boto3_raw_data["LastModificationTimes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EBSItemFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EBSItemFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ItemFilter:
    boto3_raw_data: "type_defs.S3ItemFilterTypeDef" = dataclasses.field()

    @cached_property
    def ObjectKeys(self):  # pragma: no cover
        return StringCondition.make_many(self.boto3_raw_data["ObjectKeys"])

    @cached_property
    def Sizes(self):  # pragma: no cover
        return LongCondition.make_many(self.boto3_raw_data["Sizes"])

    @cached_property
    def CreationTimes(self):  # pragma: no cover
        return TimeCondition.make_many(self.boto3_raw_data["CreationTimes"])

    @cached_property
    def VersionIds(self):  # pragma: no cover
        return StringCondition.make_many(self.boto3_raw_data["VersionIds"])

    @cached_property
    def ETags(self):  # pragma: no cover
        return StringCondition.make_many(self.boto3_raw_data["ETags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ItemFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ItemFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ItemFiltersOutput:
    boto3_raw_data: "type_defs.ItemFiltersOutputTypeDef" = dataclasses.field()

    @cached_property
    def S3ItemFilters(self):  # pragma: no cover
        return S3ItemFilterOutput.make_many(self.boto3_raw_data["S3ItemFilters"])

    @cached_property
    def EBSItemFilters(self):  # pragma: no cover
        return EBSItemFilterOutput.make_many(self.boto3_raw_data["EBSItemFilters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ItemFiltersOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ItemFiltersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSearchResultExportJobOutput:
    boto3_raw_data: "type_defs.GetSearchResultExportJobOutputTypeDef" = (
        dataclasses.field()
    )

    ExportJobIdentifier = field("ExportJobIdentifier")
    ExportJobArn = field("ExportJobArn")
    Status = field("Status")
    CreationTime = field("CreationTime")
    CompletionTime = field("CompletionTime")
    StatusMessage = field("StatusMessage")

    @cached_property
    def ExportSpecification(self):  # pragma: no cover
        return ExportSpecification.make_one(self.boto3_raw_data["ExportSpecification"])

    SearchJobArn = field("SearchJobArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSearchResultExportJobOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSearchResultExportJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSearchResultExportJobInput:
    boto3_raw_data: "type_defs.StartSearchResultExportJobInputTypeDef" = (
        dataclasses.field()
    )

    SearchJobIdentifier = field("SearchJobIdentifier")

    @cached_property
    def ExportSpecification(self):  # pragma: no cover
        return ExportSpecification.make_one(self.boto3_raw_data["ExportSpecification"])

    ClientToken = field("ClientToken")
    Tags = field("Tags")
    RoleArn = field("RoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartSearchResultExportJobInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSearchResultExportJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSearchJobsOutput:
    boto3_raw_data: "type_defs.ListSearchJobsOutputTypeDef" = dataclasses.field()

    @cached_property
    def SearchJobs(self):  # pragma: no cover
        return SearchJobSummary.make_many(self.boto3_raw_data["SearchJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSearchJobsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSearchJobsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSearchJobResultsOutput:
    boto3_raw_data: "type_defs.ListSearchJobResultsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Results(self):  # pragma: no cover
        return ResultItem.make_many(self.boto3_raw_data["Results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSearchJobResultsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSearchJobResultsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ItemFilters:
    boto3_raw_data: "type_defs.ItemFiltersTypeDef" = dataclasses.field()

    @cached_property
    def S3ItemFilters(self):  # pragma: no cover
        return S3ItemFilter.make_many(self.boto3_raw_data["S3ItemFilters"])

    @cached_property
    def EBSItemFilters(self):  # pragma: no cover
        return EBSItemFilter.make_many(self.boto3_raw_data["EBSItemFilters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ItemFiltersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ItemFiltersTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSearchJobOutput:
    boto3_raw_data: "type_defs.GetSearchJobOutputTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def SearchScopeSummary(self):  # pragma: no cover
        return SearchScopeSummary.make_one(self.boto3_raw_data["SearchScopeSummary"])

    @cached_property
    def CurrentSearchProgress(self):  # pragma: no cover
        return CurrentSearchProgress.make_one(
            self.boto3_raw_data["CurrentSearchProgress"]
        )

    StatusMessage = field("StatusMessage")
    EncryptionKeyArn = field("EncryptionKeyArn")
    CompletionTime = field("CompletionTime")
    Status = field("Status")

    @cached_property
    def SearchScope(self):  # pragma: no cover
        return SearchScopeOutput.make_one(self.boto3_raw_data["SearchScope"])

    @cached_property
    def ItemFilters(self):  # pragma: no cover
        return ItemFiltersOutput.make_one(self.boto3_raw_data["ItemFilters"])

    CreationTime = field("CreationTime")
    SearchJobIdentifier = field("SearchJobIdentifier")
    SearchJobArn = field("SearchJobArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSearchJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSearchJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSearchJobInput:
    boto3_raw_data: "type_defs.StartSearchJobInputTypeDef" = dataclasses.field()

    SearchScope = field("SearchScope")
    Tags = field("Tags")
    Name = field("Name")
    EncryptionKeyArn = field("EncryptionKeyArn")
    ClientToken = field("ClientToken")
    ItemFilters = field("ItemFilters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSearchJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSearchJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
