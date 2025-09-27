# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_connectcampaignsv2 import type_defs as bs_td


class CONNECTCAMPAIGNSV2Caster:

    def create_campaign(
        self,
        res: "bs_td.CreateCampaignResponseTypeDef",
    ) -> "dc_td.CreateCampaignResponse":
        return dc_td.CreateCampaignResponse.make_one(res)

    def delete_campaign(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_campaign_channel_subtype_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_campaign_communication_limits(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_campaign_communication_time(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_connect_instance_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_connect_instance_integration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_instance_onboarding_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_campaign(
        self,
        res: "bs_td.DescribeCampaignResponseTypeDef",
    ) -> "dc_td.DescribeCampaignResponse":
        return dc_td.DescribeCampaignResponse.make_one(res)

    def get_campaign_state(
        self,
        res: "bs_td.GetCampaignStateResponseTypeDef",
    ) -> "dc_td.GetCampaignStateResponse":
        return dc_td.GetCampaignStateResponse.make_one(res)

    def get_campaign_state_batch(
        self,
        res: "bs_td.GetCampaignStateBatchResponseTypeDef",
    ) -> "dc_td.GetCampaignStateBatchResponse":
        return dc_td.GetCampaignStateBatchResponse.make_one(res)

    def get_connect_instance_config(
        self,
        res: "bs_td.GetConnectInstanceConfigResponseTypeDef",
    ) -> "dc_td.GetConnectInstanceConfigResponse":
        return dc_td.GetConnectInstanceConfigResponse.make_one(res)

    def get_instance_communication_limits(
        self,
        res: "bs_td.GetInstanceCommunicationLimitsResponseTypeDef",
    ) -> "dc_td.GetInstanceCommunicationLimitsResponse":
        return dc_td.GetInstanceCommunicationLimitsResponse.make_one(res)

    def get_instance_onboarding_job_status(
        self,
        res: "bs_td.GetInstanceOnboardingJobStatusResponseTypeDef",
    ) -> "dc_td.GetInstanceOnboardingJobStatusResponse":
        return dc_td.GetInstanceOnboardingJobStatusResponse.make_one(res)

    def list_campaigns(
        self,
        res: "bs_td.ListCampaignsResponseTypeDef",
    ) -> "dc_td.ListCampaignsResponse":
        return dc_td.ListCampaignsResponse.make_one(res)

    def list_connect_instance_integrations(
        self,
        res: "bs_td.ListConnectInstanceIntegrationsResponseTypeDef",
    ) -> "dc_td.ListConnectInstanceIntegrationsResponse":
        return dc_td.ListConnectInstanceIntegrationsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def pause_campaign(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_connect_instance_integration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_instance_communication_limits(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_outbound_request_batch(
        self,
        res: "bs_td.PutOutboundRequestBatchResponseTypeDef",
    ) -> "dc_td.PutOutboundRequestBatchResponse":
        return dc_td.PutOutboundRequestBatchResponse.make_one(res)

    def put_profile_outbound_request_batch(
        self,
        res: "bs_td.PutProfileOutboundRequestBatchResponseTypeDef",
    ) -> "dc_td.PutProfileOutboundRequestBatchResponse":
        return dc_td.PutProfileOutboundRequestBatchResponse.make_one(res)

    def resume_campaign(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_campaign(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_instance_onboarding_job(
        self,
        res: "bs_td.StartInstanceOnboardingJobResponseTypeDef",
    ) -> "dc_td.StartInstanceOnboardingJobResponse":
        return dc_td.StartInstanceOnboardingJobResponse.make_one(res)

    def stop_campaign(
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

    def update_campaign_channel_subtype_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_campaign_communication_limits(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_campaign_communication_time(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_campaign_flow_association(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_campaign_name(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_campaign_schedule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_campaign_source(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


connectcampaignsv2_caster = CONNECTCAMPAIGNSV2Caster()
