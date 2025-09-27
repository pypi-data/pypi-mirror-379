# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_bedrock_data_automation import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AudioExtractionCategoryOutput:
    boto3_raw_data: "type_defs.AudioExtractionCategoryOutputTypeDef" = (
        dataclasses.field()
    )

    state = field("state")
    types = field("types")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AudioExtractionCategoryOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioExtractionCategoryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioExtractionCategory:
    boto3_raw_data: "type_defs.AudioExtractionCategoryTypeDef" = dataclasses.field()

    state = field("state")
    types = field("types")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioExtractionCategoryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioExtractionCategoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModalityProcessingConfiguration:
    boto3_raw_data: "type_defs.ModalityProcessingConfigurationTypeDef" = (
        dataclasses.field()
    )

    state = field("state")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModalityProcessingConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModalityProcessingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioStandardGenerativeFieldOutput:
    boto3_raw_data: "type_defs.AudioStandardGenerativeFieldOutputTypeDef" = (
        dataclasses.field()
    )

    state = field("state")
    types = field("types")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AudioStandardGenerativeFieldOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioStandardGenerativeFieldOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioStandardGenerativeField:
    boto3_raw_data: "type_defs.AudioStandardGenerativeFieldTypeDef" = (
        dataclasses.field()
    )

    state = field("state")
    types = field("types")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioStandardGenerativeFieldTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioStandardGenerativeFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlueprintFilter:
    boto3_raw_data: "type_defs.BlueprintFilterTypeDef" = dataclasses.field()

    blueprintArn = field("blueprintArn")
    blueprintVersion = field("blueprintVersion")
    blueprintStage = field("blueprintStage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BlueprintFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BlueprintFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlueprintItem:
    boto3_raw_data: "type_defs.BlueprintItemTypeDef" = dataclasses.field()

    blueprintArn = field("blueprintArn")
    blueprintVersion = field("blueprintVersion")
    blueprintStage = field("blueprintStage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BlueprintItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BlueprintItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlueprintSummary:
    boto3_raw_data: "type_defs.BlueprintSummaryTypeDef" = dataclasses.field()

    blueprintArn = field("blueprintArn")
    creationTime = field("creationTime")
    blueprintVersion = field("blueprintVersion")
    blueprintStage = field("blueprintStage")
    blueprintName = field("blueprintName")
    lastModifiedTime = field("lastModifiedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BlueprintSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BlueprintSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Blueprint:
    boto3_raw_data: "type_defs.BlueprintTypeDef" = dataclasses.field()

    blueprintArn = field("blueprintArn")
    schema = field("schema")
    type = field("type")
    creationTime = field("creationTime")
    lastModifiedTime = field("lastModifiedTime")
    blueprintName = field("blueprintName")
    blueprintVersion = field("blueprintVersion")
    blueprintStage = field("blueprintStage")
    kmsKeyId = field("kmsKeyId")
    kmsEncryptionContext = field("kmsEncryptionContext")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BlueprintTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BlueprintTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionConfiguration:
    boto3_raw_data: "type_defs.EncryptionConfigurationTypeDef" = dataclasses.field()

    kmsKeyId = field("kmsKeyId")
    kmsEncryptionContext = field("kmsEncryptionContext")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncryptionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionConfigurationTypeDef"]
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

    key = field("key")
    value = field("value")

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
class CreateBlueprintVersionRequest:
    boto3_raw_data: "type_defs.CreateBlueprintVersionRequestTypeDef" = (
        dataclasses.field()
    )

    blueprintArn = field("blueprintArn")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateBlueprintVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBlueprintVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataAutomationProjectFilter:
    boto3_raw_data: "type_defs.DataAutomationProjectFilterTypeDef" = dataclasses.field()

    projectArn = field("projectArn")
    projectStage = field("projectStage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataAutomationProjectFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataAutomationProjectFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataAutomationProjectSummary:
    boto3_raw_data: "type_defs.DataAutomationProjectSummaryTypeDef" = (
        dataclasses.field()
    )

    projectArn = field("projectArn")
    creationTime = field("creationTime")
    projectStage = field("projectStage")
    projectName = field("projectName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataAutomationProjectSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataAutomationProjectSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBlueprintRequest:
    boto3_raw_data: "type_defs.DeleteBlueprintRequestTypeDef" = dataclasses.field()

    blueprintArn = field("blueprintArn")
    blueprintVersion = field("blueprintVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBlueprintRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBlueprintRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataAutomationProjectRequest:
    boto3_raw_data: "type_defs.DeleteDataAutomationProjectRequestTypeDef" = (
        dataclasses.field()
    )

    projectArn = field("projectArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDataAutomationProjectRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataAutomationProjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentBoundingBox:
    boto3_raw_data: "type_defs.DocumentBoundingBoxTypeDef" = dataclasses.field()

    state = field("state")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentBoundingBoxTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentBoundingBoxTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentExtractionGranularityOutput:
    boto3_raw_data: "type_defs.DocumentExtractionGranularityOutputTypeDef" = (
        dataclasses.field()
    )

    types = field("types")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DocumentExtractionGranularityOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentExtractionGranularityOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentExtractionGranularity:
    boto3_raw_data: "type_defs.DocumentExtractionGranularityTypeDef" = (
        dataclasses.field()
    )

    types = field("types")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DocumentExtractionGranularityTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentExtractionGranularityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentOutputAdditionalFileFormat:
    boto3_raw_data: "type_defs.DocumentOutputAdditionalFileFormatTypeDef" = (
        dataclasses.field()
    )

    state = field("state")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DocumentOutputAdditionalFileFormatTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentOutputAdditionalFileFormatTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentOutputTextFormatOutput:
    boto3_raw_data: "type_defs.DocumentOutputTextFormatOutputTypeDef" = (
        dataclasses.field()
    )

    types = field("types")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DocumentOutputTextFormatOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentOutputTextFormatOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentOutputTextFormat:
    boto3_raw_data: "type_defs.DocumentOutputTextFormatTypeDef" = dataclasses.field()

    types = field("types")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentOutputTextFormatTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentOutputTextFormatTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SplitterConfiguration:
    boto3_raw_data: "type_defs.SplitterConfigurationTypeDef" = dataclasses.field()

    state = field("state")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SplitterConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SplitterConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentStandardGenerativeField:
    boto3_raw_data: "type_defs.DocumentStandardGenerativeFieldTypeDef" = (
        dataclasses.field()
    )

    state = field("state")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DocumentStandardGenerativeFieldTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentStandardGenerativeFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBlueprintRequest:
    boto3_raw_data: "type_defs.GetBlueprintRequestTypeDef" = dataclasses.field()

    blueprintArn = field("blueprintArn")
    blueprintVersion = field("blueprintVersion")
    blueprintStage = field("blueprintStage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBlueprintRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBlueprintRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataAutomationProjectRequest:
    boto3_raw_data: "type_defs.GetDataAutomationProjectRequestTypeDef" = (
        dataclasses.field()
    )

    projectArn = field("projectArn")
    projectStage = field("projectStage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDataAutomationProjectRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataAutomationProjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageBoundingBox:
    boto3_raw_data: "type_defs.ImageBoundingBoxTypeDef" = dataclasses.field()

    state = field("state")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageBoundingBoxTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageBoundingBoxTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageExtractionCategoryOutput:
    boto3_raw_data: "type_defs.ImageExtractionCategoryOutputTypeDef" = (
        dataclasses.field()
    )

    state = field("state")
    types = field("types")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ImageExtractionCategoryOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageExtractionCategoryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageExtractionCategory:
    boto3_raw_data: "type_defs.ImageExtractionCategoryTypeDef" = dataclasses.field()

    state = field("state")
    types = field("types")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageExtractionCategoryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageExtractionCategoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageStandardGenerativeFieldOutput:
    boto3_raw_data: "type_defs.ImageStandardGenerativeFieldOutputTypeDef" = (
        dataclasses.field()
    )

    state = field("state")
    types = field("types")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ImageStandardGenerativeFieldOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageStandardGenerativeFieldOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageStandardGenerativeField:
    boto3_raw_data: "type_defs.ImageStandardGenerativeFieldTypeDef" = (
        dataclasses.field()
    )

    state = field("state")
    types = field("types")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageStandardGenerativeFieldTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageStandardGenerativeFieldTypeDef"]
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
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    resourceARN = field("resourceARN")

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
class ModalityRoutingConfiguration:
    boto3_raw_data: "type_defs.ModalityRoutingConfigurationTypeDef" = (
        dataclasses.field()
    )

    jpeg = field("jpeg")
    png = field("png")
    mp4 = field("mp4")
    mov = field("mov")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModalityRoutingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModalityRoutingConfigurationTypeDef"]
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

    resourceARN = field("resourceARN")
    tagKeys = field("tagKeys")

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
class VideoBoundingBox:
    boto3_raw_data: "type_defs.VideoBoundingBoxTypeDef" = dataclasses.field()

    state = field("state")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VideoBoundingBoxTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoBoundingBoxTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoExtractionCategoryOutput:
    boto3_raw_data: "type_defs.VideoExtractionCategoryOutputTypeDef" = (
        dataclasses.field()
    )

    state = field("state")
    types = field("types")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VideoExtractionCategoryOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoExtractionCategoryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoExtractionCategory:
    boto3_raw_data: "type_defs.VideoExtractionCategoryTypeDef" = dataclasses.field()

    state = field("state")
    types = field("types")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VideoExtractionCategoryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoExtractionCategoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoStandardGenerativeFieldOutput:
    boto3_raw_data: "type_defs.VideoStandardGenerativeFieldOutputTypeDef" = (
        dataclasses.field()
    )

    state = field("state")
    types = field("types")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VideoStandardGenerativeFieldOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoStandardGenerativeFieldOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoStandardGenerativeField:
    boto3_raw_data: "type_defs.VideoStandardGenerativeFieldTypeDef" = (
        dataclasses.field()
    )

    state = field("state")
    types = field("types")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VideoStandardGenerativeFieldTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoStandardGenerativeFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioStandardExtractionOutput:
    boto3_raw_data: "type_defs.AudioStandardExtractionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def category(self):  # pragma: no cover
        return AudioExtractionCategoryOutput.make_one(self.boto3_raw_data["category"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AudioStandardExtractionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioStandardExtractionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioStandardExtraction:
    boto3_raw_data: "type_defs.AudioStandardExtractionTypeDef" = dataclasses.field()

    @cached_property
    def category(self):  # pragma: no cover
        return AudioExtractionCategory.make_one(self.boto3_raw_data["category"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioStandardExtractionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioStandardExtractionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioOverrideConfiguration:
    boto3_raw_data: "type_defs.AudioOverrideConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def modalityProcessing(self):  # pragma: no cover
        return ModalityProcessingConfiguration.make_one(
            self.boto3_raw_data["modalityProcessing"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioOverrideConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioOverrideConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageOverrideConfiguration:
    boto3_raw_data: "type_defs.ImageOverrideConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def modalityProcessing(self):  # pragma: no cover
        return ModalityProcessingConfiguration.make_one(
            self.boto3_raw_data["modalityProcessing"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageOverrideConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageOverrideConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoOverrideConfiguration:
    boto3_raw_data: "type_defs.VideoOverrideConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def modalityProcessing(self):  # pragma: no cover
        return ModalityProcessingConfiguration.make_one(
            self.boto3_raw_data["modalityProcessing"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VideoOverrideConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoOverrideConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataAutomationProjectsRequest:
    boto3_raw_data: "type_defs.ListDataAutomationProjectsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    projectStageFilter = field("projectStageFilter")

    @cached_property
    def blueprintFilter(self):  # pragma: no cover
        return BlueprintFilter.make_one(self.boto3_raw_data["blueprintFilter"])

    resourceOwner = field("resourceOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataAutomationProjectsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataAutomationProjectsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomOutputConfigurationOutput:
    boto3_raw_data: "type_defs.CustomOutputConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def blueprints(self):  # pragma: no cover
        return BlueprintItem.make_many(self.boto3_raw_data["blueprints"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomOutputConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomOutputConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomOutputConfiguration:
    boto3_raw_data: "type_defs.CustomOutputConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def blueprints(self):  # pragma: no cover
        return BlueprintItem.make_many(self.boto3_raw_data["blueprints"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomOutputConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomOutputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBlueprintRequest:
    boto3_raw_data: "type_defs.UpdateBlueprintRequestTypeDef" = dataclasses.field()

    blueprintArn = field("blueprintArn")
    schema = field("schema")
    blueprintStage = field("blueprintStage")

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBlueprintRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBlueprintRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBlueprintRequest:
    boto3_raw_data: "type_defs.CreateBlueprintRequestTypeDef" = dataclasses.field()

    blueprintName = field("blueprintName")
    type = field("type")
    schema = field("schema")
    blueprintStage = field("blueprintStage")
    clientToken = field("clientToken")

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBlueprintRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBlueprintRequestTypeDef"]
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

    resourceARN = field("resourceARN")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class CreateBlueprintResponse:
    boto3_raw_data: "type_defs.CreateBlueprintResponseTypeDef" = dataclasses.field()

    @cached_property
    def blueprint(self):  # pragma: no cover
        return Blueprint.make_one(self.boto3_raw_data["blueprint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBlueprintResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBlueprintResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBlueprintVersionResponse:
    boto3_raw_data: "type_defs.CreateBlueprintVersionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def blueprint(self):  # pragma: no cover
        return Blueprint.make_one(self.boto3_raw_data["blueprint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateBlueprintVersionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBlueprintVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataAutomationProjectResponse:
    boto3_raw_data: "type_defs.CreateDataAutomationProjectResponseTypeDef" = (
        dataclasses.field()
    )

    projectArn = field("projectArn")
    projectStage = field("projectStage")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDataAutomationProjectResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataAutomationProjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataAutomationProjectResponse:
    boto3_raw_data: "type_defs.DeleteDataAutomationProjectResponseTypeDef" = (
        dataclasses.field()
    )

    projectArn = field("projectArn")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDataAutomationProjectResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataAutomationProjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBlueprintResponse:
    boto3_raw_data: "type_defs.GetBlueprintResponseTypeDef" = dataclasses.field()

    @cached_property
    def blueprint(self):  # pragma: no cover
        return Blueprint.make_one(self.boto3_raw_data["blueprint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBlueprintResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBlueprintResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBlueprintsResponse:
    boto3_raw_data: "type_defs.ListBlueprintsResponseTypeDef" = dataclasses.field()

    @cached_property
    def blueprints(self):  # pragma: no cover
        return BlueprintSummary.make_many(self.boto3_raw_data["blueprints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBlueprintsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBlueprintsResponseTypeDef"]
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
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class UpdateBlueprintResponse:
    boto3_raw_data: "type_defs.UpdateBlueprintResponseTypeDef" = dataclasses.field()

    @cached_property
    def blueprint(self):  # pragma: no cover
        return Blueprint.make_one(self.boto3_raw_data["blueprint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBlueprintResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBlueprintResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataAutomationProjectResponse:
    boto3_raw_data: "type_defs.UpdateDataAutomationProjectResponseTypeDef" = (
        dataclasses.field()
    )

    projectArn = field("projectArn")
    projectStage = field("projectStage")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDataAutomationProjectResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataAutomationProjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBlueprintsRequest:
    boto3_raw_data: "type_defs.ListBlueprintsRequestTypeDef" = dataclasses.field()

    blueprintArn = field("blueprintArn")
    resourceOwner = field("resourceOwner")
    blueprintStageFilter = field("blueprintStageFilter")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def projectFilter(self):  # pragma: no cover
        return DataAutomationProjectFilter.make_one(
            self.boto3_raw_data["projectFilter"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBlueprintsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBlueprintsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataAutomationProjectsResponse:
    boto3_raw_data: "type_defs.ListDataAutomationProjectsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def projects(self):  # pragma: no cover
        return DataAutomationProjectSummary.make_many(self.boto3_raw_data["projects"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataAutomationProjectsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataAutomationProjectsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentStandardExtractionOutput:
    boto3_raw_data: "type_defs.DocumentStandardExtractionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def granularity(self):  # pragma: no cover
        return DocumentExtractionGranularityOutput.make_one(
            self.boto3_raw_data["granularity"]
        )

    @cached_property
    def boundingBox(self):  # pragma: no cover
        return DocumentBoundingBox.make_one(self.boto3_raw_data["boundingBox"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DocumentStandardExtractionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentStandardExtractionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentStandardExtraction:
    boto3_raw_data: "type_defs.DocumentStandardExtractionTypeDef" = dataclasses.field()

    @cached_property
    def granularity(self):  # pragma: no cover
        return DocumentExtractionGranularity.make_one(
            self.boto3_raw_data["granularity"]
        )

    @cached_property
    def boundingBox(self):  # pragma: no cover
        return DocumentBoundingBox.make_one(self.boto3_raw_data["boundingBox"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentStandardExtractionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentStandardExtractionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentOutputFormatOutput:
    boto3_raw_data: "type_defs.DocumentOutputFormatOutputTypeDef" = dataclasses.field()

    @cached_property
    def textFormat(self):  # pragma: no cover
        return DocumentOutputTextFormatOutput.make_one(
            self.boto3_raw_data["textFormat"]
        )

    @cached_property
    def additionalFileFormat(self):  # pragma: no cover
        return DocumentOutputAdditionalFileFormat.make_one(
            self.boto3_raw_data["additionalFileFormat"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentOutputFormatOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentOutputFormatOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentOutputFormat:
    boto3_raw_data: "type_defs.DocumentOutputFormatTypeDef" = dataclasses.field()

    @cached_property
    def textFormat(self):  # pragma: no cover
        return DocumentOutputTextFormat.make_one(self.boto3_raw_data["textFormat"])

    @cached_property
    def additionalFileFormat(self):  # pragma: no cover
        return DocumentOutputAdditionalFileFormat.make_one(
            self.boto3_raw_data["additionalFileFormat"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentOutputFormatTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentOutputFormatTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentOverrideConfiguration:
    boto3_raw_data: "type_defs.DocumentOverrideConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def splitter(self):  # pragma: no cover
        return SplitterConfiguration.make_one(self.boto3_raw_data["splitter"])

    @cached_property
    def modalityProcessing(self):  # pragma: no cover
        return ModalityProcessingConfiguration.make_one(
            self.boto3_raw_data["modalityProcessing"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DocumentOverrideConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentOverrideConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageStandardExtractionOutput:
    boto3_raw_data: "type_defs.ImageStandardExtractionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def category(self):  # pragma: no cover
        return ImageExtractionCategoryOutput.make_one(self.boto3_raw_data["category"])

    @cached_property
    def boundingBox(self):  # pragma: no cover
        return ImageBoundingBox.make_one(self.boto3_raw_data["boundingBox"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ImageStandardExtractionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageStandardExtractionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageStandardExtraction:
    boto3_raw_data: "type_defs.ImageStandardExtractionTypeDef" = dataclasses.field()

    @cached_property
    def category(self):  # pragma: no cover
        return ImageExtractionCategory.make_one(self.boto3_raw_data["category"])

    @cached_property
    def boundingBox(self):  # pragma: no cover
        return ImageBoundingBox.make_one(self.boto3_raw_data["boundingBox"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageStandardExtractionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageStandardExtractionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBlueprintsRequestPaginate:
    boto3_raw_data: "type_defs.ListBlueprintsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    blueprintArn = field("blueprintArn")
    resourceOwner = field("resourceOwner")
    blueprintStageFilter = field("blueprintStageFilter")

    @cached_property
    def projectFilter(self):  # pragma: no cover
        return DataAutomationProjectFilter.make_one(
            self.boto3_raw_data["projectFilter"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBlueprintsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBlueprintsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataAutomationProjectsRequestPaginate:
    boto3_raw_data: "type_defs.ListDataAutomationProjectsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    projectStageFilter = field("projectStageFilter")

    @cached_property
    def blueprintFilter(self):  # pragma: no cover
        return BlueprintFilter.make_one(self.boto3_raw_data["blueprintFilter"])

    resourceOwner = field("resourceOwner")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataAutomationProjectsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataAutomationProjectsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoStandardExtractionOutput:
    boto3_raw_data: "type_defs.VideoStandardExtractionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def category(self):  # pragma: no cover
        return VideoExtractionCategoryOutput.make_one(self.boto3_raw_data["category"])

    @cached_property
    def boundingBox(self):  # pragma: no cover
        return VideoBoundingBox.make_one(self.boto3_raw_data["boundingBox"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VideoStandardExtractionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoStandardExtractionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoStandardExtraction:
    boto3_raw_data: "type_defs.VideoStandardExtractionTypeDef" = dataclasses.field()

    @cached_property
    def category(self):  # pragma: no cover
        return VideoExtractionCategory.make_one(self.boto3_raw_data["category"])

    @cached_property
    def boundingBox(self):  # pragma: no cover
        return VideoBoundingBox.make_one(self.boto3_raw_data["boundingBox"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VideoStandardExtractionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoStandardExtractionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioStandardOutputConfigurationOutput:
    boto3_raw_data: "type_defs.AudioStandardOutputConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def extraction(self):  # pragma: no cover
        return AudioStandardExtractionOutput.make_one(self.boto3_raw_data["extraction"])

    @cached_property
    def generativeField(self):  # pragma: no cover
        return AudioStandardGenerativeFieldOutput.make_one(
            self.boto3_raw_data["generativeField"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AudioStandardOutputConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioStandardOutputConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioStandardOutputConfiguration:
    boto3_raw_data: "type_defs.AudioStandardOutputConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def extraction(self):  # pragma: no cover
        return AudioStandardExtraction.make_one(self.boto3_raw_data["extraction"])

    @cached_property
    def generativeField(self):  # pragma: no cover
        return AudioStandardGenerativeField.make_one(
            self.boto3_raw_data["generativeField"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AudioStandardOutputConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioStandardOutputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentStandardOutputConfigurationOutput:
    boto3_raw_data: "type_defs.DocumentStandardOutputConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def extraction(self):  # pragma: no cover
        return DocumentStandardExtractionOutput.make_one(
            self.boto3_raw_data["extraction"]
        )

    @cached_property
    def generativeField(self):  # pragma: no cover
        return DocumentStandardGenerativeField.make_one(
            self.boto3_raw_data["generativeField"]
        )

    @cached_property
    def outputFormat(self):  # pragma: no cover
        return DocumentOutputFormatOutput.make_one(self.boto3_raw_data["outputFormat"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DocumentStandardOutputConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentStandardOutputConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentStandardOutputConfiguration:
    boto3_raw_data: "type_defs.DocumentStandardOutputConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def extraction(self):  # pragma: no cover
        return DocumentStandardExtraction.make_one(self.boto3_raw_data["extraction"])

    @cached_property
    def generativeField(self):  # pragma: no cover
        return DocumentStandardGenerativeField.make_one(
            self.boto3_raw_data["generativeField"]
        )

    @cached_property
    def outputFormat(self):  # pragma: no cover
        return DocumentOutputFormat.make_one(self.boto3_raw_data["outputFormat"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DocumentStandardOutputConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentStandardOutputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OverrideConfiguration:
    boto3_raw_data: "type_defs.OverrideConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def document(self):  # pragma: no cover
        return DocumentOverrideConfiguration.make_one(self.boto3_raw_data["document"])

    @cached_property
    def image(self):  # pragma: no cover
        return ImageOverrideConfiguration.make_one(self.boto3_raw_data["image"])

    @cached_property
    def video(self):  # pragma: no cover
        return VideoOverrideConfiguration.make_one(self.boto3_raw_data["video"])

    @cached_property
    def audio(self):  # pragma: no cover
        return AudioOverrideConfiguration.make_one(self.boto3_raw_data["audio"])

    @cached_property
    def modalityRouting(self):  # pragma: no cover
        return ModalityRoutingConfiguration.make_one(
            self.boto3_raw_data["modalityRouting"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OverrideConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OverrideConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageStandardOutputConfigurationOutput:
    boto3_raw_data: "type_defs.ImageStandardOutputConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def extraction(self):  # pragma: no cover
        return ImageStandardExtractionOutput.make_one(self.boto3_raw_data["extraction"])

    @cached_property
    def generativeField(self):  # pragma: no cover
        return ImageStandardGenerativeFieldOutput.make_one(
            self.boto3_raw_data["generativeField"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ImageStandardOutputConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageStandardOutputConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageStandardOutputConfiguration:
    boto3_raw_data: "type_defs.ImageStandardOutputConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def extraction(self):  # pragma: no cover
        return ImageStandardExtraction.make_one(self.boto3_raw_data["extraction"])

    @cached_property
    def generativeField(self):  # pragma: no cover
        return ImageStandardGenerativeField.make_one(
            self.boto3_raw_data["generativeField"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ImageStandardOutputConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageStandardOutputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoStandardOutputConfigurationOutput:
    boto3_raw_data: "type_defs.VideoStandardOutputConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def extraction(self):  # pragma: no cover
        return VideoStandardExtractionOutput.make_one(self.boto3_raw_data["extraction"])

    @cached_property
    def generativeField(self):  # pragma: no cover
        return VideoStandardGenerativeFieldOutput.make_one(
            self.boto3_raw_data["generativeField"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VideoStandardOutputConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoStandardOutputConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoStandardOutputConfiguration:
    boto3_raw_data: "type_defs.VideoStandardOutputConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def extraction(self):  # pragma: no cover
        return VideoStandardExtraction.make_one(self.boto3_raw_data["extraction"])

    @cached_property
    def generativeField(self):  # pragma: no cover
        return VideoStandardGenerativeField.make_one(
            self.boto3_raw_data["generativeField"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VideoStandardOutputConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoStandardOutputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StandardOutputConfigurationOutput:
    boto3_raw_data: "type_defs.StandardOutputConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def document(self):  # pragma: no cover
        return DocumentStandardOutputConfigurationOutput.make_one(
            self.boto3_raw_data["document"]
        )

    @cached_property
    def image(self):  # pragma: no cover
        return ImageStandardOutputConfigurationOutput.make_one(
            self.boto3_raw_data["image"]
        )

    @cached_property
    def video(self):  # pragma: no cover
        return VideoStandardOutputConfigurationOutput.make_one(
            self.boto3_raw_data["video"]
        )

    @cached_property
    def audio(self):  # pragma: no cover
        return AudioStandardOutputConfigurationOutput.make_one(
            self.boto3_raw_data["audio"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StandardOutputConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StandardOutputConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StandardOutputConfiguration:
    boto3_raw_data: "type_defs.StandardOutputConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def document(self):  # pragma: no cover
        return DocumentStandardOutputConfiguration.make_one(
            self.boto3_raw_data["document"]
        )

    @cached_property
    def image(self):  # pragma: no cover
        return ImageStandardOutputConfiguration.make_one(self.boto3_raw_data["image"])

    @cached_property
    def video(self):  # pragma: no cover
        return VideoStandardOutputConfiguration.make_one(self.boto3_raw_data["video"])

    @cached_property
    def audio(self):  # pragma: no cover
        return AudioStandardOutputConfiguration.make_one(self.boto3_raw_data["audio"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StandardOutputConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StandardOutputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataAutomationProject:
    boto3_raw_data: "type_defs.DataAutomationProjectTypeDef" = dataclasses.field()

    projectArn = field("projectArn")
    creationTime = field("creationTime")
    lastModifiedTime = field("lastModifiedTime")
    projectName = field("projectName")
    status = field("status")
    projectStage = field("projectStage")
    projectDescription = field("projectDescription")

    @cached_property
    def standardOutputConfiguration(self):  # pragma: no cover
        return StandardOutputConfigurationOutput.make_one(
            self.boto3_raw_data["standardOutputConfiguration"]
        )

    @cached_property
    def customOutputConfiguration(self):  # pragma: no cover
        return CustomOutputConfigurationOutput.make_one(
            self.boto3_raw_data["customOutputConfiguration"]
        )

    @cached_property
    def overrideConfiguration(self):  # pragma: no cover
        return OverrideConfiguration.make_one(
            self.boto3_raw_data["overrideConfiguration"]
        )

    kmsKeyId = field("kmsKeyId")
    kmsEncryptionContext = field("kmsEncryptionContext")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataAutomationProjectTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataAutomationProjectTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataAutomationProjectResponse:
    boto3_raw_data: "type_defs.GetDataAutomationProjectResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def project(self):  # pragma: no cover
        return DataAutomationProject.make_one(self.boto3_raw_data["project"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDataAutomationProjectResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataAutomationProjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataAutomationProjectRequest:
    boto3_raw_data: "type_defs.CreateDataAutomationProjectRequestTypeDef" = (
        dataclasses.field()
    )

    projectName = field("projectName")
    standardOutputConfiguration = field("standardOutputConfiguration")
    projectDescription = field("projectDescription")
    projectStage = field("projectStage")
    customOutputConfiguration = field("customOutputConfiguration")

    @cached_property
    def overrideConfiguration(self):  # pragma: no cover
        return OverrideConfiguration.make_one(
            self.boto3_raw_data["overrideConfiguration"]
        )

    clientToken = field("clientToken")

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDataAutomationProjectRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataAutomationProjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataAutomationProjectRequest:
    boto3_raw_data: "type_defs.UpdateDataAutomationProjectRequestTypeDef" = (
        dataclasses.field()
    )

    projectArn = field("projectArn")
    standardOutputConfiguration = field("standardOutputConfiguration")
    projectStage = field("projectStage")
    projectDescription = field("projectDescription")
    customOutputConfiguration = field("customOutputConfiguration")

    @cached_property
    def overrideConfiguration(self):  # pragma: no cover
        return OverrideConfiguration.make_one(
            self.boto3_raw_data["overrideConfiguration"]
        )

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDataAutomationProjectRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataAutomationProjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
