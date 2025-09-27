# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_codecommit import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ApprovalRuleEventMetadata:
    boto3_raw_data: "type_defs.ApprovalRuleEventMetadataTypeDef" = dataclasses.field()

    approvalRuleName = field("approvalRuleName")
    approvalRuleId = field("approvalRuleId")
    approvalRuleContent = field("approvalRuleContent")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApprovalRuleEventMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApprovalRuleEventMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApprovalRuleOverriddenEventMetadata:
    boto3_raw_data: "type_defs.ApprovalRuleOverriddenEventMetadataTypeDef" = (
        dataclasses.field()
    )

    revisionId = field("revisionId")
    overrideStatus = field("overrideStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApprovalRuleOverriddenEventMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApprovalRuleOverriddenEventMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApprovalRuleTemplate:
    boto3_raw_data: "type_defs.ApprovalRuleTemplateTypeDef" = dataclasses.field()

    approvalRuleTemplateId = field("approvalRuleTemplateId")
    approvalRuleTemplateName = field("approvalRuleTemplateName")
    approvalRuleTemplateDescription = field("approvalRuleTemplateDescription")
    approvalRuleTemplateContent = field("approvalRuleTemplateContent")
    ruleContentSha256 = field("ruleContentSha256")
    lastModifiedDate = field("lastModifiedDate")
    creationDate = field("creationDate")
    lastModifiedUser = field("lastModifiedUser")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApprovalRuleTemplateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApprovalRuleTemplateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginApprovalRuleTemplate:
    boto3_raw_data: "type_defs.OriginApprovalRuleTemplateTypeDef" = dataclasses.field()

    approvalRuleTemplateId = field("approvalRuleTemplateId")
    approvalRuleTemplateName = field("approvalRuleTemplateName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OriginApprovalRuleTemplateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginApprovalRuleTemplateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApprovalStateChangedEventMetadata:
    boto3_raw_data: "type_defs.ApprovalStateChangedEventMetadataTypeDef" = (
        dataclasses.field()
    )

    revisionId = field("revisionId")
    approvalStatus = field("approvalStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApprovalStateChangedEventMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApprovalStateChangedEventMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Approval:
    boto3_raw_data: "type_defs.ApprovalTypeDef" = dataclasses.field()

    userArn = field("userArn")
    approvalState = field("approvalState")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApprovalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApprovalTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateApprovalRuleTemplateWithRepositoryInput:
    boto3_raw_data: (
        "type_defs.AssociateApprovalRuleTemplateWithRepositoryInputTypeDef"
    ) = dataclasses.field()

    approvalRuleTemplateName = field("approvalRuleTemplateName")
    repositoryName = field("repositoryName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateApprovalRuleTemplateWithRepositoryInputTypeDef"
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
                "type_defs.AssociateApprovalRuleTemplateWithRepositoryInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAssociateApprovalRuleTemplateWithRepositoriesError:
    boto3_raw_data: (
        "type_defs.BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef"
    ) = dataclasses.field()

    repositoryName = field("repositoryName")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef"
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
                "type_defs.BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAssociateApprovalRuleTemplateWithRepositoriesInput:
    boto3_raw_data: (
        "type_defs.BatchAssociateApprovalRuleTemplateWithRepositoriesInputTypeDef"
    ) = dataclasses.field()

    approvalRuleTemplateName = field("approvalRuleTemplateName")
    repositoryNames = field("repositoryNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchAssociateApprovalRuleTemplateWithRepositoriesInputTypeDef"
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
                "type_defs.BatchAssociateApprovalRuleTemplateWithRepositoriesInputTypeDef"
            ]
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
class BatchDescribeMergeConflictsError:
    boto3_raw_data: "type_defs.BatchDescribeMergeConflictsErrorTypeDef" = (
        dataclasses.field()
    )

    filePath = field("filePath")
    exceptionName = field("exceptionName")
    message = field("message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchDescribeMergeConflictsErrorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDescribeMergeConflictsErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDescribeMergeConflictsInput:
    boto3_raw_data: "type_defs.BatchDescribeMergeConflictsInputTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    destinationCommitSpecifier = field("destinationCommitSpecifier")
    sourceCommitSpecifier = field("sourceCommitSpecifier")
    mergeOption = field("mergeOption")
    maxMergeHunks = field("maxMergeHunks")
    maxConflictFiles = field("maxConflictFiles")
    filePaths = field("filePaths")
    conflictDetailLevel = field("conflictDetailLevel")
    conflictResolutionStrategy = field("conflictResolutionStrategy")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchDescribeMergeConflictsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDescribeMergeConflictsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisassociateApprovalRuleTemplateFromRepositoriesError:
    boto3_raw_data: (
        "type_defs.BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef"
    ) = dataclasses.field()

    repositoryName = field("repositoryName")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef"
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
                "type_defs.BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisassociateApprovalRuleTemplateFromRepositoriesInput:
    boto3_raw_data: (
        "type_defs.BatchDisassociateApprovalRuleTemplateFromRepositoriesInputTypeDef"
    ) = dataclasses.field()

    approvalRuleTemplateName = field("approvalRuleTemplateName")
    repositoryNames = field("repositoryNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDisassociateApprovalRuleTemplateFromRepositoriesInputTypeDef"
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
                "type_defs.BatchDisassociateApprovalRuleTemplateFromRepositoriesInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetCommitsError:
    boto3_raw_data: "type_defs.BatchGetCommitsErrorTypeDef" = dataclasses.field()

    commitId = field("commitId")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetCommitsErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetCommitsErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetCommitsInput:
    boto3_raw_data: "type_defs.BatchGetCommitsInputTypeDef" = dataclasses.field()

    commitIds = field("commitIds")
    repositoryName = field("repositoryName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetCommitsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetCommitsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetRepositoriesError:
    boto3_raw_data: "type_defs.BatchGetRepositoriesErrorTypeDef" = dataclasses.field()

    repositoryId = field("repositoryId")
    repositoryName = field("repositoryName")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetRepositoriesErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetRepositoriesErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetRepositoriesInput:
    boto3_raw_data: "type_defs.BatchGetRepositoriesInputTypeDef" = dataclasses.field()

    repositoryNames = field("repositoryNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetRepositoriesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetRepositoriesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositoryMetadata:
    boto3_raw_data: "type_defs.RepositoryMetadataTypeDef" = dataclasses.field()

    accountId = field("accountId")
    repositoryId = field("repositoryId")
    repositoryName = field("repositoryName")
    repositoryDescription = field("repositoryDescription")
    defaultBranch = field("defaultBranch")
    lastModifiedDate = field("lastModifiedDate")
    creationDate = field("creationDate")
    cloneUrlHttp = field("cloneUrlHttp")
    cloneUrlSsh = field("cloneUrlSsh")
    Arn = field("Arn")
    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RepositoryMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositoryMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlobMetadata:
    boto3_raw_data: "type_defs.BlobMetadataTypeDef" = dataclasses.field()

    blobId = field("blobId")
    path = field("path")
    mode = field("mode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BlobMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BlobMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BranchInfo:
    boto3_raw_data: "type_defs.BranchInfoTypeDef" = dataclasses.field()

    branchName = field("branchName")
    commitId = field("commitId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BranchInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BranchInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Comment:
    boto3_raw_data: "type_defs.CommentTypeDef" = dataclasses.field()

    commentId = field("commentId")
    content = field("content")
    inReplyTo = field("inReplyTo")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")
    authorArn = field("authorArn")
    deleted = field("deleted")
    clientRequestToken = field("clientRequestToken")
    callerReactions = field("callerReactions")
    reactionCounts = field("reactionCounts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CommentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CommentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Location:
    boto3_raw_data: "type_defs.LocationTypeDef" = dataclasses.field()

    filePath = field("filePath")
    filePosition = field("filePosition")
    relativeFileVersion = field("relativeFileVersion")

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
class UserInfo:
    boto3_raw_data: "type_defs.UserInfoTypeDef" = dataclasses.field()

    name = field("name")
    email = field("email")
    date = field("date")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileModes:
    boto3_raw_data: "type_defs.FileModesTypeDef" = dataclasses.field()

    source = field("source")
    destination = field("destination")
    base = field("base")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileModesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FileModesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileSizes:
    boto3_raw_data: "type_defs.FileSizesTypeDef" = dataclasses.field()

    source = field("source")
    destination = field("destination")
    base = field("base")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileSizesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FileSizesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsBinaryFile:
    boto3_raw_data: "type_defs.IsBinaryFileTypeDef" = dataclasses.field()

    source = field("source")
    destination = field("destination")
    base = field("base")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IsBinaryFileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IsBinaryFileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MergeOperations:
    boto3_raw_data: "type_defs.MergeOperationsTypeDef" = dataclasses.field()

    source = field("source")
    destination = field("destination")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MergeOperationsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MergeOperationsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectTypes:
    boto3_raw_data: "type_defs.ObjectTypesTypeDef" = dataclasses.field()

    source = field("source")
    destination = field("destination")
    base = field("base")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ObjectTypesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ObjectTypesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFileEntry:
    boto3_raw_data: "type_defs.DeleteFileEntryTypeDef" = dataclasses.field()

    filePath = field("filePath")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteFileEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteFileEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetFileModeEntry:
    boto3_raw_data: "type_defs.SetFileModeEntryTypeDef" = dataclasses.field()

    filePath = field("filePath")
    fileMode = field("fileMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SetFileModeEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetFileModeEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApprovalRuleTemplateInput:
    boto3_raw_data: "type_defs.CreateApprovalRuleTemplateInputTypeDef" = (
        dataclasses.field()
    )

    approvalRuleTemplateName = field("approvalRuleTemplateName")
    approvalRuleTemplateContent = field("approvalRuleTemplateContent")
    approvalRuleTemplateDescription = field("approvalRuleTemplateDescription")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateApprovalRuleTemplateInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApprovalRuleTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBranchInput:
    boto3_raw_data: "type_defs.CreateBranchInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    branchName = field("branchName")
    commitId = field("commitId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateBranchInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBranchInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileMetadata:
    boto3_raw_data: "type_defs.FileMetadataTypeDef" = dataclasses.field()

    absolutePath = field("absolutePath")
    blobId = field("blobId")
    fileMode = field("fileMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FileMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePullRequestApprovalRuleInput:
    boto3_raw_data: "type_defs.CreatePullRequestApprovalRuleInputTypeDef" = (
        dataclasses.field()
    )

    pullRequestId = field("pullRequestId")
    approvalRuleName = field("approvalRuleName")
    approvalRuleContent = field("approvalRuleContent")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePullRequestApprovalRuleInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePullRequestApprovalRuleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Target:
    boto3_raw_data: "type_defs.TargetTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    sourceReference = field("sourceReference")
    destinationReference = field("destinationReference")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRepositoryInput:
    boto3_raw_data: "type_defs.CreateRepositoryInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    repositoryDescription = field("repositoryDescription")
    tags = field("tags")
    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRepositoryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRepositoryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApprovalRuleTemplateInput:
    boto3_raw_data: "type_defs.DeleteApprovalRuleTemplateInputTypeDef" = (
        dataclasses.field()
    )

    approvalRuleTemplateName = field("approvalRuleTemplateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteApprovalRuleTemplateInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApprovalRuleTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBranchInput:
    boto3_raw_data: "type_defs.DeleteBranchInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    branchName = field("branchName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteBranchInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBranchInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCommentContentInput:
    boto3_raw_data: "type_defs.DeleteCommentContentInputTypeDef" = dataclasses.field()

    commentId = field("commentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCommentContentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCommentContentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFileInput:
    boto3_raw_data: "type_defs.DeleteFileInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    branchName = field("branchName")
    filePath = field("filePath")
    parentCommitId = field("parentCommitId")
    keepEmptyFolders = field("keepEmptyFolders")
    commitMessage = field("commitMessage")
    name = field("name")
    email = field("email")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteFileInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteFileInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePullRequestApprovalRuleInput:
    boto3_raw_data: "type_defs.DeletePullRequestApprovalRuleInputTypeDef" = (
        dataclasses.field()
    )

    pullRequestId = field("pullRequestId")
    approvalRuleName = field("approvalRuleName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeletePullRequestApprovalRuleInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePullRequestApprovalRuleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRepositoryInput:
    boto3_raw_data: "type_defs.DeleteRepositoryInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRepositoryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRepositoryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMergeConflictsInput:
    boto3_raw_data: "type_defs.DescribeMergeConflictsInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    destinationCommitSpecifier = field("destinationCommitSpecifier")
    sourceCommitSpecifier = field("sourceCommitSpecifier")
    mergeOption = field("mergeOption")
    filePath = field("filePath")
    maxMergeHunks = field("maxMergeHunks")
    conflictDetailLevel = field("conflictDetailLevel")
    conflictResolutionStrategy = field("conflictResolutionStrategy")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMergeConflictsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMergeConflictsInputTypeDef"]
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
class DescribePullRequestEventsInput:
    boto3_raw_data: "type_defs.DescribePullRequestEventsInputTypeDef" = (
        dataclasses.field()
    )

    pullRequestId = field("pullRequestId")
    pullRequestEventType = field("pullRequestEventType")
    actorArn = field("actorArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePullRequestEventsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePullRequestEventsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateApprovalRuleTemplateFromRepositoryInput:
    boto3_raw_data: (
        "type_defs.DisassociateApprovalRuleTemplateFromRepositoryInputTypeDef"
    ) = dataclasses.field()

    approvalRuleTemplateName = field("approvalRuleTemplateName")
    repositoryName = field("repositoryName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateApprovalRuleTemplateFromRepositoryInputTypeDef"
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
                "type_defs.DisassociateApprovalRuleTemplateFromRepositoryInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluatePullRequestApprovalRulesInput:
    boto3_raw_data: "type_defs.EvaluatePullRequestApprovalRulesInputTypeDef" = (
        dataclasses.field()
    )

    pullRequestId = field("pullRequestId")
    revisionId = field("revisionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EvaluatePullRequestApprovalRulesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluatePullRequestApprovalRulesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Evaluation:
    boto3_raw_data: "type_defs.EvaluationTypeDef" = dataclasses.field()

    approved = field("approved")
    overridden = field("overridden")
    approvalRulesSatisfied = field("approvalRulesSatisfied")
    approvalRulesNotSatisfied = field("approvalRulesNotSatisfied")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EvaluationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class File:
    boto3_raw_data: "type_defs.FileTypeDef" = dataclasses.field()

    blobId = field("blobId")
    absolutePath = field("absolutePath")
    relativePath = field("relativePath")
    fileMode = field("fileMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FileTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Folder:
    boto3_raw_data: "type_defs.FolderTypeDef" = dataclasses.field()

    treeId = field("treeId")
    absolutePath = field("absolutePath")
    relativePath = field("relativePath")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FolderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FolderTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApprovalRuleTemplateInput:
    boto3_raw_data: "type_defs.GetApprovalRuleTemplateInputTypeDef" = (
        dataclasses.field()
    )

    approvalRuleTemplateName = field("approvalRuleTemplateName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApprovalRuleTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApprovalRuleTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBlobInput:
    boto3_raw_data: "type_defs.GetBlobInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    blobId = field("blobId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetBlobInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetBlobInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBranchInput:
    boto3_raw_data: "type_defs.GetBranchInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    branchName = field("branchName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetBranchInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetBranchInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCommentInput:
    boto3_raw_data: "type_defs.GetCommentInputTypeDef" = dataclasses.field()

    commentId = field("commentId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetCommentInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetCommentInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCommentReactionsInput:
    boto3_raw_data: "type_defs.GetCommentReactionsInputTypeDef" = dataclasses.field()

    commentId = field("commentId")
    reactionUserArn = field("reactionUserArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCommentReactionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCommentReactionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCommentsForComparedCommitInput:
    boto3_raw_data: "type_defs.GetCommentsForComparedCommitInputTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    afterCommitId = field("afterCommitId")
    beforeCommitId = field("beforeCommitId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCommentsForComparedCommitInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCommentsForComparedCommitInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCommentsForPullRequestInput:
    boto3_raw_data: "type_defs.GetCommentsForPullRequestInputTypeDef" = (
        dataclasses.field()
    )

    pullRequestId = field("pullRequestId")
    repositoryName = field("repositoryName")
    beforeCommitId = field("beforeCommitId")
    afterCommitId = field("afterCommitId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCommentsForPullRequestInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCommentsForPullRequestInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCommitInput:
    boto3_raw_data: "type_defs.GetCommitInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    commitId = field("commitId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetCommitInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetCommitInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDifferencesInput:
    boto3_raw_data: "type_defs.GetDifferencesInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    afterCommitSpecifier = field("afterCommitSpecifier")
    beforeCommitSpecifier = field("beforeCommitSpecifier")
    beforePath = field("beforePath")
    afterPath = field("afterPath")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDifferencesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDifferencesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFileInput:
    boto3_raw_data: "type_defs.GetFileInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    filePath = field("filePath")
    commitSpecifier = field("commitSpecifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFileInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetFileInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFolderInput:
    boto3_raw_data: "type_defs.GetFolderInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    folderPath = field("folderPath")
    commitSpecifier = field("commitSpecifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFolderInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetFolderInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubModule:
    boto3_raw_data: "type_defs.SubModuleTypeDef" = dataclasses.field()

    commitId = field("commitId")
    absolutePath = field("absolutePath")
    relativePath = field("relativePath")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubModuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubModuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SymbolicLink:
    boto3_raw_data: "type_defs.SymbolicLinkTypeDef" = dataclasses.field()

    blobId = field("blobId")
    absolutePath = field("absolutePath")
    relativePath = field("relativePath")
    fileMode = field("fileMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SymbolicLinkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SymbolicLinkTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMergeCommitInput:
    boto3_raw_data: "type_defs.GetMergeCommitInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    sourceCommitSpecifier = field("sourceCommitSpecifier")
    destinationCommitSpecifier = field("destinationCommitSpecifier")
    conflictDetailLevel = field("conflictDetailLevel")
    conflictResolutionStrategy = field("conflictResolutionStrategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMergeCommitInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMergeCommitInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMergeConflictsInput:
    boto3_raw_data: "type_defs.GetMergeConflictsInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    destinationCommitSpecifier = field("destinationCommitSpecifier")
    sourceCommitSpecifier = field("sourceCommitSpecifier")
    mergeOption = field("mergeOption")
    conflictDetailLevel = field("conflictDetailLevel")
    maxConflictFiles = field("maxConflictFiles")
    conflictResolutionStrategy = field("conflictResolutionStrategy")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMergeConflictsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMergeConflictsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMergeOptionsInput:
    boto3_raw_data: "type_defs.GetMergeOptionsInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    sourceCommitSpecifier = field("sourceCommitSpecifier")
    destinationCommitSpecifier = field("destinationCommitSpecifier")
    conflictDetailLevel = field("conflictDetailLevel")
    conflictResolutionStrategy = field("conflictResolutionStrategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMergeOptionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMergeOptionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPullRequestApprovalStatesInput:
    boto3_raw_data: "type_defs.GetPullRequestApprovalStatesInputTypeDef" = (
        dataclasses.field()
    )

    pullRequestId = field("pullRequestId")
    revisionId = field("revisionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetPullRequestApprovalStatesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPullRequestApprovalStatesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPullRequestInput:
    boto3_raw_data: "type_defs.GetPullRequestInputTypeDef" = dataclasses.field()

    pullRequestId = field("pullRequestId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPullRequestInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPullRequestInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPullRequestOverrideStateInput:
    boto3_raw_data: "type_defs.GetPullRequestOverrideStateInputTypeDef" = (
        dataclasses.field()
    )

    pullRequestId = field("pullRequestId")
    revisionId = field("revisionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPullRequestOverrideStateInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPullRequestOverrideStateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRepositoryInput:
    boto3_raw_data: "type_defs.GetRepositoryInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRepositoryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRepositoryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRepositoryTriggersInput:
    boto3_raw_data: "type_defs.GetRepositoryTriggersInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRepositoryTriggersInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRepositoryTriggersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositoryTriggerOutput:
    boto3_raw_data: "type_defs.RepositoryTriggerOutputTypeDef" = dataclasses.field()

    name = field("name")
    destinationArn = field("destinationArn")
    events = field("events")
    customData = field("customData")
    branches = field("branches")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RepositoryTriggerOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositoryTriggerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApprovalRuleTemplatesInput:
    boto3_raw_data: "type_defs.ListApprovalRuleTemplatesInputTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApprovalRuleTemplatesInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApprovalRuleTemplatesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociatedApprovalRuleTemplatesForRepositoryInput:
    boto3_raw_data: (
        "type_defs.ListAssociatedApprovalRuleTemplatesForRepositoryInputTypeDef"
    ) = dataclasses.field()

    repositoryName = field("repositoryName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssociatedApprovalRuleTemplatesForRepositoryInputTypeDef"
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
                "type_defs.ListAssociatedApprovalRuleTemplatesForRepositoryInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBranchesInput:
    boto3_raw_data: "type_defs.ListBranchesInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListBranchesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBranchesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFileCommitHistoryRequest:
    boto3_raw_data: "type_defs.ListFileCommitHistoryRequestTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    filePath = field("filePath")
    commitSpecifier = field("commitSpecifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFileCommitHistoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFileCommitHistoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPullRequestsInput:
    boto3_raw_data: "type_defs.ListPullRequestsInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    authorArn = field("authorArn")
    pullRequestStatus = field("pullRequestStatus")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPullRequestsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPullRequestsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositoriesForApprovalRuleTemplateInput:
    boto3_raw_data: "type_defs.ListRepositoriesForApprovalRuleTemplateInputTypeDef" = (
        dataclasses.field()
    )

    approvalRuleTemplateName = field("approvalRuleTemplateName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRepositoriesForApprovalRuleTemplateInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositoriesForApprovalRuleTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositoriesInput:
    boto3_raw_data: "type_defs.ListRepositoriesInputTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    sortBy = field("sortBy")
    order = field("order")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRepositoriesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositoriesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositoryNameIdPair:
    boto3_raw_data: "type_defs.RepositoryNameIdPairTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    repositoryId = field("repositoryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RepositoryNameIdPairTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositoryNameIdPairTypeDef"]
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
class MergeBranchesByFastForwardInput:
    boto3_raw_data: "type_defs.MergeBranchesByFastForwardInputTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    sourceCommitSpecifier = field("sourceCommitSpecifier")
    destinationCommitSpecifier = field("destinationCommitSpecifier")
    targetBranch = field("targetBranch")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MergeBranchesByFastForwardInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MergeBranchesByFastForwardInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MergeHunkDetail:
    boto3_raw_data: "type_defs.MergeHunkDetailTypeDef" = dataclasses.field()

    startLine = field("startLine")
    endLine = field("endLine")
    hunkContent = field("hunkContent")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MergeHunkDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MergeHunkDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MergeMetadata:
    boto3_raw_data: "type_defs.MergeMetadataTypeDef" = dataclasses.field()

    isMerged = field("isMerged")
    mergedBy = field("mergedBy")
    mergeCommitId = field("mergeCommitId")
    mergeOption = field("mergeOption")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MergeMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MergeMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MergePullRequestByFastForwardInput:
    boto3_raw_data: "type_defs.MergePullRequestByFastForwardInputTypeDef" = (
        dataclasses.field()
    )

    pullRequestId = field("pullRequestId")
    repositoryName = field("repositoryName")
    sourceCommitId = field("sourceCommitId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MergePullRequestByFastForwardInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MergePullRequestByFastForwardInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OverridePullRequestApprovalRulesInput:
    boto3_raw_data: "type_defs.OverridePullRequestApprovalRulesInputTypeDef" = (
        dataclasses.field()
    )

    pullRequestId = field("pullRequestId")
    revisionId = field("revisionId")
    overrideStatus = field("overrideStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OverridePullRequestApprovalRulesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OverridePullRequestApprovalRulesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostCommentReplyInput:
    boto3_raw_data: "type_defs.PostCommentReplyInputTypeDef" = dataclasses.field()

    inReplyTo = field("inReplyTo")
    content = field("content")
    clientRequestToken = field("clientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PostCommentReplyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostCommentReplyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PullRequestCreatedEventMetadata:
    boto3_raw_data: "type_defs.PullRequestCreatedEventMetadataTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    sourceCommitId = field("sourceCommitId")
    destinationCommitId = field("destinationCommitId")
    mergeBase = field("mergeBase")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PullRequestCreatedEventMetadataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PullRequestCreatedEventMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PullRequestSourceReferenceUpdatedEventMetadata:
    boto3_raw_data: (
        "type_defs.PullRequestSourceReferenceUpdatedEventMetadataTypeDef"
    ) = dataclasses.field()

    repositoryName = field("repositoryName")
    beforeCommitId = field("beforeCommitId")
    afterCommitId = field("afterCommitId")
    mergeBase = field("mergeBase")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PullRequestSourceReferenceUpdatedEventMetadataTypeDef"
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
                "type_defs.PullRequestSourceReferenceUpdatedEventMetadataTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PullRequestStatusChangedEventMetadata:
    boto3_raw_data: "type_defs.PullRequestStatusChangedEventMetadataTypeDef" = (
        dataclasses.field()
    )

    pullRequestStatus = field("pullRequestStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PullRequestStatusChangedEventMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PullRequestStatusChangedEventMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutCommentReactionInput:
    boto3_raw_data: "type_defs.PutCommentReactionInputTypeDef" = dataclasses.field()

    commentId = field("commentId")
    reactionValue = field("reactionValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutCommentReactionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutCommentReactionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceFileSpecifier:
    boto3_raw_data: "type_defs.SourceFileSpecifierTypeDef" = dataclasses.field()

    filePath = field("filePath")
    isMove = field("isMove")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceFileSpecifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceFileSpecifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReactionValueFormats:
    boto3_raw_data: "type_defs.ReactionValueFormatsTypeDef" = dataclasses.field()

    emoji = field("emoji")
    shortCode = field("shortCode")
    unicode = field("unicode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReactionValueFormatsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReactionValueFormatsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositoryTriggerExecutionFailure:
    boto3_raw_data: "type_defs.RepositoryTriggerExecutionFailureTypeDef" = (
        dataclasses.field()
    )

    trigger = field("trigger")
    failureMessage = field("failureMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RepositoryTriggerExecutionFailureTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositoryTriggerExecutionFailureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositoryTrigger:
    boto3_raw_data: "type_defs.RepositoryTriggerTypeDef" = dataclasses.field()

    name = field("name")
    destinationArn = field("destinationArn")
    events = field("events")
    customData = field("customData")
    branches = field("branches")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RepositoryTriggerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositoryTriggerTypeDef"]
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
    tags = field("tags")

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
class UpdateApprovalRuleTemplateContentInput:
    boto3_raw_data: "type_defs.UpdateApprovalRuleTemplateContentInputTypeDef" = (
        dataclasses.field()
    )

    approvalRuleTemplateName = field("approvalRuleTemplateName")
    newRuleContent = field("newRuleContent")
    existingRuleContentSha256 = field("existingRuleContentSha256")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateApprovalRuleTemplateContentInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApprovalRuleTemplateContentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApprovalRuleTemplateDescriptionInput:
    boto3_raw_data: "type_defs.UpdateApprovalRuleTemplateDescriptionInputTypeDef" = (
        dataclasses.field()
    )

    approvalRuleTemplateName = field("approvalRuleTemplateName")
    approvalRuleTemplateDescription = field("approvalRuleTemplateDescription")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateApprovalRuleTemplateDescriptionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApprovalRuleTemplateDescriptionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApprovalRuleTemplateNameInput:
    boto3_raw_data: "type_defs.UpdateApprovalRuleTemplateNameInputTypeDef" = (
        dataclasses.field()
    )

    oldApprovalRuleTemplateName = field("oldApprovalRuleTemplateName")
    newApprovalRuleTemplateName = field("newApprovalRuleTemplateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateApprovalRuleTemplateNameInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApprovalRuleTemplateNameInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCommentInput:
    boto3_raw_data: "type_defs.UpdateCommentInputTypeDef" = dataclasses.field()

    commentId = field("commentId")
    content = field("content")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCommentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCommentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDefaultBranchInput:
    boto3_raw_data: "type_defs.UpdateDefaultBranchInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    defaultBranchName = field("defaultBranchName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDefaultBranchInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDefaultBranchInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePullRequestApprovalRuleContentInput:
    boto3_raw_data: "type_defs.UpdatePullRequestApprovalRuleContentInputTypeDef" = (
        dataclasses.field()
    )

    pullRequestId = field("pullRequestId")
    approvalRuleName = field("approvalRuleName")
    newRuleContent = field("newRuleContent")
    existingRuleContentSha256 = field("existingRuleContentSha256")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePullRequestApprovalRuleContentInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePullRequestApprovalRuleContentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePullRequestApprovalStateInput:
    boto3_raw_data: "type_defs.UpdatePullRequestApprovalStateInputTypeDef" = (
        dataclasses.field()
    )

    pullRequestId = field("pullRequestId")
    revisionId = field("revisionId")
    approvalState = field("approvalState")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePullRequestApprovalStateInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePullRequestApprovalStateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePullRequestDescriptionInput:
    boto3_raw_data: "type_defs.UpdatePullRequestDescriptionInputTypeDef" = (
        dataclasses.field()
    )

    pullRequestId = field("pullRequestId")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePullRequestDescriptionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePullRequestDescriptionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePullRequestStatusInput:
    boto3_raw_data: "type_defs.UpdatePullRequestStatusInputTypeDef" = (
        dataclasses.field()
    )

    pullRequestId = field("pullRequestId")
    pullRequestStatus = field("pullRequestStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePullRequestStatusInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePullRequestStatusInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePullRequestTitleInput:
    boto3_raw_data: "type_defs.UpdatePullRequestTitleInputTypeDef" = dataclasses.field()

    pullRequestId = field("pullRequestId")
    title = field("title")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePullRequestTitleInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePullRequestTitleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRepositoryDescriptionInput:
    boto3_raw_data: "type_defs.UpdateRepositoryDescriptionInputTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    repositoryDescription = field("repositoryDescription")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateRepositoryDescriptionInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRepositoryDescriptionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRepositoryEncryptionKeyInput:
    boto3_raw_data: "type_defs.UpdateRepositoryEncryptionKeyInputTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateRepositoryEncryptionKeyInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRepositoryEncryptionKeyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRepositoryNameInput:
    boto3_raw_data: "type_defs.UpdateRepositoryNameInputTypeDef" = dataclasses.field()

    oldName = field("oldName")
    newName = field("newName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRepositoryNameInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRepositoryNameInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApprovalRule:
    boto3_raw_data: "type_defs.ApprovalRuleTypeDef" = dataclasses.field()

    approvalRuleId = field("approvalRuleId")
    approvalRuleName = field("approvalRuleName")
    approvalRuleContent = field("approvalRuleContent")
    ruleContentSha256 = field("ruleContentSha256")
    lastModifiedDate = field("lastModifiedDate")
    creationDate = field("creationDate")
    lastModifiedUser = field("lastModifiedUser")

    @cached_property
    def originApprovalRuleTemplate(self):  # pragma: no cover
        return OriginApprovalRuleTemplate.make_one(
            self.boto3_raw_data["originApprovalRuleTemplate"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApprovalRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApprovalRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAssociateApprovalRuleTemplateWithRepositoriesOutput:
    boto3_raw_data: (
        "type_defs.BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef"
    ) = dataclasses.field()

    associatedRepositoryNames = field("associatedRepositoryNames")

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchAssociateApprovalRuleTemplateWithRepositoriesError.make_many(
            self.boto3_raw_data["errors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef"
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
                "type_defs.BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApprovalRuleTemplateOutput:
    boto3_raw_data: "type_defs.CreateApprovalRuleTemplateOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def approvalRuleTemplate(self):  # pragma: no cover
        return ApprovalRuleTemplate.make_one(
            self.boto3_raw_data["approvalRuleTemplate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateApprovalRuleTemplateOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApprovalRuleTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUnreferencedMergeCommitOutput:
    boto3_raw_data: "type_defs.CreateUnreferencedMergeCommitOutputTypeDef" = (
        dataclasses.field()
    )

    commitId = field("commitId")
    treeId = field("treeId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateUnreferencedMergeCommitOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUnreferencedMergeCommitOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApprovalRuleTemplateOutput:
    boto3_raw_data: "type_defs.DeleteApprovalRuleTemplateOutputTypeDef" = (
        dataclasses.field()
    )

    approvalRuleTemplateId = field("approvalRuleTemplateId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteApprovalRuleTemplateOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApprovalRuleTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFileOutput:
    boto3_raw_data: "type_defs.DeleteFileOutputTypeDef" = dataclasses.field()

    commitId = field("commitId")
    blobId = field("blobId")
    treeId = field("treeId")
    filePath = field("filePath")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteFileOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFileOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePullRequestApprovalRuleOutput:
    boto3_raw_data: "type_defs.DeletePullRequestApprovalRuleOutputTypeDef" = (
        dataclasses.field()
    )

    approvalRuleId = field("approvalRuleId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeletePullRequestApprovalRuleOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePullRequestApprovalRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRepositoryOutput:
    boto3_raw_data: "type_defs.DeleteRepositoryOutputTypeDef" = dataclasses.field()

    repositoryId = field("repositoryId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRepositoryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRepositoryOutputTypeDef"]
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
class GetApprovalRuleTemplateOutput:
    boto3_raw_data: "type_defs.GetApprovalRuleTemplateOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def approvalRuleTemplate(self):  # pragma: no cover
        return ApprovalRuleTemplate.make_one(
            self.boto3_raw_data["approvalRuleTemplate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetApprovalRuleTemplateOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApprovalRuleTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBlobOutput:
    boto3_raw_data: "type_defs.GetBlobOutputTypeDef" = dataclasses.field()

    content = field("content")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetBlobOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetBlobOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFileOutput:
    boto3_raw_data: "type_defs.GetFileOutputTypeDef" = dataclasses.field()

    commitId = field("commitId")
    blobId = field("blobId")
    filePath = field("filePath")
    fileMode = field("fileMode")
    fileSize = field("fileSize")
    fileContent = field("fileContent")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFileOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetFileOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMergeCommitOutput:
    boto3_raw_data: "type_defs.GetMergeCommitOutputTypeDef" = dataclasses.field()

    sourceCommitId = field("sourceCommitId")
    destinationCommitId = field("destinationCommitId")
    baseCommitId = field("baseCommitId")
    mergedCommitId = field("mergedCommitId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMergeCommitOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMergeCommitOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMergeOptionsOutput:
    boto3_raw_data: "type_defs.GetMergeOptionsOutputTypeDef" = dataclasses.field()

    mergeOptions = field("mergeOptions")
    sourceCommitId = field("sourceCommitId")
    destinationCommitId = field("destinationCommitId")
    baseCommitId = field("baseCommitId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMergeOptionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMergeOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPullRequestApprovalStatesOutput:
    boto3_raw_data: "type_defs.GetPullRequestApprovalStatesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def approvals(self):  # pragma: no cover
        return Approval.make_many(self.boto3_raw_data["approvals"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetPullRequestApprovalStatesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPullRequestApprovalStatesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPullRequestOverrideStateOutput:
    boto3_raw_data: "type_defs.GetPullRequestOverrideStateOutputTypeDef" = (
        dataclasses.field()
    )

    overridden = field("overridden")
    overrider = field("overrider")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetPullRequestOverrideStateOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPullRequestOverrideStateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApprovalRuleTemplatesOutput:
    boto3_raw_data: "type_defs.ListApprovalRuleTemplatesOutputTypeDef" = (
        dataclasses.field()
    )

    approvalRuleTemplateNames = field("approvalRuleTemplateNames")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApprovalRuleTemplatesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApprovalRuleTemplatesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociatedApprovalRuleTemplatesForRepositoryOutput:
    boto3_raw_data: (
        "type_defs.ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef"
    ) = dataclasses.field()

    approvalRuleTemplateNames = field("approvalRuleTemplateNames")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef"
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
                "type_defs.ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBranchesOutput:
    boto3_raw_data: "type_defs.ListBranchesOutputTypeDef" = dataclasses.field()

    branches = field("branches")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBranchesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBranchesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPullRequestsOutput:
    boto3_raw_data: "type_defs.ListPullRequestsOutputTypeDef" = dataclasses.field()

    pullRequestIds = field("pullRequestIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPullRequestsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPullRequestsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositoriesForApprovalRuleTemplateOutput:
    boto3_raw_data: "type_defs.ListRepositoriesForApprovalRuleTemplateOutputTypeDef" = (
        dataclasses.field()
    )

    repositoryNames = field("repositoryNames")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRepositoriesForApprovalRuleTemplateOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositoriesForApprovalRuleTemplateOutputTypeDef"]
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

    tags = field("tags")

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
class MergeBranchesByFastForwardOutput:
    boto3_raw_data: "type_defs.MergeBranchesByFastForwardOutputTypeDef" = (
        dataclasses.field()
    )

    commitId = field("commitId")
    treeId = field("treeId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MergeBranchesByFastForwardOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MergeBranchesByFastForwardOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MergeBranchesBySquashOutput:
    boto3_raw_data: "type_defs.MergeBranchesBySquashOutputTypeDef" = dataclasses.field()

    commitId = field("commitId")
    treeId = field("treeId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MergeBranchesBySquashOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MergeBranchesBySquashOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MergeBranchesByThreeWayOutput:
    boto3_raw_data: "type_defs.MergeBranchesByThreeWayOutputTypeDef" = (
        dataclasses.field()
    )

    commitId = field("commitId")
    treeId = field("treeId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MergeBranchesByThreeWayOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MergeBranchesByThreeWayOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutFileOutput:
    boto3_raw_data: "type_defs.PutFileOutputTypeDef" = dataclasses.field()

    commitId = field("commitId")
    blobId = field("blobId")
    treeId = field("treeId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutFileOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutFileOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRepositoryTriggersOutput:
    boto3_raw_data: "type_defs.PutRepositoryTriggersOutputTypeDef" = dataclasses.field()

    configurationId = field("configurationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutRepositoryTriggersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRepositoryTriggersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApprovalRuleTemplateContentOutput:
    boto3_raw_data: "type_defs.UpdateApprovalRuleTemplateContentOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def approvalRuleTemplate(self):  # pragma: no cover
        return ApprovalRuleTemplate.make_one(
            self.boto3_raw_data["approvalRuleTemplate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateApprovalRuleTemplateContentOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApprovalRuleTemplateContentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApprovalRuleTemplateDescriptionOutput:
    boto3_raw_data: "type_defs.UpdateApprovalRuleTemplateDescriptionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def approvalRuleTemplate(self):  # pragma: no cover
        return ApprovalRuleTemplate.make_one(
            self.boto3_raw_data["approvalRuleTemplate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateApprovalRuleTemplateDescriptionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApprovalRuleTemplateDescriptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApprovalRuleTemplateNameOutput:
    boto3_raw_data: "type_defs.UpdateApprovalRuleTemplateNameOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def approvalRuleTemplate(self):  # pragma: no cover
        return ApprovalRuleTemplate.make_one(
            self.boto3_raw_data["approvalRuleTemplate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateApprovalRuleTemplateNameOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApprovalRuleTemplateNameOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRepositoryEncryptionKeyOutput:
    boto3_raw_data: "type_defs.UpdateRepositoryEncryptionKeyOutputTypeDef" = (
        dataclasses.field()
    )

    repositoryId = field("repositoryId")
    kmsKeyId = field("kmsKeyId")
    originalKmsKeyId = field("originalKmsKeyId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateRepositoryEncryptionKeyOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRepositoryEncryptionKeyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput:
    boto3_raw_data: (
        "type_defs.BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef"
    ) = dataclasses.field()

    disassociatedRepositoryNames = field("disassociatedRepositoryNames")

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchDisassociateApprovalRuleTemplateFromRepositoriesError.make_many(
            self.boto3_raw_data["errors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef"
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
                "type_defs.BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetRepositoriesOutput:
    boto3_raw_data: "type_defs.BatchGetRepositoriesOutputTypeDef" = dataclasses.field()

    @cached_property
    def repositories(self):  # pragma: no cover
        return RepositoryMetadata.make_many(self.boto3_raw_data["repositories"])

    repositoriesNotFound = field("repositoriesNotFound")

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchGetRepositoriesError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetRepositoriesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetRepositoriesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRepositoryOutput:
    boto3_raw_data: "type_defs.CreateRepositoryOutputTypeDef" = dataclasses.field()

    @cached_property
    def repositoryMetadata(self):  # pragma: no cover
        return RepositoryMetadata.make_one(self.boto3_raw_data["repositoryMetadata"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRepositoryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRepositoryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRepositoryOutput:
    boto3_raw_data: "type_defs.GetRepositoryOutputTypeDef" = dataclasses.field()

    @cached_property
    def repositoryMetadata(self):  # pragma: no cover
        return RepositoryMetadata.make_one(self.boto3_raw_data["repositoryMetadata"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRepositoryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRepositoryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Difference:
    boto3_raw_data: "type_defs.DifferenceTypeDef" = dataclasses.field()

    @cached_property
    def beforeBlob(self):  # pragma: no cover
        return BlobMetadata.make_one(self.boto3_raw_data["beforeBlob"])

    @cached_property
    def afterBlob(self):  # pragma: no cover
        return BlobMetadata.make_one(self.boto3_raw_data["afterBlob"])

    changeType = field("changeType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DifferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DifferenceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutFileInput:
    boto3_raw_data: "type_defs.PutFileInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    branchName = field("branchName")
    fileContent = field("fileContent")
    filePath = field("filePath")
    fileMode = field("fileMode")
    parentCommitId = field("parentCommitId")
    commitMessage = field("commitMessage")
    name = field("name")
    email = field("email")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutFileInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutFileInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplaceContentEntry:
    boto3_raw_data: "type_defs.ReplaceContentEntryTypeDef" = dataclasses.field()

    filePath = field("filePath")
    replacementType = field("replacementType")
    content = field("content")
    fileMode = field("fileMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplaceContentEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplaceContentEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBranchOutput:
    boto3_raw_data: "type_defs.DeleteBranchOutputTypeDef" = dataclasses.field()

    @cached_property
    def deletedBranch(self):  # pragma: no cover
        return BranchInfo.make_one(self.boto3_raw_data["deletedBranch"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBranchOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBranchOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBranchOutput:
    boto3_raw_data: "type_defs.GetBranchOutputTypeDef" = dataclasses.field()

    @cached_property
    def branch(self):  # pragma: no cover
        return BranchInfo.make_one(self.boto3_raw_data["branch"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetBranchOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetBranchOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCommentContentOutput:
    boto3_raw_data: "type_defs.DeleteCommentContentOutputTypeDef" = dataclasses.field()

    @cached_property
    def comment(self):  # pragma: no cover
        return Comment.make_one(self.boto3_raw_data["comment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCommentContentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCommentContentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCommentOutput:
    boto3_raw_data: "type_defs.GetCommentOutputTypeDef" = dataclasses.field()

    @cached_property
    def comment(self):  # pragma: no cover
        return Comment.make_one(self.boto3_raw_data["comment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetCommentOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCommentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostCommentReplyOutput:
    boto3_raw_data: "type_defs.PostCommentReplyOutputTypeDef" = dataclasses.field()

    @cached_property
    def comment(self):  # pragma: no cover
        return Comment.make_one(self.boto3_raw_data["comment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PostCommentReplyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostCommentReplyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCommentOutput:
    boto3_raw_data: "type_defs.UpdateCommentOutputTypeDef" = dataclasses.field()

    @cached_property
    def comment(self):  # pragma: no cover
        return Comment.make_one(self.boto3_raw_data["comment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCommentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCommentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommentsForComparedCommit:
    boto3_raw_data: "type_defs.CommentsForComparedCommitTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    beforeCommitId = field("beforeCommitId")
    afterCommitId = field("afterCommitId")
    beforeBlobId = field("beforeBlobId")
    afterBlobId = field("afterBlobId")

    @cached_property
    def location(self):  # pragma: no cover
        return Location.make_one(self.boto3_raw_data["location"])

    @cached_property
    def comments(self):  # pragma: no cover
        return Comment.make_many(self.boto3_raw_data["comments"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommentsForComparedCommitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommentsForComparedCommitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommentsForPullRequest:
    boto3_raw_data: "type_defs.CommentsForPullRequestTypeDef" = dataclasses.field()

    pullRequestId = field("pullRequestId")
    repositoryName = field("repositoryName")
    beforeCommitId = field("beforeCommitId")
    afterCommitId = field("afterCommitId")
    beforeBlobId = field("beforeBlobId")
    afterBlobId = field("afterBlobId")

    @cached_property
    def location(self):  # pragma: no cover
        return Location.make_one(self.boto3_raw_data["location"])

    @cached_property
    def comments(self):  # pragma: no cover
        return Comment.make_many(self.boto3_raw_data["comments"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommentsForPullRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommentsForPullRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostCommentForComparedCommitInput:
    boto3_raw_data: "type_defs.PostCommentForComparedCommitInputTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    afterCommitId = field("afterCommitId")
    content = field("content")
    beforeCommitId = field("beforeCommitId")

    @cached_property
    def location(self):  # pragma: no cover
        return Location.make_one(self.boto3_raw_data["location"])

    clientRequestToken = field("clientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PostCommentForComparedCommitInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostCommentForComparedCommitInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostCommentForComparedCommitOutput:
    boto3_raw_data: "type_defs.PostCommentForComparedCommitOutputTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    beforeCommitId = field("beforeCommitId")
    afterCommitId = field("afterCommitId")
    beforeBlobId = field("beforeBlobId")
    afterBlobId = field("afterBlobId")

    @cached_property
    def location(self):  # pragma: no cover
        return Location.make_one(self.boto3_raw_data["location"])

    @cached_property
    def comment(self):  # pragma: no cover
        return Comment.make_one(self.boto3_raw_data["comment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PostCommentForComparedCommitOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostCommentForComparedCommitOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostCommentForPullRequestInput:
    boto3_raw_data: "type_defs.PostCommentForPullRequestInputTypeDef" = (
        dataclasses.field()
    )

    pullRequestId = field("pullRequestId")
    repositoryName = field("repositoryName")
    beforeCommitId = field("beforeCommitId")
    afterCommitId = field("afterCommitId")
    content = field("content")

    @cached_property
    def location(self):  # pragma: no cover
        return Location.make_one(self.boto3_raw_data["location"])

    clientRequestToken = field("clientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PostCommentForPullRequestInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostCommentForPullRequestInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostCommentForPullRequestOutput:
    boto3_raw_data: "type_defs.PostCommentForPullRequestOutputTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    pullRequestId = field("pullRequestId")
    beforeCommitId = field("beforeCommitId")
    afterCommitId = field("afterCommitId")
    beforeBlobId = field("beforeBlobId")
    afterBlobId = field("afterBlobId")

    @cached_property
    def location(self):  # pragma: no cover
        return Location.make_one(self.boto3_raw_data["location"])

    @cached_property
    def comment(self):  # pragma: no cover
        return Comment.make_one(self.boto3_raw_data["comment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PostCommentForPullRequestOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostCommentForPullRequestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Commit:
    boto3_raw_data: "type_defs.CommitTypeDef" = dataclasses.field()

    commitId = field("commitId")
    treeId = field("treeId")
    parents = field("parents")
    message = field("message")

    @cached_property
    def author(self):  # pragma: no cover
        return UserInfo.make_one(self.boto3_raw_data["author"])

    @cached_property
    def committer(self):  # pragma: no cover
        return UserInfo.make_one(self.boto3_raw_data["committer"])

    additionalData = field("additionalData")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CommitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CommitTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConflictMetadata:
    boto3_raw_data: "type_defs.ConflictMetadataTypeDef" = dataclasses.field()

    filePath = field("filePath")

    @cached_property
    def fileSizes(self):  # pragma: no cover
        return FileSizes.make_one(self.boto3_raw_data["fileSizes"])

    @cached_property
    def fileModes(self):  # pragma: no cover
        return FileModes.make_one(self.boto3_raw_data["fileModes"])

    @cached_property
    def objectTypes(self):  # pragma: no cover
        return ObjectTypes.make_one(self.boto3_raw_data["objectTypes"])

    numberOfConflicts = field("numberOfConflicts")

    @cached_property
    def isBinaryFile(self):  # pragma: no cover
        return IsBinaryFile.make_one(self.boto3_raw_data["isBinaryFile"])

    contentConflict = field("contentConflict")
    fileModeConflict = field("fileModeConflict")
    objectTypeConflict = field("objectTypeConflict")

    @cached_property
    def mergeOperations(self):  # pragma: no cover
        return MergeOperations.make_one(self.boto3_raw_data["mergeOperations"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConflictMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConflictMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCommitOutput:
    boto3_raw_data: "type_defs.CreateCommitOutputTypeDef" = dataclasses.field()

    commitId = field("commitId")
    treeId = field("treeId")

    @cached_property
    def filesAdded(self):  # pragma: no cover
        return FileMetadata.make_many(self.boto3_raw_data["filesAdded"])

    @cached_property
    def filesUpdated(self):  # pragma: no cover
        return FileMetadata.make_many(self.boto3_raw_data["filesUpdated"])

    @cached_property
    def filesDeleted(self):  # pragma: no cover
        return FileMetadata.make_many(self.boto3_raw_data["filesDeleted"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCommitOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCommitOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePullRequestInput:
    boto3_raw_data: "type_defs.CreatePullRequestInputTypeDef" = dataclasses.field()

    title = field("title")

    @cached_property
    def targets(self):  # pragma: no cover
        return Target.make_many(self.boto3_raw_data["targets"])

    description = field("description")
    clientRequestToken = field("clientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePullRequestInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePullRequestInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePullRequestEventsInputPaginate:
    boto3_raw_data: "type_defs.DescribePullRequestEventsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    pullRequestId = field("pullRequestId")
    pullRequestEventType = field("pullRequestEventType")
    actorArn = field("actorArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePullRequestEventsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePullRequestEventsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCommentsForComparedCommitInputPaginate:
    boto3_raw_data: "type_defs.GetCommentsForComparedCommitInputPaginateTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    afterCommitId = field("afterCommitId")
    beforeCommitId = field("beforeCommitId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCommentsForComparedCommitInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCommentsForComparedCommitInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCommentsForPullRequestInputPaginate:
    boto3_raw_data: "type_defs.GetCommentsForPullRequestInputPaginateTypeDef" = (
        dataclasses.field()
    )

    pullRequestId = field("pullRequestId")
    repositoryName = field("repositoryName")
    beforeCommitId = field("beforeCommitId")
    afterCommitId = field("afterCommitId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCommentsForPullRequestInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCommentsForPullRequestInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDifferencesInputPaginate:
    boto3_raw_data: "type_defs.GetDifferencesInputPaginateTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    afterCommitSpecifier = field("afterCommitSpecifier")
    beforeCommitSpecifier = field("beforeCommitSpecifier")
    beforePath = field("beforePath")
    afterPath = field("afterPath")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDifferencesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDifferencesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBranchesInputPaginate:
    boto3_raw_data: "type_defs.ListBranchesInputPaginateTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBranchesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBranchesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPullRequestsInputPaginate:
    boto3_raw_data: "type_defs.ListPullRequestsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    authorArn = field("authorArn")
    pullRequestStatus = field("pullRequestStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPullRequestsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPullRequestsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositoriesInputPaginate:
    boto3_raw_data: "type_defs.ListRepositoriesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    sortBy = field("sortBy")
    order = field("order")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRepositoriesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositoriesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluatePullRequestApprovalRulesOutput:
    boto3_raw_data: "type_defs.EvaluatePullRequestApprovalRulesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def evaluation(self):  # pragma: no cover
        return Evaluation.make_one(self.boto3_raw_data["evaluation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EvaluatePullRequestApprovalRulesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluatePullRequestApprovalRulesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFolderOutput:
    boto3_raw_data: "type_defs.GetFolderOutputTypeDef" = dataclasses.field()

    commitId = field("commitId")
    folderPath = field("folderPath")
    treeId = field("treeId")

    @cached_property
    def subFolders(self):  # pragma: no cover
        return Folder.make_many(self.boto3_raw_data["subFolders"])

    @cached_property
    def files(self):  # pragma: no cover
        return File.make_many(self.boto3_raw_data["files"])

    @cached_property
    def symbolicLinks(self):  # pragma: no cover
        return SymbolicLink.make_many(self.boto3_raw_data["symbolicLinks"])

    @cached_property
    def subModules(self):  # pragma: no cover
        return SubModule.make_many(self.boto3_raw_data["subModules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFolderOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetFolderOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRepositoryTriggersOutput:
    boto3_raw_data: "type_defs.GetRepositoryTriggersOutputTypeDef" = dataclasses.field()

    configurationId = field("configurationId")

    @cached_property
    def triggers(self):  # pragma: no cover
        return RepositoryTriggerOutput.make_many(self.boto3_raw_data["triggers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRepositoryTriggersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRepositoryTriggersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositoriesOutput:
    boto3_raw_data: "type_defs.ListRepositoriesOutputTypeDef" = dataclasses.field()

    @cached_property
    def repositories(self):  # pragma: no cover
        return RepositoryNameIdPair.make_many(self.boto3_raw_data["repositories"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRepositoriesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositoriesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MergeHunk:
    boto3_raw_data: "type_defs.MergeHunkTypeDef" = dataclasses.field()

    isConflict = field("isConflict")

    @cached_property
    def source(self):  # pragma: no cover
        return MergeHunkDetail.make_one(self.boto3_raw_data["source"])

    @cached_property
    def destination(self):  # pragma: no cover
        return MergeHunkDetail.make_one(self.boto3_raw_data["destination"])

    @cached_property
    def base(self):  # pragma: no cover
        return MergeHunkDetail.make_one(self.boto3_raw_data["base"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MergeHunkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MergeHunkTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PullRequestMergedStateChangedEventMetadata:
    boto3_raw_data: "type_defs.PullRequestMergedStateChangedEventMetadataTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    destinationReference = field("destinationReference")

    @cached_property
    def mergeMetadata(self):  # pragma: no cover
        return MergeMetadata.make_one(self.boto3_raw_data["mergeMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PullRequestMergedStateChangedEventMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PullRequestMergedStateChangedEventMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PullRequestTarget:
    boto3_raw_data: "type_defs.PullRequestTargetTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    sourceReference = field("sourceReference")
    destinationReference = field("destinationReference")
    destinationCommit = field("destinationCommit")
    sourceCommit = field("sourceCommit")
    mergeBase = field("mergeBase")

    @cached_property
    def mergeMetadata(self):  # pragma: no cover
        return MergeMetadata.make_one(self.boto3_raw_data["mergeMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PullRequestTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PullRequestTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutFileEntry:
    boto3_raw_data: "type_defs.PutFileEntryTypeDef" = dataclasses.field()

    filePath = field("filePath")
    fileMode = field("fileMode")
    fileContent = field("fileContent")

    @cached_property
    def sourceFile(self):  # pragma: no cover
        return SourceFileSpecifier.make_one(self.boto3_raw_data["sourceFile"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutFileEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutFileEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReactionForComment:
    boto3_raw_data: "type_defs.ReactionForCommentTypeDef" = dataclasses.field()

    @cached_property
    def reaction(self):  # pragma: no cover
        return ReactionValueFormats.make_one(self.boto3_raw_data["reaction"])

    reactionUsers = field("reactionUsers")
    reactionsFromDeletedUsersCount = field("reactionsFromDeletedUsersCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReactionForCommentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReactionForCommentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestRepositoryTriggersOutput:
    boto3_raw_data: "type_defs.TestRepositoryTriggersOutputTypeDef" = (
        dataclasses.field()
    )

    successfulExecutions = field("successfulExecutions")

    @cached_property
    def failedExecutions(self):  # pragma: no cover
        return RepositoryTriggerExecutionFailure.make_many(
            self.boto3_raw_data["failedExecutions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestRepositoryTriggersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestRepositoryTriggersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePullRequestApprovalRuleOutput:
    boto3_raw_data: "type_defs.CreatePullRequestApprovalRuleOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def approvalRule(self):  # pragma: no cover
        return ApprovalRule.make_one(self.boto3_raw_data["approvalRule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePullRequestApprovalRuleOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePullRequestApprovalRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePullRequestApprovalRuleContentOutput:
    boto3_raw_data: "type_defs.UpdatePullRequestApprovalRuleContentOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def approvalRule(self):  # pragma: no cover
        return ApprovalRule.make_one(self.boto3_raw_data["approvalRule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePullRequestApprovalRuleContentOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePullRequestApprovalRuleContentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDifferencesOutput:
    boto3_raw_data: "type_defs.GetDifferencesOutputTypeDef" = dataclasses.field()

    @cached_property
    def differences(self):  # pragma: no cover
        return Difference.make_many(self.boto3_raw_data["differences"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDifferencesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDifferencesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConflictResolution:
    boto3_raw_data: "type_defs.ConflictResolutionTypeDef" = dataclasses.field()

    @cached_property
    def replaceContents(self):  # pragma: no cover
        return ReplaceContentEntry.make_many(self.boto3_raw_data["replaceContents"])

    @cached_property
    def deleteFiles(self):  # pragma: no cover
        return DeleteFileEntry.make_many(self.boto3_raw_data["deleteFiles"])

    @cached_property
    def setFileModes(self):  # pragma: no cover
        return SetFileModeEntry.make_many(self.boto3_raw_data["setFileModes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConflictResolutionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConflictResolutionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCommentsForComparedCommitOutput:
    boto3_raw_data: "type_defs.GetCommentsForComparedCommitOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def commentsForComparedCommitData(self):  # pragma: no cover
        return CommentsForComparedCommit.make_many(
            self.boto3_raw_data["commentsForComparedCommitData"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCommentsForComparedCommitOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCommentsForComparedCommitOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCommentsForPullRequestOutput:
    boto3_raw_data: "type_defs.GetCommentsForPullRequestOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def commentsForPullRequestData(self):  # pragma: no cover
        return CommentsForPullRequest.make_many(
            self.boto3_raw_data["commentsForPullRequestData"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCommentsForPullRequestOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCommentsForPullRequestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetCommitsOutput:
    boto3_raw_data: "type_defs.BatchGetCommitsOutputTypeDef" = dataclasses.field()

    @cached_property
    def commits(self):  # pragma: no cover
        return Commit.make_many(self.boto3_raw_data["commits"])

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchGetCommitsError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetCommitsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetCommitsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileVersion:
    boto3_raw_data: "type_defs.FileVersionTypeDef" = dataclasses.field()

    @cached_property
    def commit(self):  # pragma: no cover
        return Commit.make_one(self.boto3_raw_data["commit"])

    blobId = field("blobId")
    path = field("path")
    revisionChildren = field("revisionChildren")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FileVersionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCommitOutput:
    boto3_raw_data: "type_defs.GetCommitOutputTypeDef" = dataclasses.field()

    @cached_property
    def commit(self):  # pragma: no cover
        return Commit.make_one(self.boto3_raw_data["commit"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetCommitOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetCommitOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMergeConflictsOutput:
    boto3_raw_data: "type_defs.GetMergeConflictsOutputTypeDef" = dataclasses.field()

    mergeable = field("mergeable")
    destinationCommitId = field("destinationCommitId")
    sourceCommitId = field("sourceCommitId")
    baseCommitId = field("baseCommitId")

    @cached_property
    def conflictMetadataList(self):  # pragma: no cover
        return ConflictMetadata.make_many(self.boto3_raw_data["conflictMetadataList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMergeConflictsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMergeConflictsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Conflict:
    boto3_raw_data: "type_defs.ConflictTypeDef" = dataclasses.field()

    @cached_property
    def conflictMetadata(self):  # pragma: no cover
        return ConflictMetadata.make_one(self.boto3_raw_data["conflictMetadata"])

    @cached_property
    def mergeHunks(self):  # pragma: no cover
        return MergeHunk.make_many(self.boto3_raw_data["mergeHunks"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConflictTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConflictTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMergeConflictsOutput:
    boto3_raw_data: "type_defs.DescribeMergeConflictsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def conflictMetadata(self):  # pragma: no cover
        return ConflictMetadata.make_one(self.boto3_raw_data["conflictMetadata"])

    @cached_property
    def mergeHunks(self):  # pragma: no cover
        return MergeHunk.make_many(self.boto3_raw_data["mergeHunks"])

    destinationCommitId = field("destinationCommitId")
    sourceCommitId = field("sourceCommitId")
    baseCommitId = field("baseCommitId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMergeConflictsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMergeConflictsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PullRequestEvent:
    boto3_raw_data: "type_defs.PullRequestEventTypeDef" = dataclasses.field()

    pullRequestId = field("pullRequestId")
    eventDate = field("eventDate")
    pullRequestEventType = field("pullRequestEventType")
    actorArn = field("actorArn")

    @cached_property
    def pullRequestCreatedEventMetadata(self):  # pragma: no cover
        return PullRequestCreatedEventMetadata.make_one(
            self.boto3_raw_data["pullRequestCreatedEventMetadata"]
        )

    @cached_property
    def pullRequestStatusChangedEventMetadata(self):  # pragma: no cover
        return PullRequestStatusChangedEventMetadata.make_one(
            self.boto3_raw_data["pullRequestStatusChangedEventMetadata"]
        )

    @cached_property
    def pullRequestSourceReferenceUpdatedEventMetadata(self):  # pragma: no cover
        return PullRequestSourceReferenceUpdatedEventMetadata.make_one(
            self.boto3_raw_data["pullRequestSourceReferenceUpdatedEventMetadata"]
        )

    @cached_property
    def pullRequestMergedStateChangedEventMetadata(self):  # pragma: no cover
        return PullRequestMergedStateChangedEventMetadata.make_one(
            self.boto3_raw_data["pullRequestMergedStateChangedEventMetadata"]
        )

    @cached_property
    def approvalRuleEventMetadata(self):  # pragma: no cover
        return ApprovalRuleEventMetadata.make_one(
            self.boto3_raw_data["approvalRuleEventMetadata"]
        )

    @cached_property
    def approvalStateChangedEventMetadata(self):  # pragma: no cover
        return ApprovalStateChangedEventMetadata.make_one(
            self.boto3_raw_data["approvalStateChangedEventMetadata"]
        )

    @cached_property
    def approvalRuleOverriddenEventMetadata(self):  # pragma: no cover
        return ApprovalRuleOverriddenEventMetadata.make_one(
            self.boto3_raw_data["approvalRuleOverriddenEventMetadata"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PullRequestEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PullRequestEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PullRequest:
    boto3_raw_data: "type_defs.PullRequestTypeDef" = dataclasses.field()

    pullRequestId = field("pullRequestId")
    title = field("title")
    description = field("description")
    lastActivityDate = field("lastActivityDate")
    creationDate = field("creationDate")
    pullRequestStatus = field("pullRequestStatus")
    authorArn = field("authorArn")

    @cached_property
    def pullRequestTargets(self):  # pragma: no cover
        return PullRequestTarget.make_many(self.boto3_raw_data["pullRequestTargets"])

    clientRequestToken = field("clientRequestToken")
    revisionId = field("revisionId")

    @cached_property
    def approvalRules(self):  # pragma: no cover
        return ApprovalRule.make_many(self.boto3_raw_data["approvalRules"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PullRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PullRequestTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCommitInput:
    boto3_raw_data: "type_defs.CreateCommitInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    branchName = field("branchName")
    parentCommitId = field("parentCommitId")
    authorName = field("authorName")
    email = field("email")
    commitMessage = field("commitMessage")
    keepEmptyFolders = field("keepEmptyFolders")

    @cached_property
    def putFiles(self):  # pragma: no cover
        return PutFileEntry.make_many(self.boto3_raw_data["putFiles"])

    @cached_property
    def deleteFiles(self):  # pragma: no cover
        return DeleteFileEntry.make_many(self.boto3_raw_data["deleteFiles"])

    @cached_property
    def setFileModes(self):  # pragma: no cover
        return SetFileModeEntry.make_many(self.boto3_raw_data["setFileModes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateCommitInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCommitInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCommentReactionsOutput:
    boto3_raw_data: "type_defs.GetCommentReactionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def reactionsForComment(self):  # pragma: no cover
        return ReactionForComment.make_many(self.boto3_raw_data["reactionsForComment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCommentReactionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCommentReactionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRepositoryTriggersInput:
    boto3_raw_data: "type_defs.PutRepositoryTriggersInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    triggers = field("triggers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutRepositoryTriggersInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRepositoryTriggersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestRepositoryTriggersInput:
    boto3_raw_data: "type_defs.TestRepositoryTriggersInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    triggers = field("triggers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestRepositoryTriggersInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestRepositoryTriggersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUnreferencedMergeCommitInput:
    boto3_raw_data: "type_defs.CreateUnreferencedMergeCommitInputTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    sourceCommitSpecifier = field("sourceCommitSpecifier")
    destinationCommitSpecifier = field("destinationCommitSpecifier")
    mergeOption = field("mergeOption")
    conflictDetailLevel = field("conflictDetailLevel")
    conflictResolutionStrategy = field("conflictResolutionStrategy")
    authorName = field("authorName")
    email = field("email")
    commitMessage = field("commitMessage")
    keepEmptyFolders = field("keepEmptyFolders")

    @cached_property
    def conflictResolution(self):  # pragma: no cover
        return ConflictResolution.make_one(self.boto3_raw_data["conflictResolution"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateUnreferencedMergeCommitInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUnreferencedMergeCommitInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MergeBranchesBySquashInput:
    boto3_raw_data: "type_defs.MergeBranchesBySquashInputTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    sourceCommitSpecifier = field("sourceCommitSpecifier")
    destinationCommitSpecifier = field("destinationCommitSpecifier")
    targetBranch = field("targetBranch")
    conflictDetailLevel = field("conflictDetailLevel")
    conflictResolutionStrategy = field("conflictResolutionStrategy")
    authorName = field("authorName")
    email = field("email")
    commitMessage = field("commitMessage")
    keepEmptyFolders = field("keepEmptyFolders")

    @cached_property
    def conflictResolution(self):  # pragma: no cover
        return ConflictResolution.make_one(self.boto3_raw_data["conflictResolution"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MergeBranchesBySquashInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MergeBranchesBySquashInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MergeBranchesByThreeWayInput:
    boto3_raw_data: "type_defs.MergeBranchesByThreeWayInputTypeDef" = (
        dataclasses.field()
    )

    repositoryName = field("repositoryName")
    sourceCommitSpecifier = field("sourceCommitSpecifier")
    destinationCommitSpecifier = field("destinationCommitSpecifier")
    targetBranch = field("targetBranch")
    conflictDetailLevel = field("conflictDetailLevel")
    conflictResolutionStrategy = field("conflictResolutionStrategy")
    authorName = field("authorName")
    email = field("email")
    commitMessage = field("commitMessage")
    keepEmptyFolders = field("keepEmptyFolders")

    @cached_property
    def conflictResolution(self):  # pragma: no cover
        return ConflictResolution.make_one(self.boto3_raw_data["conflictResolution"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MergeBranchesByThreeWayInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MergeBranchesByThreeWayInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MergePullRequestBySquashInput:
    boto3_raw_data: "type_defs.MergePullRequestBySquashInputTypeDef" = (
        dataclasses.field()
    )

    pullRequestId = field("pullRequestId")
    repositoryName = field("repositoryName")
    sourceCommitId = field("sourceCommitId")
    conflictDetailLevel = field("conflictDetailLevel")
    conflictResolutionStrategy = field("conflictResolutionStrategy")
    commitMessage = field("commitMessage")
    authorName = field("authorName")
    email = field("email")
    keepEmptyFolders = field("keepEmptyFolders")

    @cached_property
    def conflictResolution(self):  # pragma: no cover
        return ConflictResolution.make_one(self.boto3_raw_data["conflictResolution"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MergePullRequestBySquashInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MergePullRequestBySquashInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MergePullRequestByThreeWayInput:
    boto3_raw_data: "type_defs.MergePullRequestByThreeWayInputTypeDef" = (
        dataclasses.field()
    )

    pullRequestId = field("pullRequestId")
    repositoryName = field("repositoryName")
    sourceCommitId = field("sourceCommitId")
    conflictDetailLevel = field("conflictDetailLevel")
    conflictResolutionStrategy = field("conflictResolutionStrategy")
    commitMessage = field("commitMessage")
    authorName = field("authorName")
    email = field("email")
    keepEmptyFolders = field("keepEmptyFolders")

    @cached_property
    def conflictResolution(self):  # pragma: no cover
        return ConflictResolution.make_one(self.boto3_raw_data["conflictResolution"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MergePullRequestByThreeWayInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MergePullRequestByThreeWayInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFileCommitHistoryResponse:
    boto3_raw_data: "type_defs.ListFileCommitHistoryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def revisionDag(self):  # pragma: no cover
        return FileVersion.make_many(self.boto3_raw_data["revisionDag"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFileCommitHistoryResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFileCommitHistoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDescribeMergeConflictsOutput:
    boto3_raw_data: "type_defs.BatchDescribeMergeConflictsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def conflicts(self):  # pragma: no cover
        return Conflict.make_many(self.boto3_raw_data["conflicts"])

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchDescribeMergeConflictsError.make_many(self.boto3_raw_data["errors"])

    destinationCommitId = field("destinationCommitId")
    sourceCommitId = field("sourceCommitId")
    baseCommitId = field("baseCommitId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDescribeMergeConflictsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDescribeMergeConflictsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePullRequestEventsOutput:
    boto3_raw_data: "type_defs.DescribePullRequestEventsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def pullRequestEvents(self):  # pragma: no cover
        return PullRequestEvent.make_many(self.boto3_raw_data["pullRequestEvents"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePullRequestEventsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePullRequestEventsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePullRequestOutput:
    boto3_raw_data: "type_defs.CreatePullRequestOutputTypeDef" = dataclasses.field()

    @cached_property
    def pullRequest(self):  # pragma: no cover
        return PullRequest.make_one(self.boto3_raw_data["pullRequest"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePullRequestOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePullRequestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPullRequestOutput:
    boto3_raw_data: "type_defs.GetPullRequestOutputTypeDef" = dataclasses.field()

    @cached_property
    def pullRequest(self):  # pragma: no cover
        return PullRequest.make_one(self.boto3_raw_data["pullRequest"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPullRequestOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPullRequestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MergePullRequestByFastForwardOutput:
    boto3_raw_data: "type_defs.MergePullRequestByFastForwardOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def pullRequest(self):  # pragma: no cover
        return PullRequest.make_one(self.boto3_raw_data["pullRequest"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MergePullRequestByFastForwardOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MergePullRequestByFastForwardOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MergePullRequestBySquashOutput:
    boto3_raw_data: "type_defs.MergePullRequestBySquashOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def pullRequest(self):  # pragma: no cover
        return PullRequest.make_one(self.boto3_raw_data["pullRequest"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MergePullRequestBySquashOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MergePullRequestBySquashOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MergePullRequestByThreeWayOutput:
    boto3_raw_data: "type_defs.MergePullRequestByThreeWayOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def pullRequest(self):  # pragma: no cover
        return PullRequest.make_one(self.boto3_raw_data["pullRequest"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MergePullRequestByThreeWayOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MergePullRequestByThreeWayOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePullRequestDescriptionOutput:
    boto3_raw_data: "type_defs.UpdatePullRequestDescriptionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def pullRequest(self):  # pragma: no cover
        return PullRequest.make_one(self.boto3_raw_data["pullRequest"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePullRequestDescriptionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePullRequestDescriptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePullRequestStatusOutput:
    boto3_raw_data: "type_defs.UpdatePullRequestStatusOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def pullRequest(self):  # pragma: no cover
        return PullRequest.make_one(self.boto3_raw_data["pullRequest"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdatePullRequestStatusOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePullRequestStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePullRequestTitleOutput:
    boto3_raw_data: "type_defs.UpdatePullRequestTitleOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def pullRequest(self):  # pragma: no cover
        return PullRequest.make_one(self.boto3_raw_data["pullRequest"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePullRequestTitleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePullRequestTitleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
