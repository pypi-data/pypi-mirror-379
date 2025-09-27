# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_comprehendmedical import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Trait:
    boto3_raw_data: "type_defs.TraitTypeDef" = dataclasses.field()

    Name = field("Name")
    Score = field("Score")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TraitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TraitTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Characters:
    boto3_raw_data: "type_defs.CharactersTypeDef" = dataclasses.field()

    OriginalTextCharacters = field("OriginalTextCharacters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CharactersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CharactersTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDataConfig:
    boto3_raw_data: "type_defs.InputDataConfigTypeDef" = dataclasses.field()

    S3Bucket = field("S3Bucket")
    S3Key = field("S3Key")

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
class OutputDataConfig:
    boto3_raw_data: "type_defs.OutputDataConfigTypeDef" = dataclasses.field()

    S3Bucket = field("S3Bucket")
    S3Key = field("S3Key")

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
class DescribeEntitiesDetectionV2JobRequest:
    boto3_raw_data: "type_defs.DescribeEntitiesDetectionV2JobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEntitiesDetectionV2JobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEntitiesDetectionV2JobRequestTypeDef"]
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
class DescribeICD10CMInferenceJobRequest:
    boto3_raw_data: "type_defs.DescribeICD10CMInferenceJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeICD10CMInferenceJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeICD10CMInferenceJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePHIDetectionJobRequest:
    boto3_raw_data: "type_defs.DescribePHIDetectionJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePHIDetectionJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePHIDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRxNormInferenceJobRequest:
    boto3_raw_data: "type_defs.DescribeRxNormInferenceJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRxNormInferenceJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRxNormInferenceJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSNOMEDCTInferenceJobRequest:
    boto3_raw_data: "type_defs.DescribeSNOMEDCTInferenceJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSNOMEDCTInferenceJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSNOMEDCTInferenceJobRequestTypeDef"]
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
class DetectEntitiesV2Request:
    boto3_raw_data: "type_defs.DetectEntitiesV2RequestTypeDef" = dataclasses.field()

    Text = field("Text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectEntitiesV2RequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectEntitiesV2RequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectPHIRequest:
    boto3_raw_data: "type_defs.DetectPHIRequestTypeDef" = dataclasses.field()

    Text = field("Text")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DetectPHIRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectPHIRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ICD10CMTrait:
    boto3_raw_data: "type_defs.ICD10CMTraitTypeDef" = dataclasses.field()

    Name = field("Name")
    Score = field("Score")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ICD10CMTraitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ICD10CMTraitTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ICD10CMConcept:
    boto3_raw_data: "type_defs.ICD10CMConceptTypeDef" = dataclasses.field()

    Description = field("Description")
    Code = field("Code")
    Score = field("Score")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ICD10CMConceptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ICD10CMConceptTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferICD10CMRequest:
    boto3_raw_data: "type_defs.InferICD10CMRequestTypeDef" = dataclasses.field()

    Text = field("Text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferICD10CMRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferICD10CMRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferRxNormRequest:
    boto3_raw_data: "type_defs.InferRxNormRequestTypeDef" = dataclasses.field()

    Text = field("Text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferRxNormRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferRxNormRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferSNOMEDCTRequest:
    boto3_raw_data: "type_defs.InferSNOMEDCTRequestTypeDef" = dataclasses.field()

    Text = field("Text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferSNOMEDCTRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferSNOMEDCTRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SNOMEDCTDetails:
    boto3_raw_data: "type_defs.SNOMEDCTDetailsTypeDef" = dataclasses.field()

    Edition = field("Edition")
    Language = field("Language")
    VersionDate = field("VersionDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SNOMEDCTDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SNOMEDCTDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RxNormTrait:
    boto3_raw_data: "type_defs.RxNormTraitTypeDef" = dataclasses.field()

    Name = field("Name")
    Score = field("Score")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RxNormTraitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RxNormTraitTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RxNormConcept:
    boto3_raw_data: "type_defs.RxNormConceptTypeDef" = dataclasses.field()

    Description = field("Description")
    Code = field("Code")
    Score = field("Score")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RxNormConceptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RxNormConceptTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SNOMEDCTConcept:
    boto3_raw_data: "type_defs.SNOMEDCTConceptTypeDef" = dataclasses.field()

    Description = field("Description")
    Code = field("Code")
    Score = field("Score")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SNOMEDCTConceptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SNOMEDCTConceptTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SNOMEDCTTrait:
    boto3_raw_data: "type_defs.SNOMEDCTTraitTypeDef" = dataclasses.field()

    Name = field("Name")
    Score = field("Score")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SNOMEDCTTraitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SNOMEDCTTraitTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopEntitiesDetectionV2JobRequest:
    boto3_raw_data: "type_defs.StopEntitiesDetectionV2JobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopEntitiesDetectionV2JobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopEntitiesDetectionV2JobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopICD10CMInferenceJobRequest:
    boto3_raw_data: "type_defs.StopICD10CMInferenceJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopICD10CMInferenceJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopICD10CMInferenceJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopPHIDetectionJobRequest:
    boto3_raw_data: "type_defs.StopPHIDetectionJobRequestTypeDef" = dataclasses.field()

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopPHIDetectionJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopPHIDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopRxNormInferenceJobRequest:
    boto3_raw_data: "type_defs.StopRxNormInferenceJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopRxNormInferenceJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopRxNormInferenceJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopSNOMEDCTInferenceJobRequest:
    boto3_raw_data: "type_defs.StopSNOMEDCTInferenceJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopSNOMEDCTInferenceJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopSNOMEDCTInferenceJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Attribute:
    boto3_raw_data: "type_defs.AttributeTypeDef" = dataclasses.field()

    Type = field("Type")
    Score = field("Score")
    RelationshipScore = field("RelationshipScore")
    RelationshipType = field("RelationshipType")
    Id = field("Id")
    BeginOffset = field("BeginOffset")
    EndOffset = field("EndOffset")
    Text = field("Text")
    Category = field("Category")

    @cached_property
    def Traits(self):  # pragma: no cover
        return Trait.make_many(self.boto3_raw_data["Traits"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComprehendMedicalAsyncJobFilter:
    boto3_raw_data: "type_defs.ComprehendMedicalAsyncJobFilterTypeDef" = (
        dataclasses.field()
    )

    JobName = field("JobName")
    JobStatus = field("JobStatus")
    SubmitTimeBefore = field("SubmitTimeBefore")
    SubmitTimeAfter = field("SubmitTimeAfter")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ComprehendMedicalAsyncJobFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComprehendMedicalAsyncJobFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComprehendMedicalAsyncJobProperties:
    boto3_raw_data: "type_defs.ComprehendMedicalAsyncJobPropertiesTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    JobName = field("JobName")
    JobStatus = field("JobStatus")
    Message = field("Message")
    SubmitTime = field("SubmitTime")
    EndTime = field("EndTime")
    ExpirationTime = field("ExpirationTime")

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfig.make_one(self.boto3_raw_data["InputDataConfig"])

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    LanguageCode = field("LanguageCode")
    DataAccessRoleArn = field("DataAccessRoleArn")
    ManifestFilePath = field("ManifestFilePath")
    KMSKey = field("KMSKey")
    ModelVersion = field("ModelVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ComprehendMedicalAsyncJobPropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComprehendMedicalAsyncJobPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartEntitiesDetectionV2JobRequest:
    boto3_raw_data: "type_defs.StartEntitiesDetectionV2JobRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfig.make_one(self.boto3_raw_data["InputDataConfig"])

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    DataAccessRoleArn = field("DataAccessRoleArn")
    LanguageCode = field("LanguageCode")
    JobName = field("JobName")
    ClientRequestToken = field("ClientRequestToken")
    KMSKey = field("KMSKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartEntitiesDetectionV2JobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartEntitiesDetectionV2JobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartICD10CMInferenceJobRequest:
    boto3_raw_data: "type_defs.StartICD10CMInferenceJobRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfig.make_one(self.boto3_raw_data["InputDataConfig"])

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    DataAccessRoleArn = field("DataAccessRoleArn")
    LanguageCode = field("LanguageCode")
    JobName = field("JobName")
    ClientRequestToken = field("ClientRequestToken")
    KMSKey = field("KMSKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartICD10CMInferenceJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartICD10CMInferenceJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartPHIDetectionJobRequest:
    boto3_raw_data: "type_defs.StartPHIDetectionJobRequestTypeDef" = dataclasses.field()

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfig.make_one(self.boto3_raw_data["InputDataConfig"])

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    DataAccessRoleArn = field("DataAccessRoleArn")
    LanguageCode = field("LanguageCode")
    JobName = field("JobName")
    ClientRequestToken = field("ClientRequestToken")
    KMSKey = field("KMSKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartPHIDetectionJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartPHIDetectionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRxNormInferenceJobRequest:
    boto3_raw_data: "type_defs.StartRxNormInferenceJobRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfig.make_one(self.boto3_raw_data["InputDataConfig"])

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    DataAccessRoleArn = field("DataAccessRoleArn")
    LanguageCode = field("LanguageCode")
    JobName = field("JobName")
    ClientRequestToken = field("ClientRequestToken")
    KMSKey = field("KMSKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartRxNormInferenceJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRxNormInferenceJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSNOMEDCTInferenceJobRequest:
    boto3_raw_data: "type_defs.StartSNOMEDCTInferenceJobRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfig.make_one(self.boto3_raw_data["InputDataConfig"])

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    DataAccessRoleArn = field("DataAccessRoleArn")
    LanguageCode = field("LanguageCode")
    JobName = field("JobName")
    ClientRequestToken = field("ClientRequestToken")
    KMSKey = field("KMSKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartSNOMEDCTInferenceJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSNOMEDCTInferenceJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartEntitiesDetectionV2JobResponse:
    boto3_raw_data: "type_defs.StartEntitiesDetectionV2JobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartEntitiesDetectionV2JobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartEntitiesDetectionV2JobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartICD10CMInferenceJobResponse:
    boto3_raw_data: "type_defs.StartICD10CMInferenceJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartICD10CMInferenceJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartICD10CMInferenceJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartPHIDetectionJobResponse:
    boto3_raw_data: "type_defs.StartPHIDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartPHIDetectionJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartPHIDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRxNormInferenceJobResponse:
    boto3_raw_data: "type_defs.StartRxNormInferenceJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartRxNormInferenceJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRxNormInferenceJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSNOMEDCTInferenceJobResponse:
    boto3_raw_data: "type_defs.StartSNOMEDCTInferenceJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartSNOMEDCTInferenceJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSNOMEDCTInferenceJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopEntitiesDetectionV2JobResponse:
    boto3_raw_data: "type_defs.StopEntitiesDetectionV2JobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopEntitiesDetectionV2JobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopEntitiesDetectionV2JobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopICD10CMInferenceJobResponse:
    boto3_raw_data: "type_defs.StopICD10CMInferenceJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopICD10CMInferenceJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopICD10CMInferenceJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopPHIDetectionJobResponse:
    boto3_raw_data: "type_defs.StopPHIDetectionJobResponseTypeDef" = dataclasses.field()

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopPHIDetectionJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopPHIDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopRxNormInferenceJobResponse:
    boto3_raw_data: "type_defs.StopRxNormInferenceJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopRxNormInferenceJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopRxNormInferenceJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopSNOMEDCTInferenceJobResponse:
    boto3_raw_data: "type_defs.StopSNOMEDCTInferenceJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopSNOMEDCTInferenceJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopSNOMEDCTInferenceJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ICD10CMAttribute:
    boto3_raw_data: "type_defs.ICD10CMAttributeTypeDef" = dataclasses.field()

    Type = field("Type")
    Score = field("Score")
    RelationshipScore = field("RelationshipScore")
    Id = field("Id")
    BeginOffset = field("BeginOffset")
    EndOffset = field("EndOffset")
    Text = field("Text")

    @cached_property
    def Traits(self):  # pragma: no cover
        return ICD10CMTrait.make_many(self.boto3_raw_data["Traits"])

    Category = field("Category")
    RelationshipType = field("RelationshipType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ICD10CMAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ICD10CMAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RxNormAttribute:
    boto3_raw_data: "type_defs.RxNormAttributeTypeDef" = dataclasses.field()

    Type = field("Type")
    Score = field("Score")
    RelationshipScore = field("RelationshipScore")
    Id = field("Id")
    BeginOffset = field("BeginOffset")
    EndOffset = field("EndOffset")
    Text = field("Text")

    @cached_property
    def Traits(self):  # pragma: no cover
        return RxNormTrait.make_many(self.boto3_raw_data["Traits"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RxNormAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RxNormAttributeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SNOMEDCTAttribute:
    boto3_raw_data: "type_defs.SNOMEDCTAttributeTypeDef" = dataclasses.field()

    Category = field("Category")
    Type = field("Type")
    Score = field("Score")
    RelationshipScore = field("RelationshipScore")
    RelationshipType = field("RelationshipType")
    Id = field("Id")
    BeginOffset = field("BeginOffset")
    EndOffset = field("EndOffset")
    Text = field("Text")

    @cached_property
    def Traits(self):  # pragma: no cover
        return SNOMEDCTTrait.make_many(self.boto3_raw_data["Traits"])

    @cached_property
    def SNOMEDCTConcepts(self):  # pragma: no cover
        return SNOMEDCTConcept.make_many(self.boto3_raw_data["SNOMEDCTConcepts"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SNOMEDCTAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SNOMEDCTAttributeTypeDef"]
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

    Id = field("Id")
    BeginOffset = field("BeginOffset")
    EndOffset = field("EndOffset")
    Score = field("Score")
    Text = field("Text")
    Category = field("Category")
    Type = field("Type")

    @cached_property
    def Traits(self):  # pragma: no cover
        return Trait.make_many(self.boto3_raw_data["Traits"])

    @cached_property
    def Attributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["Attributes"])

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
class UnmappedAttribute:
    boto3_raw_data: "type_defs.UnmappedAttributeTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def Attribute(self):  # pragma: no cover
        return Attribute.make_one(self.boto3_raw_data["Attribute"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UnmappedAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnmappedAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntitiesDetectionV2JobsRequest:
    boto3_raw_data: "type_defs.ListEntitiesDetectionV2JobsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return ComprehendMedicalAsyncJobFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEntitiesDetectionV2JobsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntitiesDetectionV2JobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListICD10CMInferenceJobsRequest:
    boto3_raw_data: "type_defs.ListICD10CMInferenceJobsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return ComprehendMedicalAsyncJobFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListICD10CMInferenceJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListICD10CMInferenceJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPHIDetectionJobsRequest:
    boto3_raw_data: "type_defs.ListPHIDetectionJobsRequestTypeDef" = dataclasses.field()

    @cached_property
    def Filter(self):  # pragma: no cover
        return ComprehendMedicalAsyncJobFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPHIDetectionJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPHIDetectionJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRxNormInferenceJobsRequest:
    boto3_raw_data: "type_defs.ListRxNormInferenceJobsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return ComprehendMedicalAsyncJobFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRxNormInferenceJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRxNormInferenceJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSNOMEDCTInferenceJobsRequest:
    boto3_raw_data: "type_defs.ListSNOMEDCTInferenceJobsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return ComprehendMedicalAsyncJobFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSNOMEDCTInferenceJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSNOMEDCTInferenceJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEntitiesDetectionV2JobResponse:
    boto3_raw_data: "type_defs.DescribeEntitiesDetectionV2JobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ComprehendMedicalAsyncJobProperties(self):  # pragma: no cover
        return ComprehendMedicalAsyncJobProperties.make_one(
            self.boto3_raw_data["ComprehendMedicalAsyncJobProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEntitiesDetectionV2JobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEntitiesDetectionV2JobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeICD10CMInferenceJobResponse:
    boto3_raw_data: "type_defs.DescribeICD10CMInferenceJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ComprehendMedicalAsyncJobProperties(self):  # pragma: no cover
        return ComprehendMedicalAsyncJobProperties.make_one(
            self.boto3_raw_data["ComprehendMedicalAsyncJobProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeICD10CMInferenceJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeICD10CMInferenceJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePHIDetectionJobResponse:
    boto3_raw_data: "type_defs.DescribePHIDetectionJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ComprehendMedicalAsyncJobProperties(self):  # pragma: no cover
        return ComprehendMedicalAsyncJobProperties.make_one(
            self.boto3_raw_data["ComprehendMedicalAsyncJobProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePHIDetectionJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePHIDetectionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRxNormInferenceJobResponse:
    boto3_raw_data: "type_defs.DescribeRxNormInferenceJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ComprehendMedicalAsyncJobProperties(self):  # pragma: no cover
        return ComprehendMedicalAsyncJobProperties.make_one(
            self.boto3_raw_data["ComprehendMedicalAsyncJobProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRxNormInferenceJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRxNormInferenceJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSNOMEDCTInferenceJobResponse:
    boto3_raw_data: "type_defs.DescribeSNOMEDCTInferenceJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ComprehendMedicalAsyncJobProperties(self):  # pragma: no cover
        return ComprehendMedicalAsyncJobProperties.make_one(
            self.boto3_raw_data["ComprehendMedicalAsyncJobProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSNOMEDCTInferenceJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSNOMEDCTInferenceJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntitiesDetectionV2JobsResponse:
    boto3_raw_data: "type_defs.ListEntitiesDetectionV2JobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ComprehendMedicalAsyncJobPropertiesList(self):  # pragma: no cover
        return ComprehendMedicalAsyncJobProperties.make_many(
            self.boto3_raw_data["ComprehendMedicalAsyncJobPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEntitiesDetectionV2JobsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntitiesDetectionV2JobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListICD10CMInferenceJobsResponse:
    boto3_raw_data: "type_defs.ListICD10CMInferenceJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ComprehendMedicalAsyncJobPropertiesList(self):  # pragma: no cover
        return ComprehendMedicalAsyncJobProperties.make_many(
            self.boto3_raw_data["ComprehendMedicalAsyncJobPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListICD10CMInferenceJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListICD10CMInferenceJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPHIDetectionJobsResponse:
    boto3_raw_data: "type_defs.ListPHIDetectionJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ComprehendMedicalAsyncJobPropertiesList(self):  # pragma: no cover
        return ComprehendMedicalAsyncJobProperties.make_many(
            self.boto3_raw_data["ComprehendMedicalAsyncJobPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPHIDetectionJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPHIDetectionJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRxNormInferenceJobsResponse:
    boto3_raw_data: "type_defs.ListRxNormInferenceJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ComprehendMedicalAsyncJobPropertiesList(self):  # pragma: no cover
        return ComprehendMedicalAsyncJobProperties.make_many(
            self.boto3_raw_data["ComprehendMedicalAsyncJobPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRxNormInferenceJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRxNormInferenceJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSNOMEDCTInferenceJobsResponse:
    boto3_raw_data: "type_defs.ListSNOMEDCTInferenceJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ComprehendMedicalAsyncJobPropertiesList(self):  # pragma: no cover
        return ComprehendMedicalAsyncJobProperties.make_many(
            self.boto3_raw_data["ComprehendMedicalAsyncJobPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSNOMEDCTInferenceJobsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSNOMEDCTInferenceJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ICD10CMEntity:
    boto3_raw_data: "type_defs.ICD10CMEntityTypeDef" = dataclasses.field()

    Id = field("Id")
    Text = field("Text")
    Category = field("Category")
    Type = field("Type")
    Score = field("Score")
    BeginOffset = field("BeginOffset")
    EndOffset = field("EndOffset")

    @cached_property
    def Attributes(self):  # pragma: no cover
        return ICD10CMAttribute.make_many(self.boto3_raw_data["Attributes"])

    @cached_property
    def Traits(self):  # pragma: no cover
        return ICD10CMTrait.make_many(self.boto3_raw_data["Traits"])

    @cached_property
    def ICD10CMConcepts(self):  # pragma: no cover
        return ICD10CMConcept.make_many(self.boto3_raw_data["ICD10CMConcepts"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ICD10CMEntityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ICD10CMEntityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RxNormEntity:
    boto3_raw_data: "type_defs.RxNormEntityTypeDef" = dataclasses.field()

    Id = field("Id")
    Text = field("Text")
    Category = field("Category")
    Type = field("Type")
    Score = field("Score")
    BeginOffset = field("BeginOffset")
    EndOffset = field("EndOffset")

    @cached_property
    def Attributes(self):  # pragma: no cover
        return RxNormAttribute.make_many(self.boto3_raw_data["Attributes"])

    @cached_property
    def Traits(self):  # pragma: no cover
        return RxNormTrait.make_many(self.boto3_raw_data["Traits"])

    @cached_property
    def RxNormConcepts(self):  # pragma: no cover
        return RxNormConcept.make_many(self.boto3_raw_data["RxNormConcepts"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RxNormEntityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RxNormEntityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SNOMEDCTEntity:
    boto3_raw_data: "type_defs.SNOMEDCTEntityTypeDef" = dataclasses.field()

    Id = field("Id")
    Text = field("Text")
    Category = field("Category")
    Type = field("Type")
    Score = field("Score")
    BeginOffset = field("BeginOffset")
    EndOffset = field("EndOffset")

    @cached_property
    def Attributes(self):  # pragma: no cover
        return SNOMEDCTAttribute.make_many(self.boto3_raw_data["Attributes"])

    @cached_property
    def Traits(self):  # pragma: no cover
        return SNOMEDCTTrait.make_many(self.boto3_raw_data["Traits"])

    @cached_property
    def SNOMEDCTConcepts(self):  # pragma: no cover
        return SNOMEDCTConcept.make_many(self.boto3_raw_data["SNOMEDCTConcepts"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SNOMEDCTEntityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SNOMEDCTEntityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectPHIResponse:
    boto3_raw_data: "type_defs.DetectPHIResponseTypeDef" = dataclasses.field()

    @cached_property
    def Entities(self):  # pragma: no cover
        return Entity.make_many(self.boto3_raw_data["Entities"])

    ModelVersion = field("ModelVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    PaginationToken = field("PaginationToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DetectPHIResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectPHIResponseTypeDef"]
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
    def UnmappedAttributes(self):  # pragma: no cover
        return UnmappedAttribute.make_many(self.boto3_raw_data["UnmappedAttributes"])

    ModelVersion = field("ModelVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    PaginationToken = field("PaginationToken")

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
class DetectEntitiesV2Response:
    boto3_raw_data: "type_defs.DetectEntitiesV2ResponseTypeDef" = dataclasses.field()

    @cached_property
    def Entities(self):  # pragma: no cover
        return Entity.make_many(self.boto3_raw_data["Entities"])

    @cached_property
    def UnmappedAttributes(self):  # pragma: no cover
        return UnmappedAttribute.make_many(self.boto3_raw_data["UnmappedAttributes"])

    ModelVersion = field("ModelVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    PaginationToken = field("PaginationToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectEntitiesV2ResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectEntitiesV2ResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferICD10CMResponse:
    boto3_raw_data: "type_defs.InferICD10CMResponseTypeDef" = dataclasses.field()

    @cached_property
    def Entities(self):  # pragma: no cover
        return ICD10CMEntity.make_many(self.boto3_raw_data["Entities"])

    ModelVersion = field("ModelVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    PaginationToken = field("PaginationToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferICD10CMResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferICD10CMResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferRxNormResponse:
    boto3_raw_data: "type_defs.InferRxNormResponseTypeDef" = dataclasses.field()

    @cached_property
    def Entities(self):  # pragma: no cover
        return RxNormEntity.make_many(self.boto3_raw_data["Entities"])

    ModelVersion = field("ModelVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    PaginationToken = field("PaginationToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferRxNormResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferRxNormResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferSNOMEDCTResponse:
    boto3_raw_data: "type_defs.InferSNOMEDCTResponseTypeDef" = dataclasses.field()

    @cached_property
    def Entities(self):  # pragma: no cover
        return SNOMEDCTEntity.make_many(self.boto3_raw_data["Entities"])

    ModelVersion = field("ModelVersion")

    @cached_property
    def SNOMEDCTDetails(self):  # pragma: no cover
        return SNOMEDCTDetails.make_one(self.boto3_raw_data["SNOMEDCTDetails"])

    @cached_property
    def Characters(self):  # pragma: no cover
        return Characters.make_one(self.boto3_raw_data["Characters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    PaginationToken = field("PaginationToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferSNOMEDCTResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferSNOMEDCTResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
