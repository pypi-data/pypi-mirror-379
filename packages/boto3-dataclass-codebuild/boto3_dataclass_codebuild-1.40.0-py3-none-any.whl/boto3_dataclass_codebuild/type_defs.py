# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_codebuild import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AutoRetryConfig:
    boto3_raw_data: "type_defs.AutoRetryConfigTypeDef" = dataclasses.field()

    autoRetryLimit = field("autoRetryLimit")
    autoRetryNumber = field("autoRetryNumber")
    nextAutoRetry = field("nextAutoRetry")
    previousAutoRetry = field("previousAutoRetry")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoRetryConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AutoRetryConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteBuildsInput:
    boto3_raw_data: "type_defs.BatchDeleteBuildsInputTypeDef" = dataclasses.field()

    ids = field("ids")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteBuildsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteBuildsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BuildNotDeleted:
    boto3_raw_data: "type_defs.BuildNotDeletedTypeDef" = dataclasses.field()

    id = field("id")
    statusCode = field("statusCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BuildNotDeletedTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BuildNotDeletedTypeDef"]],
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
class BatchGetBuildBatchesInput:
    boto3_raw_data: "type_defs.BatchGetBuildBatchesInputTypeDef" = dataclasses.field()

    ids = field("ids")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetBuildBatchesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetBuildBatchesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetBuildsInput:
    boto3_raw_data: "type_defs.BatchGetBuildsInputTypeDef" = dataclasses.field()

    ids = field("ids")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetBuildsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetBuildsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetCommandExecutionsInput:
    boto3_raw_data: "type_defs.BatchGetCommandExecutionsInputTypeDef" = (
        dataclasses.field()
    )

    sandboxId = field("sandboxId")
    commandExecutionIds = field("commandExecutionIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetCommandExecutionsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetCommandExecutionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetFleetsInput:
    boto3_raw_data: "type_defs.BatchGetFleetsInputTypeDef" = dataclasses.field()

    names = field("names")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetFleetsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetFleetsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetProjectsInput:
    boto3_raw_data: "type_defs.BatchGetProjectsInputTypeDef" = dataclasses.field()

    names = field("names")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetProjectsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetProjectsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetReportGroupsInput:
    boto3_raw_data: "type_defs.BatchGetReportGroupsInputTypeDef" = dataclasses.field()

    reportGroupArns = field("reportGroupArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetReportGroupsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetReportGroupsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetReportsInput:
    boto3_raw_data: "type_defs.BatchGetReportsInputTypeDef" = dataclasses.field()

    reportArns = field("reportArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetReportsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetReportsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetSandboxesInput:
    boto3_raw_data: "type_defs.BatchGetSandboxesInputTypeDef" = dataclasses.field()

    ids = field("ids")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetSandboxesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetSandboxesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchRestrictionsOutput:
    boto3_raw_data: "type_defs.BatchRestrictionsOutputTypeDef" = dataclasses.field()

    maximumBuildsAllowed = field("maximumBuildsAllowed")
    computeTypesAllowed = field("computeTypesAllowed")
    fleetsAllowed = field("fleetsAllowed")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchRestrictionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchRestrictionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchRestrictions:
    boto3_raw_data: "type_defs.BatchRestrictionsTypeDef" = dataclasses.field()

    maximumBuildsAllowed = field("maximumBuildsAllowed")
    computeTypesAllowed = field("computeTypesAllowed")
    fleetsAllowed = field("fleetsAllowed")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchRestrictionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchRestrictionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BuildArtifacts:
    boto3_raw_data: "type_defs.BuildArtifactsTypeDef" = dataclasses.field()

    location = field("location")
    sha256sum = field("sha256sum")
    md5sum = field("md5sum")
    overrideArtifactName = field("overrideArtifactName")
    encryptionDisabled = field("encryptionDisabled")
    artifactIdentifier = field("artifactIdentifier")
    bucketOwnerAccess = field("bucketOwnerAccess")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BuildArtifactsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BuildArtifactsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BuildBatchFilter:
    boto3_raw_data: "type_defs.BuildBatchFilterTypeDef" = dataclasses.field()

    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BuildBatchFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BuildBatchFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhaseContext:
    boto3_raw_data: "type_defs.PhaseContextTypeDef" = dataclasses.field()

    statusCode = field("statusCode")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PhaseContextTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PhaseContextTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectCacheOutput:
    boto3_raw_data: "type_defs.ProjectCacheOutputTypeDef" = dataclasses.field()

    type = field("type")
    location = field("location")
    modes = field("modes")
    cacheNamespace = field("cacheNamespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProjectCacheOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectCacheOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectFileSystemLocation:
    boto3_raw_data: "type_defs.ProjectFileSystemLocationTypeDef" = dataclasses.field()

    type = field("type")
    location = field("location")
    mountPoint = field("mountPoint")
    identifier = field("identifier")
    mountOptions = field("mountOptions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProjectFileSystemLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectFileSystemLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectSourceVersion:
    boto3_raw_data: "type_defs.ProjectSourceVersionTypeDef" = dataclasses.field()

    sourceIdentifier = field("sourceIdentifier")
    sourceVersion = field("sourceVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProjectSourceVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectSourceVersionTypeDef"]
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

    vpcId = field("vpcId")
    subnets = field("subnets")
    securityGroupIds = field("securityGroupIds")

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
class BuildStatusConfig:
    boto3_raw_data: "type_defs.BuildStatusConfigTypeDef" = dataclasses.field()

    context = field("context")
    targetUrl = field("targetUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BuildStatusConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BuildStatusConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolvedArtifact:
    boto3_raw_data: "type_defs.ResolvedArtifactTypeDef" = dataclasses.field()

    type = field("type")
    location = field("location")
    identifier = field("identifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResolvedArtifactTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResolvedArtifactTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DebugSession:
    boto3_raw_data: "type_defs.DebugSessionTypeDef" = dataclasses.field()

    sessionEnabled = field("sessionEnabled")
    sessionTarget = field("sessionTarget")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DebugSessionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DebugSessionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportedEnvironmentVariable:
    boto3_raw_data: "type_defs.ExportedEnvironmentVariableTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportedEnvironmentVariableTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportedEnvironmentVariableTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkInterface:
    boto3_raw_data: "type_defs.NetworkInterfaceTypeDef" = dataclasses.field()

    subnetId = field("subnetId")
    networkInterfaceId = field("networkInterfaceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkInterfaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkInterfaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchLogsConfig:
    boto3_raw_data: "type_defs.CloudWatchLogsConfigTypeDef" = dataclasses.field()

    status = field("status")
    groupName = field("groupName")
    streamName = field("streamName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchLogsConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLogsConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeCoverageReportSummary:
    boto3_raw_data: "type_defs.CodeCoverageReportSummaryTypeDef" = dataclasses.field()

    lineCoveragePercentage = field("lineCoveragePercentage")
    linesCovered = field("linesCovered")
    linesMissed = field("linesMissed")
    branchCoveragePercentage = field("branchCoveragePercentage")
    branchesCovered = field("branchesCovered")
    branchesMissed = field("branchesMissed")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodeCoverageReportSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeCoverageReportSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeCoverage:
    boto3_raw_data: "type_defs.CodeCoverageTypeDef" = dataclasses.field()

    id = field("id")
    reportARN = field("reportARN")
    filePath = field("filePath")
    lineCoveragePercentage = field("lineCoveragePercentage")
    linesCovered = field("linesCovered")
    linesMissed = field("linesMissed")
    branchCoveragePercentage = field("branchCoveragePercentage")
    branchesCovered = field("branchesCovered")
    branchesMissed = field("branchesMissed")
    expired = field("expired")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodeCoverageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CodeCoverageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeConfiguration:
    boto3_raw_data: "type_defs.ComputeConfigurationTypeDef" = dataclasses.field()

    vCpu = field("vCpu")
    memory = field("memory")
    disk = field("disk")
    machineType = field("machineType")
    instanceType = field("instanceType")

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
class ProjectArtifacts:
    boto3_raw_data: "type_defs.ProjectArtifactsTypeDef" = dataclasses.field()

    type = field("type")
    location = field("location")
    path = field("path")
    namespaceType = field("namespaceType")
    name = field("name")
    packaging = field("packaging")
    overrideArtifactName = field("overrideArtifactName")
    encryptionDisabled = field("encryptionDisabled")
    artifactIdentifier = field("artifactIdentifier")
    bucketOwnerAccess = field("bucketOwnerAccess")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProjectArtifactsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectArtifactsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScopeConfiguration:
    boto3_raw_data: "type_defs.ScopeConfigurationTypeDef" = dataclasses.field()

    name = field("name")
    scope = field("scope")
    domain = field("domain")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScopeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScopeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebhookFilter:
    boto3_raw_data: "type_defs.WebhookFilterTypeDef" = dataclasses.field()

    type = field("type")
    pattern = field("pattern")
    excludeMatchedPattern = field("excludeMatchedPattern")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WebhookFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WebhookFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBuildBatchInput:
    boto3_raw_data: "type_defs.DeleteBuildBatchInputTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBuildBatchInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBuildBatchInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFleetInput:
    boto3_raw_data: "type_defs.DeleteFleetInputTypeDef" = dataclasses.field()

    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteFleetInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFleetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProjectInput:
    boto3_raw_data: "type_defs.DeleteProjectInputTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProjectInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProjectInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReportGroupInput:
    boto3_raw_data: "type_defs.DeleteReportGroupInputTypeDef" = dataclasses.field()

    arn = field("arn")
    deleteReports = field("deleteReports")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteReportGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReportGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReportInput:
    boto3_raw_data: "type_defs.DeleteReportInputTypeDef" = dataclasses.field()

    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteReportInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReportInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourcePolicyInput:
    boto3_raw_data: "type_defs.DeleteResourcePolicyInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourcePolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourcePolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSourceCredentialsInput:
    boto3_raw_data: "type_defs.DeleteSourceCredentialsInputTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSourceCredentialsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSourceCredentialsInputTypeDef"]
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

    projectName = field("projectName")

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
class DescribeCodeCoveragesInput:
    boto3_raw_data: "type_defs.DescribeCodeCoveragesInputTypeDef" = dataclasses.field()

    reportArn = field("reportArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    sortOrder = field("sortOrder")
    sortBy = field("sortBy")
    minLineCoveragePercentage = field("minLineCoveragePercentage")
    maxLineCoveragePercentage = field("maxLineCoveragePercentage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCodeCoveragesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCodeCoveragesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestCaseFilter:
    boto3_raw_data: "type_defs.TestCaseFilterTypeDef" = dataclasses.field()

    status = field("status")
    keyword = field("keyword")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestCaseFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TestCaseFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestCase:
    boto3_raw_data: "type_defs.TestCaseTypeDef" = dataclasses.field()

    reportArn = field("reportArn")
    testRawDataPath = field("testRawDataPath")
    prefix = field("prefix")
    name = field("name")
    status = field("status")
    durationInNanoSeconds = field("durationInNanoSeconds")
    message = field("message")
    expired = field("expired")
    testSuiteName = field("testSuiteName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestCaseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TestCaseTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DockerServerStatus:
    boto3_raw_data: "type_defs.DockerServerStatusTypeDef" = dataclasses.field()

    status = field("status")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DockerServerStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DockerServerStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentImage:
    boto3_raw_data: "type_defs.EnvironmentImageTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    versions = field("versions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnvironmentImageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentImageTypeDef"]
        ],
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
class FleetProxyRuleOutput:
    boto3_raw_data: "type_defs.FleetProxyRuleOutputTypeDef" = dataclasses.field()

    type = field("type")
    effect = field("effect")
    entities = field("entities")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FleetProxyRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FleetProxyRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FleetProxyRule:
    boto3_raw_data: "type_defs.FleetProxyRuleTypeDef" = dataclasses.field()

    type = field("type")
    effect = field("effect")
    entities = field("entities")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FleetProxyRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FleetProxyRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FleetStatus:
    boto3_raw_data: "type_defs.FleetStatusTypeDef" = dataclasses.field()

    statusCode = field("statusCode")
    context = field("context")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FleetStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FleetStatusTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReportGroupTrendInput:
    boto3_raw_data: "type_defs.GetReportGroupTrendInputTypeDef" = dataclasses.field()

    reportGroupArn = field("reportGroupArn")
    trendField = field("trendField")
    numOfReports = field("numOfReports")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReportGroupTrendInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReportGroupTrendInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportGroupTrendStats:
    boto3_raw_data: "type_defs.ReportGroupTrendStatsTypeDef" = dataclasses.field()

    average = field("average")
    max = field("max")
    min = field("min")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReportGroupTrendStatsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReportGroupTrendStatsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportWithRawData:
    boto3_raw_data: "type_defs.ReportWithRawDataTypeDef" = dataclasses.field()

    reportArn = field("reportArn")
    data = field("data")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReportWithRawDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReportWithRawDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyInput:
    boto3_raw_data: "type_defs.GetResourcePolicyInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GitSubmodulesConfig:
    boto3_raw_data: "type_defs.GitSubmodulesConfigTypeDef" = dataclasses.field()

    fetchSubmodules = field("fetchSubmodules")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GitSubmodulesConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GitSubmodulesConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportSourceCredentialsInput:
    boto3_raw_data: "type_defs.ImportSourceCredentialsInputTypeDef" = (
        dataclasses.field()
    )

    token = field("token")
    serverType = field("serverType")
    authType = field("authType")
    username = field("username")
    shouldOverwrite = field("shouldOverwrite")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportSourceCredentialsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportSourceCredentialsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvalidateProjectCacheInput:
    boto3_raw_data: "type_defs.InvalidateProjectCacheInputTypeDef" = dataclasses.field()

    projectName = field("projectName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvalidateProjectCacheInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvalidateProjectCacheInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBuildsForProjectInput:
    boto3_raw_data: "type_defs.ListBuildsForProjectInputTypeDef" = dataclasses.field()

    projectName = field("projectName")
    sortOrder = field("sortOrder")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBuildsForProjectInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBuildsForProjectInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBuildsInput:
    boto3_raw_data: "type_defs.ListBuildsInputTypeDef" = dataclasses.field()

    sortOrder = field("sortOrder")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListBuildsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListBuildsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCommandExecutionsForSandboxInput:
    boto3_raw_data: "type_defs.ListCommandExecutionsForSandboxInputTypeDef" = (
        dataclasses.field()
    )

    sandboxId = field("sandboxId")
    maxResults = field("maxResults")
    sortOrder = field("sortOrder")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCommandExecutionsForSandboxInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCommandExecutionsForSandboxInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetsInput:
    boto3_raw_data: "type_defs.ListFleetsInputTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    sortOrder = field("sortOrder")
    sortBy = field("sortBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListFleetsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListFleetsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectsInput:
    boto3_raw_data: "type_defs.ListProjectsInputTypeDef" = dataclasses.field()

    sortBy = field("sortBy")
    sortOrder = field("sortOrder")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListProjectsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReportGroupsInput:
    boto3_raw_data: "type_defs.ListReportGroupsInputTypeDef" = dataclasses.field()

    sortOrder = field("sortOrder")
    sortBy = field("sortBy")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReportGroupsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReportGroupsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportFilter:
    boto3_raw_data: "type_defs.ReportFilterTypeDef" = dataclasses.field()

    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReportFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReportFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSandboxesForProjectInput:
    boto3_raw_data: "type_defs.ListSandboxesForProjectInputTypeDef" = (
        dataclasses.field()
    )

    projectName = field("projectName")
    maxResults = field("maxResults")
    sortOrder = field("sortOrder")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSandboxesForProjectInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSandboxesForProjectInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSandboxesInput:
    boto3_raw_data: "type_defs.ListSandboxesInputTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    sortOrder = field("sortOrder")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSandboxesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSandboxesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSharedProjectsInput:
    boto3_raw_data: "type_defs.ListSharedProjectsInputTypeDef" = dataclasses.field()

    sortBy = field("sortBy")
    sortOrder = field("sortOrder")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSharedProjectsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSharedProjectsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSharedReportGroupsInput:
    boto3_raw_data: "type_defs.ListSharedReportGroupsInputTypeDef" = dataclasses.field()

    sortOrder = field("sortOrder")
    sortBy = field("sortBy")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSharedReportGroupsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSharedReportGroupsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceCredentialsInfo:
    boto3_raw_data: "type_defs.SourceCredentialsInfoTypeDef" = dataclasses.field()

    arn = field("arn")
    serverType = field("serverType")
    authType = field("authType")
    resource = field("resource")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceCredentialsInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceCredentialsInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3LogsConfig:
    boto3_raw_data: "type_defs.S3LogsConfigTypeDef" = dataclasses.field()

    status = field("status")
    location = field("location")
    encryptionDisabled = field("encryptionDisabled")
    bucketOwnerAccess = field("bucketOwnerAccess")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3LogsConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3LogsConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectBadge:
    boto3_raw_data: "type_defs.ProjectBadgeTypeDef" = dataclasses.field()

    badgeEnabled = field("badgeEnabled")
    badgeRequestUrl = field("badgeRequestUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProjectBadgeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProjectBadgeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectCache:
    boto3_raw_data: "type_defs.ProjectCacheTypeDef" = dataclasses.field()

    type = field("type")
    location = field("location")
    modes = field("modes")
    cacheNamespace = field("cacheNamespace")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProjectCacheTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProjectCacheTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectFleet:
    boto3_raw_data: "type_defs.ProjectFleetTypeDef" = dataclasses.field()

    fleetArn = field("fleetArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProjectFleetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProjectFleetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistryCredential:
    boto3_raw_data: "type_defs.RegistryCredentialTypeDef" = dataclasses.field()

    credential = field("credential")
    credentialProvider = field("credentialProvider")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegistryCredentialTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistryCredentialTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceAuth:
    boto3_raw_data: "type_defs.SourceAuthTypeDef" = dataclasses.field()

    type = field("type")
    resource = field("resource")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceAuthTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceAuthTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PullRequestBuildPolicyOutput:
    boto3_raw_data: "type_defs.PullRequestBuildPolicyOutputTypeDef" = (
        dataclasses.field()
    )

    requiresCommentApproval = field("requiresCommentApproval")
    approverRoles = field("approverRoles")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PullRequestBuildPolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PullRequestBuildPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PullRequestBuildPolicy:
    boto3_raw_data: "type_defs.PullRequestBuildPolicyTypeDef" = dataclasses.field()

    requiresCommentApproval = field("requiresCommentApproval")
    approverRoles = field("approverRoles")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PullRequestBuildPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PullRequestBuildPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyInput:
    boto3_raw_data: "type_defs.PutResourcePolicyInputTypeDef" = dataclasses.field()

    policy = field("policy")
    resourceArn = field("resourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ReportExportConfig:
    boto3_raw_data: "type_defs.S3ReportExportConfigTypeDef" = dataclasses.field()

    bucket = field("bucket")
    bucketOwner = field("bucketOwner")
    path = field("path")
    packaging = field("packaging")
    encryptionKey = field("encryptionKey")
    encryptionDisabled = field("encryptionDisabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3ReportExportConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ReportExportConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestReportSummary:
    boto3_raw_data: "type_defs.TestReportSummaryTypeDef" = dataclasses.field()

    total = field("total")
    statusCounts = field("statusCounts")
    durationInNanoSeconds = field("durationInNanoSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestReportSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestReportSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetryBuildBatchInput:
    boto3_raw_data: "type_defs.RetryBuildBatchInputTypeDef" = dataclasses.field()

    id = field("id")
    idempotencyToken = field("idempotencyToken")
    retryType = field("retryType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetryBuildBatchInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetryBuildBatchInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetryBuildInput:
    boto3_raw_data: "type_defs.RetryBuildInputTypeDef" = dataclasses.field()

    id = field("id")
    idempotencyToken = field("idempotencyToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetryBuildInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RetryBuildInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SSMSession:
    boto3_raw_data: "type_defs.SSMSessionTypeDef" = dataclasses.field()

    sessionId = field("sessionId")
    tokenValue = field("tokenValue")
    streamUrl = field("streamUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SSMSessionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SSMSessionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetTrackingScalingConfiguration:
    boto3_raw_data: "type_defs.TargetTrackingScalingConfigurationTypeDef" = (
        dataclasses.field()
    )

    metricType = field("metricType")
    targetValue = field("targetValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TargetTrackingScalingConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetTrackingScalingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCommandExecutionInput:
    boto3_raw_data: "type_defs.StartCommandExecutionInputTypeDef" = dataclasses.field()

    sandboxId = field("sandboxId")
    command = field("command")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCommandExecutionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCommandExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSandboxConnectionInput:
    boto3_raw_data: "type_defs.StartSandboxConnectionInputTypeDef" = dataclasses.field()

    sandboxId = field("sandboxId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSandboxConnectionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSandboxConnectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSandboxInput:
    boto3_raw_data: "type_defs.StartSandboxInputTypeDef" = dataclasses.field()

    projectName = field("projectName")
    idempotencyToken = field("idempotencyToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartSandboxInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSandboxInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopBuildBatchInput:
    boto3_raw_data: "type_defs.StopBuildBatchInputTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopBuildBatchInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopBuildBatchInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopBuildInput:
    boto3_raw_data: "type_defs.StopBuildInputTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopBuildInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StopBuildInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopSandboxInput:
    boto3_raw_data: "type_defs.StopSandboxInputTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopSandboxInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopSandboxInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProjectVisibilityInput:
    boto3_raw_data: "type_defs.UpdateProjectVisibilityInputTypeDef" = (
        dataclasses.field()
    )

    projectArn = field("projectArn")
    projectVisibility = field("projectVisibility")
    resourceAccessRole = field("resourceAccessRole")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProjectVisibilityInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProjectVisibilityInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfig:
    boto3_raw_data: "type_defs.VpcConfigTypeDef" = dataclasses.field()

    vpcId = field("vpcId")
    subnets = field("subnets")
    securityGroupIds = field("securityGroupIds")

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
class BatchDeleteBuildsOutput:
    boto3_raw_data: "type_defs.BatchDeleteBuildsOutputTypeDef" = dataclasses.field()

    buildsDeleted = field("buildsDeleted")

    @cached_property
    def buildsNotDeleted(self):  # pragma: no cover
        return BuildNotDeleted.make_many(self.boto3_raw_data["buildsNotDeleted"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteBuildsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteBuildsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBuildBatchOutput:
    boto3_raw_data: "type_defs.DeleteBuildBatchOutputTypeDef" = dataclasses.field()

    statusCode = field("statusCode")
    buildsDeleted = field("buildsDeleted")

    @cached_property
    def buildsNotDeleted(self):  # pragma: no cover
        return BuildNotDeleted.make_many(self.boto3_raw_data["buildsNotDeleted"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBuildBatchOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBuildBatchOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSourceCredentialsOutput:
    boto3_raw_data: "type_defs.DeleteSourceCredentialsOutputTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteSourceCredentialsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSourceCredentialsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyOutput:
    boto3_raw_data: "type_defs.GetResourcePolicyOutputTypeDef" = dataclasses.field()

    policy = field("policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportSourceCredentialsOutput:
    boto3_raw_data: "type_defs.ImportSourceCredentialsOutputTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ImportSourceCredentialsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportSourceCredentialsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBuildBatchesForProjectOutput:
    boto3_raw_data: "type_defs.ListBuildBatchesForProjectOutputTypeDef" = (
        dataclasses.field()
    )

    ids = field("ids")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBuildBatchesForProjectOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBuildBatchesForProjectOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBuildBatchesOutput:
    boto3_raw_data: "type_defs.ListBuildBatchesOutputTypeDef" = dataclasses.field()

    ids = field("ids")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBuildBatchesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBuildBatchesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBuildsForProjectOutput:
    boto3_raw_data: "type_defs.ListBuildsForProjectOutputTypeDef" = dataclasses.field()

    ids = field("ids")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBuildsForProjectOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBuildsForProjectOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBuildsOutput:
    boto3_raw_data: "type_defs.ListBuildsOutputTypeDef" = dataclasses.field()

    ids = field("ids")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListBuildsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBuildsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetsOutput:
    boto3_raw_data: "type_defs.ListFleetsOutputTypeDef" = dataclasses.field()

    fleets = field("fleets")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListFleetsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectsOutput:
    boto3_raw_data: "type_defs.ListProjectsOutputTypeDef" = dataclasses.field()

    projects = field("projects")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProjectsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReportGroupsOutput:
    boto3_raw_data: "type_defs.ListReportGroupsOutputTypeDef" = dataclasses.field()

    reportGroups = field("reportGroups")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReportGroupsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReportGroupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReportsForReportGroupOutput:
    boto3_raw_data: "type_defs.ListReportsForReportGroupOutputTypeDef" = (
        dataclasses.field()
    )

    reports = field("reports")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReportsForReportGroupOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReportsForReportGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReportsOutput:
    boto3_raw_data: "type_defs.ListReportsOutputTypeDef" = dataclasses.field()

    reports = field("reports")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListReportsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReportsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSandboxesForProjectOutput:
    boto3_raw_data: "type_defs.ListSandboxesForProjectOutputTypeDef" = (
        dataclasses.field()
    )

    ids = field("ids")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSandboxesForProjectOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSandboxesForProjectOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSandboxesOutput:
    boto3_raw_data: "type_defs.ListSandboxesOutputTypeDef" = dataclasses.field()

    ids = field("ids")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSandboxesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSandboxesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSharedProjectsOutput:
    boto3_raw_data: "type_defs.ListSharedProjectsOutputTypeDef" = dataclasses.field()

    projects = field("projects")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSharedProjectsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSharedProjectsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSharedReportGroupsOutput:
    boto3_raw_data: "type_defs.ListSharedReportGroupsOutputTypeDef" = (
        dataclasses.field()
    )

    reportGroups = field("reportGroups")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSharedReportGroupsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSharedReportGroupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyOutput:
    boto3_raw_data: "type_defs.PutResourcePolicyOutputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProjectVisibilityOutput:
    boto3_raw_data: "type_defs.UpdateProjectVisibilityOutputTypeDef" = (
        dataclasses.field()
    )

    projectArn = field("projectArn")
    publicProjectAlias = field("publicProjectAlias")
    projectVisibility = field("projectVisibility")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateProjectVisibilityOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProjectVisibilityOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectBuildBatchConfigOutput:
    boto3_raw_data: "type_defs.ProjectBuildBatchConfigOutputTypeDef" = (
        dataclasses.field()
    )

    serviceRole = field("serviceRole")
    combineArtifacts = field("combineArtifacts")

    @cached_property
    def restrictions(self):  # pragma: no cover
        return BatchRestrictionsOutput.make_one(self.boto3_raw_data["restrictions"])

    timeoutInMins = field("timeoutInMins")
    batchReportMode = field("batchReportMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProjectBuildBatchConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectBuildBatchConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectBuildBatchConfig:
    boto3_raw_data: "type_defs.ProjectBuildBatchConfigTypeDef" = dataclasses.field()

    serviceRole = field("serviceRole")
    combineArtifacts = field("combineArtifacts")

    @cached_property
    def restrictions(self):  # pragma: no cover
        return BatchRestrictions.make_one(self.boto3_raw_data["restrictions"])

    timeoutInMins = field("timeoutInMins")
    batchReportMode = field("batchReportMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProjectBuildBatchConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectBuildBatchConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBuildBatchesForProjectInput:
    boto3_raw_data: "type_defs.ListBuildBatchesForProjectInputTypeDef" = (
        dataclasses.field()
    )

    projectName = field("projectName")

    @cached_property
    def filter(self):  # pragma: no cover
        return BuildBatchFilter.make_one(self.boto3_raw_data["filter"])

    maxResults = field("maxResults")
    sortOrder = field("sortOrder")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBuildBatchesForProjectInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBuildBatchesForProjectInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBuildBatchesInput:
    boto3_raw_data: "type_defs.ListBuildBatchesInputTypeDef" = dataclasses.field()

    @cached_property
    def filter(self):  # pragma: no cover
        return BuildBatchFilter.make_one(self.boto3_raw_data["filter"])

    maxResults = field("maxResults")
    sortOrder = field("sortOrder")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBuildBatchesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBuildBatchesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BuildBatchPhase:
    boto3_raw_data: "type_defs.BuildBatchPhaseTypeDef" = dataclasses.field()

    phaseType = field("phaseType")
    phaseStatus = field("phaseStatus")
    startTime = field("startTime")
    endTime = field("endTime")
    durationInSeconds = field("durationInSeconds")

    @cached_property
    def contexts(self):  # pragma: no cover
        return PhaseContext.make_many(self.boto3_raw_data["contexts"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BuildBatchPhaseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BuildBatchPhaseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BuildPhase:
    boto3_raw_data: "type_defs.BuildPhaseTypeDef" = dataclasses.field()

    phaseType = field("phaseType")
    phaseStatus = field("phaseStatus")
    startTime = field("startTime")
    endTime = field("endTime")
    durationInSeconds = field("durationInSeconds")

    @cached_property
    def contexts(self):  # pragma: no cover
        return PhaseContext.make_many(self.boto3_raw_data["contexts"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BuildPhaseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BuildPhaseTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SandboxSessionPhase:
    boto3_raw_data: "type_defs.SandboxSessionPhaseTypeDef" = dataclasses.field()

    phaseType = field("phaseType")
    phaseStatus = field("phaseStatus")
    startTime = field("startTime")
    endTime = field("endTime")
    durationInSeconds = field("durationInSeconds")

    @cached_property
    def contexts(self):  # pragma: no cover
        return PhaseContext.make_many(self.boto3_raw_data["contexts"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SandboxSessionPhaseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SandboxSessionPhaseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BuildSummary:
    boto3_raw_data: "type_defs.BuildSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    requestedOn = field("requestedOn")
    buildStatus = field("buildStatus")

    @cached_property
    def primaryArtifact(self):  # pragma: no cover
        return ResolvedArtifact.make_one(self.boto3_raw_data["primaryArtifact"])

    @cached_property
    def secondaryArtifacts(self):  # pragma: no cover
        return ResolvedArtifact.make_many(self.boto3_raw_data["secondaryArtifacts"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BuildSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BuildSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCodeCoveragesOutput:
    boto3_raw_data: "type_defs.DescribeCodeCoveragesOutputTypeDef" = dataclasses.field()

    @cached_property
    def codeCoverages(self):  # pragma: no cover
        return CodeCoverage.make_many(self.boto3_raw_data["codeCoverages"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCodeCoveragesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCodeCoveragesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCodeCoveragesInputPaginate:
    boto3_raw_data: "type_defs.DescribeCodeCoveragesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    reportArn = field("reportArn")
    sortOrder = field("sortOrder")
    sortBy = field("sortBy")
    minLineCoveragePercentage = field("minLineCoveragePercentage")
    maxLineCoveragePercentage = field("maxLineCoveragePercentage")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCodeCoveragesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCodeCoveragesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBuildBatchesForProjectInputPaginate:
    boto3_raw_data: "type_defs.ListBuildBatchesForProjectInputPaginateTypeDef" = (
        dataclasses.field()
    )

    projectName = field("projectName")

    @cached_property
    def filter(self):  # pragma: no cover
        return BuildBatchFilter.make_one(self.boto3_raw_data["filter"])

    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBuildBatchesForProjectInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBuildBatchesForProjectInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBuildBatchesInputPaginate:
    boto3_raw_data: "type_defs.ListBuildBatchesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filter(self):  # pragma: no cover
        return BuildBatchFilter.make_one(self.boto3_raw_data["filter"])

    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBuildBatchesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBuildBatchesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBuildsForProjectInputPaginate:
    boto3_raw_data: "type_defs.ListBuildsForProjectInputPaginateTypeDef" = (
        dataclasses.field()
    )

    projectName = field("projectName")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBuildsForProjectInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBuildsForProjectInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBuildsInputPaginate:
    boto3_raw_data: "type_defs.ListBuildsInputPaginateTypeDef" = dataclasses.field()

    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBuildsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBuildsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCommandExecutionsForSandboxInputPaginate:
    boto3_raw_data: "type_defs.ListCommandExecutionsForSandboxInputPaginateTypeDef" = (
        dataclasses.field()
    )

    sandboxId = field("sandboxId")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCommandExecutionsForSandboxInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCommandExecutionsForSandboxInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectsInputPaginate:
    boto3_raw_data: "type_defs.ListProjectsInputPaginateTypeDef" = dataclasses.field()

    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProjectsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReportGroupsInputPaginate:
    boto3_raw_data: "type_defs.ListReportGroupsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    sortOrder = field("sortOrder")
    sortBy = field("sortBy")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReportGroupsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReportGroupsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSandboxesForProjectInputPaginate:
    boto3_raw_data: "type_defs.ListSandboxesForProjectInputPaginateTypeDef" = (
        dataclasses.field()
    )

    projectName = field("projectName")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSandboxesForProjectInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSandboxesForProjectInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSandboxesInputPaginate:
    boto3_raw_data: "type_defs.ListSandboxesInputPaginateTypeDef" = dataclasses.field()

    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSandboxesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSandboxesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSharedProjectsInputPaginate:
    boto3_raw_data: "type_defs.ListSharedProjectsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSharedProjectsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSharedProjectsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSharedReportGroupsInputPaginate:
    boto3_raw_data: "type_defs.ListSharedReportGroupsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    sortOrder = field("sortOrder")
    sortBy = field("sortBy")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSharedReportGroupsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSharedReportGroupsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTestCasesInputPaginate:
    boto3_raw_data: "type_defs.DescribeTestCasesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    reportArn = field("reportArn")

    @cached_property
    def filter(self):  # pragma: no cover
        return TestCaseFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeTestCasesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTestCasesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTestCasesInput:
    boto3_raw_data: "type_defs.DescribeTestCasesInputTypeDef" = dataclasses.field()

    reportArn = field("reportArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filter(self):  # pragma: no cover
        return TestCaseFilter.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTestCasesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTestCasesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTestCasesOutput:
    boto3_raw_data: "type_defs.DescribeTestCasesOutputTypeDef" = dataclasses.field()

    @cached_property
    def testCases(self):  # pragma: no cover
        return TestCase.make_many(self.boto3_raw_data["testCases"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTestCasesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTestCasesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DockerServerOutput:
    boto3_raw_data: "type_defs.DockerServerOutputTypeDef" = dataclasses.field()

    computeType = field("computeType")
    securityGroupIds = field("securityGroupIds")

    @cached_property
    def status(self):  # pragma: no cover
        return DockerServerStatus.make_one(self.boto3_raw_data["status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DockerServerOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DockerServerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DockerServer:
    boto3_raw_data: "type_defs.DockerServerTypeDef" = dataclasses.field()

    computeType = field("computeType")
    securityGroupIds = field("securityGroupIds")

    @cached_property
    def status(self):  # pragma: no cover
        return DockerServerStatus.make_one(self.boto3_raw_data["status"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DockerServerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DockerServerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentLanguage:
    boto3_raw_data: "type_defs.EnvironmentLanguageTypeDef" = dataclasses.field()

    language = field("language")

    @cached_property
    def images(self):  # pragma: no cover
        return EnvironmentImage.make_many(self.boto3_raw_data["images"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentLanguageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentLanguageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProxyConfigurationOutput:
    boto3_raw_data: "type_defs.ProxyConfigurationOutputTypeDef" = dataclasses.field()

    defaultBehavior = field("defaultBehavior")

    @cached_property
    def orderedProxyRules(self):  # pragma: no cover
        return FleetProxyRuleOutput.make_many(self.boto3_raw_data["orderedProxyRules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProxyConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProxyConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProxyConfiguration:
    boto3_raw_data: "type_defs.ProxyConfigurationTypeDef" = dataclasses.field()

    defaultBehavior = field("defaultBehavior")

    @cached_property
    def orderedProxyRules(self):  # pragma: no cover
        return FleetProxyRule.make_many(self.boto3_raw_data["orderedProxyRules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProxyConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProxyConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReportGroupTrendOutput:
    boto3_raw_data: "type_defs.GetReportGroupTrendOutputTypeDef" = dataclasses.field()

    @cached_property
    def stats(self):  # pragma: no cover
        return ReportGroupTrendStats.make_one(self.boto3_raw_data["stats"])

    @cached_property
    def rawData(self):  # pragma: no cover
        return ReportWithRawData.make_many(self.boto3_raw_data["rawData"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReportGroupTrendOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReportGroupTrendOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReportsForReportGroupInputPaginate:
    boto3_raw_data: "type_defs.ListReportsForReportGroupInputPaginateTypeDef" = (
        dataclasses.field()
    )

    reportGroupArn = field("reportGroupArn")
    sortOrder = field("sortOrder")

    @cached_property
    def filter(self):  # pragma: no cover
        return ReportFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListReportsForReportGroupInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReportsForReportGroupInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReportsForReportGroupInput:
    boto3_raw_data: "type_defs.ListReportsForReportGroupInputTypeDef" = (
        dataclasses.field()
    )

    reportGroupArn = field("reportGroupArn")
    nextToken = field("nextToken")
    sortOrder = field("sortOrder")
    maxResults = field("maxResults")

    @cached_property
    def filter(self):  # pragma: no cover
        return ReportFilter.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReportsForReportGroupInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReportsForReportGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReportsInputPaginate:
    boto3_raw_data: "type_defs.ListReportsInputPaginateTypeDef" = dataclasses.field()

    sortOrder = field("sortOrder")

    @cached_property
    def filter(self):  # pragma: no cover
        return ReportFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReportsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReportsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReportsInput:
    boto3_raw_data: "type_defs.ListReportsInputTypeDef" = dataclasses.field()

    sortOrder = field("sortOrder")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filter(self):  # pragma: no cover
        return ReportFilter.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListReportsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReportsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSourceCredentialsOutput:
    boto3_raw_data: "type_defs.ListSourceCredentialsOutputTypeDef" = dataclasses.field()

    @cached_property
    def sourceCredentialsInfos(self):  # pragma: no cover
        return SourceCredentialsInfo.make_many(
            self.boto3_raw_data["sourceCredentialsInfos"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSourceCredentialsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSourceCredentialsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogsConfig:
    boto3_raw_data: "type_defs.LogsConfigTypeDef" = dataclasses.field()

    @cached_property
    def cloudWatchLogs(self):  # pragma: no cover
        return CloudWatchLogsConfig.make_one(self.boto3_raw_data["cloudWatchLogs"])

    @cached_property
    def s3Logs(self):  # pragma: no cover
        return S3LogsConfig.make_one(self.boto3_raw_data["s3Logs"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogsConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogsConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogsLocation:
    boto3_raw_data: "type_defs.LogsLocationTypeDef" = dataclasses.field()

    groupName = field("groupName")
    streamName = field("streamName")
    deepLink = field("deepLink")
    s3DeepLink = field("s3DeepLink")
    cloudWatchLogsArn = field("cloudWatchLogsArn")
    s3LogsArn = field("s3LogsArn")

    @cached_property
    def cloudWatchLogs(self):  # pragma: no cover
        return CloudWatchLogsConfig.make_one(self.boto3_raw_data["cloudWatchLogs"])

    @cached_property
    def s3Logs(self):  # pragma: no cover
        return S3LogsConfig.make_one(self.boto3_raw_data["s3Logs"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogsLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogsLocationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectSource:
    boto3_raw_data: "type_defs.ProjectSourceTypeDef" = dataclasses.field()

    type = field("type")
    location = field("location")
    gitCloneDepth = field("gitCloneDepth")

    @cached_property
    def gitSubmodulesConfig(self):  # pragma: no cover
        return GitSubmodulesConfig.make_one(self.boto3_raw_data["gitSubmodulesConfig"])

    buildspec = field("buildspec")

    @cached_property
    def auth(self):  # pragma: no cover
        return SourceAuth.make_one(self.boto3_raw_data["auth"])

    reportBuildStatus = field("reportBuildStatus")

    @cached_property
    def buildStatusConfig(self):  # pragma: no cover
        return BuildStatusConfig.make_one(self.boto3_raw_data["buildStatusConfig"])

    insecureSsl = field("insecureSsl")
    sourceIdentifier = field("sourceIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProjectSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProjectSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Webhook:
    boto3_raw_data: "type_defs.WebhookTypeDef" = dataclasses.field()

    url = field("url")
    payloadUrl = field("payloadUrl")
    secret = field("secret")
    branchFilter = field("branchFilter")

    @cached_property
    def filterGroups(self):  # pragma: no cover
        return WebhookFilter.make_many(self.boto3_raw_data["filterGroups"])

    buildType = field("buildType")
    manualCreation = field("manualCreation")
    lastModifiedSecret = field("lastModifiedSecret")

    @cached_property
    def scopeConfiguration(self):  # pragma: no cover
        return ScopeConfiguration.make_one(self.boto3_raw_data["scopeConfiguration"])

    status = field("status")
    statusMessage = field("statusMessage")

    @cached_property
    def pullRequestBuildPolicy(self):  # pragma: no cover
        return PullRequestBuildPolicyOutput.make_one(
            self.boto3_raw_data["pullRequestBuildPolicy"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WebhookTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WebhookTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportExportConfig:
    boto3_raw_data: "type_defs.ReportExportConfigTypeDef" = dataclasses.field()

    exportConfigType = field("exportConfigType")

    @cached_property
    def s3Destination(self):  # pragma: no cover
        return S3ReportExportConfig.make_one(self.boto3_raw_data["s3Destination"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReportExportConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReportExportConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSandboxConnectionOutput:
    boto3_raw_data: "type_defs.StartSandboxConnectionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ssmSession(self):  # pragma: no cover
        return SSMSession.make_one(self.boto3_raw_data["ssmSession"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSandboxConnectionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSandboxConnectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingConfigurationInput:
    boto3_raw_data: "type_defs.ScalingConfigurationInputTypeDef" = dataclasses.field()

    scalingType = field("scalingType")

    @cached_property
    def targetTrackingScalingConfigs(self):  # pragma: no cover
        return TargetTrackingScalingConfiguration.make_many(
            self.boto3_raw_data["targetTrackingScalingConfigs"]
        )

    maxCapacity = field("maxCapacity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScalingConfigurationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalingConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingConfigurationOutput:
    boto3_raw_data: "type_defs.ScalingConfigurationOutputTypeDef" = dataclasses.field()

    scalingType = field("scalingType")

    @cached_property
    def targetTrackingScalingConfigs(self):  # pragma: no cover
        return TargetTrackingScalingConfiguration.make_many(
            self.boto3_raw_data["targetTrackingScalingConfigs"]
        )

    maxCapacity = field("maxCapacity")
    desiredCapacity = field("desiredCapacity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScalingConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BuildGroup:
    boto3_raw_data: "type_defs.BuildGroupTypeDef" = dataclasses.field()

    identifier = field("identifier")
    dependsOn = field("dependsOn")
    ignoreFailure = field("ignoreFailure")

    @cached_property
    def currentBuildSummary(self):  # pragma: no cover
        return BuildSummary.make_one(self.boto3_raw_data["currentBuildSummary"])

    @cached_property
    def priorBuildSummaryList(self):  # pragma: no cover
        return BuildSummary.make_many(self.boto3_raw_data["priorBuildSummaryList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BuildGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BuildGroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectEnvironmentOutput:
    boto3_raw_data: "type_defs.ProjectEnvironmentOutputTypeDef" = dataclasses.field()

    type = field("type")
    image = field("image")
    computeType = field("computeType")

    @cached_property
    def computeConfiguration(self):  # pragma: no cover
        return ComputeConfiguration.make_one(
            self.boto3_raw_data["computeConfiguration"]
        )

    @cached_property
    def fleet(self):  # pragma: no cover
        return ProjectFleet.make_one(self.boto3_raw_data["fleet"])

    @cached_property
    def environmentVariables(self):  # pragma: no cover
        return EnvironmentVariable.make_many(
            self.boto3_raw_data["environmentVariables"]
        )

    privilegedMode = field("privilegedMode")
    certificate = field("certificate")

    @cached_property
    def registryCredential(self):  # pragma: no cover
        return RegistryCredential.make_one(self.boto3_raw_data["registryCredential"])

    imagePullCredentialsType = field("imagePullCredentialsType")

    @cached_property
    def dockerServer(self):  # pragma: no cover
        return DockerServerOutput.make_one(self.boto3_raw_data["dockerServer"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProjectEnvironmentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectEnvironmentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectEnvironment:
    boto3_raw_data: "type_defs.ProjectEnvironmentTypeDef" = dataclasses.field()

    type = field("type")
    image = field("image")
    computeType = field("computeType")

    @cached_property
    def computeConfiguration(self):  # pragma: no cover
        return ComputeConfiguration.make_one(
            self.boto3_raw_data["computeConfiguration"]
        )

    @cached_property
    def fleet(self):  # pragma: no cover
        return ProjectFleet.make_one(self.boto3_raw_data["fleet"])

    @cached_property
    def environmentVariables(self):  # pragma: no cover
        return EnvironmentVariable.make_many(
            self.boto3_raw_data["environmentVariables"]
        )

    privilegedMode = field("privilegedMode")
    certificate = field("certificate")

    @cached_property
    def registryCredential(self):  # pragma: no cover
        return RegistryCredential.make_one(self.boto3_raw_data["registryCredential"])

    imagePullCredentialsType = field("imagePullCredentialsType")

    @cached_property
    def dockerServer(self):  # pragma: no cover
        return DockerServer.make_one(self.boto3_raw_data["dockerServer"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProjectEnvironmentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectEnvironmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentPlatform:
    boto3_raw_data: "type_defs.EnvironmentPlatformTypeDef" = dataclasses.field()

    platform = field("platform")

    @cached_property
    def languages(self):  # pragma: no cover
        return EnvironmentLanguage.make_many(self.boto3_raw_data["languages"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentPlatformTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentPlatformTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommandExecution:
    boto3_raw_data: "type_defs.CommandExecutionTypeDef" = dataclasses.field()

    id = field("id")
    sandboxId = field("sandboxId")
    submitTime = field("submitTime")
    startTime = field("startTime")
    endTime = field("endTime")
    status = field("status")
    command = field("command")
    type = field("type")
    exitCode = field("exitCode")
    standardOutputContent = field("standardOutputContent")
    standardErrContent = field("standardErrContent")

    @cached_property
    def logs(self):  # pragma: no cover
        return LogsLocation.make_one(self.boto3_raw_data["logs"])

    sandboxArn = field("sandboxArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CommandExecutionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommandExecutionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SandboxSession:
    boto3_raw_data: "type_defs.SandboxSessionTypeDef" = dataclasses.field()

    id = field("id")
    status = field("status")
    startTime = field("startTime")
    endTime = field("endTime")
    currentPhase = field("currentPhase")

    @cached_property
    def phases(self):  # pragma: no cover
        return SandboxSessionPhase.make_many(self.boto3_raw_data["phases"])

    resolvedSourceVersion = field("resolvedSourceVersion")

    @cached_property
    def logs(self):  # pragma: no cover
        return LogsLocation.make_one(self.boto3_raw_data["logs"])

    @cached_property
    def networkInterface(self):  # pragma: no cover
        return NetworkInterface.make_one(self.boto3_raw_data["networkInterface"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SandboxSessionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SandboxSessionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartBuildInput:
    boto3_raw_data: "type_defs.StartBuildInputTypeDef" = dataclasses.field()

    projectName = field("projectName")

    @cached_property
    def secondarySourcesOverride(self):  # pragma: no cover
        return ProjectSource.make_many(self.boto3_raw_data["secondarySourcesOverride"])

    @cached_property
    def secondarySourcesVersionOverride(self):  # pragma: no cover
        return ProjectSourceVersion.make_many(
            self.boto3_raw_data["secondarySourcesVersionOverride"]
        )

    sourceVersion = field("sourceVersion")

    @cached_property
    def artifactsOverride(self):  # pragma: no cover
        return ProjectArtifacts.make_one(self.boto3_raw_data["artifactsOverride"])

    @cached_property
    def secondaryArtifactsOverride(self):  # pragma: no cover
        return ProjectArtifacts.make_many(
            self.boto3_raw_data["secondaryArtifactsOverride"]
        )

    @cached_property
    def environmentVariablesOverride(self):  # pragma: no cover
        return EnvironmentVariable.make_many(
            self.boto3_raw_data["environmentVariablesOverride"]
        )

    sourceTypeOverride = field("sourceTypeOverride")
    sourceLocationOverride = field("sourceLocationOverride")

    @cached_property
    def sourceAuthOverride(self):  # pragma: no cover
        return SourceAuth.make_one(self.boto3_raw_data["sourceAuthOverride"])

    gitCloneDepthOverride = field("gitCloneDepthOverride")

    @cached_property
    def gitSubmodulesConfigOverride(self):  # pragma: no cover
        return GitSubmodulesConfig.make_one(
            self.boto3_raw_data["gitSubmodulesConfigOverride"]
        )

    buildspecOverride = field("buildspecOverride")
    insecureSslOverride = field("insecureSslOverride")
    reportBuildStatusOverride = field("reportBuildStatusOverride")

    @cached_property
    def buildStatusConfigOverride(self):  # pragma: no cover
        return BuildStatusConfig.make_one(
            self.boto3_raw_data["buildStatusConfigOverride"]
        )

    environmentTypeOverride = field("environmentTypeOverride")
    imageOverride = field("imageOverride")
    computeTypeOverride = field("computeTypeOverride")
    certificateOverride = field("certificateOverride")
    cacheOverride = field("cacheOverride")
    serviceRoleOverride = field("serviceRoleOverride")
    privilegedModeOverride = field("privilegedModeOverride")
    timeoutInMinutesOverride = field("timeoutInMinutesOverride")
    queuedTimeoutInMinutesOverride = field("queuedTimeoutInMinutesOverride")
    encryptionKeyOverride = field("encryptionKeyOverride")
    idempotencyToken = field("idempotencyToken")

    @cached_property
    def logsConfigOverride(self):  # pragma: no cover
        return LogsConfig.make_one(self.boto3_raw_data["logsConfigOverride"])

    @cached_property
    def registryCredentialOverride(self):  # pragma: no cover
        return RegistryCredential.make_one(
            self.boto3_raw_data["registryCredentialOverride"]
        )

    imagePullCredentialsTypeOverride = field("imagePullCredentialsTypeOverride")
    debugSessionEnabled = field("debugSessionEnabled")

    @cached_property
    def fleetOverride(self):  # pragma: no cover
        return ProjectFleet.make_one(self.boto3_raw_data["fleetOverride"])

    autoRetryLimitOverride = field("autoRetryLimitOverride")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartBuildInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StartBuildInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWebhookOutput:
    boto3_raw_data: "type_defs.CreateWebhookOutputTypeDef" = dataclasses.field()

    @cached_property
    def webhook(self):  # pragma: no cover
        return Webhook.make_one(self.boto3_raw_data["webhook"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWebhookOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWebhookOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWebhookOutput:
    boto3_raw_data: "type_defs.UpdateWebhookOutputTypeDef" = dataclasses.field()

    @cached_property
    def webhook(self):  # pragma: no cover
        return Webhook.make_one(self.boto3_raw_data["webhook"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWebhookOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWebhookOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWebhookInput:
    boto3_raw_data: "type_defs.CreateWebhookInputTypeDef" = dataclasses.field()

    projectName = field("projectName")
    branchFilter = field("branchFilter")

    @cached_property
    def filterGroups(self):  # pragma: no cover
        return WebhookFilter.make_many(self.boto3_raw_data["filterGroups"])

    buildType = field("buildType")
    manualCreation = field("manualCreation")

    @cached_property
    def scopeConfiguration(self):  # pragma: no cover
        return ScopeConfiguration.make_one(self.boto3_raw_data["scopeConfiguration"])

    pullRequestBuildPolicy = field("pullRequestBuildPolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWebhookInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWebhookInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWebhookInput:
    boto3_raw_data: "type_defs.UpdateWebhookInputTypeDef" = dataclasses.field()

    projectName = field("projectName")
    branchFilter = field("branchFilter")
    rotateSecret = field("rotateSecret")

    @cached_property
    def filterGroups(self):  # pragma: no cover
        return WebhookFilter.make_many(self.boto3_raw_data["filterGroups"])

    buildType = field("buildType")
    pullRequestBuildPolicy = field("pullRequestBuildPolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWebhookInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWebhookInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReportGroupInput:
    boto3_raw_data: "type_defs.CreateReportGroupInputTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")

    @cached_property
    def exportConfig(self):  # pragma: no cover
        return ReportExportConfig.make_one(self.boto3_raw_data["exportConfig"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateReportGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReportGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportGroup:
    boto3_raw_data: "type_defs.ReportGroupTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    type = field("type")

    @cached_property
    def exportConfig(self):  # pragma: no cover
        return ReportExportConfig.make_one(self.boto3_raw_data["exportConfig"])

    created = field("created")
    lastModified = field("lastModified")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReportGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReportGroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Report:
    boto3_raw_data: "type_defs.ReportTypeDef" = dataclasses.field()

    arn = field("arn")
    type = field("type")
    name = field("name")
    reportGroupArn = field("reportGroupArn")
    executionId = field("executionId")
    status = field("status")
    created = field("created")
    expired = field("expired")

    @cached_property
    def exportConfig(self):  # pragma: no cover
        return ReportExportConfig.make_one(self.boto3_raw_data["exportConfig"])

    truncated = field("truncated")

    @cached_property
    def testSummary(self):  # pragma: no cover
        return TestReportSummary.make_one(self.boto3_raw_data["testSummary"])

    @cached_property
    def codeCoverageSummary(self):  # pragma: no cover
        return CodeCoverageReportSummary.make_one(
            self.boto3_raw_data["codeCoverageSummary"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReportTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReportTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateReportGroupInput:
    boto3_raw_data: "type_defs.UpdateReportGroupInputTypeDef" = dataclasses.field()

    arn = field("arn")

    @cached_property
    def exportConfig(self):  # pragma: no cover
        return ReportExportConfig.make_one(self.boto3_raw_data["exportConfig"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateReportGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateReportGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Fleet:
    boto3_raw_data: "type_defs.FleetTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    id = field("id")
    created = field("created")
    lastModified = field("lastModified")

    @cached_property
    def status(self):  # pragma: no cover
        return FleetStatus.make_one(self.boto3_raw_data["status"])

    baseCapacity = field("baseCapacity")
    environmentType = field("environmentType")
    computeType = field("computeType")

    @cached_property
    def computeConfiguration(self):  # pragma: no cover
        return ComputeConfiguration.make_one(
            self.boto3_raw_data["computeConfiguration"]
        )

    @cached_property
    def scalingConfiguration(self):  # pragma: no cover
        return ScalingConfigurationOutput.make_one(
            self.boto3_raw_data["scalingConfiguration"]
        )

    overflowBehavior = field("overflowBehavior")

    @cached_property
    def vpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["vpcConfig"])

    @cached_property
    def proxyConfiguration(self):  # pragma: no cover
        return ProxyConfigurationOutput.make_one(
            self.boto3_raw_data["proxyConfiguration"]
        )

    imageId = field("imageId")
    fleetServiceRole = field("fleetServiceRole")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FleetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FleetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartBuildBatchInput:
    boto3_raw_data: "type_defs.StartBuildBatchInputTypeDef" = dataclasses.field()

    projectName = field("projectName")

    @cached_property
    def secondarySourcesOverride(self):  # pragma: no cover
        return ProjectSource.make_many(self.boto3_raw_data["secondarySourcesOverride"])

    @cached_property
    def secondarySourcesVersionOverride(self):  # pragma: no cover
        return ProjectSourceVersion.make_many(
            self.boto3_raw_data["secondarySourcesVersionOverride"]
        )

    sourceVersion = field("sourceVersion")

    @cached_property
    def artifactsOverride(self):  # pragma: no cover
        return ProjectArtifacts.make_one(self.boto3_raw_data["artifactsOverride"])

    @cached_property
    def secondaryArtifactsOverride(self):  # pragma: no cover
        return ProjectArtifacts.make_many(
            self.boto3_raw_data["secondaryArtifactsOverride"]
        )

    @cached_property
    def environmentVariablesOverride(self):  # pragma: no cover
        return EnvironmentVariable.make_many(
            self.boto3_raw_data["environmentVariablesOverride"]
        )

    sourceTypeOverride = field("sourceTypeOverride")
    sourceLocationOverride = field("sourceLocationOverride")

    @cached_property
    def sourceAuthOverride(self):  # pragma: no cover
        return SourceAuth.make_one(self.boto3_raw_data["sourceAuthOverride"])

    gitCloneDepthOverride = field("gitCloneDepthOverride")

    @cached_property
    def gitSubmodulesConfigOverride(self):  # pragma: no cover
        return GitSubmodulesConfig.make_one(
            self.boto3_raw_data["gitSubmodulesConfigOverride"]
        )

    buildspecOverride = field("buildspecOverride")
    insecureSslOverride = field("insecureSslOverride")
    reportBuildBatchStatusOverride = field("reportBuildBatchStatusOverride")
    environmentTypeOverride = field("environmentTypeOverride")
    imageOverride = field("imageOverride")
    computeTypeOverride = field("computeTypeOverride")
    certificateOverride = field("certificateOverride")
    cacheOverride = field("cacheOverride")
    serviceRoleOverride = field("serviceRoleOverride")
    privilegedModeOverride = field("privilegedModeOverride")
    buildTimeoutInMinutesOverride = field("buildTimeoutInMinutesOverride")
    queuedTimeoutInMinutesOverride = field("queuedTimeoutInMinutesOverride")
    encryptionKeyOverride = field("encryptionKeyOverride")
    idempotencyToken = field("idempotencyToken")

    @cached_property
    def logsConfigOverride(self):  # pragma: no cover
        return LogsConfig.make_one(self.boto3_raw_data["logsConfigOverride"])

    @cached_property
    def registryCredentialOverride(self):  # pragma: no cover
        return RegistryCredential.make_one(
            self.boto3_raw_data["registryCredentialOverride"]
        )

    imagePullCredentialsTypeOverride = field("imagePullCredentialsTypeOverride")
    buildBatchConfigOverride = field("buildBatchConfigOverride")
    debugSessionEnabled = field("debugSessionEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartBuildBatchInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartBuildBatchInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BuildBatch:
    boto3_raw_data: "type_defs.BuildBatchTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    startTime = field("startTime")
    endTime = field("endTime")
    currentPhase = field("currentPhase")
    buildBatchStatus = field("buildBatchStatus")
    sourceVersion = field("sourceVersion")
    resolvedSourceVersion = field("resolvedSourceVersion")
    projectName = field("projectName")

    @cached_property
    def phases(self):  # pragma: no cover
        return BuildBatchPhase.make_many(self.boto3_raw_data["phases"])

    @cached_property
    def source(self):  # pragma: no cover
        return ProjectSource.make_one(self.boto3_raw_data["source"])

    @cached_property
    def secondarySources(self):  # pragma: no cover
        return ProjectSource.make_many(self.boto3_raw_data["secondarySources"])

    @cached_property
    def secondarySourceVersions(self):  # pragma: no cover
        return ProjectSourceVersion.make_many(
            self.boto3_raw_data["secondarySourceVersions"]
        )

    @cached_property
    def artifacts(self):  # pragma: no cover
        return BuildArtifacts.make_one(self.boto3_raw_data["artifacts"])

    @cached_property
    def secondaryArtifacts(self):  # pragma: no cover
        return BuildArtifacts.make_many(self.boto3_raw_data["secondaryArtifacts"])

    @cached_property
    def cache(self):  # pragma: no cover
        return ProjectCacheOutput.make_one(self.boto3_raw_data["cache"])

    @cached_property
    def environment(self):  # pragma: no cover
        return ProjectEnvironmentOutput.make_one(self.boto3_raw_data["environment"])

    serviceRole = field("serviceRole")

    @cached_property
    def logConfig(self):  # pragma: no cover
        return LogsConfig.make_one(self.boto3_raw_data["logConfig"])

    buildTimeoutInMinutes = field("buildTimeoutInMinutes")
    queuedTimeoutInMinutes = field("queuedTimeoutInMinutes")
    complete = field("complete")
    initiator = field("initiator")

    @cached_property
    def vpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["vpcConfig"])

    encryptionKey = field("encryptionKey")
    buildBatchNumber = field("buildBatchNumber")

    @cached_property
    def fileSystemLocations(self):  # pragma: no cover
        return ProjectFileSystemLocation.make_many(
            self.boto3_raw_data["fileSystemLocations"]
        )

    @cached_property
    def buildBatchConfig(self):  # pragma: no cover
        return ProjectBuildBatchConfigOutput.make_one(
            self.boto3_raw_data["buildBatchConfig"]
        )

    @cached_property
    def buildGroups(self):  # pragma: no cover
        return BuildGroup.make_many(self.boto3_raw_data["buildGroups"])

    debugSessionEnabled = field("debugSessionEnabled")
    reportArns = field("reportArns")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BuildBatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BuildBatchTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Build:
    boto3_raw_data: "type_defs.BuildTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    buildNumber = field("buildNumber")
    startTime = field("startTime")
    endTime = field("endTime")
    currentPhase = field("currentPhase")
    buildStatus = field("buildStatus")
    sourceVersion = field("sourceVersion")
    resolvedSourceVersion = field("resolvedSourceVersion")
    projectName = field("projectName")

    @cached_property
    def phases(self):  # pragma: no cover
        return BuildPhase.make_many(self.boto3_raw_data["phases"])

    @cached_property
    def source(self):  # pragma: no cover
        return ProjectSource.make_one(self.boto3_raw_data["source"])

    @cached_property
    def secondarySources(self):  # pragma: no cover
        return ProjectSource.make_many(self.boto3_raw_data["secondarySources"])

    @cached_property
    def secondarySourceVersions(self):  # pragma: no cover
        return ProjectSourceVersion.make_many(
            self.boto3_raw_data["secondarySourceVersions"]
        )

    @cached_property
    def artifacts(self):  # pragma: no cover
        return BuildArtifacts.make_one(self.boto3_raw_data["artifacts"])

    @cached_property
    def secondaryArtifacts(self):  # pragma: no cover
        return BuildArtifacts.make_many(self.boto3_raw_data["secondaryArtifacts"])

    @cached_property
    def cache(self):  # pragma: no cover
        return ProjectCacheOutput.make_one(self.boto3_raw_data["cache"])

    @cached_property
    def environment(self):  # pragma: no cover
        return ProjectEnvironmentOutput.make_one(self.boto3_raw_data["environment"])

    serviceRole = field("serviceRole")

    @cached_property
    def logs(self):  # pragma: no cover
        return LogsLocation.make_one(self.boto3_raw_data["logs"])

    timeoutInMinutes = field("timeoutInMinutes")
    queuedTimeoutInMinutes = field("queuedTimeoutInMinutes")
    buildComplete = field("buildComplete")
    initiator = field("initiator")

    @cached_property
    def vpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["vpcConfig"])

    @cached_property
    def networkInterface(self):  # pragma: no cover
        return NetworkInterface.make_one(self.boto3_raw_data["networkInterface"])

    encryptionKey = field("encryptionKey")

    @cached_property
    def exportedEnvironmentVariables(self):  # pragma: no cover
        return ExportedEnvironmentVariable.make_many(
            self.boto3_raw_data["exportedEnvironmentVariables"]
        )

    reportArns = field("reportArns")

    @cached_property
    def fileSystemLocations(self):  # pragma: no cover
        return ProjectFileSystemLocation.make_many(
            self.boto3_raw_data["fileSystemLocations"]
        )

    @cached_property
    def debugSession(self):  # pragma: no cover
        return DebugSession.make_one(self.boto3_raw_data["debugSession"])

    buildBatchArn = field("buildBatchArn")

    @cached_property
    def autoRetryConfig(self):  # pragma: no cover
        return AutoRetryConfig.make_one(self.boto3_raw_data["autoRetryConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BuildTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BuildTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Project:
    boto3_raw_data: "type_defs.ProjectTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    description = field("description")

    @cached_property
    def source(self):  # pragma: no cover
        return ProjectSource.make_one(self.boto3_raw_data["source"])

    @cached_property
    def secondarySources(self):  # pragma: no cover
        return ProjectSource.make_many(self.boto3_raw_data["secondarySources"])

    sourceVersion = field("sourceVersion")

    @cached_property
    def secondarySourceVersions(self):  # pragma: no cover
        return ProjectSourceVersion.make_many(
            self.boto3_raw_data["secondarySourceVersions"]
        )

    @cached_property
    def artifacts(self):  # pragma: no cover
        return ProjectArtifacts.make_one(self.boto3_raw_data["artifacts"])

    @cached_property
    def secondaryArtifacts(self):  # pragma: no cover
        return ProjectArtifacts.make_many(self.boto3_raw_data["secondaryArtifacts"])

    @cached_property
    def cache(self):  # pragma: no cover
        return ProjectCacheOutput.make_one(self.boto3_raw_data["cache"])

    @cached_property
    def environment(self):  # pragma: no cover
        return ProjectEnvironmentOutput.make_one(self.boto3_raw_data["environment"])

    serviceRole = field("serviceRole")
    timeoutInMinutes = field("timeoutInMinutes")
    queuedTimeoutInMinutes = field("queuedTimeoutInMinutes")
    encryptionKey = field("encryptionKey")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    created = field("created")
    lastModified = field("lastModified")

    @cached_property
    def webhook(self):  # pragma: no cover
        return Webhook.make_one(self.boto3_raw_data["webhook"])

    @cached_property
    def vpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["vpcConfig"])

    @cached_property
    def badge(self):  # pragma: no cover
        return ProjectBadge.make_one(self.boto3_raw_data["badge"])

    @cached_property
    def logsConfig(self):  # pragma: no cover
        return LogsConfig.make_one(self.boto3_raw_data["logsConfig"])

    @cached_property
    def fileSystemLocations(self):  # pragma: no cover
        return ProjectFileSystemLocation.make_many(
            self.boto3_raw_data["fileSystemLocations"]
        )

    @cached_property
    def buildBatchConfig(self):  # pragma: no cover
        return ProjectBuildBatchConfigOutput.make_one(
            self.boto3_raw_data["buildBatchConfig"]
        )

    concurrentBuildLimit = field("concurrentBuildLimit")
    projectVisibility = field("projectVisibility")
    publicProjectAlias = field("publicProjectAlias")
    resourceAccessRole = field("resourceAccessRole")
    autoRetryLimit = field("autoRetryLimit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProjectTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCuratedEnvironmentImagesOutput:
    boto3_raw_data: "type_defs.ListCuratedEnvironmentImagesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def platforms(self):  # pragma: no cover
        return EnvironmentPlatform.make_many(self.boto3_raw_data["platforms"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCuratedEnvironmentImagesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCuratedEnvironmentImagesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFleetInput:
    boto3_raw_data: "type_defs.CreateFleetInputTypeDef" = dataclasses.field()

    name = field("name")
    baseCapacity = field("baseCapacity")
    environmentType = field("environmentType")
    computeType = field("computeType")

    @cached_property
    def computeConfiguration(self):  # pragma: no cover
        return ComputeConfiguration.make_one(
            self.boto3_raw_data["computeConfiguration"]
        )

    @cached_property
    def scalingConfiguration(self):  # pragma: no cover
        return ScalingConfigurationInput.make_one(
            self.boto3_raw_data["scalingConfiguration"]
        )

    overflowBehavior = field("overflowBehavior")
    vpcConfig = field("vpcConfig")
    proxyConfiguration = field("proxyConfiguration")
    imageId = field("imageId")
    fleetServiceRole = field("fleetServiceRole")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateFleetInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFleetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFleetInput:
    boto3_raw_data: "type_defs.UpdateFleetInputTypeDef" = dataclasses.field()

    arn = field("arn")
    baseCapacity = field("baseCapacity")
    environmentType = field("environmentType")
    computeType = field("computeType")

    @cached_property
    def computeConfiguration(self):  # pragma: no cover
        return ComputeConfiguration.make_one(
            self.boto3_raw_data["computeConfiguration"]
        )

    @cached_property
    def scalingConfiguration(self):  # pragma: no cover
        return ScalingConfigurationInput.make_one(
            self.boto3_raw_data["scalingConfiguration"]
        )

    overflowBehavior = field("overflowBehavior")
    vpcConfig = field("vpcConfig")
    proxyConfiguration = field("proxyConfiguration")
    imageId = field("imageId")
    fleetServiceRole = field("fleetServiceRole")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateFleetInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFleetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetCommandExecutionsOutput:
    boto3_raw_data: "type_defs.BatchGetCommandExecutionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def commandExecutions(self):  # pragma: no cover
        return CommandExecution.make_many(self.boto3_raw_data["commandExecutions"])

    commandExecutionsNotFound = field("commandExecutionsNotFound")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetCommandExecutionsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetCommandExecutionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCommandExecutionsForSandboxOutput:
    boto3_raw_data: "type_defs.ListCommandExecutionsForSandboxOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def commandExecutions(self):  # pragma: no cover
        return CommandExecution.make_many(self.boto3_raw_data["commandExecutions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCommandExecutionsForSandboxOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCommandExecutionsForSandboxOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCommandExecutionOutput:
    boto3_raw_data: "type_defs.StartCommandExecutionOutputTypeDef" = dataclasses.field()

    @cached_property
    def commandExecution(self):  # pragma: no cover
        return CommandExecution.make_one(self.boto3_raw_data["commandExecution"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCommandExecutionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCommandExecutionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Sandbox:
    boto3_raw_data: "type_defs.SandboxTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    projectName = field("projectName")
    requestTime = field("requestTime")
    startTime = field("startTime")
    endTime = field("endTime")
    status = field("status")

    @cached_property
    def source(self):  # pragma: no cover
        return ProjectSource.make_one(self.boto3_raw_data["source"])

    sourceVersion = field("sourceVersion")

    @cached_property
    def secondarySources(self):  # pragma: no cover
        return ProjectSource.make_many(self.boto3_raw_data["secondarySources"])

    @cached_property
    def secondarySourceVersions(self):  # pragma: no cover
        return ProjectSourceVersion.make_many(
            self.boto3_raw_data["secondarySourceVersions"]
        )

    @cached_property
    def environment(self):  # pragma: no cover
        return ProjectEnvironmentOutput.make_one(self.boto3_raw_data["environment"])

    @cached_property
    def fileSystemLocations(self):  # pragma: no cover
        return ProjectFileSystemLocation.make_many(
            self.boto3_raw_data["fileSystemLocations"]
        )

    timeoutInMinutes = field("timeoutInMinutes")
    queuedTimeoutInMinutes = field("queuedTimeoutInMinutes")

    @cached_property
    def vpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["vpcConfig"])

    @cached_property
    def logConfig(self):  # pragma: no cover
        return LogsConfig.make_one(self.boto3_raw_data["logConfig"])

    encryptionKey = field("encryptionKey")
    serviceRole = field("serviceRole")

    @cached_property
    def currentSession(self):  # pragma: no cover
        return SandboxSession.make_one(self.boto3_raw_data["currentSession"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SandboxTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SandboxTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetReportGroupsOutput:
    boto3_raw_data: "type_defs.BatchGetReportGroupsOutputTypeDef" = dataclasses.field()

    @cached_property
    def reportGroups(self):  # pragma: no cover
        return ReportGroup.make_many(self.boto3_raw_data["reportGroups"])

    reportGroupsNotFound = field("reportGroupsNotFound")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetReportGroupsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetReportGroupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReportGroupOutput:
    boto3_raw_data: "type_defs.CreateReportGroupOutputTypeDef" = dataclasses.field()

    @cached_property
    def reportGroup(self):  # pragma: no cover
        return ReportGroup.make_one(self.boto3_raw_data["reportGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateReportGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReportGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateReportGroupOutput:
    boto3_raw_data: "type_defs.UpdateReportGroupOutputTypeDef" = dataclasses.field()

    @cached_property
    def reportGroup(self):  # pragma: no cover
        return ReportGroup.make_one(self.boto3_raw_data["reportGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateReportGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateReportGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetReportsOutput:
    boto3_raw_data: "type_defs.BatchGetReportsOutputTypeDef" = dataclasses.field()

    @cached_property
    def reports(self):  # pragma: no cover
        return Report.make_many(self.boto3_raw_data["reports"])

    reportsNotFound = field("reportsNotFound")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetReportsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetReportsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetFleetsOutput:
    boto3_raw_data: "type_defs.BatchGetFleetsOutputTypeDef" = dataclasses.field()

    @cached_property
    def fleets(self):  # pragma: no cover
        return Fleet.make_many(self.boto3_raw_data["fleets"])

    fleetsNotFound = field("fleetsNotFound")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetFleetsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetFleetsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFleetOutput:
    boto3_raw_data: "type_defs.CreateFleetOutputTypeDef" = dataclasses.field()

    @cached_property
    def fleet(self):  # pragma: no cover
        return Fleet.make_one(self.boto3_raw_data["fleet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateFleetOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFleetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFleetOutput:
    boto3_raw_data: "type_defs.UpdateFleetOutputTypeDef" = dataclasses.field()

    @cached_property
    def fleet(self):  # pragma: no cover
        return Fleet.make_one(self.boto3_raw_data["fleet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateFleetOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFleetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetBuildBatchesOutput:
    boto3_raw_data: "type_defs.BatchGetBuildBatchesOutputTypeDef" = dataclasses.field()

    @cached_property
    def buildBatches(self):  # pragma: no cover
        return BuildBatch.make_many(self.boto3_raw_data["buildBatches"])

    buildBatchesNotFound = field("buildBatchesNotFound")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetBuildBatchesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetBuildBatchesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetryBuildBatchOutput:
    boto3_raw_data: "type_defs.RetryBuildBatchOutputTypeDef" = dataclasses.field()

    @cached_property
    def buildBatch(self):  # pragma: no cover
        return BuildBatch.make_one(self.boto3_raw_data["buildBatch"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetryBuildBatchOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetryBuildBatchOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartBuildBatchOutput:
    boto3_raw_data: "type_defs.StartBuildBatchOutputTypeDef" = dataclasses.field()

    @cached_property
    def buildBatch(self):  # pragma: no cover
        return BuildBatch.make_one(self.boto3_raw_data["buildBatch"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartBuildBatchOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartBuildBatchOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopBuildBatchOutput:
    boto3_raw_data: "type_defs.StopBuildBatchOutputTypeDef" = dataclasses.field()

    @cached_property
    def buildBatch(self):  # pragma: no cover
        return BuildBatch.make_one(self.boto3_raw_data["buildBatch"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopBuildBatchOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopBuildBatchOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetBuildsOutput:
    boto3_raw_data: "type_defs.BatchGetBuildsOutputTypeDef" = dataclasses.field()

    @cached_property
    def builds(self):  # pragma: no cover
        return Build.make_many(self.boto3_raw_data["builds"])

    buildsNotFound = field("buildsNotFound")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetBuildsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetBuildsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetryBuildOutput:
    boto3_raw_data: "type_defs.RetryBuildOutputTypeDef" = dataclasses.field()

    @cached_property
    def build(self):  # pragma: no cover
        return Build.make_one(self.boto3_raw_data["build"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetryBuildOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetryBuildOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartBuildOutput:
    boto3_raw_data: "type_defs.StartBuildOutputTypeDef" = dataclasses.field()

    @cached_property
    def build(self):  # pragma: no cover
        return Build.make_one(self.boto3_raw_data["build"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartBuildOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartBuildOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopBuildOutput:
    boto3_raw_data: "type_defs.StopBuildOutputTypeDef" = dataclasses.field()

    @cached_property
    def build(self):  # pragma: no cover
        return Build.make_one(self.boto3_raw_data["build"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopBuildOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StopBuildOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetProjectsOutput:
    boto3_raw_data: "type_defs.BatchGetProjectsOutputTypeDef" = dataclasses.field()

    @cached_property
    def projects(self):  # pragma: no cover
        return Project.make_many(self.boto3_raw_data["projects"])

    projectsNotFound = field("projectsNotFound")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetProjectsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetProjectsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProjectOutput:
    boto3_raw_data: "type_defs.CreateProjectOutputTypeDef" = dataclasses.field()

    @cached_property
    def project(self):  # pragma: no cover
        return Project.make_one(self.boto3_raw_data["project"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProjectOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProjectOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProjectOutput:
    boto3_raw_data: "type_defs.UpdateProjectOutputTypeDef" = dataclasses.field()

    @cached_property
    def project(self):  # pragma: no cover
        return Project.make_one(self.boto3_raw_data["project"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProjectOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProjectOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProjectInput:
    boto3_raw_data: "type_defs.CreateProjectInputTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def source(self):  # pragma: no cover
        return ProjectSource.make_one(self.boto3_raw_data["source"])

    @cached_property
    def artifacts(self):  # pragma: no cover
        return ProjectArtifacts.make_one(self.boto3_raw_data["artifacts"])

    environment = field("environment")
    serviceRole = field("serviceRole")
    description = field("description")

    @cached_property
    def secondarySources(self):  # pragma: no cover
        return ProjectSource.make_many(self.boto3_raw_data["secondarySources"])

    sourceVersion = field("sourceVersion")

    @cached_property
    def secondarySourceVersions(self):  # pragma: no cover
        return ProjectSourceVersion.make_many(
            self.boto3_raw_data["secondarySourceVersions"]
        )

    @cached_property
    def secondaryArtifacts(self):  # pragma: no cover
        return ProjectArtifacts.make_many(self.boto3_raw_data["secondaryArtifacts"])

    cache = field("cache")
    timeoutInMinutes = field("timeoutInMinutes")
    queuedTimeoutInMinutes = field("queuedTimeoutInMinutes")
    encryptionKey = field("encryptionKey")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    vpcConfig = field("vpcConfig")
    badgeEnabled = field("badgeEnabled")

    @cached_property
    def logsConfig(self):  # pragma: no cover
        return LogsConfig.make_one(self.boto3_raw_data["logsConfig"])

    @cached_property
    def fileSystemLocations(self):  # pragma: no cover
        return ProjectFileSystemLocation.make_many(
            self.boto3_raw_data["fileSystemLocations"]
        )

    buildBatchConfig = field("buildBatchConfig")
    concurrentBuildLimit = field("concurrentBuildLimit")
    autoRetryLimit = field("autoRetryLimit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProjectInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProjectInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProjectInput:
    boto3_raw_data: "type_defs.UpdateProjectInputTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")

    @cached_property
    def source(self):  # pragma: no cover
        return ProjectSource.make_one(self.boto3_raw_data["source"])

    @cached_property
    def secondarySources(self):  # pragma: no cover
        return ProjectSource.make_many(self.boto3_raw_data["secondarySources"])

    sourceVersion = field("sourceVersion")

    @cached_property
    def secondarySourceVersions(self):  # pragma: no cover
        return ProjectSourceVersion.make_many(
            self.boto3_raw_data["secondarySourceVersions"]
        )

    @cached_property
    def artifacts(self):  # pragma: no cover
        return ProjectArtifacts.make_one(self.boto3_raw_data["artifacts"])

    @cached_property
    def secondaryArtifacts(self):  # pragma: no cover
        return ProjectArtifacts.make_many(self.boto3_raw_data["secondaryArtifacts"])

    cache = field("cache")
    environment = field("environment")
    serviceRole = field("serviceRole")
    timeoutInMinutes = field("timeoutInMinutes")
    queuedTimeoutInMinutes = field("queuedTimeoutInMinutes")
    encryptionKey = field("encryptionKey")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    vpcConfig = field("vpcConfig")
    badgeEnabled = field("badgeEnabled")

    @cached_property
    def logsConfig(self):  # pragma: no cover
        return LogsConfig.make_one(self.boto3_raw_data["logsConfig"])

    @cached_property
    def fileSystemLocations(self):  # pragma: no cover
        return ProjectFileSystemLocation.make_many(
            self.boto3_raw_data["fileSystemLocations"]
        )

    buildBatchConfig = field("buildBatchConfig")
    concurrentBuildLimit = field("concurrentBuildLimit")
    autoRetryLimit = field("autoRetryLimit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProjectInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProjectInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetSandboxesOutput:
    boto3_raw_data: "type_defs.BatchGetSandboxesOutputTypeDef" = dataclasses.field()

    @cached_property
    def sandboxes(self):  # pragma: no cover
        return Sandbox.make_many(self.boto3_raw_data["sandboxes"])

    sandboxesNotFound = field("sandboxesNotFound")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetSandboxesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetSandboxesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSandboxOutput:
    boto3_raw_data: "type_defs.StartSandboxOutputTypeDef" = dataclasses.field()

    @cached_property
    def sandbox(self):  # pragma: no cover
        return Sandbox.make_one(self.boto3_raw_data["sandbox"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSandboxOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSandboxOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopSandboxOutput:
    boto3_raw_data: "type_defs.StopSandboxOutputTypeDef" = dataclasses.field()

    @cached_property
    def sandbox(self):  # pragma: no cover
        return Sandbox.make_one(self.boto3_raw_data["sandbox"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopSandboxOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopSandboxOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
