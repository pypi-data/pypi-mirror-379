# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_deadline import type_defs as bs_td


class DEADLINECaster:

    def assume_fleet_role_for_read(
        self,
        res: "bs_td.AssumeFleetRoleForReadResponseTypeDef",
    ) -> "dc_td.AssumeFleetRoleForReadResponse":
        return dc_td.AssumeFleetRoleForReadResponse.make_one(res)

    def assume_fleet_role_for_worker(
        self,
        res: "bs_td.AssumeFleetRoleForWorkerResponseTypeDef",
    ) -> "dc_td.AssumeFleetRoleForWorkerResponse":
        return dc_td.AssumeFleetRoleForWorkerResponse.make_one(res)

    def assume_queue_role_for_read(
        self,
        res: "bs_td.AssumeQueueRoleForReadResponseTypeDef",
    ) -> "dc_td.AssumeQueueRoleForReadResponse":
        return dc_td.AssumeQueueRoleForReadResponse.make_one(res)

    def assume_queue_role_for_user(
        self,
        res: "bs_td.AssumeQueueRoleForUserResponseTypeDef",
    ) -> "dc_td.AssumeQueueRoleForUserResponse":
        return dc_td.AssumeQueueRoleForUserResponse.make_one(res)

    def assume_queue_role_for_worker(
        self,
        res: "bs_td.AssumeQueueRoleForWorkerResponseTypeDef",
    ) -> "dc_td.AssumeQueueRoleForWorkerResponse":
        return dc_td.AssumeQueueRoleForWorkerResponse.make_one(res)

    def batch_get_job_entity(
        self,
        res: "bs_td.BatchGetJobEntityResponseTypeDef",
    ) -> "dc_td.BatchGetJobEntityResponse":
        return dc_td.BatchGetJobEntityResponse.make_one(res)

    def copy_job_template(
        self,
        res: "bs_td.CopyJobTemplateResponseTypeDef",
    ) -> "dc_td.CopyJobTemplateResponse":
        return dc_td.CopyJobTemplateResponse.make_one(res)

    def create_budget(
        self,
        res: "bs_td.CreateBudgetResponseTypeDef",
    ) -> "dc_td.CreateBudgetResponse":
        return dc_td.CreateBudgetResponse.make_one(res)

    def create_farm(
        self,
        res: "bs_td.CreateFarmResponseTypeDef",
    ) -> "dc_td.CreateFarmResponse":
        return dc_td.CreateFarmResponse.make_one(res)

    def create_fleet(
        self,
        res: "bs_td.CreateFleetResponseTypeDef",
    ) -> "dc_td.CreateFleetResponse":
        return dc_td.CreateFleetResponse.make_one(res)

    def create_job(
        self,
        res: "bs_td.CreateJobResponseTypeDef",
    ) -> "dc_td.CreateJobResponse":
        return dc_td.CreateJobResponse.make_one(res)

    def create_license_endpoint(
        self,
        res: "bs_td.CreateLicenseEndpointResponseTypeDef",
    ) -> "dc_td.CreateLicenseEndpointResponse":
        return dc_td.CreateLicenseEndpointResponse.make_one(res)

    def create_limit(
        self,
        res: "bs_td.CreateLimitResponseTypeDef",
    ) -> "dc_td.CreateLimitResponse":
        return dc_td.CreateLimitResponse.make_one(res)

    def create_monitor(
        self,
        res: "bs_td.CreateMonitorResponseTypeDef",
    ) -> "dc_td.CreateMonitorResponse":
        return dc_td.CreateMonitorResponse.make_one(res)

    def create_queue(
        self,
        res: "bs_td.CreateQueueResponseTypeDef",
    ) -> "dc_td.CreateQueueResponse":
        return dc_td.CreateQueueResponse.make_one(res)

    def create_queue_environment(
        self,
        res: "bs_td.CreateQueueEnvironmentResponseTypeDef",
    ) -> "dc_td.CreateQueueEnvironmentResponse":
        return dc_td.CreateQueueEnvironmentResponse.make_one(res)

    def create_storage_profile(
        self,
        res: "bs_td.CreateStorageProfileResponseTypeDef",
    ) -> "dc_td.CreateStorageProfileResponse":
        return dc_td.CreateStorageProfileResponse.make_one(res)

    def create_worker(
        self,
        res: "bs_td.CreateWorkerResponseTypeDef",
    ) -> "dc_td.CreateWorkerResponse":
        return dc_td.CreateWorkerResponse.make_one(res)

    def get_budget(
        self,
        res: "bs_td.GetBudgetResponseTypeDef",
    ) -> "dc_td.GetBudgetResponse":
        return dc_td.GetBudgetResponse.make_one(res)

    def get_farm(
        self,
        res: "bs_td.GetFarmResponseTypeDef",
    ) -> "dc_td.GetFarmResponse":
        return dc_td.GetFarmResponse.make_one(res)

    def get_fleet(
        self,
        res: "bs_td.GetFleetResponseTypeDef",
    ) -> "dc_td.GetFleetResponse":
        return dc_td.GetFleetResponse.make_one(res)

    def get_job(
        self,
        res: "bs_td.GetJobResponseTypeDef",
    ) -> "dc_td.GetJobResponse":
        return dc_td.GetJobResponse.make_one(res)

    def get_license_endpoint(
        self,
        res: "bs_td.GetLicenseEndpointResponseTypeDef",
    ) -> "dc_td.GetLicenseEndpointResponse":
        return dc_td.GetLicenseEndpointResponse.make_one(res)

    def get_limit(
        self,
        res: "bs_td.GetLimitResponseTypeDef",
    ) -> "dc_td.GetLimitResponse":
        return dc_td.GetLimitResponse.make_one(res)

    def get_monitor(
        self,
        res: "bs_td.GetMonitorResponseTypeDef",
    ) -> "dc_td.GetMonitorResponse":
        return dc_td.GetMonitorResponse.make_one(res)

    def get_queue(
        self,
        res: "bs_td.GetQueueResponseTypeDef",
    ) -> "dc_td.GetQueueResponse":
        return dc_td.GetQueueResponse.make_one(res)

    def get_queue_environment(
        self,
        res: "bs_td.GetQueueEnvironmentResponseTypeDef",
    ) -> "dc_td.GetQueueEnvironmentResponse":
        return dc_td.GetQueueEnvironmentResponse.make_one(res)

    def get_queue_fleet_association(
        self,
        res: "bs_td.GetQueueFleetAssociationResponseTypeDef",
    ) -> "dc_td.GetQueueFleetAssociationResponse":
        return dc_td.GetQueueFleetAssociationResponse.make_one(res)

    def get_queue_limit_association(
        self,
        res: "bs_td.GetQueueLimitAssociationResponseTypeDef",
    ) -> "dc_td.GetQueueLimitAssociationResponse":
        return dc_td.GetQueueLimitAssociationResponse.make_one(res)

    def get_session(
        self,
        res: "bs_td.GetSessionResponseTypeDef",
    ) -> "dc_td.GetSessionResponse":
        return dc_td.GetSessionResponse.make_one(res)

    def get_session_action(
        self,
        res: "bs_td.GetSessionActionResponseTypeDef",
    ) -> "dc_td.GetSessionActionResponse":
        return dc_td.GetSessionActionResponse.make_one(res)

    def get_sessions_statistics_aggregation(
        self,
        res: "bs_td.GetSessionsStatisticsAggregationResponseTypeDef",
    ) -> "dc_td.GetSessionsStatisticsAggregationResponse":
        return dc_td.GetSessionsStatisticsAggregationResponse.make_one(res)

    def get_step(
        self,
        res: "bs_td.GetStepResponseTypeDef",
    ) -> "dc_td.GetStepResponse":
        return dc_td.GetStepResponse.make_one(res)

    def get_storage_profile(
        self,
        res: "bs_td.GetStorageProfileResponseTypeDef",
    ) -> "dc_td.GetStorageProfileResponse":
        return dc_td.GetStorageProfileResponse.make_one(res)

    def get_storage_profile_for_queue(
        self,
        res: "bs_td.GetStorageProfileForQueueResponseTypeDef",
    ) -> "dc_td.GetStorageProfileForQueueResponse":
        return dc_td.GetStorageProfileForQueueResponse.make_one(res)

    def get_task(
        self,
        res: "bs_td.GetTaskResponseTypeDef",
    ) -> "dc_td.GetTaskResponse":
        return dc_td.GetTaskResponse.make_one(res)

    def get_worker(
        self,
        res: "bs_td.GetWorkerResponseTypeDef",
    ) -> "dc_td.GetWorkerResponse":
        return dc_td.GetWorkerResponse.make_one(res)

    def list_available_metered_products(
        self,
        res: "bs_td.ListAvailableMeteredProductsResponseTypeDef",
    ) -> "dc_td.ListAvailableMeteredProductsResponse":
        return dc_td.ListAvailableMeteredProductsResponse.make_one(res)

    def list_budgets(
        self,
        res: "bs_td.ListBudgetsResponseTypeDef",
    ) -> "dc_td.ListBudgetsResponse":
        return dc_td.ListBudgetsResponse.make_one(res)

    def list_farm_members(
        self,
        res: "bs_td.ListFarmMembersResponseTypeDef",
    ) -> "dc_td.ListFarmMembersResponse":
        return dc_td.ListFarmMembersResponse.make_one(res)

    def list_farms(
        self,
        res: "bs_td.ListFarmsResponseTypeDef",
    ) -> "dc_td.ListFarmsResponse":
        return dc_td.ListFarmsResponse.make_one(res)

    def list_fleet_members(
        self,
        res: "bs_td.ListFleetMembersResponseTypeDef",
    ) -> "dc_td.ListFleetMembersResponse":
        return dc_td.ListFleetMembersResponse.make_one(res)

    def list_fleets(
        self,
        res: "bs_td.ListFleetsResponseTypeDef",
    ) -> "dc_td.ListFleetsResponse":
        return dc_td.ListFleetsResponse.make_one(res)

    def list_job_members(
        self,
        res: "bs_td.ListJobMembersResponseTypeDef",
    ) -> "dc_td.ListJobMembersResponse":
        return dc_td.ListJobMembersResponse.make_one(res)

    def list_job_parameter_definitions(
        self,
        res: "bs_td.ListJobParameterDefinitionsResponseTypeDef",
    ) -> "dc_td.ListJobParameterDefinitionsResponse":
        return dc_td.ListJobParameterDefinitionsResponse.make_one(res)

    def list_jobs(
        self,
        res: "bs_td.ListJobsResponseTypeDef",
    ) -> "dc_td.ListJobsResponse":
        return dc_td.ListJobsResponse.make_one(res)

    def list_license_endpoints(
        self,
        res: "bs_td.ListLicenseEndpointsResponseTypeDef",
    ) -> "dc_td.ListLicenseEndpointsResponse":
        return dc_td.ListLicenseEndpointsResponse.make_one(res)

    def list_limits(
        self,
        res: "bs_td.ListLimitsResponseTypeDef",
    ) -> "dc_td.ListLimitsResponse":
        return dc_td.ListLimitsResponse.make_one(res)

    def list_metered_products(
        self,
        res: "bs_td.ListMeteredProductsResponseTypeDef",
    ) -> "dc_td.ListMeteredProductsResponse":
        return dc_td.ListMeteredProductsResponse.make_one(res)

    def list_monitors(
        self,
        res: "bs_td.ListMonitorsResponseTypeDef",
    ) -> "dc_td.ListMonitorsResponse":
        return dc_td.ListMonitorsResponse.make_one(res)

    def list_queue_environments(
        self,
        res: "bs_td.ListQueueEnvironmentsResponseTypeDef",
    ) -> "dc_td.ListQueueEnvironmentsResponse":
        return dc_td.ListQueueEnvironmentsResponse.make_one(res)

    def list_queue_fleet_associations(
        self,
        res: "bs_td.ListQueueFleetAssociationsResponseTypeDef",
    ) -> "dc_td.ListQueueFleetAssociationsResponse":
        return dc_td.ListQueueFleetAssociationsResponse.make_one(res)

    def list_queue_limit_associations(
        self,
        res: "bs_td.ListQueueLimitAssociationsResponseTypeDef",
    ) -> "dc_td.ListQueueLimitAssociationsResponse":
        return dc_td.ListQueueLimitAssociationsResponse.make_one(res)

    def list_queue_members(
        self,
        res: "bs_td.ListQueueMembersResponseTypeDef",
    ) -> "dc_td.ListQueueMembersResponse":
        return dc_td.ListQueueMembersResponse.make_one(res)

    def list_queues(
        self,
        res: "bs_td.ListQueuesResponseTypeDef",
    ) -> "dc_td.ListQueuesResponse":
        return dc_td.ListQueuesResponse.make_one(res)

    def list_session_actions(
        self,
        res: "bs_td.ListSessionActionsResponseTypeDef",
    ) -> "dc_td.ListSessionActionsResponse":
        return dc_td.ListSessionActionsResponse.make_one(res)

    def list_sessions(
        self,
        res: "bs_td.ListSessionsResponseTypeDef",
    ) -> "dc_td.ListSessionsResponse":
        return dc_td.ListSessionsResponse.make_one(res)

    def list_sessions_for_worker(
        self,
        res: "bs_td.ListSessionsForWorkerResponseTypeDef",
    ) -> "dc_td.ListSessionsForWorkerResponse":
        return dc_td.ListSessionsForWorkerResponse.make_one(res)

    def list_step_consumers(
        self,
        res: "bs_td.ListStepConsumersResponseTypeDef",
    ) -> "dc_td.ListStepConsumersResponse":
        return dc_td.ListStepConsumersResponse.make_one(res)

    def list_step_dependencies(
        self,
        res: "bs_td.ListStepDependenciesResponseTypeDef",
    ) -> "dc_td.ListStepDependenciesResponse":
        return dc_td.ListStepDependenciesResponse.make_one(res)

    def list_steps(
        self,
        res: "bs_td.ListStepsResponseTypeDef",
    ) -> "dc_td.ListStepsResponse":
        return dc_td.ListStepsResponse.make_one(res)

    def list_storage_profiles(
        self,
        res: "bs_td.ListStorageProfilesResponseTypeDef",
    ) -> "dc_td.ListStorageProfilesResponse":
        return dc_td.ListStorageProfilesResponse.make_one(res)

    def list_storage_profiles_for_queue(
        self,
        res: "bs_td.ListStorageProfilesForQueueResponseTypeDef",
    ) -> "dc_td.ListStorageProfilesForQueueResponse":
        return dc_td.ListStorageProfilesForQueueResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_tasks(
        self,
        res: "bs_td.ListTasksResponseTypeDef",
    ) -> "dc_td.ListTasksResponse":
        return dc_td.ListTasksResponse.make_one(res)

    def list_workers(
        self,
        res: "bs_td.ListWorkersResponseTypeDef",
    ) -> "dc_td.ListWorkersResponse":
        return dc_td.ListWorkersResponse.make_one(res)

    def search_jobs(
        self,
        res: "bs_td.SearchJobsResponseTypeDef",
    ) -> "dc_td.SearchJobsResponse":
        return dc_td.SearchJobsResponse.make_one(res)

    def search_steps(
        self,
        res: "bs_td.SearchStepsResponseTypeDef",
    ) -> "dc_td.SearchStepsResponse":
        return dc_td.SearchStepsResponse.make_one(res)

    def search_tasks(
        self,
        res: "bs_td.SearchTasksResponseTypeDef",
    ) -> "dc_td.SearchTasksResponse":
        return dc_td.SearchTasksResponse.make_one(res)

    def search_workers(
        self,
        res: "bs_td.SearchWorkersResponseTypeDef",
    ) -> "dc_td.SearchWorkersResponse":
        return dc_td.SearchWorkersResponse.make_one(res)

    def start_sessions_statistics_aggregation(
        self,
        res: "bs_td.StartSessionsStatisticsAggregationResponseTypeDef",
    ) -> "dc_td.StartSessionsStatisticsAggregationResponse":
        return dc_td.StartSessionsStatisticsAggregationResponse.make_one(res)

    def update_worker(
        self,
        res: "bs_td.UpdateWorkerResponseTypeDef",
    ) -> "dc_td.UpdateWorkerResponse":
        return dc_td.UpdateWorkerResponse.make_one(res)

    def update_worker_schedule(
        self,
        res: "bs_td.UpdateWorkerScheduleResponseTypeDef",
    ) -> "dc_td.UpdateWorkerScheduleResponse":
        return dc_td.UpdateWorkerScheduleResponse.make_one(res)


deadline_caster = DEADLINECaster()
