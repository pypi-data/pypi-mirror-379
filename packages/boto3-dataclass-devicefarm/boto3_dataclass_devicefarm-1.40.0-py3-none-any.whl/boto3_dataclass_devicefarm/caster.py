# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_devicefarm import type_defs as bs_td


class DEVICEFARMCaster:

    def create_device_pool(
        self,
        res: "bs_td.CreateDevicePoolResultTypeDef",
    ) -> "dc_td.CreateDevicePoolResult":
        return dc_td.CreateDevicePoolResult.make_one(res)

    def create_instance_profile(
        self,
        res: "bs_td.CreateInstanceProfileResultTypeDef",
    ) -> "dc_td.CreateInstanceProfileResult":
        return dc_td.CreateInstanceProfileResult.make_one(res)

    def create_network_profile(
        self,
        res: "bs_td.CreateNetworkProfileResultTypeDef",
    ) -> "dc_td.CreateNetworkProfileResult":
        return dc_td.CreateNetworkProfileResult.make_one(res)

    def create_project(
        self,
        res: "bs_td.CreateProjectResultTypeDef",
    ) -> "dc_td.CreateProjectResult":
        return dc_td.CreateProjectResult.make_one(res)

    def create_remote_access_session(
        self,
        res: "bs_td.CreateRemoteAccessSessionResultTypeDef",
    ) -> "dc_td.CreateRemoteAccessSessionResult":
        return dc_td.CreateRemoteAccessSessionResult.make_one(res)

    def create_test_grid_project(
        self,
        res: "bs_td.CreateTestGridProjectResultTypeDef",
    ) -> "dc_td.CreateTestGridProjectResult":
        return dc_td.CreateTestGridProjectResult.make_one(res)

    def create_test_grid_url(
        self,
        res: "bs_td.CreateTestGridUrlResultTypeDef",
    ) -> "dc_td.CreateTestGridUrlResult":
        return dc_td.CreateTestGridUrlResult.make_one(res)

    def create_upload(
        self,
        res: "bs_td.CreateUploadResultTypeDef",
    ) -> "dc_td.CreateUploadResult":
        return dc_td.CreateUploadResult.make_one(res)

    def create_vpce_configuration(
        self,
        res: "bs_td.CreateVPCEConfigurationResultTypeDef",
    ) -> "dc_td.CreateVPCEConfigurationResult":
        return dc_td.CreateVPCEConfigurationResult.make_one(res)

    def get_account_settings(
        self,
        res: "bs_td.GetAccountSettingsResultTypeDef",
    ) -> "dc_td.GetAccountSettingsResult":
        return dc_td.GetAccountSettingsResult.make_one(res)

    def get_device(
        self,
        res: "bs_td.GetDeviceResultTypeDef",
    ) -> "dc_td.GetDeviceResult":
        return dc_td.GetDeviceResult.make_one(res)

    def get_device_instance(
        self,
        res: "bs_td.GetDeviceInstanceResultTypeDef",
    ) -> "dc_td.GetDeviceInstanceResult":
        return dc_td.GetDeviceInstanceResult.make_one(res)

    def get_device_pool(
        self,
        res: "bs_td.GetDevicePoolResultTypeDef",
    ) -> "dc_td.GetDevicePoolResult":
        return dc_td.GetDevicePoolResult.make_one(res)

    def get_device_pool_compatibility(
        self,
        res: "bs_td.GetDevicePoolCompatibilityResultTypeDef",
    ) -> "dc_td.GetDevicePoolCompatibilityResult":
        return dc_td.GetDevicePoolCompatibilityResult.make_one(res)

    def get_instance_profile(
        self,
        res: "bs_td.GetInstanceProfileResultTypeDef",
    ) -> "dc_td.GetInstanceProfileResult":
        return dc_td.GetInstanceProfileResult.make_one(res)

    def get_job(
        self,
        res: "bs_td.GetJobResultTypeDef",
    ) -> "dc_td.GetJobResult":
        return dc_td.GetJobResult.make_one(res)

    def get_network_profile(
        self,
        res: "bs_td.GetNetworkProfileResultTypeDef",
    ) -> "dc_td.GetNetworkProfileResult":
        return dc_td.GetNetworkProfileResult.make_one(res)

    def get_offering_status(
        self,
        res: "bs_td.GetOfferingStatusResultTypeDef",
    ) -> "dc_td.GetOfferingStatusResult":
        return dc_td.GetOfferingStatusResult.make_one(res)

    def get_project(
        self,
        res: "bs_td.GetProjectResultTypeDef",
    ) -> "dc_td.GetProjectResult":
        return dc_td.GetProjectResult.make_one(res)

    def get_remote_access_session(
        self,
        res: "bs_td.GetRemoteAccessSessionResultTypeDef",
    ) -> "dc_td.GetRemoteAccessSessionResult":
        return dc_td.GetRemoteAccessSessionResult.make_one(res)

    def get_run(
        self,
        res: "bs_td.GetRunResultTypeDef",
    ) -> "dc_td.GetRunResult":
        return dc_td.GetRunResult.make_one(res)

    def get_suite(
        self,
        res: "bs_td.GetSuiteResultTypeDef",
    ) -> "dc_td.GetSuiteResult":
        return dc_td.GetSuiteResult.make_one(res)

    def get_test(
        self,
        res: "bs_td.GetTestResultTypeDef",
    ) -> "dc_td.GetTestResult":
        return dc_td.GetTestResult.make_one(res)

    def get_test_grid_project(
        self,
        res: "bs_td.GetTestGridProjectResultTypeDef",
    ) -> "dc_td.GetTestGridProjectResult":
        return dc_td.GetTestGridProjectResult.make_one(res)

    def get_test_grid_session(
        self,
        res: "bs_td.GetTestGridSessionResultTypeDef",
    ) -> "dc_td.GetTestGridSessionResult":
        return dc_td.GetTestGridSessionResult.make_one(res)

    def get_upload(
        self,
        res: "bs_td.GetUploadResultTypeDef",
    ) -> "dc_td.GetUploadResult":
        return dc_td.GetUploadResult.make_one(res)

    def get_vpce_configuration(
        self,
        res: "bs_td.GetVPCEConfigurationResultTypeDef",
    ) -> "dc_td.GetVPCEConfigurationResult":
        return dc_td.GetVPCEConfigurationResult.make_one(res)

    def install_to_remote_access_session(
        self,
        res: "bs_td.InstallToRemoteAccessSessionResultTypeDef",
    ) -> "dc_td.InstallToRemoteAccessSessionResult":
        return dc_td.InstallToRemoteAccessSessionResult.make_one(res)

    def list_artifacts(
        self,
        res: "bs_td.ListArtifactsResultTypeDef",
    ) -> "dc_td.ListArtifactsResult":
        return dc_td.ListArtifactsResult.make_one(res)

    def list_device_instances(
        self,
        res: "bs_td.ListDeviceInstancesResultTypeDef",
    ) -> "dc_td.ListDeviceInstancesResult":
        return dc_td.ListDeviceInstancesResult.make_one(res)

    def list_device_pools(
        self,
        res: "bs_td.ListDevicePoolsResultTypeDef",
    ) -> "dc_td.ListDevicePoolsResult":
        return dc_td.ListDevicePoolsResult.make_one(res)

    def list_devices(
        self,
        res: "bs_td.ListDevicesResultTypeDef",
    ) -> "dc_td.ListDevicesResult":
        return dc_td.ListDevicesResult.make_one(res)

    def list_instance_profiles(
        self,
        res: "bs_td.ListInstanceProfilesResultTypeDef",
    ) -> "dc_td.ListInstanceProfilesResult":
        return dc_td.ListInstanceProfilesResult.make_one(res)

    def list_jobs(
        self,
        res: "bs_td.ListJobsResultTypeDef",
    ) -> "dc_td.ListJobsResult":
        return dc_td.ListJobsResult.make_one(res)

    def list_network_profiles(
        self,
        res: "bs_td.ListNetworkProfilesResultTypeDef",
    ) -> "dc_td.ListNetworkProfilesResult":
        return dc_td.ListNetworkProfilesResult.make_one(res)

    def list_offering_promotions(
        self,
        res: "bs_td.ListOfferingPromotionsResultTypeDef",
    ) -> "dc_td.ListOfferingPromotionsResult":
        return dc_td.ListOfferingPromotionsResult.make_one(res)

    def list_offering_transactions(
        self,
        res: "bs_td.ListOfferingTransactionsResultTypeDef",
    ) -> "dc_td.ListOfferingTransactionsResult":
        return dc_td.ListOfferingTransactionsResult.make_one(res)

    def list_offerings(
        self,
        res: "bs_td.ListOfferingsResultTypeDef",
    ) -> "dc_td.ListOfferingsResult":
        return dc_td.ListOfferingsResult.make_one(res)

    def list_projects(
        self,
        res: "bs_td.ListProjectsResultTypeDef",
    ) -> "dc_td.ListProjectsResult":
        return dc_td.ListProjectsResult.make_one(res)

    def list_remote_access_sessions(
        self,
        res: "bs_td.ListRemoteAccessSessionsResultTypeDef",
    ) -> "dc_td.ListRemoteAccessSessionsResult":
        return dc_td.ListRemoteAccessSessionsResult.make_one(res)

    def list_runs(
        self,
        res: "bs_td.ListRunsResultTypeDef",
    ) -> "dc_td.ListRunsResult":
        return dc_td.ListRunsResult.make_one(res)

    def list_samples(
        self,
        res: "bs_td.ListSamplesResultTypeDef",
    ) -> "dc_td.ListSamplesResult":
        return dc_td.ListSamplesResult.make_one(res)

    def list_suites(
        self,
        res: "bs_td.ListSuitesResultTypeDef",
    ) -> "dc_td.ListSuitesResult":
        return dc_td.ListSuitesResult.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_test_grid_projects(
        self,
        res: "bs_td.ListTestGridProjectsResultTypeDef",
    ) -> "dc_td.ListTestGridProjectsResult":
        return dc_td.ListTestGridProjectsResult.make_one(res)

    def list_test_grid_session_actions(
        self,
        res: "bs_td.ListTestGridSessionActionsResultTypeDef",
    ) -> "dc_td.ListTestGridSessionActionsResult":
        return dc_td.ListTestGridSessionActionsResult.make_one(res)

    def list_test_grid_session_artifacts(
        self,
        res: "bs_td.ListTestGridSessionArtifactsResultTypeDef",
    ) -> "dc_td.ListTestGridSessionArtifactsResult":
        return dc_td.ListTestGridSessionArtifactsResult.make_one(res)

    def list_test_grid_sessions(
        self,
        res: "bs_td.ListTestGridSessionsResultTypeDef",
    ) -> "dc_td.ListTestGridSessionsResult":
        return dc_td.ListTestGridSessionsResult.make_one(res)

    def list_tests(
        self,
        res: "bs_td.ListTestsResultTypeDef",
    ) -> "dc_td.ListTestsResult":
        return dc_td.ListTestsResult.make_one(res)

    def list_unique_problems(
        self,
        res: "bs_td.ListUniqueProblemsResultTypeDef",
    ) -> "dc_td.ListUniqueProblemsResult":
        return dc_td.ListUniqueProblemsResult.make_one(res)

    def list_uploads(
        self,
        res: "bs_td.ListUploadsResultTypeDef",
    ) -> "dc_td.ListUploadsResult":
        return dc_td.ListUploadsResult.make_one(res)

    def list_vpce_configurations(
        self,
        res: "bs_td.ListVPCEConfigurationsResultTypeDef",
    ) -> "dc_td.ListVPCEConfigurationsResult":
        return dc_td.ListVPCEConfigurationsResult.make_one(res)

    def purchase_offering(
        self,
        res: "bs_td.PurchaseOfferingResultTypeDef",
    ) -> "dc_td.PurchaseOfferingResult":
        return dc_td.PurchaseOfferingResult.make_one(res)

    def renew_offering(
        self,
        res: "bs_td.RenewOfferingResultTypeDef",
    ) -> "dc_td.RenewOfferingResult":
        return dc_td.RenewOfferingResult.make_one(res)

    def schedule_run(
        self,
        res: "bs_td.ScheduleRunResultTypeDef",
    ) -> "dc_td.ScheduleRunResult":
        return dc_td.ScheduleRunResult.make_one(res)

    def stop_job(
        self,
        res: "bs_td.StopJobResultTypeDef",
    ) -> "dc_td.StopJobResult":
        return dc_td.StopJobResult.make_one(res)

    def stop_remote_access_session(
        self,
        res: "bs_td.StopRemoteAccessSessionResultTypeDef",
    ) -> "dc_td.StopRemoteAccessSessionResult":
        return dc_td.StopRemoteAccessSessionResult.make_one(res)

    def stop_run(
        self,
        res: "bs_td.StopRunResultTypeDef",
    ) -> "dc_td.StopRunResult":
        return dc_td.StopRunResult.make_one(res)

    def update_device_instance(
        self,
        res: "bs_td.UpdateDeviceInstanceResultTypeDef",
    ) -> "dc_td.UpdateDeviceInstanceResult":
        return dc_td.UpdateDeviceInstanceResult.make_one(res)

    def update_device_pool(
        self,
        res: "bs_td.UpdateDevicePoolResultTypeDef",
    ) -> "dc_td.UpdateDevicePoolResult":
        return dc_td.UpdateDevicePoolResult.make_one(res)

    def update_instance_profile(
        self,
        res: "bs_td.UpdateInstanceProfileResultTypeDef",
    ) -> "dc_td.UpdateInstanceProfileResult":
        return dc_td.UpdateInstanceProfileResult.make_one(res)

    def update_network_profile(
        self,
        res: "bs_td.UpdateNetworkProfileResultTypeDef",
    ) -> "dc_td.UpdateNetworkProfileResult":
        return dc_td.UpdateNetworkProfileResult.make_one(res)

    def update_project(
        self,
        res: "bs_td.UpdateProjectResultTypeDef",
    ) -> "dc_td.UpdateProjectResult":
        return dc_td.UpdateProjectResult.make_one(res)

    def update_test_grid_project(
        self,
        res: "bs_td.UpdateTestGridProjectResultTypeDef",
    ) -> "dc_td.UpdateTestGridProjectResult":
        return dc_td.UpdateTestGridProjectResult.make_one(res)

    def update_upload(
        self,
        res: "bs_td.UpdateUploadResultTypeDef",
    ) -> "dc_td.UpdateUploadResult":
        return dc_td.UpdateUploadResult.make_one(res)

    def update_vpce_configuration(
        self,
        res: "bs_td.UpdateVPCEConfigurationResultTypeDef",
    ) -> "dc_td.UpdateVPCEConfigurationResult":
        return dc_td.UpdateVPCEConfigurationResult.make_one(res)


devicefarm_caster = DEVICEFARMCaster()
