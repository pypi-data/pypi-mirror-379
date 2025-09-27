# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_emr import type_defs as bs_td


class EMRCaster:

    def add_instance_fleet(
        self,
        res: "bs_td.AddInstanceFleetOutputTypeDef",
    ) -> "dc_td.AddInstanceFleetOutput":
        return dc_td.AddInstanceFleetOutput.make_one(res)

    def add_instance_groups(
        self,
        res: "bs_td.AddInstanceGroupsOutputTypeDef",
    ) -> "dc_td.AddInstanceGroupsOutput":
        return dc_td.AddInstanceGroupsOutput.make_one(res)

    def add_job_flow_steps(
        self,
        res: "bs_td.AddJobFlowStepsOutputTypeDef",
    ) -> "dc_td.AddJobFlowStepsOutput":
        return dc_td.AddJobFlowStepsOutput.make_one(res)

    def cancel_steps(
        self,
        res: "bs_td.CancelStepsOutputTypeDef",
    ) -> "dc_td.CancelStepsOutput":
        return dc_td.CancelStepsOutput.make_one(res)

    def create_persistent_app_ui(
        self,
        res: "bs_td.CreatePersistentAppUIOutputTypeDef",
    ) -> "dc_td.CreatePersistentAppUIOutput":
        return dc_td.CreatePersistentAppUIOutput.make_one(res)

    def create_security_configuration(
        self,
        res: "bs_td.CreateSecurityConfigurationOutputTypeDef",
    ) -> "dc_td.CreateSecurityConfigurationOutput":
        return dc_td.CreateSecurityConfigurationOutput.make_one(res)

    def create_studio(
        self,
        res: "bs_td.CreateStudioOutputTypeDef",
    ) -> "dc_td.CreateStudioOutput":
        return dc_td.CreateStudioOutput.make_one(res)

    def create_studio_session_mapping(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_studio(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_studio_session_mapping(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_cluster(
        self,
        res: "bs_td.DescribeClusterOutputTypeDef",
    ) -> "dc_td.DescribeClusterOutput":
        return dc_td.DescribeClusterOutput.make_one(res)

    def describe_job_flows(
        self,
        res: "bs_td.DescribeJobFlowsOutputTypeDef",
    ) -> "dc_td.DescribeJobFlowsOutput":
        return dc_td.DescribeJobFlowsOutput.make_one(res)

    def describe_notebook_execution(
        self,
        res: "bs_td.DescribeNotebookExecutionOutputTypeDef",
    ) -> "dc_td.DescribeNotebookExecutionOutput":
        return dc_td.DescribeNotebookExecutionOutput.make_one(res)

    def describe_persistent_app_ui(
        self,
        res: "bs_td.DescribePersistentAppUIOutputTypeDef",
    ) -> "dc_td.DescribePersistentAppUIOutput":
        return dc_td.DescribePersistentAppUIOutput.make_one(res)

    def describe_release_label(
        self,
        res: "bs_td.DescribeReleaseLabelOutputTypeDef",
    ) -> "dc_td.DescribeReleaseLabelOutput":
        return dc_td.DescribeReleaseLabelOutput.make_one(res)

    def describe_security_configuration(
        self,
        res: "bs_td.DescribeSecurityConfigurationOutputTypeDef",
    ) -> "dc_td.DescribeSecurityConfigurationOutput":
        return dc_td.DescribeSecurityConfigurationOutput.make_one(res)

    def describe_step(
        self,
        res: "bs_td.DescribeStepOutputTypeDef",
    ) -> "dc_td.DescribeStepOutput":
        return dc_td.DescribeStepOutput.make_one(res)

    def describe_studio(
        self,
        res: "bs_td.DescribeStudioOutputTypeDef",
    ) -> "dc_td.DescribeStudioOutput":
        return dc_td.DescribeStudioOutput.make_one(res)

    def get_auto_termination_policy(
        self,
        res: "bs_td.GetAutoTerminationPolicyOutputTypeDef",
    ) -> "dc_td.GetAutoTerminationPolicyOutput":
        return dc_td.GetAutoTerminationPolicyOutput.make_one(res)

    def get_block_public_access_configuration(
        self,
        res: "bs_td.GetBlockPublicAccessConfigurationOutputTypeDef",
    ) -> "dc_td.GetBlockPublicAccessConfigurationOutput":
        return dc_td.GetBlockPublicAccessConfigurationOutput.make_one(res)

    def get_cluster_session_credentials(
        self,
        res: "bs_td.GetClusterSessionCredentialsOutputTypeDef",
    ) -> "dc_td.GetClusterSessionCredentialsOutput":
        return dc_td.GetClusterSessionCredentialsOutput.make_one(res)

    def get_managed_scaling_policy(
        self,
        res: "bs_td.GetManagedScalingPolicyOutputTypeDef",
    ) -> "dc_td.GetManagedScalingPolicyOutput":
        return dc_td.GetManagedScalingPolicyOutput.make_one(res)

    def get_on_cluster_app_ui_presigned_url(
        self,
        res: "bs_td.GetOnClusterAppUIPresignedURLOutputTypeDef",
    ) -> "dc_td.GetOnClusterAppUIPresignedURLOutput":
        return dc_td.GetOnClusterAppUIPresignedURLOutput.make_one(res)

    def get_persistent_app_ui_presigned_url(
        self,
        res: "bs_td.GetPersistentAppUIPresignedURLOutputTypeDef",
    ) -> "dc_td.GetPersistentAppUIPresignedURLOutput":
        return dc_td.GetPersistentAppUIPresignedURLOutput.make_one(res)

    def get_studio_session_mapping(
        self,
        res: "bs_td.GetStudioSessionMappingOutputTypeDef",
    ) -> "dc_td.GetStudioSessionMappingOutput":
        return dc_td.GetStudioSessionMappingOutput.make_one(res)

    def list_bootstrap_actions(
        self,
        res: "bs_td.ListBootstrapActionsOutputTypeDef",
    ) -> "dc_td.ListBootstrapActionsOutput":
        return dc_td.ListBootstrapActionsOutput.make_one(res)

    def list_clusters(
        self,
        res: "bs_td.ListClustersOutputTypeDef",
    ) -> "dc_td.ListClustersOutput":
        return dc_td.ListClustersOutput.make_one(res)

    def list_instance_fleets(
        self,
        res: "bs_td.ListInstanceFleetsOutputTypeDef",
    ) -> "dc_td.ListInstanceFleetsOutput":
        return dc_td.ListInstanceFleetsOutput.make_one(res)

    def list_instance_groups(
        self,
        res: "bs_td.ListInstanceGroupsOutputTypeDef",
    ) -> "dc_td.ListInstanceGroupsOutput":
        return dc_td.ListInstanceGroupsOutput.make_one(res)

    def list_instances(
        self,
        res: "bs_td.ListInstancesOutputTypeDef",
    ) -> "dc_td.ListInstancesOutput":
        return dc_td.ListInstancesOutput.make_one(res)

    def list_notebook_executions(
        self,
        res: "bs_td.ListNotebookExecutionsOutputTypeDef",
    ) -> "dc_td.ListNotebookExecutionsOutput":
        return dc_td.ListNotebookExecutionsOutput.make_one(res)

    def list_release_labels(
        self,
        res: "bs_td.ListReleaseLabelsOutputTypeDef",
    ) -> "dc_td.ListReleaseLabelsOutput":
        return dc_td.ListReleaseLabelsOutput.make_one(res)

    def list_security_configurations(
        self,
        res: "bs_td.ListSecurityConfigurationsOutputTypeDef",
    ) -> "dc_td.ListSecurityConfigurationsOutput":
        return dc_td.ListSecurityConfigurationsOutput.make_one(res)

    def list_steps(
        self,
        res: "bs_td.ListStepsOutputTypeDef",
    ) -> "dc_td.ListStepsOutput":
        return dc_td.ListStepsOutput.make_one(res)

    def list_studio_session_mappings(
        self,
        res: "bs_td.ListStudioSessionMappingsOutputTypeDef",
    ) -> "dc_td.ListStudioSessionMappingsOutput":
        return dc_td.ListStudioSessionMappingsOutput.make_one(res)

    def list_studios(
        self,
        res: "bs_td.ListStudiosOutputTypeDef",
    ) -> "dc_td.ListStudiosOutput":
        return dc_td.ListStudiosOutput.make_one(res)

    def list_supported_instance_types(
        self,
        res: "bs_td.ListSupportedInstanceTypesOutputTypeDef",
    ) -> "dc_td.ListSupportedInstanceTypesOutput":
        return dc_td.ListSupportedInstanceTypesOutput.make_one(res)

    def modify_cluster(
        self,
        res: "bs_td.ModifyClusterOutputTypeDef",
    ) -> "dc_td.ModifyClusterOutput":
        return dc_td.ModifyClusterOutput.make_one(res)

    def modify_instance_fleet(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def modify_instance_groups(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_auto_scaling_policy(
        self,
        res: "bs_td.PutAutoScalingPolicyOutputTypeDef",
    ) -> "dc_td.PutAutoScalingPolicyOutput":
        return dc_td.PutAutoScalingPolicyOutput.make_one(res)

    def run_job_flow(
        self,
        res: "bs_td.RunJobFlowOutputTypeDef",
    ) -> "dc_td.RunJobFlowOutput":
        return dc_td.RunJobFlowOutput.make_one(res)

    def set_keep_job_flow_alive_when_no_steps(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def set_termination_protection(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def set_unhealthy_node_replacement(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def set_visible_to_all_users(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_notebook_execution(
        self,
        res: "bs_td.StartNotebookExecutionOutputTypeDef",
    ) -> "dc_td.StartNotebookExecutionOutput":
        return dc_td.StartNotebookExecutionOutput.make_one(res)

    def stop_notebook_execution(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def terminate_job_flows(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_studio(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_studio_session_mapping(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


emr_caster = EMRCaster()
