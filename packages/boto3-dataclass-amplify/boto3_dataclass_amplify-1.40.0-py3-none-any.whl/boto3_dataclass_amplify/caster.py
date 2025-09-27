# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_amplify import type_defs as bs_td


class AMPLIFYCaster:

    def create_app(
        self,
        res: "bs_td.CreateAppResultTypeDef",
    ) -> "dc_td.CreateAppResult":
        return dc_td.CreateAppResult.make_one(res)

    def create_backend_environment(
        self,
        res: "bs_td.CreateBackendEnvironmentResultTypeDef",
    ) -> "dc_td.CreateBackendEnvironmentResult":
        return dc_td.CreateBackendEnvironmentResult.make_one(res)

    def create_branch(
        self,
        res: "bs_td.CreateBranchResultTypeDef",
    ) -> "dc_td.CreateBranchResult":
        return dc_td.CreateBranchResult.make_one(res)

    def create_deployment(
        self,
        res: "bs_td.CreateDeploymentResultTypeDef",
    ) -> "dc_td.CreateDeploymentResult":
        return dc_td.CreateDeploymentResult.make_one(res)

    def create_domain_association(
        self,
        res: "bs_td.CreateDomainAssociationResultTypeDef",
    ) -> "dc_td.CreateDomainAssociationResult":
        return dc_td.CreateDomainAssociationResult.make_one(res)

    def create_webhook(
        self,
        res: "bs_td.CreateWebhookResultTypeDef",
    ) -> "dc_td.CreateWebhookResult":
        return dc_td.CreateWebhookResult.make_one(res)

    def delete_app(
        self,
        res: "bs_td.DeleteAppResultTypeDef",
    ) -> "dc_td.DeleteAppResult":
        return dc_td.DeleteAppResult.make_one(res)

    def delete_backend_environment(
        self,
        res: "bs_td.DeleteBackendEnvironmentResultTypeDef",
    ) -> "dc_td.DeleteBackendEnvironmentResult":
        return dc_td.DeleteBackendEnvironmentResult.make_one(res)

    def delete_branch(
        self,
        res: "bs_td.DeleteBranchResultTypeDef",
    ) -> "dc_td.DeleteBranchResult":
        return dc_td.DeleteBranchResult.make_one(res)

    def delete_domain_association(
        self,
        res: "bs_td.DeleteDomainAssociationResultTypeDef",
    ) -> "dc_td.DeleteDomainAssociationResult":
        return dc_td.DeleteDomainAssociationResult.make_one(res)

    def delete_job(
        self,
        res: "bs_td.DeleteJobResultTypeDef",
    ) -> "dc_td.DeleteJobResult":
        return dc_td.DeleteJobResult.make_one(res)

    def delete_webhook(
        self,
        res: "bs_td.DeleteWebhookResultTypeDef",
    ) -> "dc_td.DeleteWebhookResult":
        return dc_td.DeleteWebhookResult.make_one(res)

    def generate_access_logs(
        self,
        res: "bs_td.GenerateAccessLogsResultTypeDef",
    ) -> "dc_td.GenerateAccessLogsResult":
        return dc_td.GenerateAccessLogsResult.make_one(res)

    def get_app(
        self,
        res: "bs_td.GetAppResultTypeDef",
    ) -> "dc_td.GetAppResult":
        return dc_td.GetAppResult.make_one(res)

    def get_artifact_url(
        self,
        res: "bs_td.GetArtifactUrlResultTypeDef",
    ) -> "dc_td.GetArtifactUrlResult":
        return dc_td.GetArtifactUrlResult.make_one(res)

    def get_backend_environment(
        self,
        res: "bs_td.GetBackendEnvironmentResultTypeDef",
    ) -> "dc_td.GetBackendEnvironmentResult":
        return dc_td.GetBackendEnvironmentResult.make_one(res)

    def get_branch(
        self,
        res: "bs_td.GetBranchResultTypeDef",
    ) -> "dc_td.GetBranchResult":
        return dc_td.GetBranchResult.make_one(res)

    def get_domain_association(
        self,
        res: "bs_td.GetDomainAssociationResultTypeDef",
    ) -> "dc_td.GetDomainAssociationResult":
        return dc_td.GetDomainAssociationResult.make_one(res)

    def get_job(
        self,
        res: "bs_td.GetJobResultTypeDef",
    ) -> "dc_td.GetJobResult":
        return dc_td.GetJobResult.make_one(res)

    def get_webhook(
        self,
        res: "bs_td.GetWebhookResultTypeDef",
    ) -> "dc_td.GetWebhookResult":
        return dc_td.GetWebhookResult.make_one(res)

    def list_apps(
        self,
        res: "bs_td.ListAppsResultTypeDef",
    ) -> "dc_td.ListAppsResult":
        return dc_td.ListAppsResult.make_one(res)

    def list_artifacts(
        self,
        res: "bs_td.ListArtifactsResultTypeDef",
    ) -> "dc_td.ListArtifactsResult":
        return dc_td.ListArtifactsResult.make_one(res)

    def list_backend_environments(
        self,
        res: "bs_td.ListBackendEnvironmentsResultTypeDef",
    ) -> "dc_td.ListBackendEnvironmentsResult":
        return dc_td.ListBackendEnvironmentsResult.make_one(res)

    def list_branches(
        self,
        res: "bs_td.ListBranchesResultTypeDef",
    ) -> "dc_td.ListBranchesResult":
        return dc_td.ListBranchesResult.make_one(res)

    def list_domain_associations(
        self,
        res: "bs_td.ListDomainAssociationsResultTypeDef",
    ) -> "dc_td.ListDomainAssociationsResult":
        return dc_td.ListDomainAssociationsResult.make_one(res)

    def list_jobs(
        self,
        res: "bs_td.ListJobsResultTypeDef",
    ) -> "dc_td.ListJobsResult":
        return dc_td.ListJobsResult.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_webhooks(
        self,
        res: "bs_td.ListWebhooksResultTypeDef",
    ) -> "dc_td.ListWebhooksResult":
        return dc_td.ListWebhooksResult.make_one(res)

    def start_deployment(
        self,
        res: "bs_td.StartDeploymentResultTypeDef",
    ) -> "dc_td.StartDeploymentResult":
        return dc_td.StartDeploymentResult.make_one(res)

    def start_job(
        self,
        res: "bs_td.StartJobResultTypeDef",
    ) -> "dc_td.StartJobResult":
        return dc_td.StartJobResult.make_one(res)

    def stop_job(
        self,
        res: "bs_td.StopJobResultTypeDef",
    ) -> "dc_td.StopJobResult":
        return dc_td.StopJobResult.make_one(res)

    def update_app(
        self,
        res: "bs_td.UpdateAppResultTypeDef",
    ) -> "dc_td.UpdateAppResult":
        return dc_td.UpdateAppResult.make_one(res)

    def update_branch(
        self,
        res: "bs_td.UpdateBranchResultTypeDef",
    ) -> "dc_td.UpdateBranchResult":
        return dc_td.UpdateBranchResult.make_one(res)

    def update_domain_association(
        self,
        res: "bs_td.UpdateDomainAssociationResultTypeDef",
    ) -> "dc_td.UpdateDomainAssociationResult":
        return dc_td.UpdateDomainAssociationResult.make_one(res)

    def update_webhook(
        self,
        res: "bs_td.UpdateWebhookResultTypeDef",
    ) -> "dc_td.UpdateWebhookResult":
        return dc_td.UpdateWebhookResult.make_one(res)


amplify_caster = AMPLIFYCaster()
