# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_chime import type_defs as bs_td


class CHIMECaster:

    def batch_create_room_membership(
        self,
        res: "bs_td.BatchCreateRoomMembershipResponseTypeDef",
    ) -> "dc_td.BatchCreateRoomMembershipResponse":
        return dc_td.BatchCreateRoomMembershipResponse.make_one(res)

    def batch_delete_phone_number(
        self,
        res: "bs_td.BatchDeletePhoneNumberResponseTypeDef",
    ) -> "dc_td.BatchDeletePhoneNumberResponse":
        return dc_td.BatchDeletePhoneNumberResponse.make_one(res)

    def batch_suspend_user(
        self,
        res: "bs_td.BatchSuspendUserResponseTypeDef",
    ) -> "dc_td.BatchSuspendUserResponse":
        return dc_td.BatchSuspendUserResponse.make_one(res)

    def batch_unsuspend_user(
        self,
        res: "bs_td.BatchUnsuspendUserResponseTypeDef",
    ) -> "dc_td.BatchUnsuspendUserResponse":
        return dc_td.BatchUnsuspendUserResponse.make_one(res)

    def batch_update_phone_number(
        self,
        res: "bs_td.BatchUpdatePhoneNumberResponseTypeDef",
    ) -> "dc_td.BatchUpdatePhoneNumberResponse":
        return dc_td.BatchUpdatePhoneNumberResponse.make_one(res)

    def batch_update_user(
        self,
        res: "bs_td.BatchUpdateUserResponseTypeDef",
    ) -> "dc_td.BatchUpdateUserResponse":
        return dc_td.BatchUpdateUserResponse.make_one(res)

    def create_account(
        self,
        res: "bs_td.CreateAccountResponseTypeDef",
    ) -> "dc_td.CreateAccountResponse":
        return dc_td.CreateAccountResponse.make_one(res)

    def create_bot(
        self,
        res: "bs_td.CreateBotResponseTypeDef",
    ) -> "dc_td.CreateBotResponse":
        return dc_td.CreateBotResponse.make_one(res)

    def create_meeting_dial_out(
        self,
        res: "bs_td.CreateMeetingDialOutResponseTypeDef",
    ) -> "dc_td.CreateMeetingDialOutResponse":
        return dc_td.CreateMeetingDialOutResponse.make_one(res)

    def create_phone_number_order(
        self,
        res: "bs_td.CreatePhoneNumberOrderResponseTypeDef",
    ) -> "dc_td.CreatePhoneNumberOrderResponse":
        return dc_td.CreatePhoneNumberOrderResponse.make_one(res)

    def create_room(
        self,
        res: "bs_td.CreateRoomResponseTypeDef",
    ) -> "dc_td.CreateRoomResponse":
        return dc_td.CreateRoomResponse.make_one(res)

    def create_room_membership(
        self,
        res: "bs_td.CreateRoomMembershipResponseTypeDef",
    ) -> "dc_td.CreateRoomMembershipResponse":
        return dc_td.CreateRoomMembershipResponse.make_one(res)

    def create_user(
        self,
        res: "bs_td.CreateUserResponseTypeDef",
    ) -> "dc_td.CreateUserResponse":
        return dc_td.CreateUserResponse.make_one(res)

    def delete_events_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_phone_number(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_room(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_room_membership(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_account(
        self,
        res: "bs_td.GetAccountResponseTypeDef",
    ) -> "dc_td.GetAccountResponse":
        return dc_td.GetAccountResponse.make_one(res)

    def get_account_settings(
        self,
        res: "bs_td.GetAccountSettingsResponseTypeDef",
    ) -> "dc_td.GetAccountSettingsResponse":
        return dc_td.GetAccountSettingsResponse.make_one(res)

    def get_bot(
        self,
        res: "bs_td.GetBotResponseTypeDef",
    ) -> "dc_td.GetBotResponse":
        return dc_td.GetBotResponse.make_one(res)

    def get_events_configuration(
        self,
        res: "bs_td.GetEventsConfigurationResponseTypeDef",
    ) -> "dc_td.GetEventsConfigurationResponse":
        return dc_td.GetEventsConfigurationResponse.make_one(res)

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

    def get_retention_settings(
        self,
        res: "bs_td.GetRetentionSettingsResponseTypeDef",
    ) -> "dc_td.GetRetentionSettingsResponse":
        return dc_td.GetRetentionSettingsResponse.make_one(res)

    def get_room(
        self,
        res: "bs_td.GetRoomResponseTypeDef",
    ) -> "dc_td.GetRoomResponse":
        return dc_td.GetRoomResponse.make_one(res)

    def get_user(
        self,
        res: "bs_td.GetUserResponseTypeDef",
    ) -> "dc_td.GetUserResponse":
        return dc_td.GetUserResponse.make_one(res)

    def get_user_settings(
        self,
        res: "bs_td.GetUserSettingsResponseTypeDef",
    ) -> "dc_td.GetUserSettingsResponse":
        return dc_td.GetUserSettingsResponse.make_one(res)

    def invite_users(
        self,
        res: "bs_td.InviteUsersResponseTypeDef",
    ) -> "dc_td.InviteUsersResponse":
        return dc_td.InviteUsersResponse.make_one(res)

    def list_accounts(
        self,
        res: "bs_td.ListAccountsResponseTypeDef",
    ) -> "dc_td.ListAccountsResponse":
        return dc_td.ListAccountsResponse.make_one(res)

    def list_bots(
        self,
        res: "bs_td.ListBotsResponseTypeDef",
    ) -> "dc_td.ListBotsResponse":
        return dc_td.ListBotsResponse.make_one(res)

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

    def list_room_memberships(
        self,
        res: "bs_td.ListRoomMembershipsResponseTypeDef",
    ) -> "dc_td.ListRoomMembershipsResponse":
        return dc_td.ListRoomMembershipsResponse.make_one(res)

    def list_rooms(
        self,
        res: "bs_td.ListRoomsResponseTypeDef",
    ) -> "dc_td.ListRoomsResponse":
        return dc_td.ListRoomsResponse.make_one(res)

    def list_supported_phone_number_countries(
        self,
        res: "bs_td.ListSupportedPhoneNumberCountriesResponseTypeDef",
    ) -> "dc_td.ListSupportedPhoneNumberCountriesResponse":
        return dc_td.ListSupportedPhoneNumberCountriesResponse.make_one(res)

    def list_users(
        self,
        res: "bs_td.ListUsersResponseTypeDef",
    ) -> "dc_td.ListUsersResponse":
        return dc_td.ListUsersResponse.make_one(res)

    def put_events_configuration(
        self,
        res: "bs_td.PutEventsConfigurationResponseTypeDef",
    ) -> "dc_td.PutEventsConfigurationResponse":
        return dc_td.PutEventsConfigurationResponse.make_one(res)

    def put_retention_settings(
        self,
        res: "bs_td.PutRetentionSettingsResponseTypeDef",
    ) -> "dc_td.PutRetentionSettingsResponse":
        return dc_td.PutRetentionSettingsResponse.make_one(res)

    def regenerate_security_token(
        self,
        res: "bs_td.RegenerateSecurityTokenResponseTypeDef",
    ) -> "dc_td.RegenerateSecurityTokenResponse":
        return dc_td.RegenerateSecurityTokenResponse.make_one(res)

    def reset_personal_pin(
        self,
        res: "bs_td.ResetPersonalPINResponseTypeDef",
    ) -> "dc_td.ResetPersonalPINResponse":
        return dc_td.ResetPersonalPINResponse.make_one(res)

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

    def update_account(
        self,
        res: "bs_td.UpdateAccountResponseTypeDef",
    ) -> "dc_td.UpdateAccountResponse":
        return dc_td.UpdateAccountResponse.make_one(res)

    def update_bot(
        self,
        res: "bs_td.UpdateBotResponseTypeDef",
    ) -> "dc_td.UpdateBotResponse":
        return dc_td.UpdateBotResponse.make_one(res)

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

    def update_room(
        self,
        res: "bs_td.UpdateRoomResponseTypeDef",
    ) -> "dc_td.UpdateRoomResponse":
        return dc_td.UpdateRoomResponse.make_one(res)

    def update_room_membership(
        self,
        res: "bs_td.UpdateRoomMembershipResponseTypeDef",
    ) -> "dc_td.UpdateRoomMembershipResponse":
        return dc_td.UpdateRoomMembershipResponse.make_one(res)

    def update_user(
        self,
        res: "bs_td.UpdateUserResponseTypeDef",
    ) -> "dc_td.UpdateUserResponse":
        return dc_td.UpdateUserResponse.make_one(res)

    def update_user_settings(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


chime_caster = CHIMECaster()
