# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_glue import type_defs as bs_td


class GLUECaster:

    def batch_create_partition(
        self,
        res: "bs_td.BatchCreatePartitionResponseTypeDef",
    ) -> "dc_td.BatchCreatePartitionResponse":
        return dc_td.BatchCreatePartitionResponse.make_one(res)

    def batch_delete_connection(
        self,
        res: "bs_td.BatchDeleteConnectionResponseTypeDef",
    ) -> "dc_td.BatchDeleteConnectionResponse":
        return dc_td.BatchDeleteConnectionResponse.make_one(res)

    def batch_delete_partition(
        self,
        res: "bs_td.BatchDeletePartitionResponseTypeDef",
    ) -> "dc_td.BatchDeletePartitionResponse":
        return dc_td.BatchDeletePartitionResponse.make_one(res)

    def batch_delete_table(
        self,
        res: "bs_td.BatchDeleteTableResponseTypeDef",
    ) -> "dc_td.BatchDeleteTableResponse":
        return dc_td.BatchDeleteTableResponse.make_one(res)

    def batch_delete_table_version(
        self,
        res: "bs_td.BatchDeleteTableVersionResponseTypeDef",
    ) -> "dc_td.BatchDeleteTableVersionResponse":
        return dc_td.BatchDeleteTableVersionResponse.make_one(res)

    def batch_get_blueprints(
        self,
        res: "bs_td.BatchGetBlueprintsResponseTypeDef",
    ) -> "dc_td.BatchGetBlueprintsResponse":
        return dc_td.BatchGetBlueprintsResponse.make_one(res)

    def batch_get_crawlers(
        self,
        res: "bs_td.BatchGetCrawlersResponseTypeDef",
    ) -> "dc_td.BatchGetCrawlersResponse":
        return dc_td.BatchGetCrawlersResponse.make_one(res)

    def batch_get_custom_entity_types(
        self,
        res: "bs_td.BatchGetCustomEntityTypesResponseTypeDef",
    ) -> "dc_td.BatchGetCustomEntityTypesResponse":
        return dc_td.BatchGetCustomEntityTypesResponse.make_one(res)

    def batch_get_data_quality_result(
        self,
        res: "bs_td.BatchGetDataQualityResultResponseTypeDef",
    ) -> "dc_td.BatchGetDataQualityResultResponse":
        return dc_td.BatchGetDataQualityResultResponse.make_one(res)

    def batch_get_dev_endpoints(
        self,
        res: "bs_td.BatchGetDevEndpointsResponseTypeDef",
    ) -> "dc_td.BatchGetDevEndpointsResponse":
        return dc_td.BatchGetDevEndpointsResponse.make_one(res)

    def batch_get_jobs(
        self,
        res: "bs_td.BatchGetJobsResponseTypeDef",
    ) -> "dc_td.BatchGetJobsResponse":
        return dc_td.BatchGetJobsResponse.make_one(res)

    def batch_get_partition(
        self,
        res: "bs_td.BatchGetPartitionResponseTypeDef",
    ) -> "dc_td.BatchGetPartitionResponse":
        return dc_td.BatchGetPartitionResponse.make_one(res)

    def batch_get_table_optimizer(
        self,
        res: "bs_td.BatchGetTableOptimizerResponseTypeDef",
    ) -> "dc_td.BatchGetTableOptimizerResponse":
        return dc_td.BatchGetTableOptimizerResponse.make_one(res)

    def batch_get_triggers(
        self,
        res: "bs_td.BatchGetTriggersResponseTypeDef",
    ) -> "dc_td.BatchGetTriggersResponse":
        return dc_td.BatchGetTriggersResponse.make_one(res)

    def batch_get_workflows(
        self,
        res: "bs_td.BatchGetWorkflowsResponseTypeDef",
    ) -> "dc_td.BatchGetWorkflowsResponse":
        return dc_td.BatchGetWorkflowsResponse.make_one(res)

    def batch_put_data_quality_statistic_annotation(
        self,
        res: "bs_td.BatchPutDataQualityStatisticAnnotationResponseTypeDef",
    ) -> "dc_td.BatchPutDataQualityStatisticAnnotationResponse":
        return dc_td.BatchPutDataQualityStatisticAnnotationResponse.make_one(res)

    def batch_stop_job_run(
        self,
        res: "bs_td.BatchStopJobRunResponseTypeDef",
    ) -> "dc_td.BatchStopJobRunResponse":
        return dc_td.BatchStopJobRunResponse.make_one(res)

    def batch_update_partition(
        self,
        res: "bs_td.BatchUpdatePartitionResponseTypeDef",
    ) -> "dc_td.BatchUpdatePartitionResponse":
        return dc_td.BatchUpdatePartitionResponse.make_one(res)

    def cancel_ml_task_run(
        self,
        res: "bs_td.CancelMLTaskRunResponseTypeDef",
    ) -> "dc_td.CancelMLTaskRunResponse":
        return dc_td.CancelMLTaskRunResponse.make_one(res)

    def check_schema_version_validity(
        self,
        res: "bs_td.CheckSchemaVersionValidityResponseTypeDef",
    ) -> "dc_td.CheckSchemaVersionValidityResponse":
        return dc_td.CheckSchemaVersionValidityResponse.make_one(res)

    def create_blueprint(
        self,
        res: "bs_td.CreateBlueprintResponseTypeDef",
    ) -> "dc_td.CreateBlueprintResponse":
        return dc_td.CreateBlueprintResponse.make_one(res)

    def create_connection(
        self,
        res: "bs_td.CreateConnectionResponseTypeDef",
    ) -> "dc_td.CreateConnectionResponse":
        return dc_td.CreateConnectionResponse.make_one(res)

    def create_custom_entity_type(
        self,
        res: "bs_td.CreateCustomEntityTypeResponseTypeDef",
    ) -> "dc_td.CreateCustomEntityTypeResponse":
        return dc_td.CreateCustomEntityTypeResponse.make_one(res)

    def create_data_quality_ruleset(
        self,
        res: "bs_td.CreateDataQualityRulesetResponseTypeDef",
    ) -> "dc_td.CreateDataQualityRulesetResponse":
        return dc_td.CreateDataQualityRulesetResponse.make_one(res)

    def create_dev_endpoint(
        self,
        res: "bs_td.CreateDevEndpointResponseTypeDef",
    ) -> "dc_td.CreateDevEndpointResponse":
        return dc_td.CreateDevEndpointResponse.make_one(res)

    def create_glue_identity_center_configuration(
        self,
        res: "bs_td.CreateGlueIdentityCenterConfigurationResponseTypeDef",
    ) -> "dc_td.CreateGlueIdentityCenterConfigurationResponse":
        return dc_td.CreateGlueIdentityCenterConfigurationResponse.make_one(res)

    def create_integration(
        self,
        res: "bs_td.CreateIntegrationResponseTypeDef",
    ) -> "dc_td.CreateIntegrationResponse":
        return dc_td.CreateIntegrationResponse.make_one(res)

    def create_integration_resource_property(
        self,
        res: "bs_td.CreateIntegrationResourcePropertyResponseTypeDef",
    ) -> "dc_td.CreateIntegrationResourcePropertyResponse":
        return dc_td.CreateIntegrationResourcePropertyResponse.make_one(res)

    def create_job(
        self,
        res: "bs_td.CreateJobResponseTypeDef",
    ) -> "dc_td.CreateJobResponse":
        return dc_td.CreateJobResponse.make_one(res)

    def create_ml_transform(
        self,
        res: "bs_td.CreateMLTransformResponseTypeDef",
    ) -> "dc_td.CreateMLTransformResponse":
        return dc_td.CreateMLTransformResponse.make_one(res)

    def create_registry(
        self,
        res: "bs_td.CreateRegistryResponseTypeDef",
    ) -> "dc_td.CreateRegistryResponse":
        return dc_td.CreateRegistryResponse.make_one(res)

    def create_schema(
        self,
        res: "bs_td.CreateSchemaResponseTypeDef",
    ) -> "dc_td.CreateSchemaResponse":
        return dc_td.CreateSchemaResponse.make_one(res)

    def create_script(
        self,
        res: "bs_td.CreateScriptResponseTypeDef",
    ) -> "dc_td.CreateScriptResponse":
        return dc_td.CreateScriptResponse.make_one(res)

    def create_security_configuration(
        self,
        res: "bs_td.CreateSecurityConfigurationResponseTypeDef",
    ) -> "dc_td.CreateSecurityConfigurationResponse":
        return dc_td.CreateSecurityConfigurationResponse.make_one(res)

    def create_session(
        self,
        res: "bs_td.CreateSessionResponseTypeDef",
    ) -> "dc_td.CreateSessionResponse":
        return dc_td.CreateSessionResponse.make_one(res)

    def create_trigger(
        self,
        res: "bs_td.CreateTriggerResponseTypeDef",
    ) -> "dc_td.CreateTriggerResponse":
        return dc_td.CreateTriggerResponse.make_one(res)

    def create_usage_profile(
        self,
        res: "bs_td.CreateUsageProfileResponseTypeDef",
    ) -> "dc_td.CreateUsageProfileResponse":
        return dc_td.CreateUsageProfileResponse.make_one(res)

    def create_workflow(
        self,
        res: "bs_td.CreateWorkflowResponseTypeDef",
    ) -> "dc_td.CreateWorkflowResponse":
        return dc_td.CreateWorkflowResponse.make_one(res)

    def delete_blueprint(
        self,
        res: "bs_td.DeleteBlueprintResponseTypeDef",
    ) -> "dc_td.DeleteBlueprintResponse":
        return dc_td.DeleteBlueprintResponse.make_one(res)

    def delete_custom_entity_type(
        self,
        res: "bs_td.DeleteCustomEntityTypeResponseTypeDef",
    ) -> "dc_td.DeleteCustomEntityTypeResponse":
        return dc_td.DeleteCustomEntityTypeResponse.make_one(res)

    def delete_integration(
        self,
        res: "bs_td.DeleteIntegrationResponseTypeDef",
    ) -> "dc_td.DeleteIntegrationResponse":
        return dc_td.DeleteIntegrationResponse.make_one(res)

    def delete_job(
        self,
        res: "bs_td.DeleteJobResponseTypeDef",
    ) -> "dc_td.DeleteJobResponse":
        return dc_td.DeleteJobResponse.make_one(res)

    def delete_ml_transform(
        self,
        res: "bs_td.DeleteMLTransformResponseTypeDef",
    ) -> "dc_td.DeleteMLTransformResponse":
        return dc_td.DeleteMLTransformResponse.make_one(res)

    def delete_registry(
        self,
        res: "bs_td.DeleteRegistryResponseTypeDef",
    ) -> "dc_td.DeleteRegistryResponse":
        return dc_td.DeleteRegistryResponse.make_one(res)

    def delete_schema(
        self,
        res: "bs_td.DeleteSchemaResponseTypeDef",
    ) -> "dc_td.DeleteSchemaResponse":
        return dc_td.DeleteSchemaResponse.make_one(res)

    def delete_schema_versions(
        self,
        res: "bs_td.DeleteSchemaVersionsResponseTypeDef",
    ) -> "dc_td.DeleteSchemaVersionsResponse":
        return dc_td.DeleteSchemaVersionsResponse.make_one(res)

    def delete_session(
        self,
        res: "bs_td.DeleteSessionResponseTypeDef",
    ) -> "dc_td.DeleteSessionResponse":
        return dc_td.DeleteSessionResponse.make_one(res)

    def delete_trigger(
        self,
        res: "bs_td.DeleteTriggerResponseTypeDef",
    ) -> "dc_td.DeleteTriggerResponse":
        return dc_td.DeleteTriggerResponse.make_one(res)

    def delete_workflow(
        self,
        res: "bs_td.DeleteWorkflowResponseTypeDef",
    ) -> "dc_td.DeleteWorkflowResponse":
        return dc_td.DeleteWorkflowResponse.make_one(res)

    def describe_connection_type(
        self,
        res: "bs_td.DescribeConnectionTypeResponseTypeDef",
    ) -> "dc_td.DescribeConnectionTypeResponse":
        return dc_td.DescribeConnectionTypeResponse.make_one(res)

    def describe_entity(
        self,
        res: "bs_td.DescribeEntityResponseTypeDef",
    ) -> "dc_td.DescribeEntityResponse":
        return dc_td.DescribeEntityResponse.make_one(res)

    def describe_inbound_integrations(
        self,
        res: "bs_td.DescribeInboundIntegrationsResponseTypeDef",
    ) -> "dc_td.DescribeInboundIntegrationsResponse":
        return dc_td.DescribeInboundIntegrationsResponse.make_one(res)

    def describe_integrations(
        self,
        res: "bs_td.DescribeIntegrationsResponseTypeDef",
    ) -> "dc_td.DescribeIntegrationsResponse":
        return dc_td.DescribeIntegrationsResponse.make_one(res)

    def get_blueprint(
        self,
        res: "bs_td.GetBlueprintResponseTypeDef",
    ) -> "dc_td.GetBlueprintResponse":
        return dc_td.GetBlueprintResponse.make_one(res)

    def get_blueprint_run(
        self,
        res: "bs_td.GetBlueprintRunResponseTypeDef",
    ) -> "dc_td.GetBlueprintRunResponse":
        return dc_td.GetBlueprintRunResponse.make_one(res)

    def get_blueprint_runs(
        self,
        res: "bs_td.GetBlueprintRunsResponseTypeDef",
    ) -> "dc_td.GetBlueprintRunsResponse":
        return dc_td.GetBlueprintRunsResponse.make_one(res)

    def get_catalog(
        self,
        res: "bs_td.GetCatalogResponseTypeDef",
    ) -> "dc_td.GetCatalogResponse":
        return dc_td.GetCatalogResponse.make_one(res)

    def get_catalog_import_status(
        self,
        res: "bs_td.GetCatalogImportStatusResponseTypeDef",
    ) -> "dc_td.GetCatalogImportStatusResponse":
        return dc_td.GetCatalogImportStatusResponse.make_one(res)

    def get_catalogs(
        self,
        res: "bs_td.GetCatalogsResponseTypeDef",
    ) -> "dc_td.GetCatalogsResponse":
        return dc_td.GetCatalogsResponse.make_one(res)

    def get_classifier(
        self,
        res: "bs_td.GetClassifierResponseTypeDef",
    ) -> "dc_td.GetClassifierResponse":
        return dc_td.GetClassifierResponse.make_one(res)

    def get_classifiers(
        self,
        res: "bs_td.GetClassifiersResponseTypeDef",
    ) -> "dc_td.GetClassifiersResponse":
        return dc_td.GetClassifiersResponse.make_one(res)

    def get_column_statistics_for_partition(
        self,
        res: "bs_td.GetColumnStatisticsForPartitionResponseTypeDef",
    ) -> "dc_td.GetColumnStatisticsForPartitionResponse":
        return dc_td.GetColumnStatisticsForPartitionResponse.make_one(res)

    def get_column_statistics_for_table(
        self,
        res: "bs_td.GetColumnStatisticsForTableResponseTypeDef",
    ) -> "dc_td.GetColumnStatisticsForTableResponse":
        return dc_td.GetColumnStatisticsForTableResponse.make_one(res)

    def get_column_statistics_task_run(
        self,
        res: "bs_td.GetColumnStatisticsTaskRunResponseTypeDef",
    ) -> "dc_td.GetColumnStatisticsTaskRunResponse":
        return dc_td.GetColumnStatisticsTaskRunResponse.make_one(res)

    def get_column_statistics_task_runs(
        self,
        res: "bs_td.GetColumnStatisticsTaskRunsResponseTypeDef",
    ) -> "dc_td.GetColumnStatisticsTaskRunsResponse":
        return dc_td.GetColumnStatisticsTaskRunsResponse.make_one(res)

    def get_column_statistics_task_settings(
        self,
        res: "bs_td.GetColumnStatisticsTaskSettingsResponseTypeDef",
    ) -> "dc_td.GetColumnStatisticsTaskSettingsResponse":
        return dc_td.GetColumnStatisticsTaskSettingsResponse.make_one(res)

    def get_connection(
        self,
        res: "bs_td.GetConnectionResponseTypeDef",
    ) -> "dc_td.GetConnectionResponse":
        return dc_td.GetConnectionResponse.make_one(res)

    def get_connections(
        self,
        res: "bs_td.GetConnectionsResponseTypeDef",
    ) -> "dc_td.GetConnectionsResponse":
        return dc_td.GetConnectionsResponse.make_one(res)

    def get_crawler(
        self,
        res: "bs_td.GetCrawlerResponseTypeDef",
    ) -> "dc_td.GetCrawlerResponse":
        return dc_td.GetCrawlerResponse.make_one(res)

    def get_crawler_metrics(
        self,
        res: "bs_td.GetCrawlerMetricsResponseTypeDef",
    ) -> "dc_td.GetCrawlerMetricsResponse":
        return dc_td.GetCrawlerMetricsResponse.make_one(res)

    def get_crawlers(
        self,
        res: "bs_td.GetCrawlersResponseTypeDef",
    ) -> "dc_td.GetCrawlersResponse":
        return dc_td.GetCrawlersResponse.make_one(res)

    def get_custom_entity_type(
        self,
        res: "bs_td.GetCustomEntityTypeResponseTypeDef",
    ) -> "dc_td.GetCustomEntityTypeResponse":
        return dc_td.GetCustomEntityTypeResponse.make_one(res)

    def get_data_catalog_encryption_settings(
        self,
        res: "bs_td.GetDataCatalogEncryptionSettingsResponseTypeDef",
    ) -> "dc_td.GetDataCatalogEncryptionSettingsResponse":
        return dc_td.GetDataCatalogEncryptionSettingsResponse.make_one(res)

    def get_data_quality_model(
        self,
        res: "bs_td.GetDataQualityModelResponseTypeDef",
    ) -> "dc_td.GetDataQualityModelResponse":
        return dc_td.GetDataQualityModelResponse.make_one(res)

    def get_data_quality_model_result(
        self,
        res: "bs_td.GetDataQualityModelResultResponseTypeDef",
    ) -> "dc_td.GetDataQualityModelResultResponse":
        return dc_td.GetDataQualityModelResultResponse.make_one(res)

    def get_data_quality_result(
        self,
        res: "bs_td.GetDataQualityResultResponseTypeDef",
    ) -> "dc_td.GetDataQualityResultResponse":
        return dc_td.GetDataQualityResultResponse.make_one(res)

    def get_data_quality_rule_recommendation_run(
        self,
        res: "bs_td.GetDataQualityRuleRecommendationRunResponseTypeDef",
    ) -> "dc_td.GetDataQualityRuleRecommendationRunResponse":
        return dc_td.GetDataQualityRuleRecommendationRunResponse.make_one(res)

    def get_data_quality_ruleset(
        self,
        res: "bs_td.GetDataQualityRulesetResponseTypeDef",
    ) -> "dc_td.GetDataQualityRulesetResponse":
        return dc_td.GetDataQualityRulesetResponse.make_one(res)

    def get_data_quality_ruleset_evaluation_run(
        self,
        res: "bs_td.GetDataQualityRulesetEvaluationRunResponseTypeDef",
    ) -> "dc_td.GetDataQualityRulesetEvaluationRunResponse":
        return dc_td.GetDataQualityRulesetEvaluationRunResponse.make_one(res)

    def get_database(
        self,
        res: "bs_td.GetDatabaseResponseTypeDef",
    ) -> "dc_td.GetDatabaseResponse":
        return dc_td.GetDatabaseResponse.make_one(res)

    def get_databases(
        self,
        res: "bs_td.GetDatabasesResponseTypeDef",
    ) -> "dc_td.GetDatabasesResponse":
        return dc_td.GetDatabasesResponse.make_one(res)

    def get_dataflow_graph(
        self,
        res: "bs_td.GetDataflowGraphResponseTypeDef",
    ) -> "dc_td.GetDataflowGraphResponse":
        return dc_td.GetDataflowGraphResponse.make_one(res)

    def get_dev_endpoint(
        self,
        res: "bs_td.GetDevEndpointResponseTypeDef",
    ) -> "dc_td.GetDevEndpointResponse":
        return dc_td.GetDevEndpointResponse.make_one(res)

    def get_dev_endpoints(
        self,
        res: "bs_td.GetDevEndpointsResponseTypeDef",
    ) -> "dc_td.GetDevEndpointsResponse":
        return dc_td.GetDevEndpointsResponse.make_one(res)

    def get_entity_records(
        self,
        res: "bs_td.GetEntityRecordsResponseTypeDef",
    ) -> "dc_td.GetEntityRecordsResponse":
        return dc_td.GetEntityRecordsResponse.make_one(res)

    def get_glue_identity_center_configuration(
        self,
        res: "bs_td.GetGlueIdentityCenterConfigurationResponseTypeDef",
    ) -> "dc_td.GetGlueIdentityCenterConfigurationResponse":
        return dc_td.GetGlueIdentityCenterConfigurationResponse.make_one(res)

    def get_integration_resource_property(
        self,
        res: "bs_td.GetIntegrationResourcePropertyResponseTypeDef",
    ) -> "dc_td.GetIntegrationResourcePropertyResponse":
        return dc_td.GetIntegrationResourcePropertyResponse.make_one(res)

    def get_integration_table_properties(
        self,
        res: "bs_td.GetIntegrationTablePropertiesResponseTypeDef",
    ) -> "dc_td.GetIntegrationTablePropertiesResponse":
        return dc_td.GetIntegrationTablePropertiesResponse.make_one(res)

    def get_job(
        self,
        res: "bs_td.GetJobResponseTypeDef",
    ) -> "dc_td.GetJobResponse":
        return dc_td.GetJobResponse.make_one(res)

    def get_job_bookmark(
        self,
        res: "bs_td.GetJobBookmarkResponseTypeDef",
    ) -> "dc_td.GetJobBookmarkResponse":
        return dc_td.GetJobBookmarkResponse.make_one(res)

    def get_job_run(
        self,
        res: "bs_td.GetJobRunResponseTypeDef",
    ) -> "dc_td.GetJobRunResponse":
        return dc_td.GetJobRunResponse.make_one(res)

    def get_job_runs(
        self,
        res: "bs_td.GetJobRunsResponseTypeDef",
    ) -> "dc_td.GetJobRunsResponse":
        return dc_td.GetJobRunsResponse.make_one(res)

    def get_jobs(
        self,
        res: "bs_td.GetJobsResponseTypeDef",
    ) -> "dc_td.GetJobsResponse":
        return dc_td.GetJobsResponse.make_one(res)

    def get_ml_task_run(
        self,
        res: "bs_td.GetMLTaskRunResponseTypeDef",
    ) -> "dc_td.GetMLTaskRunResponse":
        return dc_td.GetMLTaskRunResponse.make_one(res)

    def get_ml_task_runs(
        self,
        res: "bs_td.GetMLTaskRunsResponseTypeDef",
    ) -> "dc_td.GetMLTaskRunsResponse":
        return dc_td.GetMLTaskRunsResponse.make_one(res)

    def get_ml_transform(
        self,
        res: "bs_td.GetMLTransformResponseTypeDef",
    ) -> "dc_td.GetMLTransformResponse":
        return dc_td.GetMLTransformResponse.make_one(res)

    def get_ml_transforms(
        self,
        res: "bs_td.GetMLTransformsResponseTypeDef",
    ) -> "dc_td.GetMLTransformsResponse":
        return dc_td.GetMLTransformsResponse.make_one(res)

    def get_mapping(
        self,
        res: "bs_td.GetMappingResponseTypeDef",
    ) -> "dc_td.GetMappingResponse":
        return dc_td.GetMappingResponse.make_one(res)

    def get_partition(
        self,
        res: "bs_td.GetPartitionResponseTypeDef",
    ) -> "dc_td.GetPartitionResponse":
        return dc_td.GetPartitionResponse.make_one(res)

    def get_partition_indexes(
        self,
        res: "bs_td.GetPartitionIndexesResponseTypeDef",
    ) -> "dc_td.GetPartitionIndexesResponse":
        return dc_td.GetPartitionIndexesResponse.make_one(res)

    def get_partitions(
        self,
        res: "bs_td.GetPartitionsResponseTypeDef",
    ) -> "dc_td.GetPartitionsResponse":
        return dc_td.GetPartitionsResponse.make_one(res)

    def get_plan(
        self,
        res: "bs_td.GetPlanResponseTypeDef",
    ) -> "dc_td.GetPlanResponse":
        return dc_td.GetPlanResponse.make_one(res)

    def get_registry(
        self,
        res: "bs_td.GetRegistryResponseTypeDef",
    ) -> "dc_td.GetRegistryResponse":
        return dc_td.GetRegistryResponse.make_one(res)

    def get_resource_policies(
        self,
        res: "bs_td.GetResourcePoliciesResponseTypeDef",
    ) -> "dc_td.GetResourcePoliciesResponse":
        return dc_td.GetResourcePoliciesResponse.make_one(res)

    def get_resource_policy(
        self,
        res: "bs_td.GetResourcePolicyResponseTypeDef",
    ) -> "dc_td.GetResourcePolicyResponse":
        return dc_td.GetResourcePolicyResponse.make_one(res)

    def get_schema(
        self,
        res: "bs_td.GetSchemaResponseTypeDef",
    ) -> "dc_td.GetSchemaResponse":
        return dc_td.GetSchemaResponse.make_one(res)

    def get_schema_by_definition(
        self,
        res: "bs_td.GetSchemaByDefinitionResponseTypeDef",
    ) -> "dc_td.GetSchemaByDefinitionResponse":
        return dc_td.GetSchemaByDefinitionResponse.make_one(res)

    def get_schema_version(
        self,
        res: "bs_td.GetSchemaVersionResponseTypeDef",
    ) -> "dc_td.GetSchemaVersionResponse":
        return dc_td.GetSchemaVersionResponse.make_one(res)

    def get_schema_versions_diff(
        self,
        res: "bs_td.GetSchemaVersionsDiffResponseTypeDef",
    ) -> "dc_td.GetSchemaVersionsDiffResponse":
        return dc_td.GetSchemaVersionsDiffResponse.make_one(res)

    def get_security_configuration(
        self,
        res: "bs_td.GetSecurityConfigurationResponseTypeDef",
    ) -> "dc_td.GetSecurityConfigurationResponse":
        return dc_td.GetSecurityConfigurationResponse.make_one(res)

    def get_security_configurations(
        self,
        res: "bs_td.GetSecurityConfigurationsResponseTypeDef",
    ) -> "dc_td.GetSecurityConfigurationsResponse":
        return dc_td.GetSecurityConfigurationsResponse.make_one(res)

    def get_session(
        self,
        res: "bs_td.GetSessionResponseTypeDef",
    ) -> "dc_td.GetSessionResponse":
        return dc_td.GetSessionResponse.make_one(res)

    def get_statement(
        self,
        res: "bs_td.GetStatementResponseTypeDef",
    ) -> "dc_td.GetStatementResponse":
        return dc_td.GetStatementResponse.make_one(res)

    def get_table(
        self,
        res: "bs_td.GetTableResponseTypeDef",
    ) -> "dc_td.GetTableResponse":
        return dc_td.GetTableResponse.make_one(res)

    def get_table_optimizer(
        self,
        res: "bs_td.GetTableOptimizerResponseTypeDef",
    ) -> "dc_td.GetTableOptimizerResponse":
        return dc_td.GetTableOptimizerResponse.make_one(res)

    def get_table_version(
        self,
        res: "bs_td.GetTableVersionResponseTypeDef",
    ) -> "dc_td.GetTableVersionResponse":
        return dc_td.GetTableVersionResponse.make_one(res)

    def get_table_versions(
        self,
        res: "bs_td.GetTableVersionsResponseTypeDef",
    ) -> "dc_td.GetTableVersionsResponse":
        return dc_td.GetTableVersionsResponse.make_one(res)

    def get_tables(
        self,
        res: "bs_td.GetTablesResponseTypeDef",
    ) -> "dc_td.GetTablesResponse":
        return dc_td.GetTablesResponse.make_one(res)

    def get_tags(
        self,
        res: "bs_td.GetTagsResponseTypeDef",
    ) -> "dc_td.GetTagsResponse":
        return dc_td.GetTagsResponse.make_one(res)

    def get_trigger(
        self,
        res: "bs_td.GetTriggerResponseTypeDef",
    ) -> "dc_td.GetTriggerResponse":
        return dc_td.GetTriggerResponse.make_one(res)

    def get_triggers(
        self,
        res: "bs_td.GetTriggersResponseTypeDef",
    ) -> "dc_td.GetTriggersResponse":
        return dc_td.GetTriggersResponse.make_one(res)

    def get_unfiltered_partition_metadata(
        self,
        res: "bs_td.GetUnfilteredPartitionMetadataResponseTypeDef",
    ) -> "dc_td.GetUnfilteredPartitionMetadataResponse":
        return dc_td.GetUnfilteredPartitionMetadataResponse.make_one(res)

    def get_unfiltered_partitions_metadata(
        self,
        res: "bs_td.GetUnfilteredPartitionsMetadataResponseTypeDef",
    ) -> "dc_td.GetUnfilteredPartitionsMetadataResponse":
        return dc_td.GetUnfilteredPartitionsMetadataResponse.make_one(res)

    def get_unfiltered_table_metadata(
        self,
        res: "bs_td.GetUnfilteredTableMetadataResponseTypeDef",
    ) -> "dc_td.GetUnfilteredTableMetadataResponse":
        return dc_td.GetUnfilteredTableMetadataResponse.make_one(res)

    def get_usage_profile(
        self,
        res: "bs_td.GetUsageProfileResponseTypeDef",
    ) -> "dc_td.GetUsageProfileResponse":
        return dc_td.GetUsageProfileResponse.make_one(res)

    def get_user_defined_function(
        self,
        res: "bs_td.GetUserDefinedFunctionResponseTypeDef",
    ) -> "dc_td.GetUserDefinedFunctionResponse":
        return dc_td.GetUserDefinedFunctionResponse.make_one(res)

    def get_user_defined_functions(
        self,
        res: "bs_td.GetUserDefinedFunctionsResponseTypeDef",
    ) -> "dc_td.GetUserDefinedFunctionsResponse":
        return dc_td.GetUserDefinedFunctionsResponse.make_one(res)

    def get_workflow(
        self,
        res: "bs_td.GetWorkflowResponseTypeDef",
    ) -> "dc_td.GetWorkflowResponse":
        return dc_td.GetWorkflowResponse.make_one(res)

    def get_workflow_run(
        self,
        res: "bs_td.GetWorkflowRunResponseTypeDef",
    ) -> "dc_td.GetWorkflowRunResponse":
        return dc_td.GetWorkflowRunResponse.make_one(res)

    def get_workflow_run_properties(
        self,
        res: "bs_td.GetWorkflowRunPropertiesResponseTypeDef",
    ) -> "dc_td.GetWorkflowRunPropertiesResponse":
        return dc_td.GetWorkflowRunPropertiesResponse.make_one(res)

    def get_workflow_runs(
        self,
        res: "bs_td.GetWorkflowRunsResponseTypeDef",
    ) -> "dc_td.GetWorkflowRunsResponse":
        return dc_td.GetWorkflowRunsResponse.make_one(res)

    def list_blueprints(
        self,
        res: "bs_td.ListBlueprintsResponseTypeDef",
    ) -> "dc_td.ListBlueprintsResponse":
        return dc_td.ListBlueprintsResponse.make_one(res)

    def list_column_statistics_task_runs(
        self,
        res: "bs_td.ListColumnStatisticsTaskRunsResponseTypeDef",
    ) -> "dc_td.ListColumnStatisticsTaskRunsResponse":
        return dc_td.ListColumnStatisticsTaskRunsResponse.make_one(res)

    def list_connection_types(
        self,
        res: "bs_td.ListConnectionTypesResponseTypeDef",
    ) -> "dc_td.ListConnectionTypesResponse":
        return dc_td.ListConnectionTypesResponse.make_one(res)

    def list_crawlers(
        self,
        res: "bs_td.ListCrawlersResponseTypeDef",
    ) -> "dc_td.ListCrawlersResponse":
        return dc_td.ListCrawlersResponse.make_one(res)

    def list_crawls(
        self,
        res: "bs_td.ListCrawlsResponseTypeDef",
    ) -> "dc_td.ListCrawlsResponse":
        return dc_td.ListCrawlsResponse.make_one(res)

    def list_custom_entity_types(
        self,
        res: "bs_td.ListCustomEntityTypesResponseTypeDef",
    ) -> "dc_td.ListCustomEntityTypesResponse":
        return dc_td.ListCustomEntityTypesResponse.make_one(res)

    def list_data_quality_results(
        self,
        res: "bs_td.ListDataQualityResultsResponseTypeDef",
    ) -> "dc_td.ListDataQualityResultsResponse":
        return dc_td.ListDataQualityResultsResponse.make_one(res)

    def list_data_quality_rule_recommendation_runs(
        self,
        res: "bs_td.ListDataQualityRuleRecommendationRunsResponseTypeDef",
    ) -> "dc_td.ListDataQualityRuleRecommendationRunsResponse":
        return dc_td.ListDataQualityRuleRecommendationRunsResponse.make_one(res)

    def list_data_quality_ruleset_evaluation_runs(
        self,
        res: "bs_td.ListDataQualityRulesetEvaluationRunsResponseTypeDef",
    ) -> "dc_td.ListDataQualityRulesetEvaluationRunsResponse":
        return dc_td.ListDataQualityRulesetEvaluationRunsResponse.make_one(res)

    def list_data_quality_rulesets(
        self,
        res: "bs_td.ListDataQualityRulesetsResponseTypeDef",
    ) -> "dc_td.ListDataQualityRulesetsResponse":
        return dc_td.ListDataQualityRulesetsResponse.make_one(res)

    def list_data_quality_statistic_annotations(
        self,
        res: "bs_td.ListDataQualityStatisticAnnotationsResponseTypeDef",
    ) -> "dc_td.ListDataQualityStatisticAnnotationsResponse":
        return dc_td.ListDataQualityStatisticAnnotationsResponse.make_one(res)

    def list_data_quality_statistics(
        self,
        res: "bs_td.ListDataQualityStatisticsResponseTypeDef",
    ) -> "dc_td.ListDataQualityStatisticsResponse":
        return dc_td.ListDataQualityStatisticsResponse.make_one(res)

    def list_dev_endpoints(
        self,
        res: "bs_td.ListDevEndpointsResponseTypeDef",
    ) -> "dc_td.ListDevEndpointsResponse":
        return dc_td.ListDevEndpointsResponse.make_one(res)

    def list_entities(
        self,
        res: "bs_td.ListEntitiesResponseTypeDef",
    ) -> "dc_td.ListEntitiesResponse":
        return dc_td.ListEntitiesResponse.make_one(res)

    def list_jobs(
        self,
        res: "bs_td.ListJobsResponseTypeDef",
    ) -> "dc_td.ListJobsResponse":
        return dc_td.ListJobsResponse.make_one(res)

    def list_ml_transforms(
        self,
        res: "bs_td.ListMLTransformsResponseTypeDef",
    ) -> "dc_td.ListMLTransformsResponse":
        return dc_td.ListMLTransformsResponse.make_one(res)

    def list_registries(
        self,
        res: "bs_td.ListRegistriesResponseTypeDef",
    ) -> "dc_td.ListRegistriesResponse":
        return dc_td.ListRegistriesResponse.make_one(res)

    def list_schema_versions(
        self,
        res: "bs_td.ListSchemaVersionsResponseTypeDef",
    ) -> "dc_td.ListSchemaVersionsResponse":
        return dc_td.ListSchemaVersionsResponse.make_one(res)

    def list_schemas(
        self,
        res: "bs_td.ListSchemasResponseTypeDef",
    ) -> "dc_td.ListSchemasResponse":
        return dc_td.ListSchemasResponse.make_one(res)

    def list_sessions(
        self,
        res: "bs_td.ListSessionsResponseTypeDef",
    ) -> "dc_td.ListSessionsResponse":
        return dc_td.ListSessionsResponse.make_one(res)

    def list_statements(
        self,
        res: "bs_td.ListStatementsResponseTypeDef",
    ) -> "dc_td.ListStatementsResponse":
        return dc_td.ListStatementsResponse.make_one(res)

    def list_table_optimizer_runs(
        self,
        res: "bs_td.ListTableOptimizerRunsResponseTypeDef",
    ) -> "dc_td.ListTableOptimizerRunsResponse":
        return dc_td.ListTableOptimizerRunsResponse.make_one(res)

    def list_triggers(
        self,
        res: "bs_td.ListTriggersResponseTypeDef",
    ) -> "dc_td.ListTriggersResponse":
        return dc_td.ListTriggersResponse.make_one(res)

    def list_usage_profiles(
        self,
        res: "bs_td.ListUsageProfilesResponseTypeDef",
    ) -> "dc_td.ListUsageProfilesResponse":
        return dc_td.ListUsageProfilesResponse.make_one(res)

    def list_workflows(
        self,
        res: "bs_td.ListWorkflowsResponseTypeDef",
    ) -> "dc_td.ListWorkflowsResponse":
        return dc_td.ListWorkflowsResponse.make_one(res)

    def modify_integration(
        self,
        res: "bs_td.ModifyIntegrationResponseTypeDef",
    ) -> "dc_td.ModifyIntegrationResponse":
        return dc_td.ModifyIntegrationResponse.make_one(res)

    def put_resource_policy(
        self,
        res: "bs_td.PutResourcePolicyResponseTypeDef",
    ) -> "dc_td.PutResourcePolicyResponse":
        return dc_td.PutResourcePolicyResponse.make_one(res)

    def put_schema_version_metadata(
        self,
        res: "bs_td.PutSchemaVersionMetadataResponseTypeDef",
    ) -> "dc_td.PutSchemaVersionMetadataResponse":
        return dc_td.PutSchemaVersionMetadataResponse.make_one(res)

    def query_schema_version_metadata(
        self,
        res: "bs_td.QuerySchemaVersionMetadataResponseTypeDef",
    ) -> "dc_td.QuerySchemaVersionMetadataResponse":
        return dc_td.QuerySchemaVersionMetadataResponse.make_one(res)

    def register_schema_version(
        self,
        res: "bs_td.RegisterSchemaVersionResponseTypeDef",
    ) -> "dc_td.RegisterSchemaVersionResponse":
        return dc_td.RegisterSchemaVersionResponse.make_one(res)

    def remove_schema_version_metadata(
        self,
        res: "bs_td.RemoveSchemaVersionMetadataResponseTypeDef",
    ) -> "dc_td.RemoveSchemaVersionMetadataResponse":
        return dc_td.RemoveSchemaVersionMetadataResponse.make_one(res)

    def reset_job_bookmark(
        self,
        res: "bs_td.ResetJobBookmarkResponseTypeDef",
    ) -> "dc_td.ResetJobBookmarkResponse":
        return dc_td.ResetJobBookmarkResponse.make_one(res)

    def resume_workflow_run(
        self,
        res: "bs_td.ResumeWorkflowRunResponseTypeDef",
    ) -> "dc_td.ResumeWorkflowRunResponse":
        return dc_td.ResumeWorkflowRunResponse.make_one(res)

    def run_statement(
        self,
        res: "bs_td.RunStatementResponseTypeDef",
    ) -> "dc_td.RunStatementResponse":
        return dc_td.RunStatementResponse.make_one(res)

    def search_tables(
        self,
        res: "bs_td.SearchTablesResponseTypeDef",
    ) -> "dc_td.SearchTablesResponse":
        return dc_td.SearchTablesResponse.make_one(res)

    def start_blueprint_run(
        self,
        res: "bs_td.StartBlueprintRunResponseTypeDef",
    ) -> "dc_td.StartBlueprintRunResponse":
        return dc_td.StartBlueprintRunResponse.make_one(res)

    def start_column_statistics_task_run(
        self,
        res: "bs_td.StartColumnStatisticsTaskRunResponseTypeDef",
    ) -> "dc_td.StartColumnStatisticsTaskRunResponse":
        return dc_td.StartColumnStatisticsTaskRunResponse.make_one(res)

    def start_data_quality_rule_recommendation_run(
        self,
        res: "bs_td.StartDataQualityRuleRecommendationRunResponseTypeDef",
    ) -> "dc_td.StartDataQualityRuleRecommendationRunResponse":
        return dc_td.StartDataQualityRuleRecommendationRunResponse.make_one(res)

    def start_data_quality_ruleset_evaluation_run(
        self,
        res: "bs_td.StartDataQualityRulesetEvaluationRunResponseTypeDef",
    ) -> "dc_td.StartDataQualityRulesetEvaluationRunResponse":
        return dc_td.StartDataQualityRulesetEvaluationRunResponse.make_one(res)

    def start_export_labels_task_run(
        self,
        res: "bs_td.StartExportLabelsTaskRunResponseTypeDef",
    ) -> "dc_td.StartExportLabelsTaskRunResponse":
        return dc_td.StartExportLabelsTaskRunResponse.make_one(res)

    def start_import_labels_task_run(
        self,
        res: "bs_td.StartImportLabelsTaskRunResponseTypeDef",
    ) -> "dc_td.StartImportLabelsTaskRunResponse":
        return dc_td.StartImportLabelsTaskRunResponse.make_one(res)

    def start_job_run(
        self,
        res: "bs_td.StartJobRunResponseTypeDef",
    ) -> "dc_td.StartJobRunResponse":
        return dc_td.StartJobRunResponse.make_one(res)

    def start_ml_evaluation_task_run(
        self,
        res: "bs_td.StartMLEvaluationTaskRunResponseTypeDef",
    ) -> "dc_td.StartMLEvaluationTaskRunResponse":
        return dc_td.StartMLEvaluationTaskRunResponse.make_one(res)

    def start_ml_labeling_set_generation_task_run(
        self,
        res: "bs_td.StartMLLabelingSetGenerationTaskRunResponseTypeDef",
    ) -> "dc_td.StartMLLabelingSetGenerationTaskRunResponse":
        return dc_td.StartMLLabelingSetGenerationTaskRunResponse.make_one(res)

    def start_trigger(
        self,
        res: "bs_td.StartTriggerResponseTypeDef",
    ) -> "dc_td.StartTriggerResponse":
        return dc_td.StartTriggerResponse.make_one(res)

    def start_workflow_run(
        self,
        res: "bs_td.StartWorkflowRunResponseTypeDef",
    ) -> "dc_td.StartWorkflowRunResponse":
        return dc_td.StartWorkflowRunResponse.make_one(res)

    def stop_session(
        self,
        res: "bs_td.StopSessionResponseTypeDef",
    ) -> "dc_td.StopSessionResponse":
        return dc_td.StopSessionResponse.make_one(res)

    def stop_trigger(
        self,
        res: "bs_td.StopTriggerResponseTypeDef",
    ) -> "dc_td.StopTriggerResponse":
        return dc_td.StopTriggerResponse.make_one(res)

    def update_blueprint(
        self,
        res: "bs_td.UpdateBlueprintResponseTypeDef",
    ) -> "dc_td.UpdateBlueprintResponse":
        return dc_td.UpdateBlueprintResponse.make_one(res)

    def update_column_statistics_for_partition(
        self,
        res: "bs_td.UpdateColumnStatisticsForPartitionResponseTypeDef",
    ) -> "dc_td.UpdateColumnStatisticsForPartitionResponse":
        return dc_td.UpdateColumnStatisticsForPartitionResponse.make_one(res)

    def update_column_statistics_for_table(
        self,
        res: "bs_td.UpdateColumnStatisticsForTableResponseTypeDef",
    ) -> "dc_td.UpdateColumnStatisticsForTableResponse":
        return dc_td.UpdateColumnStatisticsForTableResponse.make_one(res)

    def update_data_quality_ruleset(
        self,
        res: "bs_td.UpdateDataQualityRulesetResponseTypeDef",
    ) -> "dc_td.UpdateDataQualityRulesetResponse":
        return dc_td.UpdateDataQualityRulesetResponse.make_one(res)

    def update_integration_resource_property(
        self,
        res: "bs_td.UpdateIntegrationResourcePropertyResponseTypeDef",
    ) -> "dc_td.UpdateIntegrationResourcePropertyResponse":
        return dc_td.UpdateIntegrationResourcePropertyResponse.make_one(res)

    def update_job(
        self,
        res: "bs_td.UpdateJobResponseTypeDef",
    ) -> "dc_td.UpdateJobResponse":
        return dc_td.UpdateJobResponse.make_one(res)

    def update_job_from_source_control(
        self,
        res: "bs_td.UpdateJobFromSourceControlResponseTypeDef",
    ) -> "dc_td.UpdateJobFromSourceControlResponse":
        return dc_td.UpdateJobFromSourceControlResponse.make_one(res)

    def update_ml_transform(
        self,
        res: "bs_td.UpdateMLTransformResponseTypeDef",
    ) -> "dc_td.UpdateMLTransformResponse":
        return dc_td.UpdateMLTransformResponse.make_one(res)

    def update_registry(
        self,
        res: "bs_td.UpdateRegistryResponseTypeDef",
    ) -> "dc_td.UpdateRegistryResponse":
        return dc_td.UpdateRegistryResponse.make_one(res)

    def update_schema(
        self,
        res: "bs_td.UpdateSchemaResponseTypeDef",
    ) -> "dc_td.UpdateSchemaResponse":
        return dc_td.UpdateSchemaResponse.make_one(res)

    def update_source_control_from_job(
        self,
        res: "bs_td.UpdateSourceControlFromJobResponseTypeDef",
    ) -> "dc_td.UpdateSourceControlFromJobResponse":
        return dc_td.UpdateSourceControlFromJobResponse.make_one(res)

    def update_trigger(
        self,
        res: "bs_td.UpdateTriggerResponseTypeDef",
    ) -> "dc_td.UpdateTriggerResponse":
        return dc_td.UpdateTriggerResponse.make_one(res)

    def update_usage_profile(
        self,
        res: "bs_td.UpdateUsageProfileResponseTypeDef",
    ) -> "dc_td.UpdateUsageProfileResponse":
        return dc_td.UpdateUsageProfileResponse.make_one(res)

    def update_workflow(
        self,
        res: "bs_td.UpdateWorkflowResponseTypeDef",
    ) -> "dc_td.UpdateWorkflowResponse":
        return dc_td.UpdateWorkflowResponse.make_one(res)


glue_caster = GLUECaster()
