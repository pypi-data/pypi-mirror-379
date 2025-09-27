# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_logs import type_defs as bs_td


class LOGSCaster:

    def associate_kms_key(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def cancel_export_task(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_delivery(
        self,
        res: "bs_td.CreateDeliveryResponseTypeDef",
    ) -> "dc_td.CreateDeliveryResponse":
        return dc_td.CreateDeliveryResponse.make_one(res)

    def create_export_task(
        self,
        res: "bs_td.CreateExportTaskResponseTypeDef",
    ) -> "dc_td.CreateExportTaskResponse":
        return dc_td.CreateExportTaskResponse.make_one(res)

    def create_log_anomaly_detector(
        self,
        res: "bs_td.CreateLogAnomalyDetectorResponseTypeDef",
    ) -> "dc_td.CreateLogAnomalyDetectorResponse":
        return dc_td.CreateLogAnomalyDetectorResponse.make_one(res)

    def create_log_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_log_stream(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_account_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_data_protection_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_delivery(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_delivery_destination(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_delivery_destination_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_delivery_source(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_destination(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_log_anomaly_detector(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_log_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_log_stream(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_metric_filter(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_query_definition(
        self,
        res: "bs_td.DeleteQueryDefinitionResponseTypeDef",
    ) -> "dc_td.DeleteQueryDefinitionResponse":
        return dc_td.DeleteQueryDefinitionResponse.make_one(res)

    def delete_resource_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_retention_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_subscription_filter(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_transformer(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_account_policies(
        self,
        res: "bs_td.DescribeAccountPoliciesResponseTypeDef",
    ) -> "dc_td.DescribeAccountPoliciesResponse":
        return dc_td.DescribeAccountPoliciesResponse.make_one(res)

    def describe_configuration_templates(
        self,
        res: "bs_td.DescribeConfigurationTemplatesResponseTypeDef",
    ) -> "dc_td.DescribeConfigurationTemplatesResponse":
        return dc_td.DescribeConfigurationTemplatesResponse.make_one(res)

    def describe_deliveries(
        self,
        res: "bs_td.DescribeDeliveriesResponseTypeDef",
    ) -> "dc_td.DescribeDeliveriesResponse":
        return dc_td.DescribeDeliveriesResponse.make_one(res)

    def describe_delivery_destinations(
        self,
        res: "bs_td.DescribeDeliveryDestinationsResponseTypeDef",
    ) -> "dc_td.DescribeDeliveryDestinationsResponse":
        return dc_td.DescribeDeliveryDestinationsResponse.make_one(res)

    def describe_delivery_sources(
        self,
        res: "bs_td.DescribeDeliverySourcesResponseTypeDef",
    ) -> "dc_td.DescribeDeliverySourcesResponse":
        return dc_td.DescribeDeliverySourcesResponse.make_one(res)

    def describe_destinations(
        self,
        res: "bs_td.DescribeDestinationsResponseTypeDef",
    ) -> "dc_td.DescribeDestinationsResponse":
        return dc_td.DescribeDestinationsResponse.make_one(res)

    def describe_export_tasks(
        self,
        res: "bs_td.DescribeExportTasksResponseTypeDef",
    ) -> "dc_td.DescribeExportTasksResponse":
        return dc_td.DescribeExportTasksResponse.make_one(res)

    def describe_field_indexes(
        self,
        res: "bs_td.DescribeFieldIndexesResponseTypeDef",
    ) -> "dc_td.DescribeFieldIndexesResponse":
        return dc_td.DescribeFieldIndexesResponse.make_one(res)

    def describe_index_policies(
        self,
        res: "bs_td.DescribeIndexPoliciesResponseTypeDef",
    ) -> "dc_td.DescribeIndexPoliciesResponse":
        return dc_td.DescribeIndexPoliciesResponse.make_one(res)

    def describe_log_groups(
        self,
        res: "bs_td.DescribeLogGroupsResponseTypeDef",
    ) -> "dc_td.DescribeLogGroupsResponse":
        return dc_td.DescribeLogGroupsResponse.make_one(res)

    def describe_log_streams(
        self,
        res: "bs_td.DescribeLogStreamsResponseTypeDef",
    ) -> "dc_td.DescribeLogStreamsResponse":
        return dc_td.DescribeLogStreamsResponse.make_one(res)

    def describe_metric_filters(
        self,
        res: "bs_td.DescribeMetricFiltersResponseTypeDef",
    ) -> "dc_td.DescribeMetricFiltersResponse":
        return dc_td.DescribeMetricFiltersResponse.make_one(res)

    def describe_queries(
        self,
        res: "bs_td.DescribeQueriesResponseTypeDef",
    ) -> "dc_td.DescribeQueriesResponse":
        return dc_td.DescribeQueriesResponse.make_one(res)

    def describe_query_definitions(
        self,
        res: "bs_td.DescribeQueryDefinitionsResponseTypeDef",
    ) -> "dc_td.DescribeQueryDefinitionsResponse":
        return dc_td.DescribeQueryDefinitionsResponse.make_one(res)

    def describe_resource_policies(
        self,
        res: "bs_td.DescribeResourcePoliciesResponseTypeDef",
    ) -> "dc_td.DescribeResourcePoliciesResponse":
        return dc_td.DescribeResourcePoliciesResponse.make_one(res)

    def describe_subscription_filters(
        self,
        res: "bs_td.DescribeSubscriptionFiltersResponseTypeDef",
    ) -> "dc_td.DescribeSubscriptionFiltersResponse":
        return dc_td.DescribeSubscriptionFiltersResponse.make_one(res)

    def disassociate_kms_key(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def filter_log_events(
        self,
        res: "bs_td.FilterLogEventsResponseTypeDef",
    ) -> "dc_td.FilterLogEventsResponse":
        return dc_td.FilterLogEventsResponse.make_one(res)

    def get_data_protection_policy(
        self,
        res: "bs_td.GetDataProtectionPolicyResponseTypeDef",
    ) -> "dc_td.GetDataProtectionPolicyResponse":
        return dc_td.GetDataProtectionPolicyResponse.make_one(res)

    def get_delivery(
        self,
        res: "bs_td.GetDeliveryResponseTypeDef",
    ) -> "dc_td.GetDeliveryResponse":
        return dc_td.GetDeliveryResponse.make_one(res)

    def get_delivery_destination(
        self,
        res: "bs_td.GetDeliveryDestinationResponseTypeDef",
    ) -> "dc_td.GetDeliveryDestinationResponse":
        return dc_td.GetDeliveryDestinationResponse.make_one(res)

    def get_delivery_destination_policy(
        self,
        res: "bs_td.GetDeliveryDestinationPolicyResponseTypeDef",
    ) -> "dc_td.GetDeliveryDestinationPolicyResponse":
        return dc_td.GetDeliveryDestinationPolicyResponse.make_one(res)

    def get_delivery_source(
        self,
        res: "bs_td.GetDeliverySourceResponseTypeDef",
    ) -> "dc_td.GetDeliverySourceResponse":
        return dc_td.GetDeliverySourceResponse.make_one(res)

    def get_integration(
        self,
        res: "bs_td.GetIntegrationResponseTypeDef",
    ) -> "dc_td.GetIntegrationResponse":
        return dc_td.GetIntegrationResponse.make_one(res)

    def get_log_anomaly_detector(
        self,
        res: "bs_td.GetLogAnomalyDetectorResponseTypeDef",
    ) -> "dc_td.GetLogAnomalyDetectorResponse":
        return dc_td.GetLogAnomalyDetectorResponse.make_one(res)

    def get_log_events(
        self,
        res: "bs_td.GetLogEventsResponseTypeDef",
    ) -> "dc_td.GetLogEventsResponse":
        return dc_td.GetLogEventsResponse.make_one(res)

    def get_log_group_fields(
        self,
        res: "bs_td.GetLogGroupFieldsResponseTypeDef",
    ) -> "dc_td.GetLogGroupFieldsResponse":
        return dc_td.GetLogGroupFieldsResponse.make_one(res)

    def get_log_object(
        self,
        res: "bs_td.GetLogObjectResponseTypeDef",
    ) -> "dc_td.GetLogObjectResponse":
        return dc_td.GetLogObjectResponse.make_one(res)

    def get_log_record(
        self,
        res: "bs_td.GetLogRecordResponseTypeDef",
    ) -> "dc_td.GetLogRecordResponse":
        return dc_td.GetLogRecordResponse.make_one(res)

    def get_query_results(
        self,
        res: "bs_td.GetQueryResultsResponseTypeDef",
    ) -> "dc_td.GetQueryResultsResponse":
        return dc_td.GetQueryResultsResponse.make_one(res)

    def get_transformer(
        self,
        res: "bs_td.GetTransformerResponseTypeDef",
    ) -> "dc_td.GetTransformerResponse":
        return dc_td.GetTransformerResponse.make_one(res)

    def list_anomalies(
        self,
        res: "bs_td.ListAnomaliesResponseTypeDef",
    ) -> "dc_td.ListAnomaliesResponse":
        return dc_td.ListAnomaliesResponse.make_one(res)

    def list_integrations(
        self,
        res: "bs_td.ListIntegrationsResponseTypeDef",
    ) -> "dc_td.ListIntegrationsResponse":
        return dc_td.ListIntegrationsResponse.make_one(res)

    def list_log_anomaly_detectors(
        self,
        res: "bs_td.ListLogAnomalyDetectorsResponseTypeDef",
    ) -> "dc_td.ListLogAnomalyDetectorsResponse":
        return dc_td.ListLogAnomalyDetectorsResponse.make_one(res)

    def list_log_groups(
        self,
        res: "bs_td.ListLogGroupsResponseTypeDef",
    ) -> "dc_td.ListLogGroupsResponse":
        return dc_td.ListLogGroupsResponse.make_one(res)

    def list_log_groups_for_query(
        self,
        res: "bs_td.ListLogGroupsForQueryResponseTypeDef",
    ) -> "dc_td.ListLogGroupsForQueryResponse":
        return dc_td.ListLogGroupsForQueryResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_tags_log_group(
        self,
        res: "bs_td.ListTagsLogGroupResponseTypeDef",
    ) -> "dc_td.ListTagsLogGroupResponse":
        return dc_td.ListTagsLogGroupResponse.make_one(res)

    def put_account_policy(
        self,
        res: "bs_td.PutAccountPolicyResponseTypeDef",
    ) -> "dc_td.PutAccountPolicyResponse":
        return dc_td.PutAccountPolicyResponse.make_one(res)

    def put_data_protection_policy(
        self,
        res: "bs_td.PutDataProtectionPolicyResponseTypeDef",
    ) -> "dc_td.PutDataProtectionPolicyResponse":
        return dc_td.PutDataProtectionPolicyResponse.make_one(res)

    def put_delivery_destination(
        self,
        res: "bs_td.PutDeliveryDestinationResponseTypeDef",
    ) -> "dc_td.PutDeliveryDestinationResponse":
        return dc_td.PutDeliveryDestinationResponse.make_one(res)

    def put_delivery_destination_policy(
        self,
        res: "bs_td.PutDeliveryDestinationPolicyResponseTypeDef",
    ) -> "dc_td.PutDeliveryDestinationPolicyResponse":
        return dc_td.PutDeliveryDestinationPolicyResponse.make_one(res)

    def put_delivery_source(
        self,
        res: "bs_td.PutDeliverySourceResponseTypeDef",
    ) -> "dc_td.PutDeliverySourceResponse":
        return dc_td.PutDeliverySourceResponse.make_one(res)

    def put_destination(
        self,
        res: "bs_td.PutDestinationResponseTypeDef",
    ) -> "dc_td.PutDestinationResponse":
        return dc_td.PutDestinationResponse.make_one(res)

    def put_destination_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_index_policy(
        self,
        res: "bs_td.PutIndexPolicyResponseTypeDef",
    ) -> "dc_td.PutIndexPolicyResponse":
        return dc_td.PutIndexPolicyResponse.make_one(res)

    def put_integration(
        self,
        res: "bs_td.PutIntegrationResponseTypeDef",
    ) -> "dc_td.PutIntegrationResponse":
        return dc_td.PutIntegrationResponse.make_one(res)

    def put_log_events(
        self,
        res: "bs_td.PutLogEventsResponseTypeDef",
    ) -> "dc_td.PutLogEventsResponse":
        return dc_td.PutLogEventsResponse.make_one(res)

    def put_metric_filter(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_query_definition(
        self,
        res: "bs_td.PutQueryDefinitionResponseTypeDef",
    ) -> "dc_td.PutQueryDefinitionResponse":
        return dc_td.PutQueryDefinitionResponse.make_one(res)

    def put_resource_policy(
        self,
        res: "bs_td.PutResourcePolicyResponseTypeDef",
    ) -> "dc_td.PutResourcePolicyResponse":
        return dc_td.PutResourcePolicyResponse.make_one(res)

    def put_retention_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_subscription_filter(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_transformer(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_live_tail(
        self,
        res: "bs_td.StartLiveTailResponseTypeDef",
    ) -> "dc_td.StartLiveTailResponse":
        return dc_td.StartLiveTailResponse.make_one(res)

    def start_query(
        self,
        res: "bs_td.StartQueryResponseTypeDef",
    ) -> "dc_td.StartQueryResponse":
        return dc_td.StartQueryResponse.make_one(res)

    def stop_query(
        self,
        res: "bs_td.StopQueryResponseTypeDef",
    ) -> "dc_td.StopQueryResponse":
        return dc_td.StopQueryResponse.make_one(res)

    def tag_log_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def test_metric_filter(
        self,
        res: "bs_td.TestMetricFilterResponseTypeDef",
    ) -> "dc_td.TestMetricFilterResponse":
        return dc_td.TestMetricFilterResponse.make_one(res)

    def test_transformer(
        self,
        res: "bs_td.TestTransformerResponseTypeDef",
    ) -> "dc_td.TestTransformerResponse":
        return dc_td.TestTransformerResponse.make_one(res)

    def untag_log_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_anomaly(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_log_anomaly_detector(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


logs_caster = LOGSCaster()
