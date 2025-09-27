# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_codecommit import type_defs as bs_td


class CODECOMMITCaster:

    def associate_approval_rule_template_with_repository(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def batch_associate_approval_rule_template_with_repositories(
        self,
        res: "bs_td.BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef",
    ) -> "dc_td.BatchAssociateApprovalRuleTemplateWithRepositoriesOutput":
        return dc_td.BatchAssociateApprovalRuleTemplateWithRepositoriesOutput.make_one(
            res
        )

    def batch_describe_merge_conflicts(
        self,
        res: "bs_td.BatchDescribeMergeConflictsOutputTypeDef",
    ) -> "dc_td.BatchDescribeMergeConflictsOutput":
        return dc_td.BatchDescribeMergeConflictsOutput.make_one(res)

    def batch_disassociate_approval_rule_template_from_repositories(
        self,
        res: "bs_td.BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef",
    ) -> "dc_td.BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput":
        return (
            dc_td.BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput.make_one(
                res
            )
        )

    def batch_get_commits(
        self,
        res: "bs_td.BatchGetCommitsOutputTypeDef",
    ) -> "dc_td.BatchGetCommitsOutput":
        return dc_td.BatchGetCommitsOutput.make_one(res)

    def batch_get_repositories(
        self,
        res: "bs_td.BatchGetRepositoriesOutputTypeDef",
    ) -> "dc_td.BatchGetRepositoriesOutput":
        return dc_td.BatchGetRepositoriesOutput.make_one(res)

    def create_approval_rule_template(
        self,
        res: "bs_td.CreateApprovalRuleTemplateOutputTypeDef",
    ) -> "dc_td.CreateApprovalRuleTemplateOutput":
        return dc_td.CreateApprovalRuleTemplateOutput.make_one(res)

    def create_branch(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_commit(
        self,
        res: "bs_td.CreateCommitOutputTypeDef",
    ) -> "dc_td.CreateCommitOutput":
        return dc_td.CreateCommitOutput.make_one(res)

    def create_pull_request(
        self,
        res: "bs_td.CreatePullRequestOutputTypeDef",
    ) -> "dc_td.CreatePullRequestOutput":
        return dc_td.CreatePullRequestOutput.make_one(res)

    def create_pull_request_approval_rule(
        self,
        res: "bs_td.CreatePullRequestApprovalRuleOutputTypeDef",
    ) -> "dc_td.CreatePullRequestApprovalRuleOutput":
        return dc_td.CreatePullRequestApprovalRuleOutput.make_one(res)

    def create_repository(
        self,
        res: "bs_td.CreateRepositoryOutputTypeDef",
    ) -> "dc_td.CreateRepositoryOutput":
        return dc_td.CreateRepositoryOutput.make_one(res)

    def create_unreferenced_merge_commit(
        self,
        res: "bs_td.CreateUnreferencedMergeCommitOutputTypeDef",
    ) -> "dc_td.CreateUnreferencedMergeCommitOutput":
        return dc_td.CreateUnreferencedMergeCommitOutput.make_one(res)

    def delete_approval_rule_template(
        self,
        res: "bs_td.DeleteApprovalRuleTemplateOutputTypeDef",
    ) -> "dc_td.DeleteApprovalRuleTemplateOutput":
        return dc_td.DeleteApprovalRuleTemplateOutput.make_one(res)

    def delete_branch(
        self,
        res: "bs_td.DeleteBranchOutputTypeDef",
    ) -> "dc_td.DeleteBranchOutput":
        return dc_td.DeleteBranchOutput.make_one(res)

    def delete_comment_content(
        self,
        res: "bs_td.DeleteCommentContentOutputTypeDef",
    ) -> "dc_td.DeleteCommentContentOutput":
        return dc_td.DeleteCommentContentOutput.make_one(res)

    def delete_file(
        self,
        res: "bs_td.DeleteFileOutputTypeDef",
    ) -> "dc_td.DeleteFileOutput":
        return dc_td.DeleteFileOutput.make_one(res)

    def delete_pull_request_approval_rule(
        self,
        res: "bs_td.DeletePullRequestApprovalRuleOutputTypeDef",
    ) -> "dc_td.DeletePullRequestApprovalRuleOutput":
        return dc_td.DeletePullRequestApprovalRuleOutput.make_one(res)

    def delete_repository(
        self,
        res: "bs_td.DeleteRepositoryOutputTypeDef",
    ) -> "dc_td.DeleteRepositoryOutput":
        return dc_td.DeleteRepositoryOutput.make_one(res)

    def describe_merge_conflicts(
        self,
        res: "bs_td.DescribeMergeConflictsOutputTypeDef",
    ) -> "dc_td.DescribeMergeConflictsOutput":
        return dc_td.DescribeMergeConflictsOutput.make_one(res)

    def describe_pull_request_events(
        self,
        res: "bs_td.DescribePullRequestEventsOutputTypeDef",
    ) -> "dc_td.DescribePullRequestEventsOutput":
        return dc_td.DescribePullRequestEventsOutput.make_one(res)

    def disassociate_approval_rule_template_from_repository(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def evaluate_pull_request_approval_rules(
        self,
        res: "bs_td.EvaluatePullRequestApprovalRulesOutputTypeDef",
    ) -> "dc_td.EvaluatePullRequestApprovalRulesOutput":
        return dc_td.EvaluatePullRequestApprovalRulesOutput.make_one(res)

    def get_approval_rule_template(
        self,
        res: "bs_td.GetApprovalRuleTemplateOutputTypeDef",
    ) -> "dc_td.GetApprovalRuleTemplateOutput":
        return dc_td.GetApprovalRuleTemplateOutput.make_one(res)

    def get_blob(
        self,
        res: "bs_td.GetBlobOutputTypeDef",
    ) -> "dc_td.GetBlobOutput":
        return dc_td.GetBlobOutput.make_one(res)

    def get_branch(
        self,
        res: "bs_td.GetBranchOutputTypeDef",
    ) -> "dc_td.GetBranchOutput":
        return dc_td.GetBranchOutput.make_one(res)

    def get_comment(
        self,
        res: "bs_td.GetCommentOutputTypeDef",
    ) -> "dc_td.GetCommentOutput":
        return dc_td.GetCommentOutput.make_one(res)

    def get_comment_reactions(
        self,
        res: "bs_td.GetCommentReactionsOutputTypeDef",
    ) -> "dc_td.GetCommentReactionsOutput":
        return dc_td.GetCommentReactionsOutput.make_one(res)

    def get_comments_for_compared_commit(
        self,
        res: "bs_td.GetCommentsForComparedCommitOutputTypeDef",
    ) -> "dc_td.GetCommentsForComparedCommitOutput":
        return dc_td.GetCommentsForComparedCommitOutput.make_one(res)

    def get_comments_for_pull_request(
        self,
        res: "bs_td.GetCommentsForPullRequestOutputTypeDef",
    ) -> "dc_td.GetCommentsForPullRequestOutput":
        return dc_td.GetCommentsForPullRequestOutput.make_one(res)

    def get_commit(
        self,
        res: "bs_td.GetCommitOutputTypeDef",
    ) -> "dc_td.GetCommitOutput":
        return dc_td.GetCommitOutput.make_one(res)

    def get_differences(
        self,
        res: "bs_td.GetDifferencesOutputTypeDef",
    ) -> "dc_td.GetDifferencesOutput":
        return dc_td.GetDifferencesOutput.make_one(res)

    def get_file(
        self,
        res: "bs_td.GetFileOutputTypeDef",
    ) -> "dc_td.GetFileOutput":
        return dc_td.GetFileOutput.make_one(res)

    def get_folder(
        self,
        res: "bs_td.GetFolderOutputTypeDef",
    ) -> "dc_td.GetFolderOutput":
        return dc_td.GetFolderOutput.make_one(res)

    def get_merge_commit(
        self,
        res: "bs_td.GetMergeCommitOutputTypeDef",
    ) -> "dc_td.GetMergeCommitOutput":
        return dc_td.GetMergeCommitOutput.make_one(res)

    def get_merge_conflicts(
        self,
        res: "bs_td.GetMergeConflictsOutputTypeDef",
    ) -> "dc_td.GetMergeConflictsOutput":
        return dc_td.GetMergeConflictsOutput.make_one(res)

    def get_merge_options(
        self,
        res: "bs_td.GetMergeOptionsOutputTypeDef",
    ) -> "dc_td.GetMergeOptionsOutput":
        return dc_td.GetMergeOptionsOutput.make_one(res)

    def get_pull_request(
        self,
        res: "bs_td.GetPullRequestOutputTypeDef",
    ) -> "dc_td.GetPullRequestOutput":
        return dc_td.GetPullRequestOutput.make_one(res)

    def get_pull_request_approval_states(
        self,
        res: "bs_td.GetPullRequestApprovalStatesOutputTypeDef",
    ) -> "dc_td.GetPullRequestApprovalStatesOutput":
        return dc_td.GetPullRequestApprovalStatesOutput.make_one(res)

    def get_pull_request_override_state(
        self,
        res: "bs_td.GetPullRequestOverrideStateOutputTypeDef",
    ) -> "dc_td.GetPullRequestOverrideStateOutput":
        return dc_td.GetPullRequestOverrideStateOutput.make_one(res)

    def get_repository(
        self,
        res: "bs_td.GetRepositoryOutputTypeDef",
    ) -> "dc_td.GetRepositoryOutput":
        return dc_td.GetRepositoryOutput.make_one(res)

    def get_repository_triggers(
        self,
        res: "bs_td.GetRepositoryTriggersOutputTypeDef",
    ) -> "dc_td.GetRepositoryTriggersOutput":
        return dc_td.GetRepositoryTriggersOutput.make_one(res)

    def list_approval_rule_templates(
        self,
        res: "bs_td.ListApprovalRuleTemplatesOutputTypeDef",
    ) -> "dc_td.ListApprovalRuleTemplatesOutput":
        return dc_td.ListApprovalRuleTemplatesOutput.make_one(res)

    def list_associated_approval_rule_templates_for_repository(
        self,
        res: "bs_td.ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef",
    ) -> "dc_td.ListAssociatedApprovalRuleTemplatesForRepositoryOutput":
        return dc_td.ListAssociatedApprovalRuleTemplatesForRepositoryOutput.make_one(
            res
        )

    def list_branches(
        self,
        res: "bs_td.ListBranchesOutputTypeDef",
    ) -> "dc_td.ListBranchesOutput":
        return dc_td.ListBranchesOutput.make_one(res)

    def list_file_commit_history(
        self,
        res: "bs_td.ListFileCommitHistoryResponseTypeDef",
    ) -> "dc_td.ListFileCommitHistoryResponse":
        return dc_td.ListFileCommitHistoryResponse.make_one(res)

    def list_pull_requests(
        self,
        res: "bs_td.ListPullRequestsOutputTypeDef",
    ) -> "dc_td.ListPullRequestsOutput":
        return dc_td.ListPullRequestsOutput.make_one(res)

    def list_repositories(
        self,
        res: "bs_td.ListRepositoriesOutputTypeDef",
    ) -> "dc_td.ListRepositoriesOutput":
        return dc_td.ListRepositoriesOutput.make_one(res)

    def list_repositories_for_approval_rule_template(
        self,
        res: "bs_td.ListRepositoriesForApprovalRuleTemplateOutputTypeDef",
    ) -> "dc_td.ListRepositoriesForApprovalRuleTemplateOutput":
        return dc_td.ListRepositoriesForApprovalRuleTemplateOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def merge_branches_by_fast_forward(
        self,
        res: "bs_td.MergeBranchesByFastForwardOutputTypeDef",
    ) -> "dc_td.MergeBranchesByFastForwardOutput":
        return dc_td.MergeBranchesByFastForwardOutput.make_one(res)

    def merge_branches_by_squash(
        self,
        res: "bs_td.MergeBranchesBySquashOutputTypeDef",
    ) -> "dc_td.MergeBranchesBySquashOutput":
        return dc_td.MergeBranchesBySquashOutput.make_one(res)

    def merge_branches_by_three_way(
        self,
        res: "bs_td.MergeBranchesByThreeWayOutputTypeDef",
    ) -> "dc_td.MergeBranchesByThreeWayOutput":
        return dc_td.MergeBranchesByThreeWayOutput.make_one(res)

    def merge_pull_request_by_fast_forward(
        self,
        res: "bs_td.MergePullRequestByFastForwardOutputTypeDef",
    ) -> "dc_td.MergePullRequestByFastForwardOutput":
        return dc_td.MergePullRequestByFastForwardOutput.make_one(res)

    def merge_pull_request_by_squash(
        self,
        res: "bs_td.MergePullRequestBySquashOutputTypeDef",
    ) -> "dc_td.MergePullRequestBySquashOutput":
        return dc_td.MergePullRequestBySquashOutput.make_one(res)

    def merge_pull_request_by_three_way(
        self,
        res: "bs_td.MergePullRequestByThreeWayOutputTypeDef",
    ) -> "dc_td.MergePullRequestByThreeWayOutput":
        return dc_td.MergePullRequestByThreeWayOutput.make_one(res)

    def override_pull_request_approval_rules(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def post_comment_for_compared_commit(
        self,
        res: "bs_td.PostCommentForComparedCommitOutputTypeDef",
    ) -> "dc_td.PostCommentForComparedCommitOutput":
        return dc_td.PostCommentForComparedCommitOutput.make_one(res)

    def post_comment_for_pull_request(
        self,
        res: "bs_td.PostCommentForPullRequestOutputTypeDef",
    ) -> "dc_td.PostCommentForPullRequestOutput":
        return dc_td.PostCommentForPullRequestOutput.make_one(res)

    def post_comment_reply(
        self,
        res: "bs_td.PostCommentReplyOutputTypeDef",
    ) -> "dc_td.PostCommentReplyOutput":
        return dc_td.PostCommentReplyOutput.make_one(res)

    def put_comment_reaction(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_file(
        self,
        res: "bs_td.PutFileOutputTypeDef",
    ) -> "dc_td.PutFileOutput":
        return dc_td.PutFileOutput.make_one(res)

    def put_repository_triggers(
        self,
        res: "bs_td.PutRepositoryTriggersOutputTypeDef",
    ) -> "dc_td.PutRepositoryTriggersOutput":
        return dc_td.PutRepositoryTriggersOutput.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def test_repository_triggers(
        self,
        res: "bs_td.TestRepositoryTriggersOutputTypeDef",
    ) -> "dc_td.TestRepositoryTriggersOutput":
        return dc_td.TestRepositoryTriggersOutput.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_approval_rule_template_content(
        self,
        res: "bs_td.UpdateApprovalRuleTemplateContentOutputTypeDef",
    ) -> "dc_td.UpdateApprovalRuleTemplateContentOutput":
        return dc_td.UpdateApprovalRuleTemplateContentOutput.make_one(res)

    def update_approval_rule_template_description(
        self,
        res: "bs_td.UpdateApprovalRuleTemplateDescriptionOutputTypeDef",
    ) -> "dc_td.UpdateApprovalRuleTemplateDescriptionOutput":
        return dc_td.UpdateApprovalRuleTemplateDescriptionOutput.make_one(res)

    def update_approval_rule_template_name(
        self,
        res: "bs_td.UpdateApprovalRuleTemplateNameOutputTypeDef",
    ) -> "dc_td.UpdateApprovalRuleTemplateNameOutput":
        return dc_td.UpdateApprovalRuleTemplateNameOutput.make_one(res)

    def update_comment(
        self,
        res: "bs_td.UpdateCommentOutputTypeDef",
    ) -> "dc_td.UpdateCommentOutput":
        return dc_td.UpdateCommentOutput.make_one(res)

    def update_default_branch(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_pull_request_approval_rule_content(
        self,
        res: "bs_td.UpdatePullRequestApprovalRuleContentOutputTypeDef",
    ) -> "dc_td.UpdatePullRequestApprovalRuleContentOutput":
        return dc_td.UpdatePullRequestApprovalRuleContentOutput.make_one(res)

    def update_pull_request_approval_state(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_pull_request_description(
        self,
        res: "bs_td.UpdatePullRequestDescriptionOutputTypeDef",
    ) -> "dc_td.UpdatePullRequestDescriptionOutput":
        return dc_td.UpdatePullRequestDescriptionOutput.make_one(res)

    def update_pull_request_status(
        self,
        res: "bs_td.UpdatePullRequestStatusOutputTypeDef",
    ) -> "dc_td.UpdatePullRequestStatusOutput":
        return dc_td.UpdatePullRequestStatusOutput.make_one(res)

    def update_pull_request_title(
        self,
        res: "bs_td.UpdatePullRequestTitleOutputTypeDef",
    ) -> "dc_td.UpdatePullRequestTitleOutput":
        return dc_td.UpdatePullRequestTitleOutput.make_one(res)

    def update_repository_description(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_repository_encryption_key(
        self,
        res: "bs_td.UpdateRepositoryEncryptionKeyOutputTypeDef",
    ) -> "dc_td.UpdateRepositoryEncryptionKeyOutput":
        return dc_td.UpdateRepositoryEncryptionKeyOutput.make_one(res)

    def update_repository_name(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


codecommit_caster = CODECOMMITCaster()
