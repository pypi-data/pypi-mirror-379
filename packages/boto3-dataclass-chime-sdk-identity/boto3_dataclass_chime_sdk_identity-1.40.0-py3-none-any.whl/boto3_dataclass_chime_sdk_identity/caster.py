# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_chime_sdk_identity import type_defs as bs_td


class CHIME_SDK_IDENTITYCaster:

    def create_app_instance(
        self,
        res: "bs_td.CreateAppInstanceResponseTypeDef",
    ) -> "dc_td.CreateAppInstanceResponse":
        return dc_td.CreateAppInstanceResponse.make_one(res)

    def create_app_instance_admin(
        self,
        res: "bs_td.CreateAppInstanceAdminResponseTypeDef",
    ) -> "dc_td.CreateAppInstanceAdminResponse":
        return dc_td.CreateAppInstanceAdminResponse.make_one(res)

    def create_app_instance_bot(
        self,
        res: "bs_td.CreateAppInstanceBotResponseTypeDef",
    ) -> "dc_td.CreateAppInstanceBotResponse":
        return dc_td.CreateAppInstanceBotResponse.make_one(res)

    def create_app_instance_user(
        self,
        res: "bs_td.CreateAppInstanceUserResponseTypeDef",
    ) -> "dc_td.CreateAppInstanceUserResponse":
        return dc_td.CreateAppInstanceUserResponse.make_one(res)

    def delete_app_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_app_instance_admin(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_app_instance_bot(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_app_instance_user(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def deregister_app_instance_user_endpoint(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_app_instance(
        self,
        res: "bs_td.DescribeAppInstanceResponseTypeDef",
    ) -> "dc_td.DescribeAppInstanceResponse":
        return dc_td.DescribeAppInstanceResponse.make_one(res)

    def describe_app_instance_admin(
        self,
        res: "bs_td.DescribeAppInstanceAdminResponseTypeDef",
    ) -> "dc_td.DescribeAppInstanceAdminResponse":
        return dc_td.DescribeAppInstanceAdminResponse.make_one(res)

    def describe_app_instance_bot(
        self,
        res: "bs_td.DescribeAppInstanceBotResponseTypeDef",
    ) -> "dc_td.DescribeAppInstanceBotResponse":
        return dc_td.DescribeAppInstanceBotResponse.make_one(res)

    def describe_app_instance_user(
        self,
        res: "bs_td.DescribeAppInstanceUserResponseTypeDef",
    ) -> "dc_td.DescribeAppInstanceUserResponse":
        return dc_td.DescribeAppInstanceUserResponse.make_one(res)

    def describe_app_instance_user_endpoint(
        self,
        res: "bs_td.DescribeAppInstanceUserEndpointResponseTypeDef",
    ) -> "dc_td.DescribeAppInstanceUserEndpointResponse":
        return dc_td.DescribeAppInstanceUserEndpointResponse.make_one(res)

    def get_app_instance_retention_settings(
        self,
        res: "bs_td.GetAppInstanceRetentionSettingsResponseTypeDef",
    ) -> "dc_td.GetAppInstanceRetentionSettingsResponse":
        return dc_td.GetAppInstanceRetentionSettingsResponse.make_one(res)

    def list_app_instance_admins(
        self,
        res: "bs_td.ListAppInstanceAdminsResponseTypeDef",
    ) -> "dc_td.ListAppInstanceAdminsResponse":
        return dc_td.ListAppInstanceAdminsResponse.make_one(res)

    def list_app_instance_bots(
        self,
        res: "bs_td.ListAppInstanceBotsResponseTypeDef",
    ) -> "dc_td.ListAppInstanceBotsResponse":
        return dc_td.ListAppInstanceBotsResponse.make_one(res)

    def list_app_instance_user_endpoints(
        self,
        res: "bs_td.ListAppInstanceUserEndpointsResponseTypeDef",
    ) -> "dc_td.ListAppInstanceUserEndpointsResponse":
        return dc_td.ListAppInstanceUserEndpointsResponse.make_one(res)

    def list_app_instance_users(
        self,
        res: "bs_td.ListAppInstanceUsersResponseTypeDef",
    ) -> "dc_td.ListAppInstanceUsersResponse":
        return dc_td.ListAppInstanceUsersResponse.make_one(res)

    def list_app_instances(
        self,
        res: "bs_td.ListAppInstancesResponseTypeDef",
    ) -> "dc_td.ListAppInstancesResponse":
        return dc_td.ListAppInstancesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_app_instance_retention_settings(
        self,
        res: "bs_td.PutAppInstanceRetentionSettingsResponseTypeDef",
    ) -> "dc_td.PutAppInstanceRetentionSettingsResponse":
        return dc_td.PutAppInstanceRetentionSettingsResponse.make_one(res)

    def put_app_instance_user_expiration_settings(
        self,
        res: "bs_td.PutAppInstanceUserExpirationSettingsResponseTypeDef",
    ) -> "dc_td.PutAppInstanceUserExpirationSettingsResponse":
        return dc_td.PutAppInstanceUserExpirationSettingsResponse.make_one(res)

    def register_app_instance_user_endpoint(
        self,
        res: "bs_td.RegisterAppInstanceUserEndpointResponseTypeDef",
    ) -> "dc_td.RegisterAppInstanceUserEndpointResponse":
        return dc_td.RegisterAppInstanceUserEndpointResponse.make_one(res)

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

    def update_app_instance(
        self,
        res: "bs_td.UpdateAppInstanceResponseTypeDef",
    ) -> "dc_td.UpdateAppInstanceResponse":
        return dc_td.UpdateAppInstanceResponse.make_one(res)

    def update_app_instance_bot(
        self,
        res: "bs_td.UpdateAppInstanceBotResponseTypeDef",
    ) -> "dc_td.UpdateAppInstanceBotResponse":
        return dc_td.UpdateAppInstanceBotResponse.make_one(res)

    def update_app_instance_user(
        self,
        res: "bs_td.UpdateAppInstanceUserResponseTypeDef",
    ) -> "dc_td.UpdateAppInstanceUserResponse":
        return dc_td.UpdateAppInstanceUserResponse.make_one(res)

    def update_app_instance_user_endpoint(
        self,
        res: "bs_td.UpdateAppInstanceUserEndpointResponseTypeDef",
    ) -> "dc_td.UpdateAppInstanceUserEndpointResponse":
        return dc_td.UpdateAppInstanceUserEndpointResponse.make_one(res)


chime_sdk_identity_caster = CHIME_SDK_IDENTITYCaster()
