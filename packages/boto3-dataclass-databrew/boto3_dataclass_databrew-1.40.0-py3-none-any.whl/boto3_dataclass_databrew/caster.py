# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_databrew import type_defs as bs_td


class DATABREWCaster:

    def batch_delete_recipe_version(
        self,
        res: "bs_td.BatchDeleteRecipeVersionResponseTypeDef",
    ) -> "dc_td.BatchDeleteRecipeVersionResponse":
        return dc_td.BatchDeleteRecipeVersionResponse.make_one(res)

    def create_dataset(
        self,
        res: "bs_td.CreateDatasetResponseTypeDef",
    ) -> "dc_td.CreateDatasetResponse":
        return dc_td.CreateDatasetResponse.make_one(res)

    def create_profile_job(
        self,
        res: "bs_td.CreateProfileJobResponseTypeDef",
    ) -> "dc_td.CreateProfileJobResponse":
        return dc_td.CreateProfileJobResponse.make_one(res)

    def create_project(
        self,
        res: "bs_td.CreateProjectResponseTypeDef",
    ) -> "dc_td.CreateProjectResponse":
        return dc_td.CreateProjectResponse.make_one(res)

    def create_recipe(
        self,
        res: "bs_td.CreateRecipeResponseTypeDef",
    ) -> "dc_td.CreateRecipeResponse":
        return dc_td.CreateRecipeResponse.make_one(res)

    def create_recipe_job(
        self,
        res: "bs_td.CreateRecipeJobResponseTypeDef",
    ) -> "dc_td.CreateRecipeJobResponse":
        return dc_td.CreateRecipeJobResponse.make_one(res)

    def create_ruleset(
        self,
        res: "bs_td.CreateRulesetResponseTypeDef",
    ) -> "dc_td.CreateRulesetResponse":
        return dc_td.CreateRulesetResponse.make_one(res)

    def create_schedule(
        self,
        res: "bs_td.CreateScheduleResponseTypeDef",
    ) -> "dc_td.CreateScheduleResponse":
        return dc_td.CreateScheduleResponse.make_one(res)

    def delete_dataset(
        self,
        res: "bs_td.DeleteDatasetResponseTypeDef",
    ) -> "dc_td.DeleteDatasetResponse":
        return dc_td.DeleteDatasetResponse.make_one(res)

    def delete_job(
        self,
        res: "bs_td.DeleteJobResponseTypeDef",
    ) -> "dc_td.DeleteJobResponse":
        return dc_td.DeleteJobResponse.make_one(res)

    def delete_project(
        self,
        res: "bs_td.DeleteProjectResponseTypeDef",
    ) -> "dc_td.DeleteProjectResponse":
        return dc_td.DeleteProjectResponse.make_one(res)

    def delete_recipe_version(
        self,
        res: "bs_td.DeleteRecipeVersionResponseTypeDef",
    ) -> "dc_td.DeleteRecipeVersionResponse":
        return dc_td.DeleteRecipeVersionResponse.make_one(res)

    def delete_ruleset(
        self,
        res: "bs_td.DeleteRulesetResponseTypeDef",
    ) -> "dc_td.DeleteRulesetResponse":
        return dc_td.DeleteRulesetResponse.make_one(res)

    def delete_schedule(
        self,
        res: "bs_td.DeleteScheduleResponseTypeDef",
    ) -> "dc_td.DeleteScheduleResponse":
        return dc_td.DeleteScheduleResponse.make_one(res)

    def describe_dataset(
        self,
        res: "bs_td.DescribeDatasetResponseTypeDef",
    ) -> "dc_td.DescribeDatasetResponse":
        return dc_td.DescribeDatasetResponse.make_one(res)

    def describe_job(
        self,
        res: "bs_td.DescribeJobResponseTypeDef",
    ) -> "dc_td.DescribeJobResponse":
        return dc_td.DescribeJobResponse.make_one(res)

    def describe_job_run(
        self,
        res: "bs_td.DescribeJobRunResponseTypeDef",
    ) -> "dc_td.DescribeJobRunResponse":
        return dc_td.DescribeJobRunResponse.make_one(res)

    def describe_project(
        self,
        res: "bs_td.DescribeProjectResponseTypeDef",
    ) -> "dc_td.DescribeProjectResponse":
        return dc_td.DescribeProjectResponse.make_one(res)

    def describe_recipe(
        self,
        res: "bs_td.DescribeRecipeResponseTypeDef",
    ) -> "dc_td.DescribeRecipeResponse":
        return dc_td.DescribeRecipeResponse.make_one(res)

    def describe_ruleset(
        self,
        res: "bs_td.DescribeRulesetResponseTypeDef",
    ) -> "dc_td.DescribeRulesetResponse":
        return dc_td.DescribeRulesetResponse.make_one(res)

    def describe_schedule(
        self,
        res: "bs_td.DescribeScheduleResponseTypeDef",
    ) -> "dc_td.DescribeScheduleResponse":
        return dc_td.DescribeScheduleResponse.make_one(res)

    def list_datasets(
        self,
        res: "bs_td.ListDatasetsResponseTypeDef",
    ) -> "dc_td.ListDatasetsResponse":
        return dc_td.ListDatasetsResponse.make_one(res)

    def list_job_runs(
        self,
        res: "bs_td.ListJobRunsResponseTypeDef",
    ) -> "dc_td.ListJobRunsResponse":
        return dc_td.ListJobRunsResponse.make_one(res)

    def list_jobs(
        self,
        res: "bs_td.ListJobsResponseTypeDef",
    ) -> "dc_td.ListJobsResponse":
        return dc_td.ListJobsResponse.make_one(res)

    def list_projects(
        self,
        res: "bs_td.ListProjectsResponseTypeDef",
    ) -> "dc_td.ListProjectsResponse":
        return dc_td.ListProjectsResponse.make_one(res)

    def list_recipe_versions(
        self,
        res: "bs_td.ListRecipeVersionsResponseTypeDef",
    ) -> "dc_td.ListRecipeVersionsResponse":
        return dc_td.ListRecipeVersionsResponse.make_one(res)

    def list_recipes(
        self,
        res: "bs_td.ListRecipesResponseTypeDef",
    ) -> "dc_td.ListRecipesResponse":
        return dc_td.ListRecipesResponse.make_one(res)

    def list_rulesets(
        self,
        res: "bs_td.ListRulesetsResponseTypeDef",
    ) -> "dc_td.ListRulesetsResponse":
        return dc_td.ListRulesetsResponse.make_one(res)

    def list_schedules(
        self,
        res: "bs_td.ListSchedulesResponseTypeDef",
    ) -> "dc_td.ListSchedulesResponse":
        return dc_td.ListSchedulesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def publish_recipe(
        self,
        res: "bs_td.PublishRecipeResponseTypeDef",
    ) -> "dc_td.PublishRecipeResponse":
        return dc_td.PublishRecipeResponse.make_one(res)

    def send_project_session_action(
        self,
        res: "bs_td.SendProjectSessionActionResponseTypeDef",
    ) -> "dc_td.SendProjectSessionActionResponse":
        return dc_td.SendProjectSessionActionResponse.make_one(res)

    def start_job_run(
        self,
        res: "bs_td.StartJobRunResponseTypeDef",
    ) -> "dc_td.StartJobRunResponse":
        return dc_td.StartJobRunResponse.make_one(res)

    def start_project_session(
        self,
        res: "bs_td.StartProjectSessionResponseTypeDef",
    ) -> "dc_td.StartProjectSessionResponse":
        return dc_td.StartProjectSessionResponse.make_one(res)

    def stop_job_run(
        self,
        res: "bs_td.StopJobRunResponseTypeDef",
    ) -> "dc_td.StopJobRunResponse":
        return dc_td.StopJobRunResponse.make_one(res)

    def update_dataset(
        self,
        res: "bs_td.UpdateDatasetResponseTypeDef",
    ) -> "dc_td.UpdateDatasetResponse":
        return dc_td.UpdateDatasetResponse.make_one(res)

    def update_profile_job(
        self,
        res: "bs_td.UpdateProfileJobResponseTypeDef",
    ) -> "dc_td.UpdateProfileJobResponse":
        return dc_td.UpdateProfileJobResponse.make_one(res)

    def update_project(
        self,
        res: "bs_td.UpdateProjectResponseTypeDef",
    ) -> "dc_td.UpdateProjectResponse":
        return dc_td.UpdateProjectResponse.make_one(res)

    def update_recipe(
        self,
        res: "bs_td.UpdateRecipeResponseTypeDef",
    ) -> "dc_td.UpdateRecipeResponse":
        return dc_td.UpdateRecipeResponse.make_one(res)

    def update_recipe_job(
        self,
        res: "bs_td.UpdateRecipeJobResponseTypeDef",
    ) -> "dc_td.UpdateRecipeJobResponse":
        return dc_td.UpdateRecipeJobResponse.make_one(res)

    def update_ruleset(
        self,
        res: "bs_td.UpdateRulesetResponseTypeDef",
    ) -> "dc_td.UpdateRulesetResponse":
        return dc_td.UpdateRulesetResponse.make_one(res)

    def update_schedule(
        self,
        res: "bs_td.UpdateScheduleResponseTypeDef",
    ) -> "dc_td.UpdateScheduleResponse":
        return dc_td.UpdateScheduleResponse.make_one(res)


databrew_caster = DATABREWCaster()
