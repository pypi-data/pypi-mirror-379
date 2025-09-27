# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_connect import type_defs as bs_td


class CONNECTCaster:

    def activate_evaluation_form(
        self,
        res: "bs_td.ActivateEvaluationFormResponseTypeDef",
    ) -> "dc_td.ActivateEvaluationFormResponse":
        return dc_td.ActivateEvaluationFormResponse.make_one(res)

    def associate_analytics_data_set(
        self,
        res: "bs_td.AssociateAnalyticsDataSetResponseTypeDef",
    ) -> "dc_td.AssociateAnalyticsDataSetResponse":
        return dc_td.AssociateAnalyticsDataSetResponse.make_one(res)

    def associate_approved_origin(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def associate_bot(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def associate_instance_storage_config(
        self,
        res: "bs_td.AssociateInstanceStorageConfigResponseTypeDef",
    ) -> "dc_td.AssociateInstanceStorageConfigResponse":
        return dc_td.AssociateInstanceStorageConfigResponse.make_one(res)

    def associate_lambda_function(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def associate_lex_bot(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def associate_phone_number_contact_flow(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def associate_queue_quick_connects(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def associate_routing_profile_queues(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def associate_security_key(
        self,
        res: "bs_td.AssociateSecurityKeyResponseTypeDef",
    ) -> "dc_td.AssociateSecurityKeyResponse":
        return dc_td.AssociateSecurityKeyResponse.make_one(res)

    def associate_user_proficiencies(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def batch_associate_analytics_data_set(
        self,
        res: "bs_td.BatchAssociateAnalyticsDataSetResponseTypeDef",
    ) -> "dc_td.BatchAssociateAnalyticsDataSetResponse":
        return dc_td.BatchAssociateAnalyticsDataSetResponse.make_one(res)

    def batch_disassociate_analytics_data_set(
        self,
        res: "bs_td.BatchDisassociateAnalyticsDataSetResponseTypeDef",
    ) -> "dc_td.BatchDisassociateAnalyticsDataSetResponse":
        return dc_td.BatchDisassociateAnalyticsDataSetResponse.make_one(res)

    def batch_get_attached_file_metadata(
        self,
        res: "bs_td.BatchGetAttachedFileMetadataResponseTypeDef",
    ) -> "dc_td.BatchGetAttachedFileMetadataResponse":
        return dc_td.BatchGetAttachedFileMetadataResponse.make_one(res)

    def batch_get_flow_association(
        self,
        res: "bs_td.BatchGetFlowAssociationResponseTypeDef",
    ) -> "dc_td.BatchGetFlowAssociationResponse":
        return dc_td.BatchGetFlowAssociationResponse.make_one(res)

    def batch_put_contact(
        self,
        res: "bs_td.BatchPutContactResponseTypeDef",
    ) -> "dc_td.BatchPutContactResponse":
        return dc_td.BatchPutContactResponse.make_one(res)

    def claim_phone_number(
        self,
        res: "bs_td.ClaimPhoneNumberResponseTypeDef",
    ) -> "dc_td.ClaimPhoneNumberResponse":
        return dc_td.ClaimPhoneNumberResponse.make_one(res)

    def create_agent_status(
        self,
        res: "bs_td.CreateAgentStatusResponseTypeDef",
    ) -> "dc_td.CreateAgentStatusResponse":
        return dc_td.CreateAgentStatusResponse.make_one(res)

    def create_contact(
        self,
        res: "bs_td.CreateContactResponseTypeDef",
    ) -> "dc_td.CreateContactResponse":
        return dc_td.CreateContactResponse.make_one(res)

    def create_contact_flow(
        self,
        res: "bs_td.CreateContactFlowResponseTypeDef",
    ) -> "dc_td.CreateContactFlowResponse":
        return dc_td.CreateContactFlowResponse.make_one(res)

    def create_contact_flow_module(
        self,
        res: "bs_td.CreateContactFlowModuleResponseTypeDef",
    ) -> "dc_td.CreateContactFlowModuleResponse":
        return dc_td.CreateContactFlowModuleResponse.make_one(res)

    def create_contact_flow_version(
        self,
        res: "bs_td.CreateContactFlowVersionResponseTypeDef",
    ) -> "dc_td.CreateContactFlowVersionResponse":
        return dc_td.CreateContactFlowVersionResponse.make_one(res)

    def create_email_address(
        self,
        res: "bs_td.CreateEmailAddressResponseTypeDef",
    ) -> "dc_td.CreateEmailAddressResponse":
        return dc_td.CreateEmailAddressResponse.make_one(res)

    def create_evaluation_form(
        self,
        res: "bs_td.CreateEvaluationFormResponseTypeDef",
    ) -> "dc_td.CreateEvaluationFormResponse":
        return dc_td.CreateEvaluationFormResponse.make_one(res)

    def create_hours_of_operation(
        self,
        res: "bs_td.CreateHoursOfOperationResponseTypeDef",
    ) -> "dc_td.CreateHoursOfOperationResponse":
        return dc_td.CreateHoursOfOperationResponse.make_one(res)

    def create_hours_of_operation_override(
        self,
        res: "bs_td.CreateHoursOfOperationOverrideResponseTypeDef",
    ) -> "dc_td.CreateHoursOfOperationOverrideResponse":
        return dc_td.CreateHoursOfOperationOverrideResponse.make_one(res)

    def create_instance(
        self,
        res: "bs_td.CreateInstanceResponseTypeDef",
    ) -> "dc_td.CreateInstanceResponse":
        return dc_td.CreateInstanceResponse.make_one(res)

    def create_integration_association(
        self,
        res: "bs_td.CreateIntegrationAssociationResponseTypeDef",
    ) -> "dc_td.CreateIntegrationAssociationResponse":
        return dc_td.CreateIntegrationAssociationResponse.make_one(res)

    def create_participant(
        self,
        res: "bs_td.CreateParticipantResponseTypeDef",
    ) -> "dc_td.CreateParticipantResponse":
        return dc_td.CreateParticipantResponse.make_one(res)

    def create_persistent_contact_association(
        self,
        res: "bs_td.CreatePersistentContactAssociationResponseTypeDef",
    ) -> "dc_td.CreatePersistentContactAssociationResponse":
        return dc_td.CreatePersistentContactAssociationResponse.make_one(res)

    def create_predefined_attribute(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_prompt(
        self,
        res: "bs_td.CreatePromptResponseTypeDef",
    ) -> "dc_td.CreatePromptResponse":
        return dc_td.CreatePromptResponse.make_one(res)

    def create_push_notification_registration(
        self,
        res: "bs_td.CreatePushNotificationRegistrationResponseTypeDef",
    ) -> "dc_td.CreatePushNotificationRegistrationResponse":
        return dc_td.CreatePushNotificationRegistrationResponse.make_one(res)

    def create_queue(
        self,
        res: "bs_td.CreateQueueResponseTypeDef",
    ) -> "dc_td.CreateQueueResponse":
        return dc_td.CreateQueueResponse.make_one(res)

    def create_quick_connect(
        self,
        res: "bs_td.CreateQuickConnectResponseTypeDef",
    ) -> "dc_td.CreateQuickConnectResponse":
        return dc_td.CreateQuickConnectResponse.make_one(res)

    def create_routing_profile(
        self,
        res: "bs_td.CreateRoutingProfileResponseTypeDef",
    ) -> "dc_td.CreateRoutingProfileResponse":
        return dc_td.CreateRoutingProfileResponse.make_one(res)

    def create_rule(
        self,
        res: "bs_td.CreateRuleResponseTypeDef",
    ) -> "dc_td.CreateRuleResponse":
        return dc_td.CreateRuleResponse.make_one(res)

    def create_security_profile(
        self,
        res: "bs_td.CreateSecurityProfileResponseTypeDef",
    ) -> "dc_td.CreateSecurityProfileResponse":
        return dc_td.CreateSecurityProfileResponse.make_one(res)

    def create_task_template(
        self,
        res: "bs_td.CreateTaskTemplateResponseTypeDef",
    ) -> "dc_td.CreateTaskTemplateResponse":
        return dc_td.CreateTaskTemplateResponse.make_one(res)

    def create_traffic_distribution_group(
        self,
        res: "bs_td.CreateTrafficDistributionGroupResponseTypeDef",
    ) -> "dc_td.CreateTrafficDistributionGroupResponse":
        return dc_td.CreateTrafficDistributionGroupResponse.make_one(res)

    def create_use_case(
        self,
        res: "bs_td.CreateUseCaseResponseTypeDef",
    ) -> "dc_td.CreateUseCaseResponse":
        return dc_td.CreateUseCaseResponse.make_one(res)

    def create_user(
        self,
        res: "bs_td.CreateUserResponseTypeDef",
    ) -> "dc_td.CreateUserResponse":
        return dc_td.CreateUserResponse.make_one(res)

    def create_user_hierarchy_group(
        self,
        res: "bs_td.CreateUserHierarchyGroupResponseTypeDef",
    ) -> "dc_td.CreateUserHierarchyGroupResponse":
        return dc_td.CreateUserHierarchyGroupResponse.make_one(res)

    def create_view(
        self,
        res: "bs_td.CreateViewResponseTypeDef",
    ) -> "dc_td.CreateViewResponse":
        return dc_td.CreateViewResponse.make_one(res)

    def create_view_version(
        self,
        res: "bs_td.CreateViewVersionResponseTypeDef",
    ) -> "dc_td.CreateViewVersionResponse":
        return dc_td.CreateViewVersionResponse.make_one(res)

    def create_vocabulary(
        self,
        res: "bs_td.CreateVocabularyResponseTypeDef",
    ) -> "dc_td.CreateVocabularyResponse":
        return dc_td.CreateVocabularyResponse.make_one(res)

    def deactivate_evaluation_form(
        self,
        res: "bs_td.DeactivateEvaluationFormResponseTypeDef",
    ) -> "dc_td.DeactivateEvaluationFormResponse":
        return dc_td.DeactivateEvaluationFormResponse.make_one(res)

    def delete_contact_evaluation(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_evaluation_form(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_hours_of_operation(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_hours_of_operation_override(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_integration_association(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_predefined_attribute(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_prompt(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_queue(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_quick_connect(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_routing_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_rule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_security_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_use_case(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_user(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_user_hierarchy_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_vocabulary(
        self,
        res: "bs_td.DeleteVocabularyResponseTypeDef",
    ) -> "dc_td.DeleteVocabularyResponse":
        return dc_td.DeleteVocabularyResponse.make_one(res)

    def describe_agent_status(
        self,
        res: "bs_td.DescribeAgentStatusResponseTypeDef",
    ) -> "dc_td.DescribeAgentStatusResponse":
        return dc_td.DescribeAgentStatusResponse.make_one(res)

    def describe_authentication_profile(
        self,
        res: "bs_td.DescribeAuthenticationProfileResponseTypeDef",
    ) -> "dc_td.DescribeAuthenticationProfileResponse":
        return dc_td.DescribeAuthenticationProfileResponse.make_one(res)

    def describe_contact(
        self,
        res: "bs_td.DescribeContactResponseTypeDef",
    ) -> "dc_td.DescribeContactResponse":
        return dc_td.DescribeContactResponse.make_one(res)

    def describe_contact_evaluation(
        self,
        res: "bs_td.DescribeContactEvaluationResponseTypeDef",
    ) -> "dc_td.DescribeContactEvaluationResponse":
        return dc_td.DescribeContactEvaluationResponse.make_one(res)

    def describe_contact_flow(
        self,
        res: "bs_td.DescribeContactFlowResponseTypeDef",
    ) -> "dc_td.DescribeContactFlowResponse":
        return dc_td.DescribeContactFlowResponse.make_one(res)

    def describe_contact_flow_module(
        self,
        res: "bs_td.DescribeContactFlowModuleResponseTypeDef",
    ) -> "dc_td.DescribeContactFlowModuleResponse":
        return dc_td.DescribeContactFlowModuleResponse.make_one(res)

    def describe_email_address(
        self,
        res: "bs_td.DescribeEmailAddressResponseTypeDef",
    ) -> "dc_td.DescribeEmailAddressResponse":
        return dc_td.DescribeEmailAddressResponse.make_one(res)

    def describe_evaluation_form(
        self,
        res: "bs_td.DescribeEvaluationFormResponseTypeDef",
    ) -> "dc_td.DescribeEvaluationFormResponse":
        return dc_td.DescribeEvaluationFormResponse.make_one(res)

    def describe_hours_of_operation(
        self,
        res: "bs_td.DescribeHoursOfOperationResponseTypeDef",
    ) -> "dc_td.DescribeHoursOfOperationResponse":
        return dc_td.DescribeHoursOfOperationResponse.make_one(res)

    def describe_hours_of_operation_override(
        self,
        res: "bs_td.DescribeHoursOfOperationOverrideResponseTypeDef",
    ) -> "dc_td.DescribeHoursOfOperationOverrideResponse":
        return dc_td.DescribeHoursOfOperationOverrideResponse.make_one(res)

    def describe_instance(
        self,
        res: "bs_td.DescribeInstanceResponseTypeDef",
    ) -> "dc_td.DescribeInstanceResponse":
        return dc_td.DescribeInstanceResponse.make_one(res)

    def describe_instance_attribute(
        self,
        res: "bs_td.DescribeInstanceAttributeResponseTypeDef",
    ) -> "dc_td.DescribeInstanceAttributeResponse":
        return dc_td.DescribeInstanceAttributeResponse.make_one(res)

    def describe_instance_storage_config(
        self,
        res: "bs_td.DescribeInstanceStorageConfigResponseTypeDef",
    ) -> "dc_td.DescribeInstanceStorageConfigResponse":
        return dc_td.DescribeInstanceStorageConfigResponse.make_one(res)

    def describe_phone_number(
        self,
        res: "bs_td.DescribePhoneNumberResponseTypeDef",
    ) -> "dc_td.DescribePhoneNumberResponse":
        return dc_td.DescribePhoneNumberResponse.make_one(res)

    def describe_predefined_attribute(
        self,
        res: "bs_td.DescribePredefinedAttributeResponseTypeDef",
    ) -> "dc_td.DescribePredefinedAttributeResponse":
        return dc_td.DescribePredefinedAttributeResponse.make_one(res)

    def describe_prompt(
        self,
        res: "bs_td.DescribePromptResponseTypeDef",
    ) -> "dc_td.DescribePromptResponse":
        return dc_td.DescribePromptResponse.make_one(res)

    def describe_queue(
        self,
        res: "bs_td.DescribeQueueResponseTypeDef",
    ) -> "dc_td.DescribeQueueResponse":
        return dc_td.DescribeQueueResponse.make_one(res)

    def describe_quick_connect(
        self,
        res: "bs_td.DescribeQuickConnectResponseTypeDef",
    ) -> "dc_td.DescribeQuickConnectResponse":
        return dc_td.DescribeQuickConnectResponse.make_one(res)

    def describe_routing_profile(
        self,
        res: "bs_td.DescribeRoutingProfileResponseTypeDef",
    ) -> "dc_td.DescribeRoutingProfileResponse":
        return dc_td.DescribeRoutingProfileResponse.make_one(res)

    def describe_rule(
        self,
        res: "bs_td.DescribeRuleResponseTypeDef",
    ) -> "dc_td.DescribeRuleResponse":
        return dc_td.DescribeRuleResponse.make_one(res)

    def describe_security_profile(
        self,
        res: "bs_td.DescribeSecurityProfileResponseTypeDef",
    ) -> "dc_td.DescribeSecurityProfileResponse":
        return dc_td.DescribeSecurityProfileResponse.make_one(res)

    def describe_traffic_distribution_group(
        self,
        res: "bs_td.DescribeTrafficDistributionGroupResponseTypeDef",
    ) -> "dc_td.DescribeTrafficDistributionGroupResponse":
        return dc_td.DescribeTrafficDistributionGroupResponse.make_one(res)

    def describe_user(
        self,
        res: "bs_td.DescribeUserResponseTypeDef",
    ) -> "dc_td.DescribeUserResponse":
        return dc_td.DescribeUserResponse.make_one(res)

    def describe_user_hierarchy_group(
        self,
        res: "bs_td.DescribeUserHierarchyGroupResponseTypeDef",
    ) -> "dc_td.DescribeUserHierarchyGroupResponse":
        return dc_td.DescribeUserHierarchyGroupResponse.make_one(res)

    def describe_user_hierarchy_structure(
        self,
        res: "bs_td.DescribeUserHierarchyStructureResponseTypeDef",
    ) -> "dc_td.DescribeUserHierarchyStructureResponse":
        return dc_td.DescribeUserHierarchyStructureResponse.make_one(res)

    def describe_view(
        self,
        res: "bs_td.DescribeViewResponseTypeDef",
    ) -> "dc_td.DescribeViewResponse":
        return dc_td.DescribeViewResponse.make_one(res)

    def describe_vocabulary(
        self,
        res: "bs_td.DescribeVocabularyResponseTypeDef",
    ) -> "dc_td.DescribeVocabularyResponse":
        return dc_td.DescribeVocabularyResponse.make_one(res)

    def disassociate_analytics_data_set(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_approved_origin(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_bot(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_instance_storage_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_lambda_function(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_lex_bot(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_phone_number_contact_flow(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_queue_quick_connects(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_routing_profile_queues(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_security_key(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_user_proficiencies(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_attached_file(
        self,
        res: "bs_td.GetAttachedFileResponseTypeDef",
    ) -> "dc_td.GetAttachedFileResponse":
        return dc_td.GetAttachedFileResponse.make_one(res)

    def get_contact_attributes(
        self,
        res: "bs_td.GetContactAttributesResponseTypeDef",
    ) -> "dc_td.GetContactAttributesResponse":
        return dc_td.GetContactAttributesResponse.make_one(res)

    def get_contact_metrics(
        self,
        res: "bs_td.GetContactMetricsResponseTypeDef",
    ) -> "dc_td.GetContactMetricsResponse":
        return dc_td.GetContactMetricsResponse.make_one(res)

    def get_current_metric_data(
        self,
        res: "bs_td.GetCurrentMetricDataResponseTypeDef",
    ) -> "dc_td.GetCurrentMetricDataResponse":
        return dc_td.GetCurrentMetricDataResponse.make_one(res)

    def get_current_user_data(
        self,
        res: "bs_td.GetCurrentUserDataResponseTypeDef",
    ) -> "dc_td.GetCurrentUserDataResponse":
        return dc_td.GetCurrentUserDataResponse.make_one(res)

    def get_effective_hours_of_operations(
        self,
        res: "bs_td.GetEffectiveHoursOfOperationsResponseTypeDef",
    ) -> "dc_td.GetEffectiveHoursOfOperationsResponse":
        return dc_td.GetEffectiveHoursOfOperationsResponse.make_one(res)

    def get_federation_token(
        self,
        res: "bs_td.GetFederationTokenResponseTypeDef",
    ) -> "dc_td.GetFederationTokenResponse":
        return dc_td.GetFederationTokenResponse.make_one(res)

    def get_flow_association(
        self,
        res: "bs_td.GetFlowAssociationResponseTypeDef",
    ) -> "dc_td.GetFlowAssociationResponse":
        return dc_td.GetFlowAssociationResponse.make_one(res)

    def get_metric_data(
        self,
        res: "bs_td.GetMetricDataResponseTypeDef",
    ) -> "dc_td.GetMetricDataResponse":
        return dc_td.GetMetricDataResponse.make_one(res)

    def get_metric_data_v2(
        self,
        res: "bs_td.GetMetricDataV2ResponseTypeDef",
    ) -> "dc_td.GetMetricDataV2Response":
        return dc_td.GetMetricDataV2Response.make_one(res)

    def get_prompt_file(
        self,
        res: "bs_td.GetPromptFileResponseTypeDef",
    ) -> "dc_td.GetPromptFileResponse":
        return dc_td.GetPromptFileResponse.make_one(res)

    def get_task_template(
        self,
        res: "bs_td.GetTaskTemplateResponseTypeDef",
    ) -> "dc_td.GetTaskTemplateResponse":
        return dc_td.GetTaskTemplateResponse.make_one(res)

    def get_traffic_distribution(
        self,
        res: "bs_td.GetTrafficDistributionResponseTypeDef",
    ) -> "dc_td.GetTrafficDistributionResponse":
        return dc_td.GetTrafficDistributionResponse.make_one(res)

    def import_phone_number(
        self,
        res: "bs_td.ImportPhoneNumberResponseTypeDef",
    ) -> "dc_td.ImportPhoneNumberResponse":
        return dc_td.ImportPhoneNumberResponse.make_one(res)

    def list_agent_statuses(
        self,
        res: "bs_td.ListAgentStatusResponseTypeDef",
    ) -> "dc_td.ListAgentStatusResponse":
        return dc_td.ListAgentStatusResponse.make_one(res)

    def list_analytics_data_associations(
        self,
        res: "bs_td.ListAnalyticsDataAssociationsResponseTypeDef",
    ) -> "dc_td.ListAnalyticsDataAssociationsResponse":
        return dc_td.ListAnalyticsDataAssociationsResponse.make_one(res)

    def list_analytics_data_lake_data_sets(
        self,
        res: "bs_td.ListAnalyticsDataLakeDataSetsResponseTypeDef",
    ) -> "dc_td.ListAnalyticsDataLakeDataSetsResponse":
        return dc_td.ListAnalyticsDataLakeDataSetsResponse.make_one(res)

    def list_approved_origins(
        self,
        res: "bs_td.ListApprovedOriginsResponseTypeDef",
    ) -> "dc_td.ListApprovedOriginsResponse":
        return dc_td.ListApprovedOriginsResponse.make_one(res)

    def list_associated_contacts(
        self,
        res: "bs_td.ListAssociatedContactsResponseTypeDef",
    ) -> "dc_td.ListAssociatedContactsResponse":
        return dc_td.ListAssociatedContactsResponse.make_one(res)

    def list_authentication_profiles(
        self,
        res: "bs_td.ListAuthenticationProfilesResponseTypeDef",
    ) -> "dc_td.ListAuthenticationProfilesResponse":
        return dc_td.ListAuthenticationProfilesResponse.make_one(res)

    def list_bots(
        self,
        res: "bs_td.ListBotsResponseTypeDef",
    ) -> "dc_td.ListBotsResponse":
        return dc_td.ListBotsResponse.make_one(res)

    def list_contact_evaluations(
        self,
        res: "bs_td.ListContactEvaluationsResponseTypeDef",
    ) -> "dc_td.ListContactEvaluationsResponse":
        return dc_td.ListContactEvaluationsResponse.make_one(res)

    def list_contact_flow_modules(
        self,
        res: "bs_td.ListContactFlowModulesResponseTypeDef",
    ) -> "dc_td.ListContactFlowModulesResponse":
        return dc_td.ListContactFlowModulesResponse.make_one(res)

    def list_contact_flow_versions(
        self,
        res: "bs_td.ListContactFlowVersionsResponseTypeDef",
    ) -> "dc_td.ListContactFlowVersionsResponse":
        return dc_td.ListContactFlowVersionsResponse.make_one(res)

    def list_contact_flows(
        self,
        res: "bs_td.ListContactFlowsResponseTypeDef",
    ) -> "dc_td.ListContactFlowsResponse":
        return dc_td.ListContactFlowsResponse.make_one(res)

    def list_contact_references(
        self,
        res: "bs_td.ListContactReferencesResponseTypeDef",
    ) -> "dc_td.ListContactReferencesResponse":
        return dc_td.ListContactReferencesResponse.make_one(res)

    def list_default_vocabularies(
        self,
        res: "bs_td.ListDefaultVocabulariesResponseTypeDef",
    ) -> "dc_td.ListDefaultVocabulariesResponse":
        return dc_td.ListDefaultVocabulariesResponse.make_one(res)

    def list_evaluation_form_versions(
        self,
        res: "bs_td.ListEvaluationFormVersionsResponseTypeDef",
    ) -> "dc_td.ListEvaluationFormVersionsResponse":
        return dc_td.ListEvaluationFormVersionsResponse.make_one(res)

    def list_evaluation_forms(
        self,
        res: "bs_td.ListEvaluationFormsResponseTypeDef",
    ) -> "dc_td.ListEvaluationFormsResponse":
        return dc_td.ListEvaluationFormsResponse.make_one(res)

    def list_flow_associations(
        self,
        res: "bs_td.ListFlowAssociationsResponseTypeDef",
    ) -> "dc_td.ListFlowAssociationsResponse":
        return dc_td.ListFlowAssociationsResponse.make_one(res)

    def list_hours_of_operation_overrides(
        self,
        res: "bs_td.ListHoursOfOperationOverridesResponseTypeDef",
    ) -> "dc_td.ListHoursOfOperationOverridesResponse":
        return dc_td.ListHoursOfOperationOverridesResponse.make_one(res)

    def list_hours_of_operations(
        self,
        res: "bs_td.ListHoursOfOperationsResponseTypeDef",
    ) -> "dc_td.ListHoursOfOperationsResponse":
        return dc_td.ListHoursOfOperationsResponse.make_one(res)

    def list_instance_attributes(
        self,
        res: "bs_td.ListInstanceAttributesResponseTypeDef",
    ) -> "dc_td.ListInstanceAttributesResponse":
        return dc_td.ListInstanceAttributesResponse.make_one(res)

    def list_instance_storage_configs(
        self,
        res: "bs_td.ListInstanceStorageConfigsResponseTypeDef",
    ) -> "dc_td.ListInstanceStorageConfigsResponse":
        return dc_td.ListInstanceStorageConfigsResponse.make_one(res)

    def list_instances(
        self,
        res: "bs_td.ListInstancesResponseTypeDef",
    ) -> "dc_td.ListInstancesResponse":
        return dc_td.ListInstancesResponse.make_one(res)

    def list_integration_associations(
        self,
        res: "bs_td.ListIntegrationAssociationsResponseTypeDef",
    ) -> "dc_td.ListIntegrationAssociationsResponse":
        return dc_td.ListIntegrationAssociationsResponse.make_one(res)

    def list_lambda_functions(
        self,
        res: "bs_td.ListLambdaFunctionsResponseTypeDef",
    ) -> "dc_td.ListLambdaFunctionsResponse":
        return dc_td.ListLambdaFunctionsResponse.make_one(res)

    def list_lex_bots(
        self,
        res: "bs_td.ListLexBotsResponseTypeDef",
    ) -> "dc_td.ListLexBotsResponse":
        return dc_td.ListLexBotsResponse.make_one(res)

    def list_phone_numbers(
        self,
        res: "bs_td.ListPhoneNumbersResponseTypeDef",
    ) -> "dc_td.ListPhoneNumbersResponse":
        return dc_td.ListPhoneNumbersResponse.make_one(res)

    def list_phone_numbers_v2(
        self,
        res: "bs_td.ListPhoneNumbersV2ResponseTypeDef",
    ) -> "dc_td.ListPhoneNumbersV2Response":
        return dc_td.ListPhoneNumbersV2Response.make_one(res)

    def list_predefined_attributes(
        self,
        res: "bs_td.ListPredefinedAttributesResponseTypeDef",
    ) -> "dc_td.ListPredefinedAttributesResponse":
        return dc_td.ListPredefinedAttributesResponse.make_one(res)

    def list_prompts(
        self,
        res: "bs_td.ListPromptsResponseTypeDef",
    ) -> "dc_td.ListPromptsResponse":
        return dc_td.ListPromptsResponse.make_one(res)

    def list_queue_quick_connects(
        self,
        res: "bs_td.ListQueueQuickConnectsResponseTypeDef",
    ) -> "dc_td.ListQueueQuickConnectsResponse":
        return dc_td.ListQueueQuickConnectsResponse.make_one(res)

    def list_queues(
        self,
        res: "bs_td.ListQueuesResponseTypeDef",
    ) -> "dc_td.ListQueuesResponse":
        return dc_td.ListQueuesResponse.make_one(res)

    def list_quick_connects(
        self,
        res: "bs_td.ListQuickConnectsResponseTypeDef",
    ) -> "dc_td.ListQuickConnectsResponse":
        return dc_td.ListQuickConnectsResponse.make_one(res)

    def list_realtime_contact_analysis_segments_v2(
        self,
        res: "bs_td.ListRealtimeContactAnalysisSegmentsV2ResponseTypeDef",
    ) -> "dc_td.ListRealtimeContactAnalysisSegmentsV2Response":
        return dc_td.ListRealtimeContactAnalysisSegmentsV2Response.make_one(res)

    def list_routing_profile_queues(
        self,
        res: "bs_td.ListRoutingProfileQueuesResponseTypeDef",
    ) -> "dc_td.ListRoutingProfileQueuesResponse":
        return dc_td.ListRoutingProfileQueuesResponse.make_one(res)

    def list_routing_profiles(
        self,
        res: "bs_td.ListRoutingProfilesResponseTypeDef",
    ) -> "dc_td.ListRoutingProfilesResponse":
        return dc_td.ListRoutingProfilesResponse.make_one(res)

    def list_rules(
        self,
        res: "bs_td.ListRulesResponseTypeDef",
    ) -> "dc_td.ListRulesResponse":
        return dc_td.ListRulesResponse.make_one(res)

    def list_security_keys(
        self,
        res: "bs_td.ListSecurityKeysResponseTypeDef",
    ) -> "dc_td.ListSecurityKeysResponse":
        return dc_td.ListSecurityKeysResponse.make_one(res)

    def list_security_profile_applications(
        self,
        res: "bs_td.ListSecurityProfileApplicationsResponseTypeDef",
    ) -> "dc_td.ListSecurityProfileApplicationsResponse":
        return dc_td.ListSecurityProfileApplicationsResponse.make_one(res)

    def list_security_profile_permissions(
        self,
        res: "bs_td.ListSecurityProfilePermissionsResponseTypeDef",
    ) -> "dc_td.ListSecurityProfilePermissionsResponse":
        return dc_td.ListSecurityProfilePermissionsResponse.make_one(res)

    def list_security_profiles(
        self,
        res: "bs_td.ListSecurityProfilesResponseTypeDef",
    ) -> "dc_td.ListSecurityProfilesResponse":
        return dc_td.ListSecurityProfilesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_task_templates(
        self,
        res: "bs_td.ListTaskTemplatesResponseTypeDef",
    ) -> "dc_td.ListTaskTemplatesResponse":
        return dc_td.ListTaskTemplatesResponse.make_one(res)

    def list_traffic_distribution_group_users(
        self,
        res: "bs_td.ListTrafficDistributionGroupUsersResponseTypeDef",
    ) -> "dc_td.ListTrafficDistributionGroupUsersResponse":
        return dc_td.ListTrafficDistributionGroupUsersResponse.make_one(res)

    def list_traffic_distribution_groups(
        self,
        res: "bs_td.ListTrafficDistributionGroupsResponseTypeDef",
    ) -> "dc_td.ListTrafficDistributionGroupsResponse":
        return dc_td.ListTrafficDistributionGroupsResponse.make_one(res)

    def list_use_cases(
        self,
        res: "bs_td.ListUseCasesResponseTypeDef",
    ) -> "dc_td.ListUseCasesResponse":
        return dc_td.ListUseCasesResponse.make_one(res)

    def list_user_hierarchy_groups(
        self,
        res: "bs_td.ListUserHierarchyGroupsResponseTypeDef",
    ) -> "dc_td.ListUserHierarchyGroupsResponse":
        return dc_td.ListUserHierarchyGroupsResponse.make_one(res)

    def list_user_proficiencies(
        self,
        res: "bs_td.ListUserProficienciesResponseTypeDef",
    ) -> "dc_td.ListUserProficienciesResponse":
        return dc_td.ListUserProficienciesResponse.make_one(res)

    def list_users(
        self,
        res: "bs_td.ListUsersResponseTypeDef",
    ) -> "dc_td.ListUsersResponse":
        return dc_td.ListUsersResponse.make_one(res)

    def list_view_versions(
        self,
        res: "bs_td.ListViewVersionsResponseTypeDef",
    ) -> "dc_td.ListViewVersionsResponse":
        return dc_td.ListViewVersionsResponse.make_one(res)

    def list_views(
        self,
        res: "bs_td.ListViewsResponseTypeDef",
    ) -> "dc_td.ListViewsResponse":
        return dc_td.ListViewsResponse.make_one(res)

    def monitor_contact(
        self,
        res: "bs_td.MonitorContactResponseTypeDef",
    ) -> "dc_td.MonitorContactResponse":
        return dc_td.MonitorContactResponse.make_one(res)

    def release_phone_number(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def replicate_instance(
        self,
        res: "bs_td.ReplicateInstanceResponseTypeDef",
    ) -> "dc_td.ReplicateInstanceResponse":
        return dc_td.ReplicateInstanceResponse.make_one(res)

    def search_agent_statuses(
        self,
        res: "bs_td.SearchAgentStatusesResponseTypeDef",
    ) -> "dc_td.SearchAgentStatusesResponse":
        return dc_td.SearchAgentStatusesResponse.make_one(res)

    def search_available_phone_numbers(
        self,
        res: "bs_td.SearchAvailablePhoneNumbersResponseTypeDef",
    ) -> "dc_td.SearchAvailablePhoneNumbersResponse":
        return dc_td.SearchAvailablePhoneNumbersResponse.make_one(res)

    def search_contact_flow_modules(
        self,
        res: "bs_td.SearchContactFlowModulesResponseTypeDef",
    ) -> "dc_td.SearchContactFlowModulesResponse":
        return dc_td.SearchContactFlowModulesResponse.make_one(res)

    def search_contact_flows(
        self,
        res: "bs_td.SearchContactFlowsResponseTypeDef",
    ) -> "dc_td.SearchContactFlowsResponse":
        return dc_td.SearchContactFlowsResponse.make_one(res)

    def search_contacts(
        self,
        res: "bs_td.SearchContactsResponseTypeDef",
    ) -> "dc_td.SearchContactsResponse":
        return dc_td.SearchContactsResponse.make_one(res)

    def search_email_addresses(
        self,
        res: "bs_td.SearchEmailAddressesResponseTypeDef",
    ) -> "dc_td.SearchEmailAddressesResponse":
        return dc_td.SearchEmailAddressesResponse.make_one(res)

    def search_hours_of_operation_overrides(
        self,
        res: "bs_td.SearchHoursOfOperationOverridesResponseTypeDef",
    ) -> "dc_td.SearchHoursOfOperationOverridesResponse":
        return dc_td.SearchHoursOfOperationOverridesResponse.make_one(res)

    def search_hours_of_operations(
        self,
        res: "bs_td.SearchHoursOfOperationsResponseTypeDef",
    ) -> "dc_td.SearchHoursOfOperationsResponse":
        return dc_td.SearchHoursOfOperationsResponse.make_one(res)

    def search_predefined_attributes(
        self,
        res: "bs_td.SearchPredefinedAttributesResponseTypeDef",
    ) -> "dc_td.SearchPredefinedAttributesResponse":
        return dc_td.SearchPredefinedAttributesResponse.make_one(res)

    def search_prompts(
        self,
        res: "bs_td.SearchPromptsResponseTypeDef",
    ) -> "dc_td.SearchPromptsResponse":
        return dc_td.SearchPromptsResponse.make_one(res)

    def search_queues(
        self,
        res: "bs_td.SearchQueuesResponseTypeDef",
    ) -> "dc_td.SearchQueuesResponse":
        return dc_td.SearchQueuesResponse.make_one(res)

    def search_quick_connects(
        self,
        res: "bs_td.SearchQuickConnectsResponseTypeDef",
    ) -> "dc_td.SearchQuickConnectsResponse":
        return dc_td.SearchQuickConnectsResponse.make_one(res)

    def search_resource_tags(
        self,
        res: "bs_td.SearchResourceTagsResponseTypeDef",
    ) -> "dc_td.SearchResourceTagsResponse":
        return dc_td.SearchResourceTagsResponse.make_one(res)

    def search_routing_profiles(
        self,
        res: "bs_td.SearchRoutingProfilesResponseTypeDef",
    ) -> "dc_td.SearchRoutingProfilesResponse":
        return dc_td.SearchRoutingProfilesResponse.make_one(res)

    def search_security_profiles(
        self,
        res: "bs_td.SearchSecurityProfilesResponseTypeDef",
    ) -> "dc_td.SearchSecurityProfilesResponse":
        return dc_td.SearchSecurityProfilesResponse.make_one(res)

    def search_user_hierarchy_groups(
        self,
        res: "bs_td.SearchUserHierarchyGroupsResponseTypeDef",
    ) -> "dc_td.SearchUserHierarchyGroupsResponse":
        return dc_td.SearchUserHierarchyGroupsResponse.make_one(res)

    def search_users(
        self,
        res: "bs_td.SearchUsersResponseTypeDef",
    ) -> "dc_td.SearchUsersResponse":
        return dc_td.SearchUsersResponse.make_one(res)

    def search_vocabularies(
        self,
        res: "bs_td.SearchVocabulariesResponseTypeDef",
    ) -> "dc_td.SearchVocabulariesResponse":
        return dc_td.SearchVocabulariesResponse.make_one(res)

    def send_chat_integration_event(
        self,
        res: "bs_td.SendChatIntegrationEventResponseTypeDef",
    ) -> "dc_td.SendChatIntegrationEventResponse":
        return dc_td.SendChatIntegrationEventResponse.make_one(res)

    def start_attached_file_upload(
        self,
        res: "bs_td.StartAttachedFileUploadResponseTypeDef",
    ) -> "dc_td.StartAttachedFileUploadResponse":
        return dc_td.StartAttachedFileUploadResponse.make_one(res)

    def start_chat_contact(
        self,
        res: "bs_td.StartChatContactResponseTypeDef",
    ) -> "dc_td.StartChatContactResponse":
        return dc_td.StartChatContactResponse.make_one(res)

    def start_contact_evaluation(
        self,
        res: "bs_td.StartContactEvaluationResponseTypeDef",
    ) -> "dc_td.StartContactEvaluationResponse":
        return dc_td.StartContactEvaluationResponse.make_one(res)

    def start_contact_streaming(
        self,
        res: "bs_td.StartContactStreamingResponseTypeDef",
    ) -> "dc_td.StartContactStreamingResponse":
        return dc_td.StartContactStreamingResponse.make_one(res)

    def start_email_contact(
        self,
        res: "bs_td.StartEmailContactResponseTypeDef",
    ) -> "dc_td.StartEmailContactResponse":
        return dc_td.StartEmailContactResponse.make_one(res)

    def start_outbound_chat_contact(
        self,
        res: "bs_td.StartOutboundChatContactResponseTypeDef",
    ) -> "dc_td.StartOutboundChatContactResponse":
        return dc_td.StartOutboundChatContactResponse.make_one(res)

    def start_outbound_email_contact(
        self,
        res: "bs_td.StartOutboundEmailContactResponseTypeDef",
    ) -> "dc_td.StartOutboundEmailContactResponse":
        return dc_td.StartOutboundEmailContactResponse.make_one(res)

    def start_outbound_voice_contact(
        self,
        res: "bs_td.StartOutboundVoiceContactResponseTypeDef",
    ) -> "dc_td.StartOutboundVoiceContactResponse":
        return dc_td.StartOutboundVoiceContactResponse.make_one(res)

    def start_task_contact(
        self,
        res: "bs_td.StartTaskContactResponseTypeDef",
    ) -> "dc_td.StartTaskContactResponse":
        return dc_td.StartTaskContactResponse.make_one(res)

    def start_web_rtc_contact(
        self,
        res: "bs_td.StartWebRTCContactResponseTypeDef",
    ) -> "dc_td.StartWebRTCContactResponse":
        return dc_td.StartWebRTCContactResponse.make_one(res)

    def submit_contact_evaluation(
        self,
        res: "bs_td.SubmitContactEvaluationResponseTypeDef",
    ) -> "dc_td.SubmitContactEvaluationResponse":
        return dc_td.SubmitContactEvaluationResponse.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def transfer_contact(
        self,
        res: "bs_td.TransferContactResponseTypeDef",
    ) -> "dc_td.TransferContactResponse":
        return dc_td.TransferContactResponse.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_agent_status(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_authentication_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_contact_evaluation(
        self,
        res: "bs_td.UpdateContactEvaluationResponseTypeDef",
    ) -> "dc_td.UpdateContactEvaluationResponse":
        return dc_td.UpdateContactEvaluationResponse.make_one(res)

    def update_email_address_metadata(
        self,
        res: "bs_td.UpdateEmailAddressMetadataResponseTypeDef",
    ) -> "dc_td.UpdateEmailAddressMetadataResponse":
        return dc_td.UpdateEmailAddressMetadataResponse.make_one(res)

    def update_evaluation_form(
        self,
        res: "bs_td.UpdateEvaluationFormResponseTypeDef",
    ) -> "dc_td.UpdateEvaluationFormResponse":
        return dc_td.UpdateEvaluationFormResponse.make_one(res)

    def update_hours_of_operation(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_hours_of_operation_override(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_instance_attribute(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_instance_storage_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_phone_number(
        self,
        res: "bs_td.UpdatePhoneNumberResponseTypeDef",
    ) -> "dc_td.UpdatePhoneNumberResponse":
        return dc_td.UpdatePhoneNumberResponse.make_one(res)

    def update_phone_number_metadata(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_predefined_attribute(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_prompt(
        self,
        res: "bs_td.UpdatePromptResponseTypeDef",
    ) -> "dc_td.UpdatePromptResponse":
        return dc_td.UpdatePromptResponse.make_one(res)

    def update_queue_hours_of_operation(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_queue_max_contacts(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_queue_name(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_queue_outbound_caller_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_queue_outbound_email_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_queue_status(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_quick_connect_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_quick_connect_name(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_routing_profile_agent_availability_timer(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_routing_profile_concurrency(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_routing_profile_default_outbound_queue(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_routing_profile_name(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_routing_profile_queues(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_rule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_security_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_task_template(
        self,
        res: "bs_td.UpdateTaskTemplateResponseTypeDef",
    ) -> "dc_td.UpdateTaskTemplateResponse":
        return dc_td.UpdateTaskTemplateResponse.make_one(res)

    def update_user_hierarchy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_user_hierarchy_group_name(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_user_hierarchy_structure(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_user_identity_info(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_user_phone_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_user_proficiencies(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_user_routing_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_user_security_profiles(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_view_content(
        self,
        res: "bs_td.UpdateViewContentResponseTypeDef",
    ) -> "dc_td.UpdateViewContentResponse":
        return dc_td.UpdateViewContentResponse.make_one(res)


connect_caster = CONNECTCaster()
