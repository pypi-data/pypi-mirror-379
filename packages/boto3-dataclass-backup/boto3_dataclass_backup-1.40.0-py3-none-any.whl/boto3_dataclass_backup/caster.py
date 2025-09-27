# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_backup import type_defs as bs_td


class BACKUPCaster:

    def associate_backup_vault_mpa_approval_team(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_backup_plan(
        self,
        res: "bs_td.CreateBackupPlanOutputTypeDef",
    ) -> "dc_td.CreateBackupPlanOutput":
        return dc_td.CreateBackupPlanOutput.make_one(res)

    def create_backup_selection(
        self,
        res: "bs_td.CreateBackupSelectionOutputTypeDef",
    ) -> "dc_td.CreateBackupSelectionOutput":
        return dc_td.CreateBackupSelectionOutput.make_one(res)

    def create_backup_vault(
        self,
        res: "bs_td.CreateBackupVaultOutputTypeDef",
    ) -> "dc_td.CreateBackupVaultOutput":
        return dc_td.CreateBackupVaultOutput.make_one(res)

    def create_framework(
        self,
        res: "bs_td.CreateFrameworkOutputTypeDef",
    ) -> "dc_td.CreateFrameworkOutput":
        return dc_td.CreateFrameworkOutput.make_one(res)

    def create_legal_hold(
        self,
        res: "bs_td.CreateLegalHoldOutputTypeDef",
    ) -> "dc_td.CreateLegalHoldOutput":
        return dc_td.CreateLegalHoldOutput.make_one(res)

    def create_logically_air_gapped_backup_vault(
        self,
        res: "bs_td.CreateLogicallyAirGappedBackupVaultOutputTypeDef",
    ) -> "dc_td.CreateLogicallyAirGappedBackupVaultOutput":
        return dc_td.CreateLogicallyAirGappedBackupVaultOutput.make_one(res)

    def create_report_plan(
        self,
        res: "bs_td.CreateReportPlanOutputTypeDef",
    ) -> "dc_td.CreateReportPlanOutput":
        return dc_td.CreateReportPlanOutput.make_one(res)

    def create_restore_access_backup_vault(
        self,
        res: "bs_td.CreateRestoreAccessBackupVaultOutputTypeDef",
    ) -> "dc_td.CreateRestoreAccessBackupVaultOutput":
        return dc_td.CreateRestoreAccessBackupVaultOutput.make_one(res)

    def create_restore_testing_plan(
        self,
        res: "bs_td.CreateRestoreTestingPlanOutputTypeDef",
    ) -> "dc_td.CreateRestoreTestingPlanOutput":
        return dc_td.CreateRestoreTestingPlanOutput.make_one(res)

    def create_restore_testing_selection(
        self,
        res: "bs_td.CreateRestoreTestingSelectionOutputTypeDef",
    ) -> "dc_td.CreateRestoreTestingSelectionOutput":
        return dc_td.CreateRestoreTestingSelectionOutput.make_one(res)

    def delete_backup_plan(
        self,
        res: "bs_td.DeleteBackupPlanOutputTypeDef",
    ) -> "dc_td.DeleteBackupPlanOutput":
        return dc_td.DeleteBackupPlanOutput.make_one(res)

    def delete_backup_selection(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_backup_vault(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_backup_vault_access_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_backup_vault_lock_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_backup_vault_notifications(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_framework(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_recovery_point(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_report_plan(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_restore_testing_plan(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_restore_testing_selection(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_backup_job(
        self,
        res: "bs_td.DescribeBackupJobOutputTypeDef",
    ) -> "dc_td.DescribeBackupJobOutput":
        return dc_td.DescribeBackupJobOutput.make_one(res)

    def describe_backup_vault(
        self,
        res: "bs_td.DescribeBackupVaultOutputTypeDef",
    ) -> "dc_td.DescribeBackupVaultOutput":
        return dc_td.DescribeBackupVaultOutput.make_one(res)

    def describe_copy_job(
        self,
        res: "bs_td.DescribeCopyJobOutputTypeDef",
    ) -> "dc_td.DescribeCopyJobOutput":
        return dc_td.DescribeCopyJobOutput.make_one(res)

    def describe_framework(
        self,
        res: "bs_td.DescribeFrameworkOutputTypeDef",
    ) -> "dc_td.DescribeFrameworkOutput":
        return dc_td.DescribeFrameworkOutput.make_one(res)

    def describe_global_settings(
        self,
        res: "bs_td.DescribeGlobalSettingsOutputTypeDef",
    ) -> "dc_td.DescribeGlobalSettingsOutput":
        return dc_td.DescribeGlobalSettingsOutput.make_one(res)

    def describe_protected_resource(
        self,
        res: "bs_td.DescribeProtectedResourceOutputTypeDef",
    ) -> "dc_td.DescribeProtectedResourceOutput":
        return dc_td.DescribeProtectedResourceOutput.make_one(res)

    def describe_recovery_point(
        self,
        res: "bs_td.DescribeRecoveryPointOutputTypeDef",
    ) -> "dc_td.DescribeRecoveryPointOutput":
        return dc_td.DescribeRecoveryPointOutput.make_one(res)

    def describe_region_settings(
        self,
        res: "bs_td.DescribeRegionSettingsOutputTypeDef",
    ) -> "dc_td.DescribeRegionSettingsOutput":
        return dc_td.DescribeRegionSettingsOutput.make_one(res)

    def describe_report_job(
        self,
        res: "bs_td.DescribeReportJobOutputTypeDef",
    ) -> "dc_td.DescribeReportJobOutput":
        return dc_td.DescribeReportJobOutput.make_one(res)

    def describe_report_plan(
        self,
        res: "bs_td.DescribeReportPlanOutputTypeDef",
    ) -> "dc_td.DescribeReportPlanOutput":
        return dc_td.DescribeReportPlanOutput.make_one(res)

    def describe_restore_job(
        self,
        res: "bs_td.DescribeRestoreJobOutputTypeDef",
    ) -> "dc_td.DescribeRestoreJobOutput":
        return dc_td.DescribeRestoreJobOutput.make_one(res)

    def disassociate_backup_vault_mpa_approval_team(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_recovery_point(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_recovery_point_from_parent(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def export_backup_plan_template(
        self,
        res: "bs_td.ExportBackupPlanTemplateOutputTypeDef",
    ) -> "dc_td.ExportBackupPlanTemplateOutput":
        return dc_td.ExportBackupPlanTemplateOutput.make_one(res)

    def get_backup_plan(
        self,
        res: "bs_td.GetBackupPlanOutputTypeDef",
    ) -> "dc_td.GetBackupPlanOutput":
        return dc_td.GetBackupPlanOutput.make_one(res)

    def get_backup_plan_from_json(
        self,
        res: "bs_td.GetBackupPlanFromJSONOutputTypeDef",
    ) -> "dc_td.GetBackupPlanFromJSONOutput":
        return dc_td.GetBackupPlanFromJSONOutput.make_one(res)

    def get_backup_plan_from_template(
        self,
        res: "bs_td.GetBackupPlanFromTemplateOutputTypeDef",
    ) -> "dc_td.GetBackupPlanFromTemplateOutput":
        return dc_td.GetBackupPlanFromTemplateOutput.make_one(res)

    def get_backup_selection(
        self,
        res: "bs_td.GetBackupSelectionOutputTypeDef",
    ) -> "dc_td.GetBackupSelectionOutput":
        return dc_td.GetBackupSelectionOutput.make_one(res)

    def get_backup_vault_access_policy(
        self,
        res: "bs_td.GetBackupVaultAccessPolicyOutputTypeDef",
    ) -> "dc_td.GetBackupVaultAccessPolicyOutput":
        return dc_td.GetBackupVaultAccessPolicyOutput.make_one(res)

    def get_backup_vault_notifications(
        self,
        res: "bs_td.GetBackupVaultNotificationsOutputTypeDef",
    ) -> "dc_td.GetBackupVaultNotificationsOutput":
        return dc_td.GetBackupVaultNotificationsOutput.make_one(res)

    def get_legal_hold(
        self,
        res: "bs_td.GetLegalHoldOutputTypeDef",
    ) -> "dc_td.GetLegalHoldOutput":
        return dc_td.GetLegalHoldOutput.make_one(res)

    def get_recovery_point_index_details(
        self,
        res: "bs_td.GetRecoveryPointIndexDetailsOutputTypeDef",
    ) -> "dc_td.GetRecoveryPointIndexDetailsOutput":
        return dc_td.GetRecoveryPointIndexDetailsOutput.make_one(res)

    def get_recovery_point_restore_metadata(
        self,
        res: "bs_td.GetRecoveryPointRestoreMetadataOutputTypeDef",
    ) -> "dc_td.GetRecoveryPointRestoreMetadataOutput":
        return dc_td.GetRecoveryPointRestoreMetadataOutput.make_one(res)

    def get_restore_job_metadata(
        self,
        res: "bs_td.GetRestoreJobMetadataOutputTypeDef",
    ) -> "dc_td.GetRestoreJobMetadataOutput":
        return dc_td.GetRestoreJobMetadataOutput.make_one(res)

    def get_restore_testing_inferred_metadata(
        self,
        res: "bs_td.GetRestoreTestingInferredMetadataOutputTypeDef",
    ) -> "dc_td.GetRestoreTestingInferredMetadataOutput":
        return dc_td.GetRestoreTestingInferredMetadataOutput.make_one(res)

    def get_restore_testing_plan(
        self,
        res: "bs_td.GetRestoreTestingPlanOutputTypeDef",
    ) -> "dc_td.GetRestoreTestingPlanOutput":
        return dc_td.GetRestoreTestingPlanOutput.make_one(res)

    def get_restore_testing_selection(
        self,
        res: "bs_td.GetRestoreTestingSelectionOutputTypeDef",
    ) -> "dc_td.GetRestoreTestingSelectionOutput":
        return dc_td.GetRestoreTestingSelectionOutput.make_one(res)

    def get_supported_resource_types(
        self,
        res: "bs_td.GetSupportedResourceTypesOutputTypeDef",
    ) -> "dc_td.GetSupportedResourceTypesOutput":
        return dc_td.GetSupportedResourceTypesOutput.make_one(res)

    def list_backup_job_summaries(
        self,
        res: "bs_td.ListBackupJobSummariesOutputTypeDef",
    ) -> "dc_td.ListBackupJobSummariesOutput":
        return dc_td.ListBackupJobSummariesOutput.make_one(res)

    def list_backup_jobs(
        self,
        res: "bs_td.ListBackupJobsOutputTypeDef",
    ) -> "dc_td.ListBackupJobsOutput":
        return dc_td.ListBackupJobsOutput.make_one(res)

    def list_backup_plan_templates(
        self,
        res: "bs_td.ListBackupPlanTemplatesOutputTypeDef",
    ) -> "dc_td.ListBackupPlanTemplatesOutput":
        return dc_td.ListBackupPlanTemplatesOutput.make_one(res)

    def list_backup_plan_versions(
        self,
        res: "bs_td.ListBackupPlanVersionsOutputTypeDef",
    ) -> "dc_td.ListBackupPlanVersionsOutput":
        return dc_td.ListBackupPlanVersionsOutput.make_one(res)

    def list_backup_plans(
        self,
        res: "bs_td.ListBackupPlansOutputTypeDef",
    ) -> "dc_td.ListBackupPlansOutput":
        return dc_td.ListBackupPlansOutput.make_one(res)

    def list_backup_selections(
        self,
        res: "bs_td.ListBackupSelectionsOutputTypeDef",
    ) -> "dc_td.ListBackupSelectionsOutput":
        return dc_td.ListBackupSelectionsOutput.make_one(res)

    def list_backup_vaults(
        self,
        res: "bs_td.ListBackupVaultsOutputTypeDef",
    ) -> "dc_td.ListBackupVaultsOutput":
        return dc_td.ListBackupVaultsOutput.make_one(res)

    def list_copy_job_summaries(
        self,
        res: "bs_td.ListCopyJobSummariesOutputTypeDef",
    ) -> "dc_td.ListCopyJobSummariesOutput":
        return dc_td.ListCopyJobSummariesOutput.make_one(res)

    def list_copy_jobs(
        self,
        res: "bs_td.ListCopyJobsOutputTypeDef",
    ) -> "dc_td.ListCopyJobsOutput":
        return dc_td.ListCopyJobsOutput.make_one(res)

    def list_frameworks(
        self,
        res: "bs_td.ListFrameworksOutputTypeDef",
    ) -> "dc_td.ListFrameworksOutput":
        return dc_td.ListFrameworksOutput.make_one(res)

    def list_indexed_recovery_points(
        self,
        res: "bs_td.ListIndexedRecoveryPointsOutputTypeDef",
    ) -> "dc_td.ListIndexedRecoveryPointsOutput":
        return dc_td.ListIndexedRecoveryPointsOutput.make_one(res)

    def list_legal_holds(
        self,
        res: "bs_td.ListLegalHoldsOutputTypeDef",
    ) -> "dc_td.ListLegalHoldsOutput":
        return dc_td.ListLegalHoldsOutput.make_one(res)

    def list_protected_resources(
        self,
        res: "bs_td.ListProtectedResourcesOutputTypeDef",
    ) -> "dc_td.ListProtectedResourcesOutput":
        return dc_td.ListProtectedResourcesOutput.make_one(res)

    def list_protected_resources_by_backup_vault(
        self,
        res: "bs_td.ListProtectedResourcesByBackupVaultOutputTypeDef",
    ) -> "dc_td.ListProtectedResourcesByBackupVaultOutput":
        return dc_td.ListProtectedResourcesByBackupVaultOutput.make_one(res)

    def list_recovery_points_by_backup_vault(
        self,
        res: "bs_td.ListRecoveryPointsByBackupVaultOutputTypeDef",
    ) -> "dc_td.ListRecoveryPointsByBackupVaultOutput":
        return dc_td.ListRecoveryPointsByBackupVaultOutput.make_one(res)

    def list_recovery_points_by_legal_hold(
        self,
        res: "bs_td.ListRecoveryPointsByLegalHoldOutputTypeDef",
    ) -> "dc_td.ListRecoveryPointsByLegalHoldOutput":
        return dc_td.ListRecoveryPointsByLegalHoldOutput.make_one(res)

    def list_recovery_points_by_resource(
        self,
        res: "bs_td.ListRecoveryPointsByResourceOutputTypeDef",
    ) -> "dc_td.ListRecoveryPointsByResourceOutput":
        return dc_td.ListRecoveryPointsByResourceOutput.make_one(res)

    def list_report_jobs(
        self,
        res: "bs_td.ListReportJobsOutputTypeDef",
    ) -> "dc_td.ListReportJobsOutput":
        return dc_td.ListReportJobsOutput.make_one(res)

    def list_report_plans(
        self,
        res: "bs_td.ListReportPlansOutputTypeDef",
    ) -> "dc_td.ListReportPlansOutput":
        return dc_td.ListReportPlansOutput.make_one(res)

    def list_restore_access_backup_vaults(
        self,
        res: "bs_td.ListRestoreAccessBackupVaultsOutputTypeDef",
    ) -> "dc_td.ListRestoreAccessBackupVaultsOutput":
        return dc_td.ListRestoreAccessBackupVaultsOutput.make_one(res)

    def list_restore_job_summaries(
        self,
        res: "bs_td.ListRestoreJobSummariesOutputTypeDef",
    ) -> "dc_td.ListRestoreJobSummariesOutput":
        return dc_td.ListRestoreJobSummariesOutput.make_one(res)

    def list_restore_jobs(
        self,
        res: "bs_td.ListRestoreJobsOutputTypeDef",
    ) -> "dc_td.ListRestoreJobsOutput":
        return dc_td.ListRestoreJobsOutput.make_one(res)

    def list_restore_jobs_by_protected_resource(
        self,
        res: "bs_td.ListRestoreJobsByProtectedResourceOutputTypeDef",
    ) -> "dc_td.ListRestoreJobsByProtectedResourceOutput":
        return dc_td.ListRestoreJobsByProtectedResourceOutput.make_one(res)

    def list_restore_testing_plans(
        self,
        res: "bs_td.ListRestoreTestingPlansOutputTypeDef",
    ) -> "dc_td.ListRestoreTestingPlansOutput":
        return dc_td.ListRestoreTestingPlansOutput.make_one(res)

    def list_restore_testing_selections(
        self,
        res: "bs_td.ListRestoreTestingSelectionsOutputTypeDef",
    ) -> "dc_td.ListRestoreTestingSelectionsOutput":
        return dc_td.ListRestoreTestingSelectionsOutput.make_one(res)

    def list_tags(
        self,
        res: "bs_td.ListTagsOutputTypeDef",
    ) -> "dc_td.ListTagsOutput":
        return dc_td.ListTagsOutput.make_one(res)

    def put_backup_vault_access_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_backup_vault_lock_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_backup_vault_notifications(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_restore_validation_result(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def revoke_restore_access_backup_vault(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_backup_job(
        self,
        res: "bs_td.StartBackupJobOutputTypeDef",
    ) -> "dc_td.StartBackupJobOutput":
        return dc_td.StartBackupJobOutput.make_one(res)

    def start_copy_job(
        self,
        res: "bs_td.StartCopyJobOutputTypeDef",
    ) -> "dc_td.StartCopyJobOutput":
        return dc_td.StartCopyJobOutput.make_one(res)

    def start_report_job(
        self,
        res: "bs_td.StartReportJobOutputTypeDef",
    ) -> "dc_td.StartReportJobOutput":
        return dc_td.StartReportJobOutput.make_one(res)

    def start_restore_job(
        self,
        res: "bs_td.StartRestoreJobOutputTypeDef",
    ) -> "dc_td.StartRestoreJobOutput":
        return dc_td.StartRestoreJobOutput.make_one(res)

    def stop_backup_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

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

    def update_backup_plan(
        self,
        res: "bs_td.UpdateBackupPlanOutputTypeDef",
    ) -> "dc_td.UpdateBackupPlanOutput":
        return dc_td.UpdateBackupPlanOutput.make_one(res)

    def update_framework(
        self,
        res: "bs_td.UpdateFrameworkOutputTypeDef",
    ) -> "dc_td.UpdateFrameworkOutput":
        return dc_td.UpdateFrameworkOutput.make_one(res)

    def update_global_settings(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_recovery_point_index_settings(
        self,
        res: "bs_td.UpdateRecoveryPointIndexSettingsOutputTypeDef",
    ) -> "dc_td.UpdateRecoveryPointIndexSettingsOutput":
        return dc_td.UpdateRecoveryPointIndexSettingsOutput.make_one(res)

    def update_recovery_point_lifecycle(
        self,
        res: "bs_td.UpdateRecoveryPointLifecycleOutputTypeDef",
    ) -> "dc_td.UpdateRecoveryPointLifecycleOutput":
        return dc_td.UpdateRecoveryPointLifecycleOutput.make_one(res)

    def update_region_settings(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_report_plan(
        self,
        res: "bs_td.UpdateReportPlanOutputTypeDef",
    ) -> "dc_td.UpdateReportPlanOutput":
        return dc_td.UpdateReportPlanOutput.make_one(res)

    def update_restore_testing_plan(
        self,
        res: "bs_td.UpdateRestoreTestingPlanOutputTypeDef",
    ) -> "dc_td.UpdateRestoreTestingPlanOutput":
        return dc_td.UpdateRestoreTestingPlanOutput.make_one(res)

    def update_restore_testing_selection(
        self,
        res: "bs_td.UpdateRestoreTestingSelectionOutputTypeDef",
    ) -> "dc_td.UpdateRestoreTestingSelectionOutput":
        return dc_td.UpdateRestoreTestingSelectionOutput.make_one(res)


backup_caster = BACKUPCaster()
