# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ecr import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Attribute:
    boto3_raw_data: "type_defs.AttributeTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

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
class AuthorizationData:
    boto3_raw_data: "type_defs.AuthorizationDataTypeDef" = dataclasses.field()

    authorizationToken = field("authorizationToken")
    expiresAt = field("expiresAt")
    proxyEndpoint = field("proxyEndpoint")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuthorizationDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizationDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsEcrContainerImageDetails:
    boto3_raw_data: "type_defs.AwsEcrContainerImageDetailsTypeDef" = dataclasses.field()

    architecture = field("architecture")
    author = field("author")
    imageHash = field("imageHash")
    imageTags = field("imageTags")
    platform = field("platform")
    pushedAt = field("pushedAt")
    lastInUseAt = field("lastInUseAt")
    inUseCount = field("inUseCount")
    registry = field("registry")
    repositoryName = field("repositoryName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsEcrContainerImageDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsEcrContainerImageDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCheckLayerAvailabilityRequest:
    boto3_raw_data: "type_defs.BatchCheckLayerAvailabilityRequestTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    layerDigests = field("layerDigests")
    registryId = field("registryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCheckLayerAvailabilityRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCheckLayerAvailabilityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LayerFailure:
    boto3_raw_data: "type_defs.LayerFailureTypeDef" = dataclasses.field()

    layerDigest = field("layerDigest")
    failureCode = field("failureCode")
    failureReason = field("failureReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LayerFailureTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LayerFailureTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Layer:
    boto3_raw_data: "type_defs.LayerTypeDef" = dataclasses.field()

    layerDigest = field("layerDigest")
    layerAvailability = field("layerAvailability")
    layerSize = field("layerSize")
    mediaType = field("mediaType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LayerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LayerTypeDef"]]
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
class ImageIdentifier:
    boto3_raw_data: "type_defs.ImageIdentifierTypeDef" = dataclasses.field()

    imageDigest = field("imageDigest")
    imageTag = field("imageTag")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageIdentifierTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageIdentifierTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetRepositoryScanningConfigurationRequest:
    boto3_raw_data: (
        "type_defs.BatchGetRepositoryScanningConfigurationRequestTypeDef"
    ) = dataclasses.field()

    repositoryNames = field("repositoryNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetRepositoryScanningConfigurationRequestTypeDef"
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
                "type_defs.BatchGetRepositoryScanningConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositoryScanningConfigurationFailure:
    boto3_raw_data: "type_defs.RepositoryScanningConfigurationFailureTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    failureCode = field("failureCode")
    failureReason = field("failureReason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RepositoryScanningConfigurationFailureTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositoryScanningConfigurationFailureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompleteLayerUploadRequest:
    boto3_raw_data: "type_defs.CompleteLayerUploadRequestTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    uploadId = field("uploadId")
    layerDigests = field("layerDigests")
    registryId = field("registryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompleteLayerUploadRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompleteLayerUploadRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePullThroughCacheRuleRequest:
    boto3_raw_data: "type_defs.CreatePullThroughCacheRuleRequestTypeDef" = (
        dataclasses.field()
    )

    ecrRepositoryPrefix = field("ecrRepositoryPrefix")
    upstreamRegistryUrl = field("upstreamRegistryUrl")
    registryId = field("registryId")
    upstreamRegistry = field("upstreamRegistry")
    credentialArn = field("credentialArn")
    customRoleArn = field("customRoleArn")
    upstreamRepositoryPrefix = field("upstreamRepositoryPrefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePullThroughCacheRuleRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePullThroughCacheRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionConfigurationForRepositoryCreationTemplate:
    boto3_raw_data: (
        "type_defs.EncryptionConfigurationForRepositoryCreationTemplateTypeDef"
    ) = dataclasses.field()

    encryptionType = field("encryptionType")
    kmsKey = field("kmsKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EncryptionConfigurationForRepositoryCreationTemplateTypeDef"
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
                "type_defs.EncryptionConfigurationForRepositoryCreationTemplateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageTagMutabilityExclusionFilter:
    boto3_raw_data: "type_defs.ImageTagMutabilityExclusionFilterTypeDef" = (
        dataclasses.field()
    )

    filterType = field("filterType")
    filter = field("filter")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ImageTagMutabilityExclusionFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageTagMutabilityExclusionFilterTypeDef"]
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
class EncryptionConfiguration:
    boto3_raw_data: "type_defs.EncryptionConfigurationTypeDef" = dataclasses.field()

    encryptionType = field("encryptionType")
    kmsKey = field("kmsKey")

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
class ImageScanningConfiguration:
    boto3_raw_data: "type_defs.ImageScanningConfigurationTypeDef" = dataclasses.field()

    scanOnPush = field("scanOnPush")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageScanningConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageScanningConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CvssScoreAdjustment:
    boto3_raw_data: "type_defs.CvssScoreAdjustmentTypeDef" = dataclasses.field()

    metric = field("metric")
    reason = field("reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CvssScoreAdjustmentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CvssScoreAdjustmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CvssScore:
    boto3_raw_data: "type_defs.CvssScoreTypeDef" = dataclasses.field()

    baseScore = field("baseScore")
    scoringVector = field("scoringVector")
    source = field("source")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CvssScoreTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CvssScoreTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLifecyclePolicyRequest:
    boto3_raw_data: "type_defs.DeleteLifecyclePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    registryId = field("registryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLifecyclePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLifecyclePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePullThroughCacheRuleRequest:
    boto3_raw_data: "type_defs.DeletePullThroughCacheRuleRequestTypeDef" = (
        dataclasses.field()
    )

    ecrRepositoryPrefix = field("ecrRepositoryPrefix")
    registryId = field("registryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeletePullThroughCacheRuleRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePullThroughCacheRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRepositoryCreationTemplateRequest:
    boto3_raw_data: "type_defs.DeleteRepositoryCreationTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    prefix = field("prefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRepositoryCreationTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRepositoryCreationTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRepositoryPolicyRequest:
    boto3_raw_data: "type_defs.DeleteRepositoryPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    registryId = field("registryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteRepositoryPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRepositoryPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRepositoryRequest:
    boto3_raw_data: "type_defs.DeleteRepositoryRequestTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    registryId = field("registryId")
    force = field("force")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRepositoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRepositoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageReplicationStatus:
    boto3_raw_data: "type_defs.ImageReplicationStatusTypeDef" = dataclasses.field()

    region = field("region")
    registryId = field("registryId")
    status = field("status")
    failureCode = field("failureCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageReplicationStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageReplicationStatusTypeDef"]
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
class ImageScanStatus:
    boto3_raw_data: "type_defs.ImageScanStatusTypeDef" = dataclasses.field()

    status = field("status")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageScanStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageScanStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImagesFilter:
    boto3_raw_data: "type_defs.DescribeImagesFilterTypeDef" = dataclasses.field()

    tagStatus = field("tagStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeImagesFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImagesFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePullThroughCacheRulesRequest:
    boto3_raw_data: "type_defs.DescribePullThroughCacheRulesRequestTypeDef" = (
        dataclasses.field()
    )

    registryId = field("registryId")
    ecrRepositoryPrefixes = field("ecrRepositoryPrefixes")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePullThroughCacheRulesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePullThroughCacheRulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PullThroughCacheRule:
    boto3_raw_data: "type_defs.PullThroughCacheRuleTypeDef" = dataclasses.field()

    ecrRepositoryPrefix = field("ecrRepositoryPrefix")
    upstreamRegistryUrl = field("upstreamRegistryUrl")
    createdAt = field("createdAt")
    registryId = field("registryId")
    credentialArn = field("credentialArn")
    customRoleArn = field("customRoleArn")
    upstreamRepositoryPrefix = field("upstreamRepositoryPrefix")
    upstreamRegistry = field("upstreamRegistry")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PullThroughCacheRuleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PullThroughCacheRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRepositoriesRequest:
    boto3_raw_data: "type_defs.DescribeRepositoriesRequestTypeDef" = dataclasses.field()

    registryId = field("registryId")
    repositoryNames = field("repositoryNames")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRepositoriesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRepositoriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRepositoryCreationTemplatesRequest:
    boto3_raw_data: "type_defs.DescribeRepositoryCreationTemplatesRequestTypeDef" = (
        dataclasses.field()
    )

    prefixes = field("prefixes")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRepositoryCreationTemplatesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRepositoryCreationTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountSettingRequest:
    boto3_raw_data: "type_defs.GetAccountSettingRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccountSettingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountSettingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAuthorizationTokenRequest:
    boto3_raw_data: "type_defs.GetAuthorizationTokenRequestTypeDef" = (
        dataclasses.field()
    )

    registryIds = field("registryIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAuthorizationTokenRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAuthorizationTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDownloadUrlForLayerRequest:
    boto3_raw_data: "type_defs.GetDownloadUrlForLayerRequestTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    layerDigest = field("layerDigest")
    registryId = field("registryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDownloadUrlForLayerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDownloadUrlForLayerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicyPreviewFilter:
    boto3_raw_data: "type_defs.LifecyclePolicyPreviewFilterTypeDef" = (
        dataclasses.field()
    )

    tagStatus = field("tagStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecyclePolicyPreviewFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicyPreviewFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicyPreviewSummary:
    boto3_raw_data: "type_defs.LifecyclePolicyPreviewSummaryTypeDef" = (
        dataclasses.field()
    )

    expiringImageTotalCount = field("expiringImageTotalCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LifecyclePolicyPreviewSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicyPreviewSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLifecyclePolicyRequest:
    boto3_raw_data: "type_defs.GetLifecyclePolicyRequestTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    registryId = field("registryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLifecyclePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLifecyclePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRepositoryPolicyRequest:
    boto3_raw_data: "type_defs.GetRepositoryPolicyRequestTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    registryId = field("registryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRepositoryPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRepositoryPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageScanFindingsSummary:
    boto3_raw_data: "type_defs.ImageScanFindingsSummaryTypeDef" = dataclasses.field()

    imageScanCompletedAt = field("imageScanCompletedAt")
    vulnerabilitySourceUpdatedAt = field("vulnerabilitySourceUpdatedAt")
    findingSeverityCounts = field("findingSeverityCounts")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageScanFindingsSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageScanFindingsSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InitiateLayerUploadRequest:
    boto3_raw_data: "type_defs.InitiateLayerUploadRequestTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    registryId = field("registryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InitiateLayerUploadRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InitiateLayerUploadRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicyRuleAction:
    boto3_raw_data: "type_defs.LifecyclePolicyRuleActionTypeDef" = dataclasses.field()

    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecyclePolicyRuleActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicyRuleActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImagesFilter:
    boto3_raw_data: "type_defs.ListImagesFilterTypeDef" = dataclasses.field()

    tagStatus = field("tagStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListImagesFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImagesFilterTypeDef"]
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
class VulnerablePackage:
    boto3_raw_data: "type_defs.VulnerablePackageTypeDef" = dataclasses.field()

    arch = field("arch")
    epoch = field("epoch")
    filePath = field("filePath")
    name = field("name")
    packageManager = field("packageManager")
    release = field("release")
    sourceLayerHash = field("sourceLayerHash")
    version = field("version")
    fixedInVersion = field("fixedInVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VulnerablePackageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VulnerablePackageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAccountSettingRequest:
    boto3_raw_data: "type_defs.PutAccountSettingRequestTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAccountSettingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccountSettingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutImageRequest:
    boto3_raw_data: "type_defs.PutImageRequestTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    imageManifest = field("imageManifest")
    registryId = field("registryId")
    imageManifestMediaType = field("imageManifestMediaType")
    imageTag = field("imageTag")
    imageDigest = field("imageDigest")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutImageRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutImageRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutLifecyclePolicyRequest:
    boto3_raw_data: "type_defs.PutLifecyclePolicyRequestTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    lifecyclePolicyText = field("lifecyclePolicyText")
    registryId = field("registryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutLifecyclePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutLifecyclePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRegistryPolicyRequest:
    boto3_raw_data: "type_defs.PutRegistryPolicyRequestTypeDef" = dataclasses.field()

    policyText = field("policyText")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutRegistryPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRegistryPolicyRequestTypeDef"]
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

    url = field("url")
    text = field("text")

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
class ScanningRepositoryFilter:
    boto3_raw_data: "type_defs.ScanningRepositoryFilterTypeDef" = dataclasses.field()

    filter = field("filter")
    filterType = field("filterType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScanningRepositoryFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScanningRepositoryFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationDestination:
    boto3_raw_data: "type_defs.ReplicationDestinationTypeDef" = dataclasses.field()

    region = field("region")
    registryId = field("registryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositoryFilter:
    boto3_raw_data: "type_defs.RepositoryFilterTypeDef" = dataclasses.field()

    filter = field("filter")
    filterType = field("filterType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RepositoryFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositoryFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetRepositoryPolicyRequest:
    boto3_raw_data: "type_defs.SetRepositoryPolicyRequestTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    policyText = field("policyText")
    registryId = field("registryId")
    force = field("force")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetRepositoryPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetRepositoryPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartLifecyclePolicyPreviewRequest:
    boto3_raw_data: "type_defs.StartLifecyclePolicyPreviewRequestTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    registryId = field("registryId")
    lifecyclePolicyText = field("lifecyclePolicyText")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartLifecyclePolicyPreviewRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartLifecyclePolicyPreviewRequestTypeDef"]
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
class UpdatePullThroughCacheRuleRequest:
    boto3_raw_data: "type_defs.UpdatePullThroughCacheRuleRequestTypeDef" = (
        dataclasses.field()
    )

    ecrRepositoryPrefix = field("ecrRepositoryPrefix")
    registryId = field("registryId")
    credentialArn = field("credentialArn")
    customRoleArn = field("customRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePullThroughCacheRuleRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePullThroughCacheRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidatePullThroughCacheRuleRequest:
    boto3_raw_data: "type_defs.ValidatePullThroughCacheRuleRequestTypeDef" = (
        dataclasses.field()
    )

    ecrRepositoryPrefix = field("ecrRepositoryPrefix")
    registryId = field("registryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ValidatePullThroughCacheRuleRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidatePullThroughCacheRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageScanFinding:
    boto3_raw_data: "type_defs.ImageScanFindingTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    uri = field("uri")
    severity = field("severity")

    @cached_property
    def attributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["attributes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageScanFindingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageScanFindingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceDetails:
    boto3_raw_data: "type_defs.ResourceDetailsTypeDef" = dataclasses.field()

    @cached_property
    def awsEcrContainerImage(self):  # pragma: no cover
        return AwsEcrContainerImageDetails.make_one(
            self.boto3_raw_data["awsEcrContainerImage"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCheckLayerAvailabilityResponse:
    boto3_raw_data: "type_defs.BatchCheckLayerAvailabilityResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def layers(self):  # pragma: no cover
        return Layer.make_many(self.boto3_raw_data["layers"])

    @cached_property
    def failures(self):  # pragma: no cover
        return LayerFailure.make_many(self.boto3_raw_data["failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCheckLayerAvailabilityResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCheckLayerAvailabilityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompleteLayerUploadResponse:
    boto3_raw_data: "type_defs.CompleteLayerUploadResponseTypeDef" = dataclasses.field()

    registryId = field("registryId")
    repositoryName = field("repositoryName")
    uploadId = field("uploadId")
    layerDigest = field("layerDigest")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompleteLayerUploadResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompleteLayerUploadResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePullThroughCacheRuleResponse:
    boto3_raw_data: "type_defs.CreatePullThroughCacheRuleResponseTypeDef" = (
        dataclasses.field()
    )

    ecrRepositoryPrefix = field("ecrRepositoryPrefix")
    upstreamRegistryUrl = field("upstreamRegistryUrl")
    createdAt = field("createdAt")
    registryId = field("registryId")
    upstreamRegistry = field("upstreamRegistry")
    credentialArn = field("credentialArn")
    customRoleArn = field("customRoleArn")
    upstreamRepositoryPrefix = field("upstreamRepositoryPrefix")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePullThroughCacheRuleResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePullThroughCacheRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLifecyclePolicyResponse:
    boto3_raw_data: "type_defs.DeleteLifecyclePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    registryId = field("registryId")
    repositoryName = field("repositoryName")
    lifecyclePolicyText = field("lifecyclePolicyText")
    lastEvaluatedAt = field("lastEvaluatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteLifecyclePolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLifecyclePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePullThroughCacheRuleResponse:
    boto3_raw_data: "type_defs.DeletePullThroughCacheRuleResponseTypeDef" = (
        dataclasses.field()
    )

    ecrRepositoryPrefix = field("ecrRepositoryPrefix")
    upstreamRegistryUrl = field("upstreamRegistryUrl")
    createdAt = field("createdAt")
    registryId = field("registryId")
    credentialArn = field("credentialArn")
    customRoleArn = field("customRoleArn")
    upstreamRepositoryPrefix = field("upstreamRepositoryPrefix")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeletePullThroughCacheRuleResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePullThroughCacheRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRegistryPolicyResponse:
    boto3_raw_data: "type_defs.DeleteRegistryPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    registryId = field("registryId")
    policyText = field("policyText")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRegistryPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRegistryPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRepositoryPolicyResponse:
    boto3_raw_data: "type_defs.DeleteRepositoryPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    registryId = field("registryId")
    repositoryName = field("repositoryName")
    policyText = field("policyText")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteRepositoryPolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRepositoryPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountSettingResponse:
    boto3_raw_data: "type_defs.GetAccountSettingResponseTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccountSettingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountSettingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAuthorizationTokenResponse:
    boto3_raw_data: "type_defs.GetAuthorizationTokenResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def authorizationData(self):  # pragma: no cover
        return AuthorizationData.make_many(self.boto3_raw_data["authorizationData"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAuthorizationTokenResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAuthorizationTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDownloadUrlForLayerResponse:
    boto3_raw_data: "type_defs.GetDownloadUrlForLayerResponseTypeDef" = (
        dataclasses.field()
    )

    downloadUrl = field("downloadUrl")
    layerDigest = field("layerDigest")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDownloadUrlForLayerResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDownloadUrlForLayerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLifecyclePolicyResponse:
    boto3_raw_data: "type_defs.GetLifecyclePolicyResponseTypeDef" = dataclasses.field()

    registryId = field("registryId")
    repositoryName = field("repositoryName")
    lifecyclePolicyText = field("lifecyclePolicyText")
    lastEvaluatedAt = field("lastEvaluatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLifecyclePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLifecyclePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRegistryPolicyResponse:
    boto3_raw_data: "type_defs.GetRegistryPolicyResponseTypeDef" = dataclasses.field()

    registryId = field("registryId")
    policyText = field("policyText")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRegistryPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRegistryPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRepositoryPolicyResponse:
    boto3_raw_data: "type_defs.GetRepositoryPolicyResponseTypeDef" = dataclasses.field()

    registryId = field("registryId")
    repositoryName = field("repositoryName")
    policyText = field("policyText")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRepositoryPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRepositoryPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InitiateLayerUploadResponse:
    boto3_raw_data: "type_defs.InitiateLayerUploadResponseTypeDef" = dataclasses.field()

    uploadId = field("uploadId")
    partSize = field("partSize")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InitiateLayerUploadResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InitiateLayerUploadResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAccountSettingResponse:
    boto3_raw_data: "type_defs.PutAccountSettingResponseTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAccountSettingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccountSettingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutLifecyclePolicyResponse:
    boto3_raw_data: "type_defs.PutLifecyclePolicyResponseTypeDef" = dataclasses.field()

    registryId = field("registryId")
    repositoryName = field("repositoryName")
    lifecyclePolicyText = field("lifecyclePolicyText")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutLifecyclePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutLifecyclePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRegistryPolicyResponse:
    boto3_raw_data: "type_defs.PutRegistryPolicyResponseTypeDef" = dataclasses.field()

    registryId = field("registryId")
    policyText = field("policyText")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutRegistryPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRegistryPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetRepositoryPolicyResponse:
    boto3_raw_data: "type_defs.SetRepositoryPolicyResponseTypeDef" = dataclasses.field()

    registryId = field("registryId")
    repositoryName = field("repositoryName")
    policyText = field("policyText")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetRepositoryPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetRepositoryPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartLifecyclePolicyPreviewResponse:
    boto3_raw_data: "type_defs.StartLifecyclePolicyPreviewResponseTypeDef" = (
        dataclasses.field()
    )

    registryId = field("registryId")
    repositoryName = field("repositoryName")
    lifecyclePolicyText = field("lifecyclePolicyText")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartLifecyclePolicyPreviewResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartLifecyclePolicyPreviewResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePullThroughCacheRuleResponse:
    boto3_raw_data: "type_defs.UpdatePullThroughCacheRuleResponseTypeDef" = (
        dataclasses.field()
    )

    ecrRepositoryPrefix = field("ecrRepositoryPrefix")
    registryId = field("registryId")
    updatedAt = field("updatedAt")
    credentialArn = field("credentialArn")
    customRoleArn = field("customRoleArn")
    upstreamRepositoryPrefix = field("upstreamRepositoryPrefix")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePullThroughCacheRuleResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePullThroughCacheRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadLayerPartResponse:
    boto3_raw_data: "type_defs.UploadLayerPartResponseTypeDef" = dataclasses.field()

    registryId = field("registryId")
    repositoryName = field("repositoryName")
    uploadId = field("uploadId")
    lastByteReceived = field("lastByteReceived")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UploadLayerPartResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadLayerPartResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidatePullThroughCacheRuleResponse:
    boto3_raw_data: "type_defs.ValidatePullThroughCacheRuleResponseTypeDef" = (
        dataclasses.field()
    )

    ecrRepositoryPrefix = field("ecrRepositoryPrefix")
    registryId = field("registryId")
    upstreamRegistryUrl = field("upstreamRegistryUrl")
    credentialArn = field("credentialArn")
    customRoleArn = field("customRoleArn")
    upstreamRepositoryPrefix = field("upstreamRepositoryPrefix")
    isValid = field("isValid")
    failure = field("failure")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ValidatePullThroughCacheRuleResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidatePullThroughCacheRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteImageRequest:
    boto3_raw_data: "type_defs.BatchDeleteImageRequestTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")

    @cached_property
    def imageIds(self):  # pragma: no cover
        return ImageIdentifier.make_many(self.boto3_raw_data["imageIds"])

    registryId = field("registryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteImageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteImageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetImageRequest:
    boto3_raw_data: "type_defs.BatchGetImageRequestTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")

    @cached_property
    def imageIds(self):  # pragma: no cover
        return ImageIdentifier.make_many(self.boto3_raw_data["imageIds"])

    registryId = field("registryId")
    acceptedMediaTypes = field("acceptedMediaTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetImageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetImageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImageReplicationStatusRequest:
    boto3_raw_data: "type_defs.DescribeImageReplicationStatusRequestTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")

    @cached_property
    def imageId(self):  # pragma: no cover
        return ImageIdentifier.make_one(self.boto3_raw_data["imageId"])

    registryId = field("registryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeImageReplicationStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImageReplicationStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImageScanFindingsRequest:
    boto3_raw_data: "type_defs.DescribeImageScanFindingsRequestTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")

    @cached_property
    def imageId(self):  # pragma: no cover
        return ImageIdentifier.make_one(self.boto3_raw_data["imageId"])

    registryId = field("registryId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeImageScanFindingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImageScanFindingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageFailure:
    boto3_raw_data: "type_defs.ImageFailureTypeDef" = dataclasses.field()

    @cached_property
    def imageId(self):  # pragma: no cover
        return ImageIdentifier.make_one(self.boto3_raw_data["imageId"])

    failureCode = field("failureCode")
    failureReason = field("failureReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageFailureTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageFailureTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Image:
    boto3_raw_data: "type_defs.ImageTypeDef" = dataclasses.field()

    registryId = field("registryId")
    repositoryName = field("repositoryName")

    @cached_property
    def imageId(self):  # pragma: no cover
        return ImageIdentifier.make_one(self.boto3_raw_data["imageId"])

    imageManifest = field("imageManifest")
    imageManifestMediaType = field("imageManifestMediaType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImagesResponse:
    boto3_raw_data: "type_defs.ListImagesResponseTypeDef" = dataclasses.field()

    @cached_property
    def imageIds(self):  # pragma: no cover
        return ImageIdentifier.make_many(self.boto3_raw_data["imageIds"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImagesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartImageScanRequest:
    boto3_raw_data: "type_defs.StartImageScanRequestTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")

    @cached_property
    def imageId(self):  # pragma: no cover
        return ImageIdentifier.make_one(self.boto3_raw_data["imageId"])

    registryId = field("registryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartImageScanRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartImageScanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadLayerPartRequest:
    boto3_raw_data: "type_defs.UploadLayerPartRequestTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    uploadId = field("uploadId")
    partFirstByte = field("partFirstByte")
    partLastByte = field("partLastByte")
    layerPartBlob = field("layerPartBlob")
    registryId = field("registryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UploadLayerPartRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadLayerPartRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutImageTagMutabilityRequest:
    boto3_raw_data: "type_defs.PutImageTagMutabilityRequestTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    imageTagMutability = field("imageTagMutability")
    registryId = field("registryId")

    @cached_property
    def imageTagMutabilityExclusionFilters(self):  # pragma: no cover
        return ImageTagMutabilityExclusionFilter.make_many(
            self.boto3_raw_data["imageTagMutabilityExclusionFilters"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutImageTagMutabilityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutImageTagMutabilityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutImageTagMutabilityResponse:
    boto3_raw_data: "type_defs.PutImageTagMutabilityResponseTypeDef" = (
        dataclasses.field()
    )

    registryId = field("registryId")
    repositoryName = field("repositoryName")
    imageTagMutability = field("imageTagMutability")

    @cached_property
    def imageTagMutabilityExclusionFilters(self):  # pragma: no cover
        return ImageTagMutabilityExclusionFilter.make_many(
            self.boto3_raw_data["imageTagMutabilityExclusionFilters"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutImageTagMutabilityResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutImageTagMutabilityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRepositoryCreationTemplateRequest:
    boto3_raw_data: "type_defs.CreateRepositoryCreationTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    prefix = field("prefix")
    appliedFor = field("appliedFor")
    description = field("description")

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfigurationForRepositoryCreationTemplate.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    @cached_property
    def resourceTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["resourceTags"])

    imageTagMutability = field("imageTagMutability")

    @cached_property
    def imageTagMutabilityExclusionFilters(self):  # pragma: no cover
        return ImageTagMutabilityExclusionFilter.make_many(
            self.boto3_raw_data["imageTagMutabilityExclusionFilters"]
        )

    repositoryPolicy = field("repositoryPolicy")
    lifecyclePolicy = field("lifecyclePolicy")
    customRoleArn = field("customRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRepositoryCreationTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRepositoryCreationTemplateRequestTypeDef"]
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
class RepositoryCreationTemplate:
    boto3_raw_data: "type_defs.RepositoryCreationTemplateTypeDef" = dataclasses.field()

    prefix = field("prefix")
    description = field("description")

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfigurationForRepositoryCreationTemplate.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    @cached_property
    def resourceTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["resourceTags"])

    imageTagMutability = field("imageTagMutability")

    @cached_property
    def imageTagMutabilityExclusionFilters(self):  # pragma: no cover
        return ImageTagMutabilityExclusionFilter.make_many(
            self.boto3_raw_data["imageTagMutabilityExclusionFilters"]
        )

    repositoryPolicy = field("repositoryPolicy")
    lifecyclePolicy = field("lifecyclePolicy")
    appliedFor = field("appliedFor")
    customRoleArn = field("customRoleArn")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RepositoryCreationTemplateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositoryCreationTemplateTypeDef"]
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
class UpdateRepositoryCreationTemplateRequest:
    boto3_raw_data: "type_defs.UpdateRepositoryCreationTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    prefix = field("prefix")
    description = field("description")

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfigurationForRepositoryCreationTemplate.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    @cached_property
    def resourceTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["resourceTags"])

    imageTagMutability = field("imageTagMutability")

    @cached_property
    def imageTagMutabilityExclusionFilters(self):  # pragma: no cover
        return ImageTagMutabilityExclusionFilter.make_many(
            self.boto3_raw_data["imageTagMutabilityExclusionFilters"]
        )

    repositoryPolicy = field("repositoryPolicy")
    lifecyclePolicy = field("lifecyclePolicy")
    appliedFor = field("appliedFor")
    customRoleArn = field("customRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateRepositoryCreationTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRepositoryCreationTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRepositoryRequest:
    boto3_raw_data: "type_defs.CreateRepositoryRequestTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    registryId = field("registryId")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    imageTagMutability = field("imageTagMutability")

    @cached_property
    def imageTagMutabilityExclusionFilters(self):  # pragma: no cover
        return ImageTagMutabilityExclusionFilter.make_many(
            self.boto3_raw_data["imageTagMutabilityExclusionFilters"]
        )

    @cached_property
    def imageScanningConfiguration(self):  # pragma: no cover
        return ImageScanningConfiguration.make_one(
            self.boto3_raw_data["imageScanningConfiguration"]
        )

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRepositoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRepositoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutImageScanningConfigurationRequest:
    boto3_raw_data: "type_defs.PutImageScanningConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")

    @cached_property
    def imageScanningConfiguration(self):  # pragma: no cover
        return ImageScanningConfiguration.make_one(
            self.boto3_raw_data["imageScanningConfiguration"]
        )

    registryId = field("registryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutImageScanningConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutImageScanningConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutImageScanningConfigurationResponse:
    boto3_raw_data: "type_defs.PutImageScanningConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    registryId = field("registryId")
    repositoryName = field("repositoryName")

    @cached_property
    def imageScanningConfiguration(self):  # pragma: no cover
        return ImageScanningConfiguration.make_one(
            self.boto3_raw_data["imageScanningConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutImageScanningConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutImageScanningConfigurationResponseTypeDef"]
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

    repositoryArn = field("repositoryArn")
    registryId = field("registryId")
    repositoryName = field("repositoryName")
    repositoryUri = field("repositoryUri")
    createdAt = field("createdAt")
    imageTagMutability = field("imageTagMutability")

    @cached_property
    def imageTagMutabilityExclusionFilters(self):  # pragma: no cover
        return ImageTagMutabilityExclusionFilter.make_many(
            self.boto3_raw_data["imageTagMutabilityExclusionFilters"]
        )

    @cached_property
    def imageScanningConfiguration(self):  # pragma: no cover
        return ImageScanningConfiguration.make_one(
            self.boto3_raw_data["imageScanningConfiguration"]
        )

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

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
class CvssScoreDetails:
    boto3_raw_data: "type_defs.CvssScoreDetailsTypeDef" = dataclasses.field()

    @cached_property
    def adjustments(self):  # pragma: no cover
        return CvssScoreAdjustment.make_many(self.boto3_raw_data["adjustments"])

    score = field("score")
    scoreSource = field("scoreSource")
    scoringVector = field("scoringVector")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CvssScoreDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CvssScoreDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImageReplicationStatusResponse:
    boto3_raw_data: "type_defs.DescribeImageReplicationStatusResponseTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")

    @cached_property
    def imageId(self):  # pragma: no cover
        return ImageIdentifier.make_one(self.boto3_raw_data["imageId"])

    @cached_property
    def replicationStatuses(self):  # pragma: no cover
        return ImageReplicationStatus.make_many(
            self.boto3_raw_data["replicationStatuses"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeImageReplicationStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImageReplicationStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImageScanFindingsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeImageScanFindingsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")

    @cached_property
    def imageId(self):  # pragma: no cover
        return ImageIdentifier.make_one(self.boto3_raw_data["imageId"])

    registryId = field("registryId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeImageScanFindingsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImageScanFindingsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePullThroughCacheRulesRequestPaginate:
    boto3_raw_data: "type_defs.DescribePullThroughCacheRulesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    registryId = field("registryId")
    ecrRepositoryPrefixes = field("ecrRepositoryPrefixes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePullThroughCacheRulesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePullThroughCacheRulesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRepositoriesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeRepositoriesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    registryId = field("registryId")
    repositoryNames = field("repositoryNames")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRepositoriesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRepositoriesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRepositoryCreationTemplatesRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeRepositoryCreationTemplatesRequestPaginateTypeDef"
    ) = dataclasses.field()

    prefixes = field("prefixes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRepositoryCreationTemplatesRequestPaginateTypeDef"
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
                "type_defs.DescribeRepositoryCreationTemplatesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImageScanFindingsRequestWait:
    boto3_raw_data: "type_defs.DescribeImageScanFindingsRequestWaitTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")

    @cached_property
    def imageId(self):  # pragma: no cover
        return ImageIdentifier.make_one(self.boto3_raw_data["imageId"])

    registryId = field("registryId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeImageScanFindingsRequestWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImageScanFindingsRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartImageScanResponse:
    boto3_raw_data: "type_defs.StartImageScanResponseTypeDef" = dataclasses.field()

    registryId = field("registryId")
    repositoryName = field("repositoryName")

    @cached_property
    def imageId(self):  # pragma: no cover
        return ImageIdentifier.make_one(self.boto3_raw_data["imageId"])

    @cached_property
    def imageScanStatus(self):  # pragma: no cover
        return ImageScanStatus.make_one(self.boto3_raw_data["imageScanStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartImageScanResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartImageScanResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImagesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeImagesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    registryId = field("registryId")

    @cached_property
    def imageIds(self):  # pragma: no cover
        return ImageIdentifier.make_many(self.boto3_raw_data["imageIds"])

    @cached_property
    def filter(self):  # pragma: no cover
        return DescribeImagesFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeImagesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImagesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImagesRequest:
    boto3_raw_data: "type_defs.DescribeImagesRequestTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    registryId = field("registryId")

    @cached_property
    def imageIds(self):  # pragma: no cover
        return ImageIdentifier.make_many(self.boto3_raw_data["imageIds"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filter(self):  # pragma: no cover
        return DescribeImagesFilter.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeImagesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePullThroughCacheRulesResponse:
    boto3_raw_data: "type_defs.DescribePullThroughCacheRulesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def pullThroughCacheRules(self):  # pragma: no cover
        return PullThroughCacheRule.make_many(
            self.boto3_raw_data["pullThroughCacheRules"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePullThroughCacheRulesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePullThroughCacheRulesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLifecyclePolicyPreviewRequestPaginate:
    boto3_raw_data: "type_defs.GetLifecyclePolicyPreviewRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    registryId = field("registryId")

    @cached_property
    def imageIds(self):  # pragma: no cover
        return ImageIdentifier.make_many(self.boto3_raw_data["imageIds"])

    @cached_property
    def filter(self):  # pragma: no cover
        return LifecyclePolicyPreviewFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetLifecyclePolicyPreviewRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLifecyclePolicyPreviewRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLifecyclePolicyPreviewRequest:
    boto3_raw_data: "type_defs.GetLifecyclePolicyPreviewRequestTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    registryId = field("registryId")

    @cached_property
    def imageIds(self):  # pragma: no cover
        return ImageIdentifier.make_many(self.boto3_raw_data["imageIds"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filter(self):  # pragma: no cover
        return LifecyclePolicyPreviewFilter.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLifecyclePolicyPreviewRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLifecyclePolicyPreviewRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLifecyclePolicyPreviewRequestWait:
    boto3_raw_data: "type_defs.GetLifecyclePolicyPreviewRequestWaitTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    registryId = field("registryId")

    @cached_property
    def imageIds(self):  # pragma: no cover
        return ImageIdentifier.make_many(self.boto3_raw_data["imageIds"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filter(self):  # pragma: no cover
        return LifecyclePolicyPreviewFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetLifecyclePolicyPreviewRequestWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLifecyclePolicyPreviewRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageDetail:
    boto3_raw_data: "type_defs.ImageDetailTypeDef" = dataclasses.field()

    registryId = field("registryId")
    repositoryName = field("repositoryName")
    imageDigest = field("imageDigest")
    imageTags = field("imageTags")
    imageSizeInBytes = field("imageSizeInBytes")
    imagePushedAt = field("imagePushedAt")

    @cached_property
    def imageScanStatus(self):  # pragma: no cover
        return ImageScanStatus.make_one(self.boto3_raw_data["imageScanStatus"])

    @cached_property
    def imageScanFindingsSummary(self):  # pragma: no cover
        return ImageScanFindingsSummary.make_one(
            self.boto3_raw_data["imageScanFindingsSummary"]
        )

    imageManifestMediaType = field("imageManifestMediaType")
    artifactMediaType = field("artifactMediaType")
    lastRecordedPullTime = field("lastRecordedPullTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageDetailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicyPreviewResult:
    boto3_raw_data: "type_defs.LifecyclePolicyPreviewResultTypeDef" = (
        dataclasses.field()
    )

    imageTags = field("imageTags")
    imageDigest = field("imageDigest")
    imagePushedAt = field("imagePushedAt")

    @cached_property
    def action(self):  # pragma: no cover
        return LifecyclePolicyRuleAction.make_one(self.boto3_raw_data["action"])

    appliedRulePriority = field("appliedRulePriority")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecyclePolicyPreviewResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicyPreviewResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImagesRequestPaginate:
    boto3_raw_data: "type_defs.ListImagesRequestPaginateTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    registryId = field("registryId")

    @cached_property
    def filter(self):  # pragma: no cover
        return ListImagesFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImagesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImagesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImagesRequest:
    boto3_raw_data: "type_defs.ListImagesRequestTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    registryId = field("registryId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filter(self):  # pragma: no cover
        return ListImagesFilter.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListImagesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageVulnerabilityDetails:
    boto3_raw_data: "type_defs.PackageVulnerabilityDetailsTypeDef" = dataclasses.field()

    @cached_property
    def cvss(self):  # pragma: no cover
        return CvssScore.make_many(self.boto3_raw_data["cvss"])

    referenceUrls = field("referenceUrls")
    relatedVulnerabilities = field("relatedVulnerabilities")
    source = field("source")
    sourceUrl = field("sourceUrl")
    vendorCreatedAt = field("vendorCreatedAt")
    vendorSeverity = field("vendorSeverity")
    vendorUpdatedAt = field("vendorUpdatedAt")
    vulnerabilityId = field("vulnerabilityId")

    @cached_property
    def vulnerablePackages(self):  # pragma: no cover
        return VulnerablePackage.make_many(self.boto3_raw_data["vulnerablePackages"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageVulnerabilityDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageVulnerabilityDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Remediation:
    boto3_raw_data: "type_defs.RemediationTypeDef" = dataclasses.field()

    @cached_property
    def recommendation(self):  # pragma: no cover
        return Recommendation.make_one(self.boto3_raw_data["recommendation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RemediationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RemediationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistryScanningRuleOutput:
    boto3_raw_data: "type_defs.RegistryScanningRuleOutputTypeDef" = dataclasses.field()

    scanFrequency = field("scanFrequency")

    @cached_property
    def repositoryFilters(self):  # pragma: no cover
        return ScanningRepositoryFilter.make_many(
            self.boto3_raw_data["repositoryFilters"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegistryScanningRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistryScanningRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistryScanningRule:
    boto3_raw_data: "type_defs.RegistryScanningRuleTypeDef" = dataclasses.field()

    scanFrequency = field("scanFrequency")

    @cached_property
    def repositoryFilters(self):  # pragma: no cover
        return ScanningRepositoryFilter.make_many(
            self.boto3_raw_data["repositoryFilters"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegistryScanningRuleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistryScanningRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositoryScanningConfiguration:
    boto3_raw_data: "type_defs.RepositoryScanningConfigurationTypeDef" = (
        dataclasses.field()
    )

    repositoryArn = field("repositoryArn")
    repositoryName = field("repositoryName")
    scanOnPush = field("scanOnPush")
    scanFrequency = field("scanFrequency")

    @cached_property
    def appliedScanFilters(self):  # pragma: no cover
        return ScanningRepositoryFilter.make_many(
            self.boto3_raw_data["appliedScanFilters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RepositoryScanningConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositoryScanningConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationRuleOutput:
    boto3_raw_data: "type_defs.ReplicationRuleOutputTypeDef" = dataclasses.field()

    @cached_property
    def destinations(self):  # pragma: no cover
        return ReplicationDestination.make_many(self.boto3_raw_data["destinations"])

    @cached_property
    def repositoryFilters(self):  # pragma: no cover
        return RepositoryFilter.make_many(self.boto3_raw_data["repositoryFilters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationRule:
    boto3_raw_data: "type_defs.ReplicationRuleTypeDef" = dataclasses.field()

    @cached_property
    def destinations(self):  # pragma: no cover
        return ReplicationDestination.make_many(self.boto3_raw_data["destinations"])

    @cached_property
    def repositoryFilters(self):  # pragma: no cover
        return RepositoryFilter.make_many(self.boto3_raw_data["repositoryFilters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReplicationRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReplicationRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Resource:
    boto3_raw_data: "type_defs.ResourceTypeDef" = dataclasses.field()

    @cached_property
    def details(self):  # pragma: no cover
        return ResourceDetails.make_one(self.boto3_raw_data["details"])

    id = field("id")
    tags = field("tags")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteImageResponse:
    boto3_raw_data: "type_defs.BatchDeleteImageResponseTypeDef" = dataclasses.field()

    @cached_property
    def imageIds(self):  # pragma: no cover
        return ImageIdentifier.make_many(self.boto3_raw_data["imageIds"])

    @cached_property
    def failures(self):  # pragma: no cover
        return ImageFailure.make_many(self.boto3_raw_data["failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteImageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteImageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetImageResponse:
    boto3_raw_data: "type_defs.BatchGetImageResponseTypeDef" = dataclasses.field()

    @cached_property
    def images(self):  # pragma: no cover
        return Image.make_many(self.boto3_raw_data["images"])

    @cached_property
    def failures(self):  # pragma: no cover
        return ImageFailure.make_many(self.boto3_raw_data["failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetImageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetImageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutImageResponse:
    boto3_raw_data: "type_defs.PutImageResponseTypeDef" = dataclasses.field()

    @cached_property
    def image(self):  # pragma: no cover
        return Image.make_one(self.boto3_raw_data["image"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutImageResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutImageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRepositoryCreationTemplateResponse:
    boto3_raw_data: "type_defs.CreateRepositoryCreationTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    registryId = field("registryId")

    @cached_property
    def repositoryCreationTemplate(self):  # pragma: no cover
        return RepositoryCreationTemplate.make_one(
            self.boto3_raw_data["repositoryCreationTemplate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRepositoryCreationTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRepositoryCreationTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRepositoryCreationTemplateResponse:
    boto3_raw_data: "type_defs.DeleteRepositoryCreationTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    registryId = field("registryId")

    @cached_property
    def repositoryCreationTemplate(self):  # pragma: no cover
        return RepositoryCreationTemplate.make_one(
            self.boto3_raw_data["repositoryCreationTemplate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRepositoryCreationTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRepositoryCreationTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRepositoryCreationTemplatesResponse:
    boto3_raw_data: "type_defs.DescribeRepositoryCreationTemplatesResponseTypeDef" = (
        dataclasses.field()
    )

    registryId = field("registryId")

    @cached_property
    def repositoryCreationTemplates(self):  # pragma: no cover
        return RepositoryCreationTemplate.make_many(
            self.boto3_raw_data["repositoryCreationTemplates"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRepositoryCreationTemplatesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRepositoryCreationTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRepositoryCreationTemplateResponse:
    boto3_raw_data: "type_defs.UpdateRepositoryCreationTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    registryId = field("registryId")

    @cached_property
    def repositoryCreationTemplate(self):  # pragma: no cover
        return RepositoryCreationTemplate.make_one(
            self.boto3_raw_data["repositoryCreationTemplate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateRepositoryCreationTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRepositoryCreationTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRepositoryResponse:
    boto3_raw_data: "type_defs.CreateRepositoryResponseTypeDef" = dataclasses.field()

    @cached_property
    def repository(self):  # pragma: no cover
        return Repository.make_one(self.boto3_raw_data["repository"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRepositoryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRepositoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRepositoryResponse:
    boto3_raw_data: "type_defs.DeleteRepositoryResponseTypeDef" = dataclasses.field()

    @cached_property
    def repository(self):  # pragma: no cover
        return Repository.make_one(self.boto3_raw_data["repository"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRepositoryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRepositoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRepositoriesResponse:
    boto3_raw_data: "type_defs.DescribeRepositoriesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def repositories(self):  # pragma: no cover
        return Repository.make_many(self.boto3_raw_data["repositories"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRepositoriesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRepositoriesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScoreDetails:
    boto3_raw_data: "type_defs.ScoreDetailsTypeDef" = dataclasses.field()

    @cached_property
    def cvss(self):  # pragma: no cover
        return CvssScoreDetails.make_one(self.boto3_raw_data["cvss"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScoreDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScoreDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImagesResponse:
    boto3_raw_data: "type_defs.DescribeImagesResponseTypeDef" = dataclasses.field()

    @cached_property
    def imageDetails(self):  # pragma: no cover
        return ImageDetail.make_many(self.boto3_raw_data["imageDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeImagesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLifecyclePolicyPreviewResponse:
    boto3_raw_data: "type_defs.GetLifecyclePolicyPreviewResponseTypeDef" = (
        dataclasses.field()
    )

    registryId = field("registryId")
    repositoryName = field("repositoryName")
    lifecyclePolicyText = field("lifecyclePolicyText")
    status = field("status")

    @cached_property
    def previewResults(self):  # pragma: no cover
        return LifecyclePolicyPreviewResult.make_many(
            self.boto3_raw_data["previewResults"]
        )

    @cached_property
    def summary(self):  # pragma: no cover
        return LifecyclePolicyPreviewSummary.make_one(self.boto3_raw_data["summary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetLifecyclePolicyPreviewResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLifecyclePolicyPreviewResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistryScanningConfiguration:
    boto3_raw_data: "type_defs.RegistryScanningConfigurationTypeDef" = (
        dataclasses.field()
    )

    scanType = field("scanType")

    @cached_property
    def rules(self):  # pragma: no cover
        return RegistryScanningRuleOutput.make_many(self.boto3_raw_data["rules"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegistryScanningConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistryScanningConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetRepositoryScanningConfigurationResponse:
    boto3_raw_data: (
        "type_defs.BatchGetRepositoryScanningConfigurationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def scanningConfigurations(self):  # pragma: no cover
        return RepositoryScanningConfiguration.make_many(
            self.boto3_raw_data["scanningConfigurations"]
        )

    @cached_property
    def failures(self):  # pragma: no cover
        return RepositoryScanningConfigurationFailure.make_many(
            self.boto3_raw_data["failures"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetRepositoryScanningConfigurationResponseTypeDef"
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
                "type_defs.BatchGetRepositoryScanningConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationConfigurationOutput:
    boto3_raw_data: "type_defs.ReplicationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def rules(self):  # pragma: no cover
        return ReplicationRuleOutput.make_many(self.boto3_raw_data["rules"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReplicationConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationConfiguration:
    boto3_raw_data: "type_defs.ReplicationConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def rules(self):  # pragma: no cover
        return ReplicationRule.make_many(self.boto3_raw_data["rules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnhancedImageScanFinding:
    boto3_raw_data: "type_defs.EnhancedImageScanFindingTypeDef" = dataclasses.field()

    awsAccountId = field("awsAccountId")
    description = field("description")
    findingArn = field("findingArn")
    firstObservedAt = field("firstObservedAt")
    lastObservedAt = field("lastObservedAt")

    @cached_property
    def packageVulnerabilityDetails(self):  # pragma: no cover
        return PackageVulnerabilityDetails.make_one(
            self.boto3_raw_data["packageVulnerabilityDetails"]
        )

    @cached_property
    def remediation(self):  # pragma: no cover
        return Remediation.make_one(self.boto3_raw_data["remediation"])

    @cached_property
    def resources(self):  # pragma: no cover
        return Resource.make_many(self.boto3_raw_data["resources"])

    score = field("score")

    @cached_property
    def scoreDetails(self):  # pragma: no cover
        return ScoreDetails.make_one(self.boto3_raw_data["scoreDetails"])

    severity = field("severity")
    status = field("status")
    title = field("title")
    type = field("type")
    updatedAt = field("updatedAt")
    fixAvailable = field("fixAvailable")
    exploitAvailable = field("exploitAvailable")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnhancedImageScanFindingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnhancedImageScanFindingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRegistryScanningConfigurationResponse:
    boto3_raw_data: "type_defs.GetRegistryScanningConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    registryId = field("registryId")

    @cached_property
    def scanningConfiguration(self):  # pragma: no cover
        return RegistryScanningConfiguration.make_one(
            self.boto3_raw_data["scanningConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRegistryScanningConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRegistryScanningConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRegistryScanningConfigurationResponse:
    boto3_raw_data: "type_defs.PutRegistryScanningConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def registryScanningConfiguration(self):  # pragma: no cover
        return RegistryScanningConfiguration.make_one(
            self.boto3_raw_data["registryScanningConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutRegistryScanningConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRegistryScanningConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRegistryScanningConfigurationRequest:
    boto3_raw_data: "type_defs.PutRegistryScanningConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    scanType = field("scanType")
    rules = field("rules")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutRegistryScanningConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRegistryScanningConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegistryResponse:
    boto3_raw_data: "type_defs.DescribeRegistryResponseTypeDef" = dataclasses.field()

    registryId = field("registryId")

    @cached_property
    def replicationConfiguration(self):  # pragma: no cover
        return ReplicationConfigurationOutput.make_one(
            self.boto3_raw_data["replicationConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRegistryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRegistryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutReplicationConfigurationResponse:
    boto3_raw_data: "type_defs.PutReplicationConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def replicationConfiguration(self):  # pragma: no cover
        return ReplicationConfigurationOutput.make_one(
            self.boto3_raw_data["replicationConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutReplicationConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutReplicationConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageScanFindings:
    boto3_raw_data: "type_defs.ImageScanFindingsTypeDef" = dataclasses.field()

    imageScanCompletedAt = field("imageScanCompletedAt")
    vulnerabilitySourceUpdatedAt = field("vulnerabilitySourceUpdatedAt")
    findingSeverityCounts = field("findingSeverityCounts")

    @cached_property
    def findings(self):  # pragma: no cover
        return ImageScanFinding.make_many(self.boto3_raw_data["findings"])

    @cached_property
    def enhancedFindings(self):  # pragma: no cover
        return EnhancedImageScanFinding.make_many(
            self.boto3_raw_data["enhancedFindings"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageScanFindingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageScanFindingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutReplicationConfigurationRequest:
    boto3_raw_data: "type_defs.PutReplicationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    replicationConfiguration = field("replicationConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutReplicationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutReplicationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImageScanFindingsResponse:
    boto3_raw_data: "type_defs.DescribeImageScanFindingsResponseTypeDef" = (
        dataclasses.field()
    )

    registryId = field("registryId")
    repositoryName = field("repositoryName")

    @cached_property
    def imageId(self):  # pragma: no cover
        return ImageIdentifier.make_one(self.boto3_raw_data["imageId"])

    @cached_property
    def imageScanStatus(self):  # pragma: no cover
        return ImageScanStatus.make_one(self.boto3_raw_data["imageScanStatus"])

    @cached_property
    def imageScanFindings(self):  # pragma: no cover
        return ImageScanFindings.make_one(self.boto3_raw_data["imageScanFindings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeImageScanFindingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImageScanFindingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
