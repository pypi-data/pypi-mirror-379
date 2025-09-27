# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_comprehend import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AugmentedManifestsListItemOutput:
    boto3_raw_data: "type_defs.AugmentedManifestsListItemOutputTypeDef" = (
        dataclasses.field()
    )

    S3Uri = field("S3Uri")
    AttributeNames = field("AttributeNames")
    Split = field("Split")
    AnnotationDataS3Uri = field("AnnotationDataS3Uri")
    SourceDocumentsS3Uri = field("SourceDocumentsS3Uri")
    DocumentType = field("DocumentType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AugmentedManifestsListItemOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AugmentedManifestsListItemOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AugmentedManifestsListItem:
    boto3_raw_data: "type_defs.AugmentedManifestsListItemTypeDef" = dataclasses.field()

    S3Uri = field("S3Uri")
    AttributeNames = field("AttributeNames")
    Split = field("Split")
    AnnotationDataS3Uri = field("AnnotationDataS3Uri")
    SourceDocumentsS3Uri = field("SourceDocumentsS3Uri")
    DocumentType = field("DocumentType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AugmentedManifestsListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AugmentedManifestsListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DominantLanguage:
    boto3_raw_data: "type_defs.DominantLanguageTypeDef" = dataclasses.field()

    LanguageCode = field("LanguageCode")
    Score = field("Score")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DominantLanguageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DominantLanguageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetectDominantLanguageRequest:
    boto3_raw_data: "type_defs.BatchDetectDominantLanguageRequestTypeDef" = (
        dataclasses.field()
    )

    TextList = field("TextList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDetectDominantLanguageRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetectDominantLanguageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchItemError:
    boto3_raw_data: "type_defs.BatchItemErrorTypeDef" = dataclasses.field()

    Index = field("Index")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchItemErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BatchItemErrorTypeDef"]],
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
class BatchDetectEntitiesRequest:
    boto3_raw_data: "type_defs.BatchDetectEntitiesRequestTypeDef" = dataclasses.field()

    TextList = field("TextList")
    LanguageCode = field("LanguageCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDetectEntitiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetectEntitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyPhrase:
    boto3_raw_data: "type_defs.KeyPhraseTypeDef" = dataclasses.field()

    Score = field("Score")
    Text = field("Text")
    BeginOffset = field("BeginOffset")
    EndOffset = field("EndOffset")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyPhraseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyPhraseTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetectKeyPhrasesRequest:
    boto3_raw_data: "type_defs.BatchDetectKeyPhrasesRequestTypeDef" = (
        dataclasses.field()
    )

    TextList = field("TextList")
    LanguageCode = field("LanguageCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDetectKeyPhrasesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetectKeyPhrasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SentimentScore:
    boto3_raw_data: "type_defs.SentimentScoreTypeDef" = dataclasses.field()

    Positive = field("Positive")
    Negative = field("Negative")
    Neutral = field("Neutral")
    Mixed = field("Mixed")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SentimentScoreTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SentimentScoreTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetectSentimentRequest:
    boto3_raw_data: "type_defs.BatchDetectSentimentRequestTypeDef" = dataclasses.field()

    TextList = field("TextList")
    LanguageCode = field("LanguageCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDetectSentimentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetectSentimentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetectSyntaxRequest:
    boto3_raw_data: "type_defs.BatchDetectSyntaxRequestTypeDef" = dataclasses.field()

    TextList = field("TextList")
    LanguageCode = field("LanguageCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDetectSyntaxRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetectSyntaxRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetectTargetedSentimentRequest:
    boto3_raw_data: "type_defs.BatchDetectTargetedSentimentRequestTypeDef" = (
        dataclasses.field()
    )

    TextList = field("TextList")
    LanguageCode = field("LanguageCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDetectTargetedSentimentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetectTargetedSentimentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChildBlock:
    boto3_raw_data: "type_defs.ChildBlockTypeDef" = dataclasses.field()

    ChildBlockId = field("ChildBlockId")
    BeginOffset = field("BeginOffset")
    EndOffset = field("EndOffset")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChildBlockTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChildBlockTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelationshipsListItem:
    boto3_raw_data: "type_defs.RelationshipsListItemTypeDef" = dataclasses.field()

    Ids = field("Ids")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RelationshipsListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelationshipsListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BoundingBox:
    boto3_raw_data: "type_defs.BoundingBoxTypeDef" = dataclasses.field()

    Height = field("Height")
    Left = field("Left")
    Top = field("Top")
    Width = field("Width")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BoundingBoxTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BoundingBoxTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClassifierEvaluationMetrics:
    boto3_raw_data: "type_defs.ClassifierEvaluationMetricsTypeDef" = dataclasses.field()

    Accuracy = field("Accuracy")
    Precision = field("Precision")
    Recall = field("Recall")
    F1Score = field("F1Score")
    MicroPrecision = field("MicroPrecision")
    MicroRecall = field("MicroRecall")
    MicroF1Score = field("MicroF1Score")
    HammingLoss = field("HammingLoss")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClassifierEvaluationMetricsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClassifierEvaluationMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentClass:
    boto3_raw_data: "type_defs.DocumentClassTypeDef" = dataclasses.field()

    Name = field("Name")
    Score = field("Score")
    Page = field("Page")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentClassTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DocumentClassTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentLabel:
    boto3_raw_data: "type_defs.DocumentLabelTypeDef" = dataclasses.field()

    Name = field("Name")
    Score = field("Score")
    Page = field("Page")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentLabelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DocumentLabelTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentTypeListItem:
    boto3_raw_data: "type_defs.DocumentTypeListItemTypeDef" = dataclasses.field()

    Page = field("Page")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentTypeListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentTypeListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorsListItem:
    boto3_raw_data: "type_defs.ErrorsListItemTypeDef" = dataclasses.field()

    Page = field("Page")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorsListItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorsListItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WarningsListItem:
    boto3_raw_data: "type_defs.WarningsListItemTypeDef" = dataclasses.field()

    Page = field("Page")
    WarnCode = field("WarnCode")
    WarnMessage = field("WarnMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WarningsListItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WarningsListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainsPiiEntitiesRequest:
    boto3_raw_data: "type_defs.ContainsPiiEntitiesRequestTypeDef" = dataclasses.field()

    Text = field("Text")
    LanguageCode = field("LanguageCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainsPiiEntitiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainsPiiEntitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityLabel:
    boto3_raw_data: "type_defs.EntityLabelTypeDef" = dataclasses.field()

    Name = field("Name")
    Score = field("Score")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntityLabelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntityLabelTypeDef"]]
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
class DocumentClassifierOutputDataConfig:
    boto3_raw_data: "type_defs.DocumentClassifierOutputDataConfigTypeDef" = (
        dataclasses.field()
    )

    S3Uri = field("S3Uri")
    KmsKeyId = field("KmsKeyId")
    FlywheelStatsS3Prefix = field("FlywheelStatsS3Prefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DocumentClassifierOutputDataConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentClassifierOutputDataConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfigOutput:
    boto3_raw_data: "type_defs.VpcConfigOutputTypeDef" = dataclasses.field()

    SecurityGroupIds = field("SecurityGroupIds")
    Subnets = field("Subnets")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcConfigOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfig:
    boto3_raw_data: "type_defs.VpcConfigTypeDef" = dataclasses.field()

    SecurityGroupIds = field("SecurityGroupIds")
    Subnets = field("Subnets")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetAugmentedManifestsListItem:
    boto3_raw_data: "type_defs.DatasetAugmentedManifestsListItemTypeDef" = (
        dataclasses.field()
    )

    AttributeNames = field("AttributeNames")
    S3Uri = field("S3Uri")
    AnnotationDataS3Uri = field("AnnotationDataS3Uri")
    SourceDocumentsS3Uri = field("SourceDocumentsS3Uri")
    DocumentType = field("DocumentType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DatasetAugmentedManifestsListItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetAugmentedManifestsListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetDocumentClassifierInputDataConfig:
    boto3_raw_data: "type_defs.DatasetDocumentClassifierInputDataConfigTypeDef" = (
        dataclasses.field()
    )

    S3Uri = field("S3Uri")
    LabelDelimiter = field("LabelDelimiter")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DatasetDocumentClassifierInputDataConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetDocumentClassifierInputDataConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetEntityRecognizerAnnotations:
    boto3_raw_data: "type_defs.DatasetEntityRecognizerAnnotationsTypeDef" = (
        dataclasses.field()
    )

    S3Uri = field("S3Uri")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DatasetEntityRecognizerAnnotationsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetEntityRecognizerAnnotationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetEntityRecognizerDocuments:
    boto3_raw_data: "type_defs.DatasetEntityRecognizerDocumentsTypeDef" = (
        dataclasses.field()
    )

    S3Uri = field("S3Uri")
    InputFormat = field("InputFormat")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DatasetEntityRecognizerDocumentsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetEntityRecognizerDocumentsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetEntityRecognizerEntityList:
    boto3_raw_data: "type_defs.DatasetEntityRecognizerEntityListTypeDef" = (
        dataclasses.field()
    )

    S3Uri = field("S3Uri")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DatasetEntityRecognizerEntityListTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetEntityRecognizerEntityListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetProperties:
    boto3_raw_data: "type_defs.DatasetPropertiesTypeDef" = dataclasses.field()

    DatasetArn = field("DatasetArn")
    DatasetName = field("DatasetName")
    DatasetType = field("DatasetType")
    DatasetS3Uri = field("DatasetS3Uri")
    Description = field("Description")
    Status = field("Status")
    Message = field("Message")
    NumberOfDocuments = field("NumberOfDocuments")
    CreationTime = field("CreationTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetPropertiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDocumentClassifierRequest:
    boto3_raw_data: "type_defs.DeleteDocumentClassifierRequestTypeDef" = (
        dataclasses.field()
    )

    DocumentClassifierArn = field("DocumentClassifierArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDocumentClassifierRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDocumentClassifierRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEndpointRequest:
    boto3_raw_data: "type_defs.DeleteEndpointRequestTypeDef" = dataclasses.field()

    EndpointArn = field("EndpointArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEntityRecognizerRequest:
    boto3_raw_data: "type_defs.DeleteEntityRecognizerRequestTypeDef" = (
        dataclasses.field()
    )

    EntityRecognizerArn = field("EntityRecognizerArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteEntityRecognizerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEntityRecognizerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFlywheelRequest:
    boto3_raw_data: "type_defs.DeleteFlywheelRequestTypeDef" = dataclasses.field()

    FlywheelArn = field("FlywheelArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFlywheelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFlywheelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourcePolicyRequest:
    boto3_raw_data: "type_defs.DeleteResourcePolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    PolicyRevisionId = field("PolicyRevisionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourcePolicyRequestTypeDef"]
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
class DescribeDocumentClassificationJobRequest:
    boto3_raw_data: "type_defs.DescribeDocumentClassificationJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDocumentClassificationJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDocumentClassificationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDocumentClassifierRequest:
    boto3_raw_data: "type_defs.DescribeDocumentClassifierRequestTypeDef" = (
        dataclasses.field()
    )

    DocumentClassifierArn = field("DocumentClassifierArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDocumentClassifierRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDocumentClassifierRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDominantLanguageDetectionJobRequest:
    boto3_raw_data: "type_defs.DescribeDominantLanguageDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDominantLanguageDetectionJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDominantLanguageDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointRequest:
    boto3_raw_data: "type_defs.DescribeEndpointRequestTypeDef" = dataclasses.field()

    EndpointArn = field("EndpointArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointProperties:
    boto3_raw_data: "type_defs.EndpointPropertiesTypeDef" = dataclasses.field()

    EndpointArn = field("EndpointArn")
    Status = field("Status")
    Message = field("Message")
    ModelArn = field("ModelArn")
    DesiredModelArn = field("DesiredModelArn")
    DesiredInferenceUnits = field("DesiredInferenceUnits")
    CurrentInferenceUnits = field("CurrentInferenceUnits")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")
    DataAccessRoleArn = field("DataAccessRoleArn")
    DesiredDataAccessRoleArn = field("DesiredDataAccessRoleArn")
    FlywheelArn = field("FlywheelArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EndpointPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEntitiesDetectionJobRequest:
    boto3_raw_data: "type_defs.DescribeEntitiesDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEntitiesDetectionJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEntitiesDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEntityRecognizerRequest:
    boto3_raw_data: "type_defs.DescribeEntityRecognizerRequestTypeDef" = (
        dataclasses.field()
    )

    EntityRecognizerArn = field("EntityRecognizerArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEntityRecognizerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEntityRecognizerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventsDetectionJobRequest:
    boto3_raw_data: "type_defs.DescribeEventsDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEventsDetectionJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventsDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFlywheelIterationRequest:
    boto3_raw_data: "type_defs.DescribeFlywheelIterationRequestTypeDef" = (
        dataclasses.field()
    )

    FlywheelArn = field("FlywheelArn")
    FlywheelIterationId = field("FlywheelIterationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFlywheelIterationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFlywheelIterationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFlywheelRequest:
    boto3_raw_data: "type_defs.DescribeFlywheelRequestTypeDef" = dataclasses.field()

    FlywheelArn = field("FlywheelArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFlywheelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFlywheelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeKeyPhrasesDetectionJobRequest:
    boto3_raw_data: "type_defs.DescribeKeyPhrasesDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeKeyPhrasesDetectionJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeKeyPhrasesDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePiiEntitiesDetectionJobRequest:
    boto3_raw_data: "type_defs.DescribePiiEntitiesDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePiiEntitiesDetectionJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePiiEntitiesDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourcePolicyRequest:
    boto3_raw_data: "type_defs.DescribeResourcePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeResourcePolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSentimentDetectionJobRequest:
    boto3_raw_data: "type_defs.DescribeSentimentDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSentimentDetectionJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSentimentDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTargetedSentimentDetectionJobRequest:
    boto3_raw_data: "type_defs.DescribeTargetedSentimentDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTargetedSentimentDetectionJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTargetedSentimentDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTopicsDetectionJobRequest:
    boto3_raw_data: "type_defs.DescribeTopicsDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTopicsDetectionJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTopicsDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectDominantLanguageRequest:
    boto3_raw_data: "type_defs.DetectDominantLanguageRequestTypeDef" = (
        dataclasses.field()
    )

    Text = field("Text")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DetectDominantLanguageRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectDominantLanguageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectKeyPhrasesRequest:
    boto3_raw_data: "type_defs.DetectKeyPhrasesRequestTypeDef" = dataclasses.field()

    Text = field("Text")
    LanguageCode = field("LanguageCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectKeyPhrasesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectKeyPhrasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectPiiEntitiesRequest:
    boto3_raw_data: "type_defs.DetectPiiEntitiesRequestTypeDef" = dataclasses.field()

    Text = field("Text")
    LanguageCode = field("LanguageCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectPiiEntitiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectPiiEntitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PiiEntity:
    boto3_raw_data: "type_defs.PiiEntityTypeDef" = dataclasses.field()

    Score = field("Score")
    Type = field("Type")
    BeginOffset = field("BeginOffset")
    EndOffset = field("EndOffset")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PiiEntityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PiiEntityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectSentimentRequest:
    boto3_raw_data: "type_defs.DetectSentimentRequestTypeDef" = dataclasses.field()

    Text = field("Text")
    LanguageCode = field("LanguageCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectSentimentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectSentimentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectSyntaxRequest:
    boto3_raw_data: "type_defs.DetectSyntaxRequestTypeDef" = dataclasses.field()

    Text = field("Text")
    LanguageCode = field("LanguageCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectSyntaxRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectSyntaxRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectTargetedSentimentRequest:
    boto3_raw_data: "type_defs.DetectTargetedSentimentRequestTypeDef" = (
        dataclasses.field()
    )

    Text = field("Text")
    LanguageCode = field("LanguageCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DetectTargetedSentimentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectTargetedSentimentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextSegment:
    boto3_raw_data: "type_defs.TextSegmentTypeDef" = dataclasses.field()

    Text = field("Text")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TextSegmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TextSegmentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentClassificationConfigOutput:
    boto3_raw_data: "type_defs.DocumentClassificationConfigOutputTypeDef" = (
        dataclasses.field()
    )

    Mode = field("Mode")
    Labels = field("Labels")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DocumentClassificationConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentClassificationConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentClassificationConfig:
    boto3_raw_data: "type_defs.DocumentClassificationConfigTypeDef" = (
        dataclasses.field()
    )

    Mode = field("Mode")
    Labels = field("Labels")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentClassificationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentClassificationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputDataConfig:
    boto3_raw_data: "type_defs.OutputDataConfigTypeDef" = dataclasses.field()

    S3Uri = field("S3Uri")
    KmsKeyId = field("KmsKeyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputDataConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputDataConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentClassifierDocuments:
    boto3_raw_data: "type_defs.DocumentClassifierDocumentsTypeDef" = dataclasses.field()

    S3Uri = field("S3Uri")
    TestS3Uri = field("TestS3Uri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentClassifierDocumentsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentClassifierDocumentsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentReaderConfigOutput:
    boto3_raw_data: "type_defs.DocumentReaderConfigOutputTypeDef" = dataclasses.field()

    DocumentReadAction = field("DocumentReadAction")
    DocumentReadMode = field("DocumentReadMode")
    FeatureTypes = field("FeatureTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentReaderConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentReaderConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentReaderConfig:
    boto3_raw_data: "type_defs.DocumentReaderConfigTypeDef" = dataclasses.field()

    DocumentReadAction = field("DocumentReadAction")
    DocumentReadMode = field("DocumentReadMode")
    FeatureTypes = field("FeatureTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentReaderConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentReaderConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentClassifierSummary:
    boto3_raw_data: "type_defs.DocumentClassifierSummaryTypeDef" = dataclasses.field()

    DocumentClassifierName = field("DocumentClassifierName")
    NumberOfVersions = field("NumberOfVersions")
    LatestVersionCreatedAt = field("LatestVersionCreatedAt")
    LatestVersionName = field("LatestVersionName")
    LatestVersionStatus = field("LatestVersionStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentClassifierSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentClassifierSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtractedCharactersListItem:
    boto3_raw_data: "type_defs.ExtractedCharactersListItemTypeDef" = dataclasses.field()

    Page = field("Page")
    Count = field("Count")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExtractedCharactersListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExtractedCharactersListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityTypesListItem:
    boto3_raw_data: "type_defs.EntityTypesListItemTypeDef" = dataclasses.field()

    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EntityTypesListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityTypesListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityRecognizerAnnotations:
    boto3_raw_data: "type_defs.EntityRecognizerAnnotationsTypeDef" = dataclasses.field()

    S3Uri = field("S3Uri")
    TestS3Uri = field("TestS3Uri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EntityRecognizerAnnotationsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityRecognizerAnnotationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityRecognizerDocuments:
    boto3_raw_data: "type_defs.EntityRecognizerDocumentsTypeDef" = dataclasses.field()

    S3Uri = field("S3Uri")
    TestS3Uri = field("TestS3Uri")
    InputFormat = field("InputFormat")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EntityRecognizerDocumentsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityRecognizerDocumentsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityRecognizerEntityList:
    boto3_raw_data: "type_defs.EntityRecognizerEntityListTypeDef" = dataclasses.field()

    S3Uri = field("S3Uri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EntityRecognizerEntityListTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityRecognizerEntityListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityRecognizerEvaluationMetrics:
    boto3_raw_data: "type_defs.EntityRecognizerEvaluationMetricsTypeDef" = (
        dataclasses.field()
    )

    Precision = field("Precision")
    Recall = field("Recall")
    F1Score = field("F1Score")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EntityRecognizerEvaluationMetricsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityRecognizerEvaluationMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityTypesEvaluationMetrics:
    boto3_raw_data: "type_defs.EntityTypesEvaluationMetricsTypeDef" = (
        dataclasses.field()
    )

    Precision = field("Precision")
    Recall = field("Recall")
    F1Score = field("F1Score")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EntityTypesEvaluationMetricsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityTypesEvaluationMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityRecognizerOutputDataConfig:
    boto3_raw_data: "type_defs.EntityRecognizerOutputDataConfigTypeDef" = (
        dataclasses.field()
    )

    FlywheelStatsS3Prefix = field("FlywheelStatsS3Prefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EntityRecognizerOutputDataConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityRecognizerOutputDataConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityRecognizerSummary:
    boto3_raw_data: "type_defs.EntityRecognizerSummaryTypeDef" = dataclasses.field()

    RecognizerName = field("RecognizerName")
    NumberOfVersions = field("NumberOfVersions")
    LatestVersionCreatedAt = field("LatestVersionCreatedAt")
    LatestVersionName = field("LatestVersionName")
    LatestVersionStatus = field("LatestVersionStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EntityRecognizerSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityRecognizerSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlywheelModelEvaluationMetrics:
    boto3_raw_data: "type_defs.FlywheelModelEvaluationMetricsTypeDef" = (
        dataclasses.field()
    )

    AverageF1Score = field("AverageF1Score")
    AveragePrecision = field("AveragePrecision")
    AverageRecall = field("AverageRecall")
    AverageAccuracy = field("AverageAccuracy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FlywheelModelEvaluationMetricsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlywheelModelEvaluationMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlywheelSummary:
    boto3_raw_data: "type_defs.FlywheelSummaryTypeDef" = dataclasses.field()

    FlywheelArn = field("FlywheelArn")
    ActiveModelArn = field("ActiveModelArn")
    DataLakeS3Uri = field("DataLakeS3Uri")
    Status = field("Status")
    ModelType = field("ModelType")
    Message = field("Message")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")
    LatestFlywheelIteration = field("LatestFlywheelIteration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlywheelSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlywheelSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Point:
    boto3_raw_data: "type_defs.PointTypeDef" = dataclasses.field()

    X = field("X")
    Y = field("Y")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PointTypeDef"]]
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
class ListDocumentClassifierSummariesRequest:
    boto3_raw_data: "type_defs.ListDocumentClassifierSummariesRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDocumentClassifierSummariesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDocumentClassifierSummariesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntityRecognizerSummariesRequest:
    boto3_raw_data: "type_defs.ListEntityRecognizerSummariesRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEntityRecognizerSummariesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntityRecognizerSummariesRequestTypeDef"]
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
class PartOfSpeechTag:
    boto3_raw_data: "type_defs.PartOfSpeechTagTypeDef" = dataclasses.field()

    Tag = field("Tag")
    Score = field("Score")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PartOfSpeechTagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PartOfSpeechTagTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PiiOutputDataConfig:
    boto3_raw_data: "type_defs.PiiOutputDataConfigTypeDef" = dataclasses.field()

    S3Uri = field("S3Uri")
    KmsKeyId = field("KmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PiiOutputDataConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PiiOutputDataConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedactionConfigOutput:
    boto3_raw_data: "type_defs.RedactionConfigOutputTypeDef" = dataclasses.field()

    PiiEntityTypes = field("PiiEntityTypes")
    MaskMode = field("MaskMode")
    MaskCharacter = field("MaskCharacter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedactionConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedactionConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyRequest:
    boto3_raw_data: "type_defs.PutResourcePolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    ResourcePolicy = field("ResourcePolicy")
    PolicyRevisionId = field("PolicyRevisionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedactionConfig:
    boto3_raw_data: "type_defs.RedactionConfigTypeDef" = dataclasses.field()

    PiiEntityTypes = field("PiiEntityTypes")
    MaskMode = field("MaskMode")
    MaskCharacter = field("MaskCharacter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RedactionConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RedactionConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFlywheelIterationRequest:
    boto3_raw_data: "type_defs.StartFlywheelIterationRequestTypeDef" = (
        dataclasses.field()
    )

    FlywheelArn = field("FlywheelArn")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartFlywheelIterationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFlywheelIterationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopDominantLanguageDetectionJobRequest:
    boto3_raw_data: "type_defs.StopDominantLanguageDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopDominantLanguageDetectionJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopDominantLanguageDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopEntitiesDetectionJobRequest:
    boto3_raw_data: "type_defs.StopEntitiesDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopEntitiesDetectionJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopEntitiesDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopEventsDetectionJobRequest:
    boto3_raw_data: "type_defs.StopEventsDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopEventsDetectionJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopEventsDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopKeyPhrasesDetectionJobRequest:
    boto3_raw_data: "type_defs.StopKeyPhrasesDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopKeyPhrasesDetectionJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopKeyPhrasesDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopPiiEntitiesDetectionJobRequest:
    boto3_raw_data: "type_defs.StopPiiEntitiesDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopPiiEntitiesDetectionJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopPiiEntitiesDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopSentimentDetectionJobRequest:
    boto3_raw_data: "type_defs.StopSentimentDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopSentimentDetectionJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopSentimentDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopTargetedSentimentDetectionJobRequest:
    boto3_raw_data: "type_defs.StopTargetedSentimentDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopTargetedSentimentDetectionJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopTargetedSentimentDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopTrainingDocumentClassifierRequest:
    boto3_raw_data: "type_defs.StopTrainingDocumentClassifierRequestTypeDef" = (
        dataclasses.field()
    )

    DocumentClassifierArn = field("DocumentClassifierArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopTrainingDocumentClassifierRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopTrainingDocumentClassifierRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopTrainingEntityRecognizerRequest:
    boto3_raw_data: "type_defs.StopTrainingEntityRecognizerRequestTypeDef" = (
        dataclasses.field()
    )

    EntityRecognizerArn = field("EntityRecognizerArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopTrainingEntityRecognizerRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopTrainingEntityRecognizerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToxicContent:
    boto3_raw_data: "type_defs.ToxicContentTypeDef" = dataclasses.field()

    Name = field("Name")
    Score = field("Score")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ToxicContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ToxicContentTypeDef"]],
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
class UpdateEndpointRequest:
    boto3_raw_data: "type_defs.UpdateEndpointRequestTypeDef" = dataclasses.field()

    EndpointArn = field("EndpointArn")
    DesiredModelArn = field("DesiredModelArn")
    DesiredInferenceUnits = field("DesiredInferenceUnits")
    DesiredDataAccessRoleArn = field("DesiredDataAccessRoleArn")
    FlywheelArn = field("FlywheelArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetectDominantLanguageItemResult:
    boto3_raw_data: "type_defs.BatchDetectDominantLanguageItemResultTypeDef" = (
        dataclasses.field()
    )

    Index = field("Index")

    @cached_property
    def Languages(self):  # pragma: no cover
        return DominantLanguage.make_many(self.boto3_raw_data["Languages"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDetectDominantLanguageItemResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetectDominantLanguageItemResultTypeDef"]
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
class CreateDocumentClassifierResponse:
    boto3_raw_data: "type_defs.CreateDocumentClassifierResponseTypeDef" = (
        dataclasses.field()
    )

    DocumentClassifierArn = field("DocumentClassifierArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDocumentClassifierResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDocumentClassifierResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEndpointResponse:
    boto3_raw_data: "type_defs.CreateEndpointResponseTypeDef" = dataclasses.field()

    EndpointArn = field("EndpointArn")
    ModelArn = field("ModelArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEntityRecognizerResponse:
    boto3_raw_data: "type_defs.CreateEntityRecognizerResponseTypeDef" = (
        dataclasses.field()
    )

    EntityRecognizerArn = field("EntityRecognizerArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateEntityRecognizerResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEntityRecognizerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFlywheelResponse:
    boto3_raw_data: "type_defs.CreateFlywheelResponseTypeDef" = dataclasses.field()

    FlywheelArn = field("FlywheelArn")
    ActiveModelArn = field("ActiveModelArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFlywheelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFlywheelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourcePolicyResponse:
    boto3_raw_data: "type_defs.DescribeResourcePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    ResourcePolicy = field("ResourcePolicy")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")
    PolicyRevisionId = field("PolicyRevisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeResourcePolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourcePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectDominantLanguageResponse:
    boto3_raw_data: "type_defs.DetectDominantLanguageResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Languages(self):  # pragma: no cover
        return DominantLanguage.make_many(self.boto3_raw_data["Languages"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DetectDominantLanguageResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectDominantLanguageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportModelResponse:
    boto3_raw_data: "type_defs.ImportModelResponseTypeDef" = dataclasses.field()

    ModelArn = field("ModelArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyResponse:
    boto3_raw_data: "type_defs.PutResourcePolicyResponseTypeDef" = dataclasses.field()

    PolicyRevisionId = field("PolicyRevisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDocumentClassificationJobResponse:
    boto3_raw_data: "type_defs.StartDocumentClassificationJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobArn = field("JobArn")
    JobStatus = field("JobStatus")
    DocumentClassifierArn = field("DocumentClassifierArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartDocumentClassificationJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDocumentClassificationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDominantLanguageDetectionJobResponse:
    boto3_raw_data: "type_defs.StartDominantLanguageDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobArn = field("JobArn")
    JobStatus = field("JobStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartDominantLanguageDetectionJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDominantLanguageDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartEntitiesDetectionJobResponse:
    boto3_raw_data: "type_defs.StartEntitiesDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobArn = field("JobArn")
    JobStatus = field("JobStatus")
    EntityRecognizerArn = field("EntityRecognizerArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartEntitiesDetectionJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartEntitiesDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartEventsDetectionJobResponse:
    boto3_raw_data: "type_defs.StartEventsDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobArn = field("JobArn")
    JobStatus = field("JobStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartEventsDetectionJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartEventsDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFlywheelIterationResponse:
    boto3_raw_data: "type_defs.StartFlywheelIterationResponseTypeDef" = (
        dataclasses.field()
    )

    FlywheelArn = field("FlywheelArn")
    FlywheelIterationId = field("FlywheelIterationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartFlywheelIterationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFlywheelIterationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartKeyPhrasesDetectionJobResponse:
    boto3_raw_data: "type_defs.StartKeyPhrasesDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobArn = field("JobArn")
    JobStatus = field("JobStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartKeyPhrasesDetectionJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartKeyPhrasesDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartPiiEntitiesDetectionJobResponse:
    boto3_raw_data: "type_defs.StartPiiEntitiesDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobArn = field("JobArn")
    JobStatus = field("JobStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartPiiEntitiesDetectionJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartPiiEntitiesDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSentimentDetectionJobResponse:
    boto3_raw_data: "type_defs.StartSentimentDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobArn = field("JobArn")
    JobStatus = field("JobStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartSentimentDetectionJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSentimentDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTargetedSentimentDetectionJobResponse:
    boto3_raw_data: "type_defs.StartTargetedSentimentDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobArn = field("JobArn")
    JobStatus = field("JobStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartTargetedSentimentDetectionJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTargetedSentimentDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTopicsDetectionJobResponse:
    boto3_raw_data: "type_defs.StartTopicsDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobArn = field("JobArn")
    JobStatus = field("JobStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartTopicsDetectionJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTopicsDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopDominantLanguageDetectionJobResponse:
    boto3_raw_data: "type_defs.StopDominantLanguageDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobStatus = field("JobStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopDominantLanguageDetectionJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopDominantLanguageDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopEntitiesDetectionJobResponse:
    boto3_raw_data: "type_defs.StopEntitiesDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobStatus = field("JobStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopEntitiesDetectionJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopEntitiesDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopEventsDetectionJobResponse:
    boto3_raw_data: "type_defs.StopEventsDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobStatus = field("JobStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopEventsDetectionJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopEventsDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopKeyPhrasesDetectionJobResponse:
    boto3_raw_data: "type_defs.StopKeyPhrasesDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobStatus = field("JobStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopKeyPhrasesDetectionJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopKeyPhrasesDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopPiiEntitiesDetectionJobResponse:
    boto3_raw_data: "type_defs.StopPiiEntitiesDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobStatus = field("JobStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopPiiEntitiesDetectionJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopPiiEntitiesDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopSentimentDetectionJobResponse:
    boto3_raw_data: "type_defs.StopSentimentDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobStatus = field("JobStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopSentimentDetectionJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopSentimentDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopTargetedSentimentDetectionJobResponse:
    boto3_raw_data: "type_defs.StopTargetedSentimentDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobStatus = field("JobStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopTargetedSentimentDetectionJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopTargetedSentimentDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEndpointResponse:
    boto3_raw_data: "type_defs.UpdateEndpointResponseTypeDef" = dataclasses.field()

    DesiredModelArn = field("DesiredModelArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetectKeyPhrasesItemResult:
    boto3_raw_data: "type_defs.BatchDetectKeyPhrasesItemResultTypeDef" = (
        dataclasses.field()
    )

    Index = field("Index")

    @cached_property
    def KeyPhrases(self):  # pragma: no cover
        return KeyPhrase.make_many(self.boto3_raw_data["KeyPhrases"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchDetectKeyPhrasesItemResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetectKeyPhrasesItemResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectKeyPhrasesResponse:
    boto3_raw_data: "type_defs.DetectKeyPhrasesResponseTypeDef" = dataclasses.field()

    @cached_property
    def KeyPhrases(self):  # pragma: no cover
        return KeyPhrase.make_many(self.boto3_raw_data["KeyPhrases"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectKeyPhrasesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectKeyPhrasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetectSentimentItemResult:
    boto3_raw_data: "type_defs.BatchDetectSentimentItemResultTypeDef" = (
        dataclasses.field()
    )

    Index = field("Index")
    Sentiment = field("Sentiment")

    @cached_property
    def SentimentScore(self):  # pragma: no cover
        return SentimentScore.make_one(self.boto3_raw_data["SentimentScore"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchDetectSentimentItemResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetectSentimentItemResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectSentimentResponse:
    boto3_raw_data: "type_defs.DetectSentimentResponseTypeDef" = dataclasses.field()

    Sentiment = field("Sentiment")

    @cached_property
    def SentimentScore(self):  # pragma: no cover
        return SentimentScore.make_one(self.boto3_raw_data["SentimentScore"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectSentimentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectSentimentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MentionSentiment:
    boto3_raw_data: "type_defs.MentionSentimentTypeDef" = dataclasses.field()

    Sentiment = field("Sentiment")

    @cached_property
    def SentimentScore(self):  # pragma: no cover
        return SentimentScore.make_one(self.boto3_raw_data["SentimentScore"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MentionSentimentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MentionSentimentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlockReference:
    boto3_raw_data: "type_defs.BlockReferenceTypeDef" = dataclasses.field()

    BlockId = field("BlockId")
    BeginOffset = field("BeginOffset")
    EndOffset = field("EndOffset")

    @cached_property
    def ChildBlocks(self):  # pragma: no cover
        return ChildBlock.make_many(self.boto3_raw_data["ChildBlocks"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BlockReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BlockReferenceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClassifierMetadata:
    boto3_raw_data: "type_defs.ClassifierMetadataTypeDef" = dataclasses.field()

    NumberOfLabels = field("NumberOfLabels")
    NumberOfTrainedDocuments = field("NumberOfTrainedDocuments")
    NumberOfTestDocuments = field("NumberOfTestDocuments")

    @cached_property
    def EvaluationMetrics(self):  # pragma: no cover
        return ClassifierEvaluationMetrics.make_one(
            self.boto3_raw_data["EvaluationMetrics"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClassifierMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClassifierMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainsPiiEntitiesResponse:
    boto3_raw_data: "type_defs.ContainsPiiEntitiesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Labels(self):  # pragma: no cover
        return EntityLabel.make_many(self.boto3_raw_data["Labels"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainsPiiEntitiesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainsPiiEntitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEndpointRequest:
    boto3_raw_data: "type_defs.CreateEndpointRequestTypeDef" = dataclasses.field()

    EndpointName = field("EndpointName")
    DesiredInferenceUnits = field("DesiredInferenceUnits")
    ModelArn = field("ModelArn")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    DataAccessRoleArn = field("DataAccessRoleArn")
    FlywheelArn = field("FlywheelArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportModelRequest:
    boto3_raw_data: "type_defs.ImportModelRequestTypeDef" = dataclasses.field()

    SourceModelArn = field("SourceModelArn")
    ModelName = field("ModelName")
    VersionName = field("VersionName")
    ModelKmsKeyId = field("ModelKmsKeyId")
    DataAccessRoleArn = field("DataAccessRoleArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportModelRequestTypeDef"]
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

    ResourceArn = field("ResourceArn")

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
class DataSecurityConfigOutput:
    boto3_raw_data: "type_defs.DataSecurityConfigOutputTypeDef" = dataclasses.field()

    ModelKmsKeyId = field("ModelKmsKeyId")
    VolumeKmsKeyId = field("VolumeKmsKeyId")
    DataLakeKmsKeyId = field("DataLakeKmsKeyId")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["VpcConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSecurityConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSecurityConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSecurityConfig:
    boto3_raw_data: "type_defs.DataSecurityConfigTypeDef" = dataclasses.field()

    ModelKmsKeyId = field("ModelKmsKeyId")
    VolumeKmsKeyId = field("VolumeKmsKeyId")
    DataLakeKmsKeyId = field("DataLakeKmsKeyId")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfig.make_one(self.boto3_raw_data["VpcConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSecurityConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSecurityConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetEntityRecognizerInputDataConfig:
    boto3_raw_data: "type_defs.DatasetEntityRecognizerInputDataConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Documents(self):  # pragma: no cover
        return DatasetEntityRecognizerDocuments.make_one(
            self.boto3_raw_data["Documents"]
        )

    @cached_property
    def Annotations(self):  # pragma: no cover
        return DatasetEntityRecognizerAnnotations.make_one(
            self.boto3_raw_data["Annotations"]
        )

    @cached_property
    def EntityList(self):  # pragma: no cover
        return DatasetEntityRecognizerEntityList.make_one(
            self.boto3_raw_data["EntityList"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DatasetEntityRecognizerInputDataConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetEntityRecognizerInputDataConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetFilter:
    boto3_raw_data: "type_defs.DatasetFilterTypeDef" = dataclasses.field()

    Status = field("Status")
    DatasetType = field("DatasetType")
    CreationTimeAfter = field("CreationTimeAfter")
    CreationTimeBefore = field("CreationTimeBefore")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentClassificationJobFilter:
    boto3_raw_data: "type_defs.DocumentClassificationJobFilterTypeDef" = (
        dataclasses.field()
    )

    JobName = field("JobName")
    JobStatus = field("JobStatus")
    SubmitTimeBefore = field("SubmitTimeBefore")
    SubmitTimeAfter = field("SubmitTimeAfter")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DocumentClassificationJobFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentClassificationJobFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentClassifierFilter:
    boto3_raw_data: "type_defs.DocumentClassifierFilterTypeDef" = dataclasses.field()

    Status = field("Status")
    DocumentClassifierName = field("DocumentClassifierName")
    SubmitTimeBefore = field("SubmitTimeBefore")
    SubmitTimeAfter = field("SubmitTimeAfter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentClassifierFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentClassifierFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DominantLanguageDetectionJobFilter:
    boto3_raw_data: "type_defs.DominantLanguageDetectionJobFilterTypeDef" = (
        dataclasses.field()
    )

    JobName = field("JobName")
    JobStatus = field("JobStatus")
    SubmitTimeBefore = field("SubmitTimeBefore")
    SubmitTimeAfter = field("SubmitTimeAfter")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DominantLanguageDetectionJobFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DominantLanguageDetectionJobFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointFilter:
    boto3_raw_data: "type_defs.EndpointFilterTypeDef" = dataclasses.field()

    ModelArn = field("ModelArn")
    Status = field("Status")
    CreationTimeBefore = field("CreationTimeBefore")
    CreationTimeAfter = field("CreationTimeAfter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EndpointFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntitiesDetectionJobFilter:
    boto3_raw_data: "type_defs.EntitiesDetectionJobFilterTypeDef" = dataclasses.field()

    JobName = field("JobName")
    JobStatus = field("JobStatus")
    SubmitTimeBefore = field("SubmitTimeBefore")
    SubmitTimeAfter = field("SubmitTimeAfter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EntitiesDetectionJobFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntitiesDetectionJobFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityRecognizerFilter:
    boto3_raw_data: "type_defs.EntityRecognizerFilterTypeDef" = dataclasses.field()

    Status = field("Status")
    RecognizerName = field("RecognizerName")
    SubmitTimeBefore = field("SubmitTimeBefore")
    SubmitTimeAfter = field("SubmitTimeAfter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EntityRecognizerFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityRecognizerFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventsDetectionJobFilter:
    boto3_raw_data: "type_defs.EventsDetectionJobFilterTypeDef" = dataclasses.field()

    JobName = field("JobName")
    JobStatus = field("JobStatus")
    SubmitTimeBefore = field("SubmitTimeBefore")
    SubmitTimeAfter = field("SubmitTimeAfter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventsDetectionJobFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventsDetectionJobFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlywheelFilter:
    boto3_raw_data: "type_defs.FlywheelFilterTypeDef" = dataclasses.field()

    Status = field("Status")
    CreationTimeAfter = field("CreationTimeAfter")
    CreationTimeBefore = field("CreationTimeBefore")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlywheelFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlywheelFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlywheelIterationFilter:
    boto3_raw_data: "type_defs.FlywheelIterationFilterTypeDef" = dataclasses.field()

    CreationTimeAfter = field("CreationTimeAfter")
    CreationTimeBefore = field("CreationTimeBefore")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlywheelIterationFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlywheelIterationFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyPhrasesDetectionJobFilter:
    boto3_raw_data: "type_defs.KeyPhrasesDetectionJobFilterTypeDef" = (
        dataclasses.field()
    )

    JobName = field("JobName")
    JobStatus = field("JobStatus")
    SubmitTimeBefore = field("SubmitTimeBefore")
    SubmitTimeAfter = field("SubmitTimeAfter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KeyPhrasesDetectionJobFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeyPhrasesDetectionJobFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PiiEntitiesDetectionJobFilter:
    boto3_raw_data: "type_defs.PiiEntitiesDetectionJobFilterTypeDef" = (
        dataclasses.field()
    )

    JobName = field("JobName")
    JobStatus = field("JobStatus")
    SubmitTimeBefore = field("SubmitTimeBefore")
    SubmitTimeAfter = field("SubmitTimeAfter")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PiiEntitiesDetectionJobFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PiiEntitiesDetectionJobFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SentimentDetectionJobFilter:
    boto3_raw_data: "type_defs.SentimentDetectionJobFilterTypeDef" = dataclasses.field()

    JobName = field("JobName")
    JobStatus = field("JobStatus")
    SubmitTimeBefore = field("SubmitTimeBefore")
    SubmitTimeAfter = field("SubmitTimeAfter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SentimentDetectionJobFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SentimentDetectionJobFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetedSentimentDetectionJobFilter:
    boto3_raw_data: "type_defs.TargetedSentimentDetectionJobFilterTypeDef" = (
        dataclasses.field()
    )

    JobName = field("JobName")
    JobStatus = field("JobStatus")
    SubmitTimeBefore = field("SubmitTimeBefore")
    SubmitTimeAfter = field("SubmitTimeAfter")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TargetedSentimentDetectionJobFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetedSentimentDetectionJobFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TopicsDetectionJobFilter:
    boto3_raw_data: "type_defs.TopicsDetectionJobFilterTypeDef" = dataclasses.field()

    JobName = field("JobName")
    JobStatus = field("JobStatus")
    SubmitTimeBefore = field("SubmitTimeBefore")
    SubmitTimeAfter = field("SubmitTimeAfter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TopicsDetectionJobFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TopicsDetectionJobFilterTypeDef"]
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

    @cached_property
    def DatasetProperties(self):  # pragma: no cover
        return DatasetProperties.make_one(self.boto3_raw_data["DatasetProperties"])

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
class ListDatasetsResponse:
    boto3_raw_data: "type_defs.ListDatasetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def DatasetPropertiesList(self):  # pragma: no cover
        return DatasetProperties.make_many(self.boto3_raw_data["DatasetPropertiesList"])

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
class DescribeEndpointResponse:
    boto3_raw_data: "type_defs.DescribeEndpointResponseTypeDef" = dataclasses.field()

    @cached_property
    def EndpointProperties(self):  # pragma: no cover
        return EndpointProperties.make_one(self.boto3_raw_data["EndpointProperties"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEndpointsResponse:
    boto3_raw_data: "type_defs.ListEndpointsResponseTypeDef" = dataclasses.field()

    @cached_property
    def EndpointPropertiesList(self):  # pragma: no cover
        return EndpointProperties.make_many(
            self.boto3_raw_data["EndpointPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEndpointsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectPiiEntitiesResponse:
    boto3_raw_data: "type_defs.DetectPiiEntitiesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Entities(self):  # pragma: no cover
        return PiiEntity.make_many(self.boto3_raw_data["Entities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectPiiEntitiesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectPiiEntitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectToxicContentRequest:
    boto3_raw_data: "type_defs.DetectToxicContentRequestTypeDef" = dataclasses.field()

    @cached_property
    def TextSegments(self):  # pragma: no cover
        return TextSegment.make_many(self.boto3_raw_data["TextSegments"])

    LanguageCode = field("LanguageCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectToxicContentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectToxicContentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentClassifierInputDataConfigOutput:
    boto3_raw_data: "type_defs.DocumentClassifierInputDataConfigOutputTypeDef" = (
        dataclasses.field()
    )

    DataFormat = field("DataFormat")
    S3Uri = field("S3Uri")
    TestS3Uri = field("TestS3Uri")
    LabelDelimiter = field("LabelDelimiter")

    @cached_property
    def AugmentedManifests(self):  # pragma: no cover
        return AugmentedManifestsListItemOutput.make_many(
            self.boto3_raw_data["AugmentedManifests"]
        )

    DocumentType = field("DocumentType")

    @cached_property
    def Documents(self):  # pragma: no cover
        return DocumentClassifierDocuments.make_one(self.boto3_raw_data["Documents"])

    @cached_property
    def DocumentReaderConfig(self):  # pragma: no cover
        return DocumentReaderConfigOutput.make_one(
            self.boto3_raw_data["DocumentReaderConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DocumentClassifierInputDataConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentClassifierInputDataConfigOutputTypeDef"]
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

    S3Uri = field("S3Uri")
    InputFormat = field("InputFormat")

    @cached_property
    def DocumentReaderConfig(self):  # pragma: no cover
        return DocumentReaderConfigOutput.make_one(
            self.boto3_raw_data["DocumentReaderConfig"]
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
class DocumentClassifierInputDataConfig:
    boto3_raw_data: "type_defs.DocumentClassifierInputDataConfigTypeDef" = (
        dataclasses.field()
    )

    DataFormat = field("DataFormat")
    S3Uri = field("S3Uri")
    TestS3Uri = field("TestS3Uri")
    LabelDelimiter = field("LabelDelimiter")

    @cached_property
    def AugmentedManifests(self):  # pragma: no cover
        return AugmentedManifestsListItem.make_many(
            self.boto3_raw_data["AugmentedManifests"]
        )

    DocumentType = field("DocumentType")

    @cached_property
    def Documents(self):  # pragma: no cover
        return DocumentClassifierDocuments.make_one(self.boto3_raw_data["Documents"])

    @cached_property
    def DocumentReaderConfig(self):  # pragma: no cover
        return DocumentReaderConfig.make_one(
            self.boto3_raw_data["DocumentReaderConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DocumentClassifierInputDataConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentClassifierInputDataConfigTypeDef"]
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

    S3Uri = field("S3Uri")
    InputFormat = field("InputFormat")

    @cached_property
    def DocumentReaderConfig(self):  # pragma: no cover
        return DocumentReaderConfig.make_one(
            self.boto3_raw_data["DocumentReaderConfig"]
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
class ListDocumentClassifierSummariesResponse:
    boto3_raw_data: "type_defs.ListDocumentClassifierSummariesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DocumentClassifierSummariesList(self):  # pragma: no cover
        return DocumentClassifierSummary.make_many(
            self.boto3_raw_data["DocumentClassifierSummariesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDocumentClassifierSummariesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDocumentClassifierSummariesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentMetadata:
    boto3_raw_data: "type_defs.DocumentMetadataTypeDef" = dataclasses.field()

    Pages = field("Pages")

    @cached_property
    def ExtractedCharacters(self):  # pragma: no cover
        return ExtractedCharactersListItem.make_many(
            self.boto3_raw_data["ExtractedCharacters"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityRecognitionConfigOutput:
    boto3_raw_data: "type_defs.EntityRecognitionConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EntityTypes(self):  # pragma: no cover
        return EntityTypesListItem.make_many(self.boto3_raw_data["EntityTypes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EntityRecognitionConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityRecognitionConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityRecognitionConfig:
    boto3_raw_data: "type_defs.EntityRecognitionConfigTypeDef" = dataclasses.field()

    @cached_property
    def EntityTypes(self):  # pragma: no cover
        return EntityTypesListItem.make_many(self.boto3_raw_data["EntityTypes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EntityRecognitionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityRecognitionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityRecognizerInputDataConfigOutput:
    boto3_raw_data: "type_defs.EntityRecognizerInputDataConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EntityTypes(self):  # pragma: no cover
        return EntityTypesListItem.make_many(self.boto3_raw_data["EntityTypes"])

    DataFormat = field("DataFormat")

    @cached_property
    def Documents(self):  # pragma: no cover
        return EntityRecognizerDocuments.make_one(self.boto3_raw_data["Documents"])

    @cached_property
    def Annotations(self):  # pragma: no cover
        return EntityRecognizerAnnotations.make_one(self.boto3_raw_data["Annotations"])

    @cached_property
    def EntityList(self):  # pragma: no cover
        return EntityRecognizerEntityList.make_one(self.boto3_raw_data["EntityList"])

    @cached_property
    def AugmentedManifests(self):  # pragma: no cover
        return AugmentedManifestsListItemOutput.make_many(
            self.boto3_raw_data["AugmentedManifests"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EntityRecognizerInputDataConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityRecognizerInputDataConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityRecognizerInputDataConfig:
    boto3_raw_data: "type_defs.EntityRecognizerInputDataConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EntityTypes(self):  # pragma: no cover
        return EntityTypesListItem.make_many(self.boto3_raw_data["EntityTypes"])

    DataFormat = field("DataFormat")

    @cached_property
    def Documents(self):  # pragma: no cover
        return EntityRecognizerDocuments.make_one(self.boto3_raw_data["Documents"])

    @cached_property
    def Annotations(self):  # pragma: no cover
        return EntityRecognizerAnnotations.make_one(self.boto3_raw_data["Annotations"])

    @cached_property
    def EntityList(self):  # pragma: no cover
        return EntityRecognizerEntityList.make_one(self.boto3_raw_data["EntityList"])

    @cached_property
    def AugmentedManifests(self):  # pragma: no cover
        return AugmentedManifestsListItem.make_many(
            self.boto3_raw_data["AugmentedManifests"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EntityRecognizerInputDataConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityRecognizerInputDataConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityRecognizerMetadataEntityTypesListItem:
    boto3_raw_data: "type_defs.EntityRecognizerMetadataEntityTypesListItemTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")

    @cached_property
    def EvaluationMetrics(self):  # pragma: no cover
        return EntityTypesEvaluationMetrics.make_one(
            self.boto3_raw_data["EvaluationMetrics"]
        )

    NumberOfTrainMentions = field("NumberOfTrainMentions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EntityRecognizerMetadataEntityTypesListItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityRecognizerMetadataEntityTypesListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntityRecognizerSummariesResponse:
    boto3_raw_data: "type_defs.ListEntityRecognizerSummariesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EntityRecognizerSummariesList(self):  # pragma: no cover
        return EntityRecognizerSummary.make_many(
            self.boto3_raw_data["EntityRecognizerSummariesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEntityRecognizerSummariesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntityRecognizerSummariesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlywheelIterationProperties:
    boto3_raw_data: "type_defs.FlywheelIterationPropertiesTypeDef" = dataclasses.field()

    FlywheelArn = field("FlywheelArn")
    FlywheelIterationId = field("FlywheelIterationId")
    CreationTime = field("CreationTime")
    EndTime = field("EndTime")
    Status = field("Status")
    Message = field("Message")
    EvaluatedModelArn = field("EvaluatedModelArn")

    @cached_property
    def EvaluatedModelMetrics(self):  # pragma: no cover
        return FlywheelModelEvaluationMetrics.make_one(
            self.boto3_raw_data["EvaluatedModelMetrics"]
        )

    TrainedModelArn = field("TrainedModelArn")

    @cached_property
    def TrainedModelMetrics(self):  # pragma: no cover
        return FlywheelModelEvaluationMetrics.make_one(
            self.boto3_raw_data["TrainedModelMetrics"]
        )

    EvaluationManifestS3Prefix = field("EvaluationManifestS3Prefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlywheelIterationPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlywheelIterationPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlywheelsResponse:
    boto3_raw_data: "type_defs.ListFlywheelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def FlywheelSummaryList(self):  # pragma: no cover
        return FlywheelSummary.make_many(self.boto3_raw_data["FlywheelSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFlywheelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlywheelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Geometry:
    boto3_raw_data: "type_defs.GeometryTypeDef" = dataclasses.field()

    @cached_property
    def BoundingBox(self):  # pragma: no cover
        return BoundingBox.make_one(self.boto3_raw_data["BoundingBox"])

    @cached_property
    def Polygon(self):  # pragma: no cover
        return Point.make_many(self.boto3_raw_data["Polygon"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GeometryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GeometryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SyntaxToken:
    boto3_raw_data: "type_defs.SyntaxTokenTypeDef" = dataclasses.field()

    TokenId = field("TokenId")
    Text = field("Text")
    BeginOffset = field("BeginOffset")
    EndOffset = field("EndOffset")

    @cached_property
    def PartOfSpeech(self):  # pragma: no cover
        return PartOfSpeechTag.make_one(self.boto3_raw_data["PartOfSpeech"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SyntaxTokenTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SyntaxTokenTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToxicLabels:
    boto3_raw_data: "type_defs.ToxicLabelsTypeDef" = dataclasses.field()

    @cached_property
    def Labels(self):  # pragma: no cover
        return ToxicContent.make_many(self.boto3_raw_data["Labels"])

    Toxicity = field("Toxicity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ToxicLabelsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ToxicLabelsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetectDominantLanguageResponse:
    boto3_raw_data: "type_defs.BatchDetectDominantLanguageResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResultList(self):  # pragma: no cover
        return BatchDetectDominantLanguageItemResult.make_many(
            self.boto3_raw_data["ResultList"]
        )

    @cached_property
    def ErrorList(self):  # pragma: no cover
        return BatchItemError.make_many(self.boto3_raw_data["ErrorList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDetectDominantLanguageResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetectDominantLanguageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetectKeyPhrasesResponse:
    boto3_raw_data: "type_defs.BatchDetectKeyPhrasesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResultList(self):  # pragma: no cover
        return BatchDetectKeyPhrasesItemResult.make_many(
            self.boto3_raw_data["ResultList"]
        )

    @cached_property
    def ErrorList(self):  # pragma: no cover
        return BatchItemError.make_many(self.boto3_raw_data["ErrorList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchDetectKeyPhrasesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetectKeyPhrasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetectSentimentResponse:
    boto3_raw_data: "type_defs.BatchDetectSentimentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResultList(self):  # pragma: no cover
        return BatchDetectSentimentItemResult.make_many(
            self.boto3_raw_data["ResultList"]
        )

    @cached_property
    def ErrorList(self):  # pragma: no cover
        return BatchItemError.make_many(self.boto3_raw_data["ErrorList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDetectSentimentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetectSentimentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetedSentimentMention:
    boto3_raw_data: "type_defs.TargetedSentimentMentionTypeDef" = dataclasses.field()

    Score = field("Score")
    GroupScore = field("GroupScore")
    Text = field("Text")
    Type = field("Type")

    @cached_property
    def MentionSentiment(self):  # pragma: no cover
        return MentionSentiment.make_one(self.boto3_raw_data["MentionSentiment"])

    BeginOffset = field("BeginOffset")
    EndOffset = field("EndOffset")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetedSentimentMentionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetedSentimentMentionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Entity:
    boto3_raw_data: "type_defs.EntityTypeDef" = dataclasses.field()

    Score = field("Score")
    Type = field("Type")
    Text = field("Text")
    BeginOffset = field("BeginOffset")
    EndOffset = field("EndOffset")

    @cached_property
    def BlockReferences(self):  # pragma: no cover
        return BlockReference.make_many(self.boto3_raw_data["BlockReferences"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataSecurityConfig:
    boto3_raw_data: "type_defs.UpdateDataSecurityConfigTypeDef" = dataclasses.field()

    ModelKmsKeyId = field("ModelKmsKeyId")
    VolumeKmsKeyId = field("VolumeKmsKeyId")
    VpcConfig = field("VpcConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDataSecurityConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataSecurityConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetInputDataConfig:
    boto3_raw_data: "type_defs.DatasetInputDataConfigTypeDef" = dataclasses.field()

    @cached_property
    def AugmentedManifests(self):  # pragma: no cover
        return DatasetAugmentedManifestsListItem.make_many(
            self.boto3_raw_data["AugmentedManifests"]
        )

    DataFormat = field("DataFormat")

    @cached_property
    def DocumentClassifierInputDataConfig(self):  # pragma: no cover
        return DatasetDocumentClassifierInputDataConfig.make_one(
            self.boto3_raw_data["DocumentClassifierInputDataConfig"]
        )

    @cached_property
    def EntityRecognizerInputDataConfig(self):  # pragma: no cover
        return DatasetEntityRecognizerInputDataConfig.make_one(
            self.boto3_raw_data["EntityRecognizerInputDataConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasetInputDataConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetInputDataConfigTypeDef"]
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

    FlywheelArn = field("FlywheelArn")

    @cached_property
    def Filter(self):  # pragma: no cover
        return DatasetFilter.make_one(self.boto3_raw_data["Filter"])

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
class ListDocumentClassificationJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListDocumentClassificationJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return DocumentClassificationJobFilter.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDocumentClassificationJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDocumentClassificationJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDocumentClassificationJobsRequest:
    boto3_raw_data: "type_defs.ListDocumentClassificationJobsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return DocumentClassificationJobFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDocumentClassificationJobsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDocumentClassificationJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDocumentClassifiersRequestPaginate:
    boto3_raw_data: "type_defs.ListDocumentClassifiersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return DocumentClassifierFilter.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDocumentClassifiersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDocumentClassifiersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDocumentClassifiersRequest:
    boto3_raw_data: "type_defs.ListDocumentClassifiersRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return DocumentClassifierFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDocumentClassifiersRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDocumentClassifiersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDominantLanguageDetectionJobsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListDominantLanguageDetectionJobsRequestPaginateTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Filter(self):  # pragma: no cover
        return DominantLanguageDetectionJobFilter.make_one(
            self.boto3_raw_data["Filter"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDominantLanguageDetectionJobsRequestPaginateTypeDef"
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
                "type_defs.ListDominantLanguageDetectionJobsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDominantLanguageDetectionJobsRequest:
    boto3_raw_data: "type_defs.ListDominantLanguageDetectionJobsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return DominantLanguageDetectionJobFilter.make_one(
            self.boto3_raw_data["Filter"]
        )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDominantLanguageDetectionJobsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDominantLanguageDetectionJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEndpointsRequestPaginate:
    boto3_raw_data: "type_defs.ListEndpointsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return EndpointFilter.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEndpointsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEndpointsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEndpointsRequest:
    boto3_raw_data: "type_defs.ListEndpointsRequestTypeDef" = dataclasses.field()

    @cached_property
    def Filter(self):  # pragma: no cover
        return EndpointFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEndpointsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEndpointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntitiesDetectionJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListEntitiesDetectionJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return EntitiesDetectionJobFilter.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEntitiesDetectionJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntitiesDetectionJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntitiesDetectionJobsRequest:
    boto3_raw_data: "type_defs.ListEntitiesDetectionJobsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return EntitiesDetectionJobFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEntitiesDetectionJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntitiesDetectionJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntityRecognizersRequestPaginate:
    boto3_raw_data: "type_defs.ListEntityRecognizersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return EntityRecognizerFilter.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEntityRecognizersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntityRecognizersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntityRecognizersRequest:
    boto3_raw_data: "type_defs.ListEntityRecognizersRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return EntityRecognizerFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEntityRecognizersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntityRecognizersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventsDetectionJobsRequest:
    boto3_raw_data: "type_defs.ListEventsDetectionJobsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return EventsDetectionJobFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEventsDetectionJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventsDetectionJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlywheelsRequest:
    boto3_raw_data: "type_defs.ListFlywheelsRequestTypeDef" = dataclasses.field()

    @cached_property
    def Filter(self):  # pragma: no cover
        return FlywheelFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFlywheelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlywheelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlywheelIterationHistoryRequest:
    boto3_raw_data: "type_defs.ListFlywheelIterationHistoryRequestTypeDef" = (
        dataclasses.field()
    )

    FlywheelArn = field("FlywheelArn")

    @cached_property
    def Filter(self):  # pragma: no cover
        return FlywheelIterationFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFlywheelIterationHistoryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlywheelIterationHistoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeyPhrasesDetectionJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListKeyPhrasesDetectionJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return KeyPhrasesDetectionJobFilter.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListKeyPhrasesDetectionJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeyPhrasesDetectionJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeyPhrasesDetectionJobsRequest:
    boto3_raw_data: "type_defs.ListKeyPhrasesDetectionJobsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return KeyPhrasesDetectionJobFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListKeyPhrasesDetectionJobsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeyPhrasesDetectionJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPiiEntitiesDetectionJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListPiiEntitiesDetectionJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return PiiEntitiesDetectionJobFilter.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPiiEntitiesDetectionJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPiiEntitiesDetectionJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPiiEntitiesDetectionJobsRequest:
    boto3_raw_data: "type_defs.ListPiiEntitiesDetectionJobsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return PiiEntitiesDetectionJobFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPiiEntitiesDetectionJobsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPiiEntitiesDetectionJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSentimentDetectionJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListSentimentDetectionJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return SentimentDetectionJobFilter.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSentimentDetectionJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSentimentDetectionJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSentimentDetectionJobsRequest:
    boto3_raw_data: "type_defs.ListSentimentDetectionJobsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return SentimentDetectionJobFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSentimentDetectionJobsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSentimentDetectionJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTargetedSentimentDetectionJobsRequest:
    boto3_raw_data: "type_defs.ListTargetedSentimentDetectionJobsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return TargetedSentimentDetectionJobFilter.make_one(
            self.boto3_raw_data["Filter"]
        )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTargetedSentimentDetectionJobsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTargetedSentimentDetectionJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTopicsDetectionJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListTopicsDetectionJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return TopicsDetectionJobFilter.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTopicsDetectionJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTopicsDetectionJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTopicsDetectionJobsRequest:
    boto3_raw_data: "type_defs.ListTopicsDetectionJobsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return TopicsDetectionJobFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTopicsDetectionJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTopicsDetectionJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentClassifierProperties:
    boto3_raw_data: "type_defs.DocumentClassifierPropertiesTypeDef" = (
        dataclasses.field()
    )

    DocumentClassifierArn = field("DocumentClassifierArn")
    LanguageCode = field("LanguageCode")
    Status = field("Status")
    Message = field("Message")
    SubmitTime = field("SubmitTime")
    EndTime = field("EndTime")
    TrainingStartTime = field("TrainingStartTime")
    TrainingEndTime = field("TrainingEndTime")

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return DocumentClassifierInputDataConfigOutput.make_one(
            self.boto3_raw_data["InputDataConfig"]
        )

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return DocumentClassifierOutputDataConfig.make_one(
            self.boto3_raw_data["OutputDataConfig"]
        )

    @cached_property
    def ClassifierMetadata(self):  # pragma: no cover
        return ClassifierMetadata.make_one(self.boto3_raw_data["ClassifierMetadata"])

    DataAccessRoleArn = field("DataAccessRoleArn")
    VolumeKmsKeyId = field("VolumeKmsKeyId")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["VpcConfig"])

    Mode = field("Mode")
    ModelKmsKeyId = field("ModelKmsKeyId")
    VersionName = field("VersionName")
    SourceModelArn = field("SourceModelArn")
    FlywheelArn = field("FlywheelArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentClassifierPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentClassifierPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentClassificationJobProperties:
    boto3_raw_data: "type_defs.DocumentClassificationJobPropertiesTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobArn = field("JobArn")
    JobName = field("JobName")
    JobStatus = field("JobStatus")
    Message = field("Message")
    SubmitTime = field("SubmitTime")
    EndTime = field("EndTime")
    DocumentClassifierArn = field("DocumentClassifierArn")

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfigOutput.make_one(self.boto3_raw_data["InputDataConfig"])

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    DataAccessRoleArn = field("DataAccessRoleArn")
    VolumeKmsKeyId = field("VolumeKmsKeyId")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["VpcConfig"])

    FlywheelArn = field("FlywheelArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DocumentClassificationJobPropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentClassificationJobPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DominantLanguageDetectionJobProperties:
    boto3_raw_data: "type_defs.DominantLanguageDetectionJobPropertiesTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobArn = field("JobArn")
    JobName = field("JobName")
    JobStatus = field("JobStatus")
    Message = field("Message")
    SubmitTime = field("SubmitTime")
    EndTime = field("EndTime")

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfigOutput.make_one(self.boto3_raw_data["InputDataConfig"])

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    DataAccessRoleArn = field("DataAccessRoleArn")
    VolumeKmsKeyId = field("VolumeKmsKeyId")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["VpcConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DominantLanguageDetectionJobPropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DominantLanguageDetectionJobPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntitiesDetectionJobProperties:
    boto3_raw_data: "type_defs.EntitiesDetectionJobPropertiesTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobArn = field("JobArn")
    JobName = field("JobName")
    JobStatus = field("JobStatus")
    Message = field("Message")
    SubmitTime = field("SubmitTime")
    EndTime = field("EndTime")
    EntityRecognizerArn = field("EntityRecognizerArn")

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfigOutput.make_one(self.boto3_raw_data["InputDataConfig"])

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    LanguageCode = field("LanguageCode")
    DataAccessRoleArn = field("DataAccessRoleArn")
    VolumeKmsKeyId = field("VolumeKmsKeyId")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["VpcConfig"])

    FlywheelArn = field("FlywheelArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EntitiesDetectionJobPropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntitiesDetectionJobPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventsDetectionJobProperties:
    boto3_raw_data: "type_defs.EventsDetectionJobPropertiesTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobArn = field("JobArn")
    JobName = field("JobName")
    JobStatus = field("JobStatus")
    Message = field("Message")
    SubmitTime = field("SubmitTime")
    EndTime = field("EndTime")

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfigOutput.make_one(self.boto3_raw_data["InputDataConfig"])

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    LanguageCode = field("LanguageCode")
    DataAccessRoleArn = field("DataAccessRoleArn")
    TargetEventTypes = field("TargetEventTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventsDetectionJobPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventsDetectionJobPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyPhrasesDetectionJobProperties:
    boto3_raw_data: "type_defs.KeyPhrasesDetectionJobPropertiesTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobArn = field("JobArn")
    JobName = field("JobName")
    JobStatus = field("JobStatus")
    Message = field("Message")
    SubmitTime = field("SubmitTime")
    EndTime = field("EndTime")

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfigOutput.make_one(self.boto3_raw_data["InputDataConfig"])

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    LanguageCode = field("LanguageCode")
    DataAccessRoleArn = field("DataAccessRoleArn")
    VolumeKmsKeyId = field("VolumeKmsKeyId")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["VpcConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KeyPhrasesDetectionJobPropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeyPhrasesDetectionJobPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PiiEntitiesDetectionJobProperties:
    boto3_raw_data: "type_defs.PiiEntitiesDetectionJobPropertiesTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobArn = field("JobArn")
    JobName = field("JobName")
    JobStatus = field("JobStatus")
    Message = field("Message")
    SubmitTime = field("SubmitTime")
    EndTime = field("EndTime")

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfigOutput.make_one(self.boto3_raw_data["InputDataConfig"])

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return PiiOutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    @cached_property
    def RedactionConfig(self):  # pragma: no cover
        return RedactionConfigOutput.make_one(self.boto3_raw_data["RedactionConfig"])

    LanguageCode = field("LanguageCode")
    DataAccessRoleArn = field("DataAccessRoleArn")
    Mode = field("Mode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PiiEntitiesDetectionJobPropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PiiEntitiesDetectionJobPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SentimentDetectionJobProperties:
    boto3_raw_data: "type_defs.SentimentDetectionJobPropertiesTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobArn = field("JobArn")
    JobName = field("JobName")
    JobStatus = field("JobStatus")
    Message = field("Message")
    SubmitTime = field("SubmitTime")
    EndTime = field("EndTime")

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfigOutput.make_one(self.boto3_raw_data["InputDataConfig"])

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    LanguageCode = field("LanguageCode")
    DataAccessRoleArn = field("DataAccessRoleArn")
    VolumeKmsKeyId = field("VolumeKmsKeyId")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["VpcConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SentimentDetectionJobPropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SentimentDetectionJobPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetedSentimentDetectionJobProperties:
    boto3_raw_data: "type_defs.TargetedSentimentDetectionJobPropertiesTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobArn = field("JobArn")
    JobName = field("JobName")
    JobStatus = field("JobStatus")
    Message = field("Message")
    SubmitTime = field("SubmitTime")
    EndTime = field("EndTime")

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfigOutput.make_one(self.boto3_raw_data["InputDataConfig"])

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    LanguageCode = field("LanguageCode")
    DataAccessRoleArn = field("DataAccessRoleArn")
    VolumeKmsKeyId = field("VolumeKmsKeyId")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["VpcConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TargetedSentimentDetectionJobPropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetedSentimentDetectionJobPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TopicsDetectionJobProperties:
    boto3_raw_data: "type_defs.TopicsDetectionJobPropertiesTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobArn = field("JobArn")
    JobName = field("JobName")
    JobStatus = field("JobStatus")
    Message = field("Message")
    SubmitTime = field("SubmitTime")
    EndTime = field("EndTime")

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfigOutput.make_one(self.boto3_raw_data["InputDataConfig"])

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    NumberOfTopics = field("NumberOfTopics")
    DataAccessRoleArn = field("DataAccessRoleArn")
    VolumeKmsKeyId = field("VolumeKmsKeyId")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["VpcConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TopicsDetectionJobPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TopicsDetectionJobPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClassifyDocumentRequest:
    boto3_raw_data: "type_defs.ClassifyDocumentRequestTypeDef" = dataclasses.field()

    EndpointArn = field("EndpointArn")
    Text = field("Text")
    Bytes = field("Bytes")
    DocumentReaderConfig = field("DocumentReaderConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClassifyDocumentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClassifyDocumentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectEntitiesRequest:
    boto3_raw_data: "type_defs.DetectEntitiesRequestTypeDef" = dataclasses.field()

    Text = field("Text")
    LanguageCode = field("LanguageCode")
    EndpointArn = field("EndpointArn")
    Bytes = field("Bytes")
    DocumentReaderConfig = field("DocumentReaderConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectEntitiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectEntitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClassifyDocumentResponse:
    boto3_raw_data: "type_defs.ClassifyDocumentResponseTypeDef" = dataclasses.field()

    @cached_property
    def Classes(self):  # pragma: no cover
        return DocumentClass.make_many(self.boto3_raw_data["Classes"])

    @cached_property
    def Labels(self):  # pragma: no cover
        return DocumentLabel.make_many(self.boto3_raw_data["Labels"])

    @cached_property
    def DocumentMetadata(self):  # pragma: no cover
        return DocumentMetadata.make_one(self.boto3_raw_data["DocumentMetadata"])

    @cached_property
    def DocumentType(self):  # pragma: no cover
        return DocumentTypeListItem.make_many(self.boto3_raw_data["DocumentType"])

    @cached_property
    def Errors(self):  # pragma: no cover
        return ErrorsListItem.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def Warnings(self):  # pragma: no cover
        return WarningsListItem.make_many(self.boto3_raw_data["Warnings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClassifyDocumentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClassifyDocumentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskConfigOutput:
    boto3_raw_data: "type_defs.TaskConfigOutputTypeDef" = dataclasses.field()

    LanguageCode = field("LanguageCode")

    @cached_property
    def DocumentClassificationConfig(self):  # pragma: no cover
        return DocumentClassificationConfigOutput.make_one(
            self.boto3_raw_data["DocumentClassificationConfig"]
        )

    @cached_property
    def EntityRecognitionConfig(self):  # pragma: no cover
        return EntityRecognitionConfigOutput.make_one(
            self.boto3_raw_data["EntityRecognitionConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaskConfigOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskConfig:
    boto3_raw_data: "type_defs.TaskConfigTypeDef" = dataclasses.field()

    LanguageCode = field("LanguageCode")

    @cached_property
    def DocumentClassificationConfig(self):  # pragma: no cover
        return DocumentClassificationConfig.make_one(
            self.boto3_raw_data["DocumentClassificationConfig"]
        )

    @cached_property
    def EntityRecognitionConfig(self):  # pragma: no cover
        return EntityRecognitionConfig.make_one(
            self.boto3_raw_data["EntityRecognitionConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaskConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaskConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityRecognizerMetadata:
    boto3_raw_data: "type_defs.EntityRecognizerMetadataTypeDef" = dataclasses.field()

    NumberOfTrainedDocuments = field("NumberOfTrainedDocuments")
    NumberOfTestDocuments = field("NumberOfTestDocuments")

    @cached_property
    def EvaluationMetrics(self):  # pragma: no cover
        return EntityRecognizerEvaluationMetrics.make_one(
            self.boto3_raw_data["EvaluationMetrics"]
        )

    @cached_property
    def EntityTypes(self):  # pragma: no cover
        return EntityRecognizerMetadataEntityTypesListItem.make_many(
            self.boto3_raw_data["EntityTypes"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EntityRecognizerMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityRecognizerMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFlywheelIterationResponse:
    boto3_raw_data: "type_defs.DescribeFlywheelIterationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FlywheelIterationProperties(self):  # pragma: no cover
        return FlywheelIterationProperties.make_one(
            self.boto3_raw_data["FlywheelIterationProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFlywheelIterationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFlywheelIterationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlywheelIterationHistoryResponse:
    boto3_raw_data: "type_defs.ListFlywheelIterationHistoryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FlywheelIterationPropertiesList(self):  # pragma: no cover
        return FlywheelIterationProperties.make_many(
            self.boto3_raw_data["FlywheelIterationPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFlywheelIterationHistoryResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlywheelIterationHistoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Block:
    boto3_raw_data: "type_defs.BlockTypeDef" = dataclasses.field()

    Id = field("Id")
    BlockType = field("BlockType")
    Text = field("Text")
    Page = field("Page")

    @cached_property
    def Geometry(self):  # pragma: no cover
        return Geometry.make_one(self.boto3_raw_data["Geometry"])

    @cached_property
    def Relationships(self):  # pragma: no cover
        return RelationshipsListItem.make_many(self.boto3_raw_data["Relationships"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BlockTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BlockTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetectSyntaxItemResult:
    boto3_raw_data: "type_defs.BatchDetectSyntaxItemResultTypeDef" = dataclasses.field()

    Index = field("Index")

    @cached_property
    def SyntaxTokens(self):  # pragma: no cover
        return SyntaxToken.make_many(self.boto3_raw_data["SyntaxTokens"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDetectSyntaxItemResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetectSyntaxItemResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectSyntaxResponse:
    boto3_raw_data: "type_defs.DetectSyntaxResponseTypeDef" = dataclasses.field()

    @cached_property
    def SyntaxTokens(self):  # pragma: no cover
        return SyntaxToken.make_many(self.boto3_raw_data["SyntaxTokens"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectSyntaxResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectSyntaxResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectToxicContentResponse:
    boto3_raw_data: "type_defs.DetectToxicContentResponseTypeDef" = dataclasses.field()

    @cached_property
    def ResultList(self):  # pragma: no cover
        return ToxicLabels.make_many(self.boto3_raw_data["ResultList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectToxicContentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectToxicContentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetedSentimentEntity:
    boto3_raw_data: "type_defs.TargetedSentimentEntityTypeDef" = dataclasses.field()

    DescriptiveMentionIndex = field("DescriptiveMentionIndex")

    @cached_property
    def Mentions(self):  # pragma: no cover
        return TargetedSentimentMention.make_many(self.boto3_raw_data["Mentions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetedSentimentEntityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetedSentimentEntityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetectEntitiesItemResult:
    boto3_raw_data: "type_defs.BatchDetectEntitiesItemResultTypeDef" = (
        dataclasses.field()
    )

    Index = field("Index")

    @cached_property
    def Entities(self):  # pragma: no cover
        return Entity.make_many(self.boto3_raw_data["Entities"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchDetectEntitiesItemResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetectEntitiesItemResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFlywheelRequest:
    boto3_raw_data: "type_defs.UpdateFlywheelRequestTypeDef" = dataclasses.field()

    FlywheelArn = field("FlywheelArn")
    ActiveModelArn = field("ActiveModelArn")
    DataAccessRoleArn = field("DataAccessRoleArn")

    @cached_property
    def DataSecurityConfig(self):  # pragma: no cover
        return UpdateDataSecurityConfig.make_one(
            self.boto3_raw_data["DataSecurityConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFlywheelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFlywheelRequestTypeDef"]
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

    FlywheelArn = field("FlywheelArn")
    DatasetName = field("DatasetName")

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return DatasetInputDataConfig.make_one(self.boto3_raw_data["InputDataConfig"])

    DatasetType = field("DatasetType")
    Description = field("Description")
    ClientRequestToken = field("ClientRequestToken")

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
class DescribeDocumentClassifierResponse:
    boto3_raw_data: "type_defs.DescribeDocumentClassifierResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DocumentClassifierProperties(self):  # pragma: no cover
        return DocumentClassifierProperties.make_one(
            self.boto3_raw_data["DocumentClassifierProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDocumentClassifierResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDocumentClassifierResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDocumentClassifiersResponse:
    boto3_raw_data: "type_defs.ListDocumentClassifiersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DocumentClassifierPropertiesList(self):  # pragma: no cover
        return DocumentClassifierProperties.make_many(
            self.boto3_raw_data["DocumentClassifierPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDocumentClassifiersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDocumentClassifiersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDocumentClassificationJobResponse:
    boto3_raw_data: "type_defs.DescribeDocumentClassificationJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DocumentClassificationJobProperties(self):  # pragma: no cover
        return DocumentClassificationJobProperties.make_one(
            self.boto3_raw_data["DocumentClassificationJobProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDocumentClassificationJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDocumentClassificationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDocumentClassificationJobsResponse:
    boto3_raw_data: "type_defs.ListDocumentClassificationJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DocumentClassificationJobPropertiesList(self):  # pragma: no cover
        return DocumentClassificationJobProperties.make_many(
            self.boto3_raw_data["DocumentClassificationJobPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDocumentClassificationJobsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDocumentClassificationJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDominantLanguageDetectionJobResponse:
    boto3_raw_data: "type_defs.DescribeDominantLanguageDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DominantLanguageDetectionJobProperties(self):  # pragma: no cover
        return DominantLanguageDetectionJobProperties.make_one(
            self.boto3_raw_data["DominantLanguageDetectionJobProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDominantLanguageDetectionJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDominantLanguageDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDominantLanguageDetectionJobsResponse:
    boto3_raw_data: "type_defs.ListDominantLanguageDetectionJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DominantLanguageDetectionJobPropertiesList(self):  # pragma: no cover
        return DominantLanguageDetectionJobProperties.make_many(
            self.boto3_raw_data["DominantLanguageDetectionJobPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDominantLanguageDetectionJobsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDominantLanguageDetectionJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEntitiesDetectionJobResponse:
    boto3_raw_data: "type_defs.DescribeEntitiesDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EntitiesDetectionJobProperties(self):  # pragma: no cover
        return EntitiesDetectionJobProperties.make_one(
            self.boto3_raw_data["EntitiesDetectionJobProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEntitiesDetectionJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEntitiesDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntitiesDetectionJobsResponse:
    boto3_raw_data: "type_defs.ListEntitiesDetectionJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EntitiesDetectionJobPropertiesList(self):  # pragma: no cover
        return EntitiesDetectionJobProperties.make_many(
            self.boto3_raw_data["EntitiesDetectionJobPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEntitiesDetectionJobsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntitiesDetectionJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventsDetectionJobResponse:
    boto3_raw_data: "type_defs.DescribeEventsDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventsDetectionJobProperties(self):  # pragma: no cover
        return EventsDetectionJobProperties.make_one(
            self.boto3_raw_data["EventsDetectionJobProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEventsDetectionJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventsDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventsDetectionJobsResponse:
    boto3_raw_data: "type_defs.ListEventsDetectionJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventsDetectionJobPropertiesList(self):  # pragma: no cover
        return EventsDetectionJobProperties.make_many(
            self.boto3_raw_data["EventsDetectionJobPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEventsDetectionJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventsDetectionJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeKeyPhrasesDetectionJobResponse:
    boto3_raw_data: "type_defs.DescribeKeyPhrasesDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def KeyPhrasesDetectionJobProperties(self):  # pragma: no cover
        return KeyPhrasesDetectionJobProperties.make_one(
            self.boto3_raw_data["KeyPhrasesDetectionJobProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeKeyPhrasesDetectionJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeKeyPhrasesDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeyPhrasesDetectionJobsResponse:
    boto3_raw_data: "type_defs.ListKeyPhrasesDetectionJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def KeyPhrasesDetectionJobPropertiesList(self):  # pragma: no cover
        return KeyPhrasesDetectionJobProperties.make_many(
            self.boto3_raw_data["KeyPhrasesDetectionJobPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListKeyPhrasesDetectionJobsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeyPhrasesDetectionJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePiiEntitiesDetectionJobResponse:
    boto3_raw_data: "type_defs.DescribePiiEntitiesDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PiiEntitiesDetectionJobProperties(self):  # pragma: no cover
        return PiiEntitiesDetectionJobProperties.make_one(
            self.boto3_raw_data["PiiEntitiesDetectionJobProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePiiEntitiesDetectionJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePiiEntitiesDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPiiEntitiesDetectionJobsResponse:
    boto3_raw_data: "type_defs.ListPiiEntitiesDetectionJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PiiEntitiesDetectionJobPropertiesList(self):  # pragma: no cover
        return PiiEntitiesDetectionJobProperties.make_many(
            self.boto3_raw_data["PiiEntitiesDetectionJobPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPiiEntitiesDetectionJobsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPiiEntitiesDetectionJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSentimentDetectionJobResponse:
    boto3_raw_data: "type_defs.DescribeSentimentDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SentimentDetectionJobProperties(self):  # pragma: no cover
        return SentimentDetectionJobProperties.make_one(
            self.boto3_raw_data["SentimentDetectionJobProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSentimentDetectionJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSentimentDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSentimentDetectionJobsResponse:
    boto3_raw_data: "type_defs.ListSentimentDetectionJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SentimentDetectionJobPropertiesList(self):  # pragma: no cover
        return SentimentDetectionJobProperties.make_many(
            self.boto3_raw_data["SentimentDetectionJobPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSentimentDetectionJobsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSentimentDetectionJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTargetedSentimentDetectionJobResponse:
    boto3_raw_data: "type_defs.DescribeTargetedSentimentDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TargetedSentimentDetectionJobProperties(self):  # pragma: no cover
        return TargetedSentimentDetectionJobProperties.make_one(
            self.boto3_raw_data["TargetedSentimentDetectionJobProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTargetedSentimentDetectionJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTargetedSentimentDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTargetedSentimentDetectionJobsResponse:
    boto3_raw_data: "type_defs.ListTargetedSentimentDetectionJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TargetedSentimentDetectionJobPropertiesList(self):  # pragma: no cover
        return TargetedSentimentDetectionJobProperties.make_many(
            self.boto3_raw_data["TargetedSentimentDetectionJobPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTargetedSentimentDetectionJobsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTargetedSentimentDetectionJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTopicsDetectionJobResponse:
    boto3_raw_data: "type_defs.DescribeTopicsDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TopicsDetectionJobProperties(self):  # pragma: no cover
        return TopicsDetectionJobProperties.make_one(
            self.boto3_raw_data["TopicsDetectionJobProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTopicsDetectionJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTopicsDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTopicsDetectionJobsResponse:
    boto3_raw_data: "type_defs.ListTopicsDetectionJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TopicsDetectionJobPropertiesList(self):  # pragma: no cover
        return TopicsDetectionJobProperties.make_many(
            self.boto3_raw_data["TopicsDetectionJobPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTopicsDetectionJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTopicsDetectionJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDocumentClassifierRequest:
    boto3_raw_data: "type_defs.CreateDocumentClassifierRequestTypeDef" = (
        dataclasses.field()
    )

    DocumentClassifierName = field("DocumentClassifierName")
    DataAccessRoleArn = field("DataAccessRoleArn")
    InputDataConfig = field("InputDataConfig")
    LanguageCode = field("LanguageCode")
    VersionName = field("VersionName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return DocumentClassifierOutputDataConfig.make_one(
            self.boto3_raw_data["OutputDataConfig"]
        )

    ClientRequestToken = field("ClientRequestToken")
    VolumeKmsKeyId = field("VolumeKmsKeyId")
    VpcConfig = field("VpcConfig")
    Mode = field("Mode")
    ModelKmsKeyId = field("ModelKmsKeyId")
    ModelPolicy = field("ModelPolicy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDocumentClassifierRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDocumentClassifierRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDocumentClassificationJobRequest:
    boto3_raw_data: "type_defs.StartDocumentClassificationJobRequestTypeDef" = (
        dataclasses.field()
    )

    InputDataConfig = field("InputDataConfig")

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    DataAccessRoleArn = field("DataAccessRoleArn")
    JobName = field("JobName")
    DocumentClassifierArn = field("DocumentClassifierArn")
    ClientRequestToken = field("ClientRequestToken")
    VolumeKmsKeyId = field("VolumeKmsKeyId")
    VpcConfig = field("VpcConfig")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    FlywheelArn = field("FlywheelArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartDocumentClassificationJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDocumentClassificationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDominantLanguageDetectionJobRequest:
    boto3_raw_data: "type_defs.StartDominantLanguageDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    InputDataConfig = field("InputDataConfig")

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    DataAccessRoleArn = field("DataAccessRoleArn")
    JobName = field("JobName")
    ClientRequestToken = field("ClientRequestToken")
    VolumeKmsKeyId = field("VolumeKmsKeyId")
    VpcConfig = field("VpcConfig")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartDominantLanguageDetectionJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDominantLanguageDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartEntitiesDetectionJobRequest:
    boto3_raw_data: "type_defs.StartEntitiesDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    InputDataConfig = field("InputDataConfig")

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    DataAccessRoleArn = field("DataAccessRoleArn")
    LanguageCode = field("LanguageCode")
    JobName = field("JobName")
    EntityRecognizerArn = field("EntityRecognizerArn")
    ClientRequestToken = field("ClientRequestToken")
    VolumeKmsKeyId = field("VolumeKmsKeyId")
    VpcConfig = field("VpcConfig")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    FlywheelArn = field("FlywheelArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartEntitiesDetectionJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartEntitiesDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartEventsDetectionJobRequest:
    boto3_raw_data: "type_defs.StartEventsDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    InputDataConfig = field("InputDataConfig")

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    DataAccessRoleArn = field("DataAccessRoleArn")
    LanguageCode = field("LanguageCode")
    TargetEventTypes = field("TargetEventTypes")
    JobName = field("JobName")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartEventsDetectionJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartEventsDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartKeyPhrasesDetectionJobRequest:
    boto3_raw_data: "type_defs.StartKeyPhrasesDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    InputDataConfig = field("InputDataConfig")

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    DataAccessRoleArn = field("DataAccessRoleArn")
    LanguageCode = field("LanguageCode")
    JobName = field("JobName")
    ClientRequestToken = field("ClientRequestToken")
    VolumeKmsKeyId = field("VolumeKmsKeyId")
    VpcConfig = field("VpcConfig")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartKeyPhrasesDetectionJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartKeyPhrasesDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartPiiEntitiesDetectionJobRequest:
    boto3_raw_data: "type_defs.StartPiiEntitiesDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    InputDataConfig = field("InputDataConfig")

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    Mode = field("Mode")
    DataAccessRoleArn = field("DataAccessRoleArn")
    LanguageCode = field("LanguageCode")
    RedactionConfig = field("RedactionConfig")
    JobName = field("JobName")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartPiiEntitiesDetectionJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartPiiEntitiesDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSentimentDetectionJobRequest:
    boto3_raw_data: "type_defs.StartSentimentDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    InputDataConfig = field("InputDataConfig")

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    DataAccessRoleArn = field("DataAccessRoleArn")
    LanguageCode = field("LanguageCode")
    JobName = field("JobName")
    ClientRequestToken = field("ClientRequestToken")
    VolumeKmsKeyId = field("VolumeKmsKeyId")
    VpcConfig = field("VpcConfig")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartSentimentDetectionJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSentimentDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTargetedSentimentDetectionJobRequest:
    boto3_raw_data: "type_defs.StartTargetedSentimentDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    InputDataConfig = field("InputDataConfig")

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    DataAccessRoleArn = field("DataAccessRoleArn")
    LanguageCode = field("LanguageCode")
    JobName = field("JobName")
    ClientRequestToken = field("ClientRequestToken")
    VolumeKmsKeyId = field("VolumeKmsKeyId")
    VpcConfig = field("VpcConfig")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartTargetedSentimentDetectionJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTargetedSentimentDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTopicsDetectionJobRequest:
    boto3_raw_data: "type_defs.StartTopicsDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    InputDataConfig = field("InputDataConfig")

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    DataAccessRoleArn = field("DataAccessRoleArn")
    JobName = field("JobName")
    NumberOfTopics = field("NumberOfTopics")
    ClientRequestToken = field("ClientRequestToken")
    VolumeKmsKeyId = field("VolumeKmsKeyId")
    VpcConfig = field("VpcConfig")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartTopicsDetectionJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTopicsDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlywheelProperties:
    boto3_raw_data: "type_defs.FlywheelPropertiesTypeDef" = dataclasses.field()

    FlywheelArn = field("FlywheelArn")
    ActiveModelArn = field("ActiveModelArn")
    DataAccessRoleArn = field("DataAccessRoleArn")

    @cached_property
    def TaskConfig(self):  # pragma: no cover
        return TaskConfigOutput.make_one(self.boto3_raw_data["TaskConfig"])

    DataLakeS3Uri = field("DataLakeS3Uri")

    @cached_property
    def DataSecurityConfig(self):  # pragma: no cover
        return DataSecurityConfigOutput.make_one(
            self.boto3_raw_data["DataSecurityConfig"]
        )

    Status = field("Status")
    ModelType = field("ModelType")
    Message = field("Message")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")
    LatestFlywheelIteration = field("LatestFlywheelIteration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlywheelPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlywheelPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEntityRecognizerRequest:
    boto3_raw_data: "type_defs.CreateEntityRecognizerRequestTypeDef" = (
        dataclasses.field()
    )

    RecognizerName = field("RecognizerName")
    DataAccessRoleArn = field("DataAccessRoleArn")
    InputDataConfig = field("InputDataConfig")
    LanguageCode = field("LanguageCode")
    VersionName = field("VersionName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientRequestToken = field("ClientRequestToken")
    VolumeKmsKeyId = field("VolumeKmsKeyId")
    VpcConfig = field("VpcConfig")
    ModelKmsKeyId = field("ModelKmsKeyId")
    ModelPolicy = field("ModelPolicy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateEntityRecognizerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEntityRecognizerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityRecognizerProperties:
    boto3_raw_data: "type_defs.EntityRecognizerPropertiesTypeDef" = dataclasses.field()

    EntityRecognizerArn = field("EntityRecognizerArn")
    LanguageCode = field("LanguageCode")
    Status = field("Status")
    Message = field("Message")
    SubmitTime = field("SubmitTime")
    EndTime = field("EndTime")
    TrainingStartTime = field("TrainingStartTime")
    TrainingEndTime = field("TrainingEndTime")

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return EntityRecognizerInputDataConfigOutput.make_one(
            self.boto3_raw_data["InputDataConfig"]
        )

    @cached_property
    def RecognizerMetadata(self):  # pragma: no cover
        return EntityRecognizerMetadata.make_one(
            self.boto3_raw_data["RecognizerMetadata"]
        )

    DataAccessRoleArn = field("DataAccessRoleArn")
    VolumeKmsKeyId = field("VolumeKmsKeyId")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["VpcConfig"])

    ModelKmsKeyId = field("ModelKmsKeyId")
    VersionName = field("VersionName")
    SourceModelArn = field("SourceModelArn")
    FlywheelArn = field("FlywheelArn")

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return EntityRecognizerOutputDataConfig.make_one(
            self.boto3_raw_data["OutputDataConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EntityRecognizerPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityRecognizerPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectEntitiesResponse:
    boto3_raw_data: "type_defs.DetectEntitiesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Entities(self):  # pragma: no cover
        return Entity.make_many(self.boto3_raw_data["Entities"])

    @cached_property
    def DocumentMetadata(self):  # pragma: no cover
        return DocumentMetadata.make_one(self.boto3_raw_data["DocumentMetadata"])

    @cached_property
    def DocumentType(self):  # pragma: no cover
        return DocumentTypeListItem.make_many(self.boto3_raw_data["DocumentType"])

    @cached_property
    def Blocks(self):  # pragma: no cover
        return Block.make_many(self.boto3_raw_data["Blocks"])

    @cached_property
    def Errors(self):  # pragma: no cover
        return ErrorsListItem.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectEntitiesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectEntitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetectSyntaxResponse:
    boto3_raw_data: "type_defs.BatchDetectSyntaxResponseTypeDef" = dataclasses.field()

    @cached_property
    def ResultList(self):  # pragma: no cover
        return BatchDetectSyntaxItemResult.make_many(self.boto3_raw_data["ResultList"])

    @cached_property
    def ErrorList(self):  # pragma: no cover
        return BatchItemError.make_many(self.boto3_raw_data["ErrorList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDetectSyntaxResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetectSyntaxResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetectTargetedSentimentItemResult:
    boto3_raw_data: "type_defs.BatchDetectTargetedSentimentItemResultTypeDef" = (
        dataclasses.field()
    )

    Index = field("Index")

    @cached_property
    def Entities(self):  # pragma: no cover
        return TargetedSentimentEntity.make_many(self.boto3_raw_data["Entities"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDetectTargetedSentimentItemResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetectTargetedSentimentItemResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectTargetedSentimentResponse:
    boto3_raw_data: "type_defs.DetectTargetedSentimentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Entities(self):  # pragma: no cover
        return TargetedSentimentEntity.make_many(self.boto3_raw_data["Entities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DetectTargetedSentimentResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectTargetedSentimentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetectEntitiesResponse:
    boto3_raw_data: "type_defs.BatchDetectEntitiesResponseTypeDef" = dataclasses.field()

    @cached_property
    def ResultList(self):  # pragma: no cover
        return BatchDetectEntitiesItemResult.make_many(
            self.boto3_raw_data["ResultList"]
        )

    @cached_property
    def ErrorList(self):  # pragma: no cover
        return BatchItemError.make_many(self.boto3_raw_data["ErrorList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDetectEntitiesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetectEntitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFlywheelResponse:
    boto3_raw_data: "type_defs.DescribeFlywheelResponseTypeDef" = dataclasses.field()

    @cached_property
    def FlywheelProperties(self):  # pragma: no cover
        return FlywheelProperties.make_one(self.boto3_raw_data["FlywheelProperties"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFlywheelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFlywheelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFlywheelResponse:
    boto3_raw_data: "type_defs.UpdateFlywheelResponseTypeDef" = dataclasses.field()

    @cached_property
    def FlywheelProperties(self):  # pragma: no cover
        return FlywheelProperties.make_one(self.boto3_raw_data["FlywheelProperties"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFlywheelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFlywheelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFlywheelRequest:
    boto3_raw_data: "type_defs.CreateFlywheelRequestTypeDef" = dataclasses.field()

    FlywheelName = field("FlywheelName")
    DataAccessRoleArn = field("DataAccessRoleArn")
    DataLakeS3Uri = field("DataLakeS3Uri")
    ActiveModelArn = field("ActiveModelArn")
    TaskConfig = field("TaskConfig")
    ModelType = field("ModelType")
    DataSecurityConfig = field("DataSecurityConfig")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFlywheelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFlywheelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEntityRecognizerResponse:
    boto3_raw_data: "type_defs.DescribeEntityRecognizerResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EntityRecognizerProperties(self):  # pragma: no cover
        return EntityRecognizerProperties.make_one(
            self.boto3_raw_data["EntityRecognizerProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEntityRecognizerResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEntityRecognizerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntityRecognizersResponse:
    boto3_raw_data: "type_defs.ListEntityRecognizersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EntityRecognizerPropertiesList(self):  # pragma: no cover
        return EntityRecognizerProperties.make_many(
            self.boto3_raw_data["EntityRecognizerPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEntityRecognizersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntityRecognizersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetectTargetedSentimentResponse:
    boto3_raw_data: "type_defs.BatchDetectTargetedSentimentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResultList(self):  # pragma: no cover
        return BatchDetectTargetedSentimentItemResult.make_many(
            self.boto3_raw_data["ResultList"]
        )

    @cached_property
    def ErrorList(self):  # pragma: no cover
        return BatchItemError.make_many(self.boto3_raw_data["ErrorList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDetectTargetedSentimentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetectTargetedSentimentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
