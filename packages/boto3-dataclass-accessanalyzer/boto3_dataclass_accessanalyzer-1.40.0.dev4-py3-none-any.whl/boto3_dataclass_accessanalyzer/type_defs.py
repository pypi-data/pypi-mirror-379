# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_accessanalyzer import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccessPreviewStatusReason:
    boto3_raw_data: "type_defs.AccessPreviewStatusReasonTypeDef" = dataclasses.field()

    code = field("code")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessPreviewStatusReasonTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessPreviewStatusReasonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Access:
    boto3_raw_data: "type_defs.AccessTypeDef" = dataclasses.field()

    actions = field("actions")
    resources = field("resources")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccessTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AclGrantee:
    boto3_raw_data: "type_defs.AclGranteeTypeDef" = dataclasses.field()

    id = field("id")
    uri = field("uri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AclGranteeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AclGranteeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisRuleCriteriaOutput:
    boto3_raw_data: "type_defs.AnalysisRuleCriteriaOutputTypeDef" = dataclasses.field()

    accountIds = field("accountIds")
    resourceTags = field("resourceTags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalysisRuleCriteriaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisRuleCriteriaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisRuleCriteria:
    boto3_raw_data: "type_defs.AnalysisRuleCriteriaTypeDef" = dataclasses.field()

    accountIds = field("accountIds")
    resourceTags = field("resourceTags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalysisRuleCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisRuleCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyzedResourceSummary:
    boto3_raw_data: "type_defs.AnalyzedResourceSummaryTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    resourceOwnerAccount = field("resourceOwnerAccount")
    resourceType = field("resourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyzedResourceSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyzedResourceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyzedResource:
    boto3_raw_data: "type_defs.AnalyzedResourceTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    resourceType = field("resourceType")
    createdAt = field("createdAt")
    analyzedAt = field("analyzedAt")
    updatedAt = field("updatedAt")
    isPublic = field("isPublic")
    resourceOwnerAccount = field("resourceOwnerAccount")
    actions = field("actions")
    sharedVia = field("sharedVia")
    status = field("status")
    error = field("error")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalyzedResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyzedResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatusReason:
    boto3_raw_data: "type_defs.StatusReasonTypeDef" = dataclasses.field()

    code = field("code")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatusReasonTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatusReasonTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplyArchiveRuleRequest:
    boto3_raw_data: "type_defs.ApplyArchiveRuleRequestTypeDef" = dataclasses.field()

    analyzerArn = field("analyzerArn")
    ruleName = field("ruleName")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplyArchiveRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplyArchiveRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CriterionOutput:
    boto3_raw_data: "type_defs.CriterionOutputTypeDef" = dataclasses.field()

    eq = field("eq")
    neq = field("neq")
    contains = field("contains")
    exists = field("exists")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CriterionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CriterionOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelPolicyGenerationRequest:
    boto3_raw_data: "type_defs.CancelPolicyGenerationRequestTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelPolicyGenerationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelPolicyGenerationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReasonSummary:
    boto3_raw_data: "type_defs.ReasonSummaryTypeDef" = dataclasses.field()

    description = field("description")
    statementIndex = field("statementIndex")
    statementId = field("statementId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReasonSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReasonSummaryTypeDef"]],
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
class CheckNoNewAccessRequest:
    boto3_raw_data: "type_defs.CheckNoNewAccessRequestTypeDef" = dataclasses.field()

    newPolicyDocument = field("newPolicyDocument")
    existingPolicyDocument = field("existingPolicyDocument")
    policyType = field("policyType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CheckNoNewAccessRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckNoNewAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckNoPublicAccessRequest:
    boto3_raw_data: "type_defs.CheckNoPublicAccessRequestTypeDef" = dataclasses.field()

    policyDocument = field("policyDocument")
    resourceType = field("resourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CheckNoPublicAccessRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckNoPublicAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Trail:
    boto3_raw_data: "type_defs.TrailTypeDef" = dataclasses.field()

    cloudTrailArn = field("cloudTrailArn")
    regions = field("regions")
    allRegions = field("allRegions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TrailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrailProperties:
    boto3_raw_data: "type_defs.TrailPropertiesTypeDef" = dataclasses.field()

    cloudTrailArn = field("cloudTrailArn")
    regions = field("regions")
    allRegions = field("allRegions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrailPropertiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TrailPropertiesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DynamodbStreamConfiguration:
    boto3_raw_data: "type_defs.DynamodbStreamConfigurationTypeDef" = dataclasses.field()

    streamPolicy = field("streamPolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DynamodbStreamConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DynamodbStreamConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DynamodbTableConfiguration:
    boto3_raw_data: "type_defs.DynamodbTableConfigurationTypeDef" = dataclasses.field()

    tablePolicy = field("tablePolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DynamodbTableConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DynamodbTableConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EbsSnapshotConfigurationOutput:
    boto3_raw_data: "type_defs.EbsSnapshotConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    userIds = field("userIds")
    groups = field("groups")
    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EbsSnapshotConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EbsSnapshotConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcrRepositoryConfiguration:
    boto3_raw_data: "type_defs.EcrRepositoryConfigurationTypeDef" = dataclasses.field()

    repositoryPolicy = field("repositoryPolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EcrRepositoryConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcrRepositoryConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EfsFileSystemConfiguration:
    boto3_raw_data: "type_defs.EfsFileSystemConfigurationTypeDef" = dataclasses.field()

    fileSystemPolicy = field("fileSystemPolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EfsFileSystemConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EfsFileSystemConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IamRoleConfiguration:
    boto3_raw_data: "type_defs.IamRoleConfigurationTypeDef" = dataclasses.field()

    trustPolicy = field("trustPolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IamRoleConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IamRoleConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecretsManagerSecretConfiguration:
    boto3_raw_data: "type_defs.SecretsManagerSecretConfigurationTypeDef" = (
        dataclasses.field()
    )

    kmsKeyId = field("kmsKeyId")
    secretPolicy = field("secretPolicy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SecretsManagerSecretConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecretsManagerSecretConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnsTopicConfiguration:
    boto3_raw_data: "type_defs.SnsTopicConfigurationTypeDef" = dataclasses.field()

    topicPolicy = field("topicPolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnsTopicConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnsTopicConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SqsQueueConfiguration:
    boto3_raw_data: "type_defs.SqsQueueConfigurationTypeDef" = dataclasses.field()

    queuePolicy = field("queuePolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SqsQueueConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SqsQueueConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Criterion:
    boto3_raw_data: "type_defs.CriterionTypeDef" = dataclasses.field()

    eq = field("eq")
    neq = field("neq")
    contains = field("contains")
    exists = field("exists")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CriterionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CriterionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAnalyzerRequest:
    boto3_raw_data: "type_defs.DeleteAnalyzerRequestTypeDef" = dataclasses.field()

    analyzerName = field("analyzerName")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAnalyzerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAnalyzerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteArchiveRuleRequest:
    boto3_raw_data: "type_defs.DeleteArchiveRuleRequestTypeDef" = dataclasses.field()

    analyzerName = field("analyzerName")
    ruleName = field("ruleName")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteArchiveRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteArchiveRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EbsSnapshotConfiguration:
    boto3_raw_data: "type_defs.EbsSnapshotConfigurationTypeDef" = dataclasses.field()

    userIds = field("userIds")
    groups = field("groups")
    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EbsSnapshotConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EbsSnapshotConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceTypeDetails:
    boto3_raw_data: "type_defs.ResourceTypeDetailsTypeDef" = dataclasses.field()

    totalActivePublic = field("totalActivePublic")
    totalActiveCrossAccount = field("totalActiveCrossAccount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceTypeDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceTypeDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingAggregationAccountDetails:
    boto3_raw_data: "type_defs.FindingAggregationAccountDetailsTypeDef" = (
        dataclasses.field()
    )

    account = field("account")
    numberOfActiveFindings = field("numberOfActiveFindings")
    details = field("details")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FindingAggregationAccountDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FindingAggregationAccountDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnusedIamRoleDetails:
    boto3_raw_data: "type_defs.UnusedIamRoleDetailsTypeDef" = dataclasses.field()

    lastAccessed = field("lastAccessed")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnusedIamRoleDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnusedIamRoleDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnusedIamUserAccessKeyDetails:
    boto3_raw_data: "type_defs.UnusedIamUserAccessKeyDetailsTypeDef" = (
        dataclasses.field()
    )

    accessKeyId = field("accessKeyId")
    lastAccessed = field("lastAccessed")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UnusedIamUserAccessKeyDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnusedIamUserAccessKeyDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnusedIamUserPasswordDetails:
    boto3_raw_data: "type_defs.UnusedIamUserPasswordDetailsTypeDef" = (
        dataclasses.field()
    )

    lastAccessed = field("lastAccessed")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnusedIamUserPasswordDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnusedIamUserPasswordDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingSourceDetail:
    boto3_raw_data: "type_defs.FindingSourceDetailTypeDef" = dataclasses.field()

    accessPointArn = field("accessPointArn")
    accessPointAccount = field("accessPointAccount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FindingSourceDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FindingSourceDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingSummaryV2:
    boto3_raw_data: "type_defs.FindingSummaryV2TypeDef" = dataclasses.field()

    analyzedAt = field("analyzedAt")
    createdAt = field("createdAt")
    id = field("id")
    resourceType = field("resourceType")
    resourceOwnerAccount = field("resourceOwnerAccount")
    status = field("status")
    updatedAt = field("updatedAt")
    error = field("error")
    resource = field("resource")
    findingType = field("findingType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FindingSummaryV2TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FindingSummaryV2TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateFindingRecommendationRequest:
    boto3_raw_data: "type_defs.GenerateFindingRecommendationRequestTypeDef" = (
        dataclasses.field()
    )

    analyzerArn = field("analyzerArn")
    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GenerateFindingRecommendationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateFindingRecommendationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeneratedPolicy:
    boto3_raw_data: "type_defs.GeneratedPolicyTypeDef" = dataclasses.field()

    policy = field("policy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GeneratedPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GeneratedPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessPreviewRequest:
    boto3_raw_data: "type_defs.GetAccessPreviewRequestTypeDef" = dataclasses.field()

    accessPreviewId = field("accessPreviewId")
    analyzerArn = field("analyzerArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccessPreviewRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessPreviewRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnalyzedResourceRequest:
    boto3_raw_data: "type_defs.GetAnalyzedResourceRequestTypeDef" = dataclasses.field()

    analyzerArn = field("analyzerArn")
    resourceArn = field("resourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAnalyzedResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnalyzedResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnalyzerRequest:
    boto3_raw_data: "type_defs.GetAnalyzerRequestTypeDef" = dataclasses.field()

    analyzerName = field("analyzerName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAnalyzerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnalyzerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetArchiveRuleRequest:
    boto3_raw_data: "type_defs.GetArchiveRuleRequestTypeDef" = dataclasses.field()

    analyzerName = field("analyzerName")
    ruleName = field("ruleName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetArchiveRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetArchiveRuleRequestTypeDef"]
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
class GetFindingRecommendationRequest:
    boto3_raw_data: "type_defs.GetFindingRecommendationRequestTypeDef" = (
        dataclasses.field()
    )

    analyzerArn = field("analyzerArn")
    id = field("id")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetFindingRecommendationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingRecommendationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationError:
    boto3_raw_data: "type_defs.RecommendationErrorTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendationErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingRequest:
    boto3_raw_data: "type_defs.GetFindingRequestTypeDef" = dataclasses.field()

    analyzerArn = field("analyzerArn")
    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFindingRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingV2Request:
    boto3_raw_data: "type_defs.GetFindingV2RequestTypeDef" = dataclasses.field()

    analyzerArn = field("analyzerArn")
    id = field("id")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFindingV2RequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingV2RequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingsStatisticsRequest:
    boto3_raw_data: "type_defs.GetFindingsStatisticsRequestTypeDef" = (
        dataclasses.field()
    )

    analyzerArn = field("analyzerArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFindingsStatisticsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingsStatisticsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGeneratedPolicyRequest:
    boto3_raw_data: "type_defs.GetGeneratedPolicyRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")
    includeResourcePlaceholders = field("includeResourcePlaceholders")
    includeServiceLevelTemplate = field("includeServiceLevelTemplate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGeneratedPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGeneratedPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InternalAccessAnalysisRuleCriteriaOutput:
    boto3_raw_data: "type_defs.InternalAccessAnalysisRuleCriteriaOutputTypeDef" = (
        dataclasses.field()
    )

    accountIds = field("accountIds")
    resourceTypes = field("resourceTypes")
    resourceArns = field("resourceArns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InternalAccessAnalysisRuleCriteriaOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InternalAccessAnalysisRuleCriteriaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InternalAccessAnalysisRuleCriteria:
    boto3_raw_data: "type_defs.InternalAccessAnalysisRuleCriteriaTypeDef" = (
        dataclasses.field()
    )

    accountIds = field("accountIds")
    resourceTypes = field("resourceTypes")
    resourceArns = field("resourceArns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InternalAccessAnalysisRuleCriteriaTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InternalAccessAnalysisRuleCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InternalAccessResourceTypeDetails:
    boto3_raw_data: "type_defs.InternalAccessResourceTypeDetailsTypeDef" = (
        dataclasses.field()
    )

    totalActiveFindings = field("totalActiveFindings")
    totalResolvedFindings = field("totalResolvedFindings")
    totalArchivedFindings = field("totalArchivedFindings")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InternalAccessResourceTypeDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InternalAccessResourceTypeDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobError:
    boto3_raw_data: "type_defs.JobErrorTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobErrorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KmsGrantConstraintsOutput:
    boto3_raw_data: "type_defs.KmsGrantConstraintsOutputTypeDef" = dataclasses.field()

    encryptionContextEquals = field("encryptionContextEquals")
    encryptionContextSubset = field("encryptionContextSubset")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KmsGrantConstraintsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KmsGrantConstraintsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KmsGrantConstraints:
    boto3_raw_data: "type_defs.KmsGrantConstraintsTypeDef" = dataclasses.field()

    encryptionContextEquals = field("encryptionContextEquals")
    encryptionContextSubset = field("encryptionContextSubset")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KmsGrantConstraintsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KmsGrantConstraintsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessPreviewsRequest:
    boto3_raw_data: "type_defs.ListAccessPreviewsRequestTypeDef" = dataclasses.field()

    analyzerArn = field("analyzerArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccessPreviewsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessPreviewsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnalyzedResourcesRequest:
    boto3_raw_data: "type_defs.ListAnalyzedResourcesRequestTypeDef" = (
        dataclasses.field()
    )

    analyzerArn = field("analyzerArn")
    resourceType = field("resourceType")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAnalyzedResourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnalyzedResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnalyzersRequest:
    boto3_raw_data: "type_defs.ListAnalyzersRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAnalyzersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnalyzersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListArchiveRulesRequest:
    boto3_raw_data: "type_defs.ListArchiveRulesRequestTypeDef" = dataclasses.field()

    analyzerName = field("analyzerName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListArchiveRulesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListArchiveRulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SortCriteria:
    boto3_raw_data: "type_defs.SortCriteriaTypeDef" = dataclasses.field()

    attributeName = field("attributeName")
    orderBy = field("orderBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SortCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SortCriteriaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyGenerationsRequest:
    boto3_raw_data: "type_defs.ListPolicyGenerationsRequestTypeDef" = (
        dataclasses.field()
    )

    principalArn = field("principalArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPolicyGenerationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyGenerationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyGeneration:
    boto3_raw_data: "type_defs.PolicyGenerationTypeDef" = dataclasses.field()

    jobId = field("jobId")
    principalArn = field("principalArn")
    status = field("status")
    startedOn = field("startedOn")
    completedOn = field("completedOn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyGenerationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyGenerationTypeDef"]
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
class VpcConfiguration:
    boto3_raw_data: "type_defs.VpcConfigurationTypeDef" = dataclasses.field()

    vpcId = field("vpcId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Substring:
    boto3_raw_data: "type_defs.SubstringTypeDef" = dataclasses.field()

    start = field("start")
    length = field("length")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubstringTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubstringTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyGenerationDetails:
    boto3_raw_data: "type_defs.PolicyGenerationDetailsTypeDef" = dataclasses.field()

    principalArn = field("principalArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyGenerationDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyGenerationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Position:
    boto3_raw_data: "type_defs.PositionTypeDef" = dataclasses.field()

    line = field("line")
    column = field("column")
    offset = field("offset")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PositionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PositionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsDbClusterSnapshotAttributeValueOutput:
    boto3_raw_data: "type_defs.RdsDbClusterSnapshotAttributeValueOutputTypeDef" = (
        dataclasses.field()
    )

    accountIds = field("accountIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RdsDbClusterSnapshotAttributeValueOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsDbClusterSnapshotAttributeValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsDbClusterSnapshotAttributeValue:
    boto3_raw_data: "type_defs.RdsDbClusterSnapshotAttributeValueTypeDef" = (
        dataclasses.field()
    )

    accountIds = field("accountIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RdsDbClusterSnapshotAttributeValueTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsDbClusterSnapshotAttributeValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsDbSnapshotAttributeValueOutput:
    boto3_raw_data: "type_defs.RdsDbSnapshotAttributeValueOutputTypeDef" = (
        dataclasses.field()
    )

    accountIds = field("accountIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RdsDbSnapshotAttributeValueOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsDbSnapshotAttributeValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsDbSnapshotAttributeValue:
    boto3_raw_data: "type_defs.RdsDbSnapshotAttributeValueTypeDef" = dataclasses.field()

    accountIds = field("accountIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RdsDbSnapshotAttributeValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsDbSnapshotAttributeValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnusedPermissionsRecommendedStep:
    boto3_raw_data: "type_defs.UnusedPermissionsRecommendedStepTypeDef" = (
        dataclasses.field()
    )

    recommendedAction = field("recommendedAction")
    policyUpdatedAt = field("policyUpdatedAt")
    recommendedPolicy = field("recommendedPolicy")
    existingPolicyId = field("existingPolicyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UnusedPermissionsRecommendedStepTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnusedPermissionsRecommendedStepTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3PublicAccessBlockConfiguration:
    boto3_raw_data: "type_defs.S3PublicAccessBlockConfigurationTypeDef" = (
        dataclasses.field()
    )

    ignorePublicAcls = field("ignorePublicAcls")
    restrictPublicBuckets = field("restrictPublicBuckets")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3PublicAccessBlockConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3PublicAccessBlockConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartResourceScanRequest:
    boto3_raw_data: "type_defs.StartResourceScanRequestTypeDef" = dataclasses.field()

    analyzerArn = field("analyzerArn")
    resourceArn = field("resourceArn")
    resourceOwnerAccount = field("resourceOwnerAccount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartResourceScanRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartResourceScanRequestTypeDef"]
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
class UnusedAccessTypeStatistics:
    boto3_raw_data: "type_defs.UnusedAccessTypeStatisticsTypeDef" = dataclasses.field()

    unusedAccessType = field("unusedAccessType")
    total = field("total")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnusedAccessTypeStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnusedAccessTypeStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnusedAction:
    boto3_raw_data: "type_defs.UnusedActionTypeDef" = dataclasses.field()

    action = field("action")
    lastAccessed = field("lastAccessed")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UnusedActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UnusedActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFindingsRequest:
    boto3_raw_data: "type_defs.UpdateFindingsRequestTypeDef" = dataclasses.field()

    analyzerArn = field("analyzerArn")
    status = field("status")
    ids = field("ids")
    resourceArn = field("resourceArn")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFindingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFindingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidatePolicyRequest:
    boto3_raw_data: "type_defs.ValidatePolicyRequestTypeDef" = dataclasses.field()

    policyDocument = field("policyDocument")
    policyType = field("policyType")
    locale = field("locale")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    validatePolicyResourceType = field("validatePolicyResourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValidatePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidatePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessPreviewSummary:
    boto3_raw_data: "type_defs.AccessPreviewSummaryTypeDef" = dataclasses.field()

    id = field("id")
    analyzerArn = field("analyzerArn")
    createdAt = field("createdAt")
    status = field("status")

    @cached_property
    def statusReason(self):  # pragma: no cover
        return AccessPreviewStatusReason.make_one(self.boto3_raw_data["statusReason"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessPreviewSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessPreviewSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckAccessNotGrantedRequest:
    boto3_raw_data: "type_defs.CheckAccessNotGrantedRequestTypeDef" = (
        dataclasses.field()
    )

    policyDocument = field("policyDocument")

    @cached_property
    def access(self):  # pragma: no cover
        return Access.make_many(self.boto3_raw_data["access"])

    policyType = field("policyType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CheckAccessNotGrantedRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckAccessNotGrantedRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3BucketAclGrantConfiguration:
    boto3_raw_data: "type_defs.S3BucketAclGrantConfigurationTypeDef" = (
        dataclasses.field()
    )

    permission = field("permission")

    @cached_property
    def grantee(self):  # pragma: no cover
        return AclGrantee.make_one(self.boto3_raw_data["grantee"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3BucketAclGrantConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3BucketAclGrantConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisRuleOutput:
    boto3_raw_data: "type_defs.AnalysisRuleOutputTypeDef" = dataclasses.field()

    @cached_property
    def exclusions(self):  # pragma: no cover
        return AnalysisRuleCriteriaOutput.make_many(self.boto3_raw_data["exclusions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalysisRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisRule:
    boto3_raw_data: "type_defs.AnalysisRuleTypeDef" = dataclasses.field()

    @cached_property
    def exclusions(self):  # pragma: no cover
        return AnalysisRuleCriteria.make_many(self.boto3_raw_data["exclusions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalysisRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnalysisRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveRuleSummary:
    boto3_raw_data: "type_defs.ArchiveRuleSummaryTypeDef" = dataclasses.field()

    ruleName = field("ruleName")
    filter = field("filter")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ArchiveRuleSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchiveRuleSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckAccessNotGrantedResponse:
    boto3_raw_data: "type_defs.CheckAccessNotGrantedResponseTypeDef" = (
        dataclasses.field()
    )

    result = field("result")
    message = field("message")

    @cached_property
    def reasons(self):  # pragma: no cover
        return ReasonSummary.make_many(self.boto3_raw_data["reasons"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CheckAccessNotGrantedResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckAccessNotGrantedResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckNoNewAccessResponse:
    boto3_raw_data: "type_defs.CheckNoNewAccessResponseTypeDef" = dataclasses.field()

    result = field("result")
    message = field("message")

    @cached_property
    def reasons(self):  # pragma: no cover
        return ReasonSummary.make_many(self.boto3_raw_data["reasons"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CheckNoNewAccessResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckNoNewAccessResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckNoPublicAccessResponse:
    boto3_raw_data: "type_defs.CheckNoPublicAccessResponseTypeDef" = dataclasses.field()

    result = field("result")
    message = field("message")

    @cached_property
    def reasons(self):  # pragma: no cover
        return ReasonSummary.make_many(self.boto3_raw_data["reasons"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CheckNoPublicAccessResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckNoPublicAccessResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessPreviewResponse:
    boto3_raw_data: "type_defs.CreateAccessPreviewResponseTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccessPreviewResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessPreviewResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAnalyzerResponse:
    boto3_raw_data: "type_defs.CreateAnalyzerResponseTypeDef" = dataclasses.field()

    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAnalyzerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAnalyzerResponseTypeDef"]
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
class GetAnalyzedResourceResponse:
    boto3_raw_data: "type_defs.GetAnalyzedResourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def resource(self):  # pragma: no cover
        return AnalyzedResource.make_one(self.boto3_raw_data["resource"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAnalyzedResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnalyzedResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnalyzedResourcesResponse:
    boto3_raw_data: "type_defs.ListAnalyzedResourcesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def analyzedResources(self):  # pragma: no cover
        return AnalyzedResourceSummary.make_many(
            self.boto3_raw_data["analyzedResources"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAnalyzedResourcesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnalyzedResourcesResponseTypeDef"]
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
class StartPolicyGenerationResponse:
    boto3_raw_data: "type_defs.StartPolicyGenerationResponseTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartPolicyGenerationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartPolicyGenerationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudTrailDetails:
    boto3_raw_data: "type_defs.CloudTrailDetailsTypeDef" = dataclasses.field()

    @cached_property
    def trails(self):  # pragma: no cover
        return Trail.make_many(self.boto3_raw_data["trails"])

    accessRole = field("accessRole")
    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CloudTrailDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudTrailDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudTrailProperties:
    boto3_raw_data: "type_defs.CloudTrailPropertiesTypeDef" = dataclasses.field()

    @cached_property
    def trailProperties(self):  # pragma: no cover
        return TrailProperties.make_many(self.boto3_raw_data["trailProperties"])

    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudTrailPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudTrailPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalAccessFindingsStatistics:
    boto3_raw_data: "type_defs.ExternalAccessFindingsStatisticsTypeDef" = (
        dataclasses.field()
    )

    resourceTypeStatistics = field("resourceTypeStatistics")
    totalActiveFindings = field("totalActiveFindings")
    totalArchivedFindings = field("totalArchivedFindings")
    totalResolvedFindings = field("totalResolvedFindings")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExternalAccessFindingsStatisticsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExternalAccessFindingsStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingSource:
    boto3_raw_data: "type_defs.FindingSourceTypeDef" = dataclasses.field()

    type = field("type")

    @cached_property
    def detail(self):  # pragma: no cover
        return FindingSourceDetail.make_one(self.boto3_raw_data["detail"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FindingSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FindingSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFindingsV2Response:
    boto3_raw_data: "type_defs.ListFindingsV2ResponseTypeDef" = dataclasses.field()

    @cached_property
    def findings(self):  # pragma: no cover
        return FindingSummaryV2.make_many(self.boto3_raw_data["findings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFindingsV2ResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingsV2ResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingRecommendationRequestPaginate:
    boto3_raw_data: "type_defs.GetFindingRecommendationRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    analyzerArn = field("analyzerArn")
    id = field("id")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFindingRecommendationRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingRecommendationRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingV2RequestPaginate:
    boto3_raw_data: "type_defs.GetFindingV2RequestPaginateTypeDef" = dataclasses.field()

    analyzerArn = field("analyzerArn")
    id = field("id")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFindingV2RequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingV2RequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessPreviewsRequestPaginate:
    boto3_raw_data: "type_defs.ListAccessPreviewsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    analyzerArn = field("analyzerArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccessPreviewsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessPreviewsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnalyzedResourcesRequestPaginate:
    boto3_raw_data: "type_defs.ListAnalyzedResourcesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    analyzerArn = field("analyzerArn")
    resourceType = field("resourceType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAnalyzedResourcesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnalyzedResourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnalyzersRequestPaginate:
    boto3_raw_data: "type_defs.ListAnalyzersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAnalyzersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnalyzersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListArchiveRulesRequestPaginate:
    boto3_raw_data: "type_defs.ListArchiveRulesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    analyzerName = field("analyzerName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListArchiveRulesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListArchiveRulesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyGenerationsRequestPaginate:
    boto3_raw_data: "type_defs.ListPolicyGenerationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    principalArn = field("principalArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPolicyGenerationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyGenerationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidatePolicyRequestPaginate:
    boto3_raw_data: "type_defs.ValidatePolicyRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    policyDocument = field("policyDocument")
    policyType = field("policyType")
    locale = field("locale")
    validatePolicyResourceType = field("validatePolicyResourceType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ValidatePolicyRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidatePolicyRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InternalAccessAnalysisRuleOutput:
    boto3_raw_data: "type_defs.InternalAccessAnalysisRuleOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def inclusions(self):  # pragma: no cover
        return InternalAccessAnalysisRuleCriteriaOutput.make_many(
            self.boto3_raw_data["inclusions"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InternalAccessAnalysisRuleOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InternalAccessAnalysisRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InternalAccessAnalysisRule:
    boto3_raw_data: "type_defs.InternalAccessAnalysisRuleTypeDef" = dataclasses.field()

    @cached_property
    def inclusions(self):  # pragma: no cover
        return InternalAccessAnalysisRuleCriteria.make_many(
            self.boto3_raw_data["inclusions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InternalAccessAnalysisRuleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InternalAccessAnalysisRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InternalAccessFindingsStatistics:
    boto3_raw_data: "type_defs.InternalAccessFindingsStatisticsTypeDef" = (
        dataclasses.field()
    )

    resourceTypeStatistics = field("resourceTypeStatistics")
    totalActiveFindings = field("totalActiveFindings")
    totalArchivedFindings = field("totalArchivedFindings")
    totalResolvedFindings = field("totalResolvedFindings")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InternalAccessFindingsStatisticsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InternalAccessFindingsStatisticsTypeDef"]
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

    jobId = field("jobId")
    status = field("status")
    startedOn = field("startedOn")
    completedOn = field("completedOn")

    @cached_property
    def jobError(self):  # pragma: no cover
        return JobError.make_one(self.boto3_raw_data["jobError"])

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
class KmsGrantConfigurationOutput:
    boto3_raw_data: "type_defs.KmsGrantConfigurationOutputTypeDef" = dataclasses.field()

    operations = field("operations")
    granteePrincipal = field("granteePrincipal")
    issuingAccount = field("issuingAccount")
    retiringPrincipal = field("retiringPrincipal")

    @cached_property
    def constraints(self):  # pragma: no cover
        return KmsGrantConstraintsOutput.make_one(self.boto3_raw_data["constraints"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KmsGrantConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KmsGrantConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyGenerationsResponse:
    boto3_raw_data: "type_defs.ListPolicyGenerationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def policyGenerations(self):  # pragma: no cover
        return PolicyGeneration.make_many(self.boto3_raw_data["policyGenerations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPolicyGenerationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyGenerationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkOriginConfigurationOutput:
    boto3_raw_data: "type_defs.NetworkOriginConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def vpcConfiguration(self):  # pragma: no cover
        return VpcConfiguration.make_one(self.boto3_raw_data["vpcConfiguration"])

    internetConfiguration = field("internetConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.NetworkOriginConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkOriginConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkOriginConfiguration:
    boto3_raw_data: "type_defs.NetworkOriginConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def vpcConfiguration(self):  # pragma: no cover
        return VpcConfiguration.make_one(self.boto3_raw_data["vpcConfiguration"])

    internetConfiguration = field("internetConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkOriginConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkOriginConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PathElement:
    boto3_raw_data: "type_defs.PathElementTypeDef" = dataclasses.field()

    index = field("index")
    key = field("key")

    @cached_property
    def substring(self):  # pragma: no cover
        return Substring.make_one(self.boto3_raw_data["substring"])

    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PathElementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PathElementTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Span:
    boto3_raw_data: "type_defs.SpanTypeDef" = dataclasses.field()

    @cached_property
    def start(self):  # pragma: no cover
        return Position.make_one(self.boto3_raw_data["start"])

    @cached_property
    def end(self):  # pragma: no cover
        return Position.make_one(self.boto3_raw_data["end"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SpanTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SpanTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsDbClusterSnapshotConfigurationOutput:
    boto3_raw_data: "type_defs.RdsDbClusterSnapshotConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    attributes = field("attributes")
    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RdsDbClusterSnapshotConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsDbClusterSnapshotConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsDbSnapshotConfigurationOutput:
    boto3_raw_data: "type_defs.RdsDbSnapshotConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    attributes = field("attributes")
    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RdsDbSnapshotConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsDbSnapshotConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendedStep:
    boto3_raw_data: "type_defs.RecommendedStepTypeDef" = dataclasses.field()

    @cached_property
    def unusedPermissionsRecommendedStep(self):  # pragma: no cover
        return UnusedPermissionsRecommendedStep.make_one(
            self.boto3_raw_data["unusedPermissionsRecommendedStep"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecommendedStepTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecommendedStepTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnusedAccessFindingsStatistics:
    boto3_raw_data: "type_defs.UnusedAccessFindingsStatisticsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def unusedAccessTypeStatistics(self):  # pragma: no cover
        return UnusedAccessTypeStatistics.make_many(
            self.boto3_raw_data["unusedAccessTypeStatistics"]
        )

    @cached_property
    def topAccounts(self):  # pragma: no cover
        return FindingAggregationAccountDetails.make_many(
            self.boto3_raw_data["topAccounts"]
        )

    totalActiveFindings = field("totalActiveFindings")
    totalArchivedFindings = field("totalArchivedFindings")
    totalResolvedFindings = field("totalResolvedFindings")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UnusedAccessFindingsStatisticsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnusedAccessFindingsStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnusedPermissionDetails:
    boto3_raw_data: "type_defs.UnusedPermissionDetailsTypeDef" = dataclasses.field()

    serviceNamespace = field("serviceNamespace")

    @cached_property
    def actions(self):  # pragma: no cover
        return UnusedAction.make_many(self.boto3_raw_data["actions"])

    lastAccessed = field("lastAccessed")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnusedPermissionDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnusedPermissionDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessPreviewsResponse:
    boto3_raw_data: "type_defs.ListAccessPreviewsResponseTypeDef" = dataclasses.field()

    @cached_property
    def accessPreviews(self):  # pragma: no cover
        return AccessPreviewSummary.make_many(self.boto3_raw_data["accessPreviews"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccessPreviewsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessPreviewsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnusedAccessConfigurationOutput:
    boto3_raw_data: "type_defs.UnusedAccessConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    unusedAccessAge = field("unusedAccessAge")

    @cached_property
    def analysisRule(self):  # pragma: no cover
        return AnalysisRuleOutput.make_one(self.boto3_raw_data["analysisRule"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UnusedAccessConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnusedAccessConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnusedAccessConfiguration:
    boto3_raw_data: "type_defs.UnusedAccessConfigurationTypeDef" = dataclasses.field()

    unusedAccessAge = field("unusedAccessAge")

    @cached_property
    def analysisRule(self):  # pragma: no cover
        return AnalysisRule.make_one(self.boto3_raw_data["analysisRule"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnusedAccessConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnusedAccessConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetArchiveRuleResponse:
    boto3_raw_data: "type_defs.GetArchiveRuleResponseTypeDef" = dataclasses.field()

    @cached_property
    def archiveRule(self):  # pragma: no cover
        return ArchiveRuleSummary.make_one(self.boto3_raw_data["archiveRule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetArchiveRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetArchiveRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListArchiveRulesResponse:
    boto3_raw_data: "type_defs.ListArchiveRulesResponseTypeDef" = dataclasses.field()

    @cached_property
    def archiveRules(self):  # pragma: no cover
        return ArchiveRuleSummary.make_many(self.boto3_raw_data["archiveRules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListArchiveRulesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListArchiveRulesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartPolicyGenerationRequest:
    boto3_raw_data: "type_defs.StartPolicyGenerationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def policyGenerationDetails(self):  # pragma: no cover
        return PolicyGenerationDetails.make_one(
            self.boto3_raw_data["policyGenerationDetails"]
        )

    @cached_property
    def cloudTrailDetails(self):  # pragma: no cover
        return CloudTrailDetails.make_one(self.boto3_raw_data["cloudTrailDetails"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartPolicyGenerationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartPolicyGenerationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeneratedPolicyProperties:
    boto3_raw_data: "type_defs.GeneratedPolicyPropertiesTypeDef" = dataclasses.field()

    principalArn = field("principalArn")
    isComplete = field("isComplete")

    @cached_property
    def cloudTrailProperties(self):  # pragma: no cover
        return CloudTrailProperties.make_one(
            self.boto3_raw_data["cloudTrailProperties"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GeneratedPolicyPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeneratedPolicyPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateArchiveRuleRequest:
    boto3_raw_data: "type_defs.CreateArchiveRuleRequestTypeDef" = dataclasses.field()

    analyzerName = field("analyzerName")
    ruleName = field("ruleName")
    filter = field("filter")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateArchiveRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateArchiveRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InlineArchiveRule:
    boto3_raw_data: "type_defs.InlineArchiveRuleTypeDef" = dataclasses.field()

    ruleName = field("ruleName")
    filter = field("filter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InlineArchiveRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InlineArchiveRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessPreviewFindingsRequestPaginate:
    boto3_raw_data: "type_defs.ListAccessPreviewFindingsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    accessPreviewId = field("accessPreviewId")
    analyzerArn = field("analyzerArn")
    filter = field("filter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccessPreviewFindingsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessPreviewFindingsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessPreviewFindingsRequest:
    boto3_raw_data: "type_defs.ListAccessPreviewFindingsRequestTypeDef" = (
        dataclasses.field()
    )

    accessPreviewId = field("accessPreviewId")
    analyzerArn = field("analyzerArn")
    filter = field("filter")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccessPreviewFindingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessPreviewFindingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFindingsRequestPaginate:
    boto3_raw_data: "type_defs.ListFindingsRequestPaginateTypeDef" = dataclasses.field()

    analyzerArn = field("analyzerArn")
    filter = field("filter")

    @cached_property
    def sort(self):  # pragma: no cover
        return SortCriteria.make_one(self.boto3_raw_data["sort"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFindingsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFindingsRequest:
    boto3_raw_data: "type_defs.ListFindingsRequestTypeDef" = dataclasses.field()

    analyzerArn = field("analyzerArn")
    filter = field("filter")

    @cached_property
    def sort(self):  # pragma: no cover
        return SortCriteria.make_one(self.boto3_raw_data["sort"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFindingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFindingsV2RequestPaginate:
    boto3_raw_data: "type_defs.ListFindingsV2RequestPaginateTypeDef" = (
        dataclasses.field()
    )

    analyzerArn = field("analyzerArn")
    filter = field("filter")

    @cached_property
    def sort(self):  # pragma: no cover
        return SortCriteria.make_one(self.boto3_raw_data["sort"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFindingsV2RequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingsV2RequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFindingsV2Request:
    boto3_raw_data: "type_defs.ListFindingsV2RequestTypeDef" = dataclasses.field()

    analyzerArn = field("analyzerArn")
    filter = field("filter")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def sort(self):  # pragma: no cover
        return SortCriteria.make_one(self.boto3_raw_data["sort"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFindingsV2RequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingsV2RequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateArchiveRuleRequest:
    boto3_raw_data: "type_defs.UpdateArchiveRuleRequestTypeDef" = dataclasses.field()

    analyzerName = field("analyzerName")
    ruleName = field("ruleName")
    filter = field("filter")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateArchiveRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateArchiveRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessPreviewFinding:
    boto3_raw_data: "type_defs.AccessPreviewFindingTypeDef" = dataclasses.field()

    id = field("id")
    resourceType = field("resourceType")
    createdAt = field("createdAt")
    changeType = field("changeType")
    status = field("status")
    resourceOwnerAccount = field("resourceOwnerAccount")
    existingFindingId = field("existingFindingId")
    existingFindingStatus = field("existingFindingStatus")
    principal = field("principal")
    action = field("action")
    condition = field("condition")
    resource = field("resource")
    isPublic = field("isPublic")
    error = field("error")

    @cached_property
    def sources(self):  # pragma: no cover
        return FindingSource.make_many(self.boto3_raw_data["sources"])

    resourceControlPolicyRestriction = field("resourceControlPolicyRestriction")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessPreviewFindingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessPreviewFindingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalAccessDetails:
    boto3_raw_data: "type_defs.ExternalAccessDetailsTypeDef" = dataclasses.field()

    condition = field("condition")
    action = field("action")
    isPublic = field("isPublic")
    principal = field("principal")

    @cached_property
    def sources(self):  # pragma: no cover
        return FindingSource.make_many(self.boto3_raw_data["sources"])

    resourceControlPolicyRestriction = field("resourceControlPolicyRestriction")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExternalAccessDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExternalAccessDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingSummary:
    boto3_raw_data: "type_defs.FindingSummaryTypeDef" = dataclasses.field()

    id = field("id")
    resourceType = field("resourceType")
    condition = field("condition")
    createdAt = field("createdAt")
    analyzedAt = field("analyzedAt")
    updatedAt = field("updatedAt")
    status = field("status")
    resourceOwnerAccount = field("resourceOwnerAccount")
    principal = field("principal")
    action = field("action")
    resource = field("resource")
    isPublic = field("isPublic")
    error = field("error")

    @cached_property
    def sources(self):  # pragma: no cover
        return FindingSource.make_many(self.boto3_raw_data["sources"])

    resourceControlPolicyRestriction = field("resourceControlPolicyRestriction")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FindingSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FindingSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Finding:
    boto3_raw_data: "type_defs.FindingTypeDef" = dataclasses.field()

    id = field("id")
    resourceType = field("resourceType")
    condition = field("condition")
    createdAt = field("createdAt")
    analyzedAt = field("analyzedAt")
    updatedAt = field("updatedAt")
    status = field("status")
    resourceOwnerAccount = field("resourceOwnerAccount")
    principal = field("principal")
    action = field("action")
    resource = field("resource")
    isPublic = field("isPublic")
    error = field("error")

    @cached_property
    def sources(self):  # pragma: no cover
        return FindingSource.make_many(self.boto3_raw_data["sources"])

    resourceControlPolicyRestriction = field("resourceControlPolicyRestriction")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FindingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FindingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InternalAccessDetails:
    boto3_raw_data: "type_defs.InternalAccessDetailsTypeDef" = dataclasses.field()

    action = field("action")
    condition = field("condition")
    principal = field("principal")
    principalOwnerAccount = field("principalOwnerAccount")
    accessType = field("accessType")
    principalType = field("principalType")

    @cached_property
    def sources(self):  # pragma: no cover
        return FindingSource.make_many(self.boto3_raw_data["sources"])

    resourceControlPolicyRestriction = field("resourceControlPolicyRestriction")
    serviceControlPolicyRestriction = field("serviceControlPolicyRestriction")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InternalAccessDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InternalAccessDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InternalAccessConfigurationOutput:
    boto3_raw_data: "type_defs.InternalAccessConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def analysisRule(self):  # pragma: no cover
        return InternalAccessAnalysisRuleOutput.make_one(
            self.boto3_raw_data["analysisRule"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InternalAccessConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InternalAccessConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InternalAccessConfiguration:
    boto3_raw_data: "type_defs.InternalAccessConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def analysisRule(self):  # pragma: no cover
        return InternalAccessAnalysisRule.make_one(self.boto3_raw_data["analysisRule"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InternalAccessConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InternalAccessConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KmsKeyConfigurationOutput:
    boto3_raw_data: "type_defs.KmsKeyConfigurationOutputTypeDef" = dataclasses.field()

    keyPolicies = field("keyPolicies")

    @cached_property
    def grants(self):  # pragma: no cover
        return KmsGrantConfigurationOutput.make_many(self.boto3_raw_data["grants"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KmsKeyConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KmsKeyConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KmsGrantConfiguration:
    boto3_raw_data: "type_defs.KmsGrantConfigurationTypeDef" = dataclasses.field()

    operations = field("operations")
    granteePrincipal = field("granteePrincipal")
    issuingAccount = field("issuingAccount")
    retiringPrincipal = field("retiringPrincipal")
    constraints = field("constraints")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KmsGrantConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KmsGrantConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3AccessPointConfigurationOutput:
    boto3_raw_data: "type_defs.S3AccessPointConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    accessPointPolicy = field("accessPointPolicy")

    @cached_property
    def publicAccessBlock(self):  # pragma: no cover
        return S3PublicAccessBlockConfiguration.make_one(
            self.boto3_raw_data["publicAccessBlock"]
        )

    @cached_property
    def networkOrigin(self):  # pragma: no cover
        return NetworkOriginConfigurationOutput.make_one(
            self.boto3_raw_data["networkOrigin"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3AccessPointConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3AccessPointConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ExpressDirectoryAccessPointConfigurationOutput:
    boto3_raw_data: (
        "type_defs.S3ExpressDirectoryAccessPointConfigurationOutputTypeDef"
    ) = dataclasses.field()

    accessPointPolicy = field("accessPointPolicy")

    @cached_property
    def networkOrigin(self):  # pragma: no cover
        return NetworkOriginConfigurationOutput.make_one(
            self.boto3_raw_data["networkOrigin"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.S3ExpressDirectoryAccessPointConfigurationOutputTypeDef"
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
                "type_defs.S3ExpressDirectoryAccessPointConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Location:
    boto3_raw_data: "type_defs.LocationTypeDef" = dataclasses.field()

    @cached_property
    def path(self):  # pragma: no cover
        return PathElement.make_many(self.boto3_raw_data["path"])

    @cached_property
    def span(self):  # pragma: no cover
        return Span.make_one(self.boto3_raw_data["span"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LocationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsDbClusterSnapshotConfiguration:
    boto3_raw_data: "type_defs.RdsDbClusterSnapshotConfigurationTypeDef" = (
        dataclasses.field()
    )

    attributes = field("attributes")
    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RdsDbClusterSnapshotConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsDbClusterSnapshotConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsDbSnapshotConfiguration:
    boto3_raw_data: "type_defs.RdsDbSnapshotConfigurationTypeDef" = dataclasses.field()

    attributes = field("attributes")
    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RdsDbSnapshotConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsDbSnapshotConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingRecommendationResponse:
    boto3_raw_data: "type_defs.GetFindingRecommendationResponseTypeDef" = (
        dataclasses.field()
    )

    startedAt = field("startedAt")
    completedAt = field("completedAt")

    @cached_property
    def error(self):  # pragma: no cover
        return RecommendationError.make_one(self.boto3_raw_data["error"])

    resourceArn = field("resourceArn")

    @cached_property
    def recommendedSteps(self):  # pragma: no cover
        return RecommendedStep.make_many(self.boto3_raw_data["recommendedSteps"])

    recommendationType = field("recommendationType")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetFindingRecommendationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingRecommendationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingsStatistics:
    boto3_raw_data: "type_defs.FindingsStatisticsTypeDef" = dataclasses.field()

    @cached_property
    def externalAccessFindingsStatistics(self):  # pragma: no cover
        return ExternalAccessFindingsStatistics.make_one(
            self.boto3_raw_data["externalAccessFindingsStatistics"]
        )

    @cached_property
    def internalAccessFindingsStatistics(self):  # pragma: no cover
        return InternalAccessFindingsStatistics.make_one(
            self.boto3_raw_data["internalAccessFindingsStatistics"]
        )

    @cached_property
    def unusedAccessFindingsStatistics(self):  # pragma: no cover
        return UnusedAccessFindingsStatistics.make_one(
            self.boto3_raw_data["unusedAccessFindingsStatistics"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FindingsStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FindingsStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeneratedPolicyResult:
    boto3_raw_data: "type_defs.GeneratedPolicyResultTypeDef" = dataclasses.field()

    @cached_property
    def properties(self):  # pragma: no cover
        return GeneratedPolicyProperties.make_one(self.boto3_raw_data["properties"])

    @cached_property
    def generatedPolicies(self):  # pragma: no cover
        return GeneratedPolicy.make_many(self.boto3_raw_data["generatedPolicies"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GeneratedPolicyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeneratedPolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessPreviewFindingsResponse:
    boto3_raw_data: "type_defs.ListAccessPreviewFindingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def findings(self):  # pragma: no cover
        return AccessPreviewFinding.make_many(self.boto3_raw_data["findings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccessPreviewFindingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessPreviewFindingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFindingsResponse:
    boto3_raw_data: "type_defs.ListFindingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def findings(self):  # pragma: no cover
        return FindingSummary.make_many(self.boto3_raw_data["findings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFindingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingResponse:
    boto3_raw_data: "type_defs.GetFindingResponseTypeDef" = dataclasses.field()

    @cached_property
    def finding(self):  # pragma: no cover
        return Finding.make_one(self.boto3_raw_data["finding"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFindingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingDetails:
    boto3_raw_data: "type_defs.FindingDetailsTypeDef" = dataclasses.field()

    @cached_property
    def internalAccessDetails(self):  # pragma: no cover
        return InternalAccessDetails.make_one(
            self.boto3_raw_data["internalAccessDetails"]
        )

    @cached_property
    def externalAccessDetails(self):  # pragma: no cover
        return ExternalAccessDetails.make_one(
            self.boto3_raw_data["externalAccessDetails"]
        )

    @cached_property
    def unusedPermissionDetails(self):  # pragma: no cover
        return UnusedPermissionDetails.make_one(
            self.boto3_raw_data["unusedPermissionDetails"]
        )

    @cached_property
    def unusedIamUserAccessKeyDetails(self):  # pragma: no cover
        return UnusedIamUserAccessKeyDetails.make_one(
            self.boto3_raw_data["unusedIamUserAccessKeyDetails"]
        )

    @cached_property
    def unusedIamRoleDetails(self):  # pragma: no cover
        return UnusedIamRoleDetails.make_one(
            self.boto3_raw_data["unusedIamRoleDetails"]
        )

    @cached_property
    def unusedIamUserPasswordDetails(self):  # pragma: no cover
        return UnusedIamUserPasswordDetails.make_one(
            self.boto3_raw_data["unusedIamUserPasswordDetails"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FindingDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FindingDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyzerConfigurationOutput:
    boto3_raw_data: "type_defs.AnalyzerConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def unusedAccess(self):  # pragma: no cover
        return UnusedAccessConfigurationOutput.make_one(
            self.boto3_raw_data["unusedAccess"]
        )

    @cached_property
    def internalAccess(self):  # pragma: no cover
        return InternalAccessConfigurationOutput.make_one(
            self.boto3_raw_data["internalAccess"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyzerConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyzerConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyzerConfiguration:
    boto3_raw_data: "type_defs.AnalyzerConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def unusedAccess(self):  # pragma: no cover
        return UnusedAccessConfiguration.make_one(self.boto3_raw_data["unusedAccess"])

    @cached_property
    def internalAccess(self):  # pragma: no cover
        return InternalAccessConfiguration.make_one(
            self.boto3_raw_data["internalAccess"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyzerConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyzerConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3BucketConfigurationOutput:
    boto3_raw_data: "type_defs.S3BucketConfigurationOutputTypeDef" = dataclasses.field()

    bucketPolicy = field("bucketPolicy")

    @cached_property
    def bucketAclGrants(self):  # pragma: no cover
        return S3BucketAclGrantConfiguration.make_many(
            self.boto3_raw_data["bucketAclGrants"]
        )

    @cached_property
    def bucketPublicAccessBlock(self):  # pragma: no cover
        return S3PublicAccessBlockConfiguration.make_one(
            self.boto3_raw_data["bucketPublicAccessBlock"]
        )

    accessPoints = field("accessPoints")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3BucketConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3BucketConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ExpressDirectoryBucketConfigurationOutput:
    boto3_raw_data: "type_defs.S3ExpressDirectoryBucketConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    bucketPolicy = field("bucketPolicy")
    accessPoints = field("accessPoints")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.S3ExpressDirectoryBucketConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ExpressDirectoryBucketConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3AccessPointConfiguration:
    boto3_raw_data: "type_defs.S3AccessPointConfigurationTypeDef" = dataclasses.field()

    accessPointPolicy = field("accessPointPolicy")

    @cached_property
    def publicAccessBlock(self):  # pragma: no cover
        return S3PublicAccessBlockConfiguration.make_one(
            self.boto3_raw_data["publicAccessBlock"]
        )

    networkOrigin = field("networkOrigin")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3AccessPointConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3AccessPointConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ExpressDirectoryAccessPointConfiguration:
    boto3_raw_data: "type_defs.S3ExpressDirectoryAccessPointConfigurationTypeDef" = (
        dataclasses.field()
    )

    accessPointPolicy = field("accessPointPolicy")
    networkOrigin = field("networkOrigin")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.S3ExpressDirectoryAccessPointConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ExpressDirectoryAccessPointConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidatePolicyFinding:
    boto3_raw_data: "type_defs.ValidatePolicyFindingTypeDef" = dataclasses.field()

    findingDetails = field("findingDetails")
    findingType = field("findingType")
    issueCode = field("issueCode")
    learnMoreLink = field("learnMoreLink")

    @cached_property
    def locations(self):  # pragma: no cover
        return Location.make_many(self.boto3_raw_data["locations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValidatePolicyFindingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidatePolicyFindingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingsStatisticsResponse:
    boto3_raw_data: "type_defs.GetFindingsStatisticsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def findingsStatistics(self):  # pragma: no cover
        return FindingsStatistics.make_many(self.boto3_raw_data["findingsStatistics"])

    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetFindingsStatisticsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingsStatisticsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGeneratedPolicyResponse:
    boto3_raw_data: "type_defs.GetGeneratedPolicyResponseTypeDef" = dataclasses.field()

    @cached_property
    def jobDetails(self):  # pragma: no cover
        return JobDetails.make_one(self.boto3_raw_data["jobDetails"])

    @cached_property
    def generatedPolicyResult(self):  # pragma: no cover
        return GeneratedPolicyResult.make_one(
            self.boto3_raw_data["generatedPolicyResult"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGeneratedPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGeneratedPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingV2Response:
    boto3_raw_data: "type_defs.GetFindingV2ResponseTypeDef" = dataclasses.field()

    analyzedAt = field("analyzedAt")
    createdAt = field("createdAt")
    error = field("error")
    id = field("id")
    resource = field("resource")
    resourceType = field("resourceType")
    resourceOwnerAccount = field("resourceOwnerAccount")
    status = field("status")
    updatedAt = field("updatedAt")

    @cached_property
    def findingDetails(self):  # pragma: no cover
        return FindingDetails.make_many(self.boto3_raw_data["findingDetails"])

    findingType = field("findingType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFindingV2ResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingV2ResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyzerSummary:
    boto3_raw_data: "type_defs.AnalyzerSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    type = field("type")
    createdAt = field("createdAt")
    status = field("status")
    lastResourceAnalyzed = field("lastResourceAnalyzed")
    lastResourceAnalyzedAt = field("lastResourceAnalyzedAt")
    tags = field("tags")

    @cached_property
    def statusReason(self):  # pragma: no cover
        return StatusReason.make_one(self.boto3_raw_data["statusReason"])

    @cached_property
    def configuration(self):  # pragma: no cover
        return AnalyzerConfigurationOutput.make_one(
            self.boto3_raw_data["configuration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalyzerSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnalyzerSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAnalyzerResponse:
    boto3_raw_data: "type_defs.UpdateAnalyzerResponseTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return AnalyzerConfigurationOutput.make_one(
            self.boto3_raw_data["configuration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAnalyzerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAnalyzerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KmsKeyConfiguration:
    boto3_raw_data: "type_defs.KmsKeyConfigurationTypeDef" = dataclasses.field()

    keyPolicies = field("keyPolicies")
    grants = field("grants")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KmsKeyConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KmsKeyConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationOutput:
    boto3_raw_data: "type_defs.ConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def ebsSnapshot(self):  # pragma: no cover
        return EbsSnapshotConfigurationOutput.make_one(
            self.boto3_raw_data["ebsSnapshot"]
        )

    @cached_property
    def ecrRepository(self):  # pragma: no cover
        return EcrRepositoryConfiguration.make_one(self.boto3_raw_data["ecrRepository"])

    @cached_property
    def iamRole(self):  # pragma: no cover
        return IamRoleConfiguration.make_one(self.boto3_raw_data["iamRole"])

    @cached_property
    def efsFileSystem(self):  # pragma: no cover
        return EfsFileSystemConfiguration.make_one(self.boto3_raw_data["efsFileSystem"])

    @cached_property
    def kmsKey(self):  # pragma: no cover
        return KmsKeyConfigurationOutput.make_one(self.boto3_raw_data["kmsKey"])

    @cached_property
    def rdsDbClusterSnapshot(self):  # pragma: no cover
        return RdsDbClusterSnapshotConfigurationOutput.make_one(
            self.boto3_raw_data["rdsDbClusterSnapshot"]
        )

    @cached_property
    def rdsDbSnapshot(self):  # pragma: no cover
        return RdsDbSnapshotConfigurationOutput.make_one(
            self.boto3_raw_data["rdsDbSnapshot"]
        )

    @cached_property
    def secretsManagerSecret(self):  # pragma: no cover
        return SecretsManagerSecretConfiguration.make_one(
            self.boto3_raw_data["secretsManagerSecret"]
        )

    @cached_property
    def s3Bucket(self):  # pragma: no cover
        return S3BucketConfigurationOutput.make_one(self.boto3_raw_data["s3Bucket"])

    @cached_property
    def snsTopic(self):  # pragma: no cover
        return SnsTopicConfiguration.make_one(self.boto3_raw_data["snsTopic"])

    @cached_property
    def sqsQueue(self):  # pragma: no cover
        return SqsQueueConfiguration.make_one(self.boto3_raw_data["sqsQueue"])

    @cached_property
    def s3ExpressDirectoryBucket(self):  # pragma: no cover
        return S3ExpressDirectoryBucketConfigurationOutput.make_one(
            self.boto3_raw_data["s3ExpressDirectoryBucket"]
        )

    @cached_property
    def dynamodbStream(self):  # pragma: no cover
        return DynamodbStreamConfiguration.make_one(
            self.boto3_raw_data["dynamodbStream"]
        )

    @cached_property
    def dynamodbTable(self):  # pragma: no cover
        return DynamodbTableConfiguration.make_one(self.boto3_raw_data["dynamodbTable"])

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
class ValidatePolicyResponse:
    boto3_raw_data: "type_defs.ValidatePolicyResponseTypeDef" = dataclasses.field()

    @cached_property
    def findings(self):  # pragma: no cover
        return ValidatePolicyFinding.make_many(self.boto3_raw_data["findings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValidatePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidatePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnalyzerResponse:
    boto3_raw_data: "type_defs.GetAnalyzerResponseTypeDef" = dataclasses.field()

    @cached_property
    def analyzer(self):  # pragma: no cover
        return AnalyzerSummary.make_one(self.boto3_raw_data["analyzer"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAnalyzerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnalyzerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnalyzersResponse:
    boto3_raw_data: "type_defs.ListAnalyzersResponseTypeDef" = dataclasses.field()

    @cached_property
    def analyzers(self):  # pragma: no cover
        return AnalyzerSummary.make_many(self.boto3_raw_data["analyzers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAnalyzersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnalyzersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAnalyzerRequest:
    boto3_raw_data: "type_defs.CreateAnalyzerRequestTypeDef" = dataclasses.field()

    analyzerName = field("analyzerName")
    type = field("type")

    @cached_property
    def archiveRules(self):  # pragma: no cover
        return InlineArchiveRule.make_many(self.boto3_raw_data["archiveRules"])

    tags = field("tags")
    clientToken = field("clientToken")
    configuration = field("configuration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAnalyzerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAnalyzerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAnalyzerRequest:
    boto3_raw_data: "type_defs.UpdateAnalyzerRequestTypeDef" = dataclasses.field()

    analyzerName = field("analyzerName")
    configuration = field("configuration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAnalyzerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAnalyzerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessPreview:
    boto3_raw_data: "type_defs.AccessPreviewTypeDef" = dataclasses.field()

    id = field("id")
    analyzerArn = field("analyzerArn")
    configurations = field("configurations")
    createdAt = field("createdAt")
    status = field("status")

    @cached_property
    def statusReason(self):  # pragma: no cover
        return AccessPreviewStatusReason.make_one(self.boto3_raw_data["statusReason"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessPreviewTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccessPreviewTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3BucketConfiguration:
    boto3_raw_data: "type_defs.S3BucketConfigurationTypeDef" = dataclasses.field()

    bucketPolicy = field("bucketPolicy")

    @cached_property
    def bucketAclGrants(self):  # pragma: no cover
        return S3BucketAclGrantConfiguration.make_many(
            self.boto3_raw_data["bucketAclGrants"]
        )

    @cached_property
    def bucketPublicAccessBlock(self):  # pragma: no cover
        return S3PublicAccessBlockConfiguration.make_one(
            self.boto3_raw_data["bucketPublicAccessBlock"]
        )

    accessPoints = field("accessPoints")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3BucketConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3BucketConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ExpressDirectoryBucketConfiguration:
    boto3_raw_data: "type_defs.S3ExpressDirectoryBucketConfigurationTypeDef" = (
        dataclasses.field()
    )

    bucketPolicy = field("bucketPolicy")
    accessPoints = field("accessPoints")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.S3ExpressDirectoryBucketConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ExpressDirectoryBucketConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessPreviewResponse:
    boto3_raw_data: "type_defs.GetAccessPreviewResponseTypeDef" = dataclasses.field()

    @cached_property
    def accessPreview(self):  # pragma: no cover
        return AccessPreview.make_one(self.boto3_raw_data["accessPreview"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccessPreviewResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessPreviewResponseTypeDef"]
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

    ebsSnapshot = field("ebsSnapshot")

    @cached_property
    def ecrRepository(self):  # pragma: no cover
        return EcrRepositoryConfiguration.make_one(self.boto3_raw_data["ecrRepository"])

    @cached_property
    def iamRole(self):  # pragma: no cover
        return IamRoleConfiguration.make_one(self.boto3_raw_data["iamRole"])

    @cached_property
    def efsFileSystem(self):  # pragma: no cover
        return EfsFileSystemConfiguration.make_one(self.boto3_raw_data["efsFileSystem"])

    kmsKey = field("kmsKey")
    rdsDbClusterSnapshot = field("rdsDbClusterSnapshot")
    rdsDbSnapshot = field("rdsDbSnapshot")

    @cached_property
    def secretsManagerSecret(self):  # pragma: no cover
        return SecretsManagerSecretConfiguration.make_one(
            self.boto3_raw_data["secretsManagerSecret"]
        )

    s3Bucket = field("s3Bucket")

    @cached_property
    def snsTopic(self):  # pragma: no cover
        return SnsTopicConfiguration.make_one(self.boto3_raw_data["snsTopic"])

    @cached_property
    def sqsQueue(self):  # pragma: no cover
        return SqsQueueConfiguration.make_one(self.boto3_raw_data["sqsQueue"])

    s3ExpressDirectoryBucket = field("s3ExpressDirectoryBucket")

    @cached_property
    def dynamodbStream(self):  # pragma: no cover
        return DynamodbStreamConfiguration.make_one(
            self.boto3_raw_data["dynamodbStream"]
        )

    @cached_property
    def dynamodbTable(self):  # pragma: no cover
        return DynamodbTableConfiguration.make_one(self.boto3_raw_data["dynamodbTable"])

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
class CreateAccessPreviewRequest:
    boto3_raw_data: "type_defs.CreateAccessPreviewRequestTypeDef" = dataclasses.field()

    analyzerArn = field("analyzerArn")
    configurations = field("configurations")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccessPreviewRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessPreviewRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
