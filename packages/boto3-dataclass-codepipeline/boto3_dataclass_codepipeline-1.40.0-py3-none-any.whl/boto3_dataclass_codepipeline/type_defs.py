# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_codepipeline import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AWSSessionCredentials:
    boto3_raw_data: "type_defs.AWSSessionCredentialsTypeDef" = dataclasses.field()

    accessKeyId = field("accessKeyId")
    secretAccessKey = field("secretAccessKey")
    sessionToken = field("sessionToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AWSSessionCredentialsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AWSSessionCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcknowledgeJobInput:
    boto3_raw_data: "type_defs.AcknowledgeJobInputTypeDef" = dataclasses.field()

    jobId = field("jobId")
    nonce = field("nonce")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcknowledgeJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcknowledgeJobInputTypeDef"]
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
class AcknowledgeThirdPartyJobInput:
    boto3_raw_data: "type_defs.AcknowledgeThirdPartyJobInputTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")
    nonce = field("nonce")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AcknowledgeThirdPartyJobInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcknowledgeThirdPartyJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionConfigurationProperty:
    boto3_raw_data: "type_defs.ActionConfigurationPropertyTypeDef" = dataclasses.field()

    name = field("name")
    required = field("required")
    key = field("key")
    secret = field("secret")
    queryable = field("queryable")
    description = field("description")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionConfigurationPropertyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionConfigurationPropertyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionConfiguration:
    boto3_raw_data: "type_defs.ActionConfigurationTypeDef" = dataclasses.field()

    configuration = field("configuration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionContext:
    boto3_raw_data: "type_defs.ActionContextTypeDef" = dataclasses.field()

    name = field("name")
    actionExecutionId = field("actionExecutionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionContextTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionContextTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionTypeId:
    boto3_raw_data: "type_defs.ActionTypeIdTypeDef" = dataclasses.field()

    category = field("category")
    owner = field("owner")
    provider = field("provider")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionTypeIdTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionTypeIdTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentVariable:
    boto3_raw_data: "type_defs.EnvironmentVariableTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentVariableTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentVariableTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputArtifact:
    boto3_raw_data: "type_defs.InputArtifactTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputArtifactTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputArtifactTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputArtifactOutput:
    boto3_raw_data: "type_defs.OutputArtifactOutputTypeDef" = dataclasses.field()

    name = field("name")
    files = field("files")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutputArtifactOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputArtifactOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputArtifact:
    boto3_raw_data: "type_defs.OutputArtifactTypeDef" = dataclasses.field()

    name = field("name")
    files = field("files")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputArtifactTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputArtifactTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LatestInPipelineExecutionFilter:
    boto3_raw_data: "type_defs.LatestInPipelineExecutionFilterTypeDef" = (
        dataclasses.field()
    )

    pipelineExecutionId = field("pipelineExecutionId")
    startTimeRange = field("startTimeRange")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LatestInPipelineExecutionFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LatestInPipelineExecutionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorDetails:
    boto3_raw_data: "type_defs.ErrorDetailsTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionRevisionOutput:
    boto3_raw_data: "type_defs.ActionRevisionOutputTypeDef" = dataclasses.field()

    revisionId = field("revisionId")
    revisionChangeId = field("revisionChangeId")
    created = field("created")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionRevisionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionRevisionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionTypeArtifactDetails:
    boto3_raw_data: "type_defs.ActionTypeArtifactDetailsTypeDef" = dataclasses.field()

    minimumCount = field("minimumCount")
    maximumCount = field("maximumCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionTypeArtifactDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionTypeArtifactDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionTypeIdentifier:
    boto3_raw_data: "type_defs.ActionTypeIdentifierTypeDef" = dataclasses.field()

    category = field("category")
    owner = field("owner")
    provider = field("provider")
    version = field("version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionTypeIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionTypeIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionTypePermissionsOutput:
    boto3_raw_data: "type_defs.ActionTypePermissionsOutputTypeDef" = dataclasses.field()

    allowedAccounts = field("allowedAccounts")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionTypePermissionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionTypePermissionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionTypeProperty:
    boto3_raw_data: "type_defs.ActionTypePropertyTypeDef" = dataclasses.field()

    name = field("name")
    optional = field("optional")
    key = field("key")
    noEcho = field("noEcho")
    queryable = field("queryable")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionTypePropertyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionTypePropertyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionTypeUrls:
    boto3_raw_data: "type_defs.ActionTypeUrlsTypeDef" = dataclasses.field()

    configurationUrl = field("configurationUrl")
    entityUrlTemplate = field("entityUrlTemplate")
    executionUrlTemplate = field("executionUrlTemplate")
    revisionUrlTemplate = field("revisionUrlTemplate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionTypeUrlsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionTypeUrlsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionTypePermissions:
    boto3_raw_data: "type_defs.ActionTypePermissionsTypeDef" = dataclasses.field()

    allowedAccounts = field("allowedAccounts")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionTypePermissionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionTypePermissionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionTypeSettings:
    boto3_raw_data: "type_defs.ActionTypeSettingsTypeDef" = dataclasses.field()

    thirdPartyConfigurationUrl = field("thirdPartyConfigurationUrl")
    entityUrlTemplate = field("entityUrlTemplate")
    executionUrlTemplate = field("executionUrlTemplate")
    revisionUrlTemplate = field("revisionUrlTemplate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionTypeSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionTypeSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArtifactDetails:
    boto3_raw_data: "type_defs.ArtifactDetailsTypeDef" = dataclasses.field()

    minimumCount = field("minimumCount")
    maximumCount = field("maximumCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ArtifactDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ArtifactDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApprovalResult:
    boto3_raw_data: "type_defs.ApprovalResultTypeDef" = dataclasses.field()

    summary = field("summary")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApprovalResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApprovalResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Location:
    boto3_raw_data: "type_defs.S3LocationTypeDef" = dataclasses.field()

    bucket = field("bucket")
    key = field("key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3LocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3LocationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ArtifactLocation:
    boto3_raw_data: "type_defs.S3ArtifactLocationTypeDef" = dataclasses.field()

    bucketName = field("bucketName")
    objectKey = field("objectKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3ArtifactLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ArtifactLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArtifactRevision:
    boto3_raw_data: "type_defs.ArtifactRevisionTypeDef" = dataclasses.field()

    name = field("name")
    revisionId = field("revisionId")
    revisionChangeIdentifier = field("revisionChangeIdentifier")
    revisionSummary = field("revisionSummary")
    created = field("created")
    revisionUrl = field("revisionUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ArtifactRevisionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArtifactRevisionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionKey:
    boto3_raw_data: "type_defs.EncryptionKeyTypeDef" = dataclasses.field()

    id = field("id")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptionKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EncryptionKeyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlockerDeclaration:
    boto3_raw_data: "type_defs.BlockerDeclarationTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BlockerDeclarationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BlockerDeclarationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionExecution:
    boto3_raw_data: "type_defs.ConditionExecutionTypeDef" = dataclasses.field()

    status = field("status")
    summary = field("summary")
    lastStatusChange = field("lastStatusChange")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConditionExecutionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConditionExecutionTypeDef"]
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
class DeleteCustomActionTypeInput:
    boto3_raw_data: "type_defs.DeleteCustomActionTypeInputTypeDef" = dataclasses.field()

    category = field("category")
    provider = field("provider")
    version = field("version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCustomActionTypeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCustomActionTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePipelineInput:
    boto3_raw_data: "type_defs.DeletePipelineInputTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePipelineInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePipelineInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWebhookInput:
    boto3_raw_data: "type_defs.DeleteWebhookInputTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWebhookInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWebhookInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeployTargetEventContext:
    boto3_raw_data: "type_defs.DeployTargetEventContextTypeDef" = dataclasses.field()

    ssmCommandId = field("ssmCommandId")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeployTargetEventContextTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeployTargetEventContextTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterWebhookWithThirdPartyInput:
    boto3_raw_data: "type_defs.DeregisterWebhookWithThirdPartyInputTypeDef" = (
        dataclasses.field()
    )

    webhookName = field("webhookName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeregisterWebhookWithThirdPartyInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterWebhookWithThirdPartyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableStageTransitionInput:
    boto3_raw_data: "type_defs.DisableStageTransitionInputTypeDef" = dataclasses.field()

    pipelineName = field("pipelineName")
    stageName = field("stageName")
    transitionType = field("transitionType")
    reason = field("reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableStageTransitionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableStageTransitionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableStageTransitionInput:
    boto3_raw_data: "type_defs.EnableStageTransitionInputTypeDef" = dataclasses.field()

    pipelineName = field("pipelineName")
    stageName = field("stageName")
    transitionType = field("transitionType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableStageTransitionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableStageTransitionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionDetails:
    boto3_raw_data: "type_defs.ExecutionDetailsTypeDef" = dataclasses.field()

    summary = field("summary")
    externalExecutionId = field("externalExecutionId")
    percentComplete = field("percentComplete")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExecutionDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutionDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionTrigger:
    boto3_raw_data: "type_defs.ExecutionTriggerTypeDef" = dataclasses.field()

    triggerType = field("triggerType")
    triggerDetail = field("triggerDetail")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExecutionTriggerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutionTriggerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobWorkerExecutorConfigurationOutput:
    boto3_raw_data: "type_defs.JobWorkerExecutorConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    pollingAccounts = field("pollingAccounts")
    pollingServicePrincipals = field("pollingServicePrincipals")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.JobWorkerExecutorConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobWorkerExecutorConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaExecutorConfiguration:
    boto3_raw_data: "type_defs.LambdaExecutorConfigurationTypeDef" = dataclasses.field()

    lambdaFunctionArn = field("lambdaFunctionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaExecutorConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaExecutorConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobWorkerExecutorConfiguration:
    boto3_raw_data: "type_defs.JobWorkerExecutorConfigurationTypeDef" = (
        dataclasses.field()
    )

    pollingAccounts = field("pollingAccounts")
    pollingServicePrincipals = field("pollingServicePrincipals")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.JobWorkerExecutorConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobWorkerExecutorConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetryConfiguration:
    boto3_raw_data: "type_defs.RetryConfigurationTypeDef" = dataclasses.field()

    retryMode = field("retryMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetryConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetryConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailureDetails:
    boto3_raw_data: "type_defs.FailureDetailsTypeDef" = dataclasses.field()

    type = field("type")
    message = field("message")
    externalExecutionId = field("externalExecutionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailureDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FailureDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetActionTypeInput:
    boto3_raw_data: "type_defs.GetActionTypeInputTypeDef" = dataclasses.field()

    category = field("category")
    owner = field("owner")
    provider = field("provider")
    version = field("version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetActionTypeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetActionTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobDetailsInput:
    boto3_raw_data: "type_defs.GetJobDetailsInputTypeDef" = dataclasses.field()

    jobId = field("jobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetJobDetailsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJobDetailsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPipelineExecutionInput:
    boto3_raw_data: "type_defs.GetPipelineExecutionInputTypeDef" = dataclasses.field()

    pipelineName = field("pipelineName")
    pipelineExecutionId = field("pipelineExecutionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPipelineExecutionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPipelineExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPipelineInput:
    boto3_raw_data: "type_defs.GetPipelineInputTypeDef" = dataclasses.field()

    name = field("name")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPipelineInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPipelineInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineMetadata:
    boto3_raw_data: "type_defs.PipelineMetadataTypeDef" = dataclasses.field()

    pipelineArn = field("pipelineArn")
    created = field("created")
    updated = field("updated")
    pollingDisabledAt = field("pollingDisabledAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PipelineMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPipelineStateInput:
    boto3_raw_data: "type_defs.GetPipelineStateInputTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPipelineStateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPipelineStateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetThirdPartyJobDetailsInput:
    boto3_raw_data: "type_defs.GetThirdPartyJobDetailsInputTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetThirdPartyJobDetailsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetThirdPartyJobDetailsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GitBranchFilterCriteriaOutput:
    boto3_raw_data: "type_defs.GitBranchFilterCriteriaOutputTypeDef" = (
        dataclasses.field()
    )

    includes = field("includes")
    excludes = field("excludes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GitBranchFilterCriteriaOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GitBranchFilterCriteriaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GitBranchFilterCriteria:
    boto3_raw_data: "type_defs.GitBranchFilterCriteriaTypeDef" = dataclasses.field()

    includes = field("includes")
    excludes = field("excludes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GitBranchFilterCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GitBranchFilterCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GitFilePathFilterCriteriaOutput:
    boto3_raw_data: "type_defs.GitFilePathFilterCriteriaOutputTypeDef" = (
        dataclasses.field()
    )

    includes = field("includes")
    excludes = field("excludes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GitFilePathFilterCriteriaOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GitFilePathFilterCriteriaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GitFilePathFilterCriteria:
    boto3_raw_data: "type_defs.GitFilePathFilterCriteriaTypeDef" = dataclasses.field()

    includes = field("includes")
    excludes = field("excludes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GitFilePathFilterCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GitFilePathFilterCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GitTagFilterCriteriaOutput:
    boto3_raw_data: "type_defs.GitTagFilterCriteriaOutputTypeDef" = dataclasses.field()

    includes = field("includes")
    excludes = field("excludes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GitTagFilterCriteriaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GitTagFilterCriteriaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GitTagFilterCriteria:
    boto3_raw_data: "type_defs.GitTagFilterCriteriaTypeDef" = dataclasses.field()

    includes = field("includes")
    excludes = field("excludes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GitTagFilterCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GitTagFilterCriteriaTypeDef"]
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
class ListActionTypesInput:
    boto3_raw_data: "type_defs.ListActionTypesInputTypeDef" = dataclasses.field()

    actionOwnerFilter = field("actionOwnerFilter")
    nextToken = field("nextToken")
    regionFilter = field("regionFilter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListActionTypesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListActionTypesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetFilter:
    boto3_raw_data: "type_defs.TargetFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelinesInput:
    boto3_raw_data: "type_defs.ListPipelinesInputTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPipelinesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelinesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineSummary:
    boto3_raw_data: "type_defs.PipelineSummaryTypeDef" = dataclasses.field()

    name = field("name")
    version = field("version")
    pipelineType = field("pipelineType")
    executionMode = field("executionMode")
    created = field("created")
    updated = field("updated")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PipelineSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PipelineSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRuleTypesInput:
    boto3_raw_data: "type_defs.ListRuleTypesInputTypeDef" = dataclasses.field()

    ruleOwnerFilter = field("ruleOwnerFilter")
    regionFilter = field("regionFilter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRuleTypesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRuleTypesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInput:
    boto3_raw_data: "type_defs.ListTagsForResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWebhooksInput:
    boto3_raw_data: "type_defs.ListWebhooksInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListWebhooksInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWebhooksInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OverrideStageConditionInput:
    boto3_raw_data: "type_defs.OverrideStageConditionInputTypeDef" = dataclasses.field()

    pipelineName = field("pipelineName")
    stageName = field("stageName")
    pipelineExecutionId = field("pipelineExecutionId")
    conditionType = field("conditionType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OverrideStageConditionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OverrideStageConditionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StageContext:
    boto3_raw_data: "type_defs.StageContextTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StageContextTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StageContextTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineVariableDeclaration:
    boto3_raw_data: "type_defs.PipelineVariableDeclarationTypeDef" = dataclasses.field()

    name = field("name")
    defaultValue = field("defaultValue")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipelineVariableDeclarationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineVariableDeclarationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SucceededInStageFilter:
    boto3_raw_data: "type_defs.SucceededInStageFilterTypeDef" = dataclasses.field()

    stageName = field("stageName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SucceededInStageFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SucceededInStageFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineRollbackMetadata:
    boto3_raw_data: "type_defs.PipelineRollbackMetadataTypeDef" = dataclasses.field()

    rollbackTargetPipelineExecutionId = field("rollbackTargetPipelineExecutionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipelineRollbackMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineRollbackMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceRevision:
    boto3_raw_data: "type_defs.SourceRevisionTypeDef" = dataclasses.field()

    actionName = field("actionName")
    revisionId = field("revisionId")
    revisionSummary = field("revisionSummary")
    revisionUrl = field("revisionUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceRevisionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceRevisionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopExecutionTrigger:
    boto3_raw_data: "type_defs.StopExecutionTriggerTypeDef" = dataclasses.field()

    reason = field("reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopExecutionTriggerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopExecutionTriggerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolvedPipelineVariable:
    boto3_raw_data: "type_defs.ResolvedPipelineVariableTypeDef" = dataclasses.field()

    name = field("name")
    resolvedValue = field("resolvedValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResolvedPipelineVariableTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResolvedPipelineVariableTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineVariable:
    boto3_raw_data: "type_defs.PipelineVariableTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PipelineVariableTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineVariableTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThirdPartyJob:
    boto3_raw_data: "type_defs.ThirdPartyJobTypeDef" = dataclasses.field()

    clientId = field("clientId")
    jobId = field("jobId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThirdPartyJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ThirdPartyJobTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterWebhookWithThirdPartyInput:
    boto3_raw_data: "type_defs.RegisterWebhookWithThirdPartyInputTypeDef" = (
        dataclasses.field()
    )

    webhookName = field("webhookName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterWebhookWithThirdPartyInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterWebhookWithThirdPartyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetryStageExecutionInput:
    boto3_raw_data: "type_defs.RetryStageExecutionInputTypeDef" = dataclasses.field()

    pipelineName = field("pipelineName")
    stageName = field("stageName")
    pipelineExecutionId = field("pipelineExecutionId")
    retryMode = field("retryMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetryStageExecutionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetryStageExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetryStageMetadata:
    boto3_raw_data: "type_defs.RetryStageMetadataTypeDef" = dataclasses.field()

    autoStageRetryAttempt = field("autoStageRetryAttempt")
    manualStageRetryAttempt = field("manualStageRetryAttempt")
    latestRetryTrigger = field("latestRetryTrigger")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetryStageMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetryStageMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RollbackStageInput:
    boto3_raw_data: "type_defs.RollbackStageInputTypeDef" = dataclasses.field()

    pipelineName = field("pipelineName")
    stageName = field("stageName")
    targetPipelineExecutionId = field("targetPipelineExecutionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RollbackStageInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RollbackStageInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleConfigurationProperty:
    boto3_raw_data: "type_defs.RuleConfigurationPropertyTypeDef" = dataclasses.field()

    name = field("name")
    required = field("required")
    key = field("key")
    secret = field("secret")
    queryable = field("queryable")
    description = field("description")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleConfigurationPropertyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleConfigurationPropertyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleTypeId:
    boto3_raw_data: "type_defs.RuleTypeIdTypeDef" = dataclasses.field()

    category = field("category")
    provider = field("provider")
    owner = field("owner")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleTypeIdTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleTypeIdTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleRevision:
    boto3_raw_data: "type_defs.RuleRevisionTypeDef" = dataclasses.field()

    revisionId = field("revisionId")
    revisionChangeId = field("revisionChangeId")
    created = field("created")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleRevisionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleRevisionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleTypeSettings:
    boto3_raw_data: "type_defs.RuleTypeSettingsTypeDef" = dataclasses.field()

    thirdPartyConfigurationUrl = field("thirdPartyConfigurationUrl")
    entityUrlTemplate = field("entityUrlTemplate")
    executionUrlTemplate = field("executionUrlTemplate")
    revisionUrlTemplate = field("revisionUrlTemplate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleTypeSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleTypeSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceRevisionOverride:
    boto3_raw_data: "type_defs.SourceRevisionOverrideTypeDef" = dataclasses.field()

    actionName = field("actionName")
    revisionType = field("revisionType")
    revisionValue = field("revisionValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceRevisionOverrideTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceRevisionOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StageConditionsExecution:
    boto3_raw_data: "type_defs.StageConditionsExecutionTypeDef" = dataclasses.field()

    status = field("status")
    summary = field("summary")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StageConditionsExecutionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StageConditionsExecutionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StageExecution:
    boto3_raw_data: "type_defs.StageExecutionTypeDef" = dataclasses.field()

    pipelineExecutionId = field("pipelineExecutionId")
    status = field("status")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StageExecutionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StageExecutionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransitionState:
    boto3_raw_data: "type_defs.TransitionStateTypeDef" = dataclasses.field()

    enabled = field("enabled")
    lastChangedBy = field("lastChangedBy")
    lastChangedAt = field("lastChangedAt")
    disabledReason = field("disabledReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TransitionStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TransitionStateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopPipelineExecutionInput:
    boto3_raw_data: "type_defs.StopPipelineExecutionInputTypeDef" = dataclasses.field()

    pipelineName = field("pipelineName")
    pipelineExecutionId = field("pipelineExecutionId")
    abandon = field("abandon")
    reason = field("reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopPipelineExecutionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopPipelineExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceInput:
    boto3_raw_data: "type_defs.UntagResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebhookAuthConfiguration:
    boto3_raw_data: "type_defs.WebhookAuthConfigurationTypeDef" = dataclasses.field()

    AllowedIPRange = field("AllowedIPRange")
    SecretToken = field("SecretToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WebhookAuthConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebhookAuthConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebhookFilterRule:
    boto3_raw_data: "type_defs.WebhookFilterRuleTypeDef" = dataclasses.field()

    jsonPath = field("jsonPath")
    matchEquals = field("matchEquals")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WebhookFilterRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebhookFilterRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcknowledgeJobOutput:
    boto3_raw_data: "type_defs.AcknowledgeJobOutputTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcknowledgeJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcknowledgeJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcknowledgeThirdPartyJobOutput:
    boto3_raw_data: "type_defs.AcknowledgeThirdPartyJobOutputTypeDef" = (
        dataclasses.field()
    )

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AcknowledgeThirdPartyJobOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcknowledgeThirdPartyJobOutputTypeDef"]
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
class PutActionRevisionOutput:
    boto3_raw_data: "type_defs.PutActionRevisionOutputTypeDef" = dataclasses.field()

    newRevision = field("newRevision")
    pipelineExecutionId = field("pipelineExecutionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutActionRevisionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutActionRevisionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutApprovalResultOutput:
    boto3_raw_data: "type_defs.PutApprovalResultOutputTypeDef" = dataclasses.field()

    approvedAt = field("approvedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutApprovalResultOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutApprovalResultOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetryStageExecutionOutput:
    boto3_raw_data: "type_defs.RetryStageExecutionOutputTypeDef" = dataclasses.field()

    pipelineExecutionId = field("pipelineExecutionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetryStageExecutionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetryStageExecutionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RollbackStageOutput:
    boto3_raw_data: "type_defs.RollbackStageOutputTypeDef" = dataclasses.field()

    pipelineExecutionId = field("pipelineExecutionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RollbackStageOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RollbackStageOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartPipelineExecutionOutput:
    boto3_raw_data: "type_defs.StartPipelineExecutionOutputTypeDef" = (
        dataclasses.field()
    )

    pipelineExecutionId = field("pipelineExecutionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartPipelineExecutionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartPipelineExecutionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopPipelineExecutionOutput:
    boto3_raw_data: "type_defs.StopPipelineExecutionOutputTypeDef" = dataclasses.field()

    pipelineExecutionId = field("pipelineExecutionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopPipelineExecutionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopPipelineExecutionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PollForJobsInput:
    boto3_raw_data: "type_defs.PollForJobsInputTypeDef" = dataclasses.field()

    @cached_property
    def actionTypeId(self):  # pragma: no cover
        return ActionTypeId.make_one(self.boto3_raw_data["actionTypeId"])

    maxBatchSize = field("maxBatchSize")
    queryParam = field("queryParam")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PollForJobsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PollForJobsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PollForThirdPartyJobsInput:
    boto3_raw_data: "type_defs.PollForThirdPartyJobsInputTypeDef" = dataclasses.field()

    @cached_property
    def actionTypeId(self):  # pragma: no cover
        return ActionTypeId.make_one(self.boto3_raw_data["actionTypeId"])

    maxBatchSize = field("maxBatchSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PollForThirdPartyJobsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PollForThirdPartyJobsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionDeclarationOutput:
    boto3_raw_data: "type_defs.ActionDeclarationOutputTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def actionTypeId(self):  # pragma: no cover
        return ActionTypeId.make_one(self.boto3_raw_data["actionTypeId"])

    runOrder = field("runOrder")
    configuration = field("configuration")
    commands = field("commands")

    @cached_property
    def outputArtifacts(self):  # pragma: no cover
        return OutputArtifactOutput.make_many(self.boto3_raw_data["outputArtifacts"])

    @cached_property
    def inputArtifacts(self):  # pragma: no cover
        return InputArtifact.make_many(self.boto3_raw_data["inputArtifacts"])

    outputVariables = field("outputVariables")
    roleArn = field("roleArn")
    region = field("region")
    namespace = field("namespace")
    timeoutInMinutes = field("timeoutInMinutes")

    @cached_property
    def environmentVariables(self):  # pragma: no cover
        return EnvironmentVariable.make_many(
            self.boto3_raw_data["environmentVariables"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionDeclarationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionDeclarationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionDeclaration:
    boto3_raw_data: "type_defs.ActionDeclarationTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def actionTypeId(self):  # pragma: no cover
        return ActionTypeId.make_one(self.boto3_raw_data["actionTypeId"])

    runOrder = field("runOrder")
    configuration = field("configuration")
    commands = field("commands")

    @cached_property
    def outputArtifacts(self):  # pragma: no cover
        return OutputArtifact.make_many(self.boto3_raw_data["outputArtifacts"])

    @cached_property
    def inputArtifacts(self):  # pragma: no cover
        return InputArtifact.make_many(self.boto3_raw_data["inputArtifacts"])

    outputVariables = field("outputVariables")
    roleArn = field("roleArn")
    region = field("region")
    namespace = field("namespace")
    timeoutInMinutes = field("timeoutInMinutes")

    @cached_property
    def environmentVariables(self):  # pragma: no cover
        return EnvironmentVariable.make_many(
            self.boto3_raw_data["environmentVariables"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionDeclarationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionDeclarationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionExecutionFilter:
    boto3_raw_data: "type_defs.ActionExecutionFilterTypeDef" = dataclasses.field()

    pipelineExecutionId = field("pipelineExecutionId")

    @cached_property
    def latestInPipelineExecution(self):  # pragma: no cover
        return LatestInPipelineExecutionFilter.make_one(
            self.boto3_raw_data["latestInPipelineExecution"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionExecutionFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionExecutionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleExecutionFilter:
    boto3_raw_data: "type_defs.RuleExecutionFilterTypeDef" = dataclasses.field()

    pipelineExecutionId = field("pipelineExecutionId")

    @cached_property
    def latestInPipelineExecution(self):  # pragma: no cover
        return LatestInPipelineExecutionFilter.make_one(
            self.boto3_raw_data["latestInPipelineExecution"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleExecutionFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleExecutionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionExecutionResult:
    boto3_raw_data: "type_defs.ActionExecutionResultTypeDef" = dataclasses.field()

    externalExecutionId = field("externalExecutionId")
    externalExecutionSummary = field("externalExecutionSummary")
    externalExecutionUrl = field("externalExecutionUrl")

    @cached_property
    def errorDetails(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["errorDetails"])

    logStreamARN = field("logStreamARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionExecutionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionExecutionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionExecution:
    boto3_raw_data: "type_defs.ActionExecutionTypeDef" = dataclasses.field()

    actionExecutionId = field("actionExecutionId")
    status = field("status")
    summary = field("summary")
    lastStatusChange = field("lastStatusChange")
    token = field("token")
    lastUpdatedBy = field("lastUpdatedBy")
    externalExecutionId = field("externalExecutionId")
    externalExecutionUrl = field("externalExecutionUrl")
    percentComplete = field("percentComplete")

    @cached_property
    def errorDetails(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["errorDetails"])

    logStreamARN = field("logStreamARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionExecutionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionExecutionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleExecutionResult:
    boto3_raw_data: "type_defs.RuleExecutionResultTypeDef" = dataclasses.field()

    externalExecutionId = field("externalExecutionId")
    externalExecutionSummary = field("externalExecutionSummary")
    externalExecutionUrl = field("externalExecutionUrl")

    @cached_property
    def errorDetails(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["errorDetails"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleExecutionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleExecutionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleExecution:
    boto3_raw_data: "type_defs.RuleExecutionTypeDef" = dataclasses.field()

    ruleExecutionId = field("ruleExecutionId")
    status = field("status")
    summary = field("summary")
    lastStatusChange = field("lastStatusChange")
    token = field("token")
    lastUpdatedBy = field("lastUpdatedBy")
    externalExecutionId = field("externalExecutionId")
    externalExecutionUrl = field("externalExecutionUrl")

    @cached_property
    def errorDetails(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["errorDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleExecutionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleExecutionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionRevision:
    boto3_raw_data: "type_defs.ActionRevisionTypeDef" = dataclasses.field()

    revisionId = field("revisionId")
    revisionChangeId = field("revisionChangeId")
    created = field("created")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionRevisionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionRevisionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CurrentRevision:
    boto3_raw_data: "type_defs.CurrentRevisionTypeDef" = dataclasses.field()

    revision = field("revision")
    changeIdentifier = field("changeIdentifier")
    created = field("created")
    revisionSummary = field("revisionSummary")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CurrentRevisionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CurrentRevisionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionType:
    boto3_raw_data: "type_defs.ActionTypeTypeDef" = dataclasses.field()

    @cached_property
    def id(self):  # pragma: no cover
        return ActionTypeId.make_one(self.boto3_raw_data["id"])

    @cached_property
    def inputArtifactDetails(self):  # pragma: no cover
        return ArtifactDetails.make_one(self.boto3_raw_data["inputArtifactDetails"])

    @cached_property
    def outputArtifactDetails(self):  # pragma: no cover
        return ArtifactDetails.make_one(self.boto3_raw_data["outputArtifactDetails"])

    @cached_property
    def settings(self):  # pragma: no cover
        return ActionTypeSettings.make_one(self.boto3_raw_data["settings"])

    @cached_property
    def actionConfigurationProperties(self):  # pragma: no cover
        return ActionConfigurationProperty.make_many(
            self.boto3_raw_data["actionConfigurationProperties"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutApprovalResultInput:
    boto3_raw_data: "type_defs.PutApprovalResultInputTypeDef" = dataclasses.field()

    pipelineName = field("pipelineName")
    stageName = field("stageName")
    actionName = field("actionName")

    @cached_property
    def result(self):  # pragma: no cover
        return ApprovalResult.make_one(self.boto3_raw_data["result"])

    token = field("token")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutApprovalResultInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutApprovalResultInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArtifactDetail:
    boto3_raw_data: "type_defs.ArtifactDetailTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def s3location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ArtifactDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ArtifactDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArtifactLocation:
    boto3_raw_data: "type_defs.ArtifactLocationTypeDef" = dataclasses.field()

    type = field("type")

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3ArtifactLocation.make_one(self.boto3_raw_data["s3Location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ArtifactLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArtifactLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArtifactStore:
    boto3_raw_data: "type_defs.ArtifactStoreTypeDef" = dataclasses.field()

    type = field("type")
    location = field("location")

    @cached_property
    def encryptionKey(self):  # pragma: no cover
        return EncryptionKey.make_one(self.boto3_raw_data["encryptionKey"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ArtifactStoreTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ArtifactStoreTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomActionTypeInput:
    boto3_raw_data: "type_defs.CreateCustomActionTypeInputTypeDef" = dataclasses.field()

    category = field("category")
    provider = field("provider")
    version = field("version")

    @cached_property
    def inputArtifactDetails(self):  # pragma: no cover
        return ArtifactDetails.make_one(self.boto3_raw_data["inputArtifactDetails"])

    @cached_property
    def outputArtifactDetails(self):  # pragma: no cover
        return ArtifactDetails.make_one(self.boto3_raw_data["outputArtifactDetails"])

    @cached_property
    def settings(self):  # pragma: no cover
        return ActionTypeSettings.make_one(self.boto3_raw_data["settings"])

    @cached_property
    def configurationProperties(self):  # pragma: no cover
        return ActionConfigurationProperty.make_many(
            self.boto3_raw_data["configurationProperties"]
        )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCustomActionTypeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomActionTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceOutput:
    boto3_raw_data: "type_defs.ListTagsForResourceOutputTypeDef" = dataclasses.field()

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceInput:
    boto3_raw_data: "type_defs.TagResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagResourceInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeployTargetEvent:
    boto3_raw_data: "type_defs.DeployTargetEventTypeDef" = dataclasses.field()

    name = field("name")
    status = field("status")
    startTime = field("startTime")
    endTime = field("endTime")

    @cached_property
    def context(self):  # pragma: no cover
        return DeployTargetEventContext.make_one(self.boto3_raw_data["context"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeployTargetEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeployTargetEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutorConfigurationOutput:
    boto3_raw_data: "type_defs.ExecutorConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def lambdaExecutorConfiguration(self):  # pragma: no cover
        return LambdaExecutorConfiguration.make_one(
            self.boto3_raw_data["lambdaExecutorConfiguration"]
        )

    @cached_property
    def jobWorkerExecutorConfiguration(self):  # pragma: no cover
        return JobWorkerExecutorConfigurationOutput.make_one(
            self.boto3_raw_data["jobWorkerExecutorConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecutorConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutorConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutorConfiguration:
    boto3_raw_data: "type_defs.ExecutorConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def lambdaExecutorConfiguration(self):  # pragma: no cover
        return LambdaExecutorConfiguration.make_one(
            self.boto3_raw_data["lambdaExecutorConfiguration"]
        )

    @cached_property
    def jobWorkerExecutorConfiguration(self):  # pragma: no cover
        return JobWorkerExecutorConfiguration.make_one(
            self.boto3_raw_data["jobWorkerExecutorConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecutorConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutorConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutJobFailureResultInput:
    boto3_raw_data: "type_defs.PutJobFailureResultInputTypeDef" = dataclasses.field()

    jobId = field("jobId")

    @cached_property
    def failureDetails(self):  # pragma: no cover
        return FailureDetails.make_one(self.boto3_raw_data["failureDetails"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutJobFailureResultInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutJobFailureResultInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutThirdPartyJobFailureResultInput:
    boto3_raw_data: "type_defs.PutThirdPartyJobFailureResultInputTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")
    clientToken = field("clientToken")

    @cached_property
    def failureDetails(self):  # pragma: no cover
        return FailureDetails.make_one(self.boto3_raw_data["failureDetails"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutThirdPartyJobFailureResultInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutThirdPartyJobFailureResultInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GitPullRequestFilterOutput:
    boto3_raw_data: "type_defs.GitPullRequestFilterOutputTypeDef" = dataclasses.field()

    events = field("events")

    @cached_property
    def branches(self):  # pragma: no cover
        return GitBranchFilterCriteriaOutput.make_one(self.boto3_raw_data["branches"])

    @cached_property
    def filePaths(self):  # pragma: no cover
        return GitFilePathFilterCriteriaOutput.make_one(
            self.boto3_raw_data["filePaths"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GitPullRequestFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GitPullRequestFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GitPullRequestFilter:
    boto3_raw_data: "type_defs.GitPullRequestFilterTypeDef" = dataclasses.field()

    events = field("events")

    @cached_property
    def branches(self):  # pragma: no cover
        return GitBranchFilterCriteria.make_one(self.boto3_raw_data["branches"])

    @cached_property
    def filePaths(self):  # pragma: no cover
        return GitFilePathFilterCriteria.make_one(self.boto3_raw_data["filePaths"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GitPullRequestFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GitPullRequestFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GitPushFilterOutput:
    boto3_raw_data: "type_defs.GitPushFilterOutputTypeDef" = dataclasses.field()

    @cached_property
    def tags(self):  # pragma: no cover
        return GitTagFilterCriteriaOutput.make_one(self.boto3_raw_data["tags"])

    @cached_property
    def branches(self):  # pragma: no cover
        return GitBranchFilterCriteriaOutput.make_one(self.boto3_raw_data["branches"])

    @cached_property
    def filePaths(self):  # pragma: no cover
        return GitFilePathFilterCriteriaOutput.make_one(
            self.boto3_raw_data["filePaths"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GitPushFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GitPushFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GitPushFilter:
    boto3_raw_data: "type_defs.GitPushFilterTypeDef" = dataclasses.field()

    @cached_property
    def tags(self):  # pragma: no cover
        return GitTagFilterCriteria.make_one(self.boto3_raw_data["tags"])

    @cached_property
    def branches(self):  # pragma: no cover
        return GitBranchFilterCriteria.make_one(self.boto3_raw_data["branches"])

    @cached_property
    def filePaths(self):  # pragma: no cover
        return GitFilePathFilterCriteria.make_one(self.boto3_raw_data["filePaths"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GitPushFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GitPushFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListActionTypesInputPaginate:
    boto3_raw_data: "type_defs.ListActionTypesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    actionOwnerFilter = field("actionOwnerFilter")
    regionFilter = field("regionFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListActionTypesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListActionTypesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelinesInputPaginate:
    boto3_raw_data: "type_defs.ListPipelinesInputPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPipelinesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelinesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInputPaginate:
    boto3_raw_data: "type_defs.ListTagsForResourceInputPaginateTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTagsForResourceInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWebhooksInputPaginate:
    boto3_raw_data: "type_defs.ListWebhooksInputPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWebhooksInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWebhooksInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeployActionExecutionTargetsInputPaginate:
    boto3_raw_data: "type_defs.ListDeployActionExecutionTargetsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    actionExecutionId = field("actionExecutionId")
    pipelineName = field("pipelineName")

    @cached_property
    def filters(self):  # pragma: no cover
        return TargetFilter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDeployActionExecutionTargetsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeployActionExecutionTargetsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeployActionExecutionTargetsInput:
    boto3_raw_data: "type_defs.ListDeployActionExecutionTargetsInputTypeDef" = (
        dataclasses.field()
    )

    actionExecutionId = field("actionExecutionId")
    pipelineName = field("pipelineName")

    @cached_property
    def filters(self):  # pragma: no cover
        return TargetFilter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDeployActionExecutionTargetsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeployActionExecutionTargetsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelinesOutput:
    boto3_raw_data: "type_defs.ListPipelinesOutputTypeDef" = dataclasses.field()

    @cached_property
    def pipelines(self):  # pragma: no cover
        return PipelineSummary.make_many(self.boto3_raw_data["pipelines"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPipelinesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelinesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineContext:
    boto3_raw_data: "type_defs.PipelineContextTypeDef" = dataclasses.field()

    pipelineName = field("pipelineName")

    @cached_property
    def stage(self):  # pragma: no cover
        return StageContext.make_one(self.boto3_raw_data["stage"])

    @cached_property
    def action(self):  # pragma: no cover
        return ActionContext.make_one(self.boto3_raw_data["action"])

    pipelineArn = field("pipelineArn")
    pipelineExecutionId = field("pipelineExecutionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PipelineContextTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PipelineContextTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineExecutionFilter:
    boto3_raw_data: "type_defs.PipelineExecutionFilterTypeDef" = dataclasses.field()

    @cached_property
    def succeededInStage(self):  # pragma: no cover
        return SucceededInStageFilter.make_one(self.boto3_raw_data["succeededInStage"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipelineExecutionFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineExecutionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineExecutionSummary:
    boto3_raw_data: "type_defs.PipelineExecutionSummaryTypeDef" = dataclasses.field()

    pipelineExecutionId = field("pipelineExecutionId")
    status = field("status")
    statusSummary = field("statusSummary")
    startTime = field("startTime")
    lastUpdateTime = field("lastUpdateTime")

    @cached_property
    def sourceRevisions(self):  # pragma: no cover
        return SourceRevision.make_many(self.boto3_raw_data["sourceRevisions"])

    @cached_property
    def trigger(self):  # pragma: no cover
        return ExecutionTrigger.make_one(self.boto3_raw_data["trigger"])

    @cached_property
    def stopTrigger(self):  # pragma: no cover
        return StopExecutionTrigger.make_one(self.boto3_raw_data["stopTrigger"])

    executionMode = field("executionMode")
    executionType = field("executionType")

    @cached_property
    def rollbackMetadata(self):  # pragma: no cover
        return PipelineRollbackMetadata.make_one(
            self.boto3_raw_data["rollbackMetadata"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipelineExecutionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineExecutionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineExecution:
    boto3_raw_data: "type_defs.PipelineExecutionTypeDef" = dataclasses.field()

    pipelineName = field("pipelineName")
    pipelineVersion = field("pipelineVersion")
    pipelineExecutionId = field("pipelineExecutionId")
    status = field("status")
    statusSummary = field("statusSummary")

    @cached_property
    def artifactRevisions(self):  # pragma: no cover
        return ArtifactRevision.make_many(self.boto3_raw_data["artifactRevisions"])

    @cached_property
    def variables(self):  # pragma: no cover
        return ResolvedPipelineVariable.make_many(self.boto3_raw_data["variables"])

    @cached_property
    def trigger(self):  # pragma: no cover
        return ExecutionTrigger.make_one(self.boto3_raw_data["trigger"])

    executionMode = field("executionMode")
    executionType = field("executionType")

    @cached_property
    def rollbackMetadata(self):  # pragma: no cover
        return PipelineRollbackMetadata.make_one(
            self.boto3_raw_data["rollbackMetadata"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PipelineExecutionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineExecutionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PollForThirdPartyJobsOutput:
    boto3_raw_data: "type_defs.PollForThirdPartyJobsOutputTypeDef" = dataclasses.field()

    @cached_property
    def jobs(self):  # pragma: no cover
        return ThirdPartyJob.make_many(self.boto3_raw_data["jobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PollForThirdPartyJobsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PollForThirdPartyJobsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleDeclarationOutput:
    boto3_raw_data: "type_defs.RuleDeclarationOutputTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def ruleTypeId(self):  # pragma: no cover
        return RuleTypeId.make_one(self.boto3_raw_data["ruleTypeId"])

    configuration = field("configuration")
    commands = field("commands")

    @cached_property
    def inputArtifacts(self):  # pragma: no cover
        return InputArtifact.make_many(self.boto3_raw_data["inputArtifacts"])

    roleArn = field("roleArn")
    region = field("region")
    timeoutInMinutes = field("timeoutInMinutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleDeclarationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleDeclarationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleDeclaration:
    boto3_raw_data: "type_defs.RuleDeclarationTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def ruleTypeId(self):  # pragma: no cover
        return RuleTypeId.make_one(self.boto3_raw_data["ruleTypeId"])

    configuration = field("configuration")
    commands = field("commands")

    @cached_property
    def inputArtifacts(self):  # pragma: no cover
        return InputArtifact.make_many(self.boto3_raw_data["inputArtifacts"])

    roleArn = field("roleArn")
    region = field("region")
    timeoutInMinutes = field("timeoutInMinutes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleDeclarationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleDeclarationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleType:
    boto3_raw_data: "type_defs.RuleTypeTypeDef" = dataclasses.field()

    @cached_property
    def id(self):  # pragma: no cover
        return RuleTypeId.make_one(self.boto3_raw_data["id"])

    @cached_property
    def inputArtifactDetails(self):  # pragma: no cover
        return ArtifactDetails.make_one(self.boto3_raw_data["inputArtifactDetails"])

    @cached_property
    def settings(self):  # pragma: no cover
        return RuleTypeSettings.make_one(self.boto3_raw_data["settings"])

    @cached_property
    def ruleConfigurationProperties(self):  # pragma: no cover
        return RuleConfigurationProperty.make_many(
            self.boto3_raw_data["ruleConfigurationProperties"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartPipelineExecutionInput:
    boto3_raw_data: "type_defs.StartPipelineExecutionInputTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def variables(self):  # pragma: no cover
        return PipelineVariable.make_many(self.boto3_raw_data["variables"])

    clientRequestToken = field("clientRequestToken")

    @cached_property
    def sourceRevisions(self):  # pragma: no cover
        return SourceRevisionOverride.make_many(self.boto3_raw_data["sourceRevisions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartPipelineExecutionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartPipelineExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebhookDefinitionOutput:
    boto3_raw_data: "type_defs.WebhookDefinitionOutputTypeDef" = dataclasses.field()

    name = field("name")
    targetPipeline = field("targetPipeline")
    targetAction = field("targetAction")

    @cached_property
    def filters(self):  # pragma: no cover
        return WebhookFilterRule.make_many(self.boto3_raw_data["filters"])

    authentication = field("authentication")

    @cached_property
    def authenticationConfiguration(self):  # pragma: no cover
        return WebhookAuthConfiguration.make_one(
            self.boto3_raw_data["authenticationConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WebhookDefinitionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebhookDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebhookDefinition:
    boto3_raw_data: "type_defs.WebhookDefinitionTypeDef" = dataclasses.field()

    name = field("name")
    targetPipeline = field("targetPipeline")
    targetAction = field("targetAction")

    @cached_property
    def filters(self):  # pragma: no cover
        return WebhookFilterRule.make_many(self.boto3_raw_data["filters"])

    authentication = field("authentication")

    @cached_property
    def authenticationConfiguration(self):  # pragma: no cover
        return WebhookAuthConfiguration.make_one(
            self.boto3_raw_data["authenticationConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WebhookDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebhookDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListActionExecutionsInputPaginate:
    boto3_raw_data: "type_defs.ListActionExecutionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    pipelineName = field("pipelineName")

    @cached_property
    def filter(self):  # pragma: no cover
        return ActionExecutionFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListActionExecutionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListActionExecutionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListActionExecutionsInput:
    boto3_raw_data: "type_defs.ListActionExecutionsInputTypeDef" = dataclasses.field()

    pipelineName = field("pipelineName")

    @cached_property
    def filter(self):  # pragma: no cover
        return ActionExecutionFilter.make_one(self.boto3_raw_data["filter"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListActionExecutionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListActionExecutionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRuleExecutionsInputPaginate:
    boto3_raw_data: "type_defs.ListRuleExecutionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    pipelineName = field("pipelineName")

    @cached_property
    def filter(self):  # pragma: no cover
        return RuleExecutionFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRuleExecutionsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRuleExecutionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRuleExecutionsInput:
    boto3_raw_data: "type_defs.ListRuleExecutionsInputTypeDef" = dataclasses.field()

    pipelineName = field("pipelineName")

    @cached_property
    def filter(self):  # pragma: no cover
        return RuleExecutionFilter.make_one(self.boto3_raw_data["filter"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRuleExecutionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRuleExecutionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionState:
    boto3_raw_data: "type_defs.ActionStateTypeDef" = dataclasses.field()

    actionName = field("actionName")

    @cached_property
    def currentRevision(self):  # pragma: no cover
        return ActionRevisionOutput.make_one(self.boto3_raw_data["currentRevision"])

    @cached_property
    def latestExecution(self):  # pragma: no cover
        return ActionExecution.make_one(self.boto3_raw_data["latestExecution"])

    entityUrl = field("entityUrl")
    revisionUrl = field("revisionUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionStateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleExecutionOutput:
    boto3_raw_data: "type_defs.RuleExecutionOutputTypeDef" = dataclasses.field()

    @cached_property
    def executionResult(self):  # pragma: no cover
        return RuleExecutionResult.make_one(self.boto3_raw_data["executionResult"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleExecutionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleExecutionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleState:
    boto3_raw_data: "type_defs.RuleStateTypeDef" = dataclasses.field()

    ruleName = field("ruleName")

    @cached_property
    def currentRevision(self):  # pragma: no cover
        return RuleRevision.make_one(self.boto3_raw_data["currentRevision"])

    @cached_property
    def latestExecution(self):  # pragma: no cover
        return RuleExecution.make_one(self.boto3_raw_data["latestExecution"])

    entityUrl = field("entityUrl")
    revisionUrl = field("revisionUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleStateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutJobSuccessResultInput:
    boto3_raw_data: "type_defs.PutJobSuccessResultInputTypeDef" = dataclasses.field()

    jobId = field("jobId")

    @cached_property
    def currentRevision(self):  # pragma: no cover
        return CurrentRevision.make_one(self.boto3_raw_data["currentRevision"])

    continuationToken = field("continuationToken")

    @cached_property
    def executionDetails(self):  # pragma: no cover
        return ExecutionDetails.make_one(self.boto3_raw_data["executionDetails"])

    outputVariables = field("outputVariables")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutJobSuccessResultInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutJobSuccessResultInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutThirdPartyJobSuccessResultInput:
    boto3_raw_data: "type_defs.PutThirdPartyJobSuccessResultInputTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")
    clientToken = field("clientToken")

    @cached_property
    def currentRevision(self):  # pragma: no cover
        return CurrentRevision.make_one(self.boto3_raw_data["currentRevision"])

    continuationToken = field("continuationToken")

    @cached_property
    def executionDetails(self):  # pragma: no cover
        return ExecutionDetails.make_one(self.boto3_raw_data["executionDetails"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutThirdPartyJobSuccessResultInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutThirdPartyJobSuccessResultInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomActionTypeOutput:
    boto3_raw_data: "type_defs.CreateCustomActionTypeOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def actionType(self):  # pragma: no cover
        return ActionType.make_one(self.boto3_raw_data["actionType"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCustomActionTypeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomActionTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListActionTypesOutput:
    boto3_raw_data: "type_defs.ListActionTypesOutputTypeDef" = dataclasses.field()

    @cached_property
    def actionTypes(self):  # pragma: no cover
        return ActionType.make_many(self.boto3_raw_data["actionTypes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListActionTypesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListActionTypesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionExecutionInput:
    boto3_raw_data: "type_defs.ActionExecutionInputTypeDef" = dataclasses.field()

    @cached_property
    def actionTypeId(self):  # pragma: no cover
        return ActionTypeId.make_one(self.boto3_raw_data["actionTypeId"])

    configuration = field("configuration")
    resolvedConfiguration = field("resolvedConfiguration")
    roleArn = field("roleArn")
    region = field("region")

    @cached_property
    def inputArtifacts(self):  # pragma: no cover
        return ArtifactDetail.make_many(self.boto3_raw_data["inputArtifacts"])

    namespace = field("namespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionExecutionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionExecutionOutput:
    boto3_raw_data: "type_defs.ActionExecutionOutputTypeDef" = dataclasses.field()

    @cached_property
    def outputArtifacts(self):  # pragma: no cover
        return ArtifactDetail.make_many(self.boto3_raw_data["outputArtifacts"])

    @cached_property
    def executionResult(self):  # pragma: no cover
        return ActionExecutionResult.make_one(self.boto3_raw_data["executionResult"])

    outputVariables = field("outputVariables")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionExecutionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionExecutionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleExecutionInput:
    boto3_raw_data: "type_defs.RuleExecutionInputTypeDef" = dataclasses.field()

    @cached_property
    def ruleTypeId(self):  # pragma: no cover
        return RuleTypeId.make_one(self.boto3_raw_data["ruleTypeId"])

    configuration = field("configuration")
    resolvedConfiguration = field("resolvedConfiguration")
    roleArn = field("roleArn")
    region = field("region")

    @cached_property
    def inputArtifacts(self):  # pragma: no cover
        return ArtifactDetail.make_many(self.boto3_raw_data["inputArtifacts"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleExecutionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Artifact:
    boto3_raw_data: "type_defs.ArtifactTypeDef" = dataclasses.field()

    name = field("name")
    revision = field("revision")

    @cached_property
    def location(self):  # pragma: no cover
        return ArtifactLocation.make_one(self.boto3_raw_data["location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ArtifactTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ArtifactTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeployActionExecutionTarget:
    boto3_raw_data: "type_defs.DeployActionExecutionTargetTypeDef" = dataclasses.field()

    targetId = field("targetId")
    targetType = field("targetType")
    status = field("status")
    startTime = field("startTime")
    endTime = field("endTime")

    @cached_property
    def events(self):  # pragma: no cover
        return DeployTargetEvent.make_many(self.boto3_raw_data["events"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeployActionExecutionTargetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeployActionExecutionTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionTypeExecutorOutput:
    boto3_raw_data: "type_defs.ActionTypeExecutorOutputTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return ExecutorConfigurationOutput.make_one(
            self.boto3_raw_data["configuration"]
        )

    type = field("type")
    policyStatementsTemplate = field("policyStatementsTemplate")
    jobTimeout = field("jobTimeout")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionTypeExecutorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionTypeExecutorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionTypeExecutor:
    boto3_raw_data: "type_defs.ActionTypeExecutorTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return ExecutorConfiguration.make_one(self.boto3_raw_data["configuration"])

    type = field("type")
    policyStatementsTemplate = field("policyStatementsTemplate")
    jobTimeout = field("jobTimeout")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionTypeExecutorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionTypeExecutorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GitConfigurationOutput:
    boto3_raw_data: "type_defs.GitConfigurationOutputTypeDef" = dataclasses.field()

    sourceActionName = field("sourceActionName")

    @cached_property
    def push(self):  # pragma: no cover
        return GitPushFilterOutput.make_many(self.boto3_raw_data["push"])

    @cached_property
    def pullRequest(self):  # pragma: no cover
        return GitPullRequestFilterOutput.make_many(self.boto3_raw_data["pullRequest"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GitConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GitConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GitConfiguration:
    boto3_raw_data: "type_defs.GitConfigurationTypeDef" = dataclasses.field()

    sourceActionName = field("sourceActionName")

    @cached_property
    def push(self):  # pragma: no cover
        return GitPushFilter.make_many(self.boto3_raw_data["push"])

    @cached_property
    def pullRequest(self):  # pragma: no cover
        return GitPullRequestFilter.make_many(self.boto3_raw_data["pullRequest"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GitConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GitConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelineExecutionsInputPaginate:
    boto3_raw_data: "type_defs.ListPipelineExecutionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    pipelineName = field("pipelineName")

    @cached_property
    def filter(self):  # pragma: no cover
        return PipelineExecutionFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPipelineExecutionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelineExecutionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelineExecutionsInput:
    boto3_raw_data: "type_defs.ListPipelineExecutionsInputTypeDef" = dataclasses.field()

    pipelineName = field("pipelineName")
    maxResults = field("maxResults")

    @cached_property
    def filter(self):  # pragma: no cover
        return PipelineExecutionFilter.make_one(self.boto3_raw_data["filter"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPipelineExecutionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelineExecutionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelineExecutionsOutput:
    boto3_raw_data: "type_defs.ListPipelineExecutionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def pipelineExecutionSummaries(self):  # pragma: no cover
        return PipelineExecutionSummary.make_many(
            self.boto3_raw_data["pipelineExecutionSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPipelineExecutionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelineExecutionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPipelineExecutionOutput:
    boto3_raw_data: "type_defs.GetPipelineExecutionOutputTypeDef" = dataclasses.field()

    @cached_property
    def pipelineExecution(self):  # pragma: no cover
        return PipelineExecution.make_one(self.boto3_raw_data["pipelineExecution"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPipelineExecutionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPipelineExecutionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionOutput:
    boto3_raw_data: "type_defs.ConditionOutputTypeDef" = dataclasses.field()

    result = field("result")

    @cached_property
    def rules(self):  # pragma: no cover
        return RuleDeclarationOutput.make_many(self.boto3_raw_data["rules"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConditionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConditionOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Condition:
    boto3_raw_data: "type_defs.ConditionTypeDef" = dataclasses.field()

    result = field("result")

    @cached_property
    def rules(self):  # pragma: no cover
        return RuleDeclaration.make_many(self.boto3_raw_data["rules"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConditionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRuleTypesOutput:
    boto3_raw_data: "type_defs.ListRuleTypesOutputTypeDef" = dataclasses.field()

    @cached_property
    def ruleTypes(self):  # pragma: no cover
        return RuleType.make_many(self.boto3_raw_data["ruleTypes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRuleTypesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRuleTypesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWebhookItem:
    boto3_raw_data: "type_defs.ListWebhookItemTypeDef" = dataclasses.field()

    @cached_property
    def definition(self):  # pragma: no cover
        return WebhookDefinitionOutput.make_one(self.boto3_raw_data["definition"])

    url = field("url")
    errorMessage = field("errorMessage")
    errorCode = field("errorCode")
    lastTriggered = field("lastTriggered")
    arn = field("arn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListWebhookItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListWebhookItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionState:
    boto3_raw_data: "type_defs.ConditionStateTypeDef" = dataclasses.field()

    @cached_property
    def latestExecution(self):  # pragma: no cover
        return ConditionExecution.make_one(self.boto3_raw_data["latestExecution"])

    @cached_property
    def ruleStates(self):  # pragma: no cover
        return RuleState.make_many(self.boto3_raw_data["ruleStates"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConditionStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConditionStateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutActionRevisionInput:
    boto3_raw_data: "type_defs.PutActionRevisionInputTypeDef" = dataclasses.field()

    pipelineName = field("pipelineName")
    stageName = field("stageName")
    actionName = field("actionName")
    actionRevision = field("actionRevision")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutActionRevisionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutActionRevisionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionExecutionDetail:
    boto3_raw_data: "type_defs.ActionExecutionDetailTypeDef" = dataclasses.field()

    pipelineExecutionId = field("pipelineExecutionId")
    actionExecutionId = field("actionExecutionId")
    pipelineVersion = field("pipelineVersion")
    stageName = field("stageName")
    actionName = field("actionName")
    startTime = field("startTime")
    lastUpdateTime = field("lastUpdateTime")
    updatedBy = field("updatedBy")
    status = field("status")

    @cached_property
    def input(self):  # pragma: no cover
        return ActionExecutionInput.make_one(self.boto3_raw_data["input"])

    @cached_property
    def output(self):  # pragma: no cover
        return ActionExecutionOutput.make_one(self.boto3_raw_data["output"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionExecutionDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionExecutionDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleExecutionDetail:
    boto3_raw_data: "type_defs.RuleExecutionDetailTypeDef" = dataclasses.field()

    pipelineExecutionId = field("pipelineExecutionId")
    ruleExecutionId = field("ruleExecutionId")
    pipelineVersion = field("pipelineVersion")
    stageName = field("stageName")
    ruleName = field("ruleName")
    startTime = field("startTime")
    lastUpdateTime = field("lastUpdateTime")
    updatedBy = field("updatedBy")
    status = field("status")

    @cached_property
    def input(self):  # pragma: no cover
        return RuleExecutionInput.make_one(self.boto3_raw_data["input"])

    @cached_property
    def output(self):  # pragma: no cover
        return RuleExecutionOutput.make_one(self.boto3_raw_data["output"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleExecutionDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleExecutionDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobData:
    boto3_raw_data: "type_defs.JobDataTypeDef" = dataclasses.field()

    @cached_property
    def actionTypeId(self):  # pragma: no cover
        return ActionTypeId.make_one(self.boto3_raw_data["actionTypeId"])

    @cached_property
    def actionConfiguration(self):  # pragma: no cover
        return ActionConfiguration.make_one(self.boto3_raw_data["actionConfiguration"])

    @cached_property
    def pipelineContext(self):  # pragma: no cover
        return PipelineContext.make_one(self.boto3_raw_data["pipelineContext"])

    @cached_property
    def inputArtifacts(self):  # pragma: no cover
        return Artifact.make_many(self.boto3_raw_data["inputArtifacts"])

    @cached_property
    def outputArtifacts(self):  # pragma: no cover
        return Artifact.make_many(self.boto3_raw_data["outputArtifacts"])

    @cached_property
    def artifactCredentials(self):  # pragma: no cover
        return AWSSessionCredentials.make_one(
            self.boto3_raw_data["artifactCredentials"]
        )

    continuationToken = field("continuationToken")

    @cached_property
    def encryptionKey(self):  # pragma: no cover
        return EncryptionKey.make_one(self.boto3_raw_data["encryptionKey"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThirdPartyJobData:
    boto3_raw_data: "type_defs.ThirdPartyJobDataTypeDef" = dataclasses.field()

    @cached_property
    def actionTypeId(self):  # pragma: no cover
        return ActionTypeId.make_one(self.boto3_raw_data["actionTypeId"])

    @cached_property
    def actionConfiguration(self):  # pragma: no cover
        return ActionConfiguration.make_one(self.boto3_raw_data["actionConfiguration"])

    @cached_property
    def pipelineContext(self):  # pragma: no cover
        return PipelineContext.make_one(self.boto3_raw_data["pipelineContext"])

    @cached_property
    def inputArtifacts(self):  # pragma: no cover
        return Artifact.make_many(self.boto3_raw_data["inputArtifacts"])

    @cached_property
    def outputArtifacts(self):  # pragma: no cover
        return Artifact.make_many(self.boto3_raw_data["outputArtifacts"])

    @cached_property
    def artifactCredentials(self):  # pragma: no cover
        return AWSSessionCredentials.make_one(
            self.boto3_raw_data["artifactCredentials"]
        )

    continuationToken = field("continuationToken")

    @cached_property
    def encryptionKey(self):  # pragma: no cover
        return EncryptionKey.make_one(self.boto3_raw_data["encryptionKey"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThirdPartyJobDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThirdPartyJobDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeployActionExecutionTargetsOutput:
    boto3_raw_data: "type_defs.ListDeployActionExecutionTargetsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def targets(self):  # pragma: no cover
        return DeployActionExecutionTarget.make_many(self.boto3_raw_data["targets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDeployActionExecutionTargetsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeployActionExecutionTargetsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionTypeDeclarationOutput:
    boto3_raw_data: "type_defs.ActionTypeDeclarationOutputTypeDef" = dataclasses.field()

    @cached_property
    def executor(self):  # pragma: no cover
        return ActionTypeExecutorOutput.make_one(self.boto3_raw_data["executor"])

    @cached_property
    def id(self):  # pragma: no cover
        return ActionTypeIdentifier.make_one(self.boto3_raw_data["id"])

    @cached_property
    def inputArtifactDetails(self):  # pragma: no cover
        return ActionTypeArtifactDetails.make_one(
            self.boto3_raw_data["inputArtifactDetails"]
        )

    @cached_property
    def outputArtifactDetails(self):  # pragma: no cover
        return ActionTypeArtifactDetails.make_one(
            self.boto3_raw_data["outputArtifactDetails"]
        )

    description = field("description")

    @cached_property
    def permissions(self):  # pragma: no cover
        return ActionTypePermissionsOutput.make_one(self.boto3_raw_data["permissions"])

    @cached_property
    def properties(self):  # pragma: no cover
        return ActionTypeProperty.make_many(self.boto3_raw_data["properties"])

    @cached_property
    def urls(self):  # pragma: no cover
        return ActionTypeUrls.make_one(self.boto3_raw_data["urls"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionTypeDeclarationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionTypeDeclarationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionTypeDeclaration:
    boto3_raw_data: "type_defs.ActionTypeDeclarationTypeDef" = dataclasses.field()

    @cached_property
    def executor(self):  # pragma: no cover
        return ActionTypeExecutor.make_one(self.boto3_raw_data["executor"])

    @cached_property
    def id(self):  # pragma: no cover
        return ActionTypeIdentifier.make_one(self.boto3_raw_data["id"])

    @cached_property
    def inputArtifactDetails(self):  # pragma: no cover
        return ActionTypeArtifactDetails.make_one(
            self.boto3_raw_data["inputArtifactDetails"]
        )

    @cached_property
    def outputArtifactDetails(self):  # pragma: no cover
        return ActionTypeArtifactDetails.make_one(
            self.boto3_raw_data["outputArtifactDetails"]
        )

    description = field("description")

    @cached_property
    def permissions(self):  # pragma: no cover
        return ActionTypePermissions.make_one(self.boto3_raw_data["permissions"])

    @cached_property
    def properties(self):  # pragma: no cover
        return ActionTypeProperty.make_many(self.boto3_raw_data["properties"])

    @cached_property
    def urls(self):  # pragma: no cover
        return ActionTypeUrls.make_one(self.boto3_raw_data["urls"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionTypeDeclarationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionTypeDeclarationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineTriggerDeclarationOutput:
    boto3_raw_data: "type_defs.PipelineTriggerDeclarationOutputTypeDef" = (
        dataclasses.field()
    )

    providerType = field("providerType")

    @cached_property
    def gitConfiguration(self):  # pragma: no cover
        return GitConfigurationOutput.make_one(self.boto3_raw_data["gitConfiguration"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PipelineTriggerDeclarationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineTriggerDeclarationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineTriggerDeclaration:
    boto3_raw_data: "type_defs.PipelineTriggerDeclarationTypeDef" = dataclasses.field()

    providerType = field("providerType")

    @cached_property
    def gitConfiguration(self):  # pragma: no cover
        return GitConfiguration.make_one(self.boto3_raw_data["gitConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipelineTriggerDeclarationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineTriggerDeclarationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BeforeEntryConditionsOutput:
    boto3_raw_data: "type_defs.BeforeEntryConditionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def conditions(self):  # pragma: no cover
        return ConditionOutput.make_many(self.boto3_raw_data["conditions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BeforeEntryConditionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BeforeEntryConditionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailureConditionsOutput:
    boto3_raw_data: "type_defs.FailureConditionsOutputTypeDef" = dataclasses.field()

    result = field("result")

    @cached_property
    def retryConfiguration(self):  # pragma: no cover
        return RetryConfiguration.make_one(self.boto3_raw_data["retryConfiguration"])

    @cached_property
    def conditions(self):  # pragma: no cover
        return ConditionOutput.make_many(self.boto3_raw_data["conditions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailureConditionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailureConditionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuccessConditionsOutput:
    boto3_raw_data: "type_defs.SuccessConditionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def conditions(self):  # pragma: no cover
        return ConditionOutput.make_many(self.boto3_raw_data["conditions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuccessConditionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuccessConditionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BeforeEntryConditions:
    boto3_raw_data: "type_defs.BeforeEntryConditionsTypeDef" = dataclasses.field()

    @cached_property
    def conditions(self):  # pragma: no cover
        return Condition.make_many(self.boto3_raw_data["conditions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BeforeEntryConditionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BeforeEntryConditionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailureConditions:
    boto3_raw_data: "type_defs.FailureConditionsTypeDef" = dataclasses.field()

    result = field("result")

    @cached_property
    def retryConfiguration(self):  # pragma: no cover
        return RetryConfiguration.make_one(self.boto3_raw_data["retryConfiguration"])

    @cached_property
    def conditions(self):  # pragma: no cover
        return Condition.make_many(self.boto3_raw_data["conditions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailureConditionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailureConditionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuccessConditions:
    boto3_raw_data: "type_defs.SuccessConditionsTypeDef" = dataclasses.field()

    @cached_property
    def conditions(self):  # pragma: no cover
        return Condition.make_many(self.boto3_raw_data["conditions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SuccessConditionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuccessConditionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWebhooksOutput:
    boto3_raw_data: "type_defs.ListWebhooksOutputTypeDef" = dataclasses.field()

    @cached_property
    def webhooks(self):  # pragma: no cover
        return ListWebhookItem.make_many(self.boto3_raw_data["webhooks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWebhooksOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWebhooksOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutWebhookOutput:
    boto3_raw_data: "type_defs.PutWebhookOutputTypeDef" = dataclasses.field()

    @cached_property
    def webhook(self):  # pragma: no cover
        return ListWebhookItem.make_one(self.boto3_raw_data["webhook"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutWebhookOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutWebhookOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutWebhookInput:
    boto3_raw_data: "type_defs.PutWebhookInputTypeDef" = dataclasses.field()

    webhook = field("webhook")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutWebhookInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutWebhookInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StageConditionState:
    boto3_raw_data: "type_defs.StageConditionStateTypeDef" = dataclasses.field()

    @cached_property
    def latestExecution(self):  # pragma: no cover
        return StageConditionsExecution.make_one(self.boto3_raw_data["latestExecution"])

    @cached_property
    def conditionStates(self):  # pragma: no cover
        return ConditionState.make_many(self.boto3_raw_data["conditionStates"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StageConditionStateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StageConditionStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListActionExecutionsOutput:
    boto3_raw_data: "type_defs.ListActionExecutionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def actionExecutionDetails(self):  # pragma: no cover
        return ActionExecutionDetail.make_many(
            self.boto3_raw_data["actionExecutionDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListActionExecutionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListActionExecutionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRuleExecutionsOutput:
    boto3_raw_data: "type_defs.ListRuleExecutionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def ruleExecutionDetails(self):  # pragma: no cover
        return RuleExecutionDetail.make_many(
            self.boto3_raw_data["ruleExecutionDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRuleExecutionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRuleExecutionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobDetails:
    boto3_raw_data: "type_defs.JobDetailsTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def data(self):  # pragma: no cover
        return JobData.make_one(self.boto3_raw_data["data"])

    accountId = field("accountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobDetailsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Job:
    boto3_raw_data: "type_defs.JobTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def data(self):  # pragma: no cover
        return JobData.make_one(self.boto3_raw_data["data"])

    nonce = field("nonce")
    accountId = field("accountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThirdPartyJobDetails:
    boto3_raw_data: "type_defs.ThirdPartyJobDetailsTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def data(self):  # pragma: no cover
        return ThirdPartyJobData.make_one(self.boto3_raw_data["data"])

    nonce = field("nonce")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ThirdPartyJobDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThirdPartyJobDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetActionTypeOutput:
    boto3_raw_data: "type_defs.GetActionTypeOutputTypeDef" = dataclasses.field()

    @cached_property
    def actionType(self):  # pragma: no cover
        return ActionTypeDeclarationOutput.make_one(self.boto3_raw_data["actionType"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetActionTypeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetActionTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StageDeclarationOutput:
    boto3_raw_data: "type_defs.StageDeclarationOutputTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def actions(self):  # pragma: no cover
        return ActionDeclarationOutput.make_many(self.boto3_raw_data["actions"])

    @cached_property
    def blockers(self):  # pragma: no cover
        return BlockerDeclaration.make_many(self.boto3_raw_data["blockers"])

    @cached_property
    def onFailure(self):  # pragma: no cover
        return FailureConditionsOutput.make_one(self.boto3_raw_data["onFailure"])

    @cached_property
    def onSuccess(self):  # pragma: no cover
        return SuccessConditionsOutput.make_one(self.boto3_raw_data["onSuccess"])

    @cached_property
    def beforeEntry(self):  # pragma: no cover
        return BeforeEntryConditionsOutput.make_one(self.boto3_raw_data["beforeEntry"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StageDeclarationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StageDeclarationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StageDeclaration:
    boto3_raw_data: "type_defs.StageDeclarationTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def actions(self):  # pragma: no cover
        return ActionDeclaration.make_many(self.boto3_raw_data["actions"])

    @cached_property
    def blockers(self):  # pragma: no cover
        return BlockerDeclaration.make_many(self.boto3_raw_data["blockers"])

    @cached_property
    def onFailure(self):  # pragma: no cover
        return FailureConditions.make_one(self.boto3_raw_data["onFailure"])

    @cached_property
    def onSuccess(self):  # pragma: no cover
        return SuccessConditions.make_one(self.boto3_raw_data["onSuccess"])

    @cached_property
    def beforeEntry(self):  # pragma: no cover
        return BeforeEntryConditions.make_one(self.boto3_raw_data["beforeEntry"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StageDeclarationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StageDeclarationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StageState:
    boto3_raw_data: "type_defs.StageStateTypeDef" = dataclasses.field()

    stageName = field("stageName")

    @cached_property
    def inboundExecution(self):  # pragma: no cover
        return StageExecution.make_one(self.boto3_raw_data["inboundExecution"])

    @cached_property
    def inboundExecutions(self):  # pragma: no cover
        return StageExecution.make_many(self.boto3_raw_data["inboundExecutions"])

    @cached_property
    def inboundTransitionState(self):  # pragma: no cover
        return TransitionState.make_one(self.boto3_raw_data["inboundTransitionState"])

    @cached_property
    def actionStates(self):  # pragma: no cover
        return ActionState.make_many(self.boto3_raw_data["actionStates"])

    @cached_property
    def latestExecution(self):  # pragma: no cover
        return StageExecution.make_one(self.boto3_raw_data["latestExecution"])

    @cached_property
    def beforeEntryConditionState(self):  # pragma: no cover
        return StageConditionState.make_one(
            self.boto3_raw_data["beforeEntryConditionState"]
        )

    @cached_property
    def onSuccessConditionState(self):  # pragma: no cover
        return StageConditionState.make_one(
            self.boto3_raw_data["onSuccessConditionState"]
        )

    @cached_property
    def onFailureConditionState(self):  # pragma: no cover
        return StageConditionState.make_one(
            self.boto3_raw_data["onFailureConditionState"]
        )

    @cached_property
    def retryStageMetadata(self):  # pragma: no cover
        return RetryStageMetadata.make_one(self.boto3_raw_data["retryStageMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StageStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StageStateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobDetailsOutput:
    boto3_raw_data: "type_defs.GetJobDetailsOutputTypeDef" = dataclasses.field()

    @cached_property
    def jobDetails(self):  # pragma: no cover
        return JobDetails.make_one(self.boto3_raw_data["jobDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetJobDetailsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJobDetailsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PollForJobsOutput:
    boto3_raw_data: "type_defs.PollForJobsOutputTypeDef" = dataclasses.field()

    @cached_property
    def jobs(self):  # pragma: no cover
        return Job.make_many(self.boto3_raw_data["jobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PollForJobsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PollForJobsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetThirdPartyJobDetailsOutput:
    boto3_raw_data: "type_defs.GetThirdPartyJobDetailsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def jobDetails(self):  # pragma: no cover
        return ThirdPartyJobDetails.make_one(self.boto3_raw_data["jobDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetThirdPartyJobDetailsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetThirdPartyJobDetailsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateActionTypeInput:
    boto3_raw_data: "type_defs.UpdateActionTypeInputTypeDef" = dataclasses.field()

    actionType = field("actionType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateActionTypeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateActionTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineDeclarationOutput:
    boto3_raw_data: "type_defs.PipelineDeclarationOutputTypeDef" = dataclasses.field()

    name = field("name")
    roleArn = field("roleArn")

    @cached_property
    def stages(self):  # pragma: no cover
        return StageDeclarationOutput.make_many(self.boto3_raw_data["stages"])

    @cached_property
    def artifactStore(self):  # pragma: no cover
        return ArtifactStore.make_one(self.boto3_raw_data["artifactStore"])

    artifactStores = field("artifactStores")
    version = field("version")
    executionMode = field("executionMode")
    pipelineType = field("pipelineType")

    @cached_property
    def variables(self):  # pragma: no cover
        return PipelineVariableDeclaration.make_many(self.boto3_raw_data["variables"])

    @cached_property
    def triggers(self):  # pragma: no cover
        return PipelineTriggerDeclarationOutput.make_many(
            self.boto3_raw_data["triggers"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipelineDeclarationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineDeclarationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineDeclaration:
    boto3_raw_data: "type_defs.PipelineDeclarationTypeDef" = dataclasses.field()

    name = field("name")
    roleArn = field("roleArn")

    @cached_property
    def stages(self):  # pragma: no cover
        return StageDeclaration.make_many(self.boto3_raw_data["stages"])

    @cached_property
    def artifactStore(self):  # pragma: no cover
        return ArtifactStore.make_one(self.boto3_raw_data["artifactStore"])

    artifactStores = field("artifactStores")
    version = field("version")
    executionMode = field("executionMode")
    pipelineType = field("pipelineType")

    @cached_property
    def variables(self):  # pragma: no cover
        return PipelineVariableDeclaration.make_many(self.boto3_raw_data["variables"])

    @cached_property
    def triggers(self):  # pragma: no cover
        return PipelineTriggerDeclaration.make_many(self.boto3_raw_data["triggers"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipelineDeclarationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineDeclarationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPipelineStateOutput:
    boto3_raw_data: "type_defs.GetPipelineStateOutputTypeDef" = dataclasses.field()

    pipelineName = field("pipelineName")
    pipelineVersion = field("pipelineVersion")

    @cached_property
    def stageStates(self):  # pragma: no cover
        return StageState.make_many(self.boto3_raw_data["stageStates"])

    created = field("created")
    updated = field("updated")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPipelineStateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPipelineStateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePipelineOutput:
    boto3_raw_data: "type_defs.CreatePipelineOutputTypeDef" = dataclasses.field()

    @cached_property
    def pipeline(self):  # pragma: no cover
        return PipelineDeclarationOutput.make_one(self.boto3_raw_data["pipeline"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePipelineOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePipelineOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPipelineOutput:
    boto3_raw_data: "type_defs.GetPipelineOutputTypeDef" = dataclasses.field()

    @cached_property
    def pipeline(self):  # pragma: no cover
        return PipelineDeclarationOutput.make_one(self.boto3_raw_data["pipeline"])

    @cached_property
    def metadata(self):  # pragma: no cover
        return PipelineMetadata.make_one(self.boto3_raw_data["metadata"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPipelineOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPipelineOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePipelineOutput:
    boto3_raw_data: "type_defs.UpdatePipelineOutputTypeDef" = dataclasses.field()

    @cached_property
    def pipeline(self):  # pragma: no cover
        return PipelineDeclarationOutput.make_one(self.boto3_raw_data["pipeline"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePipelineOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePipelineOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePipelineInput:
    boto3_raw_data: "type_defs.CreatePipelineInputTypeDef" = dataclasses.field()

    pipeline = field("pipeline")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePipelineInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePipelineInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePipelineInput:
    boto3_raw_data: "type_defs.UpdatePipelineInputTypeDef" = dataclasses.field()

    pipeline = field("pipeline")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePipelineInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePipelineInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
