# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_batch import type_defs as bs_td


class BATCHCaster:

    def create_compute_environment(
        self,
        res: "bs_td.CreateComputeEnvironmentResponseTypeDef",
    ) -> "dc_td.CreateComputeEnvironmentResponse":
        return dc_td.CreateComputeEnvironmentResponse.make_one(res)

    def create_consumable_resource(
        self,
        res: "bs_td.CreateConsumableResourceResponseTypeDef",
    ) -> "dc_td.CreateConsumableResourceResponse":
        return dc_td.CreateConsumableResourceResponse.make_one(res)

    def create_job_queue(
        self,
        res: "bs_td.CreateJobQueueResponseTypeDef",
    ) -> "dc_td.CreateJobQueueResponse":
        return dc_td.CreateJobQueueResponse.make_one(res)

    def create_scheduling_policy(
        self,
        res: "bs_td.CreateSchedulingPolicyResponseTypeDef",
    ) -> "dc_td.CreateSchedulingPolicyResponse":
        return dc_td.CreateSchedulingPolicyResponse.make_one(res)

    def create_service_environment(
        self,
        res: "bs_td.CreateServiceEnvironmentResponseTypeDef",
    ) -> "dc_td.CreateServiceEnvironmentResponse":
        return dc_td.CreateServiceEnvironmentResponse.make_one(res)

    def describe_compute_environments(
        self,
        res: "bs_td.DescribeComputeEnvironmentsResponseTypeDef",
    ) -> "dc_td.DescribeComputeEnvironmentsResponse":
        return dc_td.DescribeComputeEnvironmentsResponse.make_one(res)

    def describe_consumable_resource(
        self,
        res: "bs_td.DescribeConsumableResourceResponseTypeDef",
    ) -> "dc_td.DescribeConsumableResourceResponse":
        return dc_td.DescribeConsumableResourceResponse.make_one(res)

    def describe_job_definitions(
        self,
        res: "bs_td.DescribeJobDefinitionsResponseTypeDef",
    ) -> "dc_td.DescribeJobDefinitionsResponse":
        return dc_td.DescribeJobDefinitionsResponse.make_one(res)

    def describe_job_queues(
        self,
        res: "bs_td.DescribeJobQueuesResponseTypeDef",
    ) -> "dc_td.DescribeJobQueuesResponse":
        return dc_td.DescribeJobQueuesResponse.make_one(res)

    def describe_jobs(
        self,
        res: "bs_td.DescribeJobsResponseTypeDef",
    ) -> "dc_td.DescribeJobsResponse":
        return dc_td.DescribeJobsResponse.make_one(res)

    def describe_scheduling_policies(
        self,
        res: "bs_td.DescribeSchedulingPoliciesResponseTypeDef",
    ) -> "dc_td.DescribeSchedulingPoliciesResponse":
        return dc_td.DescribeSchedulingPoliciesResponse.make_one(res)

    def describe_service_environments(
        self,
        res: "bs_td.DescribeServiceEnvironmentsResponseTypeDef",
    ) -> "dc_td.DescribeServiceEnvironmentsResponse":
        return dc_td.DescribeServiceEnvironmentsResponse.make_one(res)

    def describe_service_job(
        self,
        res: "bs_td.DescribeServiceJobResponseTypeDef",
    ) -> "dc_td.DescribeServiceJobResponse":
        return dc_td.DescribeServiceJobResponse.make_one(res)

    def get_job_queue_snapshot(
        self,
        res: "bs_td.GetJobQueueSnapshotResponseTypeDef",
    ) -> "dc_td.GetJobQueueSnapshotResponse":
        return dc_td.GetJobQueueSnapshotResponse.make_one(res)

    def list_consumable_resources(
        self,
        res: "bs_td.ListConsumableResourcesResponseTypeDef",
    ) -> "dc_td.ListConsumableResourcesResponse":
        return dc_td.ListConsumableResourcesResponse.make_one(res)

    def list_jobs(
        self,
        res: "bs_td.ListJobsResponseTypeDef",
    ) -> "dc_td.ListJobsResponse":
        return dc_td.ListJobsResponse.make_one(res)

    def list_jobs_by_consumable_resource(
        self,
        res: "bs_td.ListJobsByConsumableResourceResponseTypeDef",
    ) -> "dc_td.ListJobsByConsumableResourceResponse":
        return dc_td.ListJobsByConsumableResourceResponse.make_one(res)

    def list_scheduling_policies(
        self,
        res: "bs_td.ListSchedulingPoliciesResponseTypeDef",
    ) -> "dc_td.ListSchedulingPoliciesResponse":
        return dc_td.ListSchedulingPoliciesResponse.make_one(res)

    def list_service_jobs(
        self,
        res: "bs_td.ListServiceJobsResponseTypeDef",
    ) -> "dc_td.ListServiceJobsResponse":
        return dc_td.ListServiceJobsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def register_job_definition(
        self,
        res: "bs_td.RegisterJobDefinitionResponseTypeDef",
    ) -> "dc_td.RegisterJobDefinitionResponse":
        return dc_td.RegisterJobDefinitionResponse.make_one(res)

    def submit_job(
        self,
        res: "bs_td.SubmitJobResponseTypeDef",
    ) -> "dc_td.SubmitJobResponse":
        return dc_td.SubmitJobResponse.make_one(res)

    def submit_service_job(
        self,
        res: "bs_td.SubmitServiceJobResponseTypeDef",
    ) -> "dc_td.SubmitServiceJobResponse":
        return dc_td.SubmitServiceJobResponse.make_one(res)

    def update_compute_environment(
        self,
        res: "bs_td.UpdateComputeEnvironmentResponseTypeDef",
    ) -> "dc_td.UpdateComputeEnvironmentResponse":
        return dc_td.UpdateComputeEnvironmentResponse.make_one(res)

    def update_consumable_resource(
        self,
        res: "bs_td.UpdateConsumableResourceResponseTypeDef",
    ) -> "dc_td.UpdateConsumableResourceResponse":
        return dc_td.UpdateConsumableResourceResponse.make_one(res)

    def update_job_queue(
        self,
        res: "bs_td.UpdateJobQueueResponseTypeDef",
    ) -> "dc_td.UpdateJobQueueResponse":
        return dc_td.UpdateJobQueueResponse.make_one(res)

    def update_service_environment(
        self,
        res: "bs_td.UpdateServiceEnvironmentResponseTypeDef",
    ) -> "dc_td.UpdateServiceEnvironmentResponse":
        return dc_td.UpdateServiceEnvironmentResponse.make_one(res)


batch_caster = BATCHCaster()
