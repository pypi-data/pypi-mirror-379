# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_chime import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccountSettings:
    boto3_raw_data: "type_defs.AccountSettingsTypeDef" = dataclasses.field()

    DisableRemoteControl = field("DisableRemoteControl")
    EnableDialOut = field("EnableDialOut")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SigninDelegateGroup:
    boto3_raw_data: "type_defs.SigninDelegateGroupTypeDef" = dataclasses.field()

    GroupName = field("GroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SigninDelegateGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SigninDelegateGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlexaForBusinessMetadata:
    boto3_raw_data: "type_defs.AlexaForBusinessMetadataTypeDef" = dataclasses.field()

    IsAlexaForBusinessEnabled = field("IsAlexaForBusinessEnabled")
    AlexaForBusinessRoomArn = field("AlexaForBusinessRoomArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AlexaForBusinessMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlexaForBusinessMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatePhoneNumberWithUserRequest:
    boto3_raw_data: "type_defs.AssociatePhoneNumberWithUserRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    UserId = field("UserId")
    E164PhoneNumber = field("E164PhoneNumber")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociatePhoneNumberWithUserRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatePhoneNumberWithUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MembershipItem:
    boto3_raw_data: "type_defs.MembershipItemTypeDef" = dataclasses.field()

    MemberId = field("MemberId")
    Role = field("Role")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MembershipItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MembershipItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberError:
    boto3_raw_data: "type_defs.MemberErrorTypeDef" = dataclasses.field()

    MemberId = field("MemberId")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemberErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemberErrorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseMetadata:
    boto3_raw_data: "type_defs.ResponseMetadataTypeDef" = dataclasses.field()

    RequestId = field("RequestId")
    HTTPStatusCode = field("HTTPStatusCode")
    HTTPHeaders = field("HTTPHeaders")
    RetryAttempts = field("RetryAttempts")
    HostId = field("HostId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeletePhoneNumberRequest:
    boto3_raw_data: "type_defs.BatchDeletePhoneNumberRequestTypeDef" = (
        dataclasses.field()
    )

    PhoneNumberIds = field("PhoneNumberIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchDeletePhoneNumberRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeletePhoneNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhoneNumberError:
    boto3_raw_data: "type_defs.PhoneNumberErrorTypeDef" = dataclasses.field()

    PhoneNumberId = field("PhoneNumberId")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PhoneNumberErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhoneNumberErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchSuspendUserRequest:
    boto3_raw_data: "type_defs.BatchSuspendUserRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    UserIdList = field("UserIdList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchSuspendUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchSuspendUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserError:
    boto3_raw_data: "type_defs.UserErrorTypeDef" = dataclasses.field()

    UserId = field("UserId")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserErrorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUnsuspendUserRequest:
    boto3_raw_data: "type_defs.BatchUnsuspendUserRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    UserIdList = field("UserIdList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchUnsuspendUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUnsuspendUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePhoneNumberRequestItem:
    boto3_raw_data: "type_defs.UpdatePhoneNumberRequestItemTypeDef" = (
        dataclasses.field()
    )

    PhoneNumberId = field("PhoneNumberId")
    ProductType = field("ProductType")
    CallingName = field("CallingName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePhoneNumberRequestItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePhoneNumberRequestItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Bot:
    boto3_raw_data: "type_defs.BotTypeDef" = dataclasses.field()

    BotId = field("BotId")
    UserId = field("UserId")
    DisplayName = field("DisplayName")
    BotType = field("BotType")
    Disabled = field("Disabled")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")
    BotEmail = field("BotEmail")
    SecurityToken = field("SecurityToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BotTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BotTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BusinessCallingSettings:
    boto3_raw_data: "type_defs.BusinessCallingSettingsTypeDef" = dataclasses.field()

    CdrBucket = field("CdrBucket")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BusinessCallingSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BusinessCallingSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversationRetentionSettings:
    boto3_raw_data: "type_defs.ConversationRetentionSettingsTypeDef" = (
        dataclasses.field()
    )

    RetentionDays = field("RetentionDays")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConversationRetentionSettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversationRetentionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccountRequest:
    boto3_raw_data: "type_defs.CreateAccountRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccountRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBotRequest:
    boto3_raw_data: "type_defs.CreateBotRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    DisplayName = field("DisplayName")
    Domain = field("Domain")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateBotRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMeetingDialOutRequest:
    boto3_raw_data: "type_defs.CreateMeetingDialOutRequestTypeDef" = dataclasses.field()

    MeetingId = field("MeetingId")
    FromPhoneNumber = field("FromPhoneNumber")
    ToPhoneNumber = field("ToPhoneNumber")
    JoinToken = field("JoinToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMeetingDialOutRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMeetingDialOutRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePhoneNumberOrderRequest:
    boto3_raw_data: "type_defs.CreatePhoneNumberOrderRequestTypeDef" = (
        dataclasses.field()
    )

    ProductType = field("ProductType")
    E164PhoneNumbers = field("E164PhoneNumbers")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreatePhoneNumberOrderRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePhoneNumberOrderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRoomMembershipRequest:
    boto3_raw_data: "type_defs.CreateRoomMembershipRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    RoomId = field("RoomId")
    MemberId = field("MemberId")
    Role = field("Role")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRoomMembershipRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRoomMembershipRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRoomRequest:
    boto3_raw_data: "type_defs.CreateRoomRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Name = field("Name")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateRoomRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRoomRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Room:
    boto3_raw_data: "type_defs.RoomTypeDef" = dataclasses.field()

    RoomId = field("RoomId")
    Name = field("Name")
    AccountId = field("AccountId")
    CreatedBy = field("CreatedBy")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RoomTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RoomTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserRequest:
    boto3_raw_data: "type_defs.CreateUserRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Username = field("Username")
    Email = field("Email")
    UserType = field("UserType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccountRequest:
    boto3_raw_data: "type_defs.DeleteAccountRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAccountRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventsConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteEventsConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    BotId = field("BotId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteEventsConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventsConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePhoneNumberRequest:
    boto3_raw_data: "type_defs.DeletePhoneNumberRequestTypeDef" = dataclasses.field()

    PhoneNumberId = field("PhoneNumberId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePhoneNumberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePhoneNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRoomMembershipRequest:
    boto3_raw_data: "type_defs.DeleteRoomMembershipRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    RoomId = field("RoomId")
    MemberId = field("MemberId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRoomMembershipRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRoomMembershipRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRoomRequest:
    boto3_raw_data: "type_defs.DeleteRoomRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    RoomId = field("RoomId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteRoomRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRoomRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociatePhoneNumberFromUserRequest:
    boto3_raw_data: "type_defs.DisassociatePhoneNumberFromUserRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    UserId = field("UserId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociatePhoneNumberFromUserRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociatePhoneNumberFromUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateSigninDelegateGroupsFromAccountRequest:
    boto3_raw_data: (
        "type_defs.DisassociateSigninDelegateGroupsFromAccountRequestTypeDef"
    ) = dataclasses.field()

    AccountId = field("AccountId")
    GroupNames = field("GroupNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateSigninDelegateGroupsFromAccountRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DisassociateSigninDelegateGroupsFromAccountRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventsConfiguration:
    boto3_raw_data: "type_defs.EventsConfigurationTypeDef" = dataclasses.field()

    BotId = field("BotId")
    OutboundEventsHTTPSEndpoint = field("OutboundEventsHTTPSEndpoint")
    LambdaFunctionArn = field("LambdaFunctionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountRequest:
    boto3_raw_data: "type_defs.GetAccountRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAccountRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountSettingsRequest:
    boto3_raw_data: "type_defs.GetAccountSettingsRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccountSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBotRequest:
    boto3_raw_data: "type_defs.GetBotRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    BotId = field("BotId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetBotRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetBotRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventsConfigurationRequest:
    boto3_raw_data: "type_defs.GetEventsConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    BotId = field("BotId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetEventsConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventsConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoiceConnectorSettings:
    boto3_raw_data: "type_defs.VoiceConnectorSettingsTypeDef" = dataclasses.field()

    CdrBucket = field("CdrBucket")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VoiceConnectorSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VoiceConnectorSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPhoneNumberOrderRequest:
    boto3_raw_data: "type_defs.GetPhoneNumberOrderRequestTypeDef" = dataclasses.field()

    PhoneNumberOrderId = field("PhoneNumberOrderId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPhoneNumberOrderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPhoneNumberOrderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPhoneNumberRequest:
    boto3_raw_data: "type_defs.GetPhoneNumberRequestTypeDef" = dataclasses.field()

    PhoneNumberId = field("PhoneNumberId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPhoneNumberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPhoneNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRetentionSettingsRequest:
    boto3_raw_data: "type_defs.GetRetentionSettingsRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRetentionSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRetentionSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRoomRequest:
    boto3_raw_data: "type_defs.GetRoomRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    RoomId = field("RoomId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRoomRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetRoomRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserRequest:
    boto3_raw_data: "type_defs.GetUserRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    UserId = field("UserId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetUserRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserSettingsRequest:
    boto3_raw_data: "type_defs.GetUserSettingsRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    UserId = field("UserId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUserSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUserSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Invite:
    boto3_raw_data: "type_defs.InviteTypeDef" = dataclasses.field()

    InviteId = field("InviteId")
    Status = field("Status")
    EmailAddress = field("EmailAddress")
    EmailStatus = field("EmailStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InviteTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InviteTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InviteUsersRequest:
    boto3_raw_data: "type_defs.InviteUsersRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    UserEmailList = field("UserEmailList")
    UserType = field("UserType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InviteUsersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InviteUsersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PaginatorConfig:
    boto3_raw_data: "type_defs.PaginatorConfigTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    PageSize = field("PageSize")
    StartingToken = field("StartingToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PaginatorConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PaginatorConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountsRequest:
    boto3_raw_data: "type_defs.ListAccountsRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    UserEmail = field("UserEmail")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccountsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotsRequest:
    boto3_raw_data: "type_defs.ListBotsRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListBotsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListBotsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPhoneNumberOrdersRequest:
    boto3_raw_data: "type_defs.ListPhoneNumberOrdersRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPhoneNumberOrdersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPhoneNumberOrdersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPhoneNumbersRequest:
    boto3_raw_data: "type_defs.ListPhoneNumbersRequestTypeDef" = dataclasses.field()

    Status = field("Status")
    ProductType = field("ProductType")
    FilterName = field("FilterName")
    FilterValue = field("FilterValue")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPhoneNumbersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPhoneNumbersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoomMembershipsRequest:
    boto3_raw_data: "type_defs.ListRoomMembershipsRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    RoomId = field("RoomId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRoomMembershipsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoomMembershipsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoomsRequest:
    boto3_raw_data: "type_defs.ListRoomsRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    MemberId = field("MemberId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListRoomsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoomsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSupportedPhoneNumberCountriesRequest:
    boto3_raw_data: "type_defs.ListSupportedPhoneNumberCountriesRequestTypeDef" = (
        dataclasses.field()
    )

    ProductType = field("ProductType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSupportedPhoneNumberCountriesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSupportedPhoneNumberCountriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhoneNumberCountry:
    boto3_raw_data: "type_defs.PhoneNumberCountryTypeDef" = dataclasses.field()

    CountryCode = field("CountryCode")
    SupportedPhoneNumberTypes = field("SupportedPhoneNumberTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PhoneNumberCountryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhoneNumberCountryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsersRequest:
    boto3_raw_data: "type_defs.ListUsersRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    UserEmail = field("UserEmail")
    UserType = field("UserType")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListUsersRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogoutUserRequest:
    boto3_raw_data: "type_defs.LogoutUserRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    UserId = field("UserId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogoutUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogoutUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Member:
    boto3_raw_data: "type_defs.MemberTypeDef" = dataclasses.field()

    MemberId = field("MemberId")
    MemberType = field("MemberType")
    Email = field("Email")
    FullName = field("FullName")
    AccountId = field("AccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemberTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrderedPhoneNumber:
    boto3_raw_data: "type_defs.OrderedPhoneNumberTypeDef" = dataclasses.field()

    E164PhoneNumber = field("E164PhoneNumber")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrderedPhoneNumberTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrderedPhoneNumberTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhoneNumberAssociation:
    boto3_raw_data: "type_defs.PhoneNumberAssociationTypeDef" = dataclasses.field()

    Value = field("Value")
    Name = field("Name")
    AssociatedTimestamp = field("AssociatedTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PhoneNumberAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhoneNumberAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhoneNumberCapabilities:
    boto3_raw_data: "type_defs.PhoneNumberCapabilitiesTypeDef" = dataclasses.field()

    InboundCall = field("InboundCall")
    OutboundCall = field("OutboundCall")
    InboundSMS = field("InboundSMS")
    OutboundSMS = field("OutboundSMS")
    InboundMMS = field("InboundMMS")
    OutboundMMS = field("OutboundMMS")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PhoneNumberCapabilitiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhoneNumberCapabilitiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEventsConfigurationRequest:
    boto3_raw_data: "type_defs.PutEventsConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    BotId = field("BotId")
    OutboundEventsHTTPSEndpoint = field("OutboundEventsHTTPSEndpoint")
    LambdaFunctionArn = field("LambdaFunctionArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutEventsConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEventsConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedactConversationMessageRequest:
    boto3_raw_data: "type_defs.RedactConversationMessageRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    ConversationId = field("ConversationId")
    MessageId = field("MessageId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RedactConversationMessageRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedactConversationMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedactRoomMessageRequest:
    boto3_raw_data: "type_defs.RedactRoomMessageRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    RoomId = field("RoomId")
    MessageId = field("MessageId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedactRoomMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedactRoomMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegenerateSecurityTokenRequest:
    boto3_raw_data: "type_defs.RegenerateSecurityTokenRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    BotId = field("BotId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegenerateSecurityTokenRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegenerateSecurityTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetPersonalPINRequest:
    boto3_raw_data: "type_defs.ResetPersonalPINRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    UserId = field("UserId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResetPersonalPINRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetPersonalPINRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestorePhoneNumberRequest:
    boto3_raw_data: "type_defs.RestorePhoneNumberRequestTypeDef" = dataclasses.field()

    PhoneNumberId = field("PhoneNumberId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestorePhoneNumberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestorePhoneNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoomRetentionSettings:
    boto3_raw_data: "type_defs.RoomRetentionSettingsTypeDef" = dataclasses.field()

    RetentionDays = field("RetentionDays")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoomRetentionSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoomRetentionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchAvailablePhoneNumbersRequest:
    boto3_raw_data: "type_defs.SearchAvailablePhoneNumbersRequestTypeDef" = (
        dataclasses.field()
    )

    AreaCode = field("AreaCode")
    City = field("City")
    Country = field("Country")
    State = field("State")
    TollFreePrefix = field("TollFreePrefix")
    PhoneNumberType = field("PhoneNumberType")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchAvailablePhoneNumbersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchAvailablePhoneNumbersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TelephonySettings:
    boto3_raw_data: "type_defs.TelephonySettingsTypeDef" = dataclasses.field()

    InboundCalling = field("InboundCalling")
    OutboundCalling = field("OutboundCalling")
    SMS = field("SMS")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TelephonySettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TelephonySettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccountRequest:
    boto3_raw_data: "type_defs.UpdateAccountRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Name = field("Name")
    DefaultLicense = field("DefaultLicense")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAccountRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBotRequest:
    boto3_raw_data: "type_defs.UpdateBotRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    BotId = field("BotId")
    Disabled = field("Disabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateBotRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePhoneNumberRequest:
    boto3_raw_data: "type_defs.UpdatePhoneNumberRequestTypeDef" = dataclasses.field()

    PhoneNumberId = field("PhoneNumberId")
    ProductType = field("ProductType")
    CallingName = field("CallingName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePhoneNumberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePhoneNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePhoneNumberSettingsRequest:
    boto3_raw_data: "type_defs.UpdatePhoneNumberSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    CallingName = field("CallingName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdatePhoneNumberSettingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePhoneNumberSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRoomMembershipRequest:
    boto3_raw_data: "type_defs.UpdateRoomMembershipRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    RoomId = field("RoomId")
    MemberId = field("MemberId")
    Role = field("Role")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRoomMembershipRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRoomMembershipRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRoomRequest:
    boto3_raw_data: "type_defs.UpdateRoomRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    RoomId = field("RoomId")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateRoomRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRoomRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccountSettingsRequest:
    boto3_raw_data: "type_defs.UpdateAccountSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")

    @cached_property
    def AccountSettings(self):  # pragma: no cover
        return AccountSettings.make_one(self.boto3_raw_data["AccountSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAccountSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccountSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Account:
    boto3_raw_data: "type_defs.AccountTypeDef" = dataclasses.field()

    AwsAccountId = field("AwsAccountId")
    AccountId = field("AccountId")
    Name = field("Name")
    AccountType = field("AccountType")
    CreatedTimestamp = field("CreatedTimestamp")
    DefaultLicense = field("DefaultLicense")
    SupportedLicenses = field("SupportedLicenses")
    AccountStatus = field("AccountStatus")

    @cached_property
    def SigninDelegateGroups(self):  # pragma: no cover
        return SigninDelegateGroup.make_many(
            self.boto3_raw_data["SigninDelegateGroups"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateSigninDelegateGroupsWithAccountRequest:
    boto3_raw_data: (
        "type_defs.AssociateSigninDelegateGroupsWithAccountRequestTypeDef"
    ) = dataclasses.field()

    AccountId = field("AccountId")

    @cached_property
    def SigninDelegateGroups(self):  # pragma: no cover
        return SigninDelegateGroup.make_many(
            self.boto3_raw_data["SigninDelegateGroups"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateSigninDelegateGroupsWithAccountRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AssociateSigninDelegateGroupsWithAccountRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserRequestItem:
    boto3_raw_data: "type_defs.UpdateUserRequestItemTypeDef" = dataclasses.field()

    UserId = field("UserId")
    LicenseType = field("LicenseType")
    UserType = field("UserType")

    @cached_property
    def AlexaForBusinessMetadata(self):  # pragma: no cover
        return AlexaForBusinessMetadata.make_one(
            self.boto3_raw_data["AlexaForBusinessMetadata"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUserRequestItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserRequestItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserRequest:
    boto3_raw_data: "type_defs.UpdateUserRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    UserId = field("UserId")
    LicenseType = field("LicenseType")
    UserType = field("UserType")

    @cached_property
    def AlexaForBusinessMetadata(self):  # pragma: no cover
        return AlexaForBusinessMetadata.make_one(
            self.boto3_raw_data["AlexaForBusinessMetadata"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class User:
    boto3_raw_data: "type_defs.UserTypeDef" = dataclasses.field()

    UserId = field("UserId")
    AccountId = field("AccountId")
    PrimaryEmail = field("PrimaryEmail")
    PrimaryProvisionedNumber = field("PrimaryProvisionedNumber")
    DisplayName = field("DisplayName")
    LicenseType = field("LicenseType")
    UserType = field("UserType")
    UserRegistrationStatus = field("UserRegistrationStatus")
    UserInvitationStatus = field("UserInvitationStatus")
    RegisteredOn = field("RegisteredOn")
    InvitedOn = field("InvitedOn")

    @cached_property
    def AlexaForBusinessMetadata(self):  # pragma: no cover
        return AlexaForBusinessMetadata.make_one(
            self.boto3_raw_data["AlexaForBusinessMetadata"]
        )

    PersonalPIN = field("PersonalPIN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateRoomMembershipRequest:
    boto3_raw_data: "type_defs.BatchCreateRoomMembershipRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    RoomId = field("RoomId")

    @cached_property
    def MembershipItemList(self):  # pragma: no cover
        return MembershipItem.make_many(self.boto3_raw_data["MembershipItemList"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchCreateRoomMembershipRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateRoomMembershipRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateRoomMembershipResponse:
    boto3_raw_data: "type_defs.BatchCreateRoomMembershipResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Errors(self):  # pragma: no cover
        return MemberError.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateRoomMembershipResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateRoomMembershipResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMeetingDialOutResponse:
    boto3_raw_data: "type_defs.CreateMeetingDialOutResponseTypeDef" = (
        dataclasses.field()
    )

    TransactionId = field("TransactionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMeetingDialOutResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMeetingDialOutResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountSettingsResponse:
    boto3_raw_data: "type_defs.GetAccountSettingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def AccountSettings(self):  # pragma: no cover
        return AccountSettings.make_one(self.boto3_raw_data["AccountSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccountSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPhoneNumberSettingsResponse:
    boto3_raw_data: "type_defs.GetPhoneNumberSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    CallingName = field("CallingName")
    CallingNameUpdatedTimestamp = field("CallingNameUpdatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPhoneNumberSettingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPhoneNumberSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchAvailablePhoneNumbersResponse:
    boto3_raw_data: "type_defs.SearchAvailablePhoneNumbersResponseTypeDef" = (
        dataclasses.field()
    )

    E164PhoneNumbers = field("E164PhoneNumbers")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchAvailablePhoneNumbersResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchAvailablePhoneNumbersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeletePhoneNumberResponse:
    boto3_raw_data: "type_defs.BatchDeletePhoneNumberResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PhoneNumberErrors(self):  # pragma: no cover
        return PhoneNumberError.make_many(self.boto3_raw_data["PhoneNumberErrors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchDeletePhoneNumberResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeletePhoneNumberResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdatePhoneNumberResponse:
    boto3_raw_data: "type_defs.BatchUpdatePhoneNumberResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PhoneNumberErrors(self):  # pragma: no cover
        return PhoneNumberError.make_many(self.boto3_raw_data["PhoneNumberErrors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchUpdatePhoneNumberResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdatePhoneNumberResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchSuspendUserResponse:
    boto3_raw_data: "type_defs.BatchSuspendUserResponseTypeDef" = dataclasses.field()

    @cached_property
    def UserErrors(self):  # pragma: no cover
        return UserError.make_many(self.boto3_raw_data["UserErrors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchSuspendUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchSuspendUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUnsuspendUserResponse:
    boto3_raw_data: "type_defs.BatchUnsuspendUserResponseTypeDef" = dataclasses.field()

    @cached_property
    def UserErrors(self):  # pragma: no cover
        return UserError.make_many(self.boto3_raw_data["UserErrors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchUnsuspendUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUnsuspendUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateUserResponse:
    boto3_raw_data: "type_defs.BatchUpdateUserResponseTypeDef" = dataclasses.field()

    @cached_property
    def UserErrors(self):  # pragma: no cover
        return UserError.make_many(self.boto3_raw_data["UserErrors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchUpdateUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdatePhoneNumberRequest:
    boto3_raw_data: "type_defs.BatchUpdatePhoneNumberRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UpdatePhoneNumberRequestItems(self):  # pragma: no cover
        return UpdatePhoneNumberRequestItem.make_many(
            self.boto3_raw_data["UpdatePhoneNumberRequestItems"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchUpdatePhoneNumberRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdatePhoneNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBotResponse:
    boto3_raw_data: "type_defs.CreateBotResponseTypeDef" = dataclasses.field()

    @cached_property
    def Bot(self):  # pragma: no cover
        return Bot.make_one(self.boto3_raw_data["Bot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateBotResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBotResponse:
    boto3_raw_data: "type_defs.GetBotResponseTypeDef" = dataclasses.field()

    @cached_property
    def Bot(self):  # pragma: no cover
        return Bot.make_one(self.boto3_raw_data["Bot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetBotResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetBotResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotsResponse:
    boto3_raw_data: "type_defs.ListBotsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Bots(self):  # pragma: no cover
        return Bot.make_many(self.boto3_raw_data["Bots"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListBotsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBotsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegenerateSecurityTokenResponse:
    boto3_raw_data: "type_defs.RegenerateSecurityTokenResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Bot(self):  # pragma: no cover
        return Bot.make_one(self.boto3_raw_data["Bot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegenerateSecurityTokenResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegenerateSecurityTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBotResponse:
    boto3_raw_data: "type_defs.UpdateBotResponseTypeDef" = dataclasses.field()

    @cached_property
    def Bot(self):  # pragma: no cover
        return Bot.make_one(self.boto3_raw_data["Bot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateBotResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRoomResponse:
    boto3_raw_data: "type_defs.CreateRoomResponseTypeDef" = dataclasses.field()

    @cached_property
    def Room(self):  # pragma: no cover
        return Room.make_one(self.boto3_raw_data["Room"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRoomResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRoomResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRoomResponse:
    boto3_raw_data: "type_defs.GetRoomResponseTypeDef" = dataclasses.field()

    @cached_property
    def Room(self):  # pragma: no cover
        return Room.make_one(self.boto3_raw_data["Room"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRoomResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetRoomResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoomsResponse:
    boto3_raw_data: "type_defs.ListRoomsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Rooms(self):  # pragma: no cover
        return Room.make_many(self.boto3_raw_data["Rooms"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListRoomsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoomsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRoomResponse:
    boto3_raw_data: "type_defs.UpdateRoomResponseTypeDef" = dataclasses.field()

    @cached_property
    def Room(self):  # pragma: no cover
        return Room.make_one(self.boto3_raw_data["Room"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRoomResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRoomResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventsConfigurationResponse:
    boto3_raw_data: "type_defs.GetEventsConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventsConfiguration(self):  # pragma: no cover
        return EventsConfiguration.make_one(self.boto3_raw_data["EventsConfiguration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetEventsConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventsConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEventsConfigurationResponse:
    boto3_raw_data: "type_defs.PutEventsConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventsConfiguration(self):  # pragma: no cover
        return EventsConfiguration.make_one(self.boto3_raw_data["EventsConfiguration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutEventsConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEventsConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGlobalSettingsResponse:
    boto3_raw_data: "type_defs.GetGlobalSettingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def BusinessCalling(self):  # pragma: no cover
        return BusinessCallingSettings.make_one(self.boto3_raw_data["BusinessCalling"])

    @cached_property
    def VoiceConnector(self):  # pragma: no cover
        return VoiceConnectorSettings.make_one(self.boto3_raw_data["VoiceConnector"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGlobalSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGlobalSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGlobalSettingsRequest:
    boto3_raw_data: "type_defs.UpdateGlobalSettingsRequestTypeDef" = dataclasses.field()

    @cached_property
    def BusinessCalling(self):  # pragma: no cover
        return BusinessCallingSettings.make_one(self.boto3_raw_data["BusinessCalling"])

    @cached_property
    def VoiceConnector(self):  # pragma: no cover
        return VoiceConnectorSettings.make_one(self.boto3_raw_data["VoiceConnector"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGlobalSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGlobalSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InviteUsersResponse:
    boto3_raw_data: "type_defs.InviteUsersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Invites(self):  # pragma: no cover
        return Invite.make_many(self.boto3_raw_data["Invites"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InviteUsersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InviteUsersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountsRequestPaginate:
    boto3_raw_data: "type_defs.ListAccountsRequestPaginateTypeDef" = dataclasses.field()

    Name = field("Name")
    UserEmail = field("UserEmail")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccountsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsersRequestPaginate:
    boto3_raw_data: "type_defs.ListUsersRequestPaginateTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    UserEmail = field("UserEmail")
    UserType = field("UserType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUsersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSupportedPhoneNumberCountriesResponse:
    boto3_raw_data: "type_defs.ListSupportedPhoneNumberCountriesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PhoneNumberCountries(self):  # pragma: no cover
        return PhoneNumberCountry.make_many(self.boto3_raw_data["PhoneNumberCountries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSupportedPhoneNumberCountriesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSupportedPhoneNumberCountriesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoomMembership:
    boto3_raw_data: "type_defs.RoomMembershipTypeDef" = dataclasses.field()

    RoomId = field("RoomId")

    @cached_property
    def Member(self):  # pragma: no cover
        return Member.make_one(self.boto3_raw_data["Member"])

    Role = field("Role")
    InvitedBy = field("InvitedBy")
    UpdatedTimestamp = field("UpdatedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RoomMembershipTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RoomMembershipTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhoneNumberOrder:
    boto3_raw_data: "type_defs.PhoneNumberOrderTypeDef" = dataclasses.field()

    PhoneNumberOrderId = field("PhoneNumberOrderId")
    ProductType = field("ProductType")
    Status = field("Status")

    @cached_property
    def OrderedPhoneNumbers(self):  # pragma: no cover
        return OrderedPhoneNumber.make_many(self.boto3_raw_data["OrderedPhoneNumbers"])

    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PhoneNumberOrderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhoneNumberOrderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhoneNumber:
    boto3_raw_data: "type_defs.PhoneNumberTypeDef" = dataclasses.field()

    PhoneNumberId = field("PhoneNumberId")
    E164PhoneNumber = field("E164PhoneNumber")
    Country = field("Country")
    Type = field("Type")
    ProductType = field("ProductType")
    Status = field("Status")

    @cached_property
    def Capabilities(self):  # pragma: no cover
        return PhoneNumberCapabilities.make_one(self.boto3_raw_data["Capabilities"])

    @cached_property
    def Associations(self):  # pragma: no cover
        return PhoneNumberAssociation.make_many(self.boto3_raw_data["Associations"])

    CallingName = field("CallingName")
    CallingNameStatus = field("CallingNameStatus")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")
    DeletionTimestamp = field("DeletionTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PhoneNumberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PhoneNumberTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetentionSettings:
    boto3_raw_data: "type_defs.RetentionSettingsTypeDef" = dataclasses.field()

    @cached_property
    def RoomRetentionSettings(self):  # pragma: no cover
        return RoomRetentionSettings.make_one(
            self.boto3_raw_data["RoomRetentionSettings"]
        )

    @cached_property
    def ConversationRetentionSettings(self):  # pragma: no cover
        return ConversationRetentionSettings.make_one(
            self.boto3_raw_data["ConversationRetentionSettings"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetentionSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetentionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserSettings:
    boto3_raw_data: "type_defs.UserSettingsTypeDef" = dataclasses.field()

    @cached_property
    def Telephony(self):  # pragma: no cover
        return TelephonySettings.make_one(self.boto3_raw_data["Telephony"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccountResponse:
    boto3_raw_data: "type_defs.CreateAccountResponseTypeDef" = dataclasses.field()

    @cached_property
    def Account(self):  # pragma: no cover
        return Account.make_one(self.boto3_raw_data["Account"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccountResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountResponse:
    boto3_raw_data: "type_defs.GetAccountResponseTypeDef" = dataclasses.field()

    @cached_property
    def Account(self):  # pragma: no cover
        return Account.make_one(self.boto3_raw_data["Account"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccountResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountsResponse:
    boto3_raw_data: "type_defs.ListAccountsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Accounts(self):  # pragma: no cover
        return Account.make_many(self.boto3_raw_data["Accounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccountsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccountResponse:
    boto3_raw_data: "type_defs.UpdateAccountResponseTypeDef" = dataclasses.field()

    @cached_property
    def Account(self):  # pragma: no cover
        return Account.make_one(self.boto3_raw_data["Account"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAccountResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateUserRequest:
    boto3_raw_data: "type_defs.BatchUpdateUserRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")

    @cached_property
    def UpdateUserRequestItems(self):  # pragma: no cover
        return UpdateUserRequestItem.make_many(
            self.boto3_raw_data["UpdateUserRequestItems"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchUpdateUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserResponse:
    boto3_raw_data: "type_defs.CreateUserResponseTypeDef" = dataclasses.field()

    @cached_property
    def User(self):  # pragma: no cover
        return User.make_one(self.boto3_raw_data["User"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserResponse:
    boto3_raw_data: "type_defs.GetUserResponseTypeDef" = dataclasses.field()

    @cached_property
    def User(self):  # pragma: no cover
        return User.make_one(self.boto3_raw_data["User"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetUserResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetUserResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsersResponse:
    boto3_raw_data: "type_defs.ListUsersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Users(self):  # pragma: no cover
        return User.make_many(self.boto3_raw_data["Users"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListUsersResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetPersonalPINResponse:
    boto3_raw_data: "type_defs.ResetPersonalPINResponseTypeDef" = dataclasses.field()

    @cached_property
    def User(self):  # pragma: no cover
        return User.make_one(self.boto3_raw_data["User"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResetPersonalPINResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetPersonalPINResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserResponse:
    boto3_raw_data: "type_defs.UpdateUserResponseTypeDef" = dataclasses.field()

    @cached_property
    def User(self):  # pragma: no cover
        return User.make_one(self.boto3_raw_data["User"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRoomMembershipResponse:
    boto3_raw_data: "type_defs.CreateRoomMembershipResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RoomMembership(self):  # pragma: no cover
        return RoomMembership.make_one(self.boto3_raw_data["RoomMembership"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRoomMembershipResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRoomMembershipResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoomMembershipsResponse:
    boto3_raw_data: "type_defs.ListRoomMembershipsResponseTypeDef" = dataclasses.field()

    @cached_property
    def RoomMemberships(self):  # pragma: no cover
        return RoomMembership.make_many(self.boto3_raw_data["RoomMemberships"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRoomMembershipsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoomMembershipsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRoomMembershipResponse:
    boto3_raw_data: "type_defs.UpdateRoomMembershipResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RoomMembership(self):  # pragma: no cover
        return RoomMembership.make_one(self.boto3_raw_data["RoomMembership"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRoomMembershipResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRoomMembershipResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePhoneNumberOrderResponse:
    boto3_raw_data: "type_defs.CreatePhoneNumberOrderResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PhoneNumberOrder(self):  # pragma: no cover
        return PhoneNumberOrder.make_one(self.boto3_raw_data["PhoneNumberOrder"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreatePhoneNumberOrderResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePhoneNumberOrderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPhoneNumberOrderResponse:
    boto3_raw_data: "type_defs.GetPhoneNumberOrderResponseTypeDef" = dataclasses.field()

    @cached_property
    def PhoneNumberOrder(self):  # pragma: no cover
        return PhoneNumberOrder.make_one(self.boto3_raw_data["PhoneNumberOrder"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPhoneNumberOrderResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPhoneNumberOrderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPhoneNumberOrdersResponse:
    boto3_raw_data: "type_defs.ListPhoneNumberOrdersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PhoneNumberOrders(self):  # pragma: no cover
        return PhoneNumberOrder.make_many(self.boto3_raw_data["PhoneNumberOrders"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPhoneNumberOrdersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPhoneNumberOrdersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPhoneNumberResponse:
    boto3_raw_data: "type_defs.GetPhoneNumberResponseTypeDef" = dataclasses.field()

    @cached_property
    def PhoneNumber(self):  # pragma: no cover
        return PhoneNumber.make_one(self.boto3_raw_data["PhoneNumber"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPhoneNumberResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPhoneNumberResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPhoneNumbersResponse:
    boto3_raw_data: "type_defs.ListPhoneNumbersResponseTypeDef" = dataclasses.field()

    @cached_property
    def PhoneNumbers(self):  # pragma: no cover
        return PhoneNumber.make_many(self.boto3_raw_data["PhoneNumbers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPhoneNumbersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPhoneNumbersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestorePhoneNumberResponse:
    boto3_raw_data: "type_defs.RestorePhoneNumberResponseTypeDef" = dataclasses.field()

    @cached_property
    def PhoneNumber(self):  # pragma: no cover
        return PhoneNumber.make_one(self.boto3_raw_data["PhoneNumber"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestorePhoneNumberResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestorePhoneNumberResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePhoneNumberResponse:
    boto3_raw_data: "type_defs.UpdatePhoneNumberResponseTypeDef" = dataclasses.field()

    @cached_property
    def PhoneNumber(self):  # pragma: no cover
        return PhoneNumber.make_one(self.boto3_raw_data["PhoneNumber"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePhoneNumberResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePhoneNumberResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRetentionSettingsResponse:
    boto3_raw_data: "type_defs.GetRetentionSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RetentionSettings(self):  # pragma: no cover
        return RetentionSettings.make_one(self.boto3_raw_data["RetentionSettings"])

    InitiateDeletionTimestamp = field("InitiateDeletionTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRetentionSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRetentionSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRetentionSettingsRequest:
    boto3_raw_data: "type_defs.PutRetentionSettingsRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")

    @cached_property
    def RetentionSettings(self):  # pragma: no cover
        return RetentionSettings.make_one(self.boto3_raw_data["RetentionSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutRetentionSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRetentionSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRetentionSettingsResponse:
    boto3_raw_data: "type_defs.PutRetentionSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RetentionSettings(self):  # pragma: no cover
        return RetentionSettings.make_one(self.boto3_raw_data["RetentionSettings"])

    InitiateDeletionTimestamp = field("InitiateDeletionTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutRetentionSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRetentionSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserSettingsResponse:
    boto3_raw_data: "type_defs.GetUserSettingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def UserSettings(self):  # pragma: no cover
        return UserSettings.make_one(self.boto3_raw_data["UserSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUserSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUserSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserSettingsRequest:
    boto3_raw_data: "type_defs.UpdateUserSettingsRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    UserId = field("UserId")

    @cached_property
    def UserSettings(self):  # pragma: no cover
        return UserSettings.make_one(self.boto3_raw_data["UserSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUserSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
