# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_devops_guru import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccountInsightHealth:
    boto3_raw_data: "type_defs.AccountInsightHealthTypeDef" = dataclasses.field()

    OpenProactiveInsights = field("OpenProactiveInsights")
    OpenReactiveInsights = field("OpenReactiveInsights")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountInsightHealthTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountInsightHealthTypeDef"]
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
class AmazonCodeGuruProfilerIntegration:
    boto3_raw_data: "type_defs.AmazonCodeGuruProfilerIntegrationTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AmazonCodeGuruProfilerIntegrationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmazonCodeGuruProfilerIntegrationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyReportedTimeRange:
    boto3_raw_data: "type_defs.AnomalyReportedTimeRangeTypeDef" = dataclasses.field()

    OpenTime = field("OpenTime")
    CloseTime = field("CloseTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnomalyReportedTimeRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalyReportedTimeRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyResource:
    boto3_raw_data: "type_defs.AnomalyResourceTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnomalyResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnomalyResourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalySourceMetadata:
    boto3_raw_data: "type_defs.AnomalySourceMetadataTypeDef" = dataclasses.field()

    Source = field("Source")
    SourceResourceName = field("SourceResourceName")
    SourceResourceType = field("SourceResourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnomalySourceMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalySourceMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyTimeRange:
    boto3_raw_data: "type_defs.AnomalyTimeRangeTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnomalyTimeRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalyTimeRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudFormationCollectionFilter:
    boto3_raw_data: "type_defs.CloudFormationCollectionFilterTypeDef" = (
        dataclasses.field()
    )

    StackNames = field("StackNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CloudFormationCollectionFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudFormationCollectionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudFormationCollectionOutput:
    boto3_raw_data: "type_defs.CloudFormationCollectionOutputTypeDef" = (
        dataclasses.field()
    )

    StackNames = field("StackNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CloudFormationCollectionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudFormationCollectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudFormationCollection:
    boto3_raw_data: "type_defs.CloudFormationCollectionTypeDef" = dataclasses.field()

    StackNames = field("StackNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudFormationCollectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudFormationCollectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudFormationCostEstimationResourceCollectionFilterOutput:
    boto3_raw_data: (
        "type_defs.CloudFormationCostEstimationResourceCollectionFilterOutputTypeDef"
    ) = dataclasses.field()

    StackNames = field("StackNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CloudFormationCostEstimationResourceCollectionFilterOutputTypeDef"
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
                "type_defs.CloudFormationCostEstimationResourceCollectionFilterOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudFormationCostEstimationResourceCollectionFilter:
    boto3_raw_data: (
        "type_defs.CloudFormationCostEstimationResourceCollectionFilterTypeDef"
    ) = dataclasses.field()

    StackNames = field("StackNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CloudFormationCostEstimationResourceCollectionFilterTypeDef"
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
                "type_defs.CloudFormationCostEstimationResourceCollectionFilterTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InsightHealth:
    boto3_raw_data: "type_defs.InsightHealthTypeDef" = dataclasses.field()

    OpenProactiveInsights = field("OpenProactiveInsights")
    OpenReactiveInsights = field("OpenReactiveInsights")
    MeanTimeToRecoverInMilliseconds = field("MeanTimeToRecoverInMilliseconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InsightHealthTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InsightHealthTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimestampMetricValuePair:
    boto3_raw_data: "type_defs.TimestampMetricValuePairTypeDef" = dataclasses.field()

    Timestamp = field("Timestamp")
    MetricValue = field("MetricValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimestampMetricValuePairTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimestampMetricValuePairTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchMetricsDimension:
    boto3_raw_data: "type_defs.CloudWatchMetricsDimensionTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchMetricsDimensionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchMetricsDimensionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagCostEstimationResourceCollectionFilterOutput:
    boto3_raw_data: (
        "type_defs.TagCostEstimationResourceCollectionFilterOutputTypeDef"
    ) = dataclasses.field()

    AppBoundaryKey = field("AppBoundaryKey")
    TagValues = field("TagValues")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TagCostEstimationResourceCollectionFilterOutputTypeDef"
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
                "type_defs.TagCostEstimationResourceCollectionFilterOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagCostEstimationResourceCollectionFilter:
    boto3_raw_data: "type_defs.TagCostEstimationResourceCollectionFilterTypeDef" = (
        dataclasses.field()
    )

    AppBoundaryKey = field("AppBoundaryKey")
    TagValues = field("TagValues")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TagCostEstimationResourceCollectionFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagCostEstimationResourceCollectionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostEstimationTimeRange:
    boto3_raw_data: "type_defs.CostEstimationTimeRangeTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CostEstimationTimeRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CostEstimationTimeRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInsightRequest:
    boto3_raw_data: "type_defs.DeleteInsightRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInsightRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInsightRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAnomalyRequest:
    boto3_raw_data: "type_defs.DescribeAnomalyRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAnomalyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAnomalyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFeedbackRequest:
    boto3_raw_data: "type_defs.DescribeFeedbackRequestTypeDef" = dataclasses.field()

    InsightId = field("InsightId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFeedbackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFeedbackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InsightFeedback:
    boto3_raw_data: "type_defs.InsightFeedbackTypeDef" = dataclasses.field()

    Id = field("Id")
    Feedback = field("Feedback")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InsightFeedbackTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InsightFeedbackTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInsightRequest:
    boto3_raw_data: "type_defs.DescribeInsightRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInsightRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInsightRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationHealthRequest:
    boto3_raw_data: "type_defs.DescribeOrganizationHealthRequestTypeDef" = (
        dataclasses.field()
    )

    AccountIds = field("AccountIds")
    OrganizationalUnitIds = field("OrganizationalUnitIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationHealthRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrganizationHealthRequestTypeDef"]
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
class DescribeOrganizationResourceCollectionHealthRequest:
    boto3_raw_data: (
        "type_defs.DescribeOrganizationResourceCollectionHealthRequestTypeDef"
    ) = dataclasses.field()

    OrganizationResourceCollectionType = field("OrganizationResourceCollectionType")
    AccountIds = field("AccountIds")
    OrganizationalUnitIds = field("OrganizationalUnitIds")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationResourceCollectionHealthRequestTypeDef"
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
                "type_defs.DescribeOrganizationResourceCollectionHealthRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourceCollectionHealthRequest:
    boto3_raw_data: "type_defs.DescribeResourceCollectionHealthRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceCollectionType = field("ResourceCollectionType")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeResourceCollectionHealthRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourceCollectionHealthRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventResource:
    boto3_raw_data: "type_defs.EventResourceTypeDef" = dataclasses.field()

    Type = field("Type")
    Name = field("Name")
    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventResourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCostEstimationRequest:
    boto3_raw_data: "type_defs.GetCostEstimationRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCostEstimationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCostEstimationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceResourceCost:
    boto3_raw_data: "type_defs.ServiceResourceCostTypeDef" = dataclasses.field()

    Type = field("Type")
    State = field("State")
    Count = field("Count")
    UnitCost = field("UnitCost")
    Cost = field("Cost")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceResourceCostTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceResourceCostTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceCollectionRequest:
    boto3_raw_data: "type_defs.GetResourceCollectionRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceCollectionType = field("ResourceCollectionType")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceCollectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceCollectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InsightTimeRange:
    boto3_raw_data: "type_defs.InsightTimeRangeTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InsightTimeRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InsightTimeRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KMSServerSideEncryptionIntegrationConfig:
    boto3_raw_data: "type_defs.KMSServerSideEncryptionIntegrationConfigTypeDef" = (
        dataclasses.field()
    )

    KMSKeyId = field("KMSKeyId")
    OptInStatus = field("OptInStatus")
    Type = field("Type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KMSServerSideEncryptionIntegrationConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KMSServerSideEncryptionIntegrationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KMSServerSideEncryptionIntegration:
    boto3_raw_data: "type_defs.KMSServerSideEncryptionIntegrationTypeDef" = (
        dataclasses.field()
    )

    KMSKeyId = field("KMSKeyId")
    OptInStatus = field("OptInStatus")
    Type = field("Type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KMSServerSideEncryptionIntegrationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KMSServerSideEncryptionIntegrationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnomalousLogGroupsRequest:
    boto3_raw_data: "type_defs.ListAnomalousLogGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    InsightId = field("InsightId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAnomalousLogGroupsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnomalousLogGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInsightsOngoingStatusFilter:
    boto3_raw_data: "type_defs.ListInsightsOngoingStatusFilterTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInsightsOngoingStatusFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInsightsOngoingStatusFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMonitoredResourcesFilters:
    boto3_raw_data: "type_defs.ListMonitoredResourcesFiltersTypeDef" = (
        dataclasses.field()
    )

    ResourcePermission = field("ResourcePermission")
    ResourceTypeFilters = field("ResourceTypeFilters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMonitoredResourcesFiltersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMonitoredResourcesFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotificationChannelsRequest:
    boto3_raw_data: "type_defs.ListNotificationChannelsRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListNotificationChannelsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotificationChannelsRequestTypeDef"]
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

    InsightId = field("InsightId")
    NextToken = field("NextToken")
    Locale = field("Locale")
    AccountId = field("AccountId")

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
class LogAnomalyClass:
    boto3_raw_data: "type_defs.LogAnomalyClassTypeDef" = dataclasses.field()

    LogStreamName = field("LogStreamName")
    LogAnomalyType = field("LogAnomalyType")
    LogAnomalyToken = field("LogAnomalyToken")
    LogEventId = field("LogEventId")
    Explanation = field("Explanation")
    NumberOfLogLinesOccurrences = field("NumberOfLogLinesOccurrences")
    LogEventTimestamp = field("LogEventTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogAnomalyClassTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogAnomalyClassTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogsAnomalyDetectionIntegrationConfig:
    boto3_raw_data: "type_defs.LogsAnomalyDetectionIntegrationConfigTypeDef" = (
        dataclasses.field()
    )

    OptInStatus = field("OptInStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LogsAnomalyDetectionIntegrationConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogsAnomalyDetectionIntegrationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogsAnomalyDetectionIntegration:
    boto3_raw_data: "type_defs.LogsAnomalyDetectionIntegrationTypeDef" = (
        dataclasses.field()
    )

    OptInStatus = field("OptInStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LogsAnomalyDetectionIntegrationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogsAnomalyDetectionIntegrationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationFilterConfigOutput:
    boto3_raw_data: "type_defs.NotificationFilterConfigOutputTypeDef" = (
        dataclasses.field()
    )

    Severities = field("Severities")
    MessageTypes = field("MessageTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.NotificationFilterConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationFilterConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnsChannelConfig:
    boto3_raw_data: "type_defs.SnsChannelConfigTypeDef" = dataclasses.field()

    TopicArn = field("TopicArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnsChannelConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnsChannelConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationFilterConfig:
    boto3_raw_data: "type_defs.NotificationFilterConfigTypeDef" = dataclasses.field()

    Severities = field("Severities")
    MessageTypes = field("MessageTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationFilterConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationFilterConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpsCenterIntegrationConfig:
    boto3_raw_data: "type_defs.OpsCenterIntegrationConfigTypeDef" = dataclasses.field()

    OptInStatus = field("OptInStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpsCenterIntegrationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpsCenterIntegrationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpsCenterIntegration:
    boto3_raw_data: "type_defs.OpsCenterIntegrationTypeDef" = dataclasses.field()

    OptInStatus = field("OptInStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpsCenterIntegrationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpsCenterIntegrationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PerformanceInsightsMetricDimensionGroup:
    boto3_raw_data: "type_defs.PerformanceInsightsMetricDimensionGroupTypeDef" = (
        dataclasses.field()
    )

    Group = field("Group")
    Dimensions = field("Dimensions")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PerformanceInsightsMetricDimensionGroupTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PerformanceInsightsMetricDimensionGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PerformanceInsightsStat:
    boto3_raw_data: "type_defs.PerformanceInsightsStatTypeDef" = dataclasses.field()

    Type = field("Type")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PerformanceInsightsStatTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PerformanceInsightsStatTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PerformanceInsightsReferenceScalar:
    boto3_raw_data: "type_defs.PerformanceInsightsReferenceScalarTypeDef" = (
        dataclasses.field()
    )

    Value = field("Value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PerformanceInsightsReferenceScalarTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PerformanceInsightsReferenceScalarTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictionTimeRange:
    boto3_raw_data: "type_defs.PredictionTimeRangeTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")

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
class ServiceCollectionOutput:
    boto3_raw_data: "type_defs.ServiceCollectionOutputTypeDef" = dataclasses.field()

    ServiceNames = field("ServiceNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceCollectionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceCollectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationRelatedAnomalyResource:
    boto3_raw_data: "type_defs.RecommendationRelatedAnomalyResourceTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Type = field("Type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RecommendationRelatedAnomalyResourceTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationRelatedAnomalyResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationRelatedCloudWatchMetricsSourceDetail:
    boto3_raw_data: (
        "type_defs.RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef"
    ) = dataclasses.field()

    MetricName = field("MetricName")
    Namespace = field("Namespace")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef"
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
                "type_defs.RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationRelatedEventResource:
    boto3_raw_data: "type_defs.RecommendationRelatedEventResourceTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Type = field("Type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RecommendationRelatedEventResourceTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationRelatedEventResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveNotificationChannelRequest:
    boto3_raw_data: "type_defs.RemoveNotificationChannelRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveNotificationChannelRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveNotificationChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagCollectionFilter:
    boto3_raw_data: "type_defs.TagCollectionFilterTypeDef" = dataclasses.field()

    AppBoundaryKey = field("AppBoundaryKey")
    TagValues = field("TagValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagCollectionFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagCollectionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagCollectionOutput:
    boto3_raw_data: "type_defs.TagCollectionOutputTypeDef" = dataclasses.field()

    AppBoundaryKey = field("AppBoundaryKey")
    TagValues = field("TagValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagCollectionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagCollectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceCollection:
    boto3_raw_data: "type_defs.ServiceCollectionTypeDef" = dataclasses.field()

    ServiceNames = field("ServiceNames")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceCollectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceCollectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceInsightHealth:
    boto3_raw_data: "type_defs.ServiceInsightHealthTypeDef" = dataclasses.field()

    OpenProactiveInsights = field("OpenProactiveInsights")
    OpenReactiveInsights = field("OpenReactiveInsights")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceInsightHealthTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceInsightHealthTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagCollection:
    boto3_raw_data: "type_defs.TagCollectionTypeDef" = dataclasses.field()

    AppBoundaryKey = field("AppBoundaryKey")
    TagValues = field("TagValues")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagCollectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagCollectionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCloudFormationCollectionFilter:
    boto3_raw_data: "type_defs.UpdateCloudFormationCollectionFilterTypeDef" = (
        dataclasses.field()
    )

    StackNames = field("StackNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCloudFormationCollectionFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCloudFormationCollectionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTagCollectionFilter:
    boto3_raw_data: "type_defs.UpdateTagCollectionFilterTypeDef" = dataclasses.field()

    AppBoundaryKey = field("AppBoundaryKey")
    TagValues = field("TagValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTagCollectionFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTagCollectionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountHealth:
    boto3_raw_data: "type_defs.AccountHealthTypeDef" = dataclasses.field()

    AccountId = field("AccountId")

    @cached_property
    def Insight(self):  # pragma: no cover
        return AccountInsightHealth.make_one(self.boto3_raw_data["Insight"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountHealthTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountHealthTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddNotificationChannelResponse:
    boto3_raw_data: "type_defs.AddNotificationChannelResponseTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddNotificationChannelResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddNotificationChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountHealthResponse:
    boto3_raw_data: "type_defs.DescribeAccountHealthResponseTypeDef" = (
        dataclasses.field()
    )

    OpenReactiveInsights = field("OpenReactiveInsights")
    OpenProactiveInsights = field("OpenProactiveInsights")
    MetricsAnalyzed = field("MetricsAnalyzed")
    ResourceHours = field("ResourceHours")
    AnalyzedResourceCount = field("AnalyzedResourceCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAccountHealthResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountHealthResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountOverviewResponse:
    boto3_raw_data: "type_defs.DescribeAccountOverviewResponseTypeDef" = (
        dataclasses.field()
    )

    ReactiveInsights = field("ReactiveInsights")
    ProactiveInsights = field("ProactiveInsights")
    MeanTimeToRecoverInMilliseconds = field("MeanTimeToRecoverInMilliseconds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAccountOverviewResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountOverviewResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationHealthResponse:
    boto3_raw_data: "type_defs.DescribeOrganizationHealthResponseTypeDef" = (
        dataclasses.field()
    )

    OpenReactiveInsights = field("OpenReactiveInsights")
    OpenProactiveInsights = field("OpenProactiveInsights")
    MetricsAnalyzed = field("MetricsAnalyzed")
    ResourceHours = field("ResourceHours")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationHealthResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrganizationHealthResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationOverviewResponse:
    boto3_raw_data: "type_defs.DescribeOrganizationOverviewResponseTypeDef" = (
        dataclasses.field()
    )

    ReactiveInsights = field("ReactiveInsights")
    ProactiveInsights = field("ProactiveInsights")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationOverviewResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrganizationOverviewResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventSourcesConfig:
    boto3_raw_data: "type_defs.EventSourcesConfigTypeDef" = dataclasses.field()

    @cached_property
    def AmazonCodeGuruProfiler(self):  # pragma: no cover
        return AmazonCodeGuruProfilerIntegration.make_one(
            self.boto3_raw_data["AmazonCodeGuruProfiler"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventSourcesConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventSourcesConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudFormationHealth:
    boto3_raw_data: "type_defs.CloudFormationHealthTypeDef" = dataclasses.field()

    StackName = field("StackName")

    @cached_property
    def Insight(self):  # pragma: no cover
        return InsightHealth.make_one(self.boto3_raw_data["Insight"])

    AnalyzedResourceCount = field("AnalyzedResourceCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudFormationHealthTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudFormationHealthTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagHealth:
    boto3_raw_data: "type_defs.TagHealthTypeDef" = dataclasses.field()

    AppBoundaryKey = field("AppBoundaryKey")
    TagValue = field("TagValue")

    @cached_property
    def Insight(self):  # pragma: no cover
        return InsightHealth.make_one(self.boto3_raw_data["Insight"])

    AnalyzedResourceCount = field("AnalyzedResourceCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagHealthTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagHealthTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchMetricsDataSummary:
    boto3_raw_data: "type_defs.CloudWatchMetricsDataSummaryTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TimestampMetricValuePairList(self):  # pragma: no cover
        return TimestampMetricValuePair.make_many(
            self.boto3_raw_data["TimestampMetricValuePairList"]
        )

    StatusCode = field("StatusCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchMetricsDataSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchMetricsDataSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostEstimationResourceCollectionFilterOutput:
    boto3_raw_data: "type_defs.CostEstimationResourceCollectionFilterOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CloudFormation(self):  # pragma: no cover
        return CloudFormationCostEstimationResourceCollectionFilterOutput.make_one(
            self.boto3_raw_data["CloudFormation"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagCostEstimationResourceCollectionFilterOutput.make_many(
            self.boto3_raw_data["Tags"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CostEstimationResourceCollectionFilterOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CostEstimationResourceCollectionFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostEstimationResourceCollectionFilter:
    boto3_raw_data: "type_defs.CostEstimationResourceCollectionFilterTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CloudFormation(self):  # pragma: no cover
        return CloudFormationCostEstimationResourceCollectionFilter.make_one(
            self.boto3_raw_data["CloudFormation"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagCostEstimationResourceCollectionFilter.make_many(
            self.boto3_raw_data["Tags"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CostEstimationResourceCollectionFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CostEstimationResourceCollectionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountOverviewRequest:
    boto3_raw_data: "type_defs.DescribeAccountOverviewRequestTypeDef" = (
        dataclasses.field()
    )

    FromTime = field("FromTime")
    ToTime = field("ToTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAccountOverviewRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountOverviewRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationOverviewRequest:
    boto3_raw_data: "type_defs.DescribeOrganizationOverviewRequestTypeDef" = (
        dataclasses.field()
    )

    FromTime = field("FromTime")
    ToTime = field("ToTime")
    AccountIds = field("AccountIds")
    OrganizationalUnitIds = field("OrganizationalUnitIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationOverviewRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrganizationOverviewRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndTimeRange:
    boto3_raw_data: "type_defs.EndTimeRangeTypeDef" = dataclasses.field()

    FromTime = field("FromTime")
    ToTime = field("ToTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndTimeRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EndTimeRangeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventTimeRange:
    boto3_raw_data: "type_defs.EventTimeRangeTypeDef" = dataclasses.field()

    FromTime = field("FromTime")
    ToTime = field("ToTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventTimeRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventTimeRangeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTimeRange:
    boto3_raw_data: "type_defs.StartTimeRangeTypeDef" = dataclasses.field()

    FromTime = field("FromTime")
    ToTime = field("ToTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartTimeRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StartTimeRangeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFeedbackResponse:
    boto3_raw_data: "type_defs.DescribeFeedbackResponseTypeDef" = dataclasses.field()

    @cached_property
    def InsightFeedback(self):  # pragma: no cover
        return InsightFeedback.make_one(self.boto3_raw_data["InsightFeedback"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFeedbackResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFeedbackResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutFeedbackRequest:
    boto3_raw_data: "type_defs.PutFeedbackRequestTypeDef" = dataclasses.field()

    @cached_property
    def InsightFeedback(self):  # pragma: no cover
        return InsightFeedback.make_one(self.boto3_raw_data["InsightFeedback"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutFeedbackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutFeedbackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationResourceCollectionHealthRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeOrganizationResourceCollectionHealthRequestPaginateTypeDef"
    ) = dataclasses.field()

    OrganizationResourceCollectionType = field("OrganizationResourceCollectionType")
    AccountIds = field("AccountIds")
    OrganizationalUnitIds = field("OrganizationalUnitIds")
    MaxResults = field("MaxResults")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationResourceCollectionHealthRequestPaginateTypeDef"
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
                "type_defs.DescribeOrganizationResourceCollectionHealthRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourceCollectionHealthRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeResourceCollectionHealthRequestPaginateTypeDef"
    ) = dataclasses.field()

    ResourceCollectionType = field("ResourceCollectionType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeResourceCollectionHealthRequestPaginateTypeDef"
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
                "type_defs.DescribeResourceCollectionHealthRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCostEstimationRequestPaginate:
    boto3_raw_data: "type_defs.GetCostEstimationRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCostEstimationRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCostEstimationRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceCollectionRequestPaginate:
    boto3_raw_data: "type_defs.GetResourceCollectionRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceCollectionType = field("ResourceCollectionType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetResourceCollectionRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceCollectionRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnomalousLogGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListAnomalousLogGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InsightId = field("InsightId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAnomalousLogGroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnomalousLogGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotificationChannelsRequestPaginate:
    boto3_raw_data: "type_defs.ListNotificationChannelsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListNotificationChannelsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotificationChannelsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationsRequestPaginate:
    boto3_raw_data: "type_defs.ListRecommendationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InsightId = field("InsightId")
    Locale = field("Locale")
    AccountId = field("AccountId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecommendationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMonitoredResourcesRequestPaginate:
    boto3_raw_data: "type_defs.ListMonitoredResourcesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListMonitoredResourcesFilters.make_one(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMonitoredResourcesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMonitoredResourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMonitoredResourcesRequest:
    boto3_raw_data: "type_defs.ListMonitoredResourcesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListMonitoredResourcesFilters.make_one(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMonitoredResourcesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMonitoredResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogAnomalyShowcase:
    boto3_raw_data: "type_defs.LogAnomalyShowcaseTypeDef" = dataclasses.field()

    @cached_property
    def LogAnomalyClasses(self):  # pragma: no cover
        return LogAnomalyClass.make_many(self.boto3_raw_data["LogAnomalyClasses"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LogAnomalyShowcaseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogAnomalyShowcaseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationChannelConfigOutput:
    boto3_raw_data: "type_defs.NotificationChannelConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Sns(self):  # pragma: no cover
        return SnsChannelConfig.make_one(self.boto3_raw_data["Sns"])

    @cached_property
    def Filters(self):  # pragma: no cover
        return NotificationFilterConfigOutput.make_one(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.NotificationChannelConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationChannelConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationChannelConfig:
    boto3_raw_data: "type_defs.NotificationChannelConfigTypeDef" = dataclasses.field()

    @cached_property
    def Sns(self):  # pragma: no cover
        return SnsChannelConfig.make_one(self.boto3_raw_data["Sns"])

    @cached_property
    def Filters(self):  # pragma: no cover
        return NotificationFilterConfig.make_one(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationChannelConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationChannelConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceIntegrationConfig:
    boto3_raw_data: "type_defs.UpdateServiceIntegrationConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OpsCenter(self):  # pragma: no cover
        return OpsCenterIntegrationConfig.make_one(self.boto3_raw_data["OpsCenter"])

    @cached_property
    def LogsAnomalyDetection(self):  # pragma: no cover
        return LogsAnomalyDetectionIntegrationConfig.make_one(
            self.boto3_raw_data["LogsAnomalyDetection"]
        )

    @cached_property
    def KMSServerSideEncryption(self):  # pragma: no cover
        return KMSServerSideEncryptionIntegrationConfig.make_one(
            self.boto3_raw_data["KMSServerSideEncryption"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateServiceIntegrationConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceIntegrationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceIntegrationConfig:
    boto3_raw_data: "type_defs.ServiceIntegrationConfigTypeDef" = dataclasses.field()

    @cached_property
    def OpsCenter(self):  # pragma: no cover
        return OpsCenterIntegration.make_one(self.boto3_raw_data["OpsCenter"])

    @cached_property
    def LogsAnomalyDetection(self):  # pragma: no cover
        return LogsAnomalyDetectionIntegration.make_one(
            self.boto3_raw_data["LogsAnomalyDetection"]
        )

    @cached_property
    def KMSServerSideEncryption(self):  # pragma: no cover
        return KMSServerSideEncryptionIntegration.make_one(
            self.boto3_raw_data["KMSServerSideEncryption"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceIntegrationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceIntegrationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PerformanceInsightsMetricQuery:
    boto3_raw_data: "type_defs.PerformanceInsightsMetricQueryTypeDef" = (
        dataclasses.field()
    )

    Metric = field("Metric")

    @cached_property
    def GroupBy(self):  # pragma: no cover
        return PerformanceInsightsMetricDimensionGroup.make_one(
            self.boto3_raw_data["GroupBy"]
        )

    Filter = field("Filter")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PerformanceInsightsMetricQueryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PerformanceInsightsMetricQueryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationRelatedAnomalySourceDetail:
    boto3_raw_data: "type_defs.RecommendationRelatedAnomalySourceDetailTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CloudWatchMetrics(self):  # pragma: no cover
        return RecommendationRelatedCloudWatchMetricsSourceDetail.make_many(
            self.boto3_raw_data["CloudWatchMetrics"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RecommendationRelatedAnomalySourceDetailTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationRelatedAnomalySourceDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationRelatedEvent:
    boto3_raw_data: "type_defs.RecommendationRelatedEventTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Resources(self):  # pragma: no cover
        return RecommendationRelatedEventResource.make_many(
            self.boto3_raw_data["Resources"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendationRelatedEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationRelatedEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceCollectionFilter:
    boto3_raw_data: "type_defs.ResourceCollectionFilterTypeDef" = dataclasses.field()

    @cached_property
    def CloudFormation(self):  # pragma: no cover
        return CloudFormationCollectionFilter.make_one(
            self.boto3_raw_data["CloudFormation"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagCollectionFilter.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceCollectionFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceCollectionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceCollectionOutput:
    boto3_raw_data: "type_defs.ResourceCollectionOutputTypeDef" = dataclasses.field()

    @cached_property
    def CloudFormation(self):  # pragma: no cover
        return CloudFormationCollectionOutput.make_one(
            self.boto3_raw_data["CloudFormation"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagCollectionOutput.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceCollectionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceCollectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceHealth:
    boto3_raw_data: "type_defs.ServiceHealthTypeDef" = dataclasses.field()

    ServiceName = field("ServiceName")

    @cached_property
    def Insight(self):  # pragma: no cover
        return ServiceInsightHealth.make_one(self.boto3_raw_data["Insight"])

    AnalyzedResourceCount = field("AnalyzedResourceCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceHealthTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceHealthTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResourceCollectionFilter:
    boto3_raw_data: "type_defs.UpdateResourceCollectionFilterTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CloudFormation(self):  # pragma: no cover
        return UpdateCloudFormationCollectionFilter.make_one(
            self.boto3_raw_data["CloudFormation"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return UpdateTagCollectionFilter.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateResourceCollectionFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResourceCollectionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventSourcesConfigResponse:
    boto3_raw_data: "type_defs.DescribeEventSourcesConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventSources(self):  # pragma: no cover
        return EventSourcesConfig.make_one(self.boto3_raw_data["EventSources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEventSourcesConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventSourcesConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEventSourcesConfigRequest:
    boto3_raw_data: "type_defs.UpdateEventSourcesConfigRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventSources(self):  # pragma: no cover
        return EventSourcesConfig.make_one(self.boto3_raw_data["EventSources"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateEventSourcesConfigRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEventSourcesConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchMetricsDetail:
    boto3_raw_data: "type_defs.CloudWatchMetricsDetailTypeDef" = dataclasses.field()

    MetricName = field("MetricName")
    Namespace = field("Namespace")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return CloudWatchMetricsDimension.make_many(self.boto3_raw_data["Dimensions"])

    Stat = field("Stat")
    Unit = field("Unit")
    Period = field("Period")

    @cached_property
    def MetricDataSummary(self):  # pragma: no cover
        return CloudWatchMetricsDataSummary.make_one(
            self.boto3_raw_data["MetricDataSummary"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchMetricsDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchMetricsDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCostEstimationResponse:
    boto3_raw_data: "type_defs.GetCostEstimationResponseTypeDef" = dataclasses.field()

    @cached_property
    def ResourceCollection(self):  # pragma: no cover
        return CostEstimationResourceCollectionFilterOutput.make_one(
            self.boto3_raw_data["ResourceCollection"]
        )

    Status = field("Status")

    @cached_property
    def Costs(self):  # pragma: no cover
        return ServiceResourceCost.make_many(self.boto3_raw_data["Costs"])

    @cached_property
    def TimeRange(self):  # pragma: no cover
        return CostEstimationTimeRange.make_one(self.boto3_raw_data["TimeRange"])

    TotalCost = field("TotalCost")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCostEstimationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCostEstimationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInsightsClosedStatusFilter:
    boto3_raw_data: "type_defs.ListInsightsClosedStatusFilterTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")

    @cached_property
    def EndTimeRange(self):  # pragma: no cover
        return EndTimeRange.make_one(self.boto3_raw_data["EndTimeRange"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInsightsClosedStatusFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInsightsClosedStatusFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInsightsAnyStatusFilter:
    boto3_raw_data: "type_defs.ListInsightsAnyStatusFilterTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def StartTimeRange(self):  # pragma: no cover
        return StartTimeRange.make_one(self.boto3_raw_data["StartTimeRange"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInsightsAnyStatusFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInsightsAnyStatusFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalousLogGroup:
    boto3_raw_data: "type_defs.AnomalousLogGroupTypeDef" = dataclasses.field()

    LogGroupName = field("LogGroupName")
    ImpactStartTime = field("ImpactStartTime")
    ImpactEndTime = field("ImpactEndTime")
    NumberOfLogLinesScanned = field("NumberOfLogLinesScanned")

    @cached_property
    def LogAnomalyShowcases(self):  # pragma: no cover
        return LogAnomalyShowcase.make_many(self.boto3_raw_data["LogAnomalyShowcases"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnomalousLogGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalousLogGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationChannel:
    boto3_raw_data: "type_defs.NotificationChannelTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def Config(self):  # pragma: no cover
        return NotificationChannelConfigOutput.make_one(self.boto3_raw_data["Config"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationChannelTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationChannelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceIntegrationRequest:
    boto3_raw_data: "type_defs.UpdateServiceIntegrationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServiceIntegration(self):  # pragma: no cover
        return UpdateServiceIntegrationConfig.make_one(
            self.boto3_raw_data["ServiceIntegration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateServiceIntegrationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceIntegrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceIntegrationResponse:
    boto3_raw_data: "type_defs.DescribeServiceIntegrationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServiceIntegration(self):  # pragma: no cover
        return ServiceIntegrationConfig.make_one(
            self.boto3_raw_data["ServiceIntegration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeServiceIntegrationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceIntegrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PerformanceInsightsReferenceMetric:
    boto3_raw_data: "type_defs.PerformanceInsightsReferenceMetricTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MetricQuery(self):  # pragma: no cover
        return PerformanceInsightsMetricQuery.make_one(
            self.boto3_raw_data["MetricQuery"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PerformanceInsightsReferenceMetricTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PerformanceInsightsReferenceMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationRelatedAnomaly:
    boto3_raw_data: "type_defs.RecommendationRelatedAnomalyTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Resources(self):  # pragma: no cover
        return RecommendationRelatedAnomalyResource.make_many(
            self.boto3_raw_data["Resources"]
        )

    @cached_property
    def SourceDetails(self):  # pragma: no cover
        return RecommendationRelatedAnomalySourceDetail.make_many(
            self.boto3_raw_data["SourceDetails"]
        )

    AnomalyId = field("AnomalyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendationRelatedAnomalyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationRelatedAnomalyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceCollectionResponse:
    boto3_raw_data: "type_defs.GetResourceCollectionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourceCollection(self):  # pragma: no cover
        return ResourceCollectionFilter.make_one(
            self.boto3_raw_data["ResourceCollection"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetResourceCollectionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceCollectionResponseTypeDef"]
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

    @cached_property
    def ResourceCollection(self):  # pragma: no cover
        return ResourceCollectionOutput.make_one(
            self.boto3_raw_data["ResourceCollection"]
        )

    Id = field("Id")
    Time = field("Time")
    EventSource = field("EventSource")
    Name = field("Name")
    DataSource = field("DataSource")
    EventClass = field("EventClass")

    @cached_property
    def Resources(self):  # pragma: no cover
        return EventResource.make_many(self.boto3_raw_data["Resources"])

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
class MonitoredResourceIdentifier:
    boto3_raw_data: "type_defs.MonitoredResourceIdentifierTypeDef" = dataclasses.field()

    MonitoredResourceName = field("MonitoredResourceName")
    Type = field("Type")
    ResourcePermission = field("ResourcePermission")
    LastUpdated = field("LastUpdated")

    @cached_property
    def ResourceCollection(self):  # pragma: no cover
        return ResourceCollectionOutput.make_one(
            self.boto3_raw_data["ResourceCollection"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MonitoredResourceIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MonitoredResourceIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProactiveInsightSummary:
    boto3_raw_data: "type_defs.ProactiveInsightSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Severity = field("Severity")
    Status = field("Status")

    @cached_property
    def InsightTimeRange(self):  # pragma: no cover
        return InsightTimeRange.make_one(self.boto3_raw_data["InsightTimeRange"])

    @cached_property
    def PredictionTimeRange(self):  # pragma: no cover
        return PredictionTimeRange.make_one(self.boto3_raw_data["PredictionTimeRange"])

    @cached_property
    def ResourceCollection(self):  # pragma: no cover
        return ResourceCollectionOutput.make_one(
            self.boto3_raw_data["ResourceCollection"]
        )

    @cached_property
    def ServiceCollection(self):  # pragma: no cover
        return ServiceCollectionOutput.make_one(
            self.boto3_raw_data["ServiceCollection"]
        )

    AssociatedResourceArns = field("AssociatedResourceArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProactiveInsightSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProactiveInsightSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProactiveInsight:
    boto3_raw_data: "type_defs.ProactiveInsightTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Severity = field("Severity")
    Status = field("Status")

    @cached_property
    def InsightTimeRange(self):  # pragma: no cover
        return InsightTimeRange.make_one(self.boto3_raw_data["InsightTimeRange"])

    @cached_property
    def PredictionTimeRange(self):  # pragma: no cover
        return PredictionTimeRange.make_one(self.boto3_raw_data["PredictionTimeRange"])

    @cached_property
    def ResourceCollection(self):  # pragma: no cover
        return ResourceCollectionOutput.make_one(
            self.boto3_raw_data["ResourceCollection"]
        )

    SsmOpsItemId = field("SsmOpsItemId")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProactiveInsightTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProactiveInsightTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProactiveOrganizationInsightSummary:
    boto3_raw_data: "type_defs.ProactiveOrganizationInsightSummaryTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    AccountId = field("AccountId")
    OrganizationalUnitId = field("OrganizationalUnitId")
    Name = field("Name")
    Severity = field("Severity")
    Status = field("Status")

    @cached_property
    def InsightTimeRange(self):  # pragma: no cover
        return InsightTimeRange.make_one(self.boto3_raw_data["InsightTimeRange"])

    @cached_property
    def PredictionTimeRange(self):  # pragma: no cover
        return PredictionTimeRange.make_one(self.boto3_raw_data["PredictionTimeRange"])

    @cached_property
    def ResourceCollection(self):  # pragma: no cover
        return ResourceCollectionOutput.make_one(
            self.boto3_raw_data["ResourceCollection"]
        )

    @cached_property
    def ServiceCollection(self):  # pragma: no cover
        return ServiceCollectionOutput.make_one(
            self.boto3_raw_data["ServiceCollection"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProactiveOrganizationInsightSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProactiveOrganizationInsightSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReactiveInsightSummary:
    boto3_raw_data: "type_defs.ReactiveInsightSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Severity = field("Severity")
    Status = field("Status")

    @cached_property
    def InsightTimeRange(self):  # pragma: no cover
        return InsightTimeRange.make_one(self.boto3_raw_data["InsightTimeRange"])

    @cached_property
    def ResourceCollection(self):  # pragma: no cover
        return ResourceCollectionOutput.make_one(
            self.boto3_raw_data["ResourceCollection"]
        )

    @cached_property
    def ServiceCollection(self):  # pragma: no cover
        return ServiceCollectionOutput.make_one(
            self.boto3_raw_data["ServiceCollection"]
        )

    AssociatedResourceArns = field("AssociatedResourceArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReactiveInsightSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReactiveInsightSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReactiveInsight:
    boto3_raw_data: "type_defs.ReactiveInsightTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Severity = field("Severity")
    Status = field("Status")

    @cached_property
    def InsightTimeRange(self):  # pragma: no cover
        return InsightTimeRange.make_one(self.boto3_raw_data["InsightTimeRange"])

    @cached_property
    def ResourceCollection(self):  # pragma: no cover
        return ResourceCollectionOutput.make_one(
            self.boto3_raw_data["ResourceCollection"]
        )

    SsmOpsItemId = field("SsmOpsItemId")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReactiveInsightTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReactiveInsightTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReactiveOrganizationInsightSummary:
    boto3_raw_data: "type_defs.ReactiveOrganizationInsightSummaryTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    AccountId = field("AccountId")
    OrganizationalUnitId = field("OrganizationalUnitId")
    Name = field("Name")
    Severity = field("Severity")
    Status = field("Status")

    @cached_property
    def InsightTimeRange(self):  # pragma: no cover
        return InsightTimeRange.make_one(self.boto3_raw_data["InsightTimeRange"])

    @cached_property
    def ResourceCollection(self):  # pragma: no cover
        return ResourceCollectionOutput.make_one(
            self.boto3_raw_data["ResourceCollection"]
        )

    @cached_property
    def ServiceCollection(self):  # pragma: no cover
        return ServiceCollectionOutput.make_one(
            self.boto3_raw_data["ServiceCollection"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReactiveOrganizationInsightSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReactiveOrganizationInsightSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnomaliesForInsightFilters:
    boto3_raw_data: "type_defs.ListAnomaliesForInsightFiltersTypeDef" = (
        dataclasses.field()
    )

    ServiceCollection = field("ServiceCollection")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAnomaliesForInsightFiltersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnomaliesForInsightFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationResourceCollectionHealthResponse:
    boto3_raw_data: (
        "type_defs.DescribeOrganizationResourceCollectionHealthResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def CloudFormation(self):  # pragma: no cover
        return CloudFormationHealth.make_many(self.boto3_raw_data["CloudFormation"])

    @cached_property
    def Service(self):  # pragma: no cover
        return ServiceHealth.make_many(self.boto3_raw_data["Service"])

    @cached_property
    def Account(self):  # pragma: no cover
        return AccountHealth.make_many(self.boto3_raw_data["Account"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagHealth.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationResourceCollectionHealthResponseTypeDef"
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
                "type_defs.DescribeOrganizationResourceCollectionHealthResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourceCollectionHealthResponse:
    boto3_raw_data: "type_defs.DescribeResourceCollectionHealthResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CloudFormation(self):  # pragma: no cover
        return CloudFormationHealth.make_many(self.boto3_raw_data["CloudFormation"])

    @cached_property
    def Service(self):  # pragma: no cover
        return ServiceHealth.make_many(self.boto3_raw_data["Service"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagHealth.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeResourceCollectionHealthResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourceCollectionHealthResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceCollection:
    boto3_raw_data: "type_defs.ResourceCollectionTypeDef" = dataclasses.field()

    CloudFormation = field("CloudFormation")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceCollectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceCollectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResourceCollectionRequest:
    boto3_raw_data: "type_defs.UpdateResourceCollectionRequestTypeDef" = (
        dataclasses.field()
    )

    Action = field("Action")

    @cached_property
    def ResourceCollection(self):  # pragma: no cover
        return UpdateResourceCollectionFilter.make_one(
            self.boto3_raw_data["ResourceCollection"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateResourceCollectionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResourceCollectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCostEstimationRequest:
    boto3_raw_data: "type_defs.StartCostEstimationRequestTypeDef" = dataclasses.field()

    ResourceCollection = field("ResourceCollection")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCostEstimationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCostEstimationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInsightsStatusFilter:
    boto3_raw_data: "type_defs.ListInsightsStatusFilterTypeDef" = dataclasses.field()

    @cached_property
    def Ongoing(self):  # pragma: no cover
        return ListInsightsOngoingStatusFilter.make_one(self.boto3_raw_data["Ongoing"])

    @cached_property
    def Closed(self):  # pragma: no cover
        return ListInsightsClosedStatusFilter.make_one(self.boto3_raw_data["Closed"])

    @cached_property
    def Any(self):  # pragma: no cover
        return ListInsightsAnyStatusFilter.make_one(self.boto3_raw_data["Any"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInsightsStatusFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInsightsStatusFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnomalousLogGroupsResponse:
    boto3_raw_data: "type_defs.ListAnomalousLogGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    InsightId = field("InsightId")

    @cached_property
    def AnomalousLogGroups(self):  # pragma: no cover
        return AnomalousLogGroup.make_many(self.boto3_raw_data["AnomalousLogGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAnomalousLogGroupsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnomalousLogGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotificationChannelsResponse:
    boto3_raw_data: "type_defs.ListNotificationChannelsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Channels(self):  # pragma: no cover
        return NotificationChannel.make_many(self.boto3_raw_data["Channels"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListNotificationChannelsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotificationChannelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddNotificationChannelRequest:
    boto3_raw_data: "type_defs.AddNotificationChannelRequestTypeDef" = (
        dataclasses.field()
    )

    Config = field("Config")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddNotificationChannelRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddNotificationChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PerformanceInsightsReferenceComparisonValues:
    boto3_raw_data: "type_defs.PerformanceInsightsReferenceComparisonValuesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReferenceScalar(self):  # pragma: no cover
        return PerformanceInsightsReferenceScalar.make_one(
            self.boto3_raw_data["ReferenceScalar"]
        )

    @cached_property
    def ReferenceMetric(self):  # pragma: no cover
        return PerformanceInsightsReferenceMetric.make_one(
            self.boto3_raw_data["ReferenceMetric"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PerformanceInsightsReferenceComparisonValuesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PerformanceInsightsReferenceComparisonValuesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Recommendation:
    boto3_raw_data: "type_defs.RecommendationTypeDef" = dataclasses.field()

    Description = field("Description")
    Link = field("Link")
    Name = field("Name")
    Reason = field("Reason")

    @cached_property
    def RelatedEvents(self):  # pragma: no cover
        return RecommendationRelatedEvent.make_many(
            self.boto3_raw_data["RelatedEvents"]
        )

    @cached_property
    def RelatedAnomalies(self):  # pragma: no cover
        return RecommendationRelatedAnomaly.make_many(
            self.boto3_raw_data["RelatedAnomalies"]
        )

    Category = field("Category")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecommendationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecommendationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventsResponse:
    boto3_raw_data: "type_defs.ListEventsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Events(self):  # pragma: no cover
        return Event.make_many(self.boto3_raw_data["Events"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEventsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMonitoredResourcesResponse:
    boto3_raw_data: "type_defs.ListMonitoredResourcesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MonitoredResourceIdentifiers(self):  # pragma: no cover
        return MonitoredResourceIdentifier.make_many(
            self.boto3_raw_data["MonitoredResourceIdentifiers"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMonitoredResourcesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMonitoredResourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInsightsResponse:
    boto3_raw_data: "type_defs.ListInsightsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ProactiveInsights(self):  # pragma: no cover
        return ProactiveInsightSummary.make_many(
            self.boto3_raw_data["ProactiveInsights"]
        )

    @cached_property
    def ReactiveInsights(self):  # pragma: no cover
        return ReactiveInsightSummary.make_many(self.boto3_raw_data["ReactiveInsights"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInsightsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInsightsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchInsightsResponse:
    boto3_raw_data: "type_defs.SearchInsightsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ProactiveInsights(self):  # pragma: no cover
        return ProactiveInsightSummary.make_many(
            self.boto3_raw_data["ProactiveInsights"]
        )

    @cached_property
    def ReactiveInsights(self):  # pragma: no cover
        return ReactiveInsightSummary.make_many(self.boto3_raw_data["ReactiveInsights"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchInsightsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchInsightsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchOrganizationInsightsResponse:
    boto3_raw_data: "type_defs.SearchOrganizationInsightsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ProactiveInsights(self):  # pragma: no cover
        return ProactiveInsightSummary.make_many(
            self.boto3_raw_data["ProactiveInsights"]
        )

    @cached_property
    def ReactiveInsights(self):  # pragma: no cover
        return ReactiveInsightSummary.make_many(self.boto3_raw_data["ReactiveInsights"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchOrganizationInsightsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchOrganizationInsightsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInsightResponse:
    boto3_raw_data: "type_defs.DescribeInsightResponseTypeDef" = dataclasses.field()

    @cached_property
    def ProactiveInsight(self):  # pragma: no cover
        return ProactiveInsight.make_one(self.boto3_raw_data["ProactiveInsight"])

    @cached_property
    def ReactiveInsight(self):  # pragma: no cover
        return ReactiveInsight.make_one(self.boto3_raw_data["ReactiveInsight"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInsightResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInsightResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationInsightsResponse:
    boto3_raw_data: "type_defs.ListOrganizationInsightsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ProactiveInsights(self):  # pragma: no cover
        return ProactiveOrganizationInsightSummary.make_many(
            self.boto3_raw_data["ProactiveInsights"]
        )

    @cached_property
    def ReactiveInsights(self):  # pragma: no cover
        return ReactiveOrganizationInsightSummary.make_many(
            self.boto3_raw_data["ReactiveInsights"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOrganizationInsightsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationInsightsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnomaliesForInsightRequestPaginate:
    boto3_raw_data: "type_defs.ListAnomaliesForInsightRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InsightId = field("InsightId")

    @cached_property
    def StartTimeRange(self):  # pragma: no cover
        return StartTimeRange.make_one(self.boto3_raw_data["StartTimeRange"])

    AccountId = field("AccountId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListAnomaliesForInsightFilters.make_one(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAnomaliesForInsightRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnomaliesForInsightRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnomaliesForInsightRequest:
    boto3_raw_data: "type_defs.ListAnomaliesForInsightRequestTypeDef" = (
        dataclasses.field()
    )

    InsightId = field("InsightId")

    @cached_property
    def StartTimeRange(self):  # pragma: no cover
        return StartTimeRange.make_one(self.boto3_raw_data["StartTimeRange"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    AccountId = field("AccountId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListAnomaliesForInsightFilters.make_one(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAnomaliesForInsightRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnomaliesForInsightRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInsightsRequestPaginate:
    boto3_raw_data: "type_defs.ListInsightsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def StatusFilter(self):  # pragma: no cover
        return ListInsightsStatusFilter.make_one(self.boto3_raw_data["StatusFilter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInsightsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInsightsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInsightsRequest:
    boto3_raw_data: "type_defs.ListInsightsRequestTypeDef" = dataclasses.field()

    @cached_property
    def StatusFilter(self):  # pragma: no cover
        return ListInsightsStatusFilter.make_one(self.boto3_raw_data["StatusFilter"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInsightsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInsightsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationInsightsRequestPaginate:
    boto3_raw_data: "type_defs.ListOrganizationInsightsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StatusFilter(self):  # pragma: no cover
        return ListInsightsStatusFilter.make_one(self.boto3_raw_data["StatusFilter"])

    AccountIds = field("AccountIds")
    OrganizationalUnitIds = field("OrganizationalUnitIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationInsightsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationInsightsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationInsightsRequest:
    boto3_raw_data: "type_defs.ListOrganizationInsightsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StatusFilter(self):  # pragma: no cover
        return ListInsightsStatusFilter.make_one(self.boto3_raw_data["StatusFilter"])

    MaxResults = field("MaxResults")
    AccountIds = field("AccountIds")
    OrganizationalUnitIds = field("OrganizationalUnitIds")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOrganizationInsightsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationInsightsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PerformanceInsightsReferenceData:
    boto3_raw_data: "type_defs.PerformanceInsightsReferenceDataTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @cached_property
    def ComparisonValues(self):  # pragma: no cover
        return PerformanceInsightsReferenceComparisonValues.make_one(
            self.boto3_raw_data["ComparisonValues"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PerformanceInsightsReferenceDataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PerformanceInsightsReferenceDataTypeDef"]
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
    def Recommendations(self):  # pragma: no cover
        return Recommendation.make_many(self.boto3_raw_data["Recommendations"])

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
class ListEventsFilters:
    boto3_raw_data: "type_defs.ListEventsFiltersTypeDef" = dataclasses.field()

    InsightId = field("InsightId")

    @cached_property
    def EventTimeRange(self):  # pragma: no cover
        return EventTimeRange.make_one(self.boto3_raw_data["EventTimeRange"])

    EventClass = field("EventClass")
    EventSource = field("EventSource")
    DataSource = field("DataSource")
    ResourceCollection = field("ResourceCollection")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListEventsFiltersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventsFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchInsightsFilters:
    boto3_raw_data: "type_defs.SearchInsightsFiltersTypeDef" = dataclasses.field()

    Severities = field("Severities")
    Statuses = field("Statuses")
    ResourceCollection = field("ResourceCollection")
    ServiceCollection = field("ServiceCollection")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchInsightsFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchInsightsFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchOrganizationInsightsFilters:
    boto3_raw_data: "type_defs.SearchOrganizationInsightsFiltersTypeDef" = (
        dataclasses.field()
    )

    Severities = field("Severities")
    Statuses = field("Statuses")
    ResourceCollection = field("ResourceCollection")
    ServiceCollection = field("ServiceCollection")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchOrganizationInsightsFiltersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchOrganizationInsightsFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PerformanceInsightsMetricsDetail:
    boto3_raw_data: "type_defs.PerformanceInsightsMetricsDetailTypeDef" = (
        dataclasses.field()
    )

    MetricDisplayName = field("MetricDisplayName")
    Unit = field("Unit")

    @cached_property
    def MetricQuery(self):  # pragma: no cover
        return PerformanceInsightsMetricQuery.make_one(
            self.boto3_raw_data["MetricQuery"]
        )

    @cached_property
    def ReferenceData(self):  # pragma: no cover
        return PerformanceInsightsReferenceData.make_many(
            self.boto3_raw_data["ReferenceData"]
        )

    @cached_property
    def StatsAtAnomaly(self):  # pragma: no cover
        return PerformanceInsightsStat.make_many(self.boto3_raw_data["StatsAtAnomaly"])

    @cached_property
    def StatsAtBaseline(self):  # pragma: no cover
        return PerformanceInsightsStat.make_many(self.boto3_raw_data["StatsAtBaseline"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PerformanceInsightsMetricsDetailTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PerformanceInsightsMetricsDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventsRequestPaginate:
    boto3_raw_data: "type_defs.ListEventsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListEventsFilters.make_one(self.boto3_raw_data["Filters"])

    AccountId = field("AccountId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEventsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventsRequest:
    boto3_raw_data: "type_defs.ListEventsRequestTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListEventsFilters.make_one(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    AccountId = field("AccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListEventsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchInsightsRequestPaginate:
    boto3_raw_data: "type_defs.SearchInsightsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StartTimeRange(self):  # pragma: no cover
        return StartTimeRange.make_one(self.boto3_raw_data["StartTimeRange"])

    Type = field("Type")

    @cached_property
    def Filters(self):  # pragma: no cover
        return SearchInsightsFilters.make_one(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchInsightsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchInsightsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchInsightsRequest:
    boto3_raw_data: "type_defs.SearchInsightsRequestTypeDef" = dataclasses.field()

    @cached_property
    def StartTimeRange(self):  # pragma: no cover
        return StartTimeRange.make_one(self.boto3_raw_data["StartTimeRange"])

    Type = field("Type")

    @cached_property
    def Filters(self):  # pragma: no cover
        return SearchInsightsFilters.make_one(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchInsightsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchInsightsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchOrganizationInsightsRequestPaginate:
    boto3_raw_data: "type_defs.SearchOrganizationInsightsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AccountIds = field("AccountIds")

    @cached_property
    def StartTimeRange(self):  # pragma: no cover
        return StartTimeRange.make_one(self.boto3_raw_data["StartTimeRange"])

    Type = field("Type")

    @cached_property
    def Filters(self):  # pragma: no cover
        return SearchOrganizationInsightsFilters.make_one(
            self.boto3_raw_data["Filters"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchOrganizationInsightsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchOrganizationInsightsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchOrganizationInsightsRequest:
    boto3_raw_data: "type_defs.SearchOrganizationInsightsRequestTypeDef" = (
        dataclasses.field()
    )

    AccountIds = field("AccountIds")

    @cached_property
    def StartTimeRange(self):  # pragma: no cover
        return StartTimeRange.make_one(self.boto3_raw_data["StartTimeRange"])

    Type = field("Type")

    @cached_property
    def Filters(self):  # pragma: no cover
        return SearchOrganizationInsightsFilters.make_one(
            self.boto3_raw_data["Filters"]
        )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchOrganizationInsightsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchOrganizationInsightsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalySourceDetails:
    boto3_raw_data: "type_defs.AnomalySourceDetailsTypeDef" = dataclasses.field()

    @cached_property
    def CloudWatchMetrics(self):  # pragma: no cover
        return CloudWatchMetricsDetail.make_many(
            self.boto3_raw_data["CloudWatchMetrics"]
        )

    @cached_property
    def PerformanceInsightsMetrics(self):  # pragma: no cover
        return PerformanceInsightsMetricsDetail.make_many(
            self.boto3_raw_data["PerformanceInsightsMetrics"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnomalySourceDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalySourceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProactiveAnomalySummary:
    boto3_raw_data: "type_defs.ProactiveAnomalySummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Severity = field("Severity")
    Status = field("Status")
    UpdateTime = field("UpdateTime")

    @cached_property
    def AnomalyTimeRange(self):  # pragma: no cover
        return AnomalyTimeRange.make_one(self.boto3_raw_data["AnomalyTimeRange"])

    @cached_property
    def AnomalyReportedTimeRange(self):  # pragma: no cover
        return AnomalyReportedTimeRange.make_one(
            self.boto3_raw_data["AnomalyReportedTimeRange"]
        )

    @cached_property
    def PredictionTimeRange(self):  # pragma: no cover
        return PredictionTimeRange.make_one(self.boto3_raw_data["PredictionTimeRange"])

    @cached_property
    def SourceDetails(self):  # pragma: no cover
        return AnomalySourceDetails.make_one(self.boto3_raw_data["SourceDetails"])

    AssociatedInsightId = field("AssociatedInsightId")

    @cached_property
    def ResourceCollection(self):  # pragma: no cover
        return ResourceCollectionOutput.make_one(
            self.boto3_raw_data["ResourceCollection"]
        )

    Limit = field("Limit")

    @cached_property
    def SourceMetadata(self):  # pragma: no cover
        return AnomalySourceMetadata.make_one(self.boto3_raw_data["SourceMetadata"])

    @cached_property
    def AnomalyResources(self):  # pragma: no cover
        return AnomalyResource.make_many(self.boto3_raw_data["AnomalyResources"])

    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProactiveAnomalySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProactiveAnomalySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProactiveAnomaly:
    boto3_raw_data: "type_defs.ProactiveAnomalyTypeDef" = dataclasses.field()

    Id = field("Id")
    Severity = field("Severity")
    Status = field("Status")
    UpdateTime = field("UpdateTime")

    @cached_property
    def AnomalyTimeRange(self):  # pragma: no cover
        return AnomalyTimeRange.make_one(self.boto3_raw_data["AnomalyTimeRange"])

    @cached_property
    def AnomalyReportedTimeRange(self):  # pragma: no cover
        return AnomalyReportedTimeRange.make_one(
            self.boto3_raw_data["AnomalyReportedTimeRange"]
        )

    @cached_property
    def PredictionTimeRange(self):  # pragma: no cover
        return PredictionTimeRange.make_one(self.boto3_raw_data["PredictionTimeRange"])

    @cached_property
    def SourceDetails(self):  # pragma: no cover
        return AnomalySourceDetails.make_one(self.boto3_raw_data["SourceDetails"])

    AssociatedInsightId = field("AssociatedInsightId")

    @cached_property
    def ResourceCollection(self):  # pragma: no cover
        return ResourceCollectionOutput.make_one(
            self.boto3_raw_data["ResourceCollection"]
        )

    Limit = field("Limit")

    @cached_property
    def SourceMetadata(self):  # pragma: no cover
        return AnomalySourceMetadata.make_one(self.boto3_raw_data["SourceMetadata"])

    @cached_property
    def AnomalyResources(self):  # pragma: no cover
        return AnomalyResource.make_many(self.boto3_raw_data["AnomalyResources"])

    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProactiveAnomalyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProactiveAnomalyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReactiveAnomalySummary:
    boto3_raw_data: "type_defs.ReactiveAnomalySummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Severity = field("Severity")
    Status = field("Status")

    @cached_property
    def AnomalyTimeRange(self):  # pragma: no cover
        return AnomalyTimeRange.make_one(self.boto3_raw_data["AnomalyTimeRange"])

    @cached_property
    def AnomalyReportedTimeRange(self):  # pragma: no cover
        return AnomalyReportedTimeRange.make_one(
            self.boto3_raw_data["AnomalyReportedTimeRange"]
        )

    @cached_property
    def SourceDetails(self):  # pragma: no cover
        return AnomalySourceDetails.make_one(self.boto3_raw_data["SourceDetails"])

    AssociatedInsightId = field("AssociatedInsightId")

    @cached_property
    def ResourceCollection(self):  # pragma: no cover
        return ResourceCollectionOutput.make_one(
            self.boto3_raw_data["ResourceCollection"]
        )

    Type = field("Type")
    Name = field("Name")
    Description = field("Description")
    CausalAnomalyId = field("CausalAnomalyId")

    @cached_property
    def AnomalyResources(self):  # pragma: no cover
        return AnomalyResource.make_many(self.boto3_raw_data["AnomalyResources"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReactiveAnomalySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReactiveAnomalySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReactiveAnomaly:
    boto3_raw_data: "type_defs.ReactiveAnomalyTypeDef" = dataclasses.field()

    Id = field("Id")
    Severity = field("Severity")
    Status = field("Status")

    @cached_property
    def AnomalyTimeRange(self):  # pragma: no cover
        return AnomalyTimeRange.make_one(self.boto3_raw_data["AnomalyTimeRange"])

    @cached_property
    def AnomalyReportedTimeRange(self):  # pragma: no cover
        return AnomalyReportedTimeRange.make_one(
            self.boto3_raw_data["AnomalyReportedTimeRange"]
        )

    @cached_property
    def SourceDetails(self):  # pragma: no cover
        return AnomalySourceDetails.make_one(self.boto3_raw_data["SourceDetails"])

    AssociatedInsightId = field("AssociatedInsightId")

    @cached_property
    def ResourceCollection(self):  # pragma: no cover
        return ResourceCollectionOutput.make_one(
            self.boto3_raw_data["ResourceCollection"]
        )

    Type = field("Type")
    Name = field("Name")
    Description = field("Description")
    CausalAnomalyId = field("CausalAnomalyId")

    @cached_property
    def AnomalyResources(self):  # pragma: no cover
        return AnomalyResource.make_many(self.boto3_raw_data["AnomalyResources"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReactiveAnomalyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReactiveAnomalyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnomaliesForInsightResponse:
    boto3_raw_data: "type_defs.ListAnomaliesForInsightResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ProactiveAnomalies(self):  # pragma: no cover
        return ProactiveAnomalySummary.make_many(
            self.boto3_raw_data["ProactiveAnomalies"]
        )

    @cached_property
    def ReactiveAnomalies(self):  # pragma: no cover
        return ReactiveAnomalySummary.make_many(
            self.boto3_raw_data["ReactiveAnomalies"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAnomaliesForInsightResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnomaliesForInsightResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAnomalyResponse:
    boto3_raw_data: "type_defs.DescribeAnomalyResponseTypeDef" = dataclasses.field()

    @cached_property
    def ProactiveAnomaly(self):  # pragma: no cover
        return ProactiveAnomaly.make_one(self.boto3_raw_data["ProactiveAnomaly"])

    @cached_property
    def ReactiveAnomaly(self):  # pragma: no cover
        return ReactiveAnomaly.make_one(self.boto3_raw_data["ReactiveAnomaly"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAnomalyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAnomalyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
