# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_chime_sdk_voice import type_defs as bs_td


class CHIME_SDK_VOICECaster:

    def associate_phone_numbers_with_voice_connector(
        self,
        res: "bs_td.AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef",
    ) -> "dc_td.AssociatePhoneNumbersWithVoiceConnectorResponse":
        return dc_td.AssociatePhoneNumbersWithVoiceConnectorResponse.make_one(res)

    def associate_phone_numbers_with_voice_connector_group(
        self,
        res: "bs_td.AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef",
    ) -> "dc_td.AssociatePhoneNumbersWithVoiceConnectorGroupResponse":
        return dc_td.AssociatePhoneNumbersWithVoiceConnectorGroupResponse.make_one(res)

    def batch_delete_phone_number(
        self,
        res: "bs_td.BatchDeletePhoneNumberResponseTypeDef",
    ) -> "dc_td.BatchDeletePhoneNumberResponse":
        return dc_td.BatchDeletePhoneNumberResponse.make_one(res)

    def batch_update_phone_number(
        self,
        res: "bs_td.BatchUpdatePhoneNumberResponseTypeDef",
    ) -> "dc_td.BatchUpdatePhoneNumberResponse":
        return dc_td.BatchUpdatePhoneNumberResponse.make_one(res)

    def create_phone_number_order(
        self,
        res: "bs_td.CreatePhoneNumberOrderResponseTypeDef",
    ) -> "dc_td.CreatePhoneNumberOrderResponse":
        return dc_td.CreatePhoneNumberOrderResponse.make_one(res)

    def create_proxy_session(
        self,
        res: "bs_td.CreateProxySessionResponseTypeDef",
    ) -> "dc_td.CreateProxySessionResponse":
        return dc_td.CreateProxySessionResponse.make_one(res)

    def create_sip_media_application(
        self,
        res: "bs_td.CreateSipMediaApplicationResponseTypeDef",
    ) -> "dc_td.CreateSipMediaApplicationResponse":
        return dc_td.CreateSipMediaApplicationResponse.make_one(res)

    def create_sip_media_application_call(
        self,
        res: "bs_td.CreateSipMediaApplicationCallResponseTypeDef",
    ) -> "dc_td.CreateSipMediaApplicationCallResponse":
        return dc_td.CreateSipMediaApplicationCallResponse.make_one(res)

    def create_sip_rule(
        self,
        res: "bs_td.CreateSipRuleResponseTypeDef",
    ) -> "dc_td.CreateSipRuleResponse":
        return dc_td.CreateSipRuleResponse.make_one(res)

    def create_voice_connector(
        self,
        res: "bs_td.CreateVoiceConnectorResponseTypeDef",
    ) -> "dc_td.CreateVoiceConnectorResponse":
        return dc_td.CreateVoiceConnectorResponse.make_one(res)

    def create_voice_connector_group(
        self,
        res: "bs_td.CreateVoiceConnectorGroupResponseTypeDef",
    ) -> "dc_td.CreateVoiceConnectorGroupResponse":
        return dc_td.CreateVoiceConnectorGroupResponse.make_one(res)

    def create_voice_profile(
        self,
        res: "bs_td.CreateVoiceProfileResponseTypeDef",
    ) -> "dc_td.CreateVoiceProfileResponse":
        return dc_td.CreateVoiceProfileResponse.make_one(res)

    def create_voice_profile_domain(
        self,
        res: "bs_td.CreateVoiceProfileDomainResponseTypeDef",
    ) -> "dc_td.CreateVoiceProfileDomainResponse":
        return dc_td.CreateVoiceProfileDomainResponse.make_one(res)

    def delete_phone_number(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_proxy_session(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_sip_media_application(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_sip_rule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_voice_connector(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_voice_connector_emergency_calling_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_voice_connector_external_systems_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_voice_connector_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_voice_connector_origination(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_voice_connector_proxy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_voice_connector_streaming_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_voice_connector_termination(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_voice_connector_termination_credentials(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_voice_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_voice_profile_domain(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_phone_numbers_from_voice_connector(
        self,
        res: "bs_td.DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef",
    ) -> "dc_td.DisassociatePhoneNumbersFromVoiceConnectorResponse":
        return dc_td.DisassociatePhoneNumbersFromVoiceConnectorResponse.make_one(res)

    def disassociate_phone_numbers_from_voice_connector_group(
        self,
        res: "bs_td.DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef",
    ) -> "dc_td.DisassociatePhoneNumbersFromVoiceConnectorGroupResponse":
        return dc_td.DisassociatePhoneNumbersFromVoiceConnectorGroupResponse.make_one(
            res
        )

    def get_global_settings(
        self,
        res: "bs_td.GetGlobalSettingsResponseTypeDef",
    ) -> "dc_td.GetGlobalSettingsResponse":
        return dc_td.GetGlobalSettingsResponse.make_one(res)

    def get_phone_number(
        self,
        res: "bs_td.GetPhoneNumberResponseTypeDef",
    ) -> "dc_td.GetPhoneNumberResponse":
        return dc_td.GetPhoneNumberResponse.make_one(res)

    def get_phone_number_order(
        self,
        res: "bs_td.GetPhoneNumberOrderResponseTypeDef",
    ) -> "dc_td.GetPhoneNumberOrderResponse":
        return dc_td.GetPhoneNumberOrderResponse.make_one(res)

    def get_phone_number_settings(
        self,
        res: "bs_td.GetPhoneNumberSettingsResponseTypeDef",
    ) -> "dc_td.GetPhoneNumberSettingsResponse":
        return dc_td.GetPhoneNumberSettingsResponse.make_one(res)

    def get_proxy_session(
        self,
        res: "bs_td.GetProxySessionResponseTypeDef",
    ) -> "dc_td.GetProxySessionResponse":
        return dc_td.GetProxySessionResponse.make_one(res)

    def get_sip_media_application(
        self,
        res: "bs_td.GetSipMediaApplicationResponseTypeDef",
    ) -> "dc_td.GetSipMediaApplicationResponse":
        return dc_td.GetSipMediaApplicationResponse.make_one(res)

    def get_sip_media_application_alexa_skill_configuration(
        self,
        res: "bs_td.GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef",
    ) -> "dc_td.GetSipMediaApplicationAlexaSkillConfigurationResponse":
        return dc_td.GetSipMediaApplicationAlexaSkillConfigurationResponse.make_one(res)

    def get_sip_media_application_logging_configuration(
        self,
        res: "bs_td.GetSipMediaApplicationLoggingConfigurationResponseTypeDef",
    ) -> "dc_td.GetSipMediaApplicationLoggingConfigurationResponse":
        return dc_td.GetSipMediaApplicationLoggingConfigurationResponse.make_one(res)

    def get_sip_rule(
        self,
        res: "bs_td.GetSipRuleResponseTypeDef",
    ) -> "dc_td.GetSipRuleResponse":
        return dc_td.GetSipRuleResponse.make_one(res)

    def get_speaker_search_task(
        self,
        res: "bs_td.GetSpeakerSearchTaskResponseTypeDef",
    ) -> "dc_td.GetSpeakerSearchTaskResponse":
        return dc_td.GetSpeakerSearchTaskResponse.make_one(res)

    def get_voice_connector(
        self,
        res: "bs_td.GetVoiceConnectorResponseTypeDef",
    ) -> "dc_td.GetVoiceConnectorResponse":
        return dc_td.GetVoiceConnectorResponse.make_one(res)

    def get_voice_connector_emergency_calling_configuration(
        self,
        res: "bs_td.GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    ) -> "dc_td.GetVoiceConnectorEmergencyCallingConfigurationResponse":
        return dc_td.GetVoiceConnectorEmergencyCallingConfigurationResponse.make_one(
            res
        )

    def get_voice_connector_external_systems_configuration(
        self,
        res: "bs_td.GetVoiceConnectorExternalSystemsConfigurationResponseTypeDef",
    ) -> "dc_td.GetVoiceConnectorExternalSystemsConfigurationResponse":
        return dc_td.GetVoiceConnectorExternalSystemsConfigurationResponse.make_one(res)

    def get_voice_connector_group(
        self,
        res: "bs_td.GetVoiceConnectorGroupResponseTypeDef",
    ) -> "dc_td.GetVoiceConnectorGroupResponse":
        return dc_td.GetVoiceConnectorGroupResponse.make_one(res)

    def get_voice_connector_logging_configuration(
        self,
        res: "bs_td.GetVoiceConnectorLoggingConfigurationResponseTypeDef",
    ) -> "dc_td.GetVoiceConnectorLoggingConfigurationResponse":
        return dc_td.GetVoiceConnectorLoggingConfigurationResponse.make_one(res)

    def get_voice_connector_origination(
        self,
        res: "bs_td.GetVoiceConnectorOriginationResponseTypeDef",
    ) -> "dc_td.GetVoiceConnectorOriginationResponse":
        return dc_td.GetVoiceConnectorOriginationResponse.make_one(res)

    def get_voice_connector_proxy(
        self,
        res: "bs_td.GetVoiceConnectorProxyResponseTypeDef",
    ) -> "dc_td.GetVoiceConnectorProxyResponse":
        return dc_td.GetVoiceConnectorProxyResponse.make_one(res)

    def get_voice_connector_streaming_configuration(
        self,
        res: "bs_td.GetVoiceConnectorStreamingConfigurationResponseTypeDef",
    ) -> "dc_td.GetVoiceConnectorStreamingConfigurationResponse":
        return dc_td.GetVoiceConnectorStreamingConfigurationResponse.make_one(res)

    def get_voice_connector_termination(
        self,
        res: "bs_td.GetVoiceConnectorTerminationResponseTypeDef",
    ) -> "dc_td.GetVoiceConnectorTerminationResponse":
        return dc_td.GetVoiceConnectorTerminationResponse.make_one(res)

    def get_voice_connector_termination_health(
        self,
        res: "bs_td.GetVoiceConnectorTerminationHealthResponseTypeDef",
    ) -> "dc_td.GetVoiceConnectorTerminationHealthResponse":
        return dc_td.GetVoiceConnectorTerminationHealthResponse.make_one(res)

    def get_voice_profile(
        self,
        res: "bs_td.GetVoiceProfileResponseTypeDef",
    ) -> "dc_td.GetVoiceProfileResponse":
        return dc_td.GetVoiceProfileResponse.make_one(res)

    def get_voice_profile_domain(
        self,
        res: "bs_td.GetVoiceProfileDomainResponseTypeDef",
    ) -> "dc_td.GetVoiceProfileDomainResponse":
        return dc_td.GetVoiceProfileDomainResponse.make_one(res)

    def get_voice_tone_analysis_task(
        self,
        res: "bs_td.GetVoiceToneAnalysisTaskResponseTypeDef",
    ) -> "dc_td.GetVoiceToneAnalysisTaskResponse":
        return dc_td.GetVoiceToneAnalysisTaskResponse.make_one(res)

    def list_available_voice_connector_regions(
        self,
        res: "bs_td.ListAvailableVoiceConnectorRegionsResponseTypeDef",
    ) -> "dc_td.ListAvailableVoiceConnectorRegionsResponse":
        return dc_td.ListAvailableVoiceConnectorRegionsResponse.make_one(res)

    def list_phone_number_orders(
        self,
        res: "bs_td.ListPhoneNumberOrdersResponseTypeDef",
    ) -> "dc_td.ListPhoneNumberOrdersResponse":
        return dc_td.ListPhoneNumberOrdersResponse.make_one(res)

    def list_phone_numbers(
        self,
        res: "bs_td.ListPhoneNumbersResponseTypeDef",
    ) -> "dc_td.ListPhoneNumbersResponse":
        return dc_td.ListPhoneNumbersResponse.make_one(res)

    def list_proxy_sessions(
        self,
        res: "bs_td.ListProxySessionsResponseTypeDef",
    ) -> "dc_td.ListProxySessionsResponse":
        return dc_td.ListProxySessionsResponse.make_one(res)

    def list_sip_media_applications(
        self,
        res: "bs_td.ListSipMediaApplicationsResponseTypeDef",
    ) -> "dc_td.ListSipMediaApplicationsResponse":
        return dc_td.ListSipMediaApplicationsResponse.make_one(res)

    def list_sip_rules(
        self,
        res: "bs_td.ListSipRulesResponseTypeDef",
    ) -> "dc_td.ListSipRulesResponse":
        return dc_td.ListSipRulesResponse.make_one(res)

    def list_supported_phone_number_countries(
        self,
        res: "bs_td.ListSupportedPhoneNumberCountriesResponseTypeDef",
    ) -> "dc_td.ListSupportedPhoneNumberCountriesResponse":
        return dc_td.ListSupportedPhoneNumberCountriesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_voice_connector_groups(
        self,
        res: "bs_td.ListVoiceConnectorGroupsResponseTypeDef",
    ) -> "dc_td.ListVoiceConnectorGroupsResponse":
        return dc_td.ListVoiceConnectorGroupsResponse.make_one(res)

    def list_voice_connector_termination_credentials(
        self,
        res: "bs_td.ListVoiceConnectorTerminationCredentialsResponseTypeDef",
    ) -> "dc_td.ListVoiceConnectorTerminationCredentialsResponse":
        return dc_td.ListVoiceConnectorTerminationCredentialsResponse.make_one(res)

    def list_voice_connectors(
        self,
        res: "bs_td.ListVoiceConnectorsResponseTypeDef",
    ) -> "dc_td.ListVoiceConnectorsResponse":
        return dc_td.ListVoiceConnectorsResponse.make_one(res)

    def list_voice_profile_domains(
        self,
        res: "bs_td.ListVoiceProfileDomainsResponseTypeDef",
    ) -> "dc_td.ListVoiceProfileDomainsResponse":
        return dc_td.ListVoiceProfileDomainsResponse.make_one(res)

    def list_voice_profiles(
        self,
        res: "bs_td.ListVoiceProfilesResponseTypeDef",
    ) -> "dc_td.ListVoiceProfilesResponse":
        return dc_td.ListVoiceProfilesResponse.make_one(res)

    def put_sip_media_application_alexa_skill_configuration(
        self,
        res: "bs_td.PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef",
    ) -> "dc_td.PutSipMediaApplicationAlexaSkillConfigurationResponse":
        return dc_td.PutSipMediaApplicationAlexaSkillConfigurationResponse.make_one(res)

    def put_sip_media_application_logging_configuration(
        self,
        res: "bs_td.PutSipMediaApplicationLoggingConfigurationResponseTypeDef",
    ) -> "dc_td.PutSipMediaApplicationLoggingConfigurationResponse":
        return dc_td.PutSipMediaApplicationLoggingConfigurationResponse.make_one(res)

    def put_voice_connector_emergency_calling_configuration(
        self,
        res: "bs_td.PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    ) -> "dc_td.PutVoiceConnectorEmergencyCallingConfigurationResponse":
        return dc_td.PutVoiceConnectorEmergencyCallingConfigurationResponse.make_one(
            res
        )

    def put_voice_connector_external_systems_configuration(
        self,
        res: "bs_td.PutVoiceConnectorExternalSystemsConfigurationResponseTypeDef",
    ) -> "dc_td.PutVoiceConnectorExternalSystemsConfigurationResponse":
        return dc_td.PutVoiceConnectorExternalSystemsConfigurationResponse.make_one(res)

    def put_voice_connector_logging_configuration(
        self,
        res: "bs_td.PutVoiceConnectorLoggingConfigurationResponseTypeDef",
    ) -> "dc_td.PutVoiceConnectorLoggingConfigurationResponse":
        return dc_td.PutVoiceConnectorLoggingConfigurationResponse.make_one(res)

    def put_voice_connector_origination(
        self,
        res: "bs_td.PutVoiceConnectorOriginationResponseTypeDef",
    ) -> "dc_td.PutVoiceConnectorOriginationResponse":
        return dc_td.PutVoiceConnectorOriginationResponse.make_one(res)

    def put_voice_connector_proxy(
        self,
        res: "bs_td.PutVoiceConnectorProxyResponseTypeDef",
    ) -> "dc_td.PutVoiceConnectorProxyResponse":
        return dc_td.PutVoiceConnectorProxyResponse.make_one(res)

    def put_voice_connector_streaming_configuration(
        self,
        res: "bs_td.PutVoiceConnectorStreamingConfigurationResponseTypeDef",
    ) -> "dc_td.PutVoiceConnectorStreamingConfigurationResponse":
        return dc_td.PutVoiceConnectorStreamingConfigurationResponse.make_one(res)

    def put_voice_connector_termination(
        self,
        res: "bs_td.PutVoiceConnectorTerminationResponseTypeDef",
    ) -> "dc_td.PutVoiceConnectorTerminationResponse":
        return dc_td.PutVoiceConnectorTerminationResponse.make_one(res)

    def put_voice_connector_termination_credentials(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def restore_phone_number(
        self,
        res: "bs_td.RestorePhoneNumberResponseTypeDef",
    ) -> "dc_td.RestorePhoneNumberResponse":
        return dc_td.RestorePhoneNumberResponse.make_one(res)

    def search_available_phone_numbers(
        self,
        res: "bs_td.SearchAvailablePhoneNumbersResponseTypeDef",
    ) -> "dc_td.SearchAvailablePhoneNumbersResponse":
        return dc_td.SearchAvailablePhoneNumbersResponse.make_one(res)

    def start_speaker_search_task(
        self,
        res: "bs_td.StartSpeakerSearchTaskResponseTypeDef",
    ) -> "dc_td.StartSpeakerSearchTaskResponse":
        return dc_td.StartSpeakerSearchTaskResponse.make_one(res)

    def start_voice_tone_analysis_task(
        self,
        res: "bs_td.StartVoiceToneAnalysisTaskResponseTypeDef",
    ) -> "dc_td.StartVoiceToneAnalysisTaskResponse":
        return dc_td.StartVoiceToneAnalysisTaskResponse.make_one(res)

    def stop_speaker_search_task(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_voice_tone_analysis_task(
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

    def update_global_settings(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_phone_number(
        self,
        res: "bs_td.UpdatePhoneNumberResponseTypeDef",
    ) -> "dc_td.UpdatePhoneNumberResponse":
        return dc_td.UpdatePhoneNumberResponse.make_one(res)

    def update_phone_number_settings(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_proxy_session(
        self,
        res: "bs_td.UpdateProxySessionResponseTypeDef",
    ) -> "dc_td.UpdateProxySessionResponse":
        return dc_td.UpdateProxySessionResponse.make_one(res)

    def update_sip_media_application(
        self,
        res: "bs_td.UpdateSipMediaApplicationResponseTypeDef",
    ) -> "dc_td.UpdateSipMediaApplicationResponse":
        return dc_td.UpdateSipMediaApplicationResponse.make_one(res)

    def update_sip_media_application_call(
        self,
        res: "bs_td.UpdateSipMediaApplicationCallResponseTypeDef",
    ) -> "dc_td.UpdateSipMediaApplicationCallResponse":
        return dc_td.UpdateSipMediaApplicationCallResponse.make_one(res)

    def update_sip_rule(
        self,
        res: "bs_td.UpdateSipRuleResponseTypeDef",
    ) -> "dc_td.UpdateSipRuleResponse":
        return dc_td.UpdateSipRuleResponse.make_one(res)

    def update_voice_connector(
        self,
        res: "bs_td.UpdateVoiceConnectorResponseTypeDef",
    ) -> "dc_td.UpdateVoiceConnectorResponse":
        return dc_td.UpdateVoiceConnectorResponse.make_one(res)

    def update_voice_connector_group(
        self,
        res: "bs_td.UpdateVoiceConnectorGroupResponseTypeDef",
    ) -> "dc_td.UpdateVoiceConnectorGroupResponse":
        return dc_td.UpdateVoiceConnectorGroupResponse.make_one(res)

    def update_voice_profile(
        self,
        res: "bs_td.UpdateVoiceProfileResponseTypeDef",
    ) -> "dc_td.UpdateVoiceProfileResponse":
        return dc_td.UpdateVoiceProfileResponse.make_one(res)

    def update_voice_profile_domain(
        self,
        res: "bs_td.UpdateVoiceProfileDomainResponseTypeDef",
    ) -> "dc_td.UpdateVoiceProfileDomainResponse":
        return dc_td.UpdateVoiceProfileDomainResponse.make_one(res)

    def validate_e911_address(
        self,
        res: "bs_td.ValidateE911AddressResponseTypeDef",
    ) -> "dc_td.ValidateE911AddressResponse":
        return dc_td.ValidateE911AddressResponse.make_one(res)


chime_sdk_voice_caster = CHIME_SDK_VOICECaster()
