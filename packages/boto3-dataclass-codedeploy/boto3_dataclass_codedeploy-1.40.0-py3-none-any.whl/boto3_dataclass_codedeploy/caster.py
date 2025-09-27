# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_codedeploy import type_defs as bs_td


class CODEDEPLOYCaster:

    def add_tags_to_on_premises_instances(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def batch_get_application_revisions(
        self,
        res: "bs_td.BatchGetApplicationRevisionsOutputTypeDef",
    ) -> "dc_td.BatchGetApplicationRevisionsOutput":
        return dc_td.BatchGetApplicationRevisionsOutput.make_one(res)

    def batch_get_applications(
        self,
        res: "bs_td.BatchGetApplicationsOutputTypeDef",
    ) -> "dc_td.BatchGetApplicationsOutput":
        return dc_td.BatchGetApplicationsOutput.make_one(res)

    def batch_get_deployment_groups(
        self,
        res: "bs_td.BatchGetDeploymentGroupsOutputTypeDef",
    ) -> "dc_td.BatchGetDeploymentGroupsOutput":
        return dc_td.BatchGetDeploymentGroupsOutput.make_one(res)

    def batch_get_deployment_instances(
        self,
        res: "bs_td.BatchGetDeploymentInstancesOutputTypeDef",
    ) -> "dc_td.BatchGetDeploymentInstancesOutput":
        return dc_td.BatchGetDeploymentInstancesOutput.make_one(res)

    def batch_get_deployment_targets(
        self,
        res: "bs_td.BatchGetDeploymentTargetsOutputTypeDef",
    ) -> "dc_td.BatchGetDeploymentTargetsOutput":
        return dc_td.BatchGetDeploymentTargetsOutput.make_one(res)

    def batch_get_deployments(
        self,
        res: "bs_td.BatchGetDeploymentsOutputTypeDef",
    ) -> "dc_td.BatchGetDeploymentsOutput":
        return dc_td.BatchGetDeploymentsOutput.make_one(res)

    def batch_get_on_premises_instances(
        self,
        res: "bs_td.BatchGetOnPremisesInstancesOutputTypeDef",
    ) -> "dc_td.BatchGetOnPremisesInstancesOutput":
        return dc_td.BatchGetOnPremisesInstancesOutput.make_one(res)

    def continue_deployment(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_application(
        self,
        res: "bs_td.CreateApplicationOutputTypeDef",
    ) -> "dc_td.CreateApplicationOutput":
        return dc_td.CreateApplicationOutput.make_one(res)

    def create_deployment(
        self,
        res: "bs_td.CreateDeploymentOutputTypeDef",
    ) -> "dc_td.CreateDeploymentOutput":
        return dc_td.CreateDeploymentOutput.make_one(res)

    def create_deployment_config(
        self,
        res: "bs_td.CreateDeploymentConfigOutputTypeDef",
    ) -> "dc_td.CreateDeploymentConfigOutput":
        return dc_td.CreateDeploymentConfigOutput.make_one(res)

    def create_deployment_group(
        self,
        res: "bs_td.CreateDeploymentGroupOutputTypeDef",
    ) -> "dc_td.CreateDeploymentGroupOutput":
        return dc_td.CreateDeploymentGroupOutput.make_one(res)

    def delete_application(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_deployment_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_deployment_group(
        self,
        res: "bs_td.DeleteDeploymentGroupOutputTypeDef",
    ) -> "dc_td.DeleteDeploymentGroupOutput":
        return dc_td.DeleteDeploymentGroupOutput.make_one(res)

    def delete_git_hub_account_token(
        self,
        res: "bs_td.DeleteGitHubAccountTokenOutputTypeDef",
    ) -> "dc_td.DeleteGitHubAccountTokenOutput":
        return dc_td.DeleteGitHubAccountTokenOutput.make_one(res)

    def deregister_on_premises_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_application(
        self,
        res: "bs_td.GetApplicationOutputTypeDef",
    ) -> "dc_td.GetApplicationOutput":
        return dc_td.GetApplicationOutput.make_one(res)

    def get_application_revision(
        self,
        res: "bs_td.GetApplicationRevisionOutputTypeDef",
    ) -> "dc_td.GetApplicationRevisionOutput":
        return dc_td.GetApplicationRevisionOutput.make_one(res)

    def get_deployment(
        self,
        res: "bs_td.GetDeploymentOutputTypeDef",
    ) -> "dc_td.GetDeploymentOutput":
        return dc_td.GetDeploymentOutput.make_one(res)

    def get_deployment_config(
        self,
        res: "bs_td.GetDeploymentConfigOutputTypeDef",
    ) -> "dc_td.GetDeploymentConfigOutput":
        return dc_td.GetDeploymentConfigOutput.make_one(res)

    def get_deployment_group(
        self,
        res: "bs_td.GetDeploymentGroupOutputTypeDef",
    ) -> "dc_td.GetDeploymentGroupOutput":
        return dc_td.GetDeploymentGroupOutput.make_one(res)

    def get_deployment_instance(
        self,
        res: "bs_td.GetDeploymentInstanceOutputTypeDef",
    ) -> "dc_td.GetDeploymentInstanceOutput":
        return dc_td.GetDeploymentInstanceOutput.make_one(res)

    def get_deployment_target(
        self,
        res: "bs_td.GetDeploymentTargetOutputTypeDef",
    ) -> "dc_td.GetDeploymentTargetOutput":
        return dc_td.GetDeploymentTargetOutput.make_one(res)

    def get_on_premises_instance(
        self,
        res: "bs_td.GetOnPremisesInstanceOutputTypeDef",
    ) -> "dc_td.GetOnPremisesInstanceOutput":
        return dc_td.GetOnPremisesInstanceOutput.make_one(res)

    def list_application_revisions(
        self,
        res: "bs_td.ListApplicationRevisionsOutputTypeDef",
    ) -> "dc_td.ListApplicationRevisionsOutput":
        return dc_td.ListApplicationRevisionsOutput.make_one(res)

    def list_applications(
        self,
        res: "bs_td.ListApplicationsOutputTypeDef",
    ) -> "dc_td.ListApplicationsOutput":
        return dc_td.ListApplicationsOutput.make_one(res)

    def list_deployment_configs(
        self,
        res: "bs_td.ListDeploymentConfigsOutputTypeDef",
    ) -> "dc_td.ListDeploymentConfigsOutput":
        return dc_td.ListDeploymentConfigsOutput.make_one(res)

    def list_deployment_groups(
        self,
        res: "bs_td.ListDeploymentGroupsOutputTypeDef",
    ) -> "dc_td.ListDeploymentGroupsOutput":
        return dc_td.ListDeploymentGroupsOutput.make_one(res)

    def list_deployment_instances(
        self,
        res: "bs_td.ListDeploymentInstancesOutputTypeDef",
    ) -> "dc_td.ListDeploymentInstancesOutput":
        return dc_td.ListDeploymentInstancesOutput.make_one(res)

    def list_deployment_targets(
        self,
        res: "bs_td.ListDeploymentTargetsOutputTypeDef",
    ) -> "dc_td.ListDeploymentTargetsOutput":
        return dc_td.ListDeploymentTargetsOutput.make_one(res)

    def list_deployments(
        self,
        res: "bs_td.ListDeploymentsOutputTypeDef",
    ) -> "dc_td.ListDeploymentsOutput":
        return dc_td.ListDeploymentsOutput.make_one(res)

    def list_git_hub_account_token_names(
        self,
        res: "bs_td.ListGitHubAccountTokenNamesOutputTypeDef",
    ) -> "dc_td.ListGitHubAccountTokenNamesOutput":
        return dc_td.ListGitHubAccountTokenNamesOutput.make_one(res)

    def list_on_premises_instances(
        self,
        res: "bs_td.ListOnPremisesInstancesOutputTypeDef",
    ) -> "dc_td.ListOnPremisesInstancesOutput":
        return dc_td.ListOnPremisesInstancesOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def put_lifecycle_event_hook_execution_status(
        self,
        res: "bs_td.PutLifecycleEventHookExecutionStatusOutputTypeDef",
    ) -> "dc_td.PutLifecycleEventHookExecutionStatusOutput":
        return dc_td.PutLifecycleEventHookExecutionStatusOutput.make_one(res)

    def register_application_revision(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def register_on_premises_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def remove_tags_from_on_premises_instances(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def skip_wait_time_for_instance_termination(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_deployment(
        self,
        res: "bs_td.StopDeploymentOutputTypeDef",
    ) -> "dc_td.StopDeploymentOutput":
        return dc_td.StopDeploymentOutput.make_one(res)

    def update_application(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_deployment_group(
        self,
        res: "bs_td.UpdateDeploymentGroupOutputTypeDef",
    ) -> "dc_td.UpdateDeploymentGroupOutput":
        return dc_td.UpdateDeploymentGroupOutput.make_one(res)


codedeploy_caster = CODEDEPLOYCaster()
