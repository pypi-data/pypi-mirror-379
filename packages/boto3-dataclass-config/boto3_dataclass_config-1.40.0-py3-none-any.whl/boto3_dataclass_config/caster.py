# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_config import type_defs as bs_td


class CONFIGCaster:

    def associate_resource_types(
        self,
        res: "bs_td.AssociateResourceTypesResponseTypeDef",
    ) -> "dc_td.AssociateResourceTypesResponse":
        return dc_td.AssociateResourceTypesResponse.make_one(res)

    def batch_get_aggregate_resource_config(
        self,
        res: "bs_td.BatchGetAggregateResourceConfigResponseTypeDef",
    ) -> "dc_td.BatchGetAggregateResourceConfigResponse":
        return dc_td.BatchGetAggregateResourceConfigResponse.make_one(res)

    def batch_get_resource_config(
        self,
        res: "bs_td.BatchGetResourceConfigResponseTypeDef",
    ) -> "dc_td.BatchGetResourceConfigResponse":
        return dc_td.BatchGetResourceConfigResponse.make_one(res)

    def delete_aggregation_authorization(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_config_rule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_configuration_aggregator(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_configuration_recorder(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_conformance_pack(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_delivery_channel(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_organization_config_rule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_organization_conformance_pack(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_pending_aggregation_request(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_remediation_exceptions(
        self,
        res: "bs_td.DeleteRemediationExceptionsResponseTypeDef",
    ) -> "dc_td.DeleteRemediationExceptionsResponse":
        return dc_td.DeleteRemediationExceptionsResponse.make_one(res)

    def delete_resource_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_retention_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_service_linked_configuration_recorder(
        self,
        res: "bs_td.DeleteServiceLinkedConfigurationRecorderResponseTypeDef",
    ) -> "dc_td.DeleteServiceLinkedConfigurationRecorderResponse":
        return dc_td.DeleteServiceLinkedConfigurationRecorderResponse.make_one(res)

    def deliver_config_snapshot(
        self,
        res: "bs_td.DeliverConfigSnapshotResponseTypeDef",
    ) -> "dc_td.DeliverConfigSnapshotResponse":
        return dc_td.DeliverConfigSnapshotResponse.make_one(res)

    def describe_aggregate_compliance_by_config_rules(
        self,
        res: "bs_td.DescribeAggregateComplianceByConfigRulesResponseTypeDef",
    ) -> "dc_td.DescribeAggregateComplianceByConfigRulesResponse":
        return dc_td.DescribeAggregateComplianceByConfigRulesResponse.make_one(res)

    def describe_aggregate_compliance_by_conformance_packs(
        self,
        res: "bs_td.DescribeAggregateComplianceByConformancePacksResponseTypeDef",
    ) -> "dc_td.DescribeAggregateComplianceByConformancePacksResponse":
        return dc_td.DescribeAggregateComplianceByConformancePacksResponse.make_one(res)

    def describe_aggregation_authorizations(
        self,
        res: "bs_td.DescribeAggregationAuthorizationsResponseTypeDef",
    ) -> "dc_td.DescribeAggregationAuthorizationsResponse":
        return dc_td.DescribeAggregationAuthorizationsResponse.make_one(res)

    def describe_compliance_by_config_rule(
        self,
        res: "bs_td.DescribeComplianceByConfigRuleResponseTypeDef",
    ) -> "dc_td.DescribeComplianceByConfigRuleResponse":
        return dc_td.DescribeComplianceByConfigRuleResponse.make_one(res)

    def describe_compliance_by_resource(
        self,
        res: "bs_td.DescribeComplianceByResourceResponseTypeDef",
    ) -> "dc_td.DescribeComplianceByResourceResponse":
        return dc_td.DescribeComplianceByResourceResponse.make_one(res)

    def describe_config_rule_evaluation_status(
        self,
        res: "bs_td.DescribeConfigRuleEvaluationStatusResponseTypeDef",
    ) -> "dc_td.DescribeConfigRuleEvaluationStatusResponse":
        return dc_td.DescribeConfigRuleEvaluationStatusResponse.make_one(res)

    def describe_config_rules(
        self,
        res: "bs_td.DescribeConfigRulesResponseTypeDef",
    ) -> "dc_td.DescribeConfigRulesResponse":
        return dc_td.DescribeConfigRulesResponse.make_one(res)

    def describe_configuration_aggregator_sources_status(
        self,
        res: "bs_td.DescribeConfigurationAggregatorSourcesStatusResponseTypeDef",
    ) -> "dc_td.DescribeConfigurationAggregatorSourcesStatusResponse":
        return dc_td.DescribeConfigurationAggregatorSourcesStatusResponse.make_one(res)

    def describe_configuration_aggregators(
        self,
        res: "bs_td.DescribeConfigurationAggregatorsResponseTypeDef",
    ) -> "dc_td.DescribeConfigurationAggregatorsResponse":
        return dc_td.DescribeConfigurationAggregatorsResponse.make_one(res)

    def describe_configuration_recorder_status(
        self,
        res: "bs_td.DescribeConfigurationRecorderStatusResponseTypeDef",
    ) -> "dc_td.DescribeConfigurationRecorderStatusResponse":
        return dc_td.DescribeConfigurationRecorderStatusResponse.make_one(res)

    def describe_configuration_recorders(
        self,
        res: "bs_td.DescribeConfigurationRecordersResponseTypeDef",
    ) -> "dc_td.DescribeConfigurationRecordersResponse":
        return dc_td.DescribeConfigurationRecordersResponse.make_one(res)

    def describe_conformance_pack_compliance(
        self,
        res: "bs_td.DescribeConformancePackComplianceResponseTypeDef",
    ) -> "dc_td.DescribeConformancePackComplianceResponse":
        return dc_td.DescribeConformancePackComplianceResponse.make_one(res)

    def describe_conformance_pack_status(
        self,
        res: "bs_td.DescribeConformancePackStatusResponseTypeDef",
    ) -> "dc_td.DescribeConformancePackStatusResponse":
        return dc_td.DescribeConformancePackStatusResponse.make_one(res)

    def describe_conformance_packs(
        self,
        res: "bs_td.DescribeConformancePacksResponseTypeDef",
    ) -> "dc_td.DescribeConformancePacksResponse":
        return dc_td.DescribeConformancePacksResponse.make_one(res)

    def describe_delivery_channel_status(
        self,
        res: "bs_td.DescribeDeliveryChannelStatusResponseTypeDef",
    ) -> "dc_td.DescribeDeliveryChannelStatusResponse":
        return dc_td.DescribeDeliveryChannelStatusResponse.make_one(res)

    def describe_delivery_channels(
        self,
        res: "bs_td.DescribeDeliveryChannelsResponseTypeDef",
    ) -> "dc_td.DescribeDeliveryChannelsResponse":
        return dc_td.DescribeDeliveryChannelsResponse.make_one(res)

    def describe_organization_config_rule_statuses(
        self,
        res: "bs_td.DescribeOrganizationConfigRuleStatusesResponseTypeDef",
    ) -> "dc_td.DescribeOrganizationConfigRuleStatusesResponse":
        return dc_td.DescribeOrganizationConfigRuleStatusesResponse.make_one(res)

    def describe_organization_config_rules(
        self,
        res: "bs_td.DescribeOrganizationConfigRulesResponseTypeDef",
    ) -> "dc_td.DescribeOrganizationConfigRulesResponse":
        return dc_td.DescribeOrganizationConfigRulesResponse.make_one(res)

    def describe_organization_conformance_pack_statuses(
        self,
        res: "bs_td.DescribeOrganizationConformancePackStatusesResponseTypeDef",
    ) -> "dc_td.DescribeOrganizationConformancePackStatusesResponse":
        return dc_td.DescribeOrganizationConformancePackStatusesResponse.make_one(res)

    def describe_organization_conformance_packs(
        self,
        res: "bs_td.DescribeOrganizationConformancePacksResponseTypeDef",
    ) -> "dc_td.DescribeOrganizationConformancePacksResponse":
        return dc_td.DescribeOrganizationConformancePacksResponse.make_one(res)

    def describe_pending_aggregation_requests(
        self,
        res: "bs_td.DescribePendingAggregationRequestsResponseTypeDef",
    ) -> "dc_td.DescribePendingAggregationRequestsResponse":
        return dc_td.DescribePendingAggregationRequestsResponse.make_one(res)

    def describe_remediation_configurations(
        self,
        res: "bs_td.DescribeRemediationConfigurationsResponseTypeDef",
    ) -> "dc_td.DescribeRemediationConfigurationsResponse":
        return dc_td.DescribeRemediationConfigurationsResponse.make_one(res)

    def describe_remediation_exceptions(
        self,
        res: "bs_td.DescribeRemediationExceptionsResponseTypeDef",
    ) -> "dc_td.DescribeRemediationExceptionsResponse":
        return dc_td.DescribeRemediationExceptionsResponse.make_one(res)

    def describe_remediation_execution_status(
        self,
        res: "bs_td.DescribeRemediationExecutionStatusResponseTypeDef",
    ) -> "dc_td.DescribeRemediationExecutionStatusResponse":
        return dc_td.DescribeRemediationExecutionStatusResponse.make_one(res)

    def describe_retention_configurations(
        self,
        res: "bs_td.DescribeRetentionConfigurationsResponseTypeDef",
    ) -> "dc_td.DescribeRetentionConfigurationsResponse":
        return dc_td.DescribeRetentionConfigurationsResponse.make_one(res)

    def disassociate_resource_types(
        self,
        res: "bs_td.DisassociateResourceTypesResponseTypeDef",
    ) -> "dc_td.DisassociateResourceTypesResponse":
        return dc_td.DisassociateResourceTypesResponse.make_one(res)

    def get_aggregate_compliance_details_by_config_rule(
        self,
        res: "bs_td.GetAggregateComplianceDetailsByConfigRuleResponseTypeDef",
    ) -> "dc_td.GetAggregateComplianceDetailsByConfigRuleResponse":
        return dc_td.GetAggregateComplianceDetailsByConfigRuleResponse.make_one(res)

    def get_aggregate_config_rule_compliance_summary(
        self,
        res: "bs_td.GetAggregateConfigRuleComplianceSummaryResponseTypeDef",
    ) -> "dc_td.GetAggregateConfigRuleComplianceSummaryResponse":
        return dc_td.GetAggregateConfigRuleComplianceSummaryResponse.make_one(res)

    def get_aggregate_conformance_pack_compliance_summary(
        self,
        res: "bs_td.GetAggregateConformancePackComplianceSummaryResponseTypeDef",
    ) -> "dc_td.GetAggregateConformancePackComplianceSummaryResponse":
        return dc_td.GetAggregateConformancePackComplianceSummaryResponse.make_one(res)

    def get_aggregate_discovered_resource_counts(
        self,
        res: "bs_td.GetAggregateDiscoveredResourceCountsResponseTypeDef",
    ) -> "dc_td.GetAggregateDiscoveredResourceCountsResponse":
        return dc_td.GetAggregateDiscoveredResourceCountsResponse.make_one(res)

    def get_aggregate_resource_config(
        self,
        res: "bs_td.GetAggregateResourceConfigResponseTypeDef",
    ) -> "dc_td.GetAggregateResourceConfigResponse":
        return dc_td.GetAggregateResourceConfigResponse.make_one(res)

    def get_compliance_details_by_config_rule(
        self,
        res: "bs_td.GetComplianceDetailsByConfigRuleResponseTypeDef",
    ) -> "dc_td.GetComplianceDetailsByConfigRuleResponse":
        return dc_td.GetComplianceDetailsByConfigRuleResponse.make_one(res)

    def get_compliance_details_by_resource(
        self,
        res: "bs_td.GetComplianceDetailsByResourceResponseTypeDef",
    ) -> "dc_td.GetComplianceDetailsByResourceResponse":
        return dc_td.GetComplianceDetailsByResourceResponse.make_one(res)

    def get_compliance_summary_by_config_rule(
        self,
        res: "bs_td.GetComplianceSummaryByConfigRuleResponseTypeDef",
    ) -> "dc_td.GetComplianceSummaryByConfigRuleResponse":
        return dc_td.GetComplianceSummaryByConfigRuleResponse.make_one(res)

    def get_compliance_summary_by_resource_type(
        self,
        res: "bs_td.GetComplianceSummaryByResourceTypeResponseTypeDef",
    ) -> "dc_td.GetComplianceSummaryByResourceTypeResponse":
        return dc_td.GetComplianceSummaryByResourceTypeResponse.make_one(res)

    def get_conformance_pack_compliance_details(
        self,
        res: "bs_td.GetConformancePackComplianceDetailsResponseTypeDef",
    ) -> "dc_td.GetConformancePackComplianceDetailsResponse":
        return dc_td.GetConformancePackComplianceDetailsResponse.make_one(res)

    def get_conformance_pack_compliance_summary(
        self,
        res: "bs_td.GetConformancePackComplianceSummaryResponseTypeDef",
    ) -> "dc_td.GetConformancePackComplianceSummaryResponse":
        return dc_td.GetConformancePackComplianceSummaryResponse.make_one(res)

    def get_custom_rule_policy(
        self,
        res: "bs_td.GetCustomRulePolicyResponseTypeDef",
    ) -> "dc_td.GetCustomRulePolicyResponse":
        return dc_td.GetCustomRulePolicyResponse.make_one(res)

    def get_discovered_resource_counts(
        self,
        res: "bs_td.GetDiscoveredResourceCountsResponseTypeDef",
    ) -> "dc_td.GetDiscoveredResourceCountsResponse":
        return dc_td.GetDiscoveredResourceCountsResponse.make_one(res)

    def get_organization_config_rule_detailed_status(
        self,
        res: "bs_td.GetOrganizationConfigRuleDetailedStatusResponseTypeDef",
    ) -> "dc_td.GetOrganizationConfigRuleDetailedStatusResponse":
        return dc_td.GetOrganizationConfigRuleDetailedStatusResponse.make_one(res)

    def get_organization_conformance_pack_detailed_status(
        self,
        res: "bs_td.GetOrganizationConformancePackDetailedStatusResponseTypeDef",
    ) -> "dc_td.GetOrganizationConformancePackDetailedStatusResponse":
        return dc_td.GetOrganizationConformancePackDetailedStatusResponse.make_one(res)

    def get_organization_custom_rule_policy(
        self,
        res: "bs_td.GetOrganizationCustomRulePolicyResponseTypeDef",
    ) -> "dc_td.GetOrganizationCustomRulePolicyResponse":
        return dc_td.GetOrganizationCustomRulePolicyResponse.make_one(res)

    def get_resource_config_history(
        self,
        res: "bs_td.GetResourceConfigHistoryResponseTypeDef",
    ) -> "dc_td.GetResourceConfigHistoryResponse":
        return dc_td.GetResourceConfigHistoryResponse.make_one(res)

    def get_resource_evaluation_summary(
        self,
        res: "bs_td.GetResourceEvaluationSummaryResponseTypeDef",
    ) -> "dc_td.GetResourceEvaluationSummaryResponse":
        return dc_td.GetResourceEvaluationSummaryResponse.make_one(res)

    def get_stored_query(
        self,
        res: "bs_td.GetStoredQueryResponseTypeDef",
    ) -> "dc_td.GetStoredQueryResponse":
        return dc_td.GetStoredQueryResponse.make_one(res)

    def list_aggregate_discovered_resources(
        self,
        res: "bs_td.ListAggregateDiscoveredResourcesResponseTypeDef",
    ) -> "dc_td.ListAggregateDiscoveredResourcesResponse":
        return dc_td.ListAggregateDiscoveredResourcesResponse.make_one(res)

    def list_configuration_recorders(
        self,
        res: "bs_td.ListConfigurationRecordersResponseTypeDef",
    ) -> "dc_td.ListConfigurationRecordersResponse":
        return dc_td.ListConfigurationRecordersResponse.make_one(res)

    def list_conformance_pack_compliance_scores(
        self,
        res: "bs_td.ListConformancePackComplianceScoresResponseTypeDef",
    ) -> "dc_td.ListConformancePackComplianceScoresResponse":
        return dc_td.ListConformancePackComplianceScoresResponse.make_one(res)

    def list_discovered_resources(
        self,
        res: "bs_td.ListDiscoveredResourcesResponseTypeDef",
    ) -> "dc_td.ListDiscoveredResourcesResponse":
        return dc_td.ListDiscoveredResourcesResponse.make_one(res)

    def list_resource_evaluations(
        self,
        res: "bs_td.ListResourceEvaluationsResponseTypeDef",
    ) -> "dc_td.ListResourceEvaluationsResponse":
        return dc_td.ListResourceEvaluationsResponse.make_one(res)

    def list_stored_queries(
        self,
        res: "bs_td.ListStoredQueriesResponseTypeDef",
    ) -> "dc_td.ListStoredQueriesResponse":
        return dc_td.ListStoredQueriesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_aggregation_authorization(
        self,
        res: "bs_td.PutAggregationAuthorizationResponseTypeDef",
    ) -> "dc_td.PutAggregationAuthorizationResponse":
        return dc_td.PutAggregationAuthorizationResponse.make_one(res)

    def put_config_rule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_configuration_aggregator(
        self,
        res: "bs_td.PutConfigurationAggregatorResponseTypeDef",
    ) -> "dc_td.PutConfigurationAggregatorResponse":
        return dc_td.PutConfigurationAggregatorResponse.make_one(res)

    def put_configuration_recorder(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_conformance_pack(
        self,
        res: "bs_td.PutConformancePackResponseTypeDef",
    ) -> "dc_td.PutConformancePackResponse":
        return dc_td.PutConformancePackResponse.make_one(res)

    def put_delivery_channel(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_evaluations(
        self,
        res: "bs_td.PutEvaluationsResponseTypeDef",
    ) -> "dc_td.PutEvaluationsResponse":
        return dc_td.PutEvaluationsResponse.make_one(res)

    def put_organization_config_rule(
        self,
        res: "bs_td.PutOrganizationConfigRuleResponseTypeDef",
    ) -> "dc_td.PutOrganizationConfigRuleResponse":
        return dc_td.PutOrganizationConfigRuleResponse.make_one(res)

    def put_organization_conformance_pack(
        self,
        res: "bs_td.PutOrganizationConformancePackResponseTypeDef",
    ) -> "dc_td.PutOrganizationConformancePackResponse":
        return dc_td.PutOrganizationConformancePackResponse.make_one(res)

    def put_remediation_configurations(
        self,
        res: "bs_td.PutRemediationConfigurationsResponseTypeDef",
    ) -> "dc_td.PutRemediationConfigurationsResponse":
        return dc_td.PutRemediationConfigurationsResponse.make_one(res)

    def put_remediation_exceptions(
        self,
        res: "bs_td.PutRemediationExceptionsResponseTypeDef",
    ) -> "dc_td.PutRemediationExceptionsResponse":
        return dc_td.PutRemediationExceptionsResponse.make_one(res)

    def put_resource_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_retention_configuration(
        self,
        res: "bs_td.PutRetentionConfigurationResponseTypeDef",
    ) -> "dc_td.PutRetentionConfigurationResponse":
        return dc_td.PutRetentionConfigurationResponse.make_one(res)

    def put_service_linked_configuration_recorder(
        self,
        res: "bs_td.PutServiceLinkedConfigurationRecorderResponseTypeDef",
    ) -> "dc_td.PutServiceLinkedConfigurationRecorderResponse":
        return dc_td.PutServiceLinkedConfigurationRecorderResponse.make_one(res)

    def put_stored_query(
        self,
        res: "bs_td.PutStoredQueryResponseTypeDef",
    ) -> "dc_td.PutStoredQueryResponse":
        return dc_td.PutStoredQueryResponse.make_one(res)

    def select_aggregate_resource_config(
        self,
        res: "bs_td.SelectAggregateResourceConfigResponseTypeDef",
    ) -> "dc_td.SelectAggregateResourceConfigResponse":
        return dc_td.SelectAggregateResourceConfigResponse.make_one(res)

    def select_resource_config(
        self,
        res: "bs_td.SelectResourceConfigResponseTypeDef",
    ) -> "dc_td.SelectResourceConfigResponse":
        return dc_td.SelectResourceConfigResponse.make_one(res)

    def start_configuration_recorder(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_remediation_execution(
        self,
        res: "bs_td.StartRemediationExecutionResponseTypeDef",
    ) -> "dc_td.StartRemediationExecutionResponse":
        return dc_td.StartRemediationExecutionResponse.make_one(res)

    def start_resource_evaluation(
        self,
        res: "bs_td.StartResourceEvaluationResponseTypeDef",
    ) -> "dc_td.StartResourceEvaluationResponse":
        return dc_td.StartResourceEvaluationResponse.make_one(res)

    def stop_configuration_recorder(
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


config_caster = CONFIGCaster()
