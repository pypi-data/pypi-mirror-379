# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_elasticbeanstalk import type_defs as bs_td


class ELASTICBEANSTALKCaster:

    def abort_environment_update(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def apply_environment_managed_action(
        self,
        res: "bs_td.ApplyEnvironmentManagedActionResultTypeDef",
    ) -> "dc_td.ApplyEnvironmentManagedActionResult":
        return dc_td.ApplyEnvironmentManagedActionResult.make_one(res)

    def associate_environment_operations_role(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def check_dns_availability(
        self,
        res: "bs_td.CheckDNSAvailabilityResultMessageTypeDef",
    ) -> "dc_td.CheckDNSAvailabilityResultMessage":
        return dc_td.CheckDNSAvailabilityResultMessage.make_one(res)

    def compose_environments(
        self,
        res: "bs_td.EnvironmentDescriptionsMessageTypeDef",
    ) -> "dc_td.EnvironmentDescriptionsMessage":
        return dc_td.EnvironmentDescriptionsMessage.make_one(res)

    def create_application(
        self,
        res: "bs_td.ApplicationDescriptionMessageTypeDef",
    ) -> "dc_td.ApplicationDescriptionMessage":
        return dc_td.ApplicationDescriptionMessage.make_one(res)

    def create_application_version(
        self,
        res: "bs_td.ApplicationVersionDescriptionMessageTypeDef",
    ) -> "dc_td.ApplicationVersionDescriptionMessage":
        return dc_td.ApplicationVersionDescriptionMessage.make_one(res)

    def create_configuration_template(
        self,
        res: "bs_td.ConfigurationSettingsDescriptionResponseTypeDef",
    ) -> "dc_td.ConfigurationSettingsDescriptionResponse":
        return dc_td.ConfigurationSettingsDescriptionResponse.make_one(res)

    def create_environment(
        self,
        res: "bs_td.EnvironmentDescriptionResponseTypeDef",
    ) -> "dc_td.EnvironmentDescriptionResponse":
        return dc_td.EnvironmentDescriptionResponse.make_one(res)

    def create_platform_version(
        self,
        res: "bs_td.CreatePlatformVersionResultTypeDef",
    ) -> "dc_td.CreatePlatformVersionResult":
        return dc_td.CreatePlatformVersionResult.make_one(res)

    def create_storage_location(
        self,
        res: "bs_td.CreateStorageLocationResultMessageTypeDef",
    ) -> "dc_td.CreateStorageLocationResultMessage":
        return dc_td.CreateStorageLocationResultMessage.make_one(res)

    def delete_application(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_application_version(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_configuration_template(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_environment_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_platform_version(
        self,
        res: "bs_td.DeletePlatformVersionResultTypeDef",
    ) -> "dc_td.DeletePlatformVersionResult":
        return dc_td.DeletePlatformVersionResult.make_one(res)

    def describe_account_attributes(
        self,
        res: "bs_td.DescribeAccountAttributesResultTypeDef",
    ) -> "dc_td.DescribeAccountAttributesResult":
        return dc_td.DescribeAccountAttributesResult.make_one(res)

    def describe_application_versions(
        self,
        res: "bs_td.ApplicationVersionDescriptionsMessageTypeDef",
    ) -> "dc_td.ApplicationVersionDescriptionsMessage":
        return dc_td.ApplicationVersionDescriptionsMessage.make_one(res)

    def describe_applications(
        self,
        res: "bs_td.ApplicationDescriptionsMessageTypeDef",
    ) -> "dc_td.ApplicationDescriptionsMessage":
        return dc_td.ApplicationDescriptionsMessage.make_one(res)

    def describe_configuration_options(
        self,
        res: "bs_td.ConfigurationOptionsDescriptionTypeDef",
    ) -> "dc_td.ConfigurationOptionsDescription":
        return dc_td.ConfigurationOptionsDescription.make_one(res)

    def describe_configuration_settings(
        self,
        res: "bs_td.ConfigurationSettingsDescriptionsTypeDef",
    ) -> "dc_td.ConfigurationSettingsDescriptions":
        return dc_td.ConfigurationSettingsDescriptions.make_one(res)

    def describe_environment_health(
        self,
        res: "bs_td.DescribeEnvironmentHealthResultTypeDef",
    ) -> "dc_td.DescribeEnvironmentHealthResult":
        return dc_td.DescribeEnvironmentHealthResult.make_one(res)

    def describe_environment_managed_action_history(
        self,
        res: "bs_td.DescribeEnvironmentManagedActionHistoryResultTypeDef",
    ) -> "dc_td.DescribeEnvironmentManagedActionHistoryResult":
        return dc_td.DescribeEnvironmentManagedActionHistoryResult.make_one(res)

    def describe_environment_managed_actions(
        self,
        res: "bs_td.DescribeEnvironmentManagedActionsResultTypeDef",
    ) -> "dc_td.DescribeEnvironmentManagedActionsResult":
        return dc_td.DescribeEnvironmentManagedActionsResult.make_one(res)

    def describe_environment_resources(
        self,
        res: "bs_td.EnvironmentResourceDescriptionsMessageTypeDef",
    ) -> "dc_td.EnvironmentResourceDescriptionsMessage":
        return dc_td.EnvironmentResourceDescriptionsMessage.make_one(res)

    def describe_environments(
        self,
        res: "bs_td.EnvironmentDescriptionsMessageTypeDef",
    ) -> "dc_td.EnvironmentDescriptionsMessage":
        return dc_td.EnvironmentDescriptionsMessage.make_one(res)

    def describe_events(
        self,
        res: "bs_td.EventDescriptionsMessageTypeDef",
    ) -> "dc_td.EventDescriptionsMessage":
        return dc_td.EventDescriptionsMessage.make_one(res)

    def describe_instances_health(
        self,
        res: "bs_td.DescribeInstancesHealthResultTypeDef",
    ) -> "dc_td.DescribeInstancesHealthResult":
        return dc_td.DescribeInstancesHealthResult.make_one(res)

    def describe_platform_version(
        self,
        res: "bs_td.DescribePlatformVersionResultTypeDef",
    ) -> "dc_td.DescribePlatformVersionResult":
        return dc_td.DescribePlatformVersionResult.make_one(res)

    def disassociate_environment_operations_role(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def list_available_solution_stacks(
        self,
        res: "bs_td.ListAvailableSolutionStacksResultMessageTypeDef",
    ) -> "dc_td.ListAvailableSolutionStacksResultMessage":
        return dc_td.ListAvailableSolutionStacksResultMessage.make_one(res)

    def list_platform_branches(
        self,
        res: "bs_td.ListPlatformBranchesResultTypeDef",
    ) -> "dc_td.ListPlatformBranchesResult":
        return dc_td.ListPlatformBranchesResult.make_one(res)

    def list_platform_versions(
        self,
        res: "bs_td.ListPlatformVersionsResultTypeDef",
    ) -> "dc_td.ListPlatformVersionsResult":
        return dc_td.ListPlatformVersionsResult.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ResourceTagsDescriptionMessageTypeDef",
    ) -> "dc_td.ResourceTagsDescriptionMessage":
        return dc_td.ResourceTagsDescriptionMessage.make_one(res)

    def rebuild_environment(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def request_environment_info(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def restart_app_server(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def retrieve_environment_info(
        self,
        res: "bs_td.RetrieveEnvironmentInfoResultMessageTypeDef",
    ) -> "dc_td.RetrieveEnvironmentInfoResultMessage":
        return dc_td.RetrieveEnvironmentInfoResultMessage.make_one(res)

    def swap_environment_cnames(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def terminate_environment(
        self,
        res: "bs_td.EnvironmentDescriptionResponseTypeDef",
    ) -> "dc_td.EnvironmentDescriptionResponse":
        return dc_td.EnvironmentDescriptionResponse.make_one(res)

    def update_application(
        self,
        res: "bs_td.ApplicationDescriptionMessageTypeDef",
    ) -> "dc_td.ApplicationDescriptionMessage":
        return dc_td.ApplicationDescriptionMessage.make_one(res)

    def update_application_resource_lifecycle(
        self,
        res: "bs_td.ApplicationResourceLifecycleDescriptionMessageTypeDef",
    ) -> "dc_td.ApplicationResourceLifecycleDescriptionMessage":
        return dc_td.ApplicationResourceLifecycleDescriptionMessage.make_one(res)

    def update_application_version(
        self,
        res: "bs_td.ApplicationVersionDescriptionMessageTypeDef",
    ) -> "dc_td.ApplicationVersionDescriptionMessage":
        return dc_td.ApplicationVersionDescriptionMessage.make_one(res)

    def update_configuration_template(
        self,
        res: "bs_td.ConfigurationSettingsDescriptionResponseTypeDef",
    ) -> "dc_td.ConfigurationSettingsDescriptionResponse":
        return dc_td.ConfigurationSettingsDescriptionResponse.make_one(res)

    def update_environment(
        self,
        res: "bs_td.EnvironmentDescriptionResponseTypeDef",
    ) -> "dc_td.EnvironmentDescriptionResponse":
        return dc_td.EnvironmentDescriptionResponse.make_one(res)

    def update_tags_for_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def validate_configuration_settings(
        self,
        res: "bs_td.ConfigurationSettingsValidationMessagesTypeDef",
    ) -> "dc_td.ConfigurationSettingsValidationMessages":
        return dc_td.ConfigurationSettingsValidationMessages.make_one(res)


elasticbeanstalk_caster = ELASTICBEANSTALKCaster()
