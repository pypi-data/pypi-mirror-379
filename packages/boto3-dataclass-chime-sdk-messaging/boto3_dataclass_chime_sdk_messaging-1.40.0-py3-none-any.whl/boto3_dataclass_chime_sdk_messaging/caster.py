# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_chime_sdk_messaging import type_defs as bs_td


class CHIME_SDK_MESSAGINGCaster:

    def associate_channel_flow(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def batch_create_channel_membership(
        self,
        res: "bs_td.BatchCreateChannelMembershipResponseTypeDef",
    ) -> "dc_td.BatchCreateChannelMembershipResponse":
        return dc_td.BatchCreateChannelMembershipResponse.make_one(res)

    def channel_flow_callback(
        self,
        res: "bs_td.ChannelFlowCallbackResponseTypeDef",
    ) -> "dc_td.ChannelFlowCallbackResponse":
        return dc_td.ChannelFlowCallbackResponse.make_one(res)

    def create_channel(
        self,
        res: "bs_td.CreateChannelResponseTypeDef",
    ) -> "dc_td.CreateChannelResponse":
        return dc_td.CreateChannelResponse.make_one(res)

    def create_channel_ban(
        self,
        res: "bs_td.CreateChannelBanResponseTypeDef",
    ) -> "dc_td.CreateChannelBanResponse":
        return dc_td.CreateChannelBanResponse.make_one(res)

    def create_channel_flow(
        self,
        res: "bs_td.CreateChannelFlowResponseTypeDef",
    ) -> "dc_td.CreateChannelFlowResponse":
        return dc_td.CreateChannelFlowResponse.make_one(res)

    def create_channel_membership(
        self,
        res: "bs_td.CreateChannelMembershipResponseTypeDef",
    ) -> "dc_td.CreateChannelMembershipResponse":
        return dc_td.CreateChannelMembershipResponse.make_one(res)

    def create_channel_moderator(
        self,
        res: "bs_td.CreateChannelModeratorResponseTypeDef",
    ) -> "dc_td.CreateChannelModeratorResponse":
        return dc_td.CreateChannelModeratorResponse.make_one(res)

    def delete_channel(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_channel_ban(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_channel_flow(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_channel_membership(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_channel_message(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_channel_moderator(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_messaging_streaming_configurations(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_channel(
        self,
        res: "bs_td.DescribeChannelResponseTypeDef",
    ) -> "dc_td.DescribeChannelResponse":
        return dc_td.DescribeChannelResponse.make_one(res)

    def describe_channel_ban(
        self,
        res: "bs_td.DescribeChannelBanResponseTypeDef",
    ) -> "dc_td.DescribeChannelBanResponse":
        return dc_td.DescribeChannelBanResponse.make_one(res)

    def describe_channel_flow(
        self,
        res: "bs_td.DescribeChannelFlowResponseTypeDef",
    ) -> "dc_td.DescribeChannelFlowResponse":
        return dc_td.DescribeChannelFlowResponse.make_one(res)

    def describe_channel_membership(
        self,
        res: "bs_td.DescribeChannelMembershipResponseTypeDef",
    ) -> "dc_td.DescribeChannelMembershipResponse":
        return dc_td.DescribeChannelMembershipResponse.make_one(res)

    def describe_channel_membership_for_app_instance_user(
        self,
        res: "bs_td.DescribeChannelMembershipForAppInstanceUserResponseTypeDef",
    ) -> "dc_td.DescribeChannelMembershipForAppInstanceUserResponse":
        return dc_td.DescribeChannelMembershipForAppInstanceUserResponse.make_one(res)

    def describe_channel_moderated_by_app_instance_user(
        self,
        res: "bs_td.DescribeChannelModeratedByAppInstanceUserResponseTypeDef",
    ) -> "dc_td.DescribeChannelModeratedByAppInstanceUserResponse":
        return dc_td.DescribeChannelModeratedByAppInstanceUserResponse.make_one(res)

    def describe_channel_moderator(
        self,
        res: "bs_td.DescribeChannelModeratorResponseTypeDef",
    ) -> "dc_td.DescribeChannelModeratorResponse":
        return dc_td.DescribeChannelModeratorResponse.make_one(res)

    def disassociate_channel_flow(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_channel_membership_preferences(
        self,
        res: "bs_td.GetChannelMembershipPreferencesResponseTypeDef",
    ) -> "dc_td.GetChannelMembershipPreferencesResponse":
        return dc_td.GetChannelMembershipPreferencesResponse.make_one(res)

    def get_channel_message(
        self,
        res: "bs_td.GetChannelMessageResponseTypeDef",
    ) -> "dc_td.GetChannelMessageResponse":
        return dc_td.GetChannelMessageResponse.make_one(res)

    def get_channel_message_status(
        self,
        res: "bs_td.GetChannelMessageStatusResponseTypeDef",
    ) -> "dc_td.GetChannelMessageStatusResponse":
        return dc_td.GetChannelMessageStatusResponse.make_one(res)

    def get_messaging_session_endpoint(
        self,
        res: "bs_td.GetMessagingSessionEndpointResponseTypeDef",
    ) -> "dc_td.GetMessagingSessionEndpointResponse":
        return dc_td.GetMessagingSessionEndpointResponse.make_one(res)

    def get_messaging_streaming_configurations(
        self,
        res: "bs_td.GetMessagingStreamingConfigurationsResponseTypeDef",
    ) -> "dc_td.GetMessagingStreamingConfigurationsResponse":
        return dc_td.GetMessagingStreamingConfigurationsResponse.make_one(res)

    def list_channel_bans(
        self,
        res: "bs_td.ListChannelBansResponseTypeDef",
    ) -> "dc_td.ListChannelBansResponse":
        return dc_td.ListChannelBansResponse.make_one(res)

    def list_channel_flows(
        self,
        res: "bs_td.ListChannelFlowsResponseTypeDef",
    ) -> "dc_td.ListChannelFlowsResponse":
        return dc_td.ListChannelFlowsResponse.make_one(res)

    def list_channel_memberships(
        self,
        res: "bs_td.ListChannelMembershipsResponseTypeDef",
    ) -> "dc_td.ListChannelMembershipsResponse":
        return dc_td.ListChannelMembershipsResponse.make_one(res)

    def list_channel_memberships_for_app_instance_user(
        self,
        res: "bs_td.ListChannelMembershipsForAppInstanceUserResponseTypeDef",
    ) -> "dc_td.ListChannelMembershipsForAppInstanceUserResponse":
        return dc_td.ListChannelMembershipsForAppInstanceUserResponse.make_one(res)

    def list_channel_messages(
        self,
        res: "bs_td.ListChannelMessagesResponseTypeDef",
    ) -> "dc_td.ListChannelMessagesResponse":
        return dc_td.ListChannelMessagesResponse.make_one(res)

    def list_channel_moderators(
        self,
        res: "bs_td.ListChannelModeratorsResponseTypeDef",
    ) -> "dc_td.ListChannelModeratorsResponse":
        return dc_td.ListChannelModeratorsResponse.make_one(res)

    def list_channels(
        self,
        res: "bs_td.ListChannelsResponseTypeDef",
    ) -> "dc_td.ListChannelsResponse":
        return dc_td.ListChannelsResponse.make_one(res)

    def list_channels_associated_with_channel_flow(
        self,
        res: "bs_td.ListChannelsAssociatedWithChannelFlowResponseTypeDef",
    ) -> "dc_td.ListChannelsAssociatedWithChannelFlowResponse":
        return dc_td.ListChannelsAssociatedWithChannelFlowResponse.make_one(res)

    def list_channels_moderated_by_app_instance_user(
        self,
        res: "bs_td.ListChannelsModeratedByAppInstanceUserResponseTypeDef",
    ) -> "dc_td.ListChannelsModeratedByAppInstanceUserResponse":
        return dc_td.ListChannelsModeratedByAppInstanceUserResponse.make_one(res)

    def list_sub_channels(
        self,
        res: "bs_td.ListSubChannelsResponseTypeDef",
    ) -> "dc_td.ListSubChannelsResponse":
        return dc_td.ListSubChannelsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_channel_expiration_settings(
        self,
        res: "bs_td.PutChannelExpirationSettingsResponseTypeDef",
    ) -> "dc_td.PutChannelExpirationSettingsResponse":
        return dc_td.PutChannelExpirationSettingsResponse.make_one(res)

    def put_channel_membership_preferences(
        self,
        res: "bs_td.PutChannelMembershipPreferencesResponseTypeDef",
    ) -> "dc_td.PutChannelMembershipPreferencesResponse":
        return dc_td.PutChannelMembershipPreferencesResponse.make_one(res)

    def put_messaging_streaming_configurations(
        self,
        res: "bs_td.PutMessagingStreamingConfigurationsResponseTypeDef",
    ) -> "dc_td.PutMessagingStreamingConfigurationsResponse":
        return dc_td.PutMessagingStreamingConfigurationsResponse.make_one(res)

    def redact_channel_message(
        self,
        res: "bs_td.RedactChannelMessageResponseTypeDef",
    ) -> "dc_td.RedactChannelMessageResponse":
        return dc_td.RedactChannelMessageResponse.make_one(res)

    def search_channels(
        self,
        res: "bs_td.SearchChannelsResponseTypeDef",
    ) -> "dc_td.SearchChannelsResponse":
        return dc_td.SearchChannelsResponse.make_one(res)

    def send_channel_message(
        self,
        res: "bs_td.SendChannelMessageResponseTypeDef",
    ) -> "dc_td.SendChannelMessageResponse":
        return dc_td.SendChannelMessageResponse.make_one(res)

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

    def update_channel(
        self,
        res: "bs_td.UpdateChannelResponseTypeDef",
    ) -> "dc_td.UpdateChannelResponse":
        return dc_td.UpdateChannelResponse.make_one(res)

    def update_channel_flow(
        self,
        res: "bs_td.UpdateChannelFlowResponseTypeDef",
    ) -> "dc_td.UpdateChannelFlowResponse":
        return dc_td.UpdateChannelFlowResponse.make_one(res)

    def update_channel_message(
        self,
        res: "bs_td.UpdateChannelMessageResponseTypeDef",
    ) -> "dc_td.UpdateChannelMessageResponse":
        return dc_td.UpdateChannelMessageResponse.make_one(res)

    def update_channel_read_marker(
        self,
        res: "bs_td.UpdateChannelReadMarkerResponseTypeDef",
    ) -> "dc_td.UpdateChannelReadMarkerResponse":
        return dc_td.UpdateChannelReadMarkerResponse.make_one(res)


chime_sdk_messaging_caster = CHIME_SDK_MESSAGINGCaster()
