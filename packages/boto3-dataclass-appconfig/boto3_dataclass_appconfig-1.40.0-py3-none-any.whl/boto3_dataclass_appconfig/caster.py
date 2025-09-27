# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_appconfig import type_defs as bs_td


class APPCONFIGCaster:

    def create_application(
        self,
        res: "bs_td.ApplicationResponseTypeDef",
    ) -> "dc_td.ApplicationResponse":
        return dc_td.ApplicationResponse.make_one(res)

    def create_configuration_profile(
        self,
        res: "bs_td.ConfigurationProfileTypeDef",
    ) -> "dc_td.ConfigurationProfile":
        return dc_td.ConfigurationProfile.make_one(res)

    def create_deployment_strategy(
        self,
        res: "bs_td.DeploymentStrategyResponseTypeDef",
    ) -> "dc_td.DeploymentStrategyResponse":
        return dc_td.DeploymentStrategyResponse.make_one(res)

    def create_environment(
        self,
        res: "bs_td.EnvironmentResponseTypeDef",
    ) -> "dc_td.EnvironmentResponse":
        return dc_td.EnvironmentResponse.make_one(res)

    def create_extension(
        self,
        res: "bs_td.ExtensionTypeDef",
    ) -> "dc_td.Extension":
        return dc_td.Extension.make_one(res)

    def create_extension_association(
        self,
        res: "bs_td.ExtensionAssociationTypeDef",
    ) -> "dc_td.ExtensionAssociation":
        return dc_td.ExtensionAssociation.make_one(res)

    def create_hosted_configuration_version(
        self,
        res: "bs_td.HostedConfigurationVersionTypeDef",
    ) -> "dc_td.HostedConfigurationVersion":
        return dc_td.HostedConfigurationVersion.make_one(res)

    def delete_application(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_configuration_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_deployment_strategy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_environment(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_extension(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_extension_association(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_hosted_configuration_version(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_account_settings(
        self,
        res: "bs_td.AccountSettingsTypeDef",
    ) -> "dc_td.AccountSettings":
        return dc_td.AccountSettings.make_one(res)

    def get_application(
        self,
        res: "bs_td.ApplicationResponseTypeDef",
    ) -> "dc_td.ApplicationResponse":
        return dc_td.ApplicationResponse.make_one(res)

    def get_configuration(
        self,
        res: "bs_td.ConfigurationTypeDef",
    ) -> "dc_td.Configuration":
        return dc_td.Configuration.make_one(res)

    def get_configuration_profile(
        self,
        res: "bs_td.ConfigurationProfileTypeDef",
    ) -> "dc_td.ConfigurationProfile":
        return dc_td.ConfigurationProfile.make_one(res)

    def get_deployment(
        self,
        res: "bs_td.DeploymentTypeDef",
    ) -> "dc_td.Deployment":
        return dc_td.Deployment.make_one(res)

    def get_deployment_strategy(
        self,
        res: "bs_td.DeploymentStrategyResponseTypeDef",
    ) -> "dc_td.DeploymentStrategyResponse":
        return dc_td.DeploymentStrategyResponse.make_one(res)

    def get_environment(
        self,
        res: "bs_td.EnvironmentResponseTypeDef",
    ) -> "dc_td.EnvironmentResponse":
        return dc_td.EnvironmentResponse.make_one(res)

    def get_extension(
        self,
        res: "bs_td.ExtensionTypeDef",
    ) -> "dc_td.Extension":
        return dc_td.Extension.make_one(res)

    def get_extension_association(
        self,
        res: "bs_td.ExtensionAssociationTypeDef",
    ) -> "dc_td.ExtensionAssociation":
        return dc_td.ExtensionAssociation.make_one(res)

    def get_hosted_configuration_version(
        self,
        res: "bs_td.HostedConfigurationVersionTypeDef",
    ) -> "dc_td.HostedConfigurationVersion":
        return dc_td.HostedConfigurationVersion.make_one(res)

    def list_applications(
        self,
        res: "bs_td.ApplicationsTypeDef",
    ) -> "dc_td.Applications":
        return dc_td.Applications.make_one(res)

    def list_configuration_profiles(
        self,
        res: "bs_td.ConfigurationProfilesTypeDef",
    ) -> "dc_td.ConfigurationProfiles":
        return dc_td.ConfigurationProfiles.make_one(res)

    def list_deployment_strategies(
        self,
        res: "bs_td.DeploymentStrategiesTypeDef",
    ) -> "dc_td.DeploymentStrategies":
        return dc_td.DeploymentStrategies.make_one(res)

    def list_deployments(
        self,
        res: "bs_td.DeploymentsTypeDef",
    ) -> "dc_td.Deployments":
        return dc_td.Deployments.make_one(res)

    def list_environments(
        self,
        res: "bs_td.EnvironmentsTypeDef",
    ) -> "dc_td.Environments":
        return dc_td.Environments.make_one(res)

    def list_extension_associations(
        self,
        res: "bs_td.ExtensionAssociationsTypeDef",
    ) -> "dc_td.ExtensionAssociations":
        return dc_td.ExtensionAssociations.make_one(res)

    def list_extensions(
        self,
        res: "bs_td.ExtensionsTypeDef",
    ) -> "dc_td.Extensions":
        return dc_td.Extensions.make_one(res)

    def list_hosted_configuration_versions(
        self,
        res: "bs_td.HostedConfigurationVersionsTypeDef",
    ) -> "dc_td.HostedConfigurationVersions":
        return dc_td.HostedConfigurationVersions.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ResourceTagsTypeDef",
    ) -> "dc_td.ResourceTags":
        return dc_td.ResourceTags.make_one(res)

    def start_deployment(
        self,
        res: "bs_td.DeploymentTypeDef",
    ) -> "dc_td.Deployment":
        return dc_td.Deployment.make_one(res)

    def stop_deployment(
        self,
        res: "bs_td.DeploymentTypeDef",
    ) -> "dc_td.Deployment":
        return dc_td.Deployment.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_account_settings(
        self,
        res: "bs_td.AccountSettingsTypeDef",
    ) -> "dc_td.AccountSettings":
        return dc_td.AccountSettings.make_one(res)

    def update_application(
        self,
        res: "bs_td.ApplicationResponseTypeDef",
    ) -> "dc_td.ApplicationResponse":
        return dc_td.ApplicationResponse.make_one(res)

    def update_configuration_profile(
        self,
        res: "bs_td.ConfigurationProfileTypeDef",
    ) -> "dc_td.ConfigurationProfile":
        return dc_td.ConfigurationProfile.make_one(res)

    def update_deployment_strategy(
        self,
        res: "bs_td.DeploymentStrategyResponseTypeDef",
    ) -> "dc_td.DeploymentStrategyResponse":
        return dc_td.DeploymentStrategyResponse.make_one(res)

    def update_environment(
        self,
        res: "bs_td.EnvironmentResponseTypeDef",
    ) -> "dc_td.EnvironmentResponse":
        return dc_td.EnvironmentResponse.make_one(res)

    def update_extension(
        self,
        res: "bs_td.ExtensionTypeDef",
    ) -> "dc_td.Extension":
        return dc_td.Extension.make_one(res)

    def update_extension_association(
        self,
        res: "bs_td.ExtensionAssociationTypeDef",
    ) -> "dc_td.ExtensionAssociation":
        return dc_td.ExtensionAssociation.make_one(res)

    def validate_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


appconfig_caster = APPCONFIGCaster()
