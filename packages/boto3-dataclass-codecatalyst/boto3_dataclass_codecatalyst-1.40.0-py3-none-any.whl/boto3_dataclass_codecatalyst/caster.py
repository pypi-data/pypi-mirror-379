# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_codecatalyst import type_defs as bs_td


class CODECATALYSTCaster:

    def create_access_token(
        self,
        res: "bs_td.CreateAccessTokenResponseTypeDef",
    ) -> "dc_td.CreateAccessTokenResponse":
        return dc_td.CreateAccessTokenResponse.make_one(res)

    def create_dev_environment(
        self,
        res: "bs_td.CreateDevEnvironmentResponseTypeDef",
    ) -> "dc_td.CreateDevEnvironmentResponse":
        return dc_td.CreateDevEnvironmentResponse.make_one(res)

    def create_project(
        self,
        res: "bs_td.CreateProjectResponseTypeDef",
    ) -> "dc_td.CreateProjectResponse":
        return dc_td.CreateProjectResponse.make_one(res)

    def create_source_repository(
        self,
        res: "bs_td.CreateSourceRepositoryResponseTypeDef",
    ) -> "dc_td.CreateSourceRepositoryResponse":
        return dc_td.CreateSourceRepositoryResponse.make_one(res)

    def create_source_repository_branch(
        self,
        res: "bs_td.CreateSourceRepositoryBranchResponseTypeDef",
    ) -> "dc_td.CreateSourceRepositoryBranchResponse":
        return dc_td.CreateSourceRepositoryBranchResponse.make_one(res)

    def delete_dev_environment(
        self,
        res: "bs_td.DeleteDevEnvironmentResponseTypeDef",
    ) -> "dc_td.DeleteDevEnvironmentResponse":
        return dc_td.DeleteDevEnvironmentResponse.make_one(res)

    def delete_project(
        self,
        res: "bs_td.DeleteProjectResponseTypeDef",
    ) -> "dc_td.DeleteProjectResponse":
        return dc_td.DeleteProjectResponse.make_one(res)

    def delete_source_repository(
        self,
        res: "bs_td.DeleteSourceRepositoryResponseTypeDef",
    ) -> "dc_td.DeleteSourceRepositoryResponse":
        return dc_td.DeleteSourceRepositoryResponse.make_one(res)

    def delete_space(
        self,
        res: "bs_td.DeleteSpaceResponseTypeDef",
    ) -> "dc_td.DeleteSpaceResponse":
        return dc_td.DeleteSpaceResponse.make_one(res)

    def get_dev_environment(
        self,
        res: "bs_td.GetDevEnvironmentResponseTypeDef",
    ) -> "dc_td.GetDevEnvironmentResponse":
        return dc_td.GetDevEnvironmentResponse.make_one(res)

    def get_project(
        self,
        res: "bs_td.GetProjectResponseTypeDef",
    ) -> "dc_td.GetProjectResponse":
        return dc_td.GetProjectResponse.make_one(res)

    def get_source_repository(
        self,
        res: "bs_td.GetSourceRepositoryResponseTypeDef",
    ) -> "dc_td.GetSourceRepositoryResponse":
        return dc_td.GetSourceRepositoryResponse.make_one(res)

    def get_source_repository_clone_urls(
        self,
        res: "bs_td.GetSourceRepositoryCloneUrlsResponseTypeDef",
    ) -> "dc_td.GetSourceRepositoryCloneUrlsResponse":
        return dc_td.GetSourceRepositoryCloneUrlsResponse.make_one(res)

    def get_space(
        self,
        res: "bs_td.GetSpaceResponseTypeDef",
    ) -> "dc_td.GetSpaceResponse":
        return dc_td.GetSpaceResponse.make_one(res)

    def get_subscription(
        self,
        res: "bs_td.GetSubscriptionResponseTypeDef",
    ) -> "dc_td.GetSubscriptionResponse":
        return dc_td.GetSubscriptionResponse.make_one(res)

    def get_user_details(
        self,
        res: "bs_td.GetUserDetailsResponseTypeDef",
    ) -> "dc_td.GetUserDetailsResponse":
        return dc_td.GetUserDetailsResponse.make_one(res)

    def get_workflow(
        self,
        res: "bs_td.GetWorkflowResponseTypeDef",
    ) -> "dc_td.GetWorkflowResponse":
        return dc_td.GetWorkflowResponse.make_one(res)

    def get_workflow_run(
        self,
        res: "bs_td.GetWorkflowRunResponseTypeDef",
    ) -> "dc_td.GetWorkflowRunResponse":
        return dc_td.GetWorkflowRunResponse.make_one(res)

    def list_access_tokens(
        self,
        res: "bs_td.ListAccessTokensResponseTypeDef",
    ) -> "dc_td.ListAccessTokensResponse":
        return dc_td.ListAccessTokensResponse.make_one(res)

    def list_dev_environment_sessions(
        self,
        res: "bs_td.ListDevEnvironmentSessionsResponseTypeDef",
    ) -> "dc_td.ListDevEnvironmentSessionsResponse":
        return dc_td.ListDevEnvironmentSessionsResponse.make_one(res)

    def list_dev_environments(
        self,
        res: "bs_td.ListDevEnvironmentsResponseTypeDef",
    ) -> "dc_td.ListDevEnvironmentsResponse":
        return dc_td.ListDevEnvironmentsResponse.make_one(res)

    def list_event_logs(
        self,
        res: "bs_td.ListEventLogsResponseTypeDef",
    ) -> "dc_td.ListEventLogsResponse":
        return dc_td.ListEventLogsResponse.make_one(res)

    def list_projects(
        self,
        res: "bs_td.ListProjectsResponseTypeDef",
    ) -> "dc_td.ListProjectsResponse":
        return dc_td.ListProjectsResponse.make_one(res)

    def list_source_repositories(
        self,
        res: "bs_td.ListSourceRepositoriesResponseTypeDef",
    ) -> "dc_td.ListSourceRepositoriesResponse":
        return dc_td.ListSourceRepositoriesResponse.make_one(res)

    def list_source_repository_branches(
        self,
        res: "bs_td.ListSourceRepositoryBranchesResponseTypeDef",
    ) -> "dc_td.ListSourceRepositoryBranchesResponse":
        return dc_td.ListSourceRepositoryBranchesResponse.make_one(res)

    def list_spaces(
        self,
        res: "bs_td.ListSpacesResponseTypeDef",
    ) -> "dc_td.ListSpacesResponse":
        return dc_td.ListSpacesResponse.make_one(res)

    def list_workflow_runs(
        self,
        res: "bs_td.ListWorkflowRunsResponseTypeDef",
    ) -> "dc_td.ListWorkflowRunsResponse":
        return dc_td.ListWorkflowRunsResponse.make_one(res)

    def list_workflows(
        self,
        res: "bs_td.ListWorkflowsResponseTypeDef",
    ) -> "dc_td.ListWorkflowsResponse":
        return dc_td.ListWorkflowsResponse.make_one(res)

    def start_dev_environment(
        self,
        res: "bs_td.StartDevEnvironmentResponseTypeDef",
    ) -> "dc_td.StartDevEnvironmentResponse":
        return dc_td.StartDevEnvironmentResponse.make_one(res)

    def start_dev_environment_session(
        self,
        res: "bs_td.StartDevEnvironmentSessionResponseTypeDef",
    ) -> "dc_td.StartDevEnvironmentSessionResponse":
        return dc_td.StartDevEnvironmentSessionResponse.make_one(res)

    def start_workflow_run(
        self,
        res: "bs_td.StartWorkflowRunResponseTypeDef",
    ) -> "dc_td.StartWorkflowRunResponse":
        return dc_td.StartWorkflowRunResponse.make_one(res)

    def stop_dev_environment(
        self,
        res: "bs_td.StopDevEnvironmentResponseTypeDef",
    ) -> "dc_td.StopDevEnvironmentResponse":
        return dc_td.StopDevEnvironmentResponse.make_one(res)

    def stop_dev_environment_session(
        self,
        res: "bs_td.StopDevEnvironmentSessionResponseTypeDef",
    ) -> "dc_td.StopDevEnvironmentSessionResponse":
        return dc_td.StopDevEnvironmentSessionResponse.make_one(res)

    def update_dev_environment(
        self,
        res: "bs_td.UpdateDevEnvironmentResponseTypeDef",
    ) -> "dc_td.UpdateDevEnvironmentResponse":
        return dc_td.UpdateDevEnvironmentResponse.make_one(res)

    def update_project(
        self,
        res: "bs_td.UpdateProjectResponseTypeDef",
    ) -> "dc_td.UpdateProjectResponse":
        return dc_td.UpdateProjectResponse.make_one(res)

    def update_space(
        self,
        res: "bs_td.UpdateSpaceResponseTypeDef",
    ) -> "dc_td.UpdateSpaceResponse":
        return dc_td.UpdateSpaceResponse.make_one(res)

    def verify_session(
        self,
        res: "bs_td.VerifySessionResponseTypeDef",
    ) -> "dc_td.VerifySessionResponse":
        return dc_td.VerifySessionResponse.make_one(res)


codecatalyst_caster = CODECATALYSTCaster()
