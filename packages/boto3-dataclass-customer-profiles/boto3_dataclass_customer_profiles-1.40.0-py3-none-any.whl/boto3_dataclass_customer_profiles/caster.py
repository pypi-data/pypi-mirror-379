# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_customer_profiles import type_defs as bs_td


class CUSTOMER_PROFILESCaster:

    def add_profile_key(
        self,
        res: "bs_td.AddProfileKeyResponseTypeDef",
    ) -> "dc_td.AddProfileKeyResponse":
        return dc_td.AddProfileKeyResponse.make_one(res)

    def batch_get_calculated_attribute_for_profile(
        self,
        res: "bs_td.BatchGetCalculatedAttributeForProfileResponseTypeDef",
    ) -> "dc_td.BatchGetCalculatedAttributeForProfileResponse":
        return dc_td.BatchGetCalculatedAttributeForProfileResponse.make_one(res)

    def batch_get_profile(
        self,
        res: "bs_td.BatchGetProfileResponseTypeDef",
    ) -> "dc_td.BatchGetProfileResponse":
        return dc_td.BatchGetProfileResponse.make_one(res)

    def create_calculated_attribute_definition(
        self,
        res: "bs_td.CreateCalculatedAttributeDefinitionResponseTypeDef",
    ) -> "dc_td.CreateCalculatedAttributeDefinitionResponse":
        return dc_td.CreateCalculatedAttributeDefinitionResponse.make_one(res)

    def create_domain(
        self,
        res: "bs_td.CreateDomainResponseTypeDef",
    ) -> "dc_td.CreateDomainResponse":
        return dc_td.CreateDomainResponse.make_one(res)

    def create_domain_layout(
        self,
        res: "bs_td.CreateDomainLayoutResponseTypeDef",
    ) -> "dc_td.CreateDomainLayoutResponse":
        return dc_td.CreateDomainLayoutResponse.make_one(res)

    def create_event_stream(
        self,
        res: "bs_td.CreateEventStreamResponseTypeDef",
    ) -> "dc_td.CreateEventStreamResponse":
        return dc_td.CreateEventStreamResponse.make_one(res)

    def create_event_trigger(
        self,
        res: "bs_td.CreateEventTriggerResponseTypeDef",
    ) -> "dc_td.CreateEventTriggerResponse":
        return dc_td.CreateEventTriggerResponse.make_one(res)

    def create_integration_workflow(
        self,
        res: "bs_td.CreateIntegrationWorkflowResponseTypeDef",
    ) -> "dc_td.CreateIntegrationWorkflowResponse":
        return dc_td.CreateIntegrationWorkflowResponse.make_one(res)

    def create_profile(
        self,
        res: "bs_td.CreateProfileResponseTypeDef",
    ) -> "dc_td.CreateProfileResponse":
        return dc_td.CreateProfileResponse.make_one(res)

    def create_segment_definition(
        self,
        res: "bs_td.CreateSegmentDefinitionResponseTypeDef",
    ) -> "dc_td.CreateSegmentDefinitionResponse":
        return dc_td.CreateSegmentDefinitionResponse.make_one(res)

    def create_segment_estimate(
        self,
        res: "bs_td.CreateSegmentEstimateResponseTypeDef",
    ) -> "dc_td.CreateSegmentEstimateResponse":
        return dc_td.CreateSegmentEstimateResponse.make_one(res)

    def create_segment_snapshot(
        self,
        res: "bs_td.CreateSegmentSnapshotResponseTypeDef",
    ) -> "dc_td.CreateSegmentSnapshotResponse":
        return dc_td.CreateSegmentSnapshotResponse.make_one(res)

    def create_upload_job(
        self,
        res: "bs_td.CreateUploadJobResponseTypeDef",
    ) -> "dc_td.CreateUploadJobResponse":
        return dc_td.CreateUploadJobResponse.make_one(res)

    def delete_domain(
        self,
        res: "bs_td.DeleteDomainResponseTypeDef",
    ) -> "dc_td.DeleteDomainResponse":
        return dc_td.DeleteDomainResponse.make_one(res)

    def delete_domain_layout(
        self,
        res: "bs_td.DeleteDomainLayoutResponseTypeDef",
    ) -> "dc_td.DeleteDomainLayoutResponse":
        return dc_td.DeleteDomainLayoutResponse.make_one(res)

    def delete_event_trigger(
        self,
        res: "bs_td.DeleteEventTriggerResponseTypeDef",
    ) -> "dc_td.DeleteEventTriggerResponse":
        return dc_td.DeleteEventTriggerResponse.make_one(res)

    def delete_integration(
        self,
        res: "bs_td.DeleteIntegrationResponseTypeDef",
    ) -> "dc_td.DeleteIntegrationResponse":
        return dc_td.DeleteIntegrationResponse.make_one(res)

    def delete_profile(
        self,
        res: "bs_td.DeleteProfileResponseTypeDef",
    ) -> "dc_td.DeleteProfileResponse":
        return dc_td.DeleteProfileResponse.make_one(res)

    def delete_profile_key(
        self,
        res: "bs_td.DeleteProfileKeyResponseTypeDef",
    ) -> "dc_td.DeleteProfileKeyResponse":
        return dc_td.DeleteProfileKeyResponse.make_one(res)

    def delete_profile_object(
        self,
        res: "bs_td.DeleteProfileObjectResponseTypeDef",
    ) -> "dc_td.DeleteProfileObjectResponse":
        return dc_td.DeleteProfileObjectResponse.make_one(res)

    def delete_profile_object_type(
        self,
        res: "bs_td.DeleteProfileObjectTypeResponseTypeDef",
    ) -> "dc_td.DeleteProfileObjectTypeResponse":
        return dc_td.DeleteProfileObjectTypeResponse.make_one(res)

    def delete_segment_definition(
        self,
        res: "bs_td.DeleteSegmentDefinitionResponseTypeDef",
    ) -> "dc_td.DeleteSegmentDefinitionResponse":
        return dc_td.DeleteSegmentDefinitionResponse.make_one(res)

    def detect_profile_object_type(
        self,
        res: "bs_td.DetectProfileObjectTypeResponseTypeDef",
    ) -> "dc_td.DetectProfileObjectTypeResponse":
        return dc_td.DetectProfileObjectTypeResponse.make_one(res)

    def get_auto_merging_preview(
        self,
        res: "bs_td.GetAutoMergingPreviewResponseTypeDef",
    ) -> "dc_td.GetAutoMergingPreviewResponse":
        return dc_td.GetAutoMergingPreviewResponse.make_one(res)

    def get_calculated_attribute_definition(
        self,
        res: "bs_td.GetCalculatedAttributeDefinitionResponseTypeDef",
    ) -> "dc_td.GetCalculatedAttributeDefinitionResponse":
        return dc_td.GetCalculatedAttributeDefinitionResponse.make_one(res)

    def get_calculated_attribute_for_profile(
        self,
        res: "bs_td.GetCalculatedAttributeForProfileResponseTypeDef",
    ) -> "dc_td.GetCalculatedAttributeForProfileResponse":
        return dc_td.GetCalculatedAttributeForProfileResponse.make_one(res)

    def get_domain(
        self,
        res: "bs_td.GetDomainResponseTypeDef",
    ) -> "dc_td.GetDomainResponse":
        return dc_td.GetDomainResponse.make_one(res)

    def get_domain_layout(
        self,
        res: "bs_td.GetDomainLayoutResponseTypeDef",
    ) -> "dc_td.GetDomainLayoutResponse":
        return dc_td.GetDomainLayoutResponse.make_one(res)

    def get_event_stream(
        self,
        res: "bs_td.GetEventStreamResponseTypeDef",
    ) -> "dc_td.GetEventStreamResponse":
        return dc_td.GetEventStreamResponse.make_one(res)

    def get_event_trigger(
        self,
        res: "bs_td.GetEventTriggerResponseTypeDef",
    ) -> "dc_td.GetEventTriggerResponse":
        return dc_td.GetEventTriggerResponse.make_one(res)

    def get_identity_resolution_job(
        self,
        res: "bs_td.GetIdentityResolutionJobResponseTypeDef",
    ) -> "dc_td.GetIdentityResolutionJobResponse":
        return dc_td.GetIdentityResolutionJobResponse.make_one(res)

    def get_integration(
        self,
        res: "bs_td.GetIntegrationResponseTypeDef",
    ) -> "dc_td.GetIntegrationResponse":
        return dc_td.GetIntegrationResponse.make_one(res)

    def get_matches(
        self,
        res: "bs_td.GetMatchesResponseTypeDef",
    ) -> "dc_td.GetMatchesResponse":
        return dc_td.GetMatchesResponse.make_one(res)

    def get_profile_object_type(
        self,
        res: "bs_td.GetProfileObjectTypeResponseTypeDef",
    ) -> "dc_td.GetProfileObjectTypeResponse":
        return dc_td.GetProfileObjectTypeResponse.make_one(res)

    def get_profile_object_type_template(
        self,
        res: "bs_td.GetProfileObjectTypeTemplateResponseTypeDef",
    ) -> "dc_td.GetProfileObjectTypeTemplateResponse":
        return dc_td.GetProfileObjectTypeTemplateResponse.make_one(res)

    def get_segment_definition(
        self,
        res: "bs_td.GetSegmentDefinitionResponseTypeDef",
    ) -> "dc_td.GetSegmentDefinitionResponse":
        return dc_td.GetSegmentDefinitionResponse.make_one(res)

    def get_segment_estimate(
        self,
        res: "bs_td.GetSegmentEstimateResponseTypeDef",
    ) -> "dc_td.GetSegmentEstimateResponse":
        return dc_td.GetSegmentEstimateResponse.make_one(res)

    def get_segment_membership(
        self,
        res: "bs_td.GetSegmentMembershipResponseTypeDef",
    ) -> "dc_td.GetSegmentMembershipResponse":
        return dc_td.GetSegmentMembershipResponse.make_one(res)

    def get_segment_snapshot(
        self,
        res: "bs_td.GetSegmentSnapshotResponseTypeDef",
    ) -> "dc_td.GetSegmentSnapshotResponse":
        return dc_td.GetSegmentSnapshotResponse.make_one(res)

    def get_similar_profiles(
        self,
        res: "bs_td.GetSimilarProfilesResponseTypeDef",
    ) -> "dc_td.GetSimilarProfilesResponse":
        return dc_td.GetSimilarProfilesResponse.make_one(res)

    def get_upload_job(
        self,
        res: "bs_td.GetUploadJobResponseTypeDef",
    ) -> "dc_td.GetUploadJobResponse":
        return dc_td.GetUploadJobResponse.make_one(res)

    def get_upload_job_path(
        self,
        res: "bs_td.GetUploadJobPathResponseTypeDef",
    ) -> "dc_td.GetUploadJobPathResponse":
        return dc_td.GetUploadJobPathResponse.make_one(res)

    def get_workflow(
        self,
        res: "bs_td.GetWorkflowResponseTypeDef",
    ) -> "dc_td.GetWorkflowResponse":
        return dc_td.GetWorkflowResponse.make_one(res)

    def get_workflow_steps(
        self,
        res: "bs_td.GetWorkflowStepsResponseTypeDef",
    ) -> "dc_td.GetWorkflowStepsResponse":
        return dc_td.GetWorkflowStepsResponse.make_one(res)

    def list_account_integrations(
        self,
        res: "bs_td.ListAccountIntegrationsResponseTypeDef",
    ) -> "dc_td.ListAccountIntegrationsResponse":
        return dc_td.ListAccountIntegrationsResponse.make_one(res)

    def list_calculated_attribute_definitions(
        self,
        res: "bs_td.ListCalculatedAttributeDefinitionsResponseTypeDef",
    ) -> "dc_td.ListCalculatedAttributeDefinitionsResponse":
        return dc_td.ListCalculatedAttributeDefinitionsResponse.make_one(res)

    def list_calculated_attributes_for_profile(
        self,
        res: "bs_td.ListCalculatedAttributesForProfileResponseTypeDef",
    ) -> "dc_td.ListCalculatedAttributesForProfileResponse":
        return dc_td.ListCalculatedAttributesForProfileResponse.make_one(res)

    def list_domain_layouts(
        self,
        res: "bs_td.ListDomainLayoutsResponseTypeDef",
    ) -> "dc_td.ListDomainLayoutsResponse":
        return dc_td.ListDomainLayoutsResponse.make_one(res)

    def list_domains(
        self,
        res: "bs_td.ListDomainsResponseTypeDef",
    ) -> "dc_td.ListDomainsResponse":
        return dc_td.ListDomainsResponse.make_one(res)

    def list_event_streams(
        self,
        res: "bs_td.ListEventStreamsResponseTypeDef",
    ) -> "dc_td.ListEventStreamsResponse":
        return dc_td.ListEventStreamsResponse.make_one(res)

    def list_event_triggers(
        self,
        res: "bs_td.ListEventTriggersResponseTypeDef",
    ) -> "dc_td.ListEventTriggersResponse":
        return dc_td.ListEventTriggersResponse.make_one(res)

    def list_identity_resolution_jobs(
        self,
        res: "bs_td.ListIdentityResolutionJobsResponseTypeDef",
    ) -> "dc_td.ListIdentityResolutionJobsResponse":
        return dc_td.ListIdentityResolutionJobsResponse.make_one(res)

    def list_integrations(
        self,
        res: "bs_td.ListIntegrationsResponseTypeDef",
    ) -> "dc_td.ListIntegrationsResponse":
        return dc_td.ListIntegrationsResponse.make_one(res)

    def list_object_type_attributes(
        self,
        res: "bs_td.ListObjectTypeAttributesResponseTypeDef",
    ) -> "dc_td.ListObjectTypeAttributesResponse":
        return dc_td.ListObjectTypeAttributesResponse.make_one(res)

    def list_profile_attribute_values(
        self,
        res: "bs_td.ProfileAttributeValuesResponseTypeDef",
    ) -> "dc_td.ProfileAttributeValuesResponse":
        return dc_td.ProfileAttributeValuesResponse.make_one(res)

    def list_profile_object_type_templates(
        self,
        res: "bs_td.ListProfileObjectTypeTemplatesResponseTypeDef",
    ) -> "dc_td.ListProfileObjectTypeTemplatesResponse":
        return dc_td.ListProfileObjectTypeTemplatesResponse.make_one(res)

    def list_profile_object_types(
        self,
        res: "bs_td.ListProfileObjectTypesResponseTypeDef",
    ) -> "dc_td.ListProfileObjectTypesResponse":
        return dc_td.ListProfileObjectTypesResponse.make_one(res)

    def list_profile_objects(
        self,
        res: "bs_td.ListProfileObjectsResponseTypeDef",
    ) -> "dc_td.ListProfileObjectsResponse":
        return dc_td.ListProfileObjectsResponse.make_one(res)

    def list_rule_based_matches(
        self,
        res: "bs_td.ListRuleBasedMatchesResponseTypeDef",
    ) -> "dc_td.ListRuleBasedMatchesResponse":
        return dc_td.ListRuleBasedMatchesResponse.make_one(res)

    def list_segment_definitions(
        self,
        res: "bs_td.ListSegmentDefinitionsResponseTypeDef",
    ) -> "dc_td.ListSegmentDefinitionsResponse":
        return dc_td.ListSegmentDefinitionsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_upload_jobs(
        self,
        res: "bs_td.ListUploadJobsResponseTypeDef",
    ) -> "dc_td.ListUploadJobsResponse":
        return dc_td.ListUploadJobsResponse.make_one(res)

    def list_workflows(
        self,
        res: "bs_td.ListWorkflowsResponseTypeDef",
    ) -> "dc_td.ListWorkflowsResponse":
        return dc_td.ListWorkflowsResponse.make_one(res)

    def merge_profiles(
        self,
        res: "bs_td.MergeProfilesResponseTypeDef",
    ) -> "dc_td.MergeProfilesResponse":
        return dc_td.MergeProfilesResponse.make_one(res)

    def put_integration(
        self,
        res: "bs_td.PutIntegrationResponseTypeDef",
    ) -> "dc_td.PutIntegrationResponse":
        return dc_td.PutIntegrationResponse.make_one(res)

    def put_profile_object(
        self,
        res: "bs_td.PutProfileObjectResponseTypeDef",
    ) -> "dc_td.PutProfileObjectResponse":
        return dc_td.PutProfileObjectResponse.make_one(res)

    def put_profile_object_type(
        self,
        res: "bs_td.PutProfileObjectTypeResponseTypeDef",
    ) -> "dc_td.PutProfileObjectTypeResponse":
        return dc_td.PutProfileObjectTypeResponse.make_one(res)

    def search_profiles(
        self,
        res: "bs_td.SearchProfilesResponseTypeDef",
    ) -> "dc_td.SearchProfilesResponse":
        return dc_td.SearchProfilesResponse.make_one(res)

    def update_calculated_attribute_definition(
        self,
        res: "bs_td.UpdateCalculatedAttributeDefinitionResponseTypeDef",
    ) -> "dc_td.UpdateCalculatedAttributeDefinitionResponse":
        return dc_td.UpdateCalculatedAttributeDefinitionResponse.make_one(res)

    def update_domain(
        self,
        res: "bs_td.UpdateDomainResponseTypeDef",
    ) -> "dc_td.UpdateDomainResponse":
        return dc_td.UpdateDomainResponse.make_one(res)

    def update_domain_layout(
        self,
        res: "bs_td.UpdateDomainLayoutResponseTypeDef",
    ) -> "dc_td.UpdateDomainLayoutResponse":
        return dc_td.UpdateDomainLayoutResponse.make_one(res)

    def update_event_trigger(
        self,
        res: "bs_td.UpdateEventTriggerResponseTypeDef",
    ) -> "dc_td.UpdateEventTriggerResponse":
        return dc_td.UpdateEventTriggerResponse.make_one(res)

    def update_profile(
        self,
        res: "bs_td.UpdateProfileResponseTypeDef",
    ) -> "dc_td.UpdateProfileResponse":
        return dc_td.UpdateProfileResponse.make_one(res)


customer_profiles_caster = CUSTOMER_PROFILESCaster()
