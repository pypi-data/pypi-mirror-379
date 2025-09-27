# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cleanrooms import type_defs as bs_td


class CLEANROOMSCaster:

    def batch_get_collaboration_analysis_template(
        self,
        res: "bs_td.BatchGetCollaborationAnalysisTemplateOutputTypeDef",
    ) -> "dc_td.BatchGetCollaborationAnalysisTemplateOutput":
        return dc_td.BatchGetCollaborationAnalysisTemplateOutput.make_one(res)

    def batch_get_schema(
        self,
        res: "bs_td.BatchGetSchemaOutputTypeDef",
    ) -> "dc_td.BatchGetSchemaOutput":
        return dc_td.BatchGetSchemaOutput.make_one(res)

    def batch_get_schema_analysis_rule(
        self,
        res: "bs_td.BatchGetSchemaAnalysisRuleOutputTypeDef",
    ) -> "dc_td.BatchGetSchemaAnalysisRuleOutput":
        return dc_td.BatchGetSchemaAnalysisRuleOutput.make_one(res)

    def create_analysis_template(
        self,
        res: "bs_td.CreateAnalysisTemplateOutputTypeDef",
    ) -> "dc_td.CreateAnalysisTemplateOutput":
        return dc_td.CreateAnalysisTemplateOutput.make_one(res)

    def create_collaboration(
        self,
        res: "bs_td.CreateCollaborationOutputTypeDef",
    ) -> "dc_td.CreateCollaborationOutput":
        return dc_td.CreateCollaborationOutput.make_one(res)

    def create_collaboration_change_request(
        self,
        res: "bs_td.CreateCollaborationChangeRequestOutputTypeDef",
    ) -> "dc_td.CreateCollaborationChangeRequestOutput":
        return dc_td.CreateCollaborationChangeRequestOutput.make_one(res)

    def create_configured_audience_model_association(
        self,
        res: "bs_td.CreateConfiguredAudienceModelAssociationOutputTypeDef",
    ) -> "dc_td.CreateConfiguredAudienceModelAssociationOutput":
        return dc_td.CreateConfiguredAudienceModelAssociationOutput.make_one(res)

    def create_configured_table(
        self,
        res: "bs_td.CreateConfiguredTableOutputTypeDef",
    ) -> "dc_td.CreateConfiguredTableOutput":
        return dc_td.CreateConfiguredTableOutput.make_one(res)

    def create_configured_table_analysis_rule(
        self,
        res: "bs_td.CreateConfiguredTableAnalysisRuleOutputTypeDef",
    ) -> "dc_td.CreateConfiguredTableAnalysisRuleOutput":
        return dc_td.CreateConfiguredTableAnalysisRuleOutput.make_one(res)

    def create_configured_table_association(
        self,
        res: "bs_td.CreateConfiguredTableAssociationOutputTypeDef",
    ) -> "dc_td.CreateConfiguredTableAssociationOutput":
        return dc_td.CreateConfiguredTableAssociationOutput.make_one(res)

    def create_configured_table_association_analysis_rule(
        self,
        res: "bs_td.CreateConfiguredTableAssociationAnalysisRuleOutputTypeDef",
    ) -> "dc_td.CreateConfiguredTableAssociationAnalysisRuleOutput":
        return dc_td.CreateConfiguredTableAssociationAnalysisRuleOutput.make_one(res)

    def create_id_mapping_table(
        self,
        res: "bs_td.CreateIdMappingTableOutputTypeDef",
    ) -> "dc_td.CreateIdMappingTableOutput":
        return dc_td.CreateIdMappingTableOutput.make_one(res)

    def create_id_namespace_association(
        self,
        res: "bs_td.CreateIdNamespaceAssociationOutputTypeDef",
    ) -> "dc_td.CreateIdNamespaceAssociationOutput":
        return dc_td.CreateIdNamespaceAssociationOutput.make_one(res)

    def create_membership(
        self,
        res: "bs_td.CreateMembershipOutputTypeDef",
    ) -> "dc_td.CreateMembershipOutput":
        return dc_td.CreateMembershipOutput.make_one(res)

    def create_privacy_budget_template(
        self,
        res: "bs_td.CreatePrivacyBudgetTemplateOutputTypeDef",
    ) -> "dc_td.CreatePrivacyBudgetTemplateOutput":
        return dc_td.CreatePrivacyBudgetTemplateOutput.make_one(res)

    def get_analysis_template(
        self,
        res: "bs_td.GetAnalysisTemplateOutputTypeDef",
    ) -> "dc_td.GetAnalysisTemplateOutput":
        return dc_td.GetAnalysisTemplateOutput.make_one(res)

    def get_collaboration(
        self,
        res: "bs_td.GetCollaborationOutputTypeDef",
    ) -> "dc_td.GetCollaborationOutput":
        return dc_td.GetCollaborationOutput.make_one(res)

    def get_collaboration_analysis_template(
        self,
        res: "bs_td.GetCollaborationAnalysisTemplateOutputTypeDef",
    ) -> "dc_td.GetCollaborationAnalysisTemplateOutput":
        return dc_td.GetCollaborationAnalysisTemplateOutput.make_one(res)

    def get_collaboration_change_request(
        self,
        res: "bs_td.GetCollaborationChangeRequestOutputTypeDef",
    ) -> "dc_td.GetCollaborationChangeRequestOutput":
        return dc_td.GetCollaborationChangeRequestOutput.make_one(res)

    def get_collaboration_configured_audience_model_association(
        self,
        res: "bs_td.GetCollaborationConfiguredAudienceModelAssociationOutputTypeDef",
    ) -> "dc_td.GetCollaborationConfiguredAudienceModelAssociationOutput":
        return dc_td.GetCollaborationConfiguredAudienceModelAssociationOutput.make_one(
            res
        )

    def get_collaboration_id_namespace_association(
        self,
        res: "bs_td.GetCollaborationIdNamespaceAssociationOutputTypeDef",
    ) -> "dc_td.GetCollaborationIdNamespaceAssociationOutput":
        return dc_td.GetCollaborationIdNamespaceAssociationOutput.make_one(res)

    def get_collaboration_privacy_budget_template(
        self,
        res: "bs_td.GetCollaborationPrivacyBudgetTemplateOutputTypeDef",
    ) -> "dc_td.GetCollaborationPrivacyBudgetTemplateOutput":
        return dc_td.GetCollaborationPrivacyBudgetTemplateOutput.make_one(res)

    def get_configured_audience_model_association(
        self,
        res: "bs_td.GetConfiguredAudienceModelAssociationOutputTypeDef",
    ) -> "dc_td.GetConfiguredAudienceModelAssociationOutput":
        return dc_td.GetConfiguredAudienceModelAssociationOutput.make_one(res)

    def get_configured_table(
        self,
        res: "bs_td.GetConfiguredTableOutputTypeDef",
    ) -> "dc_td.GetConfiguredTableOutput":
        return dc_td.GetConfiguredTableOutput.make_one(res)

    def get_configured_table_analysis_rule(
        self,
        res: "bs_td.GetConfiguredTableAnalysisRuleOutputTypeDef",
    ) -> "dc_td.GetConfiguredTableAnalysisRuleOutput":
        return dc_td.GetConfiguredTableAnalysisRuleOutput.make_one(res)

    def get_configured_table_association(
        self,
        res: "bs_td.GetConfiguredTableAssociationOutputTypeDef",
    ) -> "dc_td.GetConfiguredTableAssociationOutput":
        return dc_td.GetConfiguredTableAssociationOutput.make_one(res)

    def get_configured_table_association_analysis_rule(
        self,
        res: "bs_td.GetConfiguredTableAssociationAnalysisRuleOutputTypeDef",
    ) -> "dc_td.GetConfiguredTableAssociationAnalysisRuleOutput":
        return dc_td.GetConfiguredTableAssociationAnalysisRuleOutput.make_one(res)

    def get_id_mapping_table(
        self,
        res: "bs_td.GetIdMappingTableOutputTypeDef",
    ) -> "dc_td.GetIdMappingTableOutput":
        return dc_td.GetIdMappingTableOutput.make_one(res)

    def get_id_namespace_association(
        self,
        res: "bs_td.GetIdNamespaceAssociationOutputTypeDef",
    ) -> "dc_td.GetIdNamespaceAssociationOutput":
        return dc_td.GetIdNamespaceAssociationOutput.make_one(res)

    def get_membership(
        self,
        res: "bs_td.GetMembershipOutputTypeDef",
    ) -> "dc_td.GetMembershipOutput":
        return dc_td.GetMembershipOutput.make_one(res)

    def get_privacy_budget_template(
        self,
        res: "bs_td.GetPrivacyBudgetTemplateOutputTypeDef",
    ) -> "dc_td.GetPrivacyBudgetTemplateOutput":
        return dc_td.GetPrivacyBudgetTemplateOutput.make_one(res)

    def get_protected_job(
        self,
        res: "bs_td.GetProtectedJobOutputTypeDef",
    ) -> "dc_td.GetProtectedJobOutput":
        return dc_td.GetProtectedJobOutput.make_one(res)

    def get_protected_query(
        self,
        res: "bs_td.GetProtectedQueryOutputTypeDef",
    ) -> "dc_td.GetProtectedQueryOutput":
        return dc_td.GetProtectedQueryOutput.make_one(res)

    def get_schema(
        self,
        res: "bs_td.GetSchemaOutputTypeDef",
    ) -> "dc_td.GetSchemaOutput":
        return dc_td.GetSchemaOutput.make_one(res)

    def get_schema_analysis_rule(
        self,
        res: "bs_td.GetSchemaAnalysisRuleOutputTypeDef",
    ) -> "dc_td.GetSchemaAnalysisRuleOutput":
        return dc_td.GetSchemaAnalysisRuleOutput.make_one(res)

    def list_analysis_templates(
        self,
        res: "bs_td.ListAnalysisTemplatesOutputTypeDef",
    ) -> "dc_td.ListAnalysisTemplatesOutput":
        return dc_td.ListAnalysisTemplatesOutput.make_one(res)

    def list_collaboration_analysis_templates(
        self,
        res: "bs_td.ListCollaborationAnalysisTemplatesOutputTypeDef",
    ) -> "dc_td.ListCollaborationAnalysisTemplatesOutput":
        return dc_td.ListCollaborationAnalysisTemplatesOutput.make_one(res)

    def list_collaboration_change_requests(
        self,
        res: "bs_td.ListCollaborationChangeRequestsOutputTypeDef",
    ) -> "dc_td.ListCollaborationChangeRequestsOutput":
        return dc_td.ListCollaborationChangeRequestsOutput.make_one(res)

    def list_collaboration_configured_audience_model_associations(
        self,
        res: "bs_td.ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef",
    ) -> "dc_td.ListCollaborationConfiguredAudienceModelAssociationsOutput":
        return (
            dc_td.ListCollaborationConfiguredAudienceModelAssociationsOutput.make_one(
                res
            )
        )

    def list_collaboration_id_namespace_associations(
        self,
        res: "bs_td.ListCollaborationIdNamespaceAssociationsOutputTypeDef",
    ) -> "dc_td.ListCollaborationIdNamespaceAssociationsOutput":
        return dc_td.ListCollaborationIdNamespaceAssociationsOutput.make_one(res)

    def list_collaboration_privacy_budget_templates(
        self,
        res: "bs_td.ListCollaborationPrivacyBudgetTemplatesOutputTypeDef",
    ) -> "dc_td.ListCollaborationPrivacyBudgetTemplatesOutput":
        return dc_td.ListCollaborationPrivacyBudgetTemplatesOutput.make_one(res)

    def list_collaboration_privacy_budgets(
        self,
        res: "bs_td.ListCollaborationPrivacyBudgetsOutputTypeDef",
    ) -> "dc_td.ListCollaborationPrivacyBudgetsOutput":
        return dc_td.ListCollaborationPrivacyBudgetsOutput.make_one(res)

    def list_collaborations(
        self,
        res: "bs_td.ListCollaborationsOutputTypeDef",
    ) -> "dc_td.ListCollaborationsOutput":
        return dc_td.ListCollaborationsOutput.make_one(res)

    def list_configured_audience_model_associations(
        self,
        res: "bs_td.ListConfiguredAudienceModelAssociationsOutputTypeDef",
    ) -> "dc_td.ListConfiguredAudienceModelAssociationsOutput":
        return dc_td.ListConfiguredAudienceModelAssociationsOutput.make_one(res)

    def list_configured_table_associations(
        self,
        res: "bs_td.ListConfiguredTableAssociationsOutputTypeDef",
    ) -> "dc_td.ListConfiguredTableAssociationsOutput":
        return dc_td.ListConfiguredTableAssociationsOutput.make_one(res)

    def list_configured_tables(
        self,
        res: "bs_td.ListConfiguredTablesOutputTypeDef",
    ) -> "dc_td.ListConfiguredTablesOutput":
        return dc_td.ListConfiguredTablesOutput.make_one(res)

    def list_id_mapping_tables(
        self,
        res: "bs_td.ListIdMappingTablesOutputTypeDef",
    ) -> "dc_td.ListIdMappingTablesOutput":
        return dc_td.ListIdMappingTablesOutput.make_one(res)

    def list_id_namespace_associations(
        self,
        res: "bs_td.ListIdNamespaceAssociationsOutputTypeDef",
    ) -> "dc_td.ListIdNamespaceAssociationsOutput":
        return dc_td.ListIdNamespaceAssociationsOutput.make_one(res)

    def list_members(
        self,
        res: "bs_td.ListMembersOutputTypeDef",
    ) -> "dc_td.ListMembersOutput":
        return dc_td.ListMembersOutput.make_one(res)

    def list_memberships(
        self,
        res: "bs_td.ListMembershipsOutputTypeDef",
    ) -> "dc_td.ListMembershipsOutput":
        return dc_td.ListMembershipsOutput.make_one(res)

    def list_privacy_budget_templates(
        self,
        res: "bs_td.ListPrivacyBudgetTemplatesOutputTypeDef",
    ) -> "dc_td.ListPrivacyBudgetTemplatesOutput":
        return dc_td.ListPrivacyBudgetTemplatesOutput.make_one(res)

    def list_privacy_budgets(
        self,
        res: "bs_td.ListPrivacyBudgetsOutputTypeDef",
    ) -> "dc_td.ListPrivacyBudgetsOutput":
        return dc_td.ListPrivacyBudgetsOutput.make_one(res)

    def list_protected_jobs(
        self,
        res: "bs_td.ListProtectedJobsOutputTypeDef",
    ) -> "dc_td.ListProtectedJobsOutput":
        return dc_td.ListProtectedJobsOutput.make_one(res)

    def list_protected_queries(
        self,
        res: "bs_td.ListProtectedQueriesOutputTypeDef",
    ) -> "dc_td.ListProtectedQueriesOutput":
        return dc_td.ListProtectedQueriesOutput.make_one(res)

    def list_schemas(
        self,
        res: "bs_td.ListSchemasOutputTypeDef",
    ) -> "dc_td.ListSchemasOutput":
        return dc_td.ListSchemasOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def populate_id_mapping_table(
        self,
        res: "bs_td.PopulateIdMappingTableOutputTypeDef",
    ) -> "dc_td.PopulateIdMappingTableOutput":
        return dc_td.PopulateIdMappingTableOutput.make_one(res)

    def preview_privacy_impact(
        self,
        res: "bs_td.PreviewPrivacyImpactOutputTypeDef",
    ) -> "dc_td.PreviewPrivacyImpactOutput":
        return dc_td.PreviewPrivacyImpactOutput.make_one(res)

    def start_protected_job(
        self,
        res: "bs_td.StartProtectedJobOutputTypeDef",
    ) -> "dc_td.StartProtectedJobOutput":
        return dc_td.StartProtectedJobOutput.make_one(res)

    def start_protected_query(
        self,
        res: "bs_td.StartProtectedQueryOutputTypeDef",
    ) -> "dc_td.StartProtectedQueryOutput":
        return dc_td.StartProtectedQueryOutput.make_one(res)

    def update_analysis_template(
        self,
        res: "bs_td.UpdateAnalysisTemplateOutputTypeDef",
    ) -> "dc_td.UpdateAnalysisTemplateOutput":
        return dc_td.UpdateAnalysisTemplateOutput.make_one(res)

    def update_collaboration(
        self,
        res: "bs_td.UpdateCollaborationOutputTypeDef",
    ) -> "dc_td.UpdateCollaborationOutput":
        return dc_td.UpdateCollaborationOutput.make_one(res)

    def update_configured_audience_model_association(
        self,
        res: "bs_td.UpdateConfiguredAudienceModelAssociationOutputTypeDef",
    ) -> "dc_td.UpdateConfiguredAudienceModelAssociationOutput":
        return dc_td.UpdateConfiguredAudienceModelAssociationOutput.make_one(res)

    def update_configured_table(
        self,
        res: "bs_td.UpdateConfiguredTableOutputTypeDef",
    ) -> "dc_td.UpdateConfiguredTableOutput":
        return dc_td.UpdateConfiguredTableOutput.make_one(res)

    def update_configured_table_analysis_rule(
        self,
        res: "bs_td.UpdateConfiguredTableAnalysisRuleOutputTypeDef",
    ) -> "dc_td.UpdateConfiguredTableAnalysisRuleOutput":
        return dc_td.UpdateConfiguredTableAnalysisRuleOutput.make_one(res)

    def update_configured_table_association(
        self,
        res: "bs_td.UpdateConfiguredTableAssociationOutputTypeDef",
    ) -> "dc_td.UpdateConfiguredTableAssociationOutput":
        return dc_td.UpdateConfiguredTableAssociationOutput.make_one(res)

    def update_configured_table_association_analysis_rule(
        self,
        res: "bs_td.UpdateConfiguredTableAssociationAnalysisRuleOutputTypeDef",
    ) -> "dc_td.UpdateConfiguredTableAssociationAnalysisRuleOutput":
        return dc_td.UpdateConfiguredTableAssociationAnalysisRuleOutput.make_one(res)

    def update_id_mapping_table(
        self,
        res: "bs_td.UpdateIdMappingTableOutputTypeDef",
    ) -> "dc_td.UpdateIdMappingTableOutput":
        return dc_td.UpdateIdMappingTableOutput.make_one(res)

    def update_id_namespace_association(
        self,
        res: "bs_td.UpdateIdNamespaceAssociationOutputTypeDef",
    ) -> "dc_td.UpdateIdNamespaceAssociationOutput":
        return dc_td.UpdateIdNamespaceAssociationOutput.make_one(res)

    def update_membership(
        self,
        res: "bs_td.UpdateMembershipOutputTypeDef",
    ) -> "dc_td.UpdateMembershipOutput":
        return dc_td.UpdateMembershipOutput.make_one(res)

    def update_privacy_budget_template(
        self,
        res: "bs_td.UpdatePrivacyBudgetTemplateOutputTypeDef",
    ) -> "dc_td.UpdatePrivacyBudgetTemplateOutput":
        return dc_td.UpdatePrivacyBudgetTemplateOutput.make_one(res)

    def update_protected_job(
        self,
        res: "bs_td.UpdateProtectedJobOutputTypeDef",
    ) -> "dc_td.UpdateProtectedJobOutput":
        return dc_td.UpdateProtectedJobOutput.make_one(res)

    def update_protected_query(
        self,
        res: "bs_td.UpdateProtectedQueryOutputTypeDef",
    ) -> "dc_td.UpdateProtectedQueryOutput":
        return dc_td.UpdateProtectedQueryOutput.make_one(res)


cleanrooms_caster = CLEANROOMSCaster()
