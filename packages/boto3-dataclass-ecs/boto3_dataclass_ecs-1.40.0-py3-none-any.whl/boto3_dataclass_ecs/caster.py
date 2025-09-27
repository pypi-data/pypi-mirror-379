# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ecs import type_defs as bs_td


class ECSCaster:

    def create_capacity_provider(
        self,
        res: "bs_td.CreateCapacityProviderResponseTypeDef",
    ) -> "dc_td.CreateCapacityProviderResponse":
        return dc_td.CreateCapacityProviderResponse.make_one(res)

    def create_cluster(
        self,
        res: "bs_td.CreateClusterResponseTypeDef",
    ) -> "dc_td.CreateClusterResponse":
        return dc_td.CreateClusterResponse.make_one(res)

    def create_service(
        self,
        res: "bs_td.CreateServiceResponseTypeDef",
    ) -> "dc_td.CreateServiceResponse":
        return dc_td.CreateServiceResponse.make_one(res)

    def create_task_set(
        self,
        res: "bs_td.CreateTaskSetResponseTypeDef",
    ) -> "dc_td.CreateTaskSetResponse":
        return dc_td.CreateTaskSetResponse.make_one(res)

    def delete_account_setting(
        self,
        res: "bs_td.DeleteAccountSettingResponseTypeDef",
    ) -> "dc_td.DeleteAccountSettingResponse":
        return dc_td.DeleteAccountSettingResponse.make_one(res)

    def delete_attributes(
        self,
        res: "bs_td.DeleteAttributesResponseTypeDef",
    ) -> "dc_td.DeleteAttributesResponse":
        return dc_td.DeleteAttributesResponse.make_one(res)

    def delete_capacity_provider(
        self,
        res: "bs_td.DeleteCapacityProviderResponseTypeDef",
    ) -> "dc_td.DeleteCapacityProviderResponse":
        return dc_td.DeleteCapacityProviderResponse.make_one(res)

    def delete_cluster(
        self,
        res: "bs_td.DeleteClusterResponseTypeDef",
    ) -> "dc_td.DeleteClusterResponse":
        return dc_td.DeleteClusterResponse.make_one(res)

    def delete_service(
        self,
        res: "bs_td.DeleteServiceResponseTypeDef",
    ) -> "dc_td.DeleteServiceResponse":
        return dc_td.DeleteServiceResponse.make_one(res)

    def delete_task_definitions(
        self,
        res: "bs_td.DeleteTaskDefinitionsResponseTypeDef",
    ) -> "dc_td.DeleteTaskDefinitionsResponse":
        return dc_td.DeleteTaskDefinitionsResponse.make_one(res)

    def delete_task_set(
        self,
        res: "bs_td.DeleteTaskSetResponseTypeDef",
    ) -> "dc_td.DeleteTaskSetResponse":
        return dc_td.DeleteTaskSetResponse.make_one(res)

    def deregister_container_instance(
        self,
        res: "bs_td.DeregisterContainerInstanceResponseTypeDef",
    ) -> "dc_td.DeregisterContainerInstanceResponse":
        return dc_td.DeregisterContainerInstanceResponse.make_one(res)

    def deregister_task_definition(
        self,
        res: "bs_td.DeregisterTaskDefinitionResponseTypeDef",
    ) -> "dc_td.DeregisterTaskDefinitionResponse":
        return dc_td.DeregisterTaskDefinitionResponse.make_one(res)

    def describe_capacity_providers(
        self,
        res: "bs_td.DescribeCapacityProvidersResponseTypeDef",
    ) -> "dc_td.DescribeCapacityProvidersResponse":
        return dc_td.DescribeCapacityProvidersResponse.make_one(res)

    def describe_clusters(
        self,
        res: "bs_td.DescribeClustersResponseTypeDef",
    ) -> "dc_td.DescribeClustersResponse":
        return dc_td.DescribeClustersResponse.make_one(res)

    def describe_container_instances(
        self,
        res: "bs_td.DescribeContainerInstancesResponseTypeDef",
    ) -> "dc_td.DescribeContainerInstancesResponse":
        return dc_td.DescribeContainerInstancesResponse.make_one(res)

    def describe_service_deployments(
        self,
        res: "bs_td.DescribeServiceDeploymentsResponseTypeDef",
    ) -> "dc_td.DescribeServiceDeploymentsResponse":
        return dc_td.DescribeServiceDeploymentsResponse.make_one(res)

    def describe_service_revisions(
        self,
        res: "bs_td.DescribeServiceRevisionsResponseTypeDef",
    ) -> "dc_td.DescribeServiceRevisionsResponse":
        return dc_td.DescribeServiceRevisionsResponse.make_one(res)

    def describe_services(
        self,
        res: "bs_td.DescribeServicesResponseTypeDef",
    ) -> "dc_td.DescribeServicesResponse":
        return dc_td.DescribeServicesResponse.make_one(res)

    def describe_task_definition(
        self,
        res: "bs_td.DescribeTaskDefinitionResponseTypeDef",
    ) -> "dc_td.DescribeTaskDefinitionResponse":
        return dc_td.DescribeTaskDefinitionResponse.make_one(res)

    def describe_task_sets(
        self,
        res: "bs_td.DescribeTaskSetsResponseTypeDef",
    ) -> "dc_td.DescribeTaskSetsResponse":
        return dc_td.DescribeTaskSetsResponse.make_one(res)

    def describe_tasks(
        self,
        res: "bs_td.DescribeTasksResponseTypeDef",
    ) -> "dc_td.DescribeTasksResponse":
        return dc_td.DescribeTasksResponse.make_one(res)

    def discover_poll_endpoint(
        self,
        res: "bs_td.DiscoverPollEndpointResponseTypeDef",
    ) -> "dc_td.DiscoverPollEndpointResponse":
        return dc_td.DiscoverPollEndpointResponse.make_one(res)

    def execute_command(
        self,
        res: "bs_td.ExecuteCommandResponseTypeDef",
    ) -> "dc_td.ExecuteCommandResponse":
        return dc_td.ExecuteCommandResponse.make_one(res)

    def get_task_protection(
        self,
        res: "bs_td.GetTaskProtectionResponseTypeDef",
    ) -> "dc_td.GetTaskProtectionResponse":
        return dc_td.GetTaskProtectionResponse.make_one(res)

    def list_account_settings(
        self,
        res: "bs_td.ListAccountSettingsResponseTypeDef",
    ) -> "dc_td.ListAccountSettingsResponse":
        return dc_td.ListAccountSettingsResponse.make_one(res)

    def list_attributes(
        self,
        res: "bs_td.ListAttributesResponseTypeDef",
    ) -> "dc_td.ListAttributesResponse":
        return dc_td.ListAttributesResponse.make_one(res)

    def list_clusters(
        self,
        res: "bs_td.ListClustersResponseTypeDef",
    ) -> "dc_td.ListClustersResponse":
        return dc_td.ListClustersResponse.make_one(res)

    def list_container_instances(
        self,
        res: "bs_td.ListContainerInstancesResponseTypeDef",
    ) -> "dc_td.ListContainerInstancesResponse":
        return dc_td.ListContainerInstancesResponse.make_one(res)

    def list_service_deployments(
        self,
        res: "bs_td.ListServiceDeploymentsResponseTypeDef",
    ) -> "dc_td.ListServiceDeploymentsResponse":
        return dc_td.ListServiceDeploymentsResponse.make_one(res)

    def list_services(
        self,
        res: "bs_td.ListServicesResponseTypeDef",
    ) -> "dc_td.ListServicesResponse":
        return dc_td.ListServicesResponse.make_one(res)

    def list_services_by_namespace(
        self,
        res: "bs_td.ListServicesByNamespaceResponseTypeDef",
    ) -> "dc_td.ListServicesByNamespaceResponse":
        return dc_td.ListServicesByNamespaceResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_task_definition_families(
        self,
        res: "bs_td.ListTaskDefinitionFamiliesResponseTypeDef",
    ) -> "dc_td.ListTaskDefinitionFamiliesResponse":
        return dc_td.ListTaskDefinitionFamiliesResponse.make_one(res)

    def list_task_definitions(
        self,
        res: "bs_td.ListTaskDefinitionsResponseTypeDef",
    ) -> "dc_td.ListTaskDefinitionsResponse":
        return dc_td.ListTaskDefinitionsResponse.make_one(res)

    def list_tasks(
        self,
        res: "bs_td.ListTasksResponseTypeDef",
    ) -> "dc_td.ListTasksResponse":
        return dc_td.ListTasksResponse.make_one(res)

    def put_account_setting(
        self,
        res: "bs_td.PutAccountSettingResponseTypeDef",
    ) -> "dc_td.PutAccountSettingResponse":
        return dc_td.PutAccountSettingResponse.make_one(res)

    def put_account_setting_default(
        self,
        res: "bs_td.PutAccountSettingDefaultResponseTypeDef",
    ) -> "dc_td.PutAccountSettingDefaultResponse":
        return dc_td.PutAccountSettingDefaultResponse.make_one(res)

    def put_attributes(
        self,
        res: "bs_td.PutAttributesResponseTypeDef",
    ) -> "dc_td.PutAttributesResponse":
        return dc_td.PutAttributesResponse.make_one(res)

    def put_cluster_capacity_providers(
        self,
        res: "bs_td.PutClusterCapacityProvidersResponseTypeDef",
    ) -> "dc_td.PutClusterCapacityProvidersResponse":
        return dc_td.PutClusterCapacityProvidersResponse.make_one(res)

    def register_container_instance(
        self,
        res: "bs_td.RegisterContainerInstanceResponseTypeDef",
    ) -> "dc_td.RegisterContainerInstanceResponse":
        return dc_td.RegisterContainerInstanceResponse.make_one(res)

    def register_task_definition(
        self,
        res: "bs_td.RegisterTaskDefinitionResponseTypeDef",
    ) -> "dc_td.RegisterTaskDefinitionResponse":
        return dc_td.RegisterTaskDefinitionResponse.make_one(res)

    def run_task(
        self,
        res: "bs_td.RunTaskResponseTypeDef",
    ) -> "dc_td.RunTaskResponse":
        return dc_td.RunTaskResponse.make_one(res)

    def start_task(
        self,
        res: "bs_td.StartTaskResponseTypeDef",
    ) -> "dc_td.StartTaskResponse":
        return dc_td.StartTaskResponse.make_one(res)

    def stop_service_deployment(
        self,
        res: "bs_td.StopServiceDeploymentResponseTypeDef",
    ) -> "dc_td.StopServiceDeploymentResponse":
        return dc_td.StopServiceDeploymentResponse.make_one(res)

    def stop_task(
        self,
        res: "bs_td.StopTaskResponseTypeDef",
    ) -> "dc_td.StopTaskResponse":
        return dc_td.StopTaskResponse.make_one(res)

    def submit_attachment_state_changes(
        self,
        res: "bs_td.SubmitAttachmentStateChangesResponseTypeDef",
    ) -> "dc_td.SubmitAttachmentStateChangesResponse":
        return dc_td.SubmitAttachmentStateChangesResponse.make_one(res)

    def submit_container_state_change(
        self,
        res: "bs_td.SubmitContainerStateChangeResponseTypeDef",
    ) -> "dc_td.SubmitContainerStateChangeResponse":
        return dc_td.SubmitContainerStateChangeResponse.make_one(res)

    def submit_task_state_change(
        self,
        res: "bs_td.SubmitTaskStateChangeResponseTypeDef",
    ) -> "dc_td.SubmitTaskStateChangeResponse":
        return dc_td.SubmitTaskStateChangeResponse.make_one(res)

    def update_capacity_provider(
        self,
        res: "bs_td.UpdateCapacityProviderResponseTypeDef",
    ) -> "dc_td.UpdateCapacityProviderResponse":
        return dc_td.UpdateCapacityProviderResponse.make_one(res)

    def update_cluster(
        self,
        res: "bs_td.UpdateClusterResponseTypeDef",
    ) -> "dc_td.UpdateClusterResponse":
        return dc_td.UpdateClusterResponse.make_one(res)

    def update_cluster_settings(
        self,
        res: "bs_td.UpdateClusterSettingsResponseTypeDef",
    ) -> "dc_td.UpdateClusterSettingsResponse":
        return dc_td.UpdateClusterSettingsResponse.make_one(res)

    def update_container_agent(
        self,
        res: "bs_td.UpdateContainerAgentResponseTypeDef",
    ) -> "dc_td.UpdateContainerAgentResponse":
        return dc_td.UpdateContainerAgentResponse.make_one(res)

    def update_container_instances_state(
        self,
        res: "bs_td.UpdateContainerInstancesStateResponseTypeDef",
    ) -> "dc_td.UpdateContainerInstancesStateResponse":
        return dc_td.UpdateContainerInstancesStateResponse.make_one(res)

    def update_service(
        self,
        res: "bs_td.UpdateServiceResponseTypeDef",
    ) -> "dc_td.UpdateServiceResponse":
        return dc_td.UpdateServiceResponse.make_one(res)

    def update_service_primary_task_set(
        self,
        res: "bs_td.UpdateServicePrimaryTaskSetResponseTypeDef",
    ) -> "dc_td.UpdateServicePrimaryTaskSetResponse":
        return dc_td.UpdateServicePrimaryTaskSetResponse.make_one(res)

    def update_task_protection(
        self,
        res: "bs_td.UpdateTaskProtectionResponseTypeDef",
    ) -> "dc_td.UpdateTaskProtectionResponse":
        return dc_td.UpdateTaskProtectionResponse.make_one(res)

    def update_task_set(
        self,
        res: "bs_td.UpdateTaskSetResponseTypeDef",
    ) -> "dc_td.UpdateTaskSetResponse":
        return dc_td.UpdateTaskSetResponse.make_one(res)


ecs_caster = ECSCaster()
