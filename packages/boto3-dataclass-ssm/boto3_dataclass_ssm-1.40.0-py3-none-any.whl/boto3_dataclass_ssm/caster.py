# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ssm import type_defs as bs_td


class SSMCaster:

    def associate_ops_item_related_item(
        self,
        res: "bs_td.AssociateOpsItemRelatedItemResponseTypeDef",
    ) -> "dc_td.AssociateOpsItemRelatedItemResponse":
        return dc_td.AssociateOpsItemRelatedItemResponse.make_one(res)

    def cancel_maintenance_window_execution(
        self,
        res: "bs_td.CancelMaintenanceWindowExecutionResultTypeDef",
    ) -> "dc_td.CancelMaintenanceWindowExecutionResult":
        return dc_td.CancelMaintenanceWindowExecutionResult.make_one(res)

    def create_activation(
        self,
        res: "bs_td.CreateActivationResultTypeDef",
    ) -> "dc_td.CreateActivationResult":
        return dc_td.CreateActivationResult.make_one(res)

    def create_association(
        self,
        res: "bs_td.CreateAssociationResultTypeDef",
    ) -> "dc_td.CreateAssociationResult":
        return dc_td.CreateAssociationResult.make_one(res)

    def create_association_batch(
        self,
        res: "bs_td.CreateAssociationBatchResultTypeDef",
    ) -> "dc_td.CreateAssociationBatchResult":
        return dc_td.CreateAssociationBatchResult.make_one(res)

    def create_document(
        self,
        res: "bs_td.CreateDocumentResultTypeDef",
    ) -> "dc_td.CreateDocumentResult":
        return dc_td.CreateDocumentResult.make_one(res)

    def create_maintenance_window(
        self,
        res: "bs_td.CreateMaintenanceWindowResultTypeDef",
    ) -> "dc_td.CreateMaintenanceWindowResult":
        return dc_td.CreateMaintenanceWindowResult.make_one(res)

    def create_ops_item(
        self,
        res: "bs_td.CreateOpsItemResponseTypeDef",
    ) -> "dc_td.CreateOpsItemResponse":
        return dc_td.CreateOpsItemResponse.make_one(res)

    def create_ops_metadata(
        self,
        res: "bs_td.CreateOpsMetadataResultTypeDef",
    ) -> "dc_td.CreateOpsMetadataResult":
        return dc_td.CreateOpsMetadataResult.make_one(res)

    def create_patch_baseline(
        self,
        res: "bs_td.CreatePatchBaselineResultTypeDef",
    ) -> "dc_td.CreatePatchBaselineResult":
        return dc_td.CreatePatchBaselineResult.make_one(res)

    def delete_inventory(
        self,
        res: "bs_td.DeleteInventoryResultTypeDef",
    ) -> "dc_td.DeleteInventoryResult":
        return dc_td.DeleteInventoryResult.make_one(res)

    def delete_maintenance_window(
        self,
        res: "bs_td.DeleteMaintenanceWindowResultTypeDef",
    ) -> "dc_td.DeleteMaintenanceWindowResult":
        return dc_td.DeleteMaintenanceWindowResult.make_one(res)

    def delete_parameters(
        self,
        res: "bs_td.DeleteParametersResultTypeDef",
    ) -> "dc_td.DeleteParametersResult":
        return dc_td.DeleteParametersResult.make_one(res)

    def delete_patch_baseline(
        self,
        res: "bs_td.DeletePatchBaselineResultTypeDef",
    ) -> "dc_td.DeletePatchBaselineResult":
        return dc_td.DeletePatchBaselineResult.make_one(res)

    def deregister_patch_baseline_for_patch_group(
        self,
        res: "bs_td.DeregisterPatchBaselineForPatchGroupResultTypeDef",
    ) -> "dc_td.DeregisterPatchBaselineForPatchGroupResult":
        return dc_td.DeregisterPatchBaselineForPatchGroupResult.make_one(res)

    def deregister_target_from_maintenance_window(
        self,
        res: "bs_td.DeregisterTargetFromMaintenanceWindowResultTypeDef",
    ) -> "dc_td.DeregisterTargetFromMaintenanceWindowResult":
        return dc_td.DeregisterTargetFromMaintenanceWindowResult.make_one(res)

    def deregister_task_from_maintenance_window(
        self,
        res: "bs_td.DeregisterTaskFromMaintenanceWindowResultTypeDef",
    ) -> "dc_td.DeregisterTaskFromMaintenanceWindowResult":
        return dc_td.DeregisterTaskFromMaintenanceWindowResult.make_one(res)

    def describe_activations(
        self,
        res: "bs_td.DescribeActivationsResultTypeDef",
    ) -> "dc_td.DescribeActivationsResult":
        return dc_td.DescribeActivationsResult.make_one(res)

    def describe_association(
        self,
        res: "bs_td.DescribeAssociationResultTypeDef",
    ) -> "dc_td.DescribeAssociationResult":
        return dc_td.DescribeAssociationResult.make_one(res)

    def describe_association_execution_targets(
        self,
        res: "bs_td.DescribeAssociationExecutionTargetsResultTypeDef",
    ) -> "dc_td.DescribeAssociationExecutionTargetsResult":
        return dc_td.DescribeAssociationExecutionTargetsResult.make_one(res)

    def describe_association_executions(
        self,
        res: "bs_td.DescribeAssociationExecutionsResultTypeDef",
    ) -> "dc_td.DescribeAssociationExecutionsResult":
        return dc_td.DescribeAssociationExecutionsResult.make_one(res)

    def describe_automation_executions(
        self,
        res: "bs_td.DescribeAutomationExecutionsResultTypeDef",
    ) -> "dc_td.DescribeAutomationExecutionsResult":
        return dc_td.DescribeAutomationExecutionsResult.make_one(res)

    def describe_automation_step_executions(
        self,
        res: "bs_td.DescribeAutomationStepExecutionsResultTypeDef",
    ) -> "dc_td.DescribeAutomationStepExecutionsResult":
        return dc_td.DescribeAutomationStepExecutionsResult.make_one(res)

    def describe_available_patches(
        self,
        res: "bs_td.DescribeAvailablePatchesResultTypeDef",
    ) -> "dc_td.DescribeAvailablePatchesResult":
        return dc_td.DescribeAvailablePatchesResult.make_one(res)

    def describe_document(
        self,
        res: "bs_td.DescribeDocumentResultTypeDef",
    ) -> "dc_td.DescribeDocumentResult":
        return dc_td.DescribeDocumentResult.make_one(res)

    def describe_document_permission(
        self,
        res: "bs_td.DescribeDocumentPermissionResponseTypeDef",
    ) -> "dc_td.DescribeDocumentPermissionResponse":
        return dc_td.DescribeDocumentPermissionResponse.make_one(res)

    def describe_effective_instance_associations(
        self,
        res: "bs_td.DescribeEffectiveInstanceAssociationsResultTypeDef",
    ) -> "dc_td.DescribeEffectiveInstanceAssociationsResult":
        return dc_td.DescribeEffectiveInstanceAssociationsResult.make_one(res)

    def describe_effective_patches_for_patch_baseline(
        self,
        res: "bs_td.DescribeEffectivePatchesForPatchBaselineResultTypeDef",
    ) -> "dc_td.DescribeEffectivePatchesForPatchBaselineResult":
        return dc_td.DescribeEffectivePatchesForPatchBaselineResult.make_one(res)

    def describe_instance_associations_status(
        self,
        res: "bs_td.DescribeInstanceAssociationsStatusResultTypeDef",
    ) -> "dc_td.DescribeInstanceAssociationsStatusResult":
        return dc_td.DescribeInstanceAssociationsStatusResult.make_one(res)

    def describe_instance_information(
        self,
        res: "bs_td.DescribeInstanceInformationResultTypeDef",
    ) -> "dc_td.DescribeInstanceInformationResult":
        return dc_td.DescribeInstanceInformationResult.make_one(res)

    def describe_instance_patch_states(
        self,
        res: "bs_td.DescribeInstancePatchStatesResultTypeDef",
    ) -> "dc_td.DescribeInstancePatchStatesResult":
        return dc_td.DescribeInstancePatchStatesResult.make_one(res)

    def describe_instance_patch_states_for_patch_group(
        self,
        res: "bs_td.DescribeInstancePatchStatesForPatchGroupResultTypeDef",
    ) -> "dc_td.DescribeInstancePatchStatesForPatchGroupResult":
        return dc_td.DescribeInstancePatchStatesForPatchGroupResult.make_one(res)

    def describe_instance_patches(
        self,
        res: "bs_td.DescribeInstancePatchesResultTypeDef",
    ) -> "dc_td.DescribeInstancePatchesResult":
        return dc_td.DescribeInstancePatchesResult.make_one(res)

    def describe_instance_properties(
        self,
        res: "bs_td.DescribeInstancePropertiesResultTypeDef",
    ) -> "dc_td.DescribeInstancePropertiesResult":
        return dc_td.DescribeInstancePropertiesResult.make_one(res)

    def describe_inventory_deletions(
        self,
        res: "bs_td.DescribeInventoryDeletionsResultTypeDef",
    ) -> "dc_td.DescribeInventoryDeletionsResult":
        return dc_td.DescribeInventoryDeletionsResult.make_one(res)

    def describe_maintenance_window_execution_task_invocations(
        self,
        res: "bs_td.DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef",
    ) -> "dc_td.DescribeMaintenanceWindowExecutionTaskInvocationsResult":
        return dc_td.DescribeMaintenanceWindowExecutionTaskInvocationsResult.make_one(
            res
        )

    def describe_maintenance_window_execution_tasks(
        self,
        res: "bs_td.DescribeMaintenanceWindowExecutionTasksResultTypeDef",
    ) -> "dc_td.DescribeMaintenanceWindowExecutionTasksResult":
        return dc_td.DescribeMaintenanceWindowExecutionTasksResult.make_one(res)

    def describe_maintenance_window_executions(
        self,
        res: "bs_td.DescribeMaintenanceWindowExecutionsResultTypeDef",
    ) -> "dc_td.DescribeMaintenanceWindowExecutionsResult":
        return dc_td.DescribeMaintenanceWindowExecutionsResult.make_one(res)

    def describe_maintenance_window_schedule(
        self,
        res: "bs_td.DescribeMaintenanceWindowScheduleResultTypeDef",
    ) -> "dc_td.DescribeMaintenanceWindowScheduleResult":
        return dc_td.DescribeMaintenanceWindowScheduleResult.make_one(res)

    def describe_maintenance_window_targets(
        self,
        res: "bs_td.DescribeMaintenanceWindowTargetsResultTypeDef",
    ) -> "dc_td.DescribeMaintenanceWindowTargetsResult":
        return dc_td.DescribeMaintenanceWindowTargetsResult.make_one(res)

    def describe_maintenance_window_tasks(
        self,
        res: "bs_td.DescribeMaintenanceWindowTasksResultTypeDef",
    ) -> "dc_td.DescribeMaintenanceWindowTasksResult":
        return dc_td.DescribeMaintenanceWindowTasksResult.make_one(res)

    def describe_maintenance_windows(
        self,
        res: "bs_td.DescribeMaintenanceWindowsResultTypeDef",
    ) -> "dc_td.DescribeMaintenanceWindowsResult":
        return dc_td.DescribeMaintenanceWindowsResult.make_one(res)

    def describe_maintenance_windows_for_target(
        self,
        res: "bs_td.DescribeMaintenanceWindowsForTargetResultTypeDef",
    ) -> "dc_td.DescribeMaintenanceWindowsForTargetResult":
        return dc_td.DescribeMaintenanceWindowsForTargetResult.make_one(res)

    def describe_ops_items(
        self,
        res: "bs_td.DescribeOpsItemsResponseTypeDef",
    ) -> "dc_td.DescribeOpsItemsResponse":
        return dc_td.DescribeOpsItemsResponse.make_one(res)

    def describe_parameters(
        self,
        res: "bs_td.DescribeParametersResultTypeDef",
    ) -> "dc_td.DescribeParametersResult":
        return dc_td.DescribeParametersResult.make_one(res)

    def describe_patch_baselines(
        self,
        res: "bs_td.DescribePatchBaselinesResultTypeDef",
    ) -> "dc_td.DescribePatchBaselinesResult":
        return dc_td.DescribePatchBaselinesResult.make_one(res)

    def describe_patch_group_state(
        self,
        res: "bs_td.DescribePatchGroupStateResultTypeDef",
    ) -> "dc_td.DescribePatchGroupStateResult":
        return dc_td.DescribePatchGroupStateResult.make_one(res)

    def describe_patch_groups(
        self,
        res: "bs_td.DescribePatchGroupsResultTypeDef",
    ) -> "dc_td.DescribePatchGroupsResult":
        return dc_td.DescribePatchGroupsResult.make_one(res)

    def describe_patch_properties(
        self,
        res: "bs_td.DescribePatchPropertiesResultTypeDef",
    ) -> "dc_td.DescribePatchPropertiesResult":
        return dc_td.DescribePatchPropertiesResult.make_one(res)

    def describe_sessions(
        self,
        res: "bs_td.DescribeSessionsResponseTypeDef",
    ) -> "dc_td.DescribeSessionsResponse":
        return dc_td.DescribeSessionsResponse.make_one(res)

    def get_access_token(
        self,
        res: "bs_td.GetAccessTokenResponseTypeDef",
    ) -> "dc_td.GetAccessTokenResponse":
        return dc_td.GetAccessTokenResponse.make_one(res)

    def get_automation_execution(
        self,
        res: "bs_td.GetAutomationExecutionResultTypeDef",
    ) -> "dc_td.GetAutomationExecutionResult":
        return dc_td.GetAutomationExecutionResult.make_one(res)

    def get_calendar_state(
        self,
        res: "bs_td.GetCalendarStateResponseTypeDef",
    ) -> "dc_td.GetCalendarStateResponse":
        return dc_td.GetCalendarStateResponse.make_one(res)

    def get_command_invocation(
        self,
        res: "bs_td.GetCommandInvocationResultTypeDef",
    ) -> "dc_td.GetCommandInvocationResult":
        return dc_td.GetCommandInvocationResult.make_one(res)

    def get_connection_status(
        self,
        res: "bs_td.GetConnectionStatusResponseTypeDef",
    ) -> "dc_td.GetConnectionStatusResponse":
        return dc_td.GetConnectionStatusResponse.make_one(res)

    def get_default_patch_baseline(
        self,
        res: "bs_td.GetDefaultPatchBaselineResultTypeDef",
    ) -> "dc_td.GetDefaultPatchBaselineResult":
        return dc_td.GetDefaultPatchBaselineResult.make_one(res)

    def get_deployable_patch_snapshot_for_instance(
        self,
        res: "bs_td.GetDeployablePatchSnapshotForInstanceResultTypeDef",
    ) -> "dc_td.GetDeployablePatchSnapshotForInstanceResult":
        return dc_td.GetDeployablePatchSnapshotForInstanceResult.make_one(res)

    def get_document(
        self,
        res: "bs_td.GetDocumentResultTypeDef",
    ) -> "dc_td.GetDocumentResult":
        return dc_td.GetDocumentResult.make_one(res)

    def get_execution_preview(
        self,
        res: "bs_td.GetExecutionPreviewResponseTypeDef",
    ) -> "dc_td.GetExecutionPreviewResponse":
        return dc_td.GetExecutionPreviewResponse.make_one(res)

    def get_inventory(
        self,
        res: "bs_td.GetInventoryResultTypeDef",
    ) -> "dc_td.GetInventoryResult":
        return dc_td.GetInventoryResult.make_one(res)

    def get_inventory_schema(
        self,
        res: "bs_td.GetInventorySchemaResultTypeDef",
    ) -> "dc_td.GetInventorySchemaResult":
        return dc_td.GetInventorySchemaResult.make_one(res)

    def get_maintenance_window(
        self,
        res: "bs_td.GetMaintenanceWindowResultTypeDef",
    ) -> "dc_td.GetMaintenanceWindowResult":
        return dc_td.GetMaintenanceWindowResult.make_one(res)

    def get_maintenance_window_execution(
        self,
        res: "bs_td.GetMaintenanceWindowExecutionResultTypeDef",
    ) -> "dc_td.GetMaintenanceWindowExecutionResult":
        return dc_td.GetMaintenanceWindowExecutionResult.make_one(res)

    def get_maintenance_window_execution_task(
        self,
        res: "bs_td.GetMaintenanceWindowExecutionTaskResultTypeDef",
    ) -> "dc_td.GetMaintenanceWindowExecutionTaskResult":
        return dc_td.GetMaintenanceWindowExecutionTaskResult.make_one(res)

    def get_maintenance_window_execution_task_invocation(
        self,
        res: "bs_td.GetMaintenanceWindowExecutionTaskInvocationResultTypeDef",
    ) -> "dc_td.GetMaintenanceWindowExecutionTaskInvocationResult":
        return dc_td.GetMaintenanceWindowExecutionTaskInvocationResult.make_one(res)

    def get_maintenance_window_task(
        self,
        res: "bs_td.GetMaintenanceWindowTaskResultTypeDef",
    ) -> "dc_td.GetMaintenanceWindowTaskResult":
        return dc_td.GetMaintenanceWindowTaskResult.make_one(res)

    def get_ops_item(
        self,
        res: "bs_td.GetOpsItemResponseTypeDef",
    ) -> "dc_td.GetOpsItemResponse":
        return dc_td.GetOpsItemResponse.make_one(res)

    def get_ops_metadata(
        self,
        res: "bs_td.GetOpsMetadataResultTypeDef",
    ) -> "dc_td.GetOpsMetadataResult":
        return dc_td.GetOpsMetadataResult.make_one(res)

    def get_ops_summary(
        self,
        res: "bs_td.GetOpsSummaryResultTypeDef",
    ) -> "dc_td.GetOpsSummaryResult":
        return dc_td.GetOpsSummaryResult.make_one(res)

    def get_parameter(
        self,
        res: "bs_td.GetParameterResultTypeDef",
    ) -> "dc_td.GetParameterResult":
        return dc_td.GetParameterResult.make_one(res)

    def get_parameter_history(
        self,
        res: "bs_td.GetParameterHistoryResultTypeDef",
    ) -> "dc_td.GetParameterHistoryResult":
        return dc_td.GetParameterHistoryResult.make_one(res)

    def get_parameters(
        self,
        res: "bs_td.GetParametersResultTypeDef",
    ) -> "dc_td.GetParametersResult":
        return dc_td.GetParametersResult.make_one(res)

    def get_parameters_by_path(
        self,
        res: "bs_td.GetParametersByPathResultTypeDef",
    ) -> "dc_td.GetParametersByPathResult":
        return dc_td.GetParametersByPathResult.make_one(res)

    def get_patch_baseline(
        self,
        res: "bs_td.GetPatchBaselineResultTypeDef",
    ) -> "dc_td.GetPatchBaselineResult":
        return dc_td.GetPatchBaselineResult.make_one(res)

    def get_patch_baseline_for_patch_group(
        self,
        res: "bs_td.GetPatchBaselineForPatchGroupResultTypeDef",
    ) -> "dc_td.GetPatchBaselineForPatchGroupResult":
        return dc_td.GetPatchBaselineForPatchGroupResult.make_one(res)

    def get_resource_policies(
        self,
        res: "bs_td.GetResourcePoliciesResponseTypeDef",
    ) -> "dc_td.GetResourcePoliciesResponse":
        return dc_td.GetResourcePoliciesResponse.make_one(res)

    def get_service_setting(
        self,
        res: "bs_td.GetServiceSettingResultTypeDef",
    ) -> "dc_td.GetServiceSettingResult":
        return dc_td.GetServiceSettingResult.make_one(res)

    def label_parameter_version(
        self,
        res: "bs_td.LabelParameterVersionResultTypeDef",
    ) -> "dc_td.LabelParameterVersionResult":
        return dc_td.LabelParameterVersionResult.make_one(res)

    def list_association_versions(
        self,
        res: "bs_td.ListAssociationVersionsResultTypeDef",
    ) -> "dc_td.ListAssociationVersionsResult":
        return dc_td.ListAssociationVersionsResult.make_one(res)

    def list_associations(
        self,
        res: "bs_td.ListAssociationsResultTypeDef",
    ) -> "dc_td.ListAssociationsResult":
        return dc_td.ListAssociationsResult.make_one(res)

    def list_command_invocations(
        self,
        res: "bs_td.ListCommandInvocationsResultTypeDef",
    ) -> "dc_td.ListCommandInvocationsResult":
        return dc_td.ListCommandInvocationsResult.make_one(res)

    def list_commands(
        self,
        res: "bs_td.ListCommandsResultTypeDef",
    ) -> "dc_td.ListCommandsResult":
        return dc_td.ListCommandsResult.make_one(res)

    def list_compliance_items(
        self,
        res: "bs_td.ListComplianceItemsResultTypeDef",
    ) -> "dc_td.ListComplianceItemsResult":
        return dc_td.ListComplianceItemsResult.make_one(res)

    def list_compliance_summaries(
        self,
        res: "bs_td.ListComplianceSummariesResultTypeDef",
    ) -> "dc_td.ListComplianceSummariesResult":
        return dc_td.ListComplianceSummariesResult.make_one(res)

    def list_document_metadata_history(
        self,
        res: "bs_td.ListDocumentMetadataHistoryResponseTypeDef",
    ) -> "dc_td.ListDocumentMetadataHistoryResponse":
        return dc_td.ListDocumentMetadataHistoryResponse.make_one(res)

    def list_document_versions(
        self,
        res: "bs_td.ListDocumentVersionsResultTypeDef",
    ) -> "dc_td.ListDocumentVersionsResult":
        return dc_td.ListDocumentVersionsResult.make_one(res)

    def list_documents(
        self,
        res: "bs_td.ListDocumentsResultTypeDef",
    ) -> "dc_td.ListDocumentsResult":
        return dc_td.ListDocumentsResult.make_one(res)

    def list_inventory_entries(
        self,
        res: "bs_td.ListInventoryEntriesResultTypeDef",
    ) -> "dc_td.ListInventoryEntriesResult":
        return dc_td.ListInventoryEntriesResult.make_one(res)

    def list_nodes(
        self,
        res: "bs_td.ListNodesResultTypeDef",
    ) -> "dc_td.ListNodesResult":
        return dc_td.ListNodesResult.make_one(res)

    def list_nodes_summary(
        self,
        res: "bs_td.ListNodesSummaryResultTypeDef",
    ) -> "dc_td.ListNodesSummaryResult":
        return dc_td.ListNodesSummaryResult.make_one(res)

    def list_ops_item_events(
        self,
        res: "bs_td.ListOpsItemEventsResponseTypeDef",
    ) -> "dc_td.ListOpsItemEventsResponse":
        return dc_td.ListOpsItemEventsResponse.make_one(res)

    def list_ops_item_related_items(
        self,
        res: "bs_td.ListOpsItemRelatedItemsResponseTypeDef",
    ) -> "dc_td.ListOpsItemRelatedItemsResponse":
        return dc_td.ListOpsItemRelatedItemsResponse.make_one(res)

    def list_ops_metadata(
        self,
        res: "bs_td.ListOpsMetadataResultTypeDef",
    ) -> "dc_td.ListOpsMetadataResult":
        return dc_td.ListOpsMetadataResult.make_one(res)

    def list_resource_compliance_summaries(
        self,
        res: "bs_td.ListResourceComplianceSummariesResultTypeDef",
    ) -> "dc_td.ListResourceComplianceSummariesResult":
        return dc_td.ListResourceComplianceSummariesResult.make_one(res)

    def list_resource_data_sync(
        self,
        res: "bs_td.ListResourceDataSyncResultTypeDef",
    ) -> "dc_td.ListResourceDataSyncResult":
        return dc_td.ListResourceDataSyncResult.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResultTypeDef",
    ) -> "dc_td.ListTagsForResourceResult":
        return dc_td.ListTagsForResourceResult.make_one(res)

    def put_inventory(
        self,
        res: "bs_td.PutInventoryResultTypeDef",
    ) -> "dc_td.PutInventoryResult":
        return dc_td.PutInventoryResult.make_one(res)

    def put_parameter(
        self,
        res: "bs_td.PutParameterResultTypeDef",
    ) -> "dc_td.PutParameterResult":
        return dc_td.PutParameterResult.make_one(res)

    def put_resource_policy(
        self,
        res: "bs_td.PutResourcePolicyResponseTypeDef",
    ) -> "dc_td.PutResourcePolicyResponse":
        return dc_td.PutResourcePolicyResponse.make_one(res)

    def register_default_patch_baseline(
        self,
        res: "bs_td.RegisterDefaultPatchBaselineResultTypeDef",
    ) -> "dc_td.RegisterDefaultPatchBaselineResult":
        return dc_td.RegisterDefaultPatchBaselineResult.make_one(res)

    def register_patch_baseline_for_patch_group(
        self,
        res: "bs_td.RegisterPatchBaselineForPatchGroupResultTypeDef",
    ) -> "dc_td.RegisterPatchBaselineForPatchGroupResult":
        return dc_td.RegisterPatchBaselineForPatchGroupResult.make_one(res)

    def register_target_with_maintenance_window(
        self,
        res: "bs_td.RegisterTargetWithMaintenanceWindowResultTypeDef",
    ) -> "dc_td.RegisterTargetWithMaintenanceWindowResult":
        return dc_td.RegisterTargetWithMaintenanceWindowResult.make_one(res)

    def register_task_with_maintenance_window(
        self,
        res: "bs_td.RegisterTaskWithMaintenanceWindowResultTypeDef",
    ) -> "dc_td.RegisterTaskWithMaintenanceWindowResult":
        return dc_td.RegisterTaskWithMaintenanceWindowResult.make_one(res)

    def reset_service_setting(
        self,
        res: "bs_td.ResetServiceSettingResultTypeDef",
    ) -> "dc_td.ResetServiceSettingResult":
        return dc_td.ResetServiceSettingResult.make_one(res)

    def resume_session(
        self,
        res: "bs_td.ResumeSessionResponseTypeDef",
    ) -> "dc_td.ResumeSessionResponse":
        return dc_td.ResumeSessionResponse.make_one(res)

    def send_command(
        self,
        res: "bs_td.SendCommandResultTypeDef",
    ) -> "dc_td.SendCommandResult":
        return dc_td.SendCommandResult.make_one(res)

    def start_access_request(
        self,
        res: "bs_td.StartAccessRequestResponseTypeDef",
    ) -> "dc_td.StartAccessRequestResponse":
        return dc_td.StartAccessRequestResponse.make_one(res)

    def start_automation_execution(
        self,
        res: "bs_td.StartAutomationExecutionResultTypeDef",
    ) -> "dc_td.StartAutomationExecutionResult":
        return dc_td.StartAutomationExecutionResult.make_one(res)

    def start_change_request_execution(
        self,
        res: "bs_td.StartChangeRequestExecutionResultTypeDef",
    ) -> "dc_td.StartChangeRequestExecutionResult":
        return dc_td.StartChangeRequestExecutionResult.make_one(res)

    def start_execution_preview(
        self,
        res: "bs_td.StartExecutionPreviewResponseTypeDef",
    ) -> "dc_td.StartExecutionPreviewResponse":
        return dc_td.StartExecutionPreviewResponse.make_one(res)

    def start_session(
        self,
        res: "bs_td.StartSessionResponseTypeDef",
    ) -> "dc_td.StartSessionResponse":
        return dc_td.StartSessionResponse.make_one(res)

    def terminate_session(
        self,
        res: "bs_td.TerminateSessionResponseTypeDef",
    ) -> "dc_td.TerminateSessionResponse":
        return dc_td.TerminateSessionResponse.make_one(res)

    def unlabel_parameter_version(
        self,
        res: "bs_td.UnlabelParameterVersionResultTypeDef",
    ) -> "dc_td.UnlabelParameterVersionResult":
        return dc_td.UnlabelParameterVersionResult.make_one(res)

    def update_association(
        self,
        res: "bs_td.UpdateAssociationResultTypeDef",
    ) -> "dc_td.UpdateAssociationResult":
        return dc_td.UpdateAssociationResult.make_one(res)

    def update_association_status(
        self,
        res: "bs_td.UpdateAssociationStatusResultTypeDef",
    ) -> "dc_td.UpdateAssociationStatusResult":
        return dc_td.UpdateAssociationStatusResult.make_one(res)

    def update_document(
        self,
        res: "bs_td.UpdateDocumentResultTypeDef",
    ) -> "dc_td.UpdateDocumentResult":
        return dc_td.UpdateDocumentResult.make_one(res)

    def update_document_default_version(
        self,
        res: "bs_td.UpdateDocumentDefaultVersionResultTypeDef",
    ) -> "dc_td.UpdateDocumentDefaultVersionResult":
        return dc_td.UpdateDocumentDefaultVersionResult.make_one(res)

    def update_maintenance_window(
        self,
        res: "bs_td.UpdateMaintenanceWindowResultTypeDef",
    ) -> "dc_td.UpdateMaintenanceWindowResult":
        return dc_td.UpdateMaintenanceWindowResult.make_one(res)

    def update_maintenance_window_target(
        self,
        res: "bs_td.UpdateMaintenanceWindowTargetResultTypeDef",
    ) -> "dc_td.UpdateMaintenanceWindowTargetResult":
        return dc_td.UpdateMaintenanceWindowTargetResult.make_one(res)

    def update_maintenance_window_task(
        self,
        res: "bs_td.UpdateMaintenanceWindowTaskResultTypeDef",
    ) -> "dc_td.UpdateMaintenanceWindowTaskResult":
        return dc_td.UpdateMaintenanceWindowTaskResult.make_one(res)

    def update_ops_metadata(
        self,
        res: "bs_td.UpdateOpsMetadataResultTypeDef",
    ) -> "dc_td.UpdateOpsMetadataResult":
        return dc_td.UpdateOpsMetadataResult.make_one(res)

    def update_patch_baseline(
        self,
        res: "bs_td.UpdatePatchBaselineResultTypeDef",
    ) -> "dc_td.UpdatePatchBaselineResult":
        return dc_td.UpdatePatchBaselineResult.make_one(res)


ssm_caster = SSMCaster()
