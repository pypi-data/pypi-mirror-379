# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_auditmanager import type_defs as bs_td


class AUDITMANAGERCaster:

    def batch_associate_assessment_report_evidence(
        self,
        res: "bs_td.BatchAssociateAssessmentReportEvidenceResponseTypeDef",
    ) -> "dc_td.BatchAssociateAssessmentReportEvidenceResponse":
        return dc_td.BatchAssociateAssessmentReportEvidenceResponse.make_one(res)

    def batch_create_delegation_by_assessment(
        self,
        res: "bs_td.BatchCreateDelegationByAssessmentResponseTypeDef",
    ) -> "dc_td.BatchCreateDelegationByAssessmentResponse":
        return dc_td.BatchCreateDelegationByAssessmentResponse.make_one(res)

    def batch_delete_delegation_by_assessment(
        self,
        res: "bs_td.BatchDeleteDelegationByAssessmentResponseTypeDef",
    ) -> "dc_td.BatchDeleteDelegationByAssessmentResponse":
        return dc_td.BatchDeleteDelegationByAssessmentResponse.make_one(res)

    def batch_disassociate_assessment_report_evidence(
        self,
        res: "bs_td.BatchDisassociateAssessmentReportEvidenceResponseTypeDef",
    ) -> "dc_td.BatchDisassociateAssessmentReportEvidenceResponse":
        return dc_td.BatchDisassociateAssessmentReportEvidenceResponse.make_one(res)

    def batch_import_evidence_to_assessment_control(
        self,
        res: "bs_td.BatchImportEvidenceToAssessmentControlResponseTypeDef",
    ) -> "dc_td.BatchImportEvidenceToAssessmentControlResponse":
        return dc_td.BatchImportEvidenceToAssessmentControlResponse.make_one(res)

    def create_assessment(
        self,
        res: "bs_td.CreateAssessmentResponseTypeDef",
    ) -> "dc_td.CreateAssessmentResponse":
        return dc_td.CreateAssessmentResponse.make_one(res)

    def create_assessment_framework(
        self,
        res: "bs_td.CreateAssessmentFrameworkResponseTypeDef",
    ) -> "dc_td.CreateAssessmentFrameworkResponse":
        return dc_td.CreateAssessmentFrameworkResponse.make_one(res)

    def create_assessment_report(
        self,
        res: "bs_td.CreateAssessmentReportResponseTypeDef",
    ) -> "dc_td.CreateAssessmentReportResponse":
        return dc_td.CreateAssessmentReportResponse.make_one(res)

    def create_control(
        self,
        res: "bs_td.CreateControlResponseTypeDef",
    ) -> "dc_td.CreateControlResponse":
        return dc_td.CreateControlResponse.make_one(res)

    def deregister_account(
        self,
        res: "bs_td.DeregisterAccountResponseTypeDef",
    ) -> "dc_td.DeregisterAccountResponse":
        return dc_td.DeregisterAccountResponse.make_one(res)

    def get_account_status(
        self,
        res: "bs_td.GetAccountStatusResponseTypeDef",
    ) -> "dc_td.GetAccountStatusResponse":
        return dc_td.GetAccountStatusResponse.make_one(res)

    def get_assessment(
        self,
        res: "bs_td.GetAssessmentResponseTypeDef",
    ) -> "dc_td.GetAssessmentResponse":
        return dc_td.GetAssessmentResponse.make_one(res)

    def get_assessment_framework(
        self,
        res: "bs_td.GetAssessmentFrameworkResponseTypeDef",
    ) -> "dc_td.GetAssessmentFrameworkResponse":
        return dc_td.GetAssessmentFrameworkResponse.make_one(res)

    def get_assessment_report_url(
        self,
        res: "bs_td.GetAssessmentReportUrlResponseTypeDef",
    ) -> "dc_td.GetAssessmentReportUrlResponse":
        return dc_td.GetAssessmentReportUrlResponse.make_one(res)

    def get_change_logs(
        self,
        res: "bs_td.GetChangeLogsResponseTypeDef",
    ) -> "dc_td.GetChangeLogsResponse":
        return dc_td.GetChangeLogsResponse.make_one(res)

    def get_control(
        self,
        res: "bs_td.GetControlResponseTypeDef",
    ) -> "dc_td.GetControlResponse":
        return dc_td.GetControlResponse.make_one(res)

    def get_delegations(
        self,
        res: "bs_td.GetDelegationsResponseTypeDef",
    ) -> "dc_td.GetDelegationsResponse":
        return dc_td.GetDelegationsResponse.make_one(res)

    def get_evidence(
        self,
        res: "bs_td.GetEvidenceResponseTypeDef",
    ) -> "dc_td.GetEvidenceResponse":
        return dc_td.GetEvidenceResponse.make_one(res)

    def get_evidence_by_evidence_folder(
        self,
        res: "bs_td.GetEvidenceByEvidenceFolderResponseTypeDef",
    ) -> "dc_td.GetEvidenceByEvidenceFolderResponse":
        return dc_td.GetEvidenceByEvidenceFolderResponse.make_one(res)

    def get_evidence_file_upload_url(
        self,
        res: "bs_td.GetEvidenceFileUploadUrlResponseTypeDef",
    ) -> "dc_td.GetEvidenceFileUploadUrlResponse":
        return dc_td.GetEvidenceFileUploadUrlResponse.make_one(res)

    def get_evidence_folder(
        self,
        res: "bs_td.GetEvidenceFolderResponseTypeDef",
    ) -> "dc_td.GetEvidenceFolderResponse":
        return dc_td.GetEvidenceFolderResponse.make_one(res)

    def get_evidence_folders_by_assessment(
        self,
        res: "bs_td.GetEvidenceFoldersByAssessmentResponseTypeDef",
    ) -> "dc_td.GetEvidenceFoldersByAssessmentResponse":
        return dc_td.GetEvidenceFoldersByAssessmentResponse.make_one(res)

    def get_evidence_folders_by_assessment_control(
        self,
        res: "bs_td.GetEvidenceFoldersByAssessmentControlResponseTypeDef",
    ) -> "dc_td.GetEvidenceFoldersByAssessmentControlResponse":
        return dc_td.GetEvidenceFoldersByAssessmentControlResponse.make_one(res)

    def get_insights(
        self,
        res: "bs_td.GetInsightsResponseTypeDef",
    ) -> "dc_td.GetInsightsResponse":
        return dc_td.GetInsightsResponse.make_one(res)

    def get_insights_by_assessment(
        self,
        res: "bs_td.GetInsightsByAssessmentResponseTypeDef",
    ) -> "dc_td.GetInsightsByAssessmentResponse":
        return dc_td.GetInsightsByAssessmentResponse.make_one(res)

    def get_organization_admin_account(
        self,
        res: "bs_td.GetOrganizationAdminAccountResponseTypeDef",
    ) -> "dc_td.GetOrganizationAdminAccountResponse":
        return dc_td.GetOrganizationAdminAccountResponse.make_one(res)

    def get_services_in_scope(
        self,
        res: "bs_td.GetServicesInScopeResponseTypeDef",
    ) -> "dc_td.GetServicesInScopeResponse":
        return dc_td.GetServicesInScopeResponse.make_one(res)

    def get_settings(
        self,
        res: "bs_td.GetSettingsResponseTypeDef",
    ) -> "dc_td.GetSettingsResponse":
        return dc_td.GetSettingsResponse.make_one(res)

    def list_assessment_control_insights_by_control_domain(
        self,
        res: "bs_td.ListAssessmentControlInsightsByControlDomainResponseTypeDef",
    ) -> "dc_td.ListAssessmentControlInsightsByControlDomainResponse":
        return dc_td.ListAssessmentControlInsightsByControlDomainResponse.make_one(res)

    def list_assessment_framework_share_requests(
        self,
        res: "bs_td.ListAssessmentFrameworkShareRequestsResponseTypeDef",
    ) -> "dc_td.ListAssessmentFrameworkShareRequestsResponse":
        return dc_td.ListAssessmentFrameworkShareRequestsResponse.make_one(res)

    def list_assessment_frameworks(
        self,
        res: "bs_td.ListAssessmentFrameworksResponseTypeDef",
    ) -> "dc_td.ListAssessmentFrameworksResponse":
        return dc_td.ListAssessmentFrameworksResponse.make_one(res)

    def list_assessment_reports(
        self,
        res: "bs_td.ListAssessmentReportsResponseTypeDef",
    ) -> "dc_td.ListAssessmentReportsResponse":
        return dc_td.ListAssessmentReportsResponse.make_one(res)

    def list_assessments(
        self,
        res: "bs_td.ListAssessmentsResponseTypeDef",
    ) -> "dc_td.ListAssessmentsResponse":
        return dc_td.ListAssessmentsResponse.make_one(res)

    def list_control_domain_insights(
        self,
        res: "bs_td.ListControlDomainInsightsResponseTypeDef",
    ) -> "dc_td.ListControlDomainInsightsResponse":
        return dc_td.ListControlDomainInsightsResponse.make_one(res)

    def list_control_domain_insights_by_assessment(
        self,
        res: "bs_td.ListControlDomainInsightsByAssessmentResponseTypeDef",
    ) -> "dc_td.ListControlDomainInsightsByAssessmentResponse":
        return dc_td.ListControlDomainInsightsByAssessmentResponse.make_one(res)

    def list_control_insights_by_control_domain(
        self,
        res: "bs_td.ListControlInsightsByControlDomainResponseTypeDef",
    ) -> "dc_td.ListControlInsightsByControlDomainResponse":
        return dc_td.ListControlInsightsByControlDomainResponse.make_one(res)

    def list_controls(
        self,
        res: "bs_td.ListControlsResponseTypeDef",
    ) -> "dc_td.ListControlsResponse":
        return dc_td.ListControlsResponse.make_one(res)

    def list_keywords_for_data_source(
        self,
        res: "bs_td.ListKeywordsForDataSourceResponseTypeDef",
    ) -> "dc_td.ListKeywordsForDataSourceResponse":
        return dc_td.ListKeywordsForDataSourceResponse.make_one(res)

    def list_notifications(
        self,
        res: "bs_td.ListNotificationsResponseTypeDef",
    ) -> "dc_td.ListNotificationsResponse":
        return dc_td.ListNotificationsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def register_account(
        self,
        res: "bs_td.RegisterAccountResponseTypeDef",
    ) -> "dc_td.RegisterAccountResponse":
        return dc_td.RegisterAccountResponse.make_one(res)

    def register_organization_admin_account(
        self,
        res: "bs_td.RegisterOrganizationAdminAccountResponseTypeDef",
    ) -> "dc_td.RegisterOrganizationAdminAccountResponse":
        return dc_td.RegisterOrganizationAdminAccountResponse.make_one(res)

    def start_assessment_framework_share(
        self,
        res: "bs_td.StartAssessmentFrameworkShareResponseTypeDef",
    ) -> "dc_td.StartAssessmentFrameworkShareResponse":
        return dc_td.StartAssessmentFrameworkShareResponse.make_one(res)

    def update_assessment(
        self,
        res: "bs_td.UpdateAssessmentResponseTypeDef",
    ) -> "dc_td.UpdateAssessmentResponse":
        return dc_td.UpdateAssessmentResponse.make_one(res)

    def update_assessment_control(
        self,
        res: "bs_td.UpdateAssessmentControlResponseTypeDef",
    ) -> "dc_td.UpdateAssessmentControlResponse":
        return dc_td.UpdateAssessmentControlResponse.make_one(res)

    def update_assessment_control_set_status(
        self,
        res: "bs_td.UpdateAssessmentControlSetStatusResponseTypeDef",
    ) -> "dc_td.UpdateAssessmentControlSetStatusResponse":
        return dc_td.UpdateAssessmentControlSetStatusResponse.make_one(res)

    def update_assessment_framework(
        self,
        res: "bs_td.UpdateAssessmentFrameworkResponseTypeDef",
    ) -> "dc_td.UpdateAssessmentFrameworkResponse":
        return dc_td.UpdateAssessmentFrameworkResponse.make_one(res)

    def update_assessment_framework_share(
        self,
        res: "bs_td.UpdateAssessmentFrameworkShareResponseTypeDef",
    ) -> "dc_td.UpdateAssessmentFrameworkShareResponse":
        return dc_td.UpdateAssessmentFrameworkShareResponse.make_one(res)

    def update_assessment_status(
        self,
        res: "bs_td.UpdateAssessmentStatusResponseTypeDef",
    ) -> "dc_td.UpdateAssessmentStatusResponse":
        return dc_td.UpdateAssessmentStatusResponse.make_one(res)

    def update_control(
        self,
        res: "bs_td.UpdateControlResponseTypeDef",
    ) -> "dc_td.UpdateControlResponse":
        return dc_td.UpdateControlResponse.make_one(res)

    def update_settings(
        self,
        res: "bs_td.UpdateSettingsResponseTypeDef",
    ) -> "dc_td.UpdateSettingsResponse":
        return dc_td.UpdateSettingsResponse.make_one(res)

    def validate_assessment_report_integrity(
        self,
        res: "bs_td.ValidateAssessmentReportIntegrityResponseTypeDef",
    ) -> "dc_td.ValidateAssessmentReportIntegrityResponse":
        return dc_td.ValidateAssessmentReportIntegrityResponse.make_one(res)


auditmanager_caster = AUDITMANAGERCaster()
