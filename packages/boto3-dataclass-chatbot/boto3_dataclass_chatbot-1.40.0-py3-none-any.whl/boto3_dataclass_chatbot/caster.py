# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_chatbot import type_defs as bs_td


class CHATBOTCaster:

    def create_chime_webhook_configuration(
        self,
        res: "bs_td.CreateChimeWebhookConfigurationResultTypeDef",
    ) -> "dc_td.CreateChimeWebhookConfigurationResult":
        return dc_td.CreateChimeWebhookConfigurationResult.make_one(res)

    def create_custom_action(
        self,
        res: "bs_td.CreateCustomActionResultTypeDef",
    ) -> "dc_td.CreateCustomActionResult":
        return dc_td.CreateCustomActionResult.make_one(res)

    def create_microsoft_teams_channel_configuration(
        self,
        res: "bs_td.CreateTeamsChannelConfigurationResultTypeDef",
    ) -> "dc_td.CreateTeamsChannelConfigurationResult":
        return dc_td.CreateTeamsChannelConfigurationResult.make_one(res)

    def create_slack_channel_configuration(
        self,
        res: "bs_td.CreateSlackChannelConfigurationResultTypeDef",
    ) -> "dc_td.CreateSlackChannelConfigurationResult":
        return dc_td.CreateSlackChannelConfigurationResult.make_one(res)

    def describe_chime_webhook_configurations(
        self,
        res: "bs_td.DescribeChimeWebhookConfigurationsResultTypeDef",
    ) -> "dc_td.DescribeChimeWebhookConfigurationsResult":
        return dc_td.DescribeChimeWebhookConfigurationsResult.make_one(res)

    def describe_slack_channel_configurations(
        self,
        res: "bs_td.DescribeSlackChannelConfigurationsResultTypeDef",
    ) -> "dc_td.DescribeSlackChannelConfigurationsResult":
        return dc_td.DescribeSlackChannelConfigurationsResult.make_one(res)

    def describe_slack_user_identities(
        self,
        res: "bs_td.DescribeSlackUserIdentitiesResultTypeDef",
    ) -> "dc_td.DescribeSlackUserIdentitiesResult":
        return dc_td.DescribeSlackUserIdentitiesResult.make_one(res)

    def describe_slack_workspaces(
        self,
        res: "bs_td.DescribeSlackWorkspacesResultTypeDef",
    ) -> "dc_td.DescribeSlackWorkspacesResult":
        return dc_td.DescribeSlackWorkspacesResult.make_one(res)

    def get_account_preferences(
        self,
        res: "bs_td.GetAccountPreferencesResultTypeDef",
    ) -> "dc_td.GetAccountPreferencesResult":
        return dc_td.GetAccountPreferencesResult.make_one(res)

    def get_custom_action(
        self,
        res: "bs_td.GetCustomActionResultTypeDef",
    ) -> "dc_td.GetCustomActionResult":
        return dc_td.GetCustomActionResult.make_one(res)

    def get_microsoft_teams_channel_configuration(
        self,
        res: "bs_td.GetTeamsChannelConfigurationResultTypeDef",
    ) -> "dc_td.GetTeamsChannelConfigurationResult":
        return dc_td.GetTeamsChannelConfigurationResult.make_one(res)

    def list_associations(
        self,
        res: "bs_td.ListAssociationsResultTypeDef",
    ) -> "dc_td.ListAssociationsResult":
        return dc_td.ListAssociationsResult.make_one(res)

    def list_custom_actions(
        self,
        res: "bs_td.ListCustomActionsResultTypeDef",
    ) -> "dc_td.ListCustomActionsResult":
        return dc_td.ListCustomActionsResult.make_one(res)

    def list_microsoft_teams_channel_configurations(
        self,
        res: "bs_td.ListTeamsChannelConfigurationsResultTypeDef",
    ) -> "dc_td.ListTeamsChannelConfigurationsResult":
        return dc_td.ListTeamsChannelConfigurationsResult.make_one(res)

    def list_microsoft_teams_configured_teams(
        self,
        res: "bs_td.ListMicrosoftTeamsConfiguredTeamsResultTypeDef",
    ) -> "dc_td.ListMicrosoftTeamsConfiguredTeamsResult":
        return dc_td.ListMicrosoftTeamsConfiguredTeamsResult.make_one(res)

    def list_microsoft_teams_user_identities(
        self,
        res: "bs_td.ListMicrosoftTeamsUserIdentitiesResultTypeDef",
    ) -> "dc_td.ListMicrosoftTeamsUserIdentitiesResult":
        return dc_td.ListMicrosoftTeamsUserIdentitiesResult.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def update_account_preferences(
        self,
        res: "bs_td.UpdateAccountPreferencesResultTypeDef",
    ) -> "dc_td.UpdateAccountPreferencesResult":
        return dc_td.UpdateAccountPreferencesResult.make_one(res)

    def update_chime_webhook_configuration(
        self,
        res: "bs_td.UpdateChimeWebhookConfigurationResultTypeDef",
    ) -> "dc_td.UpdateChimeWebhookConfigurationResult":
        return dc_td.UpdateChimeWebhookConfigurationResult.make_one(res)

    def update_custom_action(
        self,
        res: "bs_td.UpdateCustomActionResultTypeDef",
    ) -> "dc_td.UpdateCustomActionResult":
        return dc_td.UpdateCustomActionResult.make_one(res)

    def update_microsoft_teams_channel_configuration(
        self,
        res: "bs_td.UpdateTeamsChannelConfigurationResultTypeDef",
    ) -> "dc_td.UpdateTeamsChannelConfigurationResult":
        return dc_td.UpdateTeamsChannelConfigurationResult.make_one(res)

    def update_slack_channel_configuration(
        self,
        res: "bs_td.UpdateSlackChannelConfigurationResultTypeDef",
    ) -> "dc_td.UpdateSlackChannelConfigurationResult":
        return dc_td.UpdateSlackChannelConfigurationResult.make_one(res)


chatbot_caster = CHATBOTCaster()
