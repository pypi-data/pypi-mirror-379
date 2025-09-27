# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cleanroomsml import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class S3ConfigMap:
    boto3_raw_data: "type_defs.S3ConfigMapTypeDef" = dataclasses.field()

    s3Uri = field("s3Uri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ConfigMapTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ConfigMapTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudienceSize:
    boto3_raw_data: "type_defs.AudienceSizeTypeDef" = dataclasses.field()

    type = field("type")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AudienceSizeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AudienceSizeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatusDetails:
    boto3_raw_data: "type_defs.StatusDetailsTypeDef" = dataclasses.field()

    statusCode = field("statusCode")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatusDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatusDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQuerySQLParametersOutput:
    boto3_raw_data: "type_defs.ProtectedQuerySQLParametersOutputTypeDef" = (
        dataclasses.field()
    )

    queryString = field("queryString")
    analysisTemplateArn = field("analysisTemplateArn")
    parameters = field("parameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedQuerySQLParametersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedQuerySQLParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQuerySQLParameters:
    boto3_raw_data: "type_defs.ProtectedQuerySQLParametersTypeDef" = dataclasses.field()

    queryString = field("queryString")
    analysisTemplateArn = field("analysisTemplateArn")
    parameters = field("parameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtectedQuerySQLParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedQuerySQLParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudienceGenerationJobSummary:
    boto3_raw_data: "type_defs.AudienceGenerationJobSummaryTypeDef" = (
        dataclasses.field()
    )

    createTime = field("createTime")
    updateTime = field("updateTime")
    audienceGenerationJobArn = field("audienceGenerationJobArn")
    name = field("name")
    status = field("status")
    configuredAudienceModelArn = field("configuredAudienceModelArn")
    description = field("description")
    collaborationId = field("collaborationId")
    startedBy = field("startedBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudienceGenerationJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudienceGenerationJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudienceModelSummary:
    boto3_raw_data: "type_defs.AudienceModelSummaryTypeDef" = dataclasses.field()

    createTime = field("createTime")
    updateTime = field("updateTime")
    audienceModelArn = field("audienceModelArn")
    name = field("name")
    trainingDatasetArn = field("trainingDatasetArn")
    status = field("status")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudienceModelSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudienceModelSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudienceSizeConfigOutput:
    boto3_raw_data: "type_defs.AudienceSizeConfigOutputTypeDef" = dataclasses.field()

    audienceSizeType = field("audienceSizeType")
    audienceSizeBins = field("audienceSizeBins")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudienceSizeConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudienceSizeConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudienceSizeConfig:
    boto3_raw_data: "type_defs.AudienceSizeConfigTypeDef" = dataclasses.field()

    audienceSizeType = field("audienceSizeType")
    audienceSizeBins = field("audienceSizeBins")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudienceSizeConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudienceSizeConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelTrainedModelInferenceJobRequest:
    boto3_raw_data: "type_defs.CancelTrainedModelInferenceJobRequestTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")
    trainedModelInferenceJobArn = field("trainedModelInferenceJobArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelTrainedModelInferenceJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelTrainedModelInferenceJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelTrainedModelRequest:
    boto3_raw_data: "type_defs.CancelTrainedModelRequestTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    trainedModelArn = field("trainedModelArn")
    versionIdentifier = field("versionIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelTrainedModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelTrainedModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollaborationConfiguredModelAlgorithmAssociationSummary:
    boto3_raw_data: (
        "type_defs.CollaborationConfiguredModelAlgorithmAssociationSummaryTypeDef"
    ) = dataclasses.field()

    createTime = field("createTime")
    updateTime = field("updateTime")
    configuredModelAlgorithmAssociationArn = field(
        "configuredModelAlgorithmAssociationArn"
    )
    name = field("name")
    membershipIdentifier = field("membershipIdentifier")
    collaborationIdentifier = field("collaborationIdentifier")
    configuredModelAlgorithmArn = field("configuredModelAlgorithmArn")
    creatorAccountId = field("creatorAccountId")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CollaborationConfiguredModelAlgorithmAssociationSummaryTypeDef"
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
                "type_defs.CollaborationConfiguredModelAlgorithmAssociationSummaryTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollaborationMLInputChannelSummary:
    boto3_raw_data: "type_defs.CollaborationMLInputChannelSummaryTypeDef" = (
        dataclasses.field()
    )

    createTime = field("createTime")
    updateTime = field("updateTime")
    membershipIdentifier = field("membershipIdentifier")
    collaborationIdentifier = field("collaborationIdentifier")
    name = field("name")
    configuredModelAlgorithmAssociations = field("configuredModelAlgorithmAssociations")
    mlInputChannelArn = field("mlInputChannelArn")
    status = field("status")
    creatorAccountId = field("creatorAccountId")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CollaborationMLInputChannelSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollaborationMLInputChannelSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IncrementalTrainingDataChannelOutput:
    boto3_raw_data: "type_defs.IncrementalTrainingDataChannelOutputTypeDef" = (
        dataclasses.field()
    )

    channelName = field("channelName")
    modelName = field("modelName")
    versionIdentifier = field("versionIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IncrementalTrainingDataChannelOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IncrementalTrainingDataChannelOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColumnSchemaOutput:
    boto3_raw_data: "type_defs.ColumnSchemaOutputTypeDef" = dataclasses.field()

    columnName = field("columnName")
    columnTypes = field("columnTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ColumnSchemaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ColumnSchemaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColumnSchema:
    boto3_raw_data: "type_defs.ColumnSchemaTypeDef" = dataclasses.field()

    columnName = field("columnName")
    columnTypes = field("columnTypes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ColumnSchemaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ColumnSchemaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkerComputeConfiguration:
    boto3_raw_data: "type_defs.WorkerComputeConfigurationTypeDef" = dataclasses.field()

    type = field("type")
    number = field("number")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkerComputeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkerComputeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredModelAlgorithmAssociationSummary:
    boto3_raw_data: "type_defs.ConfiguredModelAlgorithmAssociationSummaryTypeDef" = (
        dataclasses.field()
    )

    createTime = field("createTime")
    updateTime = field("updateTime")
    configuredModelAlgorithmAssociationArn = field(
        "configuredModelAlgorithmAssociationArn"
    )
    configuredModelAlgorithmArn = field("configuredModelAlgorithmArn")
    name = field("name")
    membershipIdentifier = field("membershipIdentifier")
    collaborationIdentifier = field("collaborationIdentifier")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfiguredModelAlgorithmAssociationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfiguredModelAlgorithmAssociationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredModelAlgorithmSummary:
    boto3_raw_data: "type_defs.ConfiguredModelAlgorithmSummaryTypeDef" = (
        dataclasses.field()
    )

    createTime = field("createTime")
    updateTime = field("updateTime")
    configuredModelAlgorithmArn = field("configuredModelAlgorithmArn")
    name = field("name")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConfiguredModelAlgorithmSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfiguredModelAlgorithmSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDefinition:
    boto3_raw_data: "type_defs.MetricDefinitionTypeDef" = dataclasses.field()

    name = field("name")
    regex = field("regex")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricDefinitionTypeDef"]
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
class InferenceContainerConfig:
    boto3_raw_data: "type_defs.InferenceContainerConfigTypeDef" = dataclasses.field()

    imageUri = field("imageUri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferenceContainerConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferenceContainerConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IncrementalTrainingDataChannel:
    boto3_raw_data: "type_defs.IncrementalTrainingDataChannelTypeDef" = (
        dataclasses.field()
    )

    trainedModelArn = field("trainedModelArn")
    channelName = field("channelName")
    versionIdentifier = field("versionIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IncrementalTrainingDataChannelTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IncrementalTrainingDataChannelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelTrainingDataChannel:
    boto3_raw_data: "type_defs.ModelTrainingDataChannelTypeDef" = dataclasses.field()

    mlInputChannelArn = field("mlInputChannelArn")
    channelName = field("channelName")
    s3DataDistributionType = field("s3DataDistributionType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModelTrainingDataChannelTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelTrainingDataChannelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceConfig:
    boto3_raw_data: "type_defs.ResourceConfigTypeDef" = dataclasses.field()

    instanceType = field("instanceType")
    volumeSizeInGB = field("volumeSizeInGB")
    instanceCount = field("instanceCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StoppingCondition:
    boto3_raw_data: "type_defs.StoppingConditionTypeDef" = dataclasses.field()

    maxRuntimeInSeconds = field("maxRuntimeInSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StoppingConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StoppingConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomEntityConfigOutput:
    boto3_raw_data: "type_defs.CustomEntityConfigOutputTypeDef" = dataclasses.field()

    customDataIdentifiers = field("customDataIdentifiers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomEntityConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomEntityConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomEntityConfig:
    boto3_raw_data: "type_defs.CustomEntityConfigTypeDef" = dataclasses.field()

    customDataIdentifiers = field("customDataIdentifiers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomEntityConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomEntityConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlueDataSource:
    boto3_raw_data: "type_defs.GlueDataSourceTypeDef" = dataclasses.field()

    tableName = field("tableName")
    databaseName = field("databaseName")
    catalogId = field("catalogId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GlueDataSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GlueDataSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAudienceGenerationJobRequest:
    boto3_raw_data: "type_defs.DeleteAudienceGenerationJobRequestTypeDef" = (
        dataclasses.field()
    )

    audienceGenerationJobArn = field("audienceGenerationJobArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAudienceGenerationJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAudienceGenerationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAudienceModelRequest:
    boto3_raw_data: "type_defs.DeleteAudienceModelRequestTypeDef" = dataclasses.field()

    audienceModelArn = field("audienceModelArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAudienceModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAudienceModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfiguredAudienceModelPolicyRequest:
    boto3_raw_data: "type_defs.DeleteConfiguredAudienceModelPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    configuredAudienceModelArn = field("configuredAudienceModelArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteConfiguredAudienceModelPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfiguredAudienceModelPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfiguredAudienceModelRequest:
    boto3_raw_data: "type_defs.DeleteConfiguredAudienceModelRequestTypeDef" = (
        dataclasses.field()
    )

    configuredAudienceModelArn = field("configuredAudienceModelArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteConfiguredAudienceModelRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfiguredAudienceModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfiguredModelAlgorithmAssociationRequest:
    boto3_raw_data: (
        "type_defs.DeleteConfiguredModelAlgorithmAssociationRequestTypeDef"
    ) = dataclasses.field()

    configuredModelAlgorithmAssociationArn = field(
        "configuredModelAlgorithmAssociationArn"
    )
    membershipIdentifier = field("membershipIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteConfiguredModelAlgorithmAssociationRequestTypeDef"
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
                "type_defs.DeleteConfiguredModelAlgorithmAssociationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfiguredModelAlgorithmRequest:
    boto3_raw_data: "type_defs.DeleteConfiguredModelAlgorithmRequestTypeDef" = (
        dataclasses.field()
    )

    configuredModelAlgorithmArn = field("configuredModelAlgorithmArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteConfiguredModelAlgorithmRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfiguredModelAlgorithmRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMLConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteMLConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMLConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMLConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMLInputChannelDataRequest:
    boto3_raw_data: "type_defs.DeleteMLInputChannelDataRequestTypeDef" = (
        dataclasses.field()
    )

    mlInputChannelArn = field("mlInputChannelArn")
    membershipIdentifier = field("membershipIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteMLInputChannelDataRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMLInputChannelDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTrainedModelOutputRequest:
    boto3_raw_data: "type_defs.DeleteTrainedModelOutputRequestTypeDef" = (
        dataclasses.field()
    )

    trainedModelArn = field("trainedModelArn")
    membershipIdentifier = field("membershipIdentifier")
    versionIdentifier = field("versionIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteTrainedModelOutputRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTrainedModelOutputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTrainingDatasetRequest:
    boto3_raw_data: "type_defs.DeleteTrainingDatasetRequestTypeDef" = (
        dataclasses.field()
    )

    trainingDatasetArn = field("trainingDatasetArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTrainingDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTrainingDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAudienceGenerationJobRequest:
    boto3_raw_data: "type_defs.GetAudienceGenerationJobRequestTypeDef" = (
        dataclasses.field()
    )

    audienceGenerationJobArn = field("audienceGenerationJobArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAudienceGenerationJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAudienceGenerationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAudienceModelRequest:
    boto3_raw_data: "type_defs.GetAudienceModelRequestTypeDef" = dataclasses.field()

    audienceModelArn = field("audienceModelArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAudienceModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAudienceModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCollaborationConfiguredModelAlgorithmAssociationRequest:
    boto3_raw_data: (
        "type_defs.GetCollaborationConfiguredModelAlgorithmAssociationRequestTypeDef"
    ) = dataclasses.field()

    configuredModelAlgorithmAssociationArn = field(
        "configuredModelAlgorithmAssociationArn"
    )
    collaborationIdentifier = field("collaborationIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCollaborationConfiguredModelAlgorithmAssociationRequestTypeDef"
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
                "type_defs.GetCollaborationConfiguredModelAlgorithmAssociationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCollaborationMLInputChannelRequest:
    boto3_raw_data: "type_defs.GetCollaborationMLInputChannelRequestTypeDef" = (
        dataclasses.field()
    )

    mlInputChannelArn = field("mlInputChannelArn")
    collaborationIdentifier = field("collaborationIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCollaborationMLInputChannelRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCollaborationMLInputChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCollaborationTrainedModelRequest:
    boto3_raw_data: "type_defs.GetCollaborationTrainedModelRequestTypeDef" = (
        dataclasses.field()
    )

    trainedModelArn = field("trainedModelArn")
    collaborationIdentifier = field("collaborationIdentifier")
    versionIdentifier = field("versionIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCollaborationTrainedModelRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCollaborationTrainedModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfiguredAudienceModelPolicyRequest:
    boto3_raw_data: "type_defs.GetConfiguredAudienceModelPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    configuredAudienceModelArn = field("configuredAudienceModelArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConfiguredAudienceModelPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfiguredAudienceModelPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfiguredAudienceModelRequest:
    boto3_raw_data: "type_defs.GetConfiguredAudienceModelRequestTypeDef" = (
        dataclasses.field()
    )

    configuredAudienceModelArn = field("configuredAudienceModelArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConfiguredAudienceModelRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfiguredAudienceModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfiguredModelAlgorithmAssociationRequest:
    boto3_raw_data: "type_defs.GetConfiguredModelAlgorithmAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    configuredModelAlgorithmAssociationArn = field(
        "configuredModelAlgorithmAssociationArn"
    )
    membershipIdentifier = field("membershipIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConfiguredModelAlgorithmAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfiguredModelAlgorithmAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfiguredModelAlgorithmRequest:
    boto3_raw_data: "type_defs.GetConfiguredModelAlgorithmRequestTypeDef" = (
        dataclasses.field()
    )

    configuredModelAlgorithmArn = field("configuredModelAlgorithmArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConfiguredModelAlgorithmRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfiguredModelAlgorithmRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMLConfigurationRequest:
    boto3_raw_data: "type_defs.GetMLConfigurationRequestTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMLConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMLConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMLInputChannelRequest:
    boto3_raw_data: "type_defs.GetMLInputChannelRequestTypeDef" = dataclasses.field()

    mlInputChannelArn = field("mlInputChannelArn")
    membershipIdentifier = field("membershipIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMLInputChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMLInputChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrainedModelInferenceJobRequest:
    boto3_raw_data: "type_defs.GetTrainedModelInferenceJobRequestTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")
    trainedModelInferenceJobArn = field("trainedModelInferenceJobArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTrainedModelInferenceJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrainedModelInferenceJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferenceContainerExecutionParameters:
    boto3_raw_data: "type_defs.InferenceContainerExecutionParametersTypeDef" = (
        dataclasses.field()
    )

    maxPayloadInMB = field("maxPayloadInMB")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InferenceContainerExecutionParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferenceContainerExecutionParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferenceResourceConfig:
    boto3_raw_data: "type_defs.InferenceResourceConfigTypeDef" = dataclasses.field()

    instanceType = field("instanceType")
    instanceCount = field("instanceCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferenceResourceConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferenceResourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelInferenceDataSource:
    boto3_raw_data: "type_defs.ModelInferenceDataSourceTypeDef" = dataclasses.field()

    mlInputChannelArn = field("mlInputChannelArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModelInferenceDataSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelInferenceDataSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrainedModelRequest:
    boto3_raw_data: "type_defs.GetTrainedModelRequestTypeDef" = dataclasses.field()

    trainedModelArn = field("trainedModelArn")
    membershipIdentifier = field("membershipIdentifier")
    versionIdentifier = field("versionIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTrainedModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrainedModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrainingDatasetRequest:
    boto3_raw_data: "type_defs.GetTrainingDatasetRequestTypeDef" = dataclasses.field()

    trainingDatasetArn = field("trainingDatasetArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTrainingDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrainingDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferenceReceiverMember:
    boto3_raw_data: "type_defs.InferenceReceiverMemberTypeDef" = dataclasses.field()

    accountId = field("accountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferenceReceiverMemberTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferenceReceiverMemberTypeDef"]
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
class ListAudienceExportJobsRequest:
    boto3_raw_data: "type_defs.ListAudienceExportJobsRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    audienceGenerationJobArn = field("audienceGenerationJobArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAudienceExportJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAudienceExportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAudienceGenerationJobsRequest:
    boto3_raw_data: "type_defs.ListAudienceGenerationJobsRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    configuredAudienceModelArn = field("configuredAudienceModelArn")
    collaborationId = field("collaborationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAudienceGenerationJobsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAudienceGenerationJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAudienceModelsRequest:
    boto3_raw_data: "type_defs.ListAudienceModelsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAudienceModelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAudienceModelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationConfiguredModelAlgorithmAssociationsRequest:
    boto3_raw_data: (
        "type_defs.ListCollaborationConfiguredModelAlgorithmAssociationsRequestTypeDef"
    ) = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationConfiguredModelAlgorithmAssociationsRequestTypeDef"
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
                "type_defs.ListCollaborationConfiguredModelAlgorithmAssociationsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationMLInputChannelsRequest:
    boto3_raw_data: "type_defs.ListCollaborationMLInputChannelsRequestTypeDef" = (
        dataclasses.field()
    )

    collaborationIdentifier = field("collaborationIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationMLInputChannelsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollaborationMLInputChannelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationTrainedModelExportJobsRequest:
    boto3_raw_data: (
        "type_defs.ListCollaborationTrainedModelExportJobsRequestTypeDef"
    ) = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")
    trainedModelArn = field("trainedModelArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    trainedModelVersionIdentifier = field("trainedModelVersionIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationTrainedModelExportJobsRequestTypeDef"
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
                "type_defs.ListCollaborationTrainedModelExportJobsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationTrainedModelInferenceJobsRequest:
    boto3_raw_data: (
        "type_defs.ListCollaborationTrainedModelInferenceJobsRequestTypeDef"
    ) = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    trainedModelArn = field("trainedModelArn")
    trainedModelVersionIdentifier = field("trainedModelVersionIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationTrainedModelInferenceJobsRequestTypeDef"
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
                "type_defs.ListCollaborationTrainedModelInferenceJobsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationTrainedModelsRequest:
    boto3_raw_data: "type_defs.ListCollaborationTrainedModelsRequestTypeDef" = (
        dataclasses.field()
    )

    collaborationIdentifier = field("collaborationIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationTrainedModelsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollaborationTrainedModelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfiguredAudienceModelsRequest:
    boto3_raw_data: "type_defs.ListConfiguredAudienceModelsRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfiguredAudienceModelsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfiguredAudienceModelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfiguredModelAlgorithmAssociationsRequest:
    boto3_raw_data: (
        "type_defs.ListConfiguredModelAlgorithmAssociationsRequestTypeDef"
    ) = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfiguredModelAlgorithmAssociationsRequestTypeDef"
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
                "type_defs.ListConfiguredModelAlgorithmAssociationsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfiguredModelAlgorithmsRequest:
    boto3_raw_data: "type_defs.ListConfiguredModelAlgorithmsRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfiguredModelAlgorithmsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfiguredModelAlgorithmsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMLInputChannelsRequest:
    boto3_raw_data: "type_defs.ListMLInputChannelsRequestTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMLInputChannelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMLInputChannelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MLInputChannelSummary:
    boto3_raw_data: "type_defs.MLInputChannelSummaryTypeDef" = dataclasses.field()

    createTime = field("createTime")
    updateTime = field("updateTime")
    membershipIdentifier = field("membershipIdentifier")
    collaborationIdentifier = field("collaborationIdentifier")
    name = field("name")
    configuredModelAlgorithmAssociations = field("configuredModelAlgorithmAssociations")
    mlInputChannelArn = field("mlInputChannelArn")
    status = field("status")
    protectedQueryIdentifier = field("protectedQueryIdentifier")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MLInputChannelSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MLInputChannelSummaryTypeDef"]
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
class ListTrainedModelInferenceJobsRequest:
    boto3_raw_data: "type_defs.ListTrainedModelInferenceJobsRequestTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    trainedModelArn = field("trainedModelArn")
    trainedModelVersionIdentifier = field("trainedModelVersionIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrainedModelInferenceJobsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrainedModelInferenceJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrainedModelVersionsRequest:
    boto3_raw_data: "type_defs.ListTrainedModelVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")
    trainedModelArn = field("trainedModelArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTrainedModelVersionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrainedModelVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrainedModelsRequest:
    boto3_raw_data: "type_defs.ListTrainedModelsRequestTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTrainedModelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrainedModelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrainingDatasetsRequest:
    boto3_raw_data: "type_defs.ListTrainingDatasetsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTrainingDatasetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrainingDatasetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainingDatasetSummary:
    boto3_raw_data: "type_defs.TrainingDatasetSummaryTypeDef" = dataclasses.field()

    createTime = field("createTime")
    updateTime = field("updateTime")
    trainingDatasetArn = field("trainingDatasetArn")
    name = field("name")
    status = field("status")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrainingDatasetSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainingDatasetSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricsConfigurationPolicy:
    boto3_raw_data: "type_defs.MetricsConfigurationPolicyTypeDef" = dataclasses.field()

    noiseLevel = field("noiseLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricsConfigurationPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricsConfigurationPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutConfiguredAudienceModelPolicyRequest:
    boto3_raw_data: "type_defs.PutConfiguredAudienceModelPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    configuredAudienceModelArn = field("configuredAudienceModelArn")
    configuredAudienceModelPolicy = field("configuredAudienceModelPolicy")
    previousPolicyHash = field("previousPolicyHash")
    policyExistenceCondition = field("policyExistenceCondition")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutConfiguredAudienceModelPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutConfiguredAudienceModelPolicyRequestTypeDef"]
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
    tags = field("tags")

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
class TrainedModelArtifactMaxSize:
    boto3_raw_data: "type_defs.TrainedModelArtifactMaxSizeTypeDef" = dataclasses.field()

    unit = field("unit")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrainedModelArtifactMaxSizeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainedModelArtifactMaxSizeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainedModelExportReceiverMember:
    boto3_raw_data: "type_defs.TrainedModelExportReceiverMemberTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TrainedModelExportReceiverMemberTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainedModelExportReceiverMemberTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainedModelExportsMaxSize:
    boto3_raw_data: "type_defs.TrainedModelExportsMaxSizeTypeDef" = dataclasses.field()

    unit = field("unit")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrainedModelExportsMaxSizeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainedModelExportsMaxSizeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainedModelInferenceMaxOutputSize:
    boto3_raw_data: "type_defs.TrainedModelInferenceMaxOutputSizeTypeDef" = (
        dataclasses.field()
    )

    unit = field("unit")
    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TrainedModelInferenceMaxOutputSizeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainedModelInferenceMaxOutputSizeTypeDef"]
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
class AudienceDestination:
    boto3_raw_data: "type_defs.AudienceDestinationTypeDef" = dataclasses.field()

    @cached_property
    def s3Destination(self):  # pragma: no cover
        return S3ConfigMap.make_one(self.boto3_raw_data["s3Destination"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudienceDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudienceDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Destination:
    boto3_raw_data: "type_defs.DestinationTypeDef" = dataclasses.field()

    @cached_property
    def s3Destination(self):  # pragma: no cover
        return S3ConfigMap.make_one(self.boto3_raw_data["s3Destination"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DestinationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelevanceMetric:
    boto3_raw_data: "type_defs.RelevanceMetricTypeDef" = dataclasses.field()

    @cached_property
    def audienceSize(self):  # pragma: no cover
        return AudienceSize.make_one(self.boto3_raw_data["audienceSize"])

    score = field("score")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RelevanceMetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RelevanceMetricTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAudienceExportJobRequest:
    boto3_raw_data: "type_defs.StartAudienceExportJobRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    audienceGenerationJobArn = field("audienceGenerationJobArn")

    @cached_property
    def audienceSize(self):  # pragma: no cover
        return AudienceSize.make_one(self.boto3_raw_data["audienceSize"])

    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartAudienceExportJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAudienceExportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudienceExportJobSummary:
    boto3_raw_data: "type_defs.AudienceExportJobSummaryTypeDef" = dataclasses.field()

    createTime = field("createTime")
    updateTime = field("updateTime")
    name = field("name")
    audienceGenerationJobArn = field("audienceGenerationJobArn")

    @cached_property
    def audienceSize(self):  # pragma: no cover
        return AudienceSize.make_one(self.boto3_raw_data["audienceSize"])

    status = field("status")
    description = field("description")

    @cached_property
    def statusDetails(self):  # pragma: no cover
        return StatusDetails.make_one(self.boto3_raw_data["statusDetails"])

    outputLocation = field("outputLocation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudienceExportJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudienceExportJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollaborationTrainedModelSummary:
    boto3_raw_data: "type_defs.CollaborationTrainedModelSummaryTypeDef" = (
        dataclasses.field()
    )

    createTime = field("createTime")
    updateTime = field("updateTime")
    trainedModelArn = field("trainedModelArn")
    name = field("name")
    membershipIdentifier = field("membershipIdentifier")
    collaborationIdentifier = field("collaborationIdentifier")
    status = field("status")
    configuredModelAlgorithmAssociationArn = field(
        "configuredModelAlgorithmAssociationArn"
    )
    creatorAccountId = field("creatorAccountId")
    versionIdentifier = field("versionIdentifier")

    @cached_property
    def incrementalTrainingDataChannels(self):  # pragma: no cover
        return IncrementalTrainingDataChannelOutput.make_many(
            self.boto3_raw_data["incrementalTrainingDataChannels"]
        )

    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CollaborationTrainedModelSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollaborationTrainedModelSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainedModelSummary:
    boto3_raw_data: "type_defs.TrainedModelSummaryTypeDef" = dataclasses.field()

    createTime = field("createTime")
    updateTime = field("updateTime")
    trainedModelArn = field("trainedModelArn")
    name = field("name")
    membershipIdentifier = field("membershipIdentifier")
    collaborationIdentifier = field("collaborationIdentifier")
    status = field("status")
    configuredModelAlgorithmAssociationArn = field(
        "configuredModelAlgorithmAssociationArn"
    )
    versionIdentifier = field("versionIdentifier")

    @cached_property
    def incrementalTrainingDataChannels(self):  # pragma: no cover
        return IncrementalTrainingDataChannelOutput.make_many(
            self.boto3_raw_data["incrementalTrainingDataChannels"]
        )

    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrainedModelSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainedModelSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeConfiguration:
    boto3_raw_data: "type_defs.ComputeConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def worker(self):  # pragma: no cover
        return WorkerComputeConfiguration.make_one(self.boto3_raw_data["worker"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComputeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerConfigOutput:
    boto3_raw_data: "type_defs.ContainerConfigOutputTypeDef" = dataclasses.field()

    imageUri = field("imageUri")
    entrypoint = field("entrypoint")
    arguments = field("arguments")

    @cached_property
    def metricDefinitions(self):  # pragma: no cover
        return MetricDefinition.make_many(self.boto3_raw_data["metricDefinitions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerConfig:
    boto3_raw_data: "type_defs.ContainerConfigTypeDef" = dataclasses.field()

    imageUri = field("imageUri")
    entrypoint = field("entrypoint")
    arguments = field("arguments")

    @cached_property
    def metricDefinitions(self):  # pragma: no cover
        return MetricDefinition.make_many(self.boto3_raw_data["metricDefinitions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContainerConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContainerConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAudienceModelRequest:
    boto3_raw_data: "type_defs.CreateAudienceModelRequestTypeDef" = dataclasses.field()

    name = field("name")
    trainingDatasetArn = field("trainingDatasetArn")
    trainingDataStartTime = field("trainingDataStartTime")
    trainingDataEndTime = field("trainingDataEndTime")
    kmsKeyArn = field("kmsKeyArn")
    tags = field("tags")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAudienceModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAudienceModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAudienceModelResponse:
    boto3_raw_data: "type_defs.CreateAudienceModelResponseTypeDef" = dataclasses.field()

    audienceModelArn = field("audienceModelArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAudienceModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAudienceModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfiguredAudienceModelResponse:
    boto3_raw_data: "type_defs.CreateConfiguredAudienceModelResponseTypeDef" = (
        dataclasses.field()
    )

    configuredAudienceModelArn = field("configuredAudienceModelArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConfiguredAudienceModelResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfiguredAudienceModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfiguredModelAlgorithmAssociationResponse:
    boto3_raw_data: (
        "type_defs.CreateConfiguredModelAlgorithmAssociationResponseTypeDef"
    ) = dataclasses.field()

    configuredModelAlgorithmAssociationArn = field(
        "configuredModelAlgorithmAssociationArn"
    )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConfiguredModelAlgorithmAssociationResponseTypeDef"
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
                "type_defs.CreateConfiguredModelAlgorithmAssociationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfiguredModelAlgorithmResponse:
    boto3_raw_data: "type_defs.CreateConfiguredModelAlgorithmResponseTypeDef" = (
        dataclasses.field()
    )

    configuredModelAlgorithmArn = field("configuredModelAlgorithmArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConfiguredModelAlgorithmResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfiguredModelAlgorithmResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMLInputChannelResponse:
    boto3_raw_data: "type_defs.CreateMLInputChannelResponseTypeDef" = (
        dataclasses.field()
    )

    mlInputChannelArn = field("mlInputChannelArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMLInputChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMLInputChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrainedModelResponse:
    boto3_raw_data: "type_defs.CreateTrainedModelResponseTypeDef" = dataclasses.field()

    trainedModelArn = field("trainedModelArn")
    versionIdentifier = field("versionIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTrainedModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrainedModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrainingDatasetResponse:
    boto3_raw_data: "type_defs.CreateTrainingDatasetResponseTypeDef" = (
        dataclasses.field()
    )

    trainingDatasetArn = field("trainingDatasetArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateTrainingDatasetResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrainingDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAudienceModelResponse:
    boto3_raw_data: "type_defs.GetAudienceModelResponseTypeDef" = dataclasses.field()

    createTime = field("createTime")
    updateTime = field("updateTime")
    trainingDataStartTime = field("trainingDataStartTime")
    trainingDataEndTime = field("trainingDataEndTime")
    audienceModelArn = field("audienceModelArn")
    name = field("name")
    trainingDatasetArn = field("trainingDatasetArn")
    status = field("status")

    @cached_property
    def statusDetails(self):  # pragma: no cover
        return StatusDetails.make_one(self.boto3_raw_data["statusDetails"])

    kmsKeyArn = field("kmsKeyArn")
    tags = field("tags")
    description = field("description")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAudienceModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAudienceModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCollaborationMLInputChannelResponse:
    boto3_raw_data: "type_defs.GetCollaborationMLInputChannelResponseTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")
    collaborationIdentifier = field("collaborationIdentifier")
    mlInputChannelArn = field("mlInputChannelArn")
    name = field("name")
    configuredModelAlgorithmAssociations = field("configuredModelAlgorithmAssociations")
    status = field("status")

    @cached_property
    def statusDetails(self):  # pragma: no cover
        return StatusDetails.make_one(self.boto3_raw_data["statusDetails"])

    retentionInDays = field("retentionInDays")
    numberOfRecords = field("numberOfRecords")
    description = field("description")
    createTime = field("createTime")
    updateTime = field("updateTime")
    creatorAccountId = field("creatorAccountId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCollaborationMLInputChannelResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCollaborationMLInputChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfiguredAudienceModelPolicyResponse:
    boto3_raw_data: "type_defs.GetConfiguredAudienceModelPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    configuredAudienceModelArn = field("configuredAudienceModelArn")
    configuredAudienceModelPolicy = field("configuredAudienceModelPolicy")
    policyHash = field("policyHash")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConfiguredAudienceModelPolicyResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfiguredAudienceModelPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAudienceGenerationJobsResponse:
    boto3_raw_data: "type_defs.ListAudienceGenerationJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def audienceGenerationJobs(self):  # pragma: no cover
        return AudienceGenerationJobSummary.make_many(
            self.boto3_raw_data["audienceGenerationJobs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAudienceGenerationJobsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAudienceGenerationJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAudienceModelsResponse:
    boto3_raw_data: "type_defs.ListAudienceModelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def audienceModels(self):  # pragma: no cover
        return AudienceModelSummary.make_many(self.boto3_raw_data["audienceModels"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAudienceModelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAudienceModelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationConfiguredModelAlgorithmAssociationsResponse:
    boto3_raw_data: (
        "type_defs.ListCollaborationConfiguredModelAlgorithmAssociationsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def collaborationConfiguredModelAlgorithmAssociations(self):  # pragma: no cover
        return CollaborationConfiguredModelAlgorithmAssociationSummary.make_many(
            self.boto3_raw_data["collaborationConfiguredModelAlgorithmAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationConfiguredModelAlgorithmAssociationsResponseTypeDef"
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
                "type_defs.ListCollaborationConfiguredModelAlgorithmAssociationsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationMLInputChannelsResponse:
    boto3_raw_data: "type_defs.ListCollaborationMLInputChannelsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def collaborationMLInputChannelsList(self):  # pragma: no cover
        return CollaborationMLInputChannelSummary.make_many(
            self.boto3_raw_data["collaborationMLInputChannelsList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationMLInputChannelsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollaborationMLInputChannelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfiguredModelAlgorithmAssociationsResponse:
    boto3_raw_data: (
        "type_defs.ListConfiguredModelAlgorithmAssociationsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def configuredModelAlgorithmAssociations(self):  # pragma: no cover
        return ConfiguredModelAlgorithmAssociationSummary.make_many(
            self.boto3_raw_data["configuredModelAlgorithmAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfiguredModelAlgorithmAssociationsResponseTypeDef"
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
                "type_defs.ListConfiguredModelAlgorithmAssociationsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfiguredModelAlgorithmsResponse:
    boto3_raw_data: "type_defs.ListConfiguredModelAlgorithmsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configuredModelAlgorithms(self):  # pragma: no cover
        return ConfiguredModelAlgorithmSummary.make_many(
            self.boto3_raw_data["configuredModelAlgorithms"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfiguredModelAlgorithmsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfiguredModelAlgorithmsResponseTypeDef"]
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

    tags = field("tags")

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
class PutConfiguredAudienceModelPolicyResponse:
    boto3_raw_data: "type_defs.PutConfiguredAudienceModelPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    configuredAudienceModelPolicy = field("configuredAudienceModelPolicy")
    policyHash = field("policyHash")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutConfiguredAudienceModelPolicyResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutConfiguredAudienceModelPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAudienceGenerationJobResponse:
    boto3_raw_data: "type_defs.StartAudienceGenerationJobResponseTypeDef" = (
        dataclasses.field()
    )

    audienceGenerationJobArn = field("audienceGenerationJobArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartAudienceGenerationJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAudienceGenerationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTrainedModelInferenceJobResponse:
    boto3_raw_data: "type_defs.StartTrainedModelInferenceJobResponseTypeDef" = (
        dataclasses.field()
    )

    trainedModelInferenceJobArn = field("trainedModelInferenceJobArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartTrainedModelInferenceJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTrainedModelInferenceJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfiguredAudienceModelResponse:
    boto3_raw_data: "type_defs.UpdateConfiguredAudienceModelResponseTypeDef" = (
        dataclasses.field()
    )

    configuredAudienceModelArn = field("configuredAudienceModelArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConfiguredAudienceModelResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConfiguredAudienceModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrainedModelRequest:
    boto3_raw_data: "type_defs.CreateTrainedModelRequestTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    name = field("name")
    configuredModelAlgorithmAssociationArn = field(
        "configuredModelAlgorithmAssociationArn"
    )

    @cached_property
    def resourceConfig(self):  # pragma: no cover
        return ResourceConfig.make_one(self.boto3_raw_data["resourceConfig"])

    @cached_property
    def dataChannels(self):  # pragma: no cover
        return ModelTrainingDataChannel.make_many(self.boto3_raw_data["dataChannels"])

    hyperparameters = field("hyperparameters")
    environment = field("environment")

    @cached_property
    def stoppingCondition(self):  # pragma: no cover
        return StoppingCondition.make_one(self.boto3_raw_data["stoppingCondition"])

    @cached_property
    def incrementalTrainingDataChannels(self):  # pragma: no cover
        return IncrementalTrainingDataChannel.make_many(
            self.boto3_raw_data["incrementalTrainingDataChannels"]
        )

    trainingInputMode = field("trainingInputMode")
    description = field("description")
    kmsKeyArn = field("kmsKeyArn")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTrainedModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrainedModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCollaborationTrainedModelResponse:
    boto3_raw_data: "type_defs.GetCollaborationTrainedModelResponseTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")
    collaborationIdentifier = field("collaborationIdentifier")
    trainedModelArn = field("trainedModelArn")
    versionIdentifier = field("versionIdentifier")

    @cached_property
    def incrementalTrainingDataChannels(self):  # pragma: no cover
        return IncrementalTrainingDataChannelOutput.make_many(
            self.boto3_raw_data["incrementalTrainingDataChannels"]
        )

    name = field("name")
    description = field("description")
    status = field("status")

    @cached_property
    def statusDetails(self):  # pragma: no cover
        return StatusDetails.make_one(self.boto3_raw_data["statusDetails"])

    configuredModelAlgorithmAssociationArn = field(
        "configuredModelAlgorithmAssociationArn"
    )

    @cached_property
    def resourceConfig(self):  # pragma: no cover
        return ResourceConfig.make_one(self.boto3_raw_data["resourceConfig"])

    trainingInputMode = field("trainingInputMode")

    @cached_property
    def stoppingCondition(self):  # pragma: no cover
        return StoppingCondition.make_one(self.boto3_raw_data["stoppingCondition"])

    metricsStatus = field("metricsStatus")
    metricsStatusDetails = field("metricsStatusDetails")
    logsStatus = field("logsStatus")
    logsStatusDetails = field("logsStatusDetails")
    trainingContainerImageDigest = field("trainingContainerImageDigest")
    createTime = field("createTime")
    updateTime = field("updateTime")
    creatorAccountId = field("creatorAccountId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCollaborationTrainedModelResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCollaborationTrainedModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrainedModelResponse:
    boto3_raw_data: "type_defs.GetTrainedModelResponseTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    collaborationIdentifier = field("collaborationIdentifier")
    trainedModelArn = field("trainedModelArn")
    versionIdentifier = field("versionIdentifier")

    @cached_property
    def incrementalTrainingDataChannels(self):  # pragma: no cover
        return IncrementalTrainingDataChannelOutput.make_many(
            self.boto3_raw_data["incrementalTrainingDataChannels"]
        )

    name = field("name")
    description = field("description")
    status = field("status")

    @cached_property
    def statusDetails(self):  # pragma: no cover
        return StatusDetails.make_one(self.boto3_raw_data["statusDetails"])

    configuredModelAlgorithmAssociationArn = field(
        "configuredModelAlgorithmAssociationArn"
    )

    @cached_property
    def resourceConfig(self):  # pragma: no cover
        return ResourceConfig.make_one(self.boto3_raw_data["resourceConfig"])

    trainingInputMode = field("trainingInputMode")

    @cached_property
    def stoppingCondition(self):  # pragma: no cover
        return StoppingCondition.make_one(self.boto3_raw_data["stoppingCondition"])

    metricsStatus = field("metricsStatus")
    metricsStatusDetails = field("metricsStatusDetails")
    logsStatus = field("logsStatus")
    logsStatusDetails = field("logsStatusDetails")
    trainingContainerImageDigest = field("trainingContainerImageDigest")
    createTime = field("createTime")
    updateTime = field("updateTime")
    hyperparameters = field("hyperparameters")
    environment = field("environment")
    kmsKeyArn = field("kmsKeyArn")
    tags = field("tags")

    @cached_property
    def dataChannels(self):  # pragma: no cover
        return ModelTrainingDataChannel.make_many(self.boto3_raw_data["dataChannels"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTrainedModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrainedModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogRedactionConfigurationOutput:
    boto3_raw_data: "type_defs.LogRedactionConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    entitiesToRedact = field("entitiesToRedact")

    @cached_property
    def customEntityConfig(self):  # pragma: no cover
        return CustomEntityConfigOutput.make_one(
            self.boto3_raw_data["customEntityConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LogRedactionConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogRedactionConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogRedactionConfiguration:
    boto3_raw_data: "type_defs.LogRedactionConfigurationTypeDef" = dataclasses.field()

    entitiesToRedact = field("entitiesToRedact")

    @cached_property
    def customEntityConfig(self):  # pragma: no cover
        return CustomEntityConfig.make_one(self.boto3_raw_data["customEntityConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LogRedactionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogRedactionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSource:
    boto3_raw_data: "type_defs.DataSourceTypeDef" = dataclasses.field()

    @cached_property
    def glueDataSource(self):  # pragma: no cover
        return GlueDataSource.make_one(self.boto3_raw_data["glueDataSource"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferenceOutputConfigurationOutput:
    boto3_raw_data: "type_defs.InferenceOutputConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def members(self):  # pragma: no cover
        return InferenceReceiverMember.make_many(self.boto3_raw_data["members"])

    accept = field("accept")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InferenceOutputConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferenceOutputConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferenceOutputConfiguration:
    boto3_raw_data: "type_defs.InferenceOutputConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def members(self):  # pragma: no cover
        return InferenceReceiverMember.make_many(self.boto3_raw_data["members"])

    accept = field("accept")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferenceOutputConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferenceOutputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAudienceExportJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListAudienceExportJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    audienceGenerationJobArn = field("audienceGenerationJobArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAudienceExportJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAudienceExportJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAudienceGenerationJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListAudienceGenerationJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    configuredAudienceModelArn = field("configuredAudienceModelArn")
    collaborationId = field("collaborationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAudienceGenerationJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAudienceGenerationJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAudienceModelsRequestPaginate:
    boto3_raw_data: "type_defs.ListAudienceModelsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAudienceModelsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAudienceModelsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationConfiguredModelAlgorithmAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.ListCollaborationConfiguredModelAlgorithmAssociationsRequestPaginateTypeDef" = (dataclasses.field())

    collaborationIdentifier = field("collaborationIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationConfiguredModelAlgorithmAssociationsRequestPaginateTypeDef"
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
                "type_defs.ListCollaborationConfiguredModelAlgorithmAssociationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationMLInputChannelsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListCollaborationMLInputChannelsRequestPaginateTypeDef"
    ) = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationMLInputChannelsRequestPaginateTypeDef"
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
                "type_defs.ListCollaborationMLInputChannelsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationTrainedModelExportJobsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListCollaborationTrainedModelExportJobsRequestPaginateTypeDef"
    ) = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")
    trainedModelArn = field("trainedModelArn")
    trainedModelVersionIdentifier = field("trainedModelVersionIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationTrainedModelExportJobsRequestPaginateTypeDef"
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
                "type_defs.ListCollaborationTrainedModelExportJobsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationTrainedModelInferenceJobsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListCollaborationTrainedModelInferenceJobsRequestPaginateTypeDef"
    ) = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")
    trainedModelArn = field("trainedModelArn")
    trainedModelVersionIdentifier = field("trainedModelVersionIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationTrainedModelInferenceJobsRequestPaginateTypeDef"
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
                "type_defs.ListCollaborationTrainedModelInferenceJobsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationTrainedModelsRequestPaginate:
    boto3_raw_data: "type_defs.ListCollaborationTrainedModelsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    collaborationIdentifier = field("collaborationIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationTrainedModelsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollaborationTrainedModelsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfiguredAudienceModelsRequestPaginate:
    boto3_raw_data: "type_defs.ListConfiguredAudienceModelsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfiguredAudienceModelsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfiguredAudienceModelsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfiguredModelAlgorithmAssociationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListConfiguredModelAlgorithmAssociationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfiguredModelAlgorithmAssociationsRequestPaginateTypeDef"
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
                "type_defs.ListConfiguredModelAlgorithmAssociationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfiguredModelAlgorithmsRequestPaginate:
    boto3_raw_data: "type_defs.ListConfiguredModelAlgorithmsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfiguredModelAlgorithmsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfiguredModelAlgorithmsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMLInputChannelsRequestPaginate:
    boto3_raw_data: "type_defs.ListMLInputChannelsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMLInputChannelsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMLInputChannelsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrainedModelInferenceJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListTrainedModelInferenceJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")
    trainedModelArn = field("trainedModelArn")
    trainedModelVersionIdentifier = field("trainedModelVersionIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrainedModelInferenceJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrainedModelInferenceJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrainedModelVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListTrainedModelVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")
    trainedModelArn = field("trainedModelArn")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrainedModelVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrainedModelVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrainedModelsRequestPaginate:
    boto3_raw_data: "type_defs.ListTrainedModelsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTrainedModelsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrainedModelsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrainingDatasetsRequestPaginate:
    boto3_raw_data: "type_defs.ListTrainingDatasetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrainingDatasetsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrainingDatasetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMLInputChannelsResponse:
    boto3_raw_data: "type_defs.ListMLInputChannelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def mlInputChannelsList(self):  # pragma: no cover
        return MLInputChannelSummary.make_many(
            self.boto3_raw_data["mlInputChannelsList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMLInputChannelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMLInputChannelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrainingDatasetsResponse:
    boto3_raw_data: "type_defs.ListTrainingDatasetsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def trainingDatasets(self):  # pragma: no cover
        return TrainingDatasetSummary.make_many(self.boto3_raw_data["trainingDatasets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTrainingDatasetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrainingDatasetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainedModelExportOutputConfigurationOutput:
    boto3_raw_data: "type_defs.TrainedModelExportOutputConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def members(self):  # pragma: no cover
        return TrainedModelExportReceiverMember.make_many(
            self.boto3_raw_data["members"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TrainedModelExportOutputConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainedModelExportOutputConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainedModelExportOutputConfiguration:
    boto3_raw_data: "type_defs.TrainedModelExportOutputConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def members(self):  # pragma: no cover
        return TrainedModelExportReceiverMember.make_many(
            self.boto3_raw_data["members"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TrainedModelExportOutputConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainedModelExportOutputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainedModelExportsConfigurationPolicyOutput:
    boto3_raw_data: "type_defs.TrainedModelExportsConfigurationPolicyOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def maxSize(self):  # pragma: no cover
        return TrainedModelExportsMaxSize.make_one(self.boto3_raw_data["maxSize"])

    filesToExport = field("filesToExport")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TrainedModelExportsConfigurationPolicyOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainedModelExportsConfigurationPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainedModelExportsConfigurationPolicy:
    boto3_raw_data: "type_defs.TrainedModelExportsConfigurationPolicyTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def maxSize(self):  # pragma: no cover
        return TrainedModelExportsMaxSize.make_one(self.boto3_raw_data["maxSize"])

    filesToExport = field("filesToExport")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TrainedModelExportsConfigurationPolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainedModelExportsConfigurationPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredAudienceModelOutputConfig:
    boto3_raw_data: "type_defs.ConfiguredAudienceModelOutputConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def destination(self):  # pragma: no cover
        return AudienceDestination.make_one(self.boto3_raw_data["destination"])

    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfiguredAudienceModelOutputConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfiguredAudienceModelOutputConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MLOutputConfiguration:
    boto3_raw_data: "type_defs.MLOutputConfigurationTypeDef" = dataclasses.field()

    roleArn = field("roleArn")

    @cached_property
    def destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["destination"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MLOutputConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MLOutputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudienceQualityMetrics:
    boto3_raw_data: "type_defs.AudienceQualityMetricsTypeDef" = dataclasses.field()

    @cached_property
    def relevanceMetrics(self):  # pragma: no cover
        return RelevanceMetric.make_many(self.boto3_raw_data["relevanceMetrics"])

    recallMetric = field("recallMetric")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudienceQualityMetricsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudienceQualityMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAudienceExportJobsResponse:
    boto3_raw_data: "type_defs.ListAudienceExportJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def audienceExportJobs(self):  # pragma: no cover
        return AudienceExportJobSummary.make_many(
            self.boto3_raw_data["audienceExportJobs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAudienceExportJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAudienceExportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationTrainedModelsResponse:
    boto3_raw_data: "type_defs.ListCollaborationTrainedModelsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def collaborationTrainedModels(self):  # pragma: no cover
        return CollaborationTrainedModelSummary.make_many(
            self.boto3_raw_data["collaborationTrainedModels"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationTrainedModelsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollaborationTrainedModelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrainedModelVersionsResponse:
    boto3_raw_data: "type_defs.ListTrainedModelVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def trainedModels(self):  # pragma: no cover
        return TrainedModelSummary.make_many(self.boto3_raw_data["trainedModels"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTrainedModelVersionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrainedModelVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrainedModelsResponse:
    boto3_raw_data: "type_defs.ListTrainedModelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def trainedModels(self):  # pragma: no cover
        return TrainedModelSummary.make_many(self.boto3_raw_data["trainedModels"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTrainedModelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrainedModelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudienceGenerationJobDataSourceOutput:
    boto3_raw_data: "type_defs.AudienceGenerationJobDataSourceOutputTypeDef" = (
        dataclasses.field()
    )

    roleArn = field("roleArn")

    @cached_property
    def dataSource(self):  # pragma: no cover
        return S3ConfigMap.make_one(self.boto3_raw_data["dataSource"])

    @cached_property
    def sqlParameters(self):  # pragma: no cover
        return ProtectedQuerySQLParametersOutput.make_one(
            self.boto3_raw_data["sqlParameters"]
        )

    @cached_property
    def sqlComputeConfiguration(self):  # pragma: no cover
        return ComputeConfiguration.make_one(
            self.boto3_raw_data["sqlComputeConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AudienceGenerationJobDataSourceOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudienceGenerationJobDataSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudienceGenerationJobDataSource:
    boto3_raw_data: "type_defs.AudienceGenerationJobDataSourceTypeDef" = (
        dataclasses.field()
    )

    roleArn = field("roleArn")

    @cached_property
    def dataSource(self):  # pragma: no cover
        return S3ConfigMap.make_one(self.boto3_raw_data["dataSource"])

    @cached_property
    def sqlParameters(self):  # pragma: no cover
        return ProtectedQuerySQLParameters.make_one(
            self.boto3_raw_data["sqlParameters"]
        )

    @cached_property
    def sqlComputeConfiguration(self):  # pragma: no cover
        return ComputeConfiguration.make_one(
            self.boto3_raw_data["sqlComputeConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AudienceGenerationJobDataSourceTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudienceGenerationJobDataSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQueryInputParametersOutput:
    boto3_raw_data: "type_defs.ProtectedQueryInputParametersOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sqlParameters(self):  # pragma: no cover
        return ProtectedQuerySQLParametersOutput.make_one(
            self.boto3_raw_data["sqlParameters"]
        )

    @cached_property
    def computeConfiguration(self):  # pragma: no cover
        return ComputeConfiguration.make_one(
            self.boto3_raw_data["computeConfiguration"]
        )

    resultFormat = field("resultFormat")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedQueryInputParametersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedQueryInputParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQueryInputParameters:
    boto3_raw_data: "type_defs.ProtectedQueryInputParametersTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sqlParameters(self):  # pragma: no cover
        return ProtectedQuerySQLParameters.make_one(
            self.boto3_raw_data["sqlParameters"]
        )

    @cached_property
    def computeConfiguration(self):  # pragma: no cover
        return ComputeConfiguration.make_one(
            self.boto3_raw_data["computeConfiguration"]
        )

    resultFormat = field("resultFormat")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProtectedQueryInputParametersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedQueryInputParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfiguredModelAlgorithmResponse:
    boto3_raw_data: "type_defs.GetConfiguredModelAlgorithmResponseTypeDef" = (
        dataclasses.field()
    )

    createTime = field("createTime")
    updateTime = field("updateTime")
    configuredModelAlgorithmArn = field("configuredModelAlgorithmArn")
    name = field("name")

    @cached_property
    def trainingContainerConfig(self):  # pragma: no cover
        return ContainerConfigOutput.make_one(
            self.boto3_raw_data["trainingContainerConfig"]
        )

    @cached_property
    def inferenceContainerConfig(self):  # pragma: no cover
        return InferenceContainerConfig.make_one(
            self.boto3_raw_data["inferenceContainerConfig"]
        )

    roleArn = field("roleArn")
    description = field("description")
    tags = field("tags")
    kmsKeyArn = field("kmsKeyArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConfiguredModelAlgorithmResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfiguredModelAlgorithmResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogsConfigurationPolicyOutput:
    boto3_raw_data: "type_defs.LogsConfigurationPolicyOutputTypeDef" = (
        dataclasses.field()
    )

    allowedAccountIds = field("allowedAccountIds")
    filterPattern = field("filterPattern")
    logType = field("logType")

    @cached_property
    def logRedactionConfiguration(self):  # pragma: no cover
        return LogRedactionConfigurationOutput.make_one(
            self.boto3_raw_data["logRedactionConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LogsConfigurationPolicyOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogsConfigurationPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogsConfigurationPolicy:
    boto3_raw_data: "type_defs.LogsConfigurationPolicyTypeDef" = dataclasses.field()

    allowedAccountIds = field("allowedAccountIds")
    filterPattern = field("filterPattern")
    logType = field("logType")

    @cached_property
    def logRedactionConfiguration(self):  # pragma: no cover
        return LogRedactionConfiguration.make_one(
            self.boto3_raw_data["logRedactionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LogsConfigurationPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogsConfigurationPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetInputConfigOutput:
    boto3_raw_data: "type_defs.DatasetInputConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def schema(self):  # pragma: no cover
        return ColumnSchemaOutput.make_many(self.boto3_raw_data["schema"])

    @cached_property
    def dataSource(self):  # pragma: no cover
        return DataSource.make_one(self.boto3_raw_data["dataSource"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasetInputConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetInputConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetInputConfig:
    boto3_raw_data: "type_defs.DatasetInputConfigTypeDef" = dataclasses.field()

    schema = field("schema")

    @cached_property
    def dataSource(self):  # pragma: no cover
        return DataSource.make_one(self.boto3_raw_data["dataSource"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasetInputConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetInputConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollaborationTrainedModelInferenceJobSummary:
    boto3_raw_data: "type_defs.CollaborationTrainedModelInferenceJobSummaryTypeDef" = (
        dataclasses.field()
    )

    trainedModelInferenceJobArn = field("trainedModelInferenceJobArn")
    membershipIdentifier = field("membershipIdentifier")
    trainedModelArn = field("trainedModelArn")
    collaborationIdentifier = field("collaborationIdentifier")
    status = field("status")

    @cached_property
    def outputConfiguration(self):  # pragma: no cover
        return InferenceOutputConfigurationOutput.make_one(
            self.boto3_raw_data["outputConfiguration"]
        )

    name = field("name")
    createTime = field("createTime")
    updateTime = field("updateTime")
    creatorAccountId = field("creatorAccountId")
    configuredModelAlgorithmAssociationArn = field(
        "configuredModelAlgorithmAssociationArn"
    )
    trainedModelVersionIdentifier = field("trainedModelVersionIdentifier")
    description = field("description")
    metricsStatus = field("metricsStatus")
    metricsStatusDetails = field("metricsStatusDetails")
    logsStatus = field("logsStatus")
    logsStatusDetails = field("logsStatusDetails")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CollaborationTrainedModelInferenceJobSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollaborationTrainedModelInferenceJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrainedModelInferenceJobResponse:
    boto3_raw_data: "type_defs.GetTrainedModelInferenceJobResponseTypeDef" = (
        dataclasses.field()
    )

    createTime = field("createTime")
    updateTime = field("updateTime")
    trainedModelInferenceJobArn = field("trainedModelInferenceJobArn")
    configuredModelAlgorithmAssociationArn = field(
        "configuredModelAlgorithmAssociationArn"
    )
    name = field("name")
    status = field("status")
    trainedModelArn = field("trainedModelArn")
    trainedModelVersionIdentifier = field("trainedModelVersionIdentifier")

    @cached_property
    def resourceConfig(self):  # pragma: no cover
        return InferenceResourceConfig.make_one(self.boto3_raw_data["resourceConfig"])

    @cached_property
    def outputConfiguration(self):  # pragma: no cover
        return InferenceOutputConfigurationOutput.make_one(
            self.boto3_raw_data["outputConfiguration"]
        )

    membershipIdentifier = field("membershipIdentifier")

    @cached_property
    def dataSource(self):  # pragma: no cover
        return ModelInferenceDataSource.make_one(self.boto3_raw_data["dataSource"])

    @cached_property
    def containerExecutionParameters(self):  # pragma: no cover
        return InferenceContainerExecutionParameters.make_one(
            self.boto3_raw_data["containerExecutionParameters"]
        )

    @cached_property
    def statusDetails(self):  # pragma: no cover
        return StatusDetails.make_one(self.boto3_raw_data["statusDetails"])

    description = field("description")
    inferenceContainerImageDigest = field("inferenceContainerImageDigest")
    environment = field("environment")
    kmsKeyArn = field("kmsKeyArn")
    metricsStatus = field("metricsStatus")
    metricsStatusDetails = field("metricsStatusDetails")
    logsStatus = field("logsStatus")
    logsStatusDetails = field("logsStatusDetails")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTrainedModelInferenceJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrainedModelInferenceJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainedModelInferenceJobSummary:
    boto3_raw_data: "type_defs.TrainedModelInferenceJobSummaryTypeDef" = (
        dataclasses.field()
    )

    trainedModelInferenceJobArn = field("trainedModelInferenceJobArn")
    membershipIdentifier = field("membershipIdentifier")
    trainedModelArn = field("trainedModelArn")
    collaborationIdentifier = field("collaborationIdentifier")
    status = field("status")

    @cached_property
    def outputConfiguration(self):  # pragma: no cover
        return InferenceOutputConfigurationOutput.make_one(
            self.boto3_raw_data["outputConfiguration"]
        )

    name = field("name")
    createTime = field("createTime")
    updateTime = field("updateTime")
    configuredModelAlgorithmAssociationArn = field(
        "configuredModelAlgorithmAssociationArn"
    )
    trainedModelVersionIdentifier = field("trainedModelVersionIdentifier")
    description = field("description")
    metricsStatus = field("metricsStatus")
    metricsStatusDetails = field("metricsStatusDetails")
    logsStatus = field("logsStatus")
    logsStatusDetails = field("logsStatusDetails")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TrainedModelInferenceJobSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainedModelInferenceJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollaborationTrainedModelExportJobSummary:
    boto3_raw_data: "type_defs.CollaborationTrainedModelExportJobSummaryTypeDef" = (
        dataclasses.field()
    )

    createTime = field("createTime")
    updateTime = field("updateTime")
    name = field("name")

    @cached_property
    def outputConfiguration(self):  # pragma: no cover
        return TrainedModelExportOutputConfigurationOutput.make_one(
            self.boto3_raw_data["outputConfiguration"]
        )

    status = field("status")
    creatorAccountId = field("creatorAccountId")
    trainedModelArn = field("trainedModelArn")
    membershipIdentifier = field("membershipIdentifier")
    collaborationIdentifier = field("collaborationIdentifier")

    @cached_property
    def statusDetails(self):  # pragma: no cover
        return StatusDetails.make_one(self.boto3_raw_data["statusDetails"])

    description = field("description")
    trainedModelVersionIdentifier = field("trainedModelVersionIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CollaborationTrainedModelExportJobSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollaborationTrainedModelExportJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredAudienceModelSummary:
    boto3_raw_data: "type_defs.ConfiguredAudienceModelSummaryTypeDef" = (
        dataclasses.field()
    )

    createTime = field("createTime")
    updateTime = field("updateTime")
    name = field("name")
    audienceModelArn = field("audienceModelArn")

    @cached_property
    def outputConfig(self):  # pragma: no cover
        return ConfiguredAudienceModelOutputConfig.make_one(
            self.boto3_raw_data["outputConfig"]
        )

    configuredAudienceModelArn = field("configuredAudienceModelArn")
    status = field("status")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConfiguredAudienceModelSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfiguredAudienceModelSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfiguredAudienceModelRequest:
    boto3_raw_data: "type_defs.CreateConfiguredAudienceModelRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    audienceModelArn = field("audienceModelArn")

    @cached_property
    def outputConfig(self):  # pragma: no cover
        return ConfiguredAudienceModelOutputConfig.make_one(
            self.boto3_raw_data["outputConfig"]
        )

    sharedAudienceMetrics = field("sharedAudienceMetrics")
    description = field("description")
    minMatchingSeedSize = field("minMatchingSeedSize")
    audienceSizeConfig = field("audienceSizeConfig")
    tags = field("tags")
    childResourceTagOnCreatePolicy = field("childResourceTagOnCreatePolicy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConfiguredAudienceModelRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfiguredAudienceModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfiguredAudienceModelResponse:
    boto3_raw_data: "type_defs.GetConfiguredAudienceModelResponseTypeDef" = (
        dataclasses.field()
    )

    createTime = field("createTime")
    updateTime = field("updateTime")
    configuredAudienceModelArn = field("configuredAudienceModelArn")
    name = field("name")
    audienceModelArn = field("audienceModelArn")

    @cached_property
    def outputConfig(self):  # pragma: no cover
        return ConfiguredAudienceModelOutputConfig.make_one(
            self.boto3_raw_data["outputConfig"]
        )

    description = field("description")
    status = field("status")
    sharedAudienceMetrics = field("sharedAudienceMetrics")
    minMatchingSeedSize = field("minMatchingSeedSize")

    @cached_property
    def audienceSizeConfig(self):  # pragma: no cover
        return AudienceSizeConfigOutput.make_one(
            self.boto3_raw_data["audienceSizeConfig"]
        )

    tags = field("tags")
    childResourceTagOnCreatePolicy = field("childResourceTagOnCreatePolicy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConfiguredAudienceModelResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfiguredAudienceModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfiguredAudienceModelRequest:
    boto3_raw_data: "type_defs.UpdateConfiguredAudienceModelRequestTypeDef" = (
        dataclasses.field()
    )

    configuredAudienceModelArn = field("configuredAudienceModelArn")

    @cached_property
    def outputConfig(self):  # pragma: no cover
        return ConfiguredAudienceModelOutputConfig.make_one(
            self.boto3_raw_data["outputConfig"]
        )

    audienceModelArn = field("audienceModelArn")
    sharedAudienceMetrics = field("sharedAudienceMetrics")
    minMatchingSeedSize = field("minMatchingSeedSize")
    audienceSizeConfig = field("audienceSizeConfig")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConfiguredAudienceModelRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConfiguredAudienceModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMLConfigurationResponse:
    boto3_raw_data: "type_defs.GetMLConfigurationResponseTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")

    @cached_property
    def defaultOutputLocation(self):  # pragma: no cover
        return MLOutputConfiguration.make_one(
            self.boto3_raw_data["defaultOutputLocation"]
        )

    createTime = field("createTime")
    updateTime = field("updateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMLConfigurationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMLConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutMLConfigurationRequest:
    boto3_raw_data: "type_defs.PutMLConfigurationRequestTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")

    @cached_property
    def defaultOutputLocation(self):  # pragma: no cover
        return MLOutputConfiguration.make_one(
            self.boto3_raw_data["defaultOutputLocation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutMLConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutMLConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAudienceGenerationJobResponse:
    boto3_raw_data: "type_defs.GetAudienceGenerationJobResponseTypeDef" = (
        dataclasses.field()
    )

    createTime = field("createTime")
    updateTime = field("updateTime")
    audienceGenerationJobArn = field("audienceGenerationJobArn")
    name = field("name")
    description = field("description")
    status = field("status")

    @cached_property
    def statusDetails(self):  # pragma: no cover
        return StatusDetails.make_one(self.boto3_raw_data["statusDetails"])

    configuredAudienceModelArn = field("configuredAudienceModelArn")

    @cached_property
    def seedAudience(self):  # pragma: no cover
        return AudienceGenerationJobDataSourceOutput.make_one(
            self.boto3_raw_data["seedAudience"]
        )

    includeSeedInOutput = field("includeSeedInOutput")
    collaborationId = field("collaborationId")

    @cached_property
    def metrics(self):  # pragma: no cover
        return AudienceQualityMetrics.make_one(self.boto3_raw_data["metrics"])

    startedBy = field("startedBy")
    tags = field("tags")
    protectedQueryIdentifier = field("protectedQueryIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAudienceGenerationJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAudienceGenerationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputChannelDataSourceOutput:
    boto3_raw_data: "type_defs.InputChannelDataSourceOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def protectedQueryInputParameters(self):  # pragma: no cover
        return ProtectedQueryInputParametersOutput.make_one(
            self.boto3_raw_data["protectedQueryInputParameters"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputChannelDataSourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputChannelDataSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputChannelDataSource:
    boto3_raw_data: "type_defs.InputChannelDataSourceTypeDef" = dataclasses.field()

    @cached_property
    def protectedQueryInputParameters(self):  # pragma: no cover
        return ProtectedQueryInputParameters.make_one(
            self.boto3_raw_data["protectedQueryInputParameters"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputChannelDataSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputChannelDataSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfiguredModelAlgorithmRequest:
    boto3_raw_data: "type_defs.CreateConfiguredModelAlgorithmRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    roleArn = field("roleArn")
    description = field("description")
    trainingContainerConfig = field("trainingContainerConfig")

    @cached_property
    def inferenceContainerConfig(self):  # pragma: no cover
        return InferenceContainerConfig.make_one(
            self.boto3_raw_data["inferenceContainerConfig"]
        )

    tags = field("tags")
    kmsKeyArn = field("kmsKeyArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConfiguredModelAlgorithmRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfiguredModelAlgorithmRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainedModelInferenceJobsConfigurationPolicyOutput:
    boto3_raw_data: (
        "type_defs.TrainedModelInferenceJobsConfigurationPolicyOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def containerLogs(self):  # pragma: no cover
        return LogsConfigurationPolicyOutput.make_many(
            self.boto3_raw_data["containerLogs"]
        )

    @cached_property
    def maxOutputSize(self):  # pragma: no cover
        return TrainedModelInferenceMaxOutputSize.make_one(
            self.boto3_raw_data["maxOutputSize"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TrainedModelInferenceJobsConfigurationPolicyOutputTypeDef"
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
                "type_defs.TrainedModelInferenceJobsConfigurationPolicyOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainedModelsConfigurationPolicyOutput:
    boto3_raw_data: "type_defs.TrainedModelsConfigurationPolicyOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def containerLogs(self):  # pragma: no cover
        return LogsConfigurationPolicyOutput.make_many(
            self.boto3_raw_data["containerLogs"]
        )

    @cached_property
    def containerMetrics(self):  # pragma: no cover
        return MetricsConfigurationPolicy.make_one(
            self.boto3_raw_data["containerMetrics"]
        )

    @cached_property
    def maxArtifactSize(self):  # pragma: no cover
        return TrainedModelArtifactMaxSize.make_one(
            self.boto3_raw_data["maxArtifactSize"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TrainedModelsConfigurationPolicyOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainedModelsConfigurationPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainedModelInferenceJobsConfigurationPolicy:
    boto3_raw_data: "type_defs.TrainedModelInferenceJobsConfigurationPolicyTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def containerLogs(self):  # pragma: no cover
        return LogsConfigurationPolicy.make_many(self.boto3_raw_data["containerLogs"])

    @cached_property
    def maxOutputSize(self):  # pragma: no cover
        return TrainedModelInferenceMaxOutputSize.make_one(
            self.boto3_raw_data["maxOutputSize"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TrainedModelInferenceJobsConfigurationPolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainedModelInferenceJobsConfigurationPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainedModelsConfigurationPolicy:
    boto3_raw_data: "type_defs.TrainedModelsConfigurationPolicyTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def containerLogs(self):  # pragma: no cover
        return LogsConfigurationPolicy.make_many(self.boto3_raw_data["containerLogs"])

    @cached_property
    def containerMetrics(self):  # pragma: no cover
        return MetricsConfigurationPolicy.make_one(
            self.boto3_raw_data["containerMetrics"]
        )

    @cached_property
    def maxArtifactSize(self):  # pragma: no cover
        return TrainedModelArtifactMaxSize.make_one(
            self.boto3_raw_data["maxArtifactSize"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TrainedModelsConfigurationPolicyTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainedModelsConfigurationPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetOutput:
    boto3_raw_data: "type_defs.DatasetOutputTypeDef" = dataclasses.field()

    type = field("type")

    @cached_property
    def inputConfig(self):  # pragma: no cover
        return DatasetInputConfigOutput.make_one(self.boto3_raw_data["inputConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationTrainedModelInferenceJobsResponse:
    boto3_raw_data: (
        "type_defs.ListCollaborationTrainedModelInferenceJobsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def collaborationTrainedModelInferenceJobs(self):  # pragma: no cover
        return CollaborationTrainedModelInferenceJobSummary.make_many(
            self.boto3_raw_data["collaborationTrainedModelInferenceJobs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationTrainedModelInferenceJobsResponseTypeDef"
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
                "type_defs.ListCollaborationTrainedModelInferenceJobsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrainedModelInferenceJobsResponse:
    boto3_raw_data: "type_defs.ListTrainedModelInferenceJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def trainedModelInferenceJobs(self):  # pragma: no cover
        return TrainedModelInferenceJobSummary.make_many(
            self.boto3_raw_data["trainedModelInferenceJobs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrainedModelInferenceJobsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrainedModelInferenceJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTrainedModelInferenceJobRequest:
    boto3_raw_data: "type_defs.StartTrainedModelInferenceJobRequestTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")
    name = field("name")
    trainedModelArn = field("trainedModelArn")

    @cached_property
    def resourceConfig(self):  # pragma: no cover
        return InferenceResourceConfig.make_one(self.boto3_raw_data["resourceConfig"])

    outputConfiguration = field("outputConfiguration")

    @cached_property
    def dataSource(self):  # pragma: no cover
        return ModelInferenceDataSource.make_one(self.boto3_raw_data["dataSource"])

    trainedModelVersionIdentifier = field("trainedModelVersionIdentifier")
    configuredModelAlgorithmAssociationArn = field(
        "configuredModelAlgorithmAssociationArn"
    )
    description = field("description")

    @cached_property
    def containerExecutionParameters(self):  # pragma: no cover
        return InferenceContainerExecutionParameters.make_one(
            self.boto3_raw_data["containerExecutionParameters"]
        )

    environment = field("environment")
    kmsKeyArn = field("kmsKeyArn")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartTrainedModelInferenceJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTrainedModelInferenceJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationTrainedModelExportJobsResponse:
    boto3_raw_data: (
        "type_defs.ListCollaborationTrainedModelExportJobsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def collaborationTrainedModelExportJobs(self):  # pragma: no cover
        return CollaborationTrainedModelExportJobSummary.make_many(
            self.boto3_raw_data["collaborationTrainedModelExportJobs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationTrainedModelExportJobsResponseTypeDef"
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
                "type_defs.ListCollaborationTrainedModelExportJobsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTrainedModelExportJobRequest:
    boto3_raw_data: "type_defs.StartTrainedModelExportJobRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    trainedModelArn = field("trainedModelArn")
    membershipIdentifier = field("membershipIdentifier")
    outputConfiguration = field("outputConfiguration")
    trainedModelVersionIdentifier = field("trainedModelVersionIdentifier")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartTrainedModelExportJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTrainedModelExportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfiguredAudienceModelsResponse:
    boto3_raw_data: "type_defs.ListConfiguredAudienceModelsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configuredAudienceModels(self):  # pragma: no cover
        return ConfiguredAudienceModelSummary.make_many(
            self.boto3_raw_data["configuredAudienceModels"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfiguredAudienceModelsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfiguredAudienceModelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAudienceGenerationJobRequest:
    boto3_raw_data: "type_defs.StartAudienceGenerationJobRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    configuredAudienceModelArn = field("configuredAudienceModelArn")
    seedAudience = field("seedAudience")
    includeSeedInOutput = field("includeSeedInOutput")
    collaborationId = field("collaborationId")
    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartAudienceGenerationJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAudienceGenerationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputChannelOutput:
    boto3_raw_data: "type_defs.InputChannelOutputTypeDef" = dataclasses.field()

    @cached_property
    def dataSource(self):  # pragma: no cover
        return InputChannelDataSourceOutput.make_one(self.boto3_raw_data["dataSource"])

    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputChannelOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputChannelOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputChannel:
    boto3_raw_data: "type_defs.InputChannelTypeDef" = dataclasses.field()

    @cached_property
    def dataSource(self):  # pragma: no cover
        return InputChannelDataSource.make_one(self.boto3_raw_data["dataSource"])

    roleArn = field("roleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputChannelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputChannelTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivacyConfigurationPoliciesOutput:
    boto3_raw_data: "type_defs.PrivacyConfigurationPoliciesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def trainedModels(self):  # pragma: no cover
        return TrainedModelsConfigurationPolicyOutput.make_one(
            self.boto3_raw_data["trainedModels"]
        )

    @cached_property
    def trainedModelExports(self):  # pragma: no cover
        return TrainedModelExportsConfigurationPolicyOutput.make_one(
            self.boto3_raw_data["trainedModelExports"]
        )

    @cached_property
    def trainedModelInferenceJobs(self):  # pragma: no cover
        return TrainedModelInferenceJobsConfigurationPolicyOutput.make_one(
            self.boto3_raw_data["trainedModelInferenceJobs"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PrivacyConfigurationPoliciesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivacyConfigurationPoliciesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivacyConfigurationPolicies:
    boto3_raw_data: "type_defs.PrivacyConfigurationPoliciesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def trainedModels(self):  # pragma: no cover
        return TrainedModelsConfigurationPolicy.make_one(
            self.boto3_raw_data["trainedModels"]
        )

    @cached_property
    def trainedModelExports(self):  # pragma: no cover
        return TrainedModelExportsConfigurationPolicy.make_one(
            self.boto3_raw_data["trainedModelExports"]
        )

    @cached_property
    def trainedModelInferenceJobs(self):  # pragma: no cover
        return TrainedModelInferenceJobsConfigurationPolicy.make_one(
            self.boto3_raw_data["trainedModelInferenceJobs"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrivacyConfigurationPoliciesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivacyConfigurationPoliciesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrainingDatasetResponse:
    boto3_raw_data: "type_defs.GetTrainingDatasetResponseTypeDef" = dataclasses.field()

    createTime = field("createTime")
    updateTime = field("updateTime")
    trainingDatasetArn = field("trainingDatasetArn")
    name = field("name")

    @cached_property
    def trainingData(self):  # pragma: no cover
        return DatasetOutput.make_many(self.boto3_raw_data["trainingData"])

    status = field("status")
    roleArn = field("roleArn")
    tags = field("tags")
    description = field("description")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTrainingDatasetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrainingDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Dataset:
    boto3_raw_data: "type_defs.DatasetTypeDef" = dataclasses.field()

    type = field("type")
    inputConfig = field("inputConfig")

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
class GetMLInputChannelResponse:
    boto3_raw_data: "type_defs.GetMLInputChannelResponseTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    collaborationIdentifier = field("collaborationIdentifier")
    mlInputChannelArn = field("mlInputChannelArn")
    name = field("name")
    configuredModelAlgorithmAssociations = field("configuredModelAlgorithmAssociations")
    status = field("status")

    @cached_property
    def statusDetails(self):  # pragma: no cover
        return StatusDetails.make_one(self.boto3_raw_data["statusDetails"])

    retentionInDays = field("retentionInDays")
    numberOfRecords = field("numberOfRecords")
    description = field("description")
    createTime = field("createTime")
    updateTime = field("updateTime")

    @cached_property
    def inputChannel(self):  # pragma: no cover
        return InputChannelOutput.make_one(self.boto3_raw_data["inputChannel"])

    protectedQueryIdentifier = field("protectedQueryIdentifier")
    numberOfFiles = field("numberOfFiles")
    sizeInGb = field("sizeInGb")
    kmsKeyArn = field("kmsKeyArn")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMLInputChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMLInputChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivacyConfigurationOutput:
    boto3_raw_data: "type_defs.PrivacyConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def policies(self):  # pragma: no cover
        return PrivacyConfigurationPoliciesOutput.make_one(
            self.boto3_raw_data["policies"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrivacyConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivacyConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivacyConfiguration:
    boto3_raw_data: "type_defs.PrivacyConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def policies(self):  # pragma: no cover
        return PrivacyConfigurationPolicies.make_one(self.boto3_raw_data["policies"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrivacyConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivacyConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMLInputChannelRequest:
    boto3_raw_data: "type_defs.CreateMLInputChannelRequestTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    configuredModelAlgorithmAssociations = field("configuredModelAlgorithmAssociations")
    inputChannel = field("inputChannel")
    name = field("name")
    retentionInDays = field("retentionInDays")
    description = field("description")
    kmsKeyArn = field("kmsKeyArn")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMLInputChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMLInputChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCollaborationConfiguredModelAlgorithmAssociationResponse:
    boto3_raw_data: (
        "type_defs.GetCollaborationConfiguredModelAlgorithmAssociationResponseTypeDef"
    ) = dataclasses.field()

    createTime = field("createTime")
    updateTime = field("updateTime")
    configuredModelAlgorithmAssociationArn = field(
        "configuredModelAlgorithmAssociationArn"
    )
    membershipIdentifier = field("membershipIdentifier")
    collaborationIdentifier = field("collaborationIdentifier")
    configuredModelAlgorithmArn = field("configuredModelAlgorithmArn")
    name = field("name")
    description = field("description")
    creatorAccountId = field("creatorAccountId")

    @cached_property
    def privacyConfiguration(self):  # pragma: no cover
        return PrivacyConfigurationOutput.make_one(
            self.boto3_raw_data["privacyConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCollaborationConfiguredModelAlgorithmAssociationResponseTypeDef"
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
                "type_defs.GetCollaborationConfiguredModelAlgorithmAssociationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfiguredModelAlgorithmAssociationResponse:
    boto3_raw_data: (
        "type_defs.GetConfiguredModelAlgorithmAssociationResponseTypeDef"
    ) = dataclasses.field()

    createTime = field("createTime")
    updateTime = field("updateTime")
    configuredModelAlgorithmAssociationArn = field(
        "configuredModelAlgorithmAssociationArn"
    )
    membershipIdentifier = field("membershipIdentifier")
    collaborationIdentifier = field("collaborationIdentifier")
    configuredModelAlgorithmArn = field("configuredModelAlgorithmArn")
    name = field("name")

    @cached_property
    def privacyConfiguration(self):  # pragma: no cover
        return PrivacyConfigurationOutput.make_one(
            self.boto3_raw_data["privacyConfiguration"]
        )

    description = field("description")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConfiguredModelAlgorithmAssociationResponseTypeDef"
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
                "type_defs.GetConfiguredModelAlgorithmAssociationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrainingDatasetRequest:
    boto3_raw_data: "type_defs.CreateTrainingDatasetRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    roleArn = field("roleArn")
    trainingData = field("trainingData")
    tags = field("tags")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTrainingDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrainingDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfiguredModelAlgorithmAssociationRequest:
    boto3_raw_data: (
        "type_defs.CreateConfiguredModelAlgorithmAssociationRequestTypeDef"
    ) = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    configuredModelAlgorithmArn = field("configuredModelAlgorithmArn")
    name = field("name")
    description = field("description")
    privacyConfiguration = field("privacyConfiguration")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConfiguredModelAlgorithmAssociationRequestTypeDef"
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
                "type_defs.CreateConfiguredModelAlgorithmAssociationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
