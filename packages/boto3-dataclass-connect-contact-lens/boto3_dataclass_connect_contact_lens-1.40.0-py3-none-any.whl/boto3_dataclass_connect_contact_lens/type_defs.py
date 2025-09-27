# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_connect_contact_lens import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class PointOfInterest:
    boto3_raw_data: "type_defs.PointOfInterestTypeDef" = dataclasses.field()

    BeginOffsetMillis = field("BeginOffsetMillis")
    EndOffsetMillis = field("EndOffsetMillis")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PointOfInterestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PointOfInterestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CharacterOffsets:
    boto3_raw_data: "type_defs.CharacterOffsetsTypeDef" = dataclasses.field()

    BeginOffsetChar = field("BeginOffsetChar")
    EndOffsetChar = field("EndOffsetChar")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CharacterOffsetsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CharacterOffsetsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRealtimeContactAnalysisSegmentsRequest:
    boto3_raw_data: "type_defs.ListRealtimeContactAnalysisSegmentsRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRealtimeContactAnalysisSegmentsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRealtimeContactAnalysisSegmentsRequestTypeDef"]
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
class PostContactSummary:
    boto3_raw_data: "type_defs.PostContactSummaryTypeDef" = dataclasses.field()

    Status = field("Status")
    Content = field("Content")
    FailureCode = field("FailureCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PostContactSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostContactSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CategoryDetails:
    boto3_raw_data: "type_defs.CategoryDetailsTypeDef" = dataclasses.field()

    @cached_property
    def PointsOfInterest(self):  # pragma: no cover
        return PointOfInterest.make_many(self.boto3_raw_data["PointsOfInterest"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CategoryDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CategoryDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IssueDetected:
    boto3_raw_data: "type_defs.IssueDetectedTypeDef" = dataclasses.field()

    @cached_property
    def CharacterOffsets(self):  # pragma: no cover
        return CharacterOffsets.make_one(self.boto3_raw_data["CharacterOffsets"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IssueDetectedTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IssueDetectedTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Categories:
    boto3_raw_data: "type_defs.CategoriesTypeDef" = dataclasses.field()

    MatchedCategories = field("MatchedCategories")
    MatchedDetails = field("MatchedDetails")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CategoriesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CategoriesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Transcript:
    boto3_raw_data: "type_defs.TranscriptTypeDef" = dataclasses.field()

    Id = field("Id")
    ParticipantId = field("ParticipantId")
    ParticipantRole = field("ParticipantRole")
    Content = field("Content")
    BeginOffsetMillis = field("BeginOffsetMillis")
    EndOffsetMillis = field("EndOffsetMillis")
    Sentiment = field("Sentiment")

    @cached_property
    def IssuesDetected(self):  # pragma: no cover
        return IssueDetected.make_many(self.boto3_raw_data["IssuesDetected"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TranscriptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TranscriptTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealtimeContactAnalysisSegment:
    boto3_raw_data: "type_defs.RealtimeContactAnalysisSegmentTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Transcript(self):  # pragma: no cover
        return Transcript.make_one(self.boto3_raw_data["Transcript"])

    @cached_property
    def Categories(self):  # pragma: no cover
        return Categories.make_one(self.boto3_raw_data["Categories"])

    @cached_property
    def PostContactSummary(self):  # pragma: no cover
        return PostContactSummary.make_one(self.boto3_raw_data["PostContactSummary"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RealtimeContactAnalysisSegmentTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RealtimeContactAnalysisSegmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRealtimeContactAnalysisSegmentsResponse:
    boto3_raw_data: "type_defs.ListRealtimeContactAnalysisSegmentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Segments(self):  # pragma: no cover
        return RealtimeContactAnalysisSegment.make_many(self.boto3_raw_data["Segments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRealtimeContactAnalysisSegmentsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRealtimeContactAnalysisSegmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
