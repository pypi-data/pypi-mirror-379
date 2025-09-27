# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_dms import type_defs as bs_td


class DMSCaster:

    def apply_pending_maintenance_action(
        self,
        res: "bs_td.ApplyPendingMaintenanceActionResponseTypeDef",
    ) -> "dc_td.ApplyPendingMaintenanceActionResponse":
        return dc_td.ApplyPendingMaintenanceActionResponse.make_one(res)

    def batch_start_recommendations(
        self,
        res: "bs_td.BatchStartRecommendationsResponseTypeDef",
    ) -> "dc_td.BatchStartRecommendationsResponse":
        return dc_td.BatchStartRecommendationsResponse.make_one(res)

    def cancel_replication_task_assessment_run(
        self,
        res: "bs_td.CancelReplicationTaskAssessmentRunResponseTypeDef",
    ) -> "dc_td.CancelReplicationTaskAssessmentRunResponse":
        return dc_td.CancelReplicationTaskAssessmentRunResponse.make_one(res)

    def create_data_migration(
        self,
        res: "bs_td.CreateDataMigrationResponseTypeDef",
    ) -> "dc_td.CreateDataMigrationResponse":
        return dc_td.CreateDataMigrationResponse.make_one(res)

    def create_data_provider(
        self,
        res: "bs_td.CreateDataProviderResponseTypeDef",
    ) -> "dc_td.CreateDataProviderResponse":
        return dc_td.CreateDataProviderResponse.make_one(res)

    def create_endpoint(
        self,
        res: "bs_td.CreateEndpointResponseTypeDef",
    ) -> "dc_td.CreateEndpointResponse":
        return dc_td.CreateEndpointResponse.make_one(res)

    def create_event_subscription(
        self,
        res: "bs_td.CreateEventSubscriptionResponseTypeDef",
    ) -> "dc_td.CreateEventSubscriptionResponse":
        return dc_td.CreateEventSubscriptionResponse.make_one(res)

    def create_fleet_advisor_collector(
        self,
        res: "bs_td.CreateFleetAdvisorCollectorResponseTypeDef",
    ) -> "dc_td.CreateFleetAdvisorCollectorResponse":
        return dc_td.CreateFleetAdvisorCollectorResponse.make_one(res)

    def create_instance_profile(
        self,
        res: "bs_td.CreateInstanceProfileResponseTypeDef",
    ) -> "dc_td.CreateInstanceProfileResponse":
        return dc_td.CreateInstanceProfileResponse.make_one(res)

    def create_migration_project(
        self,
        res: "bs_td.CreateMigrationProjectResponseTypeDef",
    ) -> "dc_td.CreateMigrationProjectResponse":
        return dc_td.CreateMigrationProjectResponse.make_one(res)

    def create_replication_config(
        self,
        res: "bs_td.CreateReplicationConfigResponseTypeDef",
    ) -> "dc_td.CreateReplicationConfigResponse":
        return dc_td.CreateReplicationConfigResponse.make_one(res)

    def create_replication_instance(
        self,
        res: "bs_td.CreateReplicationInstanceResponseTypeDef",
    ) -> "dc_td.CreateReplicationInstanceResponse":
        return dc_td.CreateReplicationInstanceResponse.make_one(res)

    def create_replication_subnet_group(
        self,
        res: "bs_td.CreateReplicationSubnetGroupResponseTypeDef",
    ) -> "dc_td.CreateReplicationSubnetGroupResponse":
        return dc_td.CreateReplicationSubnetGroupResponse.make_one(res)

    def create_replication_task(
        self,
        res: "bs_td.CreateReplicationTaskResponseTypeDef",
    ) -> "dc_td.CreateReplicationTaskResponse":
        return dc_td.CreateReplicationTaskResponse.make_one(res)

    def delete_certificate(
        self,
        res: "bs_td.DeleteCertificateResponseTypeDef",
    ) -> "dc_td.DeleteCertificateResponse":
        return dc_td.DeleteCertificateResponse.make_one(res)

    def delete_connection(
        self,
        res: "bs_td.DeleteConnectionResponseTypeDef",
    ) -> "dc_td.DeleteConnectionResponse":
        return dc_td.DeleteConnectionResponse.make_one(res)

    def delete_data_migration(
        self,
        res: "bs_td.DeleteDataMigrationResponseTypeDef",
    ) -> "dc_td.DeleteDataMigrationResponse":
        return dc_td.DeleteDataMigrationResponse.make_one(res)

    def delete_data_provider(
        self,
        res: "bs_td.DeleteDataProviderResponseTypeDef",
    ) -> "dc_td.DeleteDataProviderResponse":
        return dc_td.DeleteDataProviderResponse.make_one(res)

    def delete_endpoint(
        self,
        res: "bs_td.DeleteEndpointResponseTypeDef",
    ) -> "dc_td.DeleteEndpointResponse":
        return dc_td.DeleteEndpointResponse.make_one(res)

    def delete_event_subscription(
        self,
        res: "bs_td.DeleteEventSubscriptionResponseTypeDef",
    ) -> "dc_td.DeleteEventSubscriptionResponse":
        return dc_td.DeleteEventSubscriptionResponse.make_one(res)

    def delete_fleet_advisor_collector(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_fleet_advisor_databases(
        self,
        res: "bs_td.DeleteFleetAdvisorDatabasesResponseTypeDef",
    ) -> "dc_td.DeleteFleetAdvisorDatabasesResponse":
        return dc_td.DeleteFleetAdvisorDatabasesResponse.make_one(res)

    def delete_instance_profile(
        self,
        res: "bs_td.DeleteInstanceProfileResponseTypeDef",
    ) -> "dc_td.DeleteInstanceProfileResponse":
        return dc_td.DeleteInstanceProfileResponse.make_one(res)

    def delete_migration_project(
        self,
        res: "bs_td.DeleteMigrationProjectResponseTypeDef",
    ) -> "dc_td.DeleteMigrationProjectResponse":
        return dc_td.DeleteMigrationProjectResponse.make_one(res)

    def delete_replication_config(
        self,
        res: "bs_td.DeleteReplicationConfigResponseTypeDef",
    ) -> "dc_td.DeleteReplicationConfigResponse":
        return dc_td.DeleteReplicationConfigResponse.make_one(res)

    def delete_replication_instance(
        self,
        res: "bs_td.DeleteReplicationInstanceResponseTypeDef",
    ) -> "dc_td.DeleteReplicationInstanceResponse":
        return dc_td.DeleteReplicationInstanceResponse.make_one(res)

    def delete_replication_task(
        self,
        res: "bs_td.DeleteReplicationTaskResponseTypeDef",
    ) -> "dc_td.DeleteReplicationTaskResponse":
        return dc_td.DeleteReplicationTaskResponse.make_one(res)

    def delete_replication_task_assessment_run(
        self,
        res: "bs_td.DeleteReplicationTaskAssessmentRunResponseTypeDef",
    ) -> "dc_td.DeleteReplicationTaskAssessmentRunResponse":
        return dc_td.DeleteReplicationTaskAssessmentRunResponse.make_one(res)

    def describe_account_attributes(
        self,
        res: "bs_td.DescribeAccountAttributesResponseTypeDef",
    ) -> "dc_td.DescribeAccountAttributesResponse":
        return dc_td.DescribeAccountAttributesResponse.make_one(res)

    def describe_applicable_individual_assessments(
        self,
        res: "bs_td.DescribeApplicableIndividualAssessmentsResponseTypeDef",
    ) -> "dc_td.DescribeApplicableIndividualAssessmentsResponse":
        return dc_td.DescribeApplicableIndividualAssessmentsResponse.make_one(res)

    def describe_certificates(
        self,
        res: "bs_td.DescribeCertificatesResponseTypeDef",
    ) -> "dc_td.DescribeCertificatesResponse":
        return dc_td.DescribeCertificatesResponse.make_one(res)

    def describe_connections(
        self,
        res: "bs_td.DescribeConnectionsResponseTypeDef",
    ) -> "dc_td.DescribeConnectionsResponse":
        return dc_td.DescribeConnectionsResponse.make_one(res)

    def describe_conversion_configuration(
        self,
        res: "bs_td.DescribeConversionConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeConversionConfigurationResponse":
        return dc_td.DescribeConversionConfigurationResponse.make_one(res)

    def describe_data_migrations(
        self,
        res: "bs_td.DescribeDataMigrationsResponseTypeDef",
    ) -> "dc_td.DescribeDataMigrationsResponse":
        return dc_td.DescribeDataMigrationsResponse.make_one(res)

    def describe_data_providers(
        self,
        res: "bs_td.DescribeDataProvidersResponseTypeDef",
    ) -> "dc_td.DescribeDataProvidersResponse":
        return dc_td.DescribeDataProvidersResponse.make_one(res)

    def describe_endpoint_settings(
        self,
        res: "bs_td.DescribeEndpointSettingsResponseTypeDef",
    ) -> "dc_td.DescribeEndpointSettingsResponse":
        return dc_td.DescribeEndpointSettingsResponse.make_one(res)

    def describe_endpoint_types(
        self,
        res: "bs_td.DescribeEndpointTypesResponseTypeDef",
    ) -> "dc_td.DescribeEndpointTypesResponse":
        return dc_td.DescribeEndpointTypesResponse.make_one(res)

    def describe_endpoints(
        self,
        res: "bs_td.DescribeEndpointsResponseTypeDef",
    ) -> "dc_td.DescribeEndpointsResponse":
        return dc_td.DescribeEndpointsResponse.make_one(res)

    def describe_engine_versions(
        self,
        res: "bs_td.DescribeEngineVersionsResponseTypeDef",
    ) -> "dc_td.DescribeEngineVersionsResponse":
        return dc_td.DescribeEngineVersionsResponse.make_one(res)

    def describe_event_categories(
        self,
        res: "bs_td.DescribeEventCategoriesResponseTypeDef",
    ) -> "dc_td.DescribeEventCategoriesResponse":
        return dc_td.DescribeEventCategoriesResponse.make_one(res)

    def describe_event_subscriptions(
        self,
        res: "bs_td.DescribeEventSubscriptionsResponseTypeDef",
    ) -> "dc_td.DescribeEventSubscriptionsResponse":
        return dc_td.DescribeEventSubscriptionsResponse.make_one(res)

    def describe_events(
        self,
        res: "bs_td.DescribeEventsResponseTypeDef",
    ) -> "dc_td.DescribeEventsResponse":
        return dc_td.DescribeEventsResponse.make_one(res)

    def describe_extension_pack_associations(
        self,
        res: "bs_td.DescribeExtensionPackAssociationsResponseTypeDef",
    ) -> "dc_td.DescribeExtensionPackAssociationsResponse":
        return dc_td.DescribeExtensionPackAssociationsResponse.make_one(res)

    def describe_fleet_advisor_collectors(
        self,
        res: "bs_td.DescribeFleetAdvisorCollectorsResponseTypeDef",
    ) -> "dc_td.DescribeFleetAdvisorCollectorsResponse":
        return dc_td.DescribeFleetAdvisorCollectorsResponse.make_one(res)

    def describe_fleet_advisor_databases(
        self,
        res: "bs_td.DescribeFleetAdvisorDatabasesResponseTypeDef",
    ) -> "dc_td.DescribeFleetAdvisorDatabasesResponse":
        return dc_td.DescribeFleetAdvisorDatabasesResponse.make_one(res)

    def describe_fleet_advisor_lsa_analysis(
        self,
        res: "bs_td.DescribeFleetAdvisorLsaAnalysisResponseTypeDef",
    ) -> "dc_td.DescribeFleetAdvisorLsaAnalysisResponse":
        return dc_td.DescribeFleetAdvisorLsaAnalysisResponse.make_one(res)

    def describe_fleet_advisor_schema_object_summary(
        self,
        res: "bs_td.DescribeFleetAdvisorSchemaObjectSummaryResponseTypeDef",
    ) -> "dc_td.DescribeFleetAdvisorSchemaObjectSummaryResponse":
        return dc_td.DescribeFleetAdvisorSchemaObjectSummaryResponse.make_one(res)

    def describe_fleet_advisor_schemas(
        self,
        res: "bs_td.DescribeFleetAdvisorSchemasResponseTypeDef",
    ) -> "dc_td.DescribeFleetAdvisorSchemasResponse":
        return dc_td.DescribeFleetAdvisorSchemasResponse.make_one(res)

    def describe_instance_profiles(
        self,
        res: "bs_td.DescribeInstanceProfilesResponseTypeDef",
    ) -> "dc_td.DescribeInstanceProfilesResponse":
        return dc_td.DescribeInstanceProfilesResponse.make_one(res)

    def describe_metadata_model_assessments(
        self,
        res: "bs_td.DescribeMetadataModelAssessmentsResponseTypeDef",
    ) -> "dc_td.DescribeMetadataModelAssessmentsResponse":
        return dc_td.DescribeMetadataModelAssessmentsResponse.make_one(res)

    def describe_metadata_model_conversions(
        self,
        res: "bs_td.DescribeMetadataModelConversionsResponseTypeDef",
    ) -> "dc_td.DescribeMetadataModelConversionsResponse":
        return dc_td.DescribeMetadataModelConversionsResponse.make_one(res)

    def describe_metadata_model_exports_as_script(
        self,
        res: "bs_td.DescribeMetadataModelExportsAsScriptResponseTypeDef",
    ) -> "dc_td.DescribeMetadataModelExportsAsScriptResponse":
        return dc_td.DescribeMetadataModelExportsAsScriptResponse.make_one(res)

    def describe_metadata_model_exports_to_target(
        self,
        res: "bs_td.DescribeMetadataModelExportsToTargetResponseTypeDef",
    ) -> "dc_td.DescribeMetadataModelExportsToTargetResponse":
        return dc_td.DescribeMetadataModelExportsToTargetResponse.make_one(res)

    def describe_metadata_model_imports(
        self,
        res: "bs_td.DescribeMetadataModelImportsResponseTypeDef",
    ) -> "dc_td.DescribeMetadataModelImportsResponse":
        return dc_td.DescribeMetadataModelImportsResponse.make_one(res)

    def describe_migration_projects(
        self,
        res: "bs_td.DescribeMigrationProjectsResponseTypeDef",
    ) -> "dc_td.DescribeMigrationProjectsResponse":
        return dc_td.DescribeMigrationProjectsResponse.make_one(res)

    def describe_orderable_replication_instances(
        self,
        res: "bs_td.DescribeOrderableReplicationInstancesResponseTypeDef",
    ) -> "dc_td.DescribeOrderableReplicationInstancesResponse":
        return dc_td.DescribeOrderableReplicationInstancesResponse.make_one(res)

    def describe_pending_maintenance_actions(
        self,
        res: "bs_td.DescribePendingMaintenanceActionsResponseTypeDef",
    ) -> "dc_td.DescribePendingMaintenanceActionsResponse":
        return dc_td.DescribePendingMaintenanceActionsResponse.make_one(res)

    def describe_recommendation_limitations(
        self,
        res: "bs_td.DescribeRecommendationLimitationsResponseTypeDef",
    ) -> "dc_td.DescribeRecommendationLimitationsResponse":
        return dc_td.DescribeRecommendationLimitationsResponse.make_one(res)

    def describe_recommendations(
        self,
        res: "bs_td.DescribeRecommendationsResponseTypeDef",
    ) -> "dc_td.DescribeRecommendationsResponse":
        return dc_td.DescribeRecommendationsResponse.make_one(res)

    def describe_refresh_schemas_status(
        self,
        res: "bs_td.DescribeRefreshSchemasStatusResponseTypeDef",
    ) -> "dc_td.DescribeRefreshSchemasStatusResponse":
        return dc_td.DescribeRefreshSchemasStatusResponse.make_one(res)

    def describe_replication_configs(
        self,
        res: "bs_td.DescribeReplicationConfigsResponseTypeDef",
    ) -> "dc_td.DescribeReplicationConfigsResponse":
        return dc_td.DescribeReplicationConfigsResponse.make_one(res)

    def describe_replication_instance_task_logs(
        self,
        res: "bs_td.DescribeReplicationInstanceTaskLogsResponseTypeDef",
    ) -> "dc_td.DescribeReplicationInstanceTaskLogsResponse":
        return dc_td.DescribeReplicationInstanceTaskLogsResponse.make_one(res)

    def describe_replication_instances(
        self,
        res: "bs_td.DescribeReplicationInstancesResponseTypeDef",
    ) -> "dc_td.DescribeReplicationInstancesResponse":
        return dc_td.DescribeReplicationInstancesResponse.make_one(res)

    def describe_replication_subnet_groups(
        self,
        res: "bs_td.DescribeReplicationSubnetGroupsResponseTypeDef",
    ) -> "dc_td.DescribeReplicationSubnetGroupsResponse":
        return dc_td.DescribeReplicationSubnetGroupsResponse.make_one(res)

    def describe_replication_table_statistics(
        self,
        res: "bs_td.DescribeReplicationTableStatisticsResponseTypeDef",
    ) -> "dc_td.DescribeReplicationTableStatisticsResponse":
        return dc_td.DescribeReplicationTableStatisticsResponse.make_one(res)

    def describe_replication_task_assessment_results(
        self,
        res: "bs_td.DescribeReplicationTaskAssessmentResultsResponseTypeDef",
    ) -> "dc_td.DescribeReplicationTaskAssessmentResultsResponse":
        return dc_td.DescribeReplicationTaskAssessmentResultsResponse.make_one(res)

    def describe_replication_task_assessment_runs(
        self,
        res: "bs_td.DescribeReplicationTaskAssessmentRunsResponseTypeDef",
    ) -> "dc_td.DescribeReplicationTaskAssessmentRunsResponse":
        return dc_td.DescribeReplicationTaskAssessmentRunsResponse.make_one(res)

    def describe_replication_task_individual_assessments(
        self,
        res: "bs_td.DescribeReplicationTaskIndividualAssessmentsResponseTypeDef",
    ) -> "dc_td.DescribeReplicationTaskIndividualAssessmentsResponse":
        return dc_td.DescribeReplicationTaskIndividualAssessmentsResponse.make_one(res)

    def describe_replication_tasks(
        self,
        res: "bs_td.DescribeReplicationTasksResponseTypeDef",
    ) -> "dc_td.DescribeReplicationTasksResponse":
        return dc_td.DescribeReplicationTasksResponse.make_one(res)

    def describe_replications(
        self,
        res: "bs_td.DescribeReplicationsResponseTypeDef",
    ) -> "dc_td.DescribeReplicationsResponse":
        return dc_td.DescribeReplicationsResponse.make_one(res)

    def describe_schemas(
        self,
        res: "bs_td.DescribeSchemasResponseTypeDef",
    ) -> "dc_td.DescribeSchemasResponse":
        return dc_td.DescribeSchemasResponse.make_one(res)

    def describe_table_statistics(
        self,
        res: "bs_td.DescribeTableStatisticsResponseTypeDef",
    ) -> "dc_td.DescribeTableStatisticsResponse":
        return dc_td.DescribeTableStatisticsResponse.make_one(res)

    def export_metadata_model_assessment(
        self,
        res: "bs_td.ExportMetadataModelAssessmentResponseTypeDef",
    ) -> "dc_td.ExportMetadataModelAssessmentResponse":
        return dc_td.ExportMetadataModelAssessmentResponse.make_one(res)

    def import_certificate(
        self,
        res: "bs_td.ImportCertificateResponseTypeDef",
    ) -> "dc_td.ImportCertificateResponse":
        return dc_td.ImportCertificateResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def modify_conversion_configuration(
        self,
        res: "bs_td.ModifyConversionConfigurationResponseTypeDef",
    ) -> "dc_td.ModifyConversionConfigurationResponse":
        return dc_td.ModifyConversionConfigurationResponse.make_one(res)

    def modify_data_migration(
        self,
        res: "bs_td.ModifyDataMigrationResponseTypeDef",
    ) -> "dc_td.ModifyDataMigrationResponse":
        return dc_td.ModifyDataMigrationResponse.make_one(res)

    def modify_data_provider(
        self,
        res: "bs_td.ModifyDataProviderResponseTypeDef",
    ) -> "dc_td.ModifyDataProviderResponse":
        return dc_td.ModifyDataProviderResponse.make_one(res)

    def modify_endpoint(
        self,
        res: "bs_td.ModifyEndpointResponseTypeDef",
    ) -> "dc_td.ModifyEndpointResponse":
        return dc_td.ModifyEndpointResponse.make_one(res)

    def modify_event_subscription(
        self,
        res: "bs_td.ModifyEventSubscriptionResponseTypeDef",
    ) -> "dc_td.ModifyEventSubscriptionResponse":
        return dc_td.ModifyEventSubscriptionResponse.make_one(res)

    def modify_instance_profile(
        self,
        res: "bs_td.ModifyInstanceProfileResponseTypeDef",
    ) -> "dc_td.ModifyInstanceProfileResponse":
        return dc_td.ModifyInstanceProfileResponse.make_one(res)

    def modify_migration_project(
        self,
        res: "bs_td.ModifyMigrationProjectResponseTypeDef",
    ) -> "dc_td.ModifyMigrationProjectResponse":
        return dc_td.ModifyMigrationProjectResponse.make_one(res)

    def modify_replication_config(
        self,
        res: "bs_td.ModifyReplicationConfigResponseTypeDef",
    ) -> "dc_td.ModifyReplicationConfigResponse":
        return dc_td.ModifyReplicationConfigResponse.make_one(res)

    def modify_replication_instance(
        self,
        res: "bs_td.ModifyReplicationInstanceResponseTypeDef",
    ) -> "dc_td.ModifyReplicationInstanceResponse":
        return dc_td.ModifyReplicationInstanceResponse.make_one(res)

    def modify_replication_subnet_group(
        self,
        res: "bs_td.ModifyReplicationSubnetGroupResponseTypeDef",
    ) -> "dc_td.ModifyReplicationSubnetGroupResponse":
        return dc_td.ModifyReplicationSubnetGroupResponse.make_one(res)

    def modify_replication_task(
        self,
        res: "bs_td.ModifyReplicationTaskResponseTypeDef",
    ) -> "dc_td.ModifyReplicationTaskResponse":
        return dc_td.ModifyReplicationTaskResponse.make_one(res)

    def move_replication_task(
        self,
        res: "bs_td.MoveReplicationTaskResponseTypeDef",
    ) -> "dc_td.MoveReplicationTaskResponse":
        return dc_td.MoveReplicationTaskResponse.make_one(res)

    def reboot_replication_instance(
        self,
        res: "bs_td.RebootReplicationInstanceResponseTypeDef",
    ) -> "dc_td.RebootReplicationInstanceResponse":
        return dc_td.RebootReplicationInstanceResponse.make_one(res)

    def refresh_schemas(
        self,
        res: "bs_td.RefreshSchemasResponseTypeDef",
    ) -> "dc_td.RefreshSchemasResponse":
        return dc_td.RefreshSchemasResponse.make_one(res)

    def reload_replication_tables(
        self,
        res: "bs_td.ReloadReplicationTablesResponseTypeDef",
    ) -> "dc_td.ReloadReplicationTablesResponse":
        return dc_td.ReloadReplicationTablesResponse.make_one(res)

    def reload_tables(
        self,
        res: "bs_td.ReloadTablesResponseTypeDef",
    ) -> "dc_td.ReloadTablesResponse":
        return dc_td.ReloadTablesResponse.make_one(res)

    def run_fleet_advisor_lsa_analysis(
        self,
        res: "bs_td.RunFleetAdvisorLsaAnalysisResponseTypeDef",
    ) -> "dc_td.RunFleetAdvisorLsaAnalysisResponse":
        return dc_td.RunFleetAdvisorLsaAnalysisResponse.make_one(res)

    def start_data_migration(
        self,
        res: "bs_td.StartDataMigrationResponseTypeDef",
    ) -> "dc_td.StartDataMigrationResponse":
        return dc_td.StartDataMigrationResponse.make_one(res)

    def start_extension_pack_association(
        self,
        res: "bs_td.StartExtensionPackAssociationResponseTypeDef",
    ) -> "dc_td.StartExtensionPackAssociationResponse":
        return dc_td.StartExtensionPackAssociationResponse.make_one(res)

    def start_metadata_model_assessment(
        self,
        res: "bs_td.StartMetadataModelAssessmentResponseTypeDef",
    ) -> "dc_td.StartMetadataModelAssessmentResponse":
        return dc_td.StartMetadataModelAssessmentResponse.make_one(res)

    def start_metadata_model_conversion(
        self,
        res: "bs_td.StartMetadataModelConversionResponseTypeDef",
    ) -> "dc_td.StartMetadataModelConversionResponse":
        return dc_td.StartMetadataModelConversionResponse.make_one(res)

    def start_metadata_model_export_as_script(
        self,
        res: "bs_td.StartMetadataModelExportAsScriptResponseTypeDef",
    ) -> "dc_td.StartMetadataModelExportAsScriptResponse":
        return dc_td.StartMetadataModelExportAsScriptResponse.make_one(res)

    def start_metadata_model_export_to_target(
        self,
        res: "bs_td.StartMetadataModelExportToTargetResponseTypeDef",
    ) -> "dc_td.StartMetadataModelExportToTargetResponse":
        return dc_td.StartMetadataModelExportToTargetResponse.make_one(res)

    def start_metadata_model_import(
        self,
        res: "bs_td.StartMetadataModelImportResponseTypeDef",
    ) -> "dc_td.StartMetadataModelImportResponse":
        return dc_td.StartMetadataModelImportResponse.make_one(res)

    def start_recommendations(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_replication(
        self,
        res: "bs_td.StartReplicationResponseTypeDef",
    ) -> "dc_td.StartReplicationResponse":
        return dc_td.StartReplicationResponse.make_one(res)

    def start_replication_task(
        self,
        res: "bs_td.StartReplicationTaskResponseTypeDef",
    ) -> "dc_td.StartReplicationTaskResponse":
        return dc_td.StartReplicationTaskResponse.make_one(res)

    def start_replication_task_assessment(
        self,
        res: "bs_td.StartReplicationTaskAssessmentResponseTypeDef",
    ) -> "dc_td.StartReplicationTaskAssessmentResponse":
        return dc_td.StartReplicationTaskAssessmentResponse.make_one(res)

    def start_replication_task_assessment_run(
        self,
        res: "bs_td.StartReplicationTaskAssessmentRunResponseTypeDef",
    ) -> "dc_td.StartReplicationTaskAssessmentRunResponse":
        return dc_td.StartReplicationTaskAssessmentRunResponse.make_one(res)

    def stop_data_migration(
        self,
        res: "bs_td.StopDataMigrationResponseTypeDef",
    ) -> "dc_td.StopDataMigrationResponse":
        return dc_td.StopDataMigrationResponse.make_one(res)

    def stop_replication(
        self,
        res: "bs_td.StopReplicationResponseTypeDef",
    ) -> "dc_td.StopReplicationResponse":
        return dc_td.StopReplicationResponse.make_one(res)

    def stop_replication_task(
        self,
        res: "bs_td.StopReplicationTaskResponseTypeDef",
    ) -> "dc_td.StopReplicationTaskResponse":
        return dc_td.StopReplicationTaskResponse.make_one(res)

    def test_connection(
        self,
        res: "bs_td.TestConnectionResponseTypeDef",
    ) -> "dc_td.TestConnectionResponse":
        return dc_td.TestConnectionResponse.make_one(res)

    def update_subscriptions_to_event_bridge(
        self,
        res: "bs_td.UpdateSubscriptionsToEventBridgeResponseTypeDef",
    ) -> "dc_td.UpdateSubscriptionsToEventBridgeResponse":
        return dc_td.UpdateSubscriptionsToEventBridgeResponse.make_one(res)


dms_caster = DMSCaster()
