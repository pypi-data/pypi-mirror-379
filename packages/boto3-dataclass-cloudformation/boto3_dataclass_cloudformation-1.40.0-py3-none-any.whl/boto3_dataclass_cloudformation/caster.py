# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cloudformation import type_defs as bs_td


class CLOUDFORMATIONCaster:

    def activate_type(
        self,
        res: "bs_td.ActivateTypeOutputTypeDef",
    ) -> "dc_td.ActivateTypeOutput":
        return dc_td.ActivateTypeOutput.make_one(res)

    def batch_describe_type_configurations(
        self,
        res: "bs_td.BatchDescribeTypeConfigurationsOutputTypeDef",
    ) -> "dc_td.BatchDescribeTypeConfigurationsOutput":
        return dc_td.BatchDescribeTypeConfigurationsOutput.make_one(res)

    def cancel_update_stack(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_change_set(
        self,
        res: "bs_td.CreateChangeSetOutputTypeDef",
    ) -> "dc_td.CreateChangeSetOutput":
        return dc_td.CreateChangeSetOutput.make_one(res)

    def create_generated_template(
        self,
        res: "bs_td.CreateGeneratedTemplateOutputTypeDef",
    ) -> "dc_td.CreateGeneratedTemplateOutput":
        return dc_td.CreateGeneratedTemplateOutput.make_one(res)

    def create_stack(
        self,
        res: "bs_td.CreateStackOutputTypeDef",
    ) -> "dc_td.CreateStackOutput":
        return dc_td.CreateStackOutput.make_one(res)

    def create_stack_instances(
        self,
        res: "bs_td.CreateStackInstancesOutputTypeDef",
    ) -> "dc_td.CreateStackInstancesOutput":
        return dc_td.CreateStackInstancesOutput.make_one(res)

    def create_stack_refactor(
        self,
        res: "bs_td.CreateStackRefactorOutputTypeDef",
    ) -> "dc_td.CreateStackRefactorOutput":
        return dc_td.CreateStackRefactorOutput.make_one(res)

    def create_stack_set(
        self,
        res: "bs_td.CreateStackSetOutputTypeDef",
    ) -> "dc_td.CreateStackSetOutput":
        return dc_td.CreateStackSetOutput.make_one(res)

    def delete_generated_template(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_stack(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_stack_instances(
        self,
        res: "bs_td.DeleteStackInstancesOutputTypeDef",
    ) -> "dc_td.DeleteStackInstancesOutput":
        return dc_td.DeleteStackInstancesOutput.make_one(res)

    def describe_account_limits(
        self,
        res: "bs_td.DescribeAccountLimitsOutputTypeDef",
    ) -> "dc_td.DescribeAccountLimitsOutput":
        return dc_td.DescribeAccountLimitsOutput.make_one(res)

    def describe_change_set(
        self,
        res: "bs_td.DescribeChangeSetOutputTypeDef",
    ) -> "dc_td.DescribeChangeSetOutput":
        return dc_td.DescribeChangeSetOutput.make_one(res)

    def describe_change_set_hooks(
        self,
        res: "bs_td.DescribeChangeSetHooksOutputTypeDef",
    ) -> "dc_td.DescribeChangeSetHooksOutput":
        return dc_td.DescribeChangeSetHooksOutput.make_one(res)

    def describe_generated_template(
        self,
        res: "bs_td.DescribeGeneratedTemplateOutputTypeDef",
    ) -> "dc_td.DescribeGeneratedTemplateOutput":
        return dc_td.DescribeGeneratedTemplateOutput.make_one(res)

    def describe_organizations_access(
        self,
        res: "bs_td.DescribeOrganizationsAccessOutputTypeDef",
    ) -> "dc_td.DescribeOrganizationsAccessOutput":
        return dc_td.DescribeOrganizationsAccessOutput.make_one(res)

    def describe_publisher(
        self,
        res: "bs_td.DescribePublisherOutputTypeDef",
    ) -> "dc_td.DescribePublisherOutput":
        return dc_td.DescribePublisherOutput.make_one(res)

    def describe_resource_scan(
        self,
        res: "bs_td.DescribeResourceScanOutputTypeDef",
    ) -> "dc_td.DescribeResourceScanOutput":
        return dc_td.DescribeResourceScanOutput.make_one(res)

    def describe_stack_drift_detection_status(
        self,
        res: "bs_td.DescribeStackDriftDetectionStatusOutputTypeDef",
    ) -> "dc_td.DescribeStackDriftDetectionStatusOutput":
        return dc_td.DescribeStackDriftDetectionStatusOutput.make_one(res)

    def describe_stack_events(
        self,
        res: "bs_td.DescribeStackEventsOutputTypeDef",
    ) -> "dc_td.DescribeStackEventsOutput":
        return dc_td.DescribeStackEventsOutput.make_one(res)

    def describe_stack_instance(
        self,
        res: "bs_td.DescribeStackInstanceOutputTypeDef",
    ) -> "dc_td.DescribeStackInstanceOutput":
        return dc_td.DescribeStackInstanceOutput.make_one(res)

    def describe_stack_refactor(
        self,
        res: "bs_td.DescribeStackRefactorOutputTypeDef",
    ) -> "dc_td.DescribeStackRefactorOutput":
        return dc_td.DescribeStackRefactorOutput.make_one(res)

    def describe_stack_resource(
        self,
        res: "bs_td.DescribeStackResourceOutputTypeDef",
    ) -> "dc_td.DescribeStackResourceOutput":
        return dc_td.DescribeStackResourceOutput.make_one(res)

    def describe_stack_resource_drifts(
        self,
        res: "bs_td.DescribeStackResourceDriftsOutputTypeDef",
    ) -> "dc_td.DescribeStackResourceDriftsOutput":
        return dc_td.DescribeStackResourceDriftsOutput.make_one(res)

    def describe_stack_resources(
        self,
        res: "bs_td.DescribeStackResourcesOutputTypeDef",
    ) -> "dc_td.DescribeStackResourcesOutput":
        return dc_td.DescribeStackResourcesOutput.make_one(res)

    def describe_stack_set(
        self,
        res: "bs_td.DescribeStackSetOutputTypeDef",
    ) -> "dc_td.DescribeStackSetOutput":
        return dc_td.DescribeStackSetOutput.make_one(res)

    def describe_stack_set_operation(
        self,
        res: "bs_td.DescribeStackSetOperationOutputTypeDef",
    ) -> "dc_td.DescribeStackSetOperationOutput":
        return dc_td.DescribeStackSetOperationOutput.make_one(res)

    def describe_stacks(
        self,
        res: "bs_td.DescribeStacksOutputTypeDef",
    ) -> "dc_td.DescribeStacksOutput":
        return dc_td.DescribeStacksOutput.make_one(res)

    def describe_type(
        self,
        res: "bs_td.DescribeTypeOutputTypeDef",
    ) -> "dc_td.DescribeTypeOutput":
        return dc_td.DescribeTypeOutput.make_one(res)

    def describe_type_registration(
        self,
        res: "bs_td.DescribeTypeRegistrationOutputTypeDef",
    ) -> "dc_td.DescribeTypeRegistrationOutput":
        return dc_td.DescribeTypeRegistrationOutput.make_one(res)

    def detect_stack_drift(
        self,
        res: "bs_td.DetectStackDriftOutputTypeDef",
    ) -> "dc_td.DetectStackDriftOutput":
        return dc_td.DetectStackDriftOutput.make_one(res)

    def detect_stack_resource_drift(
        self,
        res: "bs_td.DetectStackResourceDriftOutputTypeDef",
    ) -> "dc_td.DetectStackResourceDriftOutput":
        return dc_td.DetectStackResourceDriftOutput.make_one(res)

    def detect_stack_set_drift(
        self,
        res: "bs_td.DetectStackSetDriftOutputTypeDef",
    ) -> "dc_td.DetectStackSetDriftOutput":
        return dc_td.DetectStackSetDriftOutput.make_one(res)

    def estimate_template_cost(
        self,
        res: "bs_td.EstimateTemplateCostOutputTypeDef",
    ) -> "dc_td.EstimateTemplateCostOutput":
        return dc_td.EstimateTemplateCostOutput.make_one(res)

    def execute_stack_refactor(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_generated_template(
        self,
        res: "bs_td.GetGeneratedTemplateOutputTypeDef",
    ) -> "dc_td.GetGeneratedTemplateOutput":
        return dc_td.GetGeneratedTemplateOutput.make_one(res)

    def get_stack_policy(
        self,
        res: "bs_td.GetStackPolicyOutputTypeDef",
    ) -> "dc_td.GetStackPolicyOutput":
        return dc_td.GetStackPolicyOutput.make_one(res)

    def get_template(
        self,
        res: "bs_td.GetTemplateOutputTypeDef",
    ) -> "dc_td.GetTemplateOutput":
        return dc_td.GetTemplateOutput.make_one(res)

    def get_template_summary(
        self,
        res: "bs_td.GetTemplateSummaryOutputTypeDef",
    ) -> "dc_td.GetTemplateSummaryOutput":
        return dc_td.GetTemplateSummaryOutput.make_one(res)

    def import_stacks_to_stack_set(
        self,
        res: "bs_td.ImportStacksToStackSetOutputTypeDef",
    ) -> "dc_td.ImportStacksToStackSetOutput":
        return dc_td.ImportStacksToStackSetOutput.make_one(res)

    def list_change_sets(
        self,
        res: "bs_td.ListChangeSetsOutputTypeDef",
    ) -> "dc_td.ListChangeSetsOutput":
        return dc_td.ListChangeSetsOutput.make_one(res)

    def list_exports(
        self,
        res: "bs_td.ListExportsOutputTypeDef",
    ) -> "dc_td.ListExportsOutput":
        return dc_td.ListExportsOutput.make_one(res)

    def list_generated_templates(
        self,
        res: "bs_td.ListGeneratedTemplatesOutputTypeDef",
    ) -> "dc_td.ListGeneratedTemplatesOutput":
        return dc_td.ListGeneratedTemplatesOutput.make_one(res)

    def list_hook_results(
        self,
        res: "bs_td.ListHookResultsOutputTypeDef",
    ) -> "dc_td.ListHookResultsOutput":
        return dc_td.ListHookResultsOutput.make_one(res)

    def list_imports(
        self,
        res: "bs_td.ListImportsOutputTypeDef",
    ) -> "dc_td.ListImportsOutput":
        return dc_td.ListImportsOutput.make_one(res)

    def list_resource_scan_related_resources(
        self,
        res: "bs_td.ListResourceScanRelatedResourcesOutputTypeDef",
    ) -> "dc_td.ListResourceScanRelatedResourcesOutput":
        return dc_td.ListResourceScanRelatedResourcesOutput.make_one(res)

    def list_resource_scan_resources(
        self,
        res: "bs_td.ListResourceScanResourcesOutputTypeDef",
    ) -> "dc_td.ListResourceScanResourcesOutput":
        return dc_td.ListResourceScanResourcesOutput.make_one(res)

    def list_resource_scans(
        self,
        res: "bs_td.ListResourceScansOutputTypeDef",
    ) -> "dc_td.ListResourceScansOutput":
        return dc_td.ListResourceScansOutput.make_one(res)

    def list_stack_instance_resource_drifts(
        self,
        res: "bs_td.ListStackInstanceResourceDriftsOutputTypeDef",
    ) -> "dc_td.ListStackInstanceResourceDriftsOutput":
        return dc_td.ListStackInstanceResourceDriftsOutput.make_one(res)

    def list_stack_instances(
        self,
        res: "bs_td.ListStackInstancesOutputTypeDef",
    ) -> "dc_td.ListStackInstancesOutput":
        return dc_td.ListStackInstancesOutput.make_one(res)

    def list_stack_refactor_actions(
        self,
        res: "bs_td.ListStackRefactorActionsOutputTypeDef",
    ) -> "dc_td.ListStackRefactorActionsOutput":
        return dc_td.ListStackRefactorActionsOutput.make_one(res)

    def list_stack_refactors(
        self,
        res: "bs_td.ListStackRefactorsOutputTypeDef",
    ) -> "dc_td.ListStackRefactorsOutput":
        return dc_td.ListStackRefactorsOutput.make_one(res)

    def list_stack_resources(
        self,
        res: "bs_td.ListStackResourcesOutputTypeDef",
    ) -> "dc_td.ListStackResourcesOutput":
        return dc_td.ListStackResourcesOutput.make_one(res)

    def list_stack_set_auto_deployment_targets(
        self,
        res: "bs_td.ListStackSetAutoDeploymentTargetsOutputTypeDef",
    ) -> "dc_td.ListStackSetAutoDeploymentTargetsOutput":
        return dc_td.ListStackSetAutoDeploymentTargetsOutput.make_one(res)

    def list_stack_set_operation_results(
        self,
        res: "bs_td.ListStackSetOperationResultsOutputTypeDef",
    ) -> "dc_td.ListStackSetOperationResultsOutput":
        return dc_td.ListStackSetOperationResultsOutput.make_one(res)

    def list_stack_set_operations(
        self,
        res: "bs_td.ListStackSetOperationsOutputTypeDef",
    ) -> "dc_td.ListStackSetOperationsOutput":
        return dc_td.ListStackSetOperationsOutput.make_one(res)

    def list_stack_sets(
        self,
        res: "bs_td.ListStackSetsOutputTypeDef",
    ) -> "dc_td.ListStackSetsOutput":
        return dc_td.ListStackSetsOutput.make_one(res)

    def list_stacks(
        self,
        res: "bs_td.ListStacksOutputTypeDef",
    ) -> "dc_td.ListStacksOutput":
        return dc_td.ListStacksOutput.make_one(res)

    def list_type_registrations(
        self,
        res: "bs_td.ListTypeRegistrationsOutputTypeDef",
    ) -> "dc_td.ListTypeRegistrationsOutput":
        return dc_td.ListTypeRegistrationsOutput.make_one(res)

    def list_type_versions(
        self,
        res: "bs_td.ListTypeVersionsOutputTypeDef",
    ) -> "dc_td.ListTypeVersionsOutput":
        return dc_td.ListTypeVersionsOutput.make_one(res)

    def list_types(
        self,
        res: "bs_td.ListTypesOutputTypeDef",
    ) -> "dc_td.ListTypesOutput":
        return dc_td.ListTypesOutput.make_one(res)

    def publish_type(
        self,
        res: "bs_td.PublishTypeOutputTypeDef",
    ) -> "dc_td.PublishTypeOutput":
        return dc_td.PublishTypeOutput.make_one(res)

    def register_publisher(
        self,
        res: "bs_td.RegisterPublisherOutputTypeDef",
    ) -> "dc_td.RegisterPublisherOutput":
        return dc_td.RegisterPublisherOutput.make_one(res)

    def register_type(
        self,
        res: "bs_td.RegisterTypeOutputTypeDef",
    ) -> "dc_td.RegisterTypeOutput":
        return dc_td.RegisterTypeOutput.make_one(res)

    def rollback_stack(
        self,
        res: "bs_td.RollbackStackOutputTypeDef",
    ) -> "dc_td.RollbackStackOutput":
        return dc_td.RollbackStackOutput.make_one(res)

    def set_stack_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def set_type_configuration(
        self,
        res: "bs_td.SetTypeConfigurationOutputTypeDef",
    ) -> "dc_td.SetTypeConfigurationOutput":
        return dc_td.SetTypeConfigurationOutput.make_one(res)

    def signal_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_resource_scan(
        self,
        res: "bs_td.StartResourceScanOutputTypeDef",
    ) -> "dc_td.StartResourceScanOutput":
        return dc_td.StartResourceScanOutput.make_one(res)

    def test_type(
        self,
        res: "bs_td.TestTypeOutputTypeDef",
    ) -> "dc_td.TestTypeOutput":
        return dc_td.TestTypeOutput.make_one(res)

    def update_generated_template(
        self,
        res: "bs_td.UpdateGeneratedTemplateOutputTypeDef",
    ) -> "dc_td.UpdateGeneratedTemplateOutput":
        return dc_td.UpdateGeneratedTemplateOutput.make_one(res)

    def update_stack(
        self,
        res: "bs_td.UpdateStackOutputTypeDef",
    ) -> "dc_td.UpdateStackOutput":
        return dc_td.UpdateStackOutput.make_one(res)

    def update_stack_instances(
        self,
        res: "bs_td.UpdateStackInstancesOutputTypeDef",
    ) -> "dc_td.UpdateStackInstancesOutput":
        return dc_td.UpdateStackInstancesOutput.make_one(res)

    def update_stack_set(
        self,
        res: "bs_td.UpdateStackSetOutputTypeDef",
    ) -> "dc_td.UpdateStackSetOutput":
        return dc_td.UpdateStackSetOutput.make_one(res)

    def update_termination_protection(
        self,
        res: "bs_td.UpdateTerminationProtectionOutputTypeDef",
    ) -> "dc_td.UpdateTerminationProtectionOutput":
        return dc_td.UpdateTerminationProtectionOutput.make_one(res)

    def validate_template(
        self,
        res: "bs_td.ValidateTemplateOutputTypeDef",
    ) -> "dc_td.ValidateTemplateOutput":
        return dc_td.ValidateTemplateOutput.make_one(res)


cloudformation_caster = CLOUDFORMATIONCaster()
