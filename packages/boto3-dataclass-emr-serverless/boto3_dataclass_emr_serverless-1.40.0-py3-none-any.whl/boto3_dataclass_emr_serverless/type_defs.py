# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_emr_serverless import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ApplicationSummary:
    boto3_raw_data: "type_defs.ApplicationSummaryTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    releaseLabel = field("releaseLabel")
    type = field("type")
    state = field("state")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    name = field("name")
    stateDetails = field("stateDetails")
    architecture = field("architecture")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoStartConfig:
    boto3_raw_data: "type_defs.AutoStartConfigTypeDef" = dataclasses.field()

    enabled = field("enabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoStartConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AutoStartConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoStopConfig:
    boto3_raw_data: "type_defs.AutoStopConfigTypeDef" = dataclasses.field()

    enabled = field("enabled")
    idleTimeoutMinutes = field("idleTimeoutMinutes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoStopConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AutoStopConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationOutput:
    boto3_raw_data: "type_defs.ConfigurationOutputTypeDef" = dataclasses.field()

    classification = field("classification")
    properties = field("properties")
    configurations = field("configurations")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityCenterConfiguration:
    boto3_raw_data: "type_defs.IdentityCenterConfigurationTypeDef" = dataclasses.field()

    identityCenterInstanceArn = field("identityCenterInstanceArn")
    identityCenterApplicationArn = field("identityCenterApplicationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentityCenterConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityCenterConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageConfiguration:
    boto3_raw_data: "type_defs.ImageConfigurationTypeDef" = dataclasses.field()

    imageUri = field("imageUri")
    resolvedImageDigest = field("resolvedImageDigest")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InteractiveConfiguration:
    boto3_raw_data: "type_defs.InteractiveConfigurationTypeDef" = dataclasses.field()

    studioEnabled = field("studioEnabled")
    livyEndpointEnabled = field("livyEndpointEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InteractiveConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InteractiveConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaximumAllowedResources:
    boto3_raw_data: "type_defs.MaximumAllowedResourcesTypeDef" = dataclasses.field()

    cpu = field("cpu")
    memory = field("memory")
    disk = field("disk")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MaximumAllowedResourcesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaximumAllowedResourcesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkConfigurationOutput:
    boto3_raw_data: "type_defs.NetworkConfigurationOutputTypeDef" = dataclasses.field()

    subnetIds = field("subnetIds")
    securityGroupIds = field("securityGroupIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchedulerConfiguration:
    boto3_raw_data: "type_defs.SchedulerConfigurationTypeDef" = dataclasses.field()

    queueTimeoutMinutes = field("queueTimeoutMinutes")
    maxConcurrentRuns = field("maxConcurrentRuns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SchedulerConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchedulerConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelJobRunRequest:
    boto3_raw_data: "type_defs.CancelJobRunRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    jobRunId = field("jobRunId")
    shutdownGracePeriodInSeconds = field("shutdownGracePeriodInSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelJobRunRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelJobRunRequestTypeDef"]
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
class CloudWatchLoggingConfigurationOutput:
    boto3_raw_data: "type_defs.CloudWatchLoggingConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    enabled = field("enabled")
    logGroupName = field("logGroupName")
    logStreamNamePrefix = field("logStreamNamePrefix")
    encryptionKeyArn = field("encryptionKeyArn")
    logTypes = field("logTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CloudWatchLoggingConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLoggingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchLoggingConfiguration:
    boto3_raw_data: "type_defs.CloudWatchLoggingConfigurationTypeDef" = (
        dataclasses.field()
    )

    enabled = field("enabled")
    logGroupName = field("logGroupName")
    logStreamNamePrefix = field("logStreamNamePrefix")
    encryptionKeyArn = field("encryptionKeyArn")
    logTypes = field("logTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CloudWatchLoggingConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLoggingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Configuration:
    boto3_raw_data: "type_defs.ConfigurationTypeDef" = dataclasses.field()

    classification = field("classification")
    properties = field("properties")
    configurations = field("configurations")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConfigurationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityCenterConfigurationInput:
    boto3_raw_data: "type_defs.IdentityCenterConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    identityCenterInstanceArn = field("identityCenterInstanceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IdentityCenterConfigurationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityCenterConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageConfigurationInput:
    boto3_raw_data: "type_defs.ImageConfigurationInputTypeDef" = dataclasses.field()

    imageUri = field("imageUri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageConfigurationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationRequest:
    boto3_raw_data: "type_defs.DeleteApplicationRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationRequest:
    boto3_raw_data: "type_defs.GetApplicationRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDashboardForJobRunRequest:
    boto3_raw_data: "type_defs.GetDashboardForJobRunRequestTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    jobRunId = field("jobRunId")
    attempt = field("attempt")
    accessSystemProfileLogs = field("accessSystemProfileLogs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDashboardForJobRunRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDashboardForJobRunRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobRunRequest:
    boto3_raw_data: "type_defs.GetJobRunRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    jobRunId = field("jobRunId")
    attempt = field("attempt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetJobRunRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJobRunRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Hive:
    boto3_raw_data: "type_defs.HiveTypeDef" = dataclasses.field()

    query = field("query")
    initQueryFile = field("initQueryFile")
    parameters = field("parameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HiveTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HiveTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkerResourceConfig:
    boto3_raw_data: "type_defs.WorkerResourceConfigTypeDef" = dataclasses.field()

    cpu = field("cpu")
    memory = field("memory")
    disk = field("disk")
    diskType = field("diskType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkerResourceConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkerResourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SparkSubmitOutput:
    boto3_raw_data: "type_defs.SparkSubmitOutputTypeDef" = dataclasses.field()

    entryPoint = field("entryPoint")
    entryPointArguments = field("entryPointArguments")
    sparkSubmitParameters = field("sparkSubmitParameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SparkSubmitOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SparkSubmitOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SparkSubmit:
    boto3_raw_data: "type_defs.SparkSubmitTypeDef" = dataclasses.field()

    entryPoint = field("entryPoint")
    entryPointArguments = field("entryPointArguments")
    sparkSubmitParameters = field("sparkSubmitParameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SparkSubmitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SparkSubmitTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobRunAttemptSummary:
    boto3_raw_data: "type_defs.JobRunAttemptSummaryTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    id = field("id")
    arn = field("arn")
    createdBy = field("createdBy")
    jobCreatedAt = field("jobCreatedAt")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    executionRole = field("executionRole")
    state = field("state")
    stateDetails = field("stateDetails")
    releaseLabel = field("releaseLabel")
    name = field("name")
    mode = field("mode")
    type = field("type")
    attempt = field("attempt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobRunAttemptSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobRunAttemptSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobRunExecutionIamPolicyOutput:
    boto3_raw_data: "type_defs.JobRunExecutionIamPolicyOutputTypeDef" = (
        dataclasses.field()
    )

    policy = field("policy")
    policyArns = field("policyArns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.JobRunExecutionIamPolicyOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobRunExecutionIamPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobRunExecutionIamPolicy:
    boto3_raw_data: "type_defs.JobRunExecutionIamPolicyTypeDef" = dataclasses.field()

    policy = field("policy")
    policyArns = field("policyArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobRunExecutionIamPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobRunExecutionIamPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobRunSummary:
    boto3_raw_data: "type_defs.JobRunSummaryTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    id = field("id")
    arn = field("arn")
    createdBy = field("createdBy")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    executionRole = field("executionRole")
    state = field("state")
    stateDetails = field("stateDetails")
    releaseLabel = field("releaseLabel")
    name = field("name")
    mode = field("mode")
    type = field("type")
    attempt = field("attempt")
    attemptCreatedAt = field("attemptCreatedAt")
    attemptUpdatedAt = field("attemptUpdatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobRunSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobRunSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceUtilization:
    boto3_raw_data: "type_defs.ResourceUtilizationTypeDef" = dataclasses.field()

    vCPUHour = field("vCPUHour")
    memoryGBHour = field("memoryGBHour")
    storageGBHour = field("storageGBHour")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceUtilizationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceUtilizationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetryPolicy:
    boto3_raw_data: "type_defs.RetryPolicyTypeDef" = dataclasses.field()

    maxAttempts = field("maxAttempts")
    maxFailedAttemptsPerHour = field("maxFailedAttemptsPerHour")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetryPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RetryPolicyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TotalResourceUtilization:
    boto3_raw_data: "type_defs.TotalResourceUtilizationTypeDef" = dataclasses.field()

    vCPUHour = field("vCPUHour")
    memoryGBHour = field("memoryGBHour")
    storageGBHour = field("storageGBHour")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TotalResourceUtilizationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TotalResourceUtilizationTypeDef"]
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
class ListApplicationsRequest:
    boto3_raw_data: "type_defs.ListApplicationsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    states = field("states")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApplicationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobRunAttemptsRequest:
    boto3_raw_data: "type_defs.ListJobRunAttemptsRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    jobRunId = field("jobRunId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobRunAttemptsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobRunAttemptsRequestTypeDef"]
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
class ManagedPersistenceMonitoringConfiguration:
    boto3_raw_data: "type_defs.ManagedPersistenceMonitoringConfigurationTypeDef" = (
        dataclasses.field()
    )

    enabled = field("enabled")
    encryptionKeyArn = field("encryptionKeyArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ManagedPersistenceMonitoringConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedPersistenceMonitoringConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrometheusMonitoringConfiguration:
    boto3_raw_data: "type_defs.PrometheusMonitoringConfigurationTypeDef" = (
        dataclasses.field()
    )

    remoteWriteUrl = field("remoteWriteUrl")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PrometheusMonitoringConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrometheusMonitoringConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3MonitoringConfiguration:
    boto3_raw_data: "type_defs.S3MonitoringConfigurationTypeDef" = dataclasses.field()

    logUri = field("logUri")
    encryptionKeyArn = field("encryptionKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3MonitoringConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3MonitoringConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkConfiguration:
    boto3_raw_data: "type_defs.NetworkConfigurationTypeDef" = dataclasses.field()

    subnetIds = field("subnetIds")
    securityGroupIds = field("securityGroupIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartApplicationRequest:
    boto3_raw_data: "type_defs.StartApplicationRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopApplicationRequest:
    boto3_raw_data: "type_defs.StopApplicationRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopApplicationRequestTypeDef"]
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
class WorkerTypeSpecification:
    boto3_raw_data: "type_defs.WorkerTypeSpecificationTypeDef" = dataclasses.field()

    @cached_property
    def imageConfiguration(self):  # pragma: no cover
        return ImageConfiguration.make_one(self.boto3_raw_data["imageConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkerTypeSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkerTypeSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelJobRunResponse:
    boto3_raw_data: "type_defs.CancelJobRunResponseTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    jobRunId = field("jobRunId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelJobRunResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelJobRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationResponse:
    boto3_raw_data: "type_defs.CreateApplicationResponseTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    name = field("name")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDashboardForJobRunResponse:
    boto3_raw_data: "type_defs.GetDashboardForJobRunResponseTypeDef" = (
        dataclasses.field()
    )

    url = field("url")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDashboardForJobRunResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDashboardForJobRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsResponse:
    boto3_raw_data: "type_defs.ListApplicationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def applications(self):  # pragma: no cover
        return ApplicationSummary.make_many(self.boto3_raw_data["applications"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApplicationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsResponseTypeDef"]
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
class StartJobRunResponse:
    boto3_raw_data: "type_defs.StartJobRunResponseTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    jobRunId = field("jobRunId")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartJobRunResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartJobRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkerTypeSpecificationInput:
    boto3_raw_data: "type_defs.WorkerTypeSpecificationInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def imageConfiguration(self):  # pragma: no cover
        return ImageConfigurationInput.make_one(
            self.boto3_raw_data["imageConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkerTypeSpecificationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkerTypeSpecificationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InitialCapacityConfig:
    boto3_raw_data: "type_defs.InitialCapacityConfigTypeDef" = dataclasses.field()

    workerCount = field("workerCount")

    @cached_property
    def workerConfiguration(self):  # pragma: no cover
        return WorkerResourceConfig.make_one(self.boto3_raw_data["workerConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InitialCapacityConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InitialCapacityConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobDriverOutput:
    boto3_raw_data: "type_defs.JobDriverOutputTypeDef" = dataclasses.field()

    @cached_property
    def sparkSubmit(self):  # pragma: no cover
        return SparkSubmitOutput.make_one(self.boto3_raw_data["sparkSubmit"])

    @cached_property
    def hive(self):  # pragma: no cover
        return Hive.make_one(self.boto3_raw_data["hive"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobDriverOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobDriverOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobDriver:
    boto3_raw_data: "type_defs.JobDriverTypeDef" = dataclasses.field()

    @cached_property
    def sparkSubmit(self):  # pragma: no cover
        return SparkSubmit.make_one(self.boto3_raw_data["sparkSubmit"])

    @cached_property
    def hive(self):  # pragma: no cover
        return Hive.make_one(self.boto3_raw_data["hive"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobDriverTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobDriverTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobRunAttemptsResponse:
    boto3_raw_data: "type_defs.ListJobRunAttemptsResponseTypeDef" = dataclasses.field()

    @cached_property
    def jobRunAttempts(self):  # pragma: no cover
        return JobRunAttemptSummary.make_many(self.boto3_raw_data["jobRunAttempts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobRunAttemptsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobRunAttemptsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobRunsResponse:
    boto3_raw_data: "type_defs.ListJobRunsResponseTypeDef" = dataclasses.field()

    @cached_property
    def jobRuns(self):  # pragma: no cover
        return JobRunSummary.make_many(self.boto3_raw_data["jobRuns"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobRunsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobRunsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsRequestPaginate:
    boto3_raw_data: "type_defs.ListApplicationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    states = field("states")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobRunAttemptsRequestPaginate:
    boto3_raw_data: "type_defs.ListJobRunAttemptsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    jobRunId = field("jobRunId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListJobRunAttemptsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobRunAttemptsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobRunsRequestPaginate:
    boto3_raw_data: "type_defs.ListJobRunsRequestPaginateTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    createdAtAfter = field("createdAtAfter")
    createdAtBefore = field("createdAtBefore")
    states = field("states")
    mode = field("mode")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobRunsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobRunsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobRunsRequest:
    boto3_raw_data: "type_defs.ListJobRunsRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    createdAtAfter = field("createdAtAfter")
    createdAtBefore = field("createdAtBefore")
    states = field("states")
    mode = field("mode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobRunsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobRunsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitoringConfigurationOutput:
    boto3_raw_data: "type_defs.MonitoringConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3MonitoringConfiguration(self):  # pragma: no cover
        return S3MonitoringConfiguration.make_one(
            self.boto3_raw_data["s3MonitoringConfiguration"]
        )

    @cached_property
    def managedPersistenceMonitoringConfiguration(self):  # pragma: no cover
        return ManagedPersistenceMonitoringConfiguration.make_one(
            self.boto3_raw_data["managedPersistenceMonitoringConfiguration"]
        )

    @cached_property
    def cloudWatchLoggingConfiguration(self):  # pragma: no cover
        return CloudWatchLoggingConfigurationOutput.make_one(
            self.boto3_raw_data["cloudWatchLoggingConfiguration"]
        )

    @cached_property
    def prometheusMonitoringConfiguration(self):  # pragma: no cover
        return PrometheusMonitoringConfiguration.make_one(
            self.boto3_raw_data["prometheusMonitoringConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MonitoringConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MonitoringConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitoringConfiguration:
    boto3_raw_data: "type_defs.MonitoringConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def s3MonitoringConfiguration(self):  # pragma: no cover
        return S3MonitoringConfiguration.make_one(
            self.boto3_raw_data["s3MonitoringConfiguration"]
        )

    @cached_property
    def managedPersistenceMonitoringConfiguration(self):  # pragma: no cover
        return ManagedPersistenceMonitoringConfiguration.make_one(
            self.boto3_raw_data["managedPersistenceMonitoringConfiguration"]
        )

    @cached_property
    def cloudWatchLoggingConfiguration(self):  # pragma: no cover
        return CloudWatchLoggingConfiguration.make_one(
            self.boto3_raw_data["cloudWatchLoggingConfiguration"]
        )

    @cached_property
    def prometheusMonitoringConfiguration(self):  # pragma: no cover
        return PrometheusMonitoringConfiguration.make_one(
            self.boto3_raw_data["prometheusMonitoringConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MonitoringConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MonitoringConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Application:
    boto3_raw_data: "type_defs.ApplicationTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    arn = field("arn")
    releaseLabel = field("releaseLabel")
    type = field("type")
    state = field("state")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    name = field("name")
    stateDetails = field("stateDetails")
    initialCapacity = field("initialCapacity")

    @cached_property
    def maximumCapacity(self):  # pragma: no cover
        return MaximumAllowedResources.make_one(self.boto3_raw_data["maximumCapacity"])

    tags = field("tags")

    @cached_property
    def autoStartConfiguration(self):  # pragma: no cover
        return AutoStartConfig.make_one(self.boto3_raw_data["autoStartConfiguration"])

    @cached_property
    def autoStopConfiguration(self):  # pragma: no cover
        return AutoStopConfig.make_one(self.boto3_raw_data["autoStopConfiguration"])

    @cached_property
    def networkConfiguration(self):  # pragma: no cover
        return NetworkConfigurationOutput.make_one(
            self.boto3_raw_data["networkConfiguration"]
        )

    architecture = field("architecture")

    @cached_property
    def imageConfiguration(self):  # pragma: no cover
        return ImageConfiguration.make_one(self.boto3_raw_data["imageConfiguration"])

    workerTypeSpecifications = field("workerTypeSpecifications")

    @cached_property
    def runtimeConfiguration(self):  # pragma: no cover
        return ConfigurationOutput.make_many(
            self.boto3_raw_data["runtimeConfiguration"]
        )

    @cached_property
    def monitoringConfiguration(self):  # pragma: no cover
        return MonitoringConfigurationOutput.make_one(
            self.boto3_raw_data["monitoringConfiguration"]
        )

    @cached_property
    def interactiveConfiguration(self):  # pragma: no cover
        return InteractiveConfiguration.make_one(
            self.boto3_raw_data["interactiveConfiguration"]
        )

    @cached_property
    def schedulerConfiguration(self):  # pragma: no cover
        return SchedulerConfiguration.make_one(
            self.boto3_raw_data["schedulerConfiguration"]
        )

    @cached_property
    def identityCenterConfiguration(self):  # pragma: no cover
        return IdentityCenterConfiguration.make_one(
            self.boto3_raw_data["identityCenterConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApplicationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApplicationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationOverridesOutput:
    boto3_raw_data: "type_defs.ConfigurationOverridesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def applicationConfiguration(self):  # pragma: no cover
        return ConfigurationOutput.make_many(
            self.boto3_raw_data["applicationConfiguration"]
        )

    @cached_property
    def monitoringConfiguration(self):  # pragma: no cover
        return MonitoringConfigurationOutput.make_one(
            self.boto3_raw_data["monitoringConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationOverridesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationOverridesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationOverrides:
    boto3_raw_data: "type_defs.ConfigurationOverridesTypeDef" = dataclasses.field()

    @cached_property
    def applicationConfiguration(self):  # pragma: no cover
        return Configuration.make_many(self.boto3_raw_data["applicationConfiguration"])

    @cached_property
    def monitoringConfiguration(self):  # pragma: no cover
        return MonitoringConfiguration.make_one(
            self.boto3_raw_data["monitoringConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationOverridesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationOverridesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationResponse:
    boto3_raw_data: "type_defs.GetApplicationResponseTypeDef" = dataclasses.field()

    @cached_property
    def application(self):  # pragma: no cover
        return Application.make_one(self.boto3_raw_data["application"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApplicationResponse:
    boto3_raw_data: "type_defs.UpdateApplicationResponseTypeDef" = dataclasses.field()

    @cached_property
    def application(self):  # pragma: no cover
        return Application.make_one(self.boto3_raw_data["application"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobRun:
    boto3_raw_data: "type_defs.JobRunTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    jobRunId = field("jobRunId")
    arn = field("arn")
    createdBy = field("createdBy")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    executionRole = field("executionRole")
    state = field("state")
    stateDetails = field("stateDetails")
    releaseLabel = field("releaseLabel")

    @cached_property
    def jobDriver(self):  # pragma: no cover
        return JobDriverOutput.make_one(self.boto3_raw_data["jobDriver"])

    name = field("name")

    @cached_property
    def executionIamPolicy(self):  # pragma: no cover
        return JobRunExecutionIamPolicyOutput.make_one(
            self.boto3_raw_data["executionIamPolicy"]
        )

    @cached_property
    def configurationOverrides(self):  # pragma: no cover
        return ConfigurationOverridesOutput.make_one(
            self.boto3_raw_data["configurationOverrides"]
        )

    tags = field("tags")

    @cached_property
    def totalResourceUtilization(self):  # pragma: no cover
        return TotalResourceUtilization.make_one(
            self.boto3_raw_data["totalResourceUtilization"]
        )

    @cached_property
    def networkConfiguration(self):  # pragma: no cover
        return NetworkConfigurationOutput.make_one(
            self.boto3_raw_data["networkConfiguration"]
        )

    totalExecutionDurationSeconds = field("totalExecutionDurationSeconds")
    executionTimeoutMinutes = field("executionTimeoutMinutes")

    @cached_property
    def billedResourceUtilization(self):  # pragma: no cover
        return ResourceUtilization.make_one(
            self.boto3_raw_data["billedResourceUtilization"]
        )

    mode = field("mode")

    @cached_property
    def retryPolicy(self):  # pragma: no cover
        return RetryPolicy.make_one(self.boto3_raw_data["retryPolicy"])

    attempt = field("attempt")
    attemptCreatedAt = field("attemptCreatedAt")
    attemptUpdatedAt = field("attemptUpdatedAt")
    startedAt = field("startedAt")
    endedAt = field("endedAt")
    queuedDurationMilliseconds = field("queuedDurationMilliseconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobRunTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobRunTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationRequest:
    boto3_raw_data: "type_defs.CreateApplicationRequestTypeDef" = dataclasses.field()

    releaseLabel = field("releaseLabel")
    type = field("type")
    clientToken = field("clientToken")
    name = field("name")
    initialCapacity = field("initialCapacity")

    @cached_property
    def maximumCapacity(self):  # pragma: no cover
        return MaximumAllowedResources.make_one(self.boto3_raw_data["maximumCapacity"])

    tags = field("tags")

    @cached_property
    def autoStartConfiguration(self):  # pragma: no cover
        return AutoStartConfig.make_one(self.boto3_raw_data["autoStartConfiguration"])

    @cached_property
    def autoStopConfiguration(self):  # pragma: no cover
        return AutoStopConfig.make_one(self.boto3_raw_data["autoStopConfiguration"])

    networkConfiguration = field("networkConfiguration")
    architecture = field("architecture")

    @cached_property
    def imageConfiguration(self):  # pragma: no cover
        return ImageConfigurationInput.make_one(
            self.boto3_raw_data["imageConfiguration"]
        )

    workerTypeSpecifications = field("workerTypeSpecifications")
    runtimeConfiguration = field("runtimeConfiguration")
    monitoringConfiguration = field("monitoringConfiguration")

    @cached_property
    def interactiveConfiguration(self):  # pragma: no cover
        return InteractiveConfiguration.make_one(
            self.boto3_raw_data["interactiveConfiguration"]
        )

    @cached_property
    def schedulerConfiguration(self):  # pragma: no cover
        return SchedulerConfiguration.make_one(
            self.boto3_raw_data["schedulerConfiguration"]
        )

    @cached_property
    def identityCenterConfiguration(self):  # pragma: no cover
        return IdentityCenterConfigurationInput.make_one(
            self.boto3_raw_data["identityCenterConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApplicationRequest:
    boto3_raw_data: "type_defs.UpdateApplicationRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    clientToken = field("clientToken")
    initialCapacity = field("initialCapacity")

    @cached_property
    def maximumCapacity(self):  # pragma: no cover
        return MaximumAllowedResources.make_one(self.boto3_raw_data["maximumCapacity"])

    @cached_property
    def autoStartConfiguration(self):  # pragma: no cover
        return AutoStartConfig.make_one(self.boto3_raw_data["autoStartConfiguration"])

    @cached_property
    def autoStopConfiguration(self):  # pragma: no cover
        return AutoStopConfig.make_one(self.boto3_raw_data["autoStopConfiguration"])

    networkConfiguration = field("networkConfiguration")
    architecture = field("architecture")

    @cached_property
    def imageConfiguration(self):  # pragma: no cover
        return ImageConfigurationInput.make_one(
            self.boto3_raw_data["imageConfiguration"]
        )

    workerTypeSpecifications = field("workerTypeSpecifications")

    @cached_property
    def interactiveConfiguration(self):  # pragma: no cover
        return InteractiveConfiguration.make_one(
            self.boto3_raw_data["interactiveConfiguration"]
        )

    releaseLabel = field("releaseLabel")
    runtimeConfiguration = field("runtimeConfiguration")
    monitoringConfiguration = field("monitoringConfiguration")

    @cached_property
    def schedulerConfiguration(self):  # pragma: no cover
        return SchedulerConfiguration.make_one(
            self.boto3_raw_data["schedulerConfiguration"]
        )

    @cached_property
    def identityCenterConfiguration(self):  # pragma: no cover
        return IdentityCenterConfigurationInput.make_one(
            self.boto3_raw_data["identityCenterConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobRunResponse:
    boto3_raw_data: "type_defs.GetJobRunResponseTypeDef" = dataclasses.field()

    @cached_property
    def jobRun(self):  # pragma: no cover
        return JobRun.make_one(self.boto3_raw_data["jobRun"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetJobRunResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJobRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartJobRunRequest:
    boto3_raw_data: "type_defs.StartJobRunRequestTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    clientToken = field("clientToken")
    executionRoleArn = field("executionRoleArn")
    executionIamPolicy = field("executionIamPolicy")
    jobDriver = field("jobDriver")
    configurationOverrides = field("configurationOverrides")
    tags = field("tags")
    executionTimeoutMinutes = field("executionTimeoutMinutes")
    name = field("name")
    mode = field("mode")

    @cached_property
    def retryPolicy(self):  # pragma: no cover
        return RetryPolicy.make_one(self.boto3_raw_data["retryPolicy"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartJobRunRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartJobRunRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
