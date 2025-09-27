# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_codestar_notifications import type_defs as bs_td


class CODESTAR_NOTIFICATIONSCaster:

    def create_notification_rule(
        self,
        res: "bs_td.CreateNotificationRuleResultTypeDef",
    ) -> "dc_td.CreateNotificationRuleResult":
        return dc_td.CreateNotificationRuleResult.make_one(res)

    def delete_notification_rule(
        self,
        res: "bs_td.DeleteNotificationRuleResultTypeDef",
    ) -> "dc_td.DeleteNotificationRuleResult":
        return dc_td.DeleteNotificationRuleResult.make_one(res)

    def describe_notification_rule(
        self,
        res: "bs_td.DescribeNotificationRuleResultTypeDef",
    ) -> "dc_td.DescribeNotificationRuleResult":
        return dc_td.DescribeNotificationRuleResult.make_one(res)

    def list_event_types(
        self,
        res: "bs_td.ListEventTypesResultTypeDef",
    ) -> "dc_td.ListEventTypesResult":
        return dc_td.ListEventTypesResult.make_one(res)

    def list_notification_rules(
        self,
        res: "bs_td.ListNotificationRulesResultTypeDef",
    ) -> "dc_td.ListNotificationRulesResult":
        return dc_td.ListNotificationRulesResult.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResultTypeDef",
    ) -> "dc_td.ListTagsForResourceResult":
        return dc_td.ListTagsForResourceResult.make_one(res)

    def list_targets(
        self,
        res: "bs_td.ListTargetsResultTypeDef",
    ) -> "dc_td.ListTargetsResult":
        return dc_td.ListTargetsResult.make_one(res)

    def subscribe(
        self,
        res: "bs_td.SubscribeResultTypeDef",
    ) -> "dc_td.SubscribeResult":
        return dc_td.SubscribeResult.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.TagResourceResultTypeDef",
    ) -> "dc_td.TagResourceResult":
        return dc_td.TagResourceResult.make_one(res)

    def unsubscribe(
        self,
        res: "bs_td.UnsubscribeResultTypeDef",
    ) -> "dc_td.UnsubscribeResult":
        return dc_td.UnsubscribeResult.make_one(res)


codestar_notifications_caster = CODESTAR_NOTIFICATIONSCaster()
