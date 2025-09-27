# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_datazone import type_defs as bs_td


class DATAZONECaster:

    def accept_predictions(
        self,
        res: "bs_td.AcceptPredictionsOutputTypeDef",
    ) -> "dc_td.AcceptPredictionsOutput":
        return dc_td.AcceptPredictionsOutput.make_one(res)

    def accept_subscription_request(
        self,
        res: "bs_td.AcceptSubscriptionRequestOutputTypeDef",
    ) -> "dc_td.AcceptSubscriptionRequestOutput":
        return dc_td.AcceptSubscriptionRequestOutput.make_one(res)

    def add_policy_grant(
        self,
        res: "bs_td.AddPolicyGrantOutputTypeDef",
    ) -> "dc_td.AddPolicyGrantOutput":
        return dc_td.AddPolicyGrantOutput.make_one(res)

    def cancel_subscription(
        self,
        res: "bs_td.CancelSubscriptionOutputTypeDef",
    ) -> "dc_td.CancelSubscriptionOutput":
        return dc_td.CancelSubscriptionOutput.make_one(res)

    def create_account_pool(
        self,
        res: "bs_td.CreateAccountPoolOutputTypeDef",
    ) -> "dc_td.CreateAccountPoolOutput":
        return dc_td.CreateAccountPoolOutput.make_one(res)

    def create_asset(
        self,
        res: "bs_td.CreateAssetOutputTypeDef",
    ) -> "dc_td.CreateAssetOutput":
        return dc_td.CreateAssetOutput.make_one(res)

    def create_asset_filter(
        self,
        res: "bs_td.CreateAssetFilterOutputTypeDef",
    ) -> "dc_td.CreateAssetFilterOutput":
        return dc_td.CreateAssetFilterOutput.make_one(res)

    def create_asset_revision(
        self,
        res: "bs_td.CreateAssetRevisionOutputTypeDef",
    ) -> "dc_td.CreateAssetRevisionOutput":
        return dc_td.CreateAssetRevisionOutput.make_one(res)

    def create_asset_type(
        self,
        res: "bs_td.CreateAssetTypeOutputTypeDef",
    ) -> "dc_td.CreateAssetTypeOutput":
        return dc_td.CreateAssetTypeOutput.make_one(res)

    def create_connection(
        self,
        res: "bs_td.CreateConnectionOutputTypeDef",
    ) -> "dc_td.CreateConnectionOutput":
        return dc_td.CreateConnectionOutput.make_one(res)

    def create_data_product(
        self,
        res: "bs_td.CreateDataProductOutputTypeDef",
    ) -> "dc_td.CreateDataProductOutput":
        return dc_td.CreateDataProductOutput.make_one(res)

    def create_data_product_revision(
        self,
        res: "bs_td.CreateDataProductRevisionOutputTypeDef",
    ) -> "dc_td.CreateDataProductRevisionOutput":
        return dc_td.CreateDataProductRevisionOutput.make_one(res)

    def create_data_source(
        self,
        res: "bs_td.CreateDataSourceOutputTypeDef",
    ) -> "dc_td.CreateDataSourceOutput":
        return dc_td.CreateDataSourceOutput.make_one(res)

    def create_domain(
        self,
        res: "bs_td.CreateDomainOutputTypeDef",
    ) -> "dc_td.CreateDomainOutput":
        return dc_td.CreateDomainOutput.make_one(res)

    def create_domain_unit(
        self,
        res: "bs_td.CreateDomainUnitOutputTypeDef",
    ) -> "dc_td.CreateDomainUnitOutput":
        return dc_td.CreateDomainUnitOutput.make_one(res)

    def create_environment(
        self,
        res: "bs_td.CreateEnvironmentOutputTypeDef",
    ) -> "dc_td.CreateEnvironmentOutput":
        return dc_td.CreateEnvironmentOutput.make_one(res)

    def create_environment_action(
        self,
        res: "bs_td.CreateEnvironmentActionOutputTypeDef",
    ) -> "dc_td.CreateEnvironmentActionOutput":
        return dc_td.CreateEnvironmentActionOutput.make_one(res)

    def create_environment_blueprint(
        self,
        res: "bs_td.CreateEnvironmentBlueprintOutputTypeDef",
    ) -> "dc_td.CreateEnvironmentBlueprintOutput":
        return dc_td.CreateEnvironmentBlueprintOutput.make_one(res)

    def create_environment_profile(
        self,
        res: "bs_td.CreateEnvironmentProfileOutputTypeDef",
    ) -> "dc_td.CreateEnvironmentProfileOutput":
        return dc_td.CreateEnvironmentProfileOutput.make_one(res)

    def create_form_type(
        self,
        res: "bs_td.CreateFormTypeOutputTypeDef",
    ) -> "dc_td.CreateFormTypeOutput":
        return dc_td.CreateFormTypeOutput.make_one(res)

    def create_glossary(
        self,
        res: "bs_td.CreateGlossaryOutputTypeDef",
    ) -> "dc_td.CreateGlossaryOutput":
        return dc_td.CreateGlossaryOutput.make_one(res)

    def create_glossary_term(
        self,
        res: "bs_td.CreateGlossaryTermOutputTypeDef",
    ) -> "dc_td.CreateGlossaryTermOutput":
        return dc_td.CreateGlossaryTermOutput.make_one(res)

    def create_group_profile(
        self,
        res: "bs_td.CreateGroupProfileOutputTypeDef",
    ) -> "dc_td.CreateGroupProfileOutput":
        return dc_td.CreateGroupProfileOutput.make_one(res)

    def create_listing_change_set(
        self,
        res: "bs_td.CreateListingChangeSetOutputTypeDef",
    ) -> "dc_td.CreateListingChangeSetOutput":
        return dc_td.CreateListingChangeSetOutput.make_one(res)

    def create_project(
        self,
        res: "bs_td.CreateProjectOutputTypeDef",
    ) -> "dc_td.CreateProjectOutput":
        return dc_td.CreateProjectOutput.make_one(res)

    def create_project_profile(
        self,
        res: "bs_td.CreateProjectProfileOutputTypeDef",
    ) -> "dc_td.CreateProjectProfileOutput":
        return dc_td.CreateProjectProfileOutput.make_one(res)

    def create_rule(
        self,
        res: "bs_td.CreateRuleOutputTypeDef",
    ) -> "dc_td.CreateRuleOutput":
        return dc_td.CreateRuleOutput.make_one(res)

    def create_subscription_grant(
        self,
        res: "bs_td.CreateSubscriptionGrantOutputTypeDef",
    ) -> "dc_td.CreateSubscriptionGrantOutput":
        return dc_td.CreateSubscriptionGrantOutput.make_one(res)

    def create_subscription_request(
        self,
        res: "bs_td.CreateSubscriptionRequestOutputTypeDef",
    ) -> "dc_td.CreateSubscriptionRequestOutput":
        return dc_td.CreateSubscriptionRequestOutput.make_one(res)

    def create_subscription_target(
        self,
        res: "bs_td.CreateSubscriptionTargetOutputTypeDef",
    ) -> "dc_td.CreateSubscriptionTargetOutput":
        return dc_td.CreateSubscriptionTargetOutput.make_one(res)

    def create_user_profile(
        self,
        res: "bs_td.CreateUserProfileOutputTypeDef",
    ) -> "dc_td.CreateUserProfileOutput":
        return dc_td.CreateUserProfileOutput.make_one(res)

    def delete_asset_filter(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_connection(
        self,
        res: "bs_td.DeleteConnectionOutputTypeDef",
    ) -> "dc_td.DeleteConnectionOutput":
        return dc_td.DeleteConnectionOutput.make_one(res)

    def delete_data_source(
        self,
        res: "bs_td.DeleteDataSourceOutputTypeDef",
    ) -> "dc_td.DeleteDataSourceOutput":
        return dc_td.DeleteDataSourceOutput.make_one(res)

    def delete_domain(
        self,
        res: "bs_td.DeleteDomainOutputTypeDef",
    ) -> "dc_td.DeleteDomainOutput":
        return dc_td.DeleteDomainOutput.make_one(res)

    def delete_environment(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_environment_action(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_environment_blueprint(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_environment_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_subscription_grant(
        self,
        res: "bs_td.DeleteSubscriptionGrantOutputTypeDef",
    ) -> "dc_td.DeleteSubscriptionGrantOutput":
        return dc_td.DeleteSubscriptionGrantOutput.make_one(res)

    def delete_subscription_request(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_subscription_target(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_account_pool(
        self,
        res: "bs_td.GetAccountPoolOutputTypeDef",
    ) -> "dc_td.GetAccountPoolOutput":
        return dc_td.GetAccountPoolOutput.make_one(res)

    def get_asset(
        self,
        res: "bs_td.GetAssetOutputTypeDef",
    ) -> "dc_td.GetAssetOutput":
        return dc_td.GetAssetOutput.make_one(res)

    def get_asset_filter(
        self,
        res: "bs_td.GetAssetFilterOutputTypeDef",
    ) -> "dc_td.GetAssetFilterOutput":
        return dc_td.GetAssetFilterOutput.make_one(res)

    def get_asset_type(
        self,
        res: "bs_td.GetAssetTypeOutputTypeDef",
    ) -> "dc_td.GetAssetTypeOutput":
        return dc_td.GetAssetTypeOutput.make_one(res)

    def get_connection(
        self,
        res: "bs_td.GetConnectionOutputTypeDef",
    ) -> "dc_td.GetConnectionOutput":
        return dc_td.GetConnectionOutput.make_one(res)

    def get_data_product(
        self,
        res: "bs_td.GetDataProductOutputTypeDef",
    ) -> "dc_td.GetDataProductOutput":
        return dc_td.GetDataProductOutput.make_one(res)

    def get_data_source(
        self,
        res: "bs_td.GetDataSourceOutputTypeDef",
    ) -> "dc_td.GetDataSourceOutput":
        return dc_td.GetDataSourceOutput.make_one(res)

    def get_data_source_run(
        self,
        res: "bs_td.GetDataSourceRunOutputTypeDef",
    ) -> "dc_td.GetDataSourceRunOutput":
        return dc_td.GetDataSourceRunOutput.make_one(res)

    def get_domain(
        self,
        res: "bs_td.GetDomainOutputTypeDef",
    ) -> "dc_td.GetDomainOutput":
        return dc_td.GetDomainOutput.make_one(res)

    def get_domain_unit(
        self,
        res: "bs_td.GetDomainUnitOutputTypeDef",
    ) -> "dc_td.GetDomainUnitOutput":
        return dc_td.GetDomainUnitOutput.make_one(res)

    def get_environment(
        self,
        res: "bs_td.GetEnvironmentOutputTypeDef",
    ) -> "dc_td.GetEnvironmentOutput":
        return dc_td.GetEnvironmentOutput.make_one(res)

    def get_environment_action(
        self,
        res: "bs_td.GetEnvironmentActionOutputTypeDef",
    ) -> "dc_td.GetEnvironmentActionOutput":
        return dc_td.GetEnvironmentActionOutput.make_one(res)

    def get_environment_blueprint(
        self,
        res: "bs_td.GetEnvironmentBlueprintOutputTypeDef",
    ) -> "dc_td.GetEnvironmentBlueprintOutput":
        return dc_td.GetEnvironmentBlueprintOutput.make_one(res)

    def get_environment_blueprint_configuration(
        self,
        res: "bs_td.GetEnvironmentBlueprintConfigurationOutputTypeDef",
    ) -> "dc_td.GetEnvironmentBlueprintConfigurationOutput":
        return dc_td.GetEnvironmentBlueprintConfigurationOutput.make_one(res)

    def get_environment_credentials(
        self,
        res: "bs_td.GetEnvironmentCredentialsOutputTypeDef",
    ) -> "dc_td.GetEnvironmentCredentialsOutput":
        return dc_td.GetEnvironmentCredentialsOutput.make_one(res)

    def get_environment_profile(
        self,
        res: "bs_td.GetEnvironmentProfileOutputTypeDef",
    ) -> "dc_td.GetEnvironmentProfileOutput":
        return dc_td.GetEnvironmentProfileOutput.make_one(res)

    def get_form_type(
        self,
        res: "bs_td.GetFormTypeOutputTypeDef",
    ) -> "dc_td.GetFormTypeOutput":
        return dc_td.GetFormTypeOutput.make_one(res)

    def get_glossary(
        self,
        res: "bs_td.GetGlossaryOutputTypeDef",
    ) -> "dc_td.GetGlossaryOutput":
        return dc_td.GetGlossaryOutput.make_one(res)

    def get_glossary_term(
        self,
        res: "bs_td.GetGlossaryTermOutputTypeDef",
    ) -> "dc_td.GetGlossaryTermOutput":
        return dc_td.GetGlossaryTermOutput.make_one(res)

    def get_group_profile(
        self,
        res: "bs_td.GetGroupProfileOutputTypeDef",
    ) -> "dc_td.GetGroupProfileOutput":
        return dc_td.GetGroupProfileOutput.make_one(res)

    def get_iam_portal_login_url(
        self,
        res: "bs_td.GetIamPortalLoginUrlOutputTypeDef",
    ) -> "dc_td.GetIamPortalLoginUrlOutput":
        return dc_td.GetIamPortalLoginUrlOutput.make_one(res)

    def get_job_run(
        self,
        res: "bs_td.GetJobRunOutputTypeDef",
    ) -> "dc_td.GetJobRunOutput":
        return dc_td.GetJobRunOutput.make_one(res)

    def get_lineage_event(
        self,
        res: "bs_td.GetLineageEventOutputTypeDef",
    ) -> "dc_td.GetLineageEventOutput":
        return dc_td.GetLineageEventOutput.make_one(res)

    def get_lineage_node(
        self,
        res: "bs_td.GetLineageNodeOutputTypeDef",
    ) -> "dc_td.GetLineageNodeOutput":
        return dc_td.GetLineageNodeOutput.make_one(res)

    def get_listing(
        self,
        res: "bs_td.GetListingOutputTypeDef",
    ) -> "dc_td.GetListingOutput":
        return dc_td.GetListingOutput.make_one(res)

    def get_metadata_generation_run(
        self,
        res: "bs_td.GetMetadataGenerationRunOutputTypeDef",
    ) -> "dc_td.GetMetadataGenerationRunOutput":
        return dc_td.GetMetadataGenerationRunOutput.make_one(res)

    def get_project(
        self,
        res: "bs_td.GetProjectOutputTypeDef",
    ) -> "dc_td.GetProjectOutput":
        return dc_td.GetProjectOutput.make_one(res)

    def get_project_profile(
        self,
        res: "bs_td.GetProjectProfileOutputTypeDef",
    ) -> "dc_td.GetProjectProfileOutput":
        return dc_td.GetProjectProfileOutput.make_one(res)

    def get_rule(
        self,
        res: "bs_td.GetRuleOutputTypeDef",
    ) -> "dc_td.GetRuleOutput":
        return dc_td.GetRuleOutput.make_one(res)

    def get_subscription(
        self,
        res: "bs_td.GetSubscriptionOutputTypeDef",
    ) -> "dc_td.GetSubscriptionOutput":
        return dc_td.GetSubscriptionOutput.make_one(res)

    def get_subscription_grant(
        self,
        res: "bs_td.GetSubscriptionGrantOutputTypeDef",
    ) -> "dc_td.GetSubscriptionGrantOutput":
        return dc_td.GetSubscriptionGrantOutput.make_one(res)

    def get_subscription_request_details(
        self,
        res: "bs_td.GetSubscriptionRequestDetailsOutputTypeDef",
    ) -> "dc_td.GetSubscriptionRequestDetailsOutput":
        return dc_td.GetSubscriptionRequestDetailsOutput.make_one(res)

    def get_subscription_target(
        self,
        res: "bs_td.GetSubscriptionTargetOutputTypeDef",
    ) -> "dc_td.GetSubscriptionTargetOutput":
        return dc_td.GetSubscriptionTargetOutput.make_one(res)

    def get_time_series_data_point(
        self,
        res: "bs_td.GetTimeSeriesDataPointOutputTypeDef",
    ) -> "dc_td.GetTimeSeriesDataPointOutput":
        return dc_td.GetTimeSeriesDataPointOutput.make_one(res)

    def get_user_profile(
        self,
        res: "bs_td.GetUserProfileOutputTypeDef",
    ) -> "dc_td.GetUserProfileOutput":
        return dc_td.GetUserProfileOutput.make_one(res)

    def list_account_pools(
        self,
        res: "bs_td.ListAccountPoolsOutputTypeDef",
    ) -> "dc_td.ListAccountPoolsOutput":
        return dc_td.ListAccountPoolsOutput.make_one(res)

    def list_accounts_in_account_pool(
        self,
        res: "bs_td.ListAccountsInAccountPoolOutputTypeDef",
    ) -> "dc_td.ListAccountsInAccountPoolOutput":
        return dc_td.ListAccountsInAccountPoolOutput.make_one(res)

    def list_asset_filters(
        self,
        res: "bs_td.ListAssetFiltersOutputTypeDef",
    ) -> "dc_td.ListAssetFiltersOutput":
        return dc_td.ListAssetFiltersOutput.make_one(res)

    def list_asset_revisions(
        self,
        res: "bs_td.ListAssetRevisionsOutputTypeDef",
    ) -> "dc_td.ListAssetRevisionsOutput":
        return dc_td.ListAssetRevisionsOutput.make_one(res)

    def list_connections(
        self,
        res: "bs_td.ListConnectionsOutputTypeDef",
    ) -> "dc_td.ListConnectionsOutput":
        return dc_td.ListConnectionsOutput.make_one(res)

    def list_data_product_revisions(
        self,
        res: "bs_td.ListDataProductRevisionsOutputTypeDef",
    ) -> "dc_td.ListDataProductRevisionsOutput":
        return dc_td.ListDataProductRevisionsOutput.make_one(res)

    def list_data_source_run_activities(
        self,
        res: "bs_td.ListDataSourceRunActivitiesOutputTypeDef",
    ) -> "dc_td.ListDataSourceRunActivitiesOutput":
        return dc_td.ListDataSourceRunActivitiesOutput.make_one(res)

    def list_data_source_runs(
        self,
        res: "bs_td.ListDataSourceRunsOutputTypeDef",
    ) -> "dc_td.ListDataSourceRunsOutput":
        return dc_td.ListDataSourceRunsOutput.make_one(res)

    def list_data_sources(
        self,
        res: "bs_td.ListDataSourcesOutputTypeDef",
    ) -> "dc_td.ListDataSourcesOutput":
        return dc_td.ListDataSourcesOutput.make_one(res)

    def list_domain_units_for_parent(
        self,
        res: "bs_td.ListDomainUnitsForParentOutputTypeDef",
    ) -> "dc_td.ListDomainUnitsForParentOutput":
        return dc_td.ListDomainUnitsForParentOutput.make_one(res)

    def list_domains(
        self,
        res: "bs_td.ListDomainsOutputTypeDef",
    ) -> "dc_td.ListDomainsOutput":
        return dc_td.ListDomainsOutput.make_one(res)

    def list_entity_owners(
        self,
        res: "bs_td.ListEntityOwnersOutputTypeDef",
    ) -> "dc_td.ListEntityOwnersOutput":
        return dc_td.ListEntityOwnersOutput.make_one(res)

    def list_environment_actions(
        self,
        res: "bs_td.ListEnvironmentActionsOutputTypeDef",
    ) -> "dc_td.ListEnvironmentActionsOutput":
        return dc_td.ListEnvironmentActionsOutput.make_one(res)

    def list_environment_blueprint_configurations(
        self,
        res: "bs_td.ListEnvironmentBlueprintConfigurationsOutputTypeDef",
    ) -> "dc_td.ListEnvironmentBlueprintConfigurationsOutput":
        return dc_td.ListEnvironmentBlueprintConfigurationsOutput.make_one(res)

    def list_environment_blueprints(
        self,
        res: "bs_td.ListEnvironmentBlueprintsOutputTypeDef",
    ) -> "dc_td.ListEnvironmentBlueprintsOutput":
        return dc_td.ListEnvironmentBlueprintsOutput.make_one(res)

    def list_environment_profiles(
        self,
        res: "bs_td.ListEnvironmentProfilesOutputTypeDef",
    ) -> "dc_td.ListEnvironmentProfilesOutput":
        return dc_td.ListEnvironmentProfilesOutput.make_one(res)

    def list_environments(
        self,
        res: "bs_td.ListEnvironmentsOutputTypeDef",
    ) -> "dc_td.ListEnvironmentsOutput":
        return dc_td.ListEnvironmentsOutput.make_one(res)

    def list_job_runs(
        self,
        res: "bs_td.ListJobRunsOutputTypeDef",
    ) -> "dc_td.ListJobRunsOutput":
        return dc_td.ListJobRunsOutput.make_one(res)

    def list_lineage_events(
        self,
        res: "bs_td.ListLineageEventsOutputTypeDef",
    ) -> "dc_td.ListLineageEventsOutput":
        return dc_td.ListLineageEventsOutput.make_one(res)

    def list_lineage_node_history(
        self,
        res: "bs_td.ListLineageNodeHistoryOutputTypeDef",
    ) -> "dc_td.ListLineageNodeHistoryOutput":
        return dc_td.ListLineageNodeHistoryOutput.make_one(res)

    def list_metadata_generation_runs(
        self,
        res: "bs_td.ListMetadataGenerationRunsOutputTypeDef",
    ) -> "dc_td.ListMetadataGenerationRunsOutput":
        return dc_td.ListMetadataGenerationRunsOutput.make_one(res)

    def list_notifications(
        self,
        res: "bs_td.ListNotificationsOutputTypeDef",
    ) -> "dc_td.ListNotificationsOutput":
        return dc_td.ListNotificationsOutput.make_one(res)

    def list_policy_grants(
        self,
        res: "bs_td.ListPolicyGrantsOutputTypeDef",
    ) -> "dc_td.ListPolicyGrantsOutput":
        return dc_td.ListPolicyGrantsOutput.make_one(res)

    def list_project_memberships(
        self,
        res: "bs_td.ListProjectMembershipsOutputTypeDef",
    ) -> "dc_td.ListProjectMembershipsOutput":
        return dc_td.ListProjectMembershipsOutput.make_one(res)

    def list_project_profiles(
        self,
        res: "bs_td.ListProjectProfilesOutputTypeDef",
    ) -> "dc_td.ListProjectProfilesOutput":
        return dc_td.ListProjectProfilesOutput.make_one(res)

    def list_projects(
        self,
        res: "bs_td.ListProjectsOutputTypeDef",
    ) -> "dc_td.ListProjectsOutput":
        return dc_td.ListProjectsOutput.make_one(res)

    def list_rules(
        self,
        res: "bs_td.ListRulesOutputTypeDef",
    ) -> "dc_td.ListRulesOutput":
        return dc_td.ListRulesOutput.make_one(res)

    def list_subscription_grants(
        self,
        res: "bs_td.ListSubscriptionGrantsOutputTypeDef",
    ) -> "dc_td.ListSubscriptionGrantsOutput":
        return dc_td.ListSubscriptionGrantsOutput.make_one(res)

    def list_subscription_requests(
        self,
        res: "bs_td.ListSubscriptionRequestsOutputTypeDef",
    ) -> "dc_td.ListSubscriptionRequestsOutput":
        return dc_td.ListSubscriptionRequestsOutput.make_one(res)

    def list_subscription_targets(
        self,
        res: "bs_td.ListSubscriptionTargetsOutputTypeDef",
    ) -> "dc_td.ListSubscriptionTargetsOutput":
        return dc_td.ListSubscriptionTargetsOutput.make_one(res)

    def list_subscriptions(
        self,
        res: "bs_td.ListSubscriptionsOutputTypeDef",
    ) -> "dc_td.ListSubscriptionsOutput":
        return dc_td.ListSubscriptionsOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_time_series_data_points(
        self,
        res: "bs_td.ListTimeSeriesDataPointsOutputTypeDef",
    ) -> "dc_td.ListTimeSeriesDataPointsOutput":
        return dc_td.ListTimeSeriesDataPointsOutput.make_one(res)

    def post_lineage_event(
        self,
        res: "bs_td.PostLineageEventOutputTypeDef",
    ) -> "dc_td.PostLineageEventOutput":
        return dc_td.PostLineageEventOutput.make_one(res)

    def post_time_series_data_points(
        self,
        res: "bs_td.PostTimeSeriesDataPointsOutputTypeDef",
    ) -> "dc_td.PostTimeSeriesDataPointsOutput":
        return dc_td.PostTimeSeriesDataPointsOutput.make_one(res)

    def put_environment_blueprint_configuration(
        self,
        res: "bs_td.PutEnvironmentBlueprintConfigurationOutputTypeDef",
    ) -> "dc_td.PutEnvironmentBlueprintConfigurationOutput":
        return dc_td.PutEnvironmentBlueprintConfigurationOutput.make_one(res)

    def reject_predictions(
        self,
        res: "bs_td.RejectPredictionsOutputTypeDef",
    ) -> "dc_td.RejectPredictionsOutput":
        return dc_td.RejectPredictionsOutput.make_one(res)

    def reject_subscription_request(
        self,
        res: "bs_td.RejectSubscriptionRequestOutputTypeDef",
    ) -> "dc_td.RejectSubscriptionRequestOutput":
        return dc_td.RejectSubscriptionRequestOutput.make_one(res)

    def revoke_subscription(
        self,
        res: "bs_td.RevokeSubscriptionOutputTypeDef",
    ) -> "dc_td.RevokeSubscriptionOutput":
        return dc_td.RevokeSubscriptionOutput.make_one(res)

    def search(
        self,
        res: "bs_td.SearchOutputTypeDef",
    ) -> "dc_td.SearchOutput":
        return dc_td.SearchOutput.make_one(res)

    def search_group_profiles(
        self,
        res: "bs_td.SearchGroupProfilesOutputTypeDef",
    ) -> "dc_td.SearchGroupProfilesOutput":
        return dc_td.SearchGroupProfilesOutput.make_one(res)

    def search_listings(
        self,
        res: "bs_td.SearchListingsOutputTypeDef",
    ) -> "dc_td.SearchListingsOutput":
        return dc_td.SearchListingsOutput.make_one(res)

    def search_types(
        self,
        res: "bs_td.SearchTypesOutputTypeDef",
    ) -> "dc_td.SearchTypesOutput":
        return dc_td.SearchTypesOutput.make_one(res)

    def search_user_profiles(
        self,
        res: "bs_td.SearchUserProfilesOutputTypeDef",
    ) -> "dc_td.SearchUserProfilesOutput":
        return dc_td.SearchUserProfilesOutput.make_one(res)

    def start_data_source_run(
        self,
        res: "bs_td.StartDataSourceRunOutputTypeDef",
    ) -> "dc_td.StartDataSourceRunOutput":
        return dc_td.StartDataSourceRunOutput.make_one(res)

    def start_metadata_generation_run(
        self,
        res: "bs_td.StartMetadataGenerationRunOutputTypeDef",
    ) -> "dc_td.StartMetadataGenerationRunOutput":
        return dc_td.StartMetadataGenerationRunOutput.make_one(res)

    def update_account_pool(
        self,
        res: "bs_td.UpdateAccountPoolOutputTypeDef",
    ) -> "dc_td.UpdateAccountPoolOutput":
        return dc_td.UpdateAccountPoolOutput.make_one(res)

    def update_asset_filter(
        self,
        res: "bs_td.UpdateAssetFilterOutputTypeDef",
    ) -> "dc_td.UpdateAssetFilterOutput":
        return dc_td.UpdateAssetFilterOutput.make_one(res)

    def update_connection(
        self,
        res: "bs_td.UpdateConnectionOutputTypeDef",
    ) -> "dc_td.UpdateConnectionOutput":
        return dc_td.UpdateConnectionOutput.make_one(res)

    def update_data_source(
        self,
        res: "bs_td.UpdateDataSourceOutputTypeDef",
    ) -> "dc_td.UpdateDataSourceOutput":
        return dc_td.UpdateDataSourceOutput.make_one(res)

    def update_domain(
        self,
        res: "bs_td.UpdateDomainOutputTypeDef",
    ) -> "dc_td.UpdateDomainOutput":
        return dc_td.UpdateDomainOutput.make_one(res)

    def update_domain_unit(
        self,
        res: "bs_td.UpdateDomainUnitOutputTypeDef",
    ) -> "dc_td.UpdateDomainUnitOutput":
        return dc_td.UpdateDomainUnitOutput.make_one(res)

    def update_environment(
        self,
        res: "bs_td.UpdateEnvironmentOutputTypeDef",
    ) -> "dc_td.UpdateEnvironmentOutput":
        return dc_td.UpdateEnvironmentOutput.make_one(res)

    def update_environment_action(
        self,
        res: "bs_td.UpdateEnvironmentActionOutputTypeDef",
    ) -> "dc_td.UpdateEnvironmentActionOutput":
        return dc_td.UpdateEnvironmentActionOutput.make_one(res)

    def update_environment_blueprint(
        self,
        res: "bs_td.UpdateEnvironmentBlueprintOutputTypeDef",
    ) -> "dc_td.UpdateEnvironmentBlueprintOutput":
        return dc_td.UpdateEnvironmentBlueprintOutput.make_one(res)

    def update_environment_profile(
        self,
        res: "bs_td.UpdateEnvironmentProfileOutputTypeDef",
    ) -> "dc_td.UpdateEnvironmentProfileOutput":
        return dc_td.UpdateEnvironmentProfileOutput.make_one(res)

    def update_glossary(
        self,
        res: "bs_td.UpdateGlossaryOutputTypeDef",
    ) -> "dc_td.UpdateGlossaryOutput":
        return dc_td.UpdateGlossaryOutput.make_one(res)

    def update_glossary_term(
        self,
        res: "bs_td.UpdateGlossaryTermOutputTypeDef",
    ) -> "dc_td.UpdateGlossaryTermOutput":
        return dc_td.UpdateGlossaryTermOutput.make_one(res)

    def update_group_profile(
        self,
        res: "bs_td.UpdateGroupProfileOutputTypeDef",
    ) -> "dc_td.UpdateGroupProfileOutput":
        return dc_td.UpdateGroupProfileOutput.make_one(res)

    def update_project(
        self,
        res: "bs_td.UpdateProjectOutputTypeDef",
    ) -> "dc_td.UpdateProjectOutput":
        return dc_td.UpdateProjectOutput.make_one(res)

    def update_project_profile(
        self,
        res: "bs_td.UpdateProjectProfileOutputTypeDef",
    ) -> "dc_td.UpdateProjectProfileOutput":
        return dc_td.UpdateProjectProfileOutput.make_one(res)

    def update_rule(
        self,
        res: "bs_td.UpdateRuleOutputTypeDef",
    ) -> "dc_td.UpdateRuleOutput":
        return dc_td.UpdateRuleOutput.make_one(res)

    def update_subscription_grant_status(
        self,
        res: "bs_td.UpdateSubscriptionGrantStatusOutputTypeDef",
    ) -> "dc_td.UpdateSubscriptionGrantStatusOutput":
        return dc_td.UpdateSubscriptionGrantStatusOutput.make_one(res)

    def update_subscription_request(
        self,
        res: "bs_td.UpdateSubscriptionRequestOutputTypeDef",
    ) -> "dc_td.UpdateSubscriptionRequestOutput":
        return dc_td.UpdateSubscriptionRequestOutput.make_one(res)

    def update_subscription_target(
        self,
        res: "bs_td.UpdateSubscriptionTargetOutputTypeDef",
    ) -> "dc_td.UpdateSubscriptionTargetOutput":
        return dc_td.UpdateSubscriptionTargetOutput.make_one(res)

    def update_user_profile(
        self,
        res: "bs_td.UpdateUserProfileOutputTypeDef",
    ) -> "dc_td.UpdateUserProfileOutput":
        return dc_td.UpdateUserProfileOutput.make_one(res)


datazone_caster = DATAZONECaster()
