# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sns import type_defs as bs_td


class SNSCaster:

    def add_permission(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def check_if_phone_number_is_opted_out(
        self,
        res: "bs_td.CheckIfPhoneNumberIsOptedOutResponseTypeDef",
    ) -> "dc_td.CheckIfPhoneNumberIsOptedOutResponse":
        return dc_td.CheckIfPhoneNumberIsOptedOutResponse.make_one(res)

    def confirm_subscription(
        self,
        res: "bs_td.ConfirmSubscriptionResponseTypeDef",
    ) -> "dc_td.ConfirmSubscriptionResponse":
        return dc_td.ConfirmSubscriptionResponse.make_one(res)

    def create_platform_application(
        self,
        res: "bs_td.CreatePlatformApplicationResponseTypeDef",
    ) -> "dc_td.CreatePlatformApplicationResponse":
        return dc_td.CreatePlatformApplicationResponse.make_one(res)

    def create_platform_endpoint(
        self,
        res: "bs_td.CreateEndpointResponseTypeDef",
    ) -> "dc_td.CreateEndpointResponse":
        return dc_td.CreateEndpointResponse.make_one(res)

    def create_topic(
        self,
        res: "bs_td.CreateTopicResponseTypeDef",
    ) -> "dc_td.CreateTopicResponse":
        return dc_td.CreateTopicResponse.make_one(res)

    def delete_endpoint(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_platform_application(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_topic(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_data_protection_policy(
        self,
        res: "bs_td.GetDataProtectionPolicyResponseTypeDef",
    ) -> "dc_td.GetDataProtectionPolicyResponse":
        return dc_td.GetDataProtectionPolicyResponse.make_one(res)

    def get_endpoint_attributes(
        self,
        res: "bs_td.GetEndpointAttributesResponseTypeDef",
    ) -> "dc_td.GetEndpointAttributesResponse":
        return dc_td.GetEndpointAttributesResponse.make_one(res)

    def get_platform_application_attributes(
        self,
        res: "bs_td.GetPlatformApplicationAttributesResponseTypeDef",
    ) -> "dc_td.GetPlatformApplicationAttributesResponse":
        return dc_td.GetPlatformApplicationAttributesResponse.make_one(res)

    def get_sms_attributes(
        self,
        res: "bs_td.GetSMSAttributesResponseTypeDef",
    ) -> "dc_td.GetSMSAttributesResponse":
        return dc_td.GetSMSAttributesResponse.make_one(res)

    def get_sms_sandbox_account_status(
        self,
        res: "bs_td.GetSMSSandboxAccountStatusResultTypeDef",
    ) -> "dc_td.GetSMSSandboxAccountStatusResult":
        return dc_td.GetSMSSandboxAccountStatusResult.make_one(res)

    def get_subscription_attributes(
        self,
        res: "bs_td.GetSubscriptionAttributesResponseTypeDef",
    ) -> "dc_td.GetSubscriptionAttributesResponse":
        return dc_td.GetSubscriptionAttributesResponse.make_one(res)

    def get_topic_attributes(
        self,
        res: "bs_td.GetTopicAttributesResponseTypeDef",
    ) -> "dc_td.GetTopicAttributesResponse":
        return dc_td.GetTopicAttributesResponse.make_one(res)

    def list_endpoints_by_platform_application(
        self,
        res: "bs_td.ListEndpointsByPlatformApplicationResponseTypeDef",
    ) -> "dc_td.ListEndpointsByPlatformApplicationResponse":
        return dc_td.ListEndpointsByPlatformApplicationResponse.make_one(res)

    def list_origination_numbers(
        self,
        res: "bs_td.ListOriginationNumbersResultTypeDef",
    ) -> "dc_td.ListOriginationNumbersResult":
        return dc_td.ListOriginationNumbersResult.make_one(res)

    def list_phone_numbers_opted_out(
        self,
        res: "bs_td.ListPhoneNumbersOptedOutResponseTypeDef",
    ) -> "dc_td.ListPhoneNumbersOptedOutResponse":
        return dc_td.ListPhoneNumbersOptedOutResponse.make_one(res)

    def list_platform_applications(
        self,
        res: "bs_td.ListPlatformApplicationsResponseTypeDef",
    ) -> "dc_td.ListPlatformApplicationsResponse":
        return dc_td.ListPlatformApplicationsResponse.make_one(res)

    def list_sms_sandbox_phone_numbers(
        self,
        res: "bs_td.ListSMSSandboxPhoneNumbersResultTypeDef",
    ) -> "dc_td.ListSMSSandboxPhoneNumbersResult":
        return dc_td.ListSMSSandboxPhoneNumbersResult.make_one(res)

    def list_subscriptions(
        self,
        res: "bs_td.ListSubscriptionsResponseTypeDef",
    ) -> "dc_td.ListSubscriptionsResponse":
        return dc_td.ListSubscriptionsResponse.make_one(res)

    def list_subscriptions_by_topic(
        self,
        res: "bs_td.ListSubscriptionsByTopicResponseTypeDef",
    ) -> "dc_td.ListSubscriptionsByTopicResponse":
        return dc_td.ListSubscriptionsByTopicResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_topics(
        self,
        res: "bs_td.ListTopicsResponseTypeDef",
    ) -> "dc_td.ListTopicsResponse":
        return dc_td.ListTopicsResponse.make_one(res)

    def publish(
        self,
        res: "bs_td.PublishResponseTypeDef",
    ) -> "dc_td.PublishResponse":
        return dc_td.PublishResponse.make_one(res)

    def publish_batch(
        self,
        res: "bs_td.PublishBatchResponseTypeDef",
    ) -> "dc_td.PublishBatchResponse":
        return dc_td.PublishBatchResponse.make_one(res)

    def put_data_protection_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def remove_permission(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def set_endpoint_attributes(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def set_platform_application_attributes(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def set_subscription_attributes(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def set_topic_attributes(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def subscribe(
        self,
        res: "bs_td.SubscribeResponseTypeDef",
    ) -> "dc_td.SubscribeResponse":
        return dc_td.SubscribeResponse.make_one(res)

    def unsubscribe(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


sns_caster = SNSCaster()
