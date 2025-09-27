# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_codeguru_reviewer import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class KMSKeyDetails:
    boto3_raw_data: "type_defs.KMSKeyDetailsTypeDef" = dataclasses.field()

    KMSKeyId = field("KMSKeyId")
    EncryptionOption = field("EncryptionOption")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KMSKeyDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KMSKeyDetailsTypeDef"]],
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
class BranchDiffSourceCodeType:
    boto3_raw_data: "type_defs.BranchDiffSourceCodeTypeTypeDef" = dataclasses.field()

    SourceBranchName = field("SourceBranchName")
    DestinationBranchName = field("DestinationBranchName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BranchDiffSourceCodeTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BranchDiffSourceCodeTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeArtifacts:
    boto3_raw_data: "type_defs.CodeArtifactsTypeDef" = dataclasses.field()

    SourceCodeArtifactsObjectKey = field("SourceCodeArtifactsObjectKey")
    BuildArtifactsObjectKey = field("BuildArtifactsObjectKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodeArtifactsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CodeArtifactsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeCommitRepository:
    boto3_raw_data: "type_defs.CodeCommitRepositoryTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodeCommitRepositoryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeCommitRepositoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricsSummary:
    boto3_raw_data: "type_defs.MetricsSummaryTypeDef" = dataclasses.field()

    MeteredLinesOfCodeCount = field("MeteredLinesOfCodeCount")
    SuppressedLinesOfCodeCount = field("SuppressedLinesOfCodeCount")
    FindingsCount = field("FindingsCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricsSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricsSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Metrics:
    boto3_raw_data: "type_defs.MetricsTypeDef" = dataclasses.field()

    MeteredLinesOfCodeCount = field("MeteredLinesOfCodeCount")
    SuppressedLinesOfCodeCount = field("SuppressedLinesOfCodeCount")
    FindingsCount = field("FindingsCount")

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
class CommitDiffSourceCodeType:
    boto3_raw_data: "type_defs.CommitDiffSourceCodeTypeTypeDef" = dataclasses.field()

    SourceCommit = field("SourceCommit")
    DestinationCommit = field("DestinationCommit")
    MergeBaseCommit = field("MergeBaseCommit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommitDiffSourceCodeTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommitDiffSourceCodeTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCodeReviewRequest:
    boto3_raw_data: "type_defs.DescribeCodeReviewRequestTypeDef" = dataclasses.field()

    CodeReviewArn = field("CodeReviewArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCodeReviewRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCodeReviewRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaiterConfig:
    boto3_raw_data: "type_defs.WaiterConfigTypeDef" = dataclasses.field()

    Delay = field("Delay")
    MaxAttempts = field("MaxAttempts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaiterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaiterConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecommendationFeedbackRequest:
    boto3_raw_data: "type_defs.DescribeRecommendationFeedbackRequestTypeDef" = (
        dataclasses.field()
    )

    CodeReviewArn = field("CodeReviewArn")
    RecommendationId = field("RecommendationId")
    UserId = field("UserId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRecommendationFeedbackRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecommendationFeedbackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationFeedback:
    boto3_raw_data: "type_defs.RecommendationFeedbackTypeDef" = dataclasses.field()

    CodeReviewArn = field("CodeReviewArn")
    RecommendationId = field("RecommendationId")
    Reactions = field("Reactions")
    UserId = field("UserId")
    CreatedTimeStamp = field("CreatedTimeStamp")
    LastUpdatedTimeStamp = field("LastUpdatedTimeStamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendationFeedbackTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationFeedbackTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRepositoryAssociationRequest:
    boto3_raw_data: "type_defs.DescribeRepositoryAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    AssociationArn = field("AssociationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRepositoryAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRepositoryAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateRepositoryRequest:
    boto3_raw_data: "type_defs.DisassociateRepositoryRequestTypeDef" = (
        dataclasses.field()
    )

    AssociationArn = field("AssociationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateRepositoryRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateRepositoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventInfo:
    boto3_raw_data: "type_defs.EventInfoTypeDef" = dataclasses.field()

    Name = field("Name")
    State = field("State")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCodeReviewsRequest:
    boto3_raw_data: "type_defs.ListCodeReviewsRequestTypeDef" = dataclasses.field()

    Type = field("Type")
    ProviderTypes = field("ProviderTypes")
    States = field("States")
    RepositoryNames = field("RepositoryNames")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCodeReviewsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCodeReviewsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationFeedbackRequest:
    boto3_raw_data: "type_defs.ListRecommendationFeedbackRequestTypeDef" = (
        dataclasses.field()
    )

    CodeReviewArn = field("CodeReviewArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    UserIds = field("UserIds")
    RecommendationIds = field("RecommendationIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecommendationFeedbackRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationFeedbackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationFeedbackSummary:
    boto3_raw_data: "type_defs.RecommendationFeedbackSummaryTypeDef" = (
        dataclasses.field()
    )

    RecommendationId = field("RecommendationId")
    Reactions = field("Reactions")
    UserId = field("UserId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RecommendationFeedbackSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationFeedbackSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationsRequest:
    boto3_raw_data: "type_defs.ListRecommendationsRequestTypeDef" = dataclasses.field()

    CodeReviewArn = field("CodeReviewArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecommendationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationsRequestTypeDef"]
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
class ListRepositoryAssociationsRequest:
    boto3_raw_data: "type_defs.ListRepositoryAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    ProviderTypes = field("ProviderTypes")
    States = field("States")
    Names = field("Names")
    Owners = field("Owners")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRepositoryAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositoryAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositoryAssociationSummary:
    boto3_raw_data: "type_defs.RepositoryAssociationSummaryTypeDef" = (
        dataclasses.field()
    )

    AssociationArn = field("AssociationArn")
    ConnectionArn = field("ConnectionArn")
    LastUpdatedTimeStamp = field("LastUpdatedTimeStamp")
    AssociationId = field("AssociationId")
    Name = field("Name")
    Owner = field("Owner")
    ProviderType = field("ProviderType")
    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RepositoryAssociationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositoryAssociationSummaryTypeDef"]
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
class PutRecommendationFeedbackRequest:
    boto3_raw_data: "type_defs.PutRecommendationFeedbackRequestTypeDef" = (
        dataclasses.field()
    )

    CodeReviewArn = field("CodeReviewArn")
    RecommendationId = field("RecommendationId")
    Reactions = field("Reactions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutRecommendationFeedbackRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRecommendationFeedbackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleMetadata:
    boto3_raw_data: "type_defs.RuleMetadataTypeDef" = dataclasses.field()

    RuleId = field("RuleId")
    RuleName = field("RuleName")
    ShortDescription = field("ShortDescription")
    LongDescription = field("LongDescription")
    RuleTags = field("RuleTags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositoryHeadSourceCodeType:
    boto3_raw_data: "type_defs.RepositoryHeadSourceCodeTypeTypeDef" = (
        dataclasses.field()
    )

    BranchName = field("BranchName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RepositoryHeadSourceCodeTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositoryHeadSourceCodeTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Repository:
    boto3_raw_data: "type_defs.S3RepositoryTypeDef" = dataclasses.field()

    Name = field("Name")
    BucketName = field("BucketName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3RepositoryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3RepositoryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThirdPartySourceRepository:
    boto3_raw_data: "type_defs.ThirdPartySourceRepositoryTypeDef" = dataclasses.field()

    Name = field("Name")
    ConnectionArn = field("ConnectionArn")
    Owner = field("Owner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ThirdPartySourceRepositoryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThirdPartySourceRepositoryTypeDef"]
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

    resourceArn = field("resourceArn")
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
class S3RepositoryDetails:
    boto3_raw_data: "type_defs.S3RepositoryDetailsTypeDef" = dataclasses.field()

    BucketName = field("BucketName")

    @cached_property
    def CodeArtifacts(self):  # pragma: no cover
        return CodeArtifacts.make_one(self.boto3_raw_data["CodeArtifacts"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3RepositoryDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3RepositoryDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCodeReviewRequestWait:
    boto3_raw_data: "type_defs.DescribeCodeReviewRequestWaitTypeDef" = (
        dataclasses.field()
    )

    CodeReviewArn = field("CodeReviewArn")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCodeReviewRequestWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCodeReviewRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRepositoryAssociationRequestWait:
    boto3_raw_data: "type_defs.DescribeRepositoryAssociationRequestWaitTypeDef" = (
        dataclasses.field()
    )

    AssociationArn = field("AssociationArn")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRepositoryAssociationRequestWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRepositoryAssociationRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecommendationFeedbackResponse:
    boto3_raw_data: "type_defs.DescribeRecommendationFeedbackResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RecommendationFeedback(self):  # pragma: no cover
        return RecommendationFeedback.make_one(
            self.boto3_raw_data["RecommendationFeedback"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRecommendationFeedbackResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecommendationFeedbackResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestMetadata:
    boto3_raw_data: "type_defs.RequestMetadataTypeDef" = dataclasses.field()

    RequestId = field("RequestId")
    Requester = field("Requester")

    @cached_property
    def EventInfo(self):  # pragma: no cover
        return EventInfo.make_one(self.boto3_raw_data["EventInfo"])

    VendorName = field("VendorName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RequestMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RequestMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationFeedbackResponse:
    boto3_raw_data: "type_defs.ListRecommendationFeedbackResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RecommendationFeedbackSummaries(self):  # pragma: no cover
        return RecommendationFeedbackSummary.make_many(
            self.boto3_raw_data["RecommendationFeedbackSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecommendationFeedbackResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationFeedbackResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositoryAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.ListRepositoryAssociationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ProviderTypes = field("ProviderTypes")
    States = field("States")
    Names = field("Names")
    Owners = field("Owners")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRepositoryAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositoryAssociationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositoryAssociationsResponse:
    boto3_raw_data: "type_defs.ListRepositoryAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RepositoryAssociationSummaries(self):  # pragma: no cover
        return RepositoryAssociationSummary.make_many(
            self.boto3_raw_data["RepositoryAssociationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRepositoryAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositoryAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationSummary:
    boto3_raw_data: "type_defs.RecommendationSummaryTypeDef" = dataclasses.field()

    FilePath = field("FilePath")
    RecommendationId = field("RecommendationId")
    StartLine = field("StartLine")
    EndLine = field("EndLine")
    Description = field("Description")
    RecommendationCategory = field("RecommendationCategory")

    @cached_property
    def RuleMetadata(self):  # pragma: no cover
        return RuleMetadata.make_one(self.boto3_raw_data["RuleMetadata"])

    Severity = field("Severity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Repository:
    boto3_raw_data: "type_defs.RepositoryTypeDef" = dataclasses.field()

    @cached_property
    def CodeCommit(self):  # pragma: no cover
        return CodeCommitRepository.make_one(self.boto3_raw_data["CodeCommit"])

    @cached_property
    def Bitbucket(self):  # pragma: no cover
        return ThirdPartySourceRepository.make_one(self.boto3_raw_data["Bitbucket"])

    @cached_property
    def GitHubEnterpriseServer(self):  # pragma: no cover
        return ThirdPartySourceRepository.make_one(
            self.boto3_raw_data["GitHubEnterpriseServer"]
        )

    @cached_property
    def S3Bucket(self):  # pragma: no cover
        return S3Repository.make_one(self.boto3_raw_data["S3Bucket"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RepositoryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RepositoryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositoryAssociation:
    boto3_raw_data: "type_defs.RepositoryAssociationTypeDef" = dataclasses.field()

    AssociationId = field("AssociationId")
    AssociationArn = field("AssociationArn")
    ConnectionArn = field("ConnectionArn")
    Name = field("Name")
    Owner = field("Owner")
    ProviderType = field("ProviderType")
    State = field("State")
    StateReason = field("StateReason")
    LastUpdatedTimeStamp = field("LastUpdatedTimeStamp")
    CreatedTimeStamp = field("CreatedTimeStamp")

    @cached_property
    def KMSKeyDetails(self):  # pragma: no cover
        return KMSKeyDetails.make_one(self.boto3_raw_data["KMSKeyDetails"])

    @cached_property
    def S3RepositoryDetails(self):  # pragma: no cover
        return S3RepositoryDetails.make_one(self.boto3_raw_data["S3RepositoryDetails"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RepositoryAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositoryAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3BucketRepository:
    boto3_raw_data: "type_defs.S3BucketRepositoryTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Details(self):  # pragma: no cover
        return S3RepositoryDetails.make_one(self.boto3_raw_data["Details"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3BucketRepositoryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3BucketRepositoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationsResponse:
    boto3_raw_data: "type_defs.ListRecommendationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def RecommendationSummaries(self):  # pragma: no cover
        return RecommendationSummary.make_many(
            self.boto3_raw_data["RecommendationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecommendationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateRepositoryRequest:
    boto3_raw_data: "type_defs.AssociateRepositoryRequestTypeDef" = dataclasses.field()

    @cached_property
    def Repository(self):  # pragma: no cover
        return Repository.make_one(self.boto3_raw_data["Repository"])

    ClientRequestToken = field("ClientRequestToken")
    Tags = field("Tags")

    @cached_property
    def KMSKeyDetails(self):  # pragma: no cover
        return KMSKeyDetails.make_one(self.boto3_raw_data["KMSKeyDetails"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateRepositoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateRepositoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateRepositoryResponse:
    boto3_raw_data: "type_defs.AssociateRepositoryResponseTypeDef" = dataclasses.field()

    @cached_property
    def RepositoryAssociation(self):  # pragma: no cover
        return RepositoryAssociation.make_one(
            self.boto3_raw_data["RepositoryAssociation"]
        )

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateRepositoryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateRepositoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRepositoryAssociationResponse:
    boto3_raw_data: "type_defs.DescribeRepositoryAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RepositoryAssociation(self):  # pragma: no cover
        return RepositoryAssociation.make_one(
            self.boto3_raw_data["RepositoryAssociation"]
        )

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRepositoryAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRepositoryAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateRepositoryResponse:
    boto3_raw_data: "type_defs.DisassociateRepositoryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RepositoryAssociation(self):  # pragma: no cover
        return RepositoryAssociation.make_one(
            self.boto3_raw_data["RepositoryAssociation"]
        )

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateRepositoryResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateRepositoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceCodeType:
    boto3_raw_data: "type_defs.SourceCodeTypeTypeDef" = dataclasses.field()

    @cached_property
    def CommitDiff(self):  # pragma: no cover
        return CommitDiffSourceCodeType.make_one(self.boto3_raw_data["CommitDiff"])

    @cached_property
    def RepositoryHead(self):  # pragma: no cover
        return RepositoryHeadSourceCodeType.make_one(
            self.boto3_raw_data["RepositoryHead"]
        )

    @cached_property
    def BranchDiff(self):  # pragma: no cover
        return BranchDiffSourceCodeType.make_one(self.boto3_raw_data["BranchDiff"])

    @cached_property
    def S3BucketRepository(self):  # pragma: no cover
        return S3BucketRepository.make_one(self.boto3_raw_data["S3BucketRepository"])

    @cached_property
    def RequestMetadata(self):  # pragma: no cover
        return RequestMetadata.make_one(self.boto3_raw_data["RequestMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceCodeTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceCodeTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeReviewSummary:
    boto3_raw_data: "type_defs.CodeReviewSummaryTypeDef" = dataclasses.field()

    Name = field("Name")
    CodeReviewArn = field("CodeReviewArn")
    RepositoryName = field("RepositoryName")
    Owner = field("Owner")
    ProviderType = field("ProviderType")
    State = field("State")
    CreatedTimeStamp = field("CreatedTimeStamp")
    LastUpdatedTimeStamp = field("LastUpdatedTimeStamp")
    Type = field("Type")
    PullRequestId = field("PullRequestId")

    @cached_property
    def MetricsSummary(self):  # pragma: no cover
        return MetricsSummary.make_one(self.boto3_raw_data["MetricsSummary"])

    @cached_property
    def SourceCodeType(self):  # pragma: no cover
        return SourceCodeType.make_one(self.boto3_raw_data["SourceCodeType"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodeReviewSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeReviewSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeReview:
    boto3_raw_data: "type_defs.CodeReviewTypeDef" = dataclasses.field()

    Name = field("Name")
    CodeReviewArn = field("CodeReviewArn")
    RepositoryName = field("RepositoryName")
    Owner = field("Owner")
    ProviderType = field("ProviderType")
    State = field("State")
    StateReason = field("StateReason")
    CreatedTimeStamp = field("CreatedTimeStamp")
    LastUpdatedTimeStamp = field("LastUpdatedTimeStamp")
    Type = field("Type")
    PullRequestId = field("PullRequestId")

    @cached_property
    def SourceCodeType(self):  # pragma: no cover
        return SourceCodeType.make_one(self.boto3_raw_data["SourceCodeType"])

    AssociationArn = field("AssociationArn")

    @cached_property
    def Metrics(self):  # pragma: no cover
        return Metrics.make_one(self.boto3_raw_data["Metrics"])

    AnalysisTypes = field("AnalysisTypes")
    ConfigFileState = field("ConfigFileState")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodeReviewTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CodeReviewTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositoryAnalysis:
    boto3_raw_data: "type_defs.RepositoryAnalysisTypeDef" = dataclasses.field()

    @cached_property
    def RepositoryHead(self):  # pragma: no cover
        return RepositoryHeadSourceCodeType.make_one(
            self.boto3_raw_data["RepositoryHead"]
        )

    @cached_property
    def SourceCodeType(self):  # pragma: no cover
        return SourceCodeType.make_one(self.boto3_raw_data["SourceCodeType"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RepositoryAnalysisTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositoryAnalysisTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCodeReviewsResponse:
    boto3_raw_data: "type_defs.ListCodeReviewsResponseTypeDef" = dataclasses.field()

    @cached_property
    def CodeReviewSummaries(self):  # pragma: no cover
        return CodeReviewSummary.make_many(self.boto3_raw_data["CodeReviewSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCodeReviewsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCodeReviewsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCodeReviewResponse:
    boto3_raw_data: "type_defs.CreateCodeReviewResponseTypeDef" = dataclasses.field()

    @cached_property
    def CodeReview(self):  # pragma: no cover
        return CodeReview.make_one(self.boto3_raw_data["CodeReview"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCodeReviewResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCodeReviewResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCodeReviewResponse:
    boto3_raw_data: "type_defs.DescribeCodeReviewResponseTypeDef" = dataclasses.field()

    @cached_property
    def CodeReview(self):  # pragma: no cover
        return CodeReview.make_one(self.boto3_raw_data["CodeReview"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCodeReviewResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCodeReviewResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeReviewType:
    boto3_raw_data: "type_defs.CodeReviewTypeTypeDef" = dataclasses.field()

    @cached_property
    def RepositoryAnalysis(self):  # pragma: no cover
        return RepositoryAnalysis.make_one(self.boto3_raw_data["RepositoryAnalysis"])

    AnalysisTypes = field("AnalysisTypes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodeReviewTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CodeReviewTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCodeReviewRequest:
    boto3_raw_data: "type_defs.CreateCodeReviewRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    RepositoryAssociationArn = field("RepositoryAssociationArn")

    @cached_property
    def Type(self):  # pragma: no cover
        return CodeReviewType.make_one(self.boto3_raw_data["Type"])

    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCodeReviewRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCodeReviewRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
