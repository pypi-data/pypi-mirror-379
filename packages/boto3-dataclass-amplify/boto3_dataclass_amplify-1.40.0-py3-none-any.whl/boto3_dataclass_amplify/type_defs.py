# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_amplify import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AutoBranchCreationConfigOutput:
    boto3_raw_data: "type_defs.AutoBranchCreationConfigOutputTypeDef" = (
        dataclasses.field()
    )

    stage = field("stage")
    framework = field("framework")
    enableAutoBuild = field("enableAutoBuild")
    environmentVariables = field("environmentVariables")
    basicAuthCredentials = field("basicAuthCredentials")
    enableBasicAuth = field("enableBasicAuth")
    enablePerformanceMode = field("enablePerformanceMode")
    buildSpec = field("buildSpec")
    enablePullRequestPreview = field("enablePullRequestPreview")
    pullRequestEnvironmentName = field("pullRequestEnvironmentName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutoBranchCreationConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoBranchCreationConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheConfig:
    boto3_raw_data: "type_defs.CacheConfigTypeDef" = dataclasses.field()

    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CacheConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CacheConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomRule:
    boto3_raw_data: "type_defs.CustomRuleTypeDef" = dataclasses.field()

    source = field("source")
    target = field("target")
    status = field("status")
    condition = field("condition")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobConfig:
    boto3_raw_data: "type_defs.JobConfigTypeDef" = dataclasses.field()

    buildComputeType = field("buildComputeType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProductionBranch:
    boto3_raw_data: "type_defs.ProductionBranchTypeDef" = dataclasses.field()

    lastDeployTime = field("lastDeployTime")
    status = field("status")
    thumbnailUrl = field("thumbnailUrl")
    branchName = field("branchName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProductionBranchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProductionBranchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WafConfiguration:
    boto3_raw_data: "type_defs.WafConfigurationTypeDef" = dataclasses.field()

    webAclArn = field("webAclArn")
    wafStatus = field("wafStatus")
    statusReason = field("statusReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WafConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WafConfigurationTypeDef"]
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

    artifactFileName = field("artifactFileName")
    artifactId = field("artifactId")

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
class AutoBranchCreationConfig:
    boto3_raw_data: "type_defs.AutoBranchCreationConfigTypeDef" = dataclasses.field()

    stage = field("stage")
    framework = field("framework")
    enableAutoBuild = field("enableAutoBuild")
    environmentVariables = field("environmentVariables")
    basicAuthCredentials = field("basicAuthCredentials")
    enableBasicAuth = field("enableBasicAuth")
    enablePerformanceMode = field("enablePerformanceMode")
    buildSpec = field("buildSpec")
    enablePullRequestPreview = field("enablePullRequestPreview")
    pullRequestEnvironmentName = field("pullRequestEnvironmentName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoBranchCreationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoBranchCreationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackendEnvironment:
    boto3_raw_data: "type_defs.BackendEnvironmentTypeDef" = dataclasses.field()

    backendEnvironmentArn = field("backendEnvironmentArn")
    environmentName = field("environmentName")
    createTime = field("createTime")
    updateTime = field("updateTime")
    stackName = field("stackName")
    deploymentArtifacts = field("deploymentArtifacts")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BackendEnvironmentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackendEnvironmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Backend:
    boto3_raw_data: "type_defs.BackendTypeDef" = dataclasses.field()

    stackArn = field("stackArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BackendTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BackendTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CertificateSettings:
    boto3_raw_data: "type_defs.CertificateSettingsTypeDef" = dataclasses.field()

    type = field("type")
    customCertificateArn = field("customCertificateArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CertificateSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CertificateSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Certificate:
    boto3_raw_data: "type_defs.CertificateTypeDef" = dataclasses.field()

    type = field("type")
    customCertificateArn = field("customCertificateArn")
    certificateVerificationDNSRecord = field("certificateVerificationDNSRecord")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CertificateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CertificateTypeDef"]]
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
class CreateBackendEnvironmentRequest:
    boto3_raw_data: "type_defs.CreateBackendEnvironmentRequestTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")
    environmentName = field("environmentName")
    stackName = field("stackName")
    deploymentArtifacts = field("deploymentArtifacts")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateBackendEnvironmentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeploymentRequest:
    boto3_raw_data: "type_defs.CreateDeploymentRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    branchName = field("branchName")
    fileMap = field("fileMap")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubDomainSetting:
    boto3_raw_data: "type_defs.SubDomainSettingTypeDef" = dataclasses.field()

    prefix = field("prefix")
    branchName = field("branchName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubDomainSettingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubDomainSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWebhookRequest:
    boto3_raw_data: "type_defs.CreateWebhookRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    branchName = field("branchName")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWebhookRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWebhookRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Webhook:
    boto3_raw_data: "type_defs.WebhookTypeDef" = dataclasses.field()

    webhookArn = field("webhookArn")
    webhookId = field("webhookId")
    webhookUrl = field("webhookUrl")
    branchName = field("branchName")
    description = field("description")
    createTime = field("createTime")
    updateTime = field("updateTime")
    appId = field("appId")

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
class DeleteAppRequest:
    boto3_raw_data: "type_defs.DeleteAppRequestTypeDef" = dataclasses.field()

    appId = field("appId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteAppRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAppRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBackendEnvironmentRequest:
    boto3_raw_data: "type_defs.DeleteBackendEnvironmentRequestTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")
    environmentName = field("environmentName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteBackendEnvironmentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBackendEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBranchRequest:
    boto3_raw_data: "type_defs.DeleteBranchRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    branchName = field("branchName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBranchRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBranchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainAssociationRequest:
    boto3_raw_data: "type_defs.DeleteDomainAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")
    domainName = field("domainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDomainAssociationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteJobRequest:
    boto3_raw_data: "type_defs.DeleteJobRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    branchName = field("branchName")
    jobId = field("jobId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobSummary:
    boto3_raw_data: "type_defs.JobSummaryTypeDef" = dataclasses.field()

    jobArn = field("jobArn")
    jobId = field("jobId")
    commitId = field("commitId")
    commitMessage = field("commitMessage")
    commitTime = field("commitTime")
    startTime = field("startTime")
    status = field("status")
    jobType = field("jobType")
    endTime = field("endTime")
    sourceUrl = field("sourceUrl")
    sourceUrlType = field("sourceUrlType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWebhookRequest:
    boto3_raw_data: "type_defs.DeleteWebhookRequestTypeDef" = dataclasses.field()

    webhookId = field("webhookId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWebhookRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWebhookRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppRequest:
    boto3_raw_data: "type_defs.GetAppRequestTypeDef" = dataclasses.field()

    appId = field("appId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAppRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetAppRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetArtifactUrlRequest:
    boto3_raw_data: "type_defs.GetArtifactUrlRequestTypeDef" = dataclasses.field()

    artifactId = field("artifactId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetArtifactUrlRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetArtifactUrlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackendEnvironmentRequest:
    boto3_raw_data: "type_defs.GetBackendEnvironmentRequestTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")
    environmentName = field("environmentName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBackendEnvironmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackendEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBranchRequest:
    boto3_raw_data: "type_defs.GetBranchRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    branchName = field("branchName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetBranchRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBranchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainAssociationRequest:
    boto3_raw_data: "type_defs.GetDomainAssociationRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    domainName = field("domainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDomainAssociationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobRequest:
    boto3_raw_data: "type_defs.GetJobRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    branchName = field("branchName")
    jobId = field("jobId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetJobRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWebhookRequest:
    boto3_raw_data: "type_defs.GetWebhookRequestTypeDef" = dataclasses.field()

    webhookId = field("webhookId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetWebhookRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWebhookRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Step:
    boto3_raw_data: "type_defs.StepTypeDef" = dataclasses.field()

    stepName = field("stepName")
    startTime = field("startTime")
    status = field("status")
    endTime = field("endTime")
    logUrl = field("logUrl")
    artifactsUrl = field("artifactsUrl")
    testArtifactsUrl = field("testArtifactsUrl")
    testConfigUrl = field("testConfigUrl")
    screenshots = field("screenshots")
    statusReason = field("statusReason")
    context = field("context")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StepTypeDef"]]
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
class ListAppsRequest:
    boto3_raw_data: "type_defs.ListAppsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAppsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListAppsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListArtifactsRequest:
    boto3_raw_data: "type_defs.ListArtifactsRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    branchName = field("branchName")
    jobId = field("jobId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListArtifactsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListArtifactsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackendEnvironmentsRequest:
    boto3_raw_data: "type_defs.ListBackendEnvironmentsRequestTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")
    environmentName = field("environmentName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBackendEnvironmentsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackendEnvironmentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBranchesRequest:
    boto3_raw_data: "type_defs.ListBranchesRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBranchesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBranchesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainAssociationsRequest:
    boto3_raw_data: "type_defs.ListDomainAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDomainAssociationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsRequest:
    boto3_raw_data: "type_defs.ListJobsRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    branchName = field("branchName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListJobsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListJobsRequestTypeDef"]],
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
class ListWebhooksRequest:
    boto3_raw_data: "type_defs.ListWebhooksRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWebhooksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWebhooksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDeploymentRequest:
    boto3_raw_data: "type_defs.StartDeploymentRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    branchName = field("branchName")
    jobId = field("jobId")
    sourceUrl = field("sourceUrl")
    sourceUrlType = field("sourceUrlType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopJobRequest:
    boto3_raw_data: "type_defs.StopJobRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    branchName = field("branchName")
    jobId = field("jobId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StopJobRequestTypeDef"]],
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
class UpdateWebhookRequest:
    boto3_raw_data: "type_defs.UpdateWebhookRequestTypeDef" = dataclasses.field()

    webhookId = field("webhookId")
    branchName = field("branchName")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWebhookRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWebhookRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class App:
    boto3_raw_data: "type_defs.AppTypeDef" = dataclasses.field()

    appId = field("appId")
    appArn = field("appArn")
    name = field("name")
    description = field("description")
    repository = field("repository")
    platform = field("platform")
    createTime = field("createTime")
    updateTime = field("updateTime")
    environmentVariables = field("environmentVariables")
    defaultDomain = field("defaultDomain")
    enableBranchAutoBuild = field("enableBranchAutoBuild")
    enableBasicAuth = field("enableBasicAuth")
    tags = field("tags")
    computeRoleArn = field("computeRoleArn")
    iamServiceRoleArn = field("iamServiceRoleArn")
    enableBranchAutoDeletion = field("enableBranchAutoDeletion")
    basicAuthCredentials = field("basicAuthCredentials")

    @cached_property
    def customRules(self):  # pragma: no cover
        return CustomRule.make_many(self.boto3_raw_data["customRules"])

    @cached_property
    def productionBranch(self):  # pragma: no cover
        return ProductionBranch.make_one(self.boto3_raw_data["productionBranch"])

    buildSpec = field("buildSpec")
    customHeaders = field("customHeaders")
    enableAutoBranchCreation = field("enableAutoBranchCreation")
    autoBranchCreationPatterns = field("autoBranchCreationPatterns")

    @cached_property
    def autoBranchCreationConfig(self):  # pragma: no cover
        return AutoBranchCreationConfigOutput.make_one(
            self.boto3_raw_data["autoBranchCreationConfig"]
        )

    repositoryCloneMethod = field("repositoryCloneMethod")

    @cached_property
    def cacheConfig(self):  # pragma: no cover
        return CacheConfig.make_one(self.boto3_raw_data["cacheConfig"])

    webhookCreateTime = field("webhookCreateTime")

    @cached_property
    def wafConfiguration(self):  # pragma: no cover
        return WafConfiguration.make_one(self.boto3_raw_data["wafConfiguration"])

    @cached_property
    def jobConfig(self):  # pragma: no cover
        return JobConfig.make_one(self.boto3_raw_data["jobConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AppTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Branch:
    boto3_raw_data: "type_defs.BranchTypeDef" = dataclasses.field()

    branchArn = field("branchArn")
    branchName = field("branchName")
    description = field("description")
    stage = field("stage")
    displayName = field("displayName")
    enableNotification = field("enableNotification")
    createTime = field("createTime")
    updateTime = field("updateTime")
    environmentVariables = field("environmentVariables")
    enableAutoBuild = field("enableAutoBuild")
    customDomains = field("customDomains")
    framework = field("framework")
    activeJobId = field("activeJobId")
    totalNumberOfJobs = field("totalNumberOfJobs")
    enableBasicAuth = field("enableBasicAuth")
    ttl = field("ttl")
    enablePullRequestPreview = field("enablePullRequestPreview")
    tags = field("tags")
    enableSkewProtection = field("enableSkewProtection")
    enablePerformanceMode = field("enablePerformanceMode")
    thumbnailUrl = field("thumbnailUrl")
    basicAuthCredentials = field("basicAuthCredentials")
    buildSpec = field("buildSpec")
    associatedResources = field("associatedResources")
    pullRequestEnvironmentName = field("pullRequestEnvironmentName")
    destinationBranch = field("destinationBranch")
    sourceBranch = field("sourceBranch")
    backendEnvironmentArn = field("backendEnvironmentArn")

    @cached_property
    def backend(self):  # pragma: no cover
        return Backend.make_one(self.boto3_raw_data["backend"])

    computeRoleArn = field("computeRoleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BranchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BranchTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBranchRequest:
    boto3_raw_data: "type_defs.CreateBranchRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    branchName = field("branchName")
    description = field("description")
    stage = field("stage")
    framework = field("framework")
    enableNotification = field("enableNotification")
    enableAutoBuild = field("enableAutoBuild")
    enableSkewProtection = field("enableSkewProtection")
    environmentVariables = field("environmentVariables")
    basicAuthCredentials = field("basicAuthCredentials")
    enableBasicAuth = field("enableBasicAuth")
    enablePerformanceMode = field("enablePerformanceMode")
    tags = field("tags")
    buildSpec = field("buildSpec")
    ttl = field("ttl")
    displayName = field("displayName")
    enablePullRequestPreview = field("enablePullRequestPreview")
    pullRequestEnvironmentName = field("pullRequestEnvironmentName")
    backendEnvironmentArn = field("backendEnvironmentArn")

    @cached_property
    def backend(self):  # pragma: no cover
        return Backend.make_one(self.boto3_raw_data["backend"])

    computeRoleArn = field("computeRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBranchRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBranchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBranchRequest:
    boto3_raw_data: "type_defs.UpdateBranchRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    branchName = field("branchName")
    description = field("description")
    framework = field("framework")
    stage = field("stage")
    enableNotification = field("enableNotification")
    enableAutoBuild = field("enableAutoBuild")
    enableSkewProtection = field("enableSkewProtection")
    environmentVariables = field("environmentVariables")
    basicAuthCredentials = field("basicAuthCredentials")
    enableBasicAuth = field("enableBasicAuth")
    enablePerformanceMode = field("enablePerformanceMode")
    buildSpec = field("buildSpec")
    ttl = field("ttl")
    displayName = field("displayName")
    enablePullRequestPreview = field("enablePullRequestPreview")
    pullRequestEnvironmentName = field("pullRequestEnvironmentName")
    backendEnvironmentArn = field("backendEnvironmentArn")

    @cached_property
    def backend(self):  # pragma: no cover
        return Backend.make_one(self.boto3_raw_data["backend"])

    computeRoleArn = field("computeRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBranchRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBranchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendEnvironmentResult:
    boto3_raw_data: "type_defs.CreateBackendEnvironmentResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def backendEnvironment(self):  # pragma: no cover
        return BackendEnvironment.make_one(self.boto3_raw_data["backendEnvironment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateBackendEnvironmentResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendEnvironmentResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeploymentResult:
    boto3_raw_data: "type_defs.CreateDeploymentResultTypeDef" = dataclasses.field()

    jobId = field("jobId")
    fileUploadUrls = field("fileUploadUrls")
    zipUploadUrl = field("zipUploadUrl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeploymentResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeploymentResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBackendEnvironmentResult:
    boto3_raw_data: "type_defs.DeleteBackendEnvironmentResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def backendEnvironment(self):  # pragma: no cover
        return BackendEnvironment.make_one(self.boto3_raw_data["backendEnvironment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteBackendEnvironmentResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBackendEnvironmentResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateAccessLogsResult:
    boto3_raw_data: "type_defs.GenerateAccessLogsResultTypeDef" = dataclasses.field()

    logUrl = field("logUrl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateAccessLogsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateAccessLogsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetArtifactUrlResult:
    boto3_raw_data: "type_defs.GetArtifactUrlResultTypeDef" = dataclasses.field()

    artifactId = field("artifactId")
    artifactUrl = field("artifactUrl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetArtifactUrlResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetArtifactUrlResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackendEnvironmentResult:
    boto3_raw_data: "type_defs.GetBackendEnvironmentResultTypeDef" = dataclasses.field()

    @cached_property
    def backendEnvironment(self):  # pragma: no cover
        return BackendEnvironment.make_one(self.boto3_raw_data["backendEnvironment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBackendEnvironmentResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackendEnvironmentResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListArtifactsResult:
    boto3_raw_data: "type_defs.ListArtifactsResultTypeDef" = dataclasses.field()

    @cached_property
    def artifacts(self):  # pragma: no cover
        return Artifact.make_many(self.boto3_raw_data["artifacts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListArtifactsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListArtifactsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackendEnvironmentsResult:
    boto3_raw_data: "type_defs.ListBackendEnvironmentsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def backendEnvironments(self):  # pragma: no cover
        return BackendEnvironment.make_many(self.boto3_raw_data["backendEnvironments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBackendEnvironmentsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackendEnvironmentsResultTypeDef"]
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
class CreateDomainAssociationRequest:
    boto3_raw_data: "type_defs.CreateDomainAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")
    domainName = field("domainName")

    @cached_property
    def subDomainSettings(self):  # pragma: no cover
        return SubDomainSetting.make_many(self.boto3_raw_data["subDomainSettings"])

    enableAutoSubDomain = field("enableAutoSubDomain")
    autoSubDomainCreationPatterns = field("autoSubDomainCreationPatterns")
    autoSubDomainIAMRole = field("autoSubDomainIAMRole")

    @cached_property
    def certificateSettings(self):  # pragma: no cover
        return CertificateSettings.make_one(self.boto3_raw_data["certificateSettings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDomainAssociationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubDomain:
    boto3_raw_data: "type_defs.SubDomainTypeDef" = dataclasses.field()

    @cached_property
    def subDomainSetting(self):  # pragma: no cover
        return SubDomainSetting.make_one(self.boto3_raw_data["subDomainSetting"])

    verified = field("verified")
    dnsRecord = field("dnsRecord")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubDomainTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubDomainTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainAssociationRequest:
    boto3_raw_data: "type_defs.UpdateDomainAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")
    domainName = field("domainName")
    enableAutoSubDomain = field("enableAutoSubDomain")

    @cached_property
    def subDomainSettings(self):  # pragma: no cover
        return SubDomainSetting.make_many(self.boto3_raw_data["subDomainSettings"])

    autoSubDomainCreationPatterns = field("autoSubDomainCreationPatterns")
    autoSubDomainIAMRole = field("autoSubDomainIAMRole")

    @cached_property
    def certificateSettings(self):  # pragma: no cover
        return CertificateSettings.make_one(self.boto3_raw_data["certificateSettings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDomainAssociationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWebhookResult:
    boto3_raw_data: "type_defs.CreateWebhookResultTypeDef" = dataclasses.field()

    @cached_property
    def webhook(self):  # pragma: no cover
        return Webhook.make_one(self.boto3_raw_data["webhook"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWebhookResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWebhookResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWebhookResult:
    boto3_raw_data: "type_defs.DeleteWebhookResultTypeDef" = dataclasses.field()

    @cached_property
    def webhook(self):  # pragma: no cover
        return Webhook.make_one(self.boto3_raw_data["webhook"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWebhookResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWebhookResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWebhookResult:
    boto3_raw_data: "type_defs.GetWebhookResultTypeDef" = dataclasses.field()

    @cached_property
    def webhook(self):  # pragma: no cover
        return Webhook.make_one(self.boto3_raw_data["webhook"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetWebhookResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWebhookResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWebhooksResult:
    boto3_raw_data: "type_defs.ListWebhooksResultTypeDef" = dataclasses.field()

    @cached_property
    def webhooks(self):  # pragma: no cover
        return Webhook.make_many(self.boto3_raw_data["webhooks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWebhooksResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWebhooksResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWebhookResult:
    boto3_raw_data: "type_defs.UpdateWebhookResultTypeDef" = dataclasses.field()

    @cached_property
    def webhook(self):  # pragma: no cover
        return Webhook.make_one(self.boto3_raw_data["webhook"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWebhookResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWebhookResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteJobResult:
    boto3_raw_data: "type_defs.DeleteJobResultTypeDef" = dataclasses.field()

    @cached_property
    def jobSummary(self):  # pragma: no cover
        return JobSummary.make_one(self.boto3_raw_data["jobSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteJobResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteJobResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsResult:
    boto3_raw_data: "type_defs.ListJobsResultTypeDef" = dataclasses.field()

    @cached_property
    def jobSummaries(self):  # pragma: no cover
        return JobSummary.make_many(self.boto3_raw_data["jobSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListJobsResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListJobsResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDeploymentResult:
    boto3_raw_data: "type_defs.StartDeploymentResultTypeDef" = dataclasses.field()

    @cached_property
    def jobSummary(self):  # pragma: no cover
        return JobSummary.make_one(self.boto3_raw_data["jobSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartDeploymentResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDeploymentResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartJobResult:
    boto3_raw_data: "type_defs.StartJobResultTypeDef" = dataclasses.field()

    @cached_property
    def jobSummary(self):  # pragma: no cover
        return JobSummary.make_one(self.boto3_raw_data["jobSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartJobResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StartJobResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopJobResult:
    boto3_raw_data: "type_defs.StopJobResultTypeDef" = dataclasses.field()

    @cached_property
    def jobSummary(self):  # pragma: no cover
        return JobSummary.make_one(self.boto3_raw_data["jobSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopJobResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StopJobResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateAccessLogsRequest:
    boto3_raw_data: "type_defs.GenerateAccessLogsRequestTypeDef" = dataclasses.field()

    domainName = field("domainName")
    appId = field("appId")
    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateAccessLogsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateAccessLogsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartJobRequest:
    boto3_raw_data: "type_defs.StartJobRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    branchName = field("branchName")
    jobType = field("jobType")
    jobId = field("jobId")
    jobReason = field("jobReason")
    commitId = field("commitId")
    commitMessage = field("commitMessage")
    commitTime = field("commitTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StartJobRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Job:
    boto3_raw_data: "type_defs.JobTypeDef" = dataclasses.field()

    @cached_property
    def summary(self):  # pragma: no cover
        return JobSummary.make_one(self.boto3_raw_data["summary"])

    @cached_property
    def steps(self):  # pragma: no cover
        return Step.make_many(self.boto3_raw_data["steps"])

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
class ListAppsRequestPaginate:
    boto3_raw_data: "type_defs.ListAppsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAppsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBranchesRequestPaginate:
    boto3_raw_data: "type_defs.ListBranchesRequestPaginateTypeDef" = dataclasses.field()

    appId = field("appId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBranchesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBranchesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.ListDomainAssociationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDomainAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainAssociationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListJobsRequestPaginateTypeDef" = dataclasses.field()

    appId = field("appId")
    branchName = field("branchName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppResult:
    boto3_raw_data: "type_defs.CreateAppResultTypeDef" = dataclasses.field()

    @cached_property
    def app(self):  # pragma: no cover
        return App.make_one(self.boto3_raw_data["app"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateAppResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CreateAppResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAppResult:
    boto3_raw_data: "type_defs.DeleteAppResultTypeDef" = dataclasses.field()

    @cached_property
    def app(self):  # pragma: no cover
        return App.make_one(self.boto3_raw_data["app"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteAppResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteAppResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppResult:
    boto3_raw_data: "type_defs.GetAppResultTypeDef" = dataclasses.field()

    @cached_property
    def app(self):  # pragma: no cover
        return App.make_one(self.boto3_raw_data["app"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAppResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetAppResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppsResult:
    boto3_raw_data: "type_defs.ListAppsResultTypeDef" = dataclasses.field()

    @cached_property
    def apps(self):  # pragma: no cover
        return App.make_many(self.boto3_raw_data["apps"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAppsResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListAppsResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAppResult:
    boto3_raw_data: "type_defs.UpdateAppResultTypeDef" = dataclasses.field()

    @cached_property
    def app(self):  # pragma: no cover
        return App.make_one(self.boto3_raw_data["app"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateAppResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateAppResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppRequest:
    boto3_raw_data: "type_defs.CreateAppRequestTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    repository = field("repository")
    platform = field("platform")
    computeRoleArn = field("computeRoleArn")
    iamServiceRoleArn = field("iamServiceRoleArn")
    oauthToken = field("oauthToken")
    accessToken = field("accessToken")
    environmentVariables = field("environmentVariables")
    enableBranchAutoBuild = field("enableBranchAutoBuild")
    enableBranchAutoDeletion = field("enableBranchAutoDeletion")
    enableBasicAuth = field("enableBasicAuth")
    basicAuthCredentials = field("basicAuthCredentials")

    @cached_property
    def customRules(self):  # pragma: no cover
        return CustomRule.make_many(self.boto3_raw_data["customRules"])

    tags = field("tags")
    buildSpec = field("buildSpec")
    customHeaders = field("customHeaders")
    enableAutoBranchCreation = field("enableAutoBranchCreation")
    autoBranchCreationPatterns = field("autoBranchCreationPatterns")
    autoBranchCreationConfig = field("autoBranchCreationConfig")

    @cached_property
    def jobConfig(self):  # pragma: no cover
        return JobConfig.make_one(self.boto3_raw_data["jobConfig"])

    @cached_property
    def cacheConfig(self):  # pragma: no cover
        return CacheConfig.make_one(self.boto3_raw_data["cacheConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateAppRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAppRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAppRequest:
    boto3_raw_data: "type_defs.UpdateAppRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    name = field("name")
    description = field("description")
    platform = field("platform")
    computeRoleArn = field("computeRoleArn")
    iamServiceRoleArn = field("iamServiceRoleArn")
    environmentVariables = field("environmentVariables")
    enableBranchAutoBuild = field("enableBranchAutoBuild")
    enableBranchAutoDeletion = field("enableBranchAutoDeletion")
    enableBasicAuth = field("enableBasicAuth")
    basicAuthCredentials = field("basicAuthCredentials")

    @cached_property
    def customRules(self):  # pragma: no cover
        return CustomRule.make_many(self.boto3_raw_data["customRules"])

    buildSpec = field("buildSpec")
    customHeaders = field("customHeaders")
    enableAutoBranchCreation = field("enableAutoBranchCreation")
    autoBranchCreationPatterns = field("autoBranchCreationPatterns")
    autoBranchCreationConfig = field("autoBranchCreationConfig")
    repository = field("repository")
    oauthToken = field("oauthToken")
    accessToken = field("accessToken")

    @cached_property
    def jobConfig(self):  # pragma: no cover
        return JobConfig.make_one(self.boto3_raw_data["jobConfig"])

    @cached_property
    def cacheConfig(self):  # pragma: no cover
        return CacheConfig.make_one(self.boto3_raw_data["cacheConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateAppRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAppRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBranchResult:
    boto3_raw_data: "type_defs.CreateBranchResultTypeDef" = dataclasses.field()

    @cached_property
    def branch(self):  # pragma: no cover
        return Branch.make_one(self.boto3_raw_data["branch"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBranchResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBranchResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBranchResult:
    boto3_raw_data: "type_defs.DeleteBranchResultTypeDef" = dataclasses.field()

    @cached_property
    def branch(self):  # pragma: no cover
        return Branch.make_one(self.boto3_raw_data["branch"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBranchResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBranchResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBranchResult:
    boto3_raw_data: "type_defs.GetBranchResultTypeDef" = dataclasses.field()

    @cached_property
    def branch(self):  # pragma: no cover
        return Branch.make_one(self.boto3_raw_data["branch"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetBranchResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetBranchResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBranchesResult:
    boto3_raw_data: "type_defs.ListBranchesResultTypeDef" = dataclasses.field()

    @cached_property
    def branches(self):  # pragma: no cover
        return Branch.make_many(self.boto3_raw_data["branches"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBranchesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBranchesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBranchResult:
    boto3_raw_data: "type_defs.UpdateBranchResultTypeDef" = dataclasses.field()

    @cached_property
    def branch(self):  # pragma: no cover
        return Branch.make_one(self.boto3_raw_data["branch"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBranchResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBranchResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainAssociation:
    boto3_raw_data: "type_defs.DomainAssociationTypeDef" = dataclasses.field()

    domainAssociationArn = field("domainAssociationArn")
    domainName = field("domainName")
    enableAutoSubDomain = field("enableAutoSubDomain")
    domainStatus = field("domainStatus")
    statusReason = field("statusReason")

    @cached_property
    def subDomains(self):  # pragma: no cover
        return SubDomain.make_many(self.boto3_raw_data["subDomains"])

    autoSubDomainCreationPatterns = field("autoSubDomainCreationPatterns")
    autoSubDomainIAMRole = field("autoSubDomainIAMRole")
    updateStatus = field("updateStatus")
    certificateVerificationDNSRecord = field("certificateVerificationDNSRecord")

    @cached_property
    def certificate(self):  # pragma: no cover
        return Certificate.make_one(self.boto3_raw_data["certificate"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainAssociationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobResult:
    boto3_raw_data: "type_defs.GetJobResultTypeDef" = dataclasses.field()

    @cached_property
    def job(self):  # pragma: no cover
        return Job.make_one(self.boto3_raw_data["job"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetJobResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetJobResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainAssociationResult:
    boto3_raw_data: "type_defs.CreateDomainAssociationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def domainAssociation(self):  # pragma: no cover
        return DomainAssociation.make_one(self.boto3_raw_data["domainAssociation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDomainAssociationResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainAssociationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainAssociationResult:
    boto3_raw_data: "type_defs.DeleteDomainAssociationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def domainAssociation(self):  # pragma: no cover
        return DomainAssociation.make_one(self.boto3_raw_data["domainAssociation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDomainAssociationResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainAssociationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainAssociationResult:
    boto3_raw_data: "type_defs.GetDomainAssociationResultTypeDef" = dataclasses.field()

    @cached_property
    def domainAssociation(self):  # pragma: no cover
        return DomainAssociation.make_one(self.boto3_raw_data["domainAssociation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDomainAssociationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainAssociationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainAssociationsResult:
    boto3_raw_data: "type_defs.ListDomainAssociationsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def domainAssociations(self):  # pragma: no cover
        return DomainAssociation.make_many(self.boto3_raw_data["domainAssociations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainAssociationsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainAssociationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainAssociationResult:
    boto3_raw_data: "type_defs.UpdateDomainAssociationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def domainAssociation(self):  # pragma: no cover
        return DomainAssociation.make_one(self.boto3_raw_data["domainAssociation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDomainAssociationResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainAssociationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
