# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cloudsearchdomain import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Bucket:
    boto3_raw_data: "type_defs.BucketTypeDef" = dataclasses.field()

    value = field("value")
    count = field("count")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BucketTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BucketTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentServiceWarning:
    boto3_raw_data: "type_defs.DocumentServiceWarningTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentServiceWarningTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentServiceWarningTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldStats:
    boto3_raw_data: "type_defs.FieldStatsTypeDef" = dataclasses.field()

    min = field("min")
    max = field("max")
    count = field("count")
    missing = field("missing")
    sum = field("sum")
    sumOfSquares = field("sumOfSquares")
    mean = field("mean")
    stddev = field("stddev")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldStatsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldStatsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Hit:
    boto3_raw_data: "type_defs.HitTypeDef" = dataclasses.field()

    id = field("id")
    fields = field("fields")
    exprs = field("exprs")
    highlights = field("highlights")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HitTypeDef"]]
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
class SearchRequest:
    boto3_raw_data: "type_defs.SearchRequestTypeDef" = dataclasses.field()

    query = field("query")
    cursor = field("cursor")
    expr = field("expr")
    facet = field("facet")
    filterQuery = field("filterQuery")
    highlight = field("highlight")
    partial = field("partial")
    queryOptions = field("queryOptions")
    queryParser = field("queryParser")
    returnFields = field("returnFields")
    size = field("size")
    sort = field("sort")
    start = field("start")
    stats = field("stats")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SearchRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchStatus:
    boto3_raw_data: "type_defs.SearchStatusTypeDef" = dataclasses.field()

    timems = field("timems")
    rid = field("rid")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SearchStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuggestionMatch:
    boto3_raw_data: "type_defs.SuggestionMatchTypeDef" = dataclasses.field()

    suggestion = field("suggestion")
    score = field("score")
    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SuggestionMatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SuggestionMatchTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuggestRequest:
    boto3_raw_data: "type_defs.SuggestRequestTypeDef" = dataclasses.field()

    query = field("query")
    suggester = field("suggester")
    size = field("size")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SuggestRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SuggestRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuggestStatus:
    boto3_raw_data: "type_defs.SuggestStatusTypeDef" = dataclasses.field()

    timems = field("timems")
    rid = field("rid")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SuggestStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SuggestStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadDocumentsRequest:
    boto3_raw_data: "type_defs.UploadDocumentsRequestTypeDef" = dataclasses.field()

    documents = field("documents")
    contentType = field("contentType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UploadDocumentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadDocumentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketInfo:
    boto3_raw_data: "type_defs.BucketInfoTypeDef" = dataclasses.field()

    @cached_property
    def buckets(self):  # pragma: no cover
        return Bucket.make_many(self.boto3_raw_data["buckets"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BucketInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BucketInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Hits:
    boto3_raw_data: "type_defs.HitsTypeDef" = dataclasses.field()

    found = field("found")
    start = field("start")
    cursor = field("cursor")

    @cached_property
    def hit(self):  # pragma: no cover
        return Hit.make_many(self.boto3_raw_data["hit"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HitsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HitsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadDocumentsResponse:
    boto3_raw_data: "type_defs.UploadDocumentsResponseTypeDef" = dataclasses.field()

    status = field("status")
    adds = field("adds")
    deletes = field("deletes")

    @cached_property
    def warnings(self):  # pragma: no cover
        return DocumentServiceWarning.make_many(self.boto3_raw_data["warnings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UploadDocumentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadDocumentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuggestModel:
    boto3_raw_data: "type_defs.SuggestModelTypeDef" = dataclasses.field()

    query = field("query")
    found = field("found")

    @cached_property
    def suggestions(self):  # pragma: no cover
        return SuggestionMatch.make_many(self.boto3_raw_data["suggestions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SuggestModelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SuggestModelTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchResponse:
    boto3_raw_data: "type_defs.SearchResponseTypeDef" = dataclasses.field()

    @cached_property
    def status(self):  # pragma: no cover
        return SearchStatus.make_one(self.boto3_raw_data["status"])

    @cached_property
    def hits(self):  # pragma: no cover
        return Hits.make_one(self.boto3_raw_data["hits"])

    facets = field("facets")
    stats = field("stats")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SearchResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuggestResponse:
    boto3_raw_data: "type_defs.SuggestResponseTypeDef" = dataclasses.field()

    @cached_property
    def status(self):  # pragma: no cover
        return SuggestStatus.make_one(self.boto3_raw_data["status"])

    @cached_property
    def suggest(self):  # pragma: no cover
        return SuggestModel.make_one(self.boto3_raw_data["suggest"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SuggestResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SuggestResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
