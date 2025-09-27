# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_codebuild import type_defs as bs_td


class CODEBUILDCaster:

    def batch_delete_builds(
        self,
        res: "bs_td.BatchDeleteBuildsOutputTypeDef",
    ) -> "dc_td.BatchDeleteBuildsOutput":
        return dc_td.BatchDeleteBuildsOutput.make_one(res)

    def batch_get_build_batches(
        self,
        res: "bs_td.BatchGetBuildBatchesOutputTypeDef",
    ) -> "dc_td.BatchGetBuildBatchesOutput":
        return dc_td.BatchGetBuildBatchesOutput.make_one(res)

    def batch_get_builds(
        self,
        res: "bs_td.BatchGetBuildsOutputTypeDef",
    ) -> "dc_td.BatchGetBuildsOutput":
        return dc_td.BatchGetBuildsOutput.make_one(res)

    def batch_get_command_executions(
        self,
        res: "bs_td.BatchGetCommandExecutionsOutputTypeDef",
    ) -> "dc_td.BatchGetCommandExecutionsOutput":
        return dc_td.BatchGetCommandExecutionsOutput.make_one(res)

    def batch_get_fleets(
        self,
        res: "bs_td.BatchGetFleetsOutputTypeDef",
    ) -> "dc_td.BatchGetFleetsOutput":
        return dc_td.BatchGetFleetsOutput.make_one(res)

    def batch_get_projects(
        self,
        res: "bs_td.BatchGetProjectsOutputTypeDef",
    ) -> "dc_td.BatchGetProjectsOutput":
        return dc_td.BatchGetProjectsOutput.make_one(res)

    def batch_get_report_groups(
        self,
        res: "bs_td.BatchGetReportGroupsOutputTypeDef",
    ) -> "dc_td.BatchGetReportGroupsOutput":
        return dc_td.BatchGetReportGroupsOutput.make_one(res)

    def batch_get_reports(
        self,
        res: "bs_td.BatchGetReportsOutputTypeDef",
    ) -> "dc_td.BatchGetReportsOutput":
        return dc_td.BatchGetReportsOutput.make_one(res)

    def batch_get_sandboxes(
        self,
        res: "bs_td.BatchGetSandboxesOutputTypeDef",
    ) -> "dc_td.BatchGetSandboxesOutput":
        return dc_td.BatchGetSandboxesOutput.make_one(res)

    def create_fleet(
        self,
        res: "bs_td.CreateFleetOutputTypeDef",
    ) -> "dc_td.CreateFleetOutput":
        return dc_td.CreateFleetOutput.make_one(res)

    def create_project(
        self,
        res: "bs_td.CreateProjectOutputTypeDef",
    ) -> "dc_td.CreateProjectOutput":
        return dc_td.CreateProjectOutput.make_one(res)

    def create_report_group(
        self,
        res: "bs_td.CreateReportGroupOutputTypeDef",
    ) -> "dc_td.CreateReportGroupOutput":
        return dc_td.CreateReportGroupOutput.make_one(res)

    def create_webhook(
        self,
        res: "bs_td.CreateWebhookOutputTypeDef",
    ) -> "dc_td.CreateWebhookOutput":
        return dc_td.CreateWebhookOutput.make_one(res)

    def delete_build_batch(
        self,
        res: "bs_td.DeleteBuildBatchOutputTypeDef",
    ) -> "dc_td.DeleteBuildBatchOutput":
        return dc_td.DeleteBuildBatchOutput.make_one(res)

    def delete_source_credentials(
        self,
        res: "bs_td.DeleteSourceCredentialsOutputTypeDef",
    ) -> "dc_td.DeleteSourceCredentialsOutput":
        return dc_td.DeleteSourceCredentialsOutput.make_one(res)

    def describe_code_coverages(
        self,
        res: "bs_td.DescribeCodeCoveragesOutputTypeDef",
    ) -> "dc_td.DescribeCodeCoveragesOutput":
        return dc_td.DescribeCodeCoveragesOutput.make_one(res)

    def describe_test_cases(
        self,
        res: "bs_td.DescribeTestCasesOutputTypeDef",
    ) -> "dc_td.DescribeTestCasesOutput":
        return dc_td.DescribeTestCasesOutput.make_one(res)

    def get_report_group_trend(
        self,
        res: "bs_td.GetReportGroupTrendOutputTypeDef",
    ) -> "dc_td.GetReportGroupTrendOutput":
        return dc_td.GetReportGroupTrendOutput.make_one(res)

    def get_resource_policy(
        self,
        res: "bs_td.GetResourcePolicyOutputTypeDef",
    ) -> "dc_td.GetResourcePolicyOutput":
        return dc_td.GetResourcePolicyOutput.make_one(res)

    def import_source_credentials(
        self,
        res: "bs_td.ImportSourceCredentialsOutputTypeDef",
    ) -> "dc_td.ImportSourceCredentialsOutput":
        return dc_td.ImportSourceCredentialsOutput.make_one(res)

    def list_build_batches(
        self,
        res: "bs_td.ListBuildBatchesOutputTypeDef",
    ) -> "dc_td.ListBuildBatchesOutput":
        return dc_td.ListBuildBatchesOutput.make_one(res)

    def list_build_batches_for_project(
        self,
        res: "bs_td.ListBuildBatchesForProjectOutputTypeDef",
    ) -> "dc_td.ListBuildBatchesForProjectOutput":
        return dc_td.ListBuildBatchesForProjectOutput.make_one(res)

    def list_builds(
        self,
        res: "bs_td.ListBuildsOutputTypeDef",
    ) -> "dc_td.ListBuildsOutput":
        return dc_td.ListBuildsOutput.make_one(res)

    def list_builds_for_project(
        self,
        res: "bs_td.ListBuildsForProjectOutputTypeDef",
    ) -> "dc_td.ListBuildsForProjectOutput":
        return dc_td.ListBuildsForProjectOutput.make_one(res)

    def list_command_executions_for_sandbox(
        self,
        res: "bs_td.ListCommandExecutionsForSandboxOutputTypeDef",
    ) -> "dc_td.ListCommandExecutionsForSandboxOutput":
        return dc_td.ListCommandExecutionsForSandboxOutput.make_one(res)

    def list_curated_environment_images(
        self,
        res: "bs_td.ListCuratedEnvironmentImagesOutputTypeDef",
    ) -> "dc_td.ListCuratedEnvironmentImagesOutput":
        return dc_td.ListCuratedEnvironmentImagesOutput.make_one(res)

    def list_fleets(
        self,
        res: "bs_td.ListFleetsOutputTypeDef",
    ) -> "dc_td.ListFleetsOutput":
        return dc_td.ListFleetsOutput.make_one(res)

    def list_projects(
        self,
        res: "bs_td.ListProjectsOutputTypeDef",
    ) -> "dc_td.ListProjectsOutput":
        return dc_td.ListProjectsOutput.make_one(res)

    def list_report_groups(
        self,
        res: "bs_td.ListReportGroupsOutputTypeDef",
    ) -> "dc_td.ListReportGroupsOutput":
        return dc_td.ListReportGroupsOutput.make_one(res)

    def list_reports(
        self,
        res: "bs_td.ListReportsOutputTypeDef",
    ) -> "dc_td.ListReportsOutput":
        return dc_td.ListReportsOutput.make_one(res)

    def list_reports_for_report_group(
        self,
        res: "bs_td.ListReportsForReportGroupOutputTypeDef",
    ) -> "dc_td.ListReportsForReportGroupOutput":
        return dc_td.ListReportsForReportGroupOutput.make_one(res)

    def list_sandboxes(
        self,
        res: "bs_td.ListSandboxesOutputTypeDef",
    ) -> "dc_td.ListSandboxesOutput":
        return dc_td.ListSandboxesOutput.make_one(res)

    def list_sandboxes_for_project(
        self,
        res: "bs_td.ListSandboxesForProjectOutputTypeDef",
    ) -> "dc_td.ListSandboxesForProjectOutput":
        return dc_td.ListSandboxesForProjectOutput.make_one(res)

    def list_shared_projects(
        self,
        res: "bs_td.ListSharedProjectsOutputTypeDef",
    ) -> "dc_td.ListSharedProjectsOutput":
        return dc_td.ListSharedProjectsOutput.make_one(res)

    def list_shared_report_groups(
        self,
        res: "bs_td.ListSharedReportGroupsOutputTypeDef",
    ) -> "dc_td.ListSharedReportGroupsOutput":
        return dc_td.ListSharedReportGroupsOutput.make_one(res)

    def list_source_credentials(
        self,
        res: "bs_td.ListSourceCredentialsOutputTypeDef",
    ) -> "dc_td.ListSourceCredentialsOutput":
        return dc_td.ListSourceCredentialsOutput.make_one(res)

    def put_resource_policy(
        self,
        res: "bs_td.PutResourcePolicyOutputTypeDef",
    ) -> "dc_td.PutResourcePolicyOutput":
        return dc_td.PutResourcePolicyOutput.make_one(res)

    def retry_build(
        self,
        res: "bs_td.RetryBuildOutputTypeDef",
    ) -> "dc_td.RetryBuildOutput":
        return dc_td.RetryBuildOutput.make_one(res)

    def retry_build_batch(
        self,
        res: "bs_td.RetryBuildBatchOutputTypeDef",
    ) -> "dc_td.RetryBuildBatchOutput":
        return dc_td.RetryBuildBatchOutput.make_one(res)

    def start_build(
        self,
        res: "bs_td.StartBuildOutputTypeDef",
    ) -> "dc_td.StartBuildOutput":
        return dc_td.StartBuildOutput.make_one(res)

    def start_build_batch(
        self,
        res: "bs_td.StartBuildBatchOutputTypeDef",
    ) -> "dc_td.StartBuildBatchOutput":
        return dc_td.StartBuildBatchOutput.make_one(res)

    def start_command_execution(
        self,
        res: "bs_td.StartCommandExecutionOutputTypeDef",
    ) -> "dc_td.StartCommandExecutionOutput":
        return dc_td.StartCommandExecutionOutput.make_one(res)

    def start_sandbox(
        self,
        res: "bs_td.StartSandboxOutputTypeDef",
    ) -> "dc_td.StartSandboxOutput":
        return dc_td.StartSandboxOutput.make_one(res)

    def start_sandbox_connection(
        self,
        res: "bs_td.StartSandboxConnectionOutputTypeDef",
    ) -> "dc_td.StartSandboxConnectionOutput":
        return dc_td.StartSandboxConnectionOutput.make_one(res)

    def stop_build(
        self,
        res: "bs_td.StopBuildOutputTypeDef",
    ) -> "dc_td.StopBuildOutput":
        return dc_td.StopBuildOutput.make_one(res)

    def stop_build_batch(
        self,
        res: "bs_td.StopBuildBatchOutputTypeDef",
    ) -> "dc_td.StopBuildBatchOutput":
        return dc_td.StopBuildBatchOutput.make_one(res)

    def stop_sandbox(
        self,
        res: "bs_td.StopSandboxOutputTypeDef",
    ) -> "dc_td.StopSandboxOutput":
        return dc_td.StopSandboxOutput.make_one(res)

    def update_fleet(
        self,
        res: "bs_td.UpdateFleetOutputTypeDef",
    ) -> "dc_td.UpdateFleetOutput":
        return dc_td.UpdateFleetOutput.make_one(res)

    def update_project(
        self,
        res: "bs_td.UpdateProjectOutputTypeDef",
    ) -> "dc_td.UpdateProjectOutput":
        return dc_td.UpdateProjectOutput.make_one(res)

    def update_project_visibility(
        self,
        res: "bs_td.UpdateProjectVisibilityOutputTypeDef",
    ) -> "dc_td.UpdateProjectVisibilityOutput":
        return dc_td.UpdateProjectVisibilityOutput.make_one(res)

    def update_report_group(
        self,
        res: "bs_td.UpdateReportGroupOutputTypeDef",
    ) -> "dc_td.UpdateReportGroupOutput":
        return dc_td.UpdateReportGroupOutput.make_one(res)

    def update_webhook(
        self,
        res: "bs_td.UpdateWebhookOutputTypeDef",
    ) -> "dc_td.UpdateWebhookOutput":
        return dc_td.UpdateWebhookOutput.make_one(res)


codebuild_caster = CODEBUILDCaster()
