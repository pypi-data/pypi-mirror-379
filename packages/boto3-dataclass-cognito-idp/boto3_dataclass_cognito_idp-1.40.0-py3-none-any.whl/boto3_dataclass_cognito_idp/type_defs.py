# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cognito_idp import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class RecoveryOptionType:
    boto3_raw_data: "type_defs.RecoveryOptionTypeTypeDef" = dataclasses.field()

    Priority = field("Priority")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecoveryOptionTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecoveryOptionTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountTakeoverActionType:
    boto3_raw_data: "type_defs.AccountTakeoverActionTypeTypeDef" = dataclasses.field()

    Notify = field("Notify")
    EventAction = field("EventAction")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountTakeoverActionTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountTakeoverActionTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminAddUserToGroupRequest:
    boto3_raw_data: "type_defs.AdminAddUserToGroupRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    Username = field("Username")
    GroupName = field("GroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdminAddUserToGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminAddUserToGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminConfirmSignUpRequest:
    boto3_raw_data: "type_defs.AdminConfirmSignUpRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    Username = field("Username")
    ClientMetadata = field("ClientMetadata")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdminConfirmSignUpRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminConfirmSignUpRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageTemplateType:
    boto3_raw_data: "type_defs.MessageTemplateTypeTypeDef" = dataclasses.field()

    SMSMessage = field("SMSMessage")
    EmailMessage = field("EmailMessage")
    EmailSubject = field("EmailSubject")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessageTemplateTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageTemplateTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeType:
    boto3_raw_data: "type_defs.AttributeTypeTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributeTypeTypeDef"]],
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
class AdminDeleteUserAttributesRequest:
    boto3_raw_data: "type_defs.AdminDeleteUserAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    Username = field("Username")
    UserAttributeNames = field("UserAttributeNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AdminDeleteUserAttributesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminDeleteUserAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminDeleteUserRequest:
    boto3_raw_data: "type_defs.AdminDeleteUserRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    Username = field("Username")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdminDeleteUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminDeleteUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProviderUserIdentifierType:
    boto3_raw_data: "type_defs.ProviderUserIdentifierTypeTypeDef" = dataclasses.field()

    ProviderName = field("ProviderName")
    ProviderAttributeName = field("ProviderAttributeName")
    ProviderAttributeValue = field("ProviderAttributeValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProviderUserIdentifierTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProviderUserIdentifierTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminDisableUserRequest:
    boto3_raw_data: "type_defs.AdminDisableUserRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    Username = field("Username")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdminDisableUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminDisableUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminEnableUserRequest:
    boto3_raw_data: "type_defs.AdminEnableUserRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    Username = field("Username")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdminEnableUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminEnableUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminForgetDeviceRequest:
    boto3_raw_data: "type_defs.AdminForgetDeviceRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    Username = field("Username")
    DeviceKey = field("DeviceKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdminForgetDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminForgetDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminGetDeviceRequest:
    boto3_raw_data: "type_defs.AdminGetDeviceRequestTypeDef" = dataclasses.field()

    DeviceKey = field("DeviceKey")
    UserPoolId = field("UserPoolId")
    Username = field("Username")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdminGetDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminGetDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminGetUserRequest:
    boto3_raw_data: "type_defs.AdminGetUserRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    Username = field("Username")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdminGetUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminGetUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MFAOptionType:
    boto3_raw_data: "type_defs.MFAOptionTypeTypeDef" = dataclasses.field()

    DeliveryMedium = field("DeliveryMedium")
    AttributeName = field("AttributeName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MFAOptionTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MFAOptionTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsMetadataType:
    boto3_raw_data: "type_defs.AnalyticsMetadataTypeTypeDef" = dataclasses.field()

    AnalyticsEndpointId = field("AnalyticsEndpointId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsMetadataTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsMetadataTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminListDevicesRequest:
    boto3_raw_data: "type_defs.AdminListDevicesRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    Username = field("Username")
    Limit = field("Limit")
    PaginationToken = field("PaginationToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdminListDevicesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminListDevicesRequestTypeDef"]
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
class AdminListGroupsForUserRequest:
    boto3_raw_data: "type_defs.AdminListGroupsForUserRequestTypeDef" = (
        dataclasses.field()
    )

    Username = field("Username")
    UserPoolId = field("UserPoolId")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AdminListGroupsForUserRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminListGroupsForUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupType:
    boto3_raw_data: "type_defs.GroupTypeTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    UserPoolId = field("UserPoolId")
    Description = field("Description")
    RoleArn = field("RoleArn")
    Precedence = field("Precedence")
    LastModifiedDate = field("LastModifiedDate")
    CreationDate = field("CreationDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminListUserAuthEventsRequest:
    boto3_raw_data: "type_defs.AdminListUserAuthEventsRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    Username = field("Username")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AdminListUserAuthEventsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminListUserAuthEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminRemoveUserFromGroupRequest:
    boto3_raw_data: "type_defs.AdminRemoveUserFromGroupRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    Username = field("Username")
    GroupName = field("GroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AdminRemoveUserFromGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminRemoveUserFromGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminResetUserPasswordRequest:
    boto3_raw_data: "type_defs.AdminResetUserPasswordRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    Username = field("Username")
    ClientMetadata = field("ClientMetadata")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AdminResetUserPasswordRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminResetUserPasswordRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailMfaSettingsType:
    boto3_raw_data: "type_defs.EmailMfaSettingsTypeTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    PreferredMfa = field("PreferredMfa")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmailMfaSettingsTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailMfaSettingsTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SMSMfaSettingsType:
    boto3_raw_data: "type_defs.SMSMfaSettingsTypeTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    PreferredMfa = field("PreferredMfa")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SMSMfaSettingsTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SMSMfaSettingsTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SoftwareTokenMfaSettingsType:
    boto3_raw_data: "type_defs.SoftwareTokenMfaSettingsTypeTypeDef" = (
        dataclasses.field()
    )

    Enabled = field("Enabled")
    PreferredMfa = field("PreferredMfa")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SoftwareTokenMfaSettingsTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SoftwareTokenMfaSettingsTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminSetUserPasswordRequest:
    boto3_raw_data: "type_defs.AdminSetUserPasswordRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    Username = field("Username")
    Password = field("Password")
    Permanent = field("Permanent")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdminSetUserPasswordRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminSetUserPasswordRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminUpdateAuthEventFeedbackRequest:
    boto3_raw_data: "type_defs.AdminUpdateAuthEventFeedbackRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    Username = field("Username")
    EventId = field("EventId")
    FeedbackValue = field("FeedbackValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AdminUpdateAuthEventFeedbackRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminUpdateAuthEventFeedbackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminUpdateDeviceStatusRequest:
    boto3_raw_data: "type_defs.AdminUpdateDeviceStatusRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    Username = field("Username")
    DeviceKey = field("DeviceKey")
    DeviceRememberedStatus = field("DeviceRememberedStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AdminUpdateDeviceStatusRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminUpdateDeviceStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminUserGlobalSignOutRequest:
    boto3_raw_data: "type_defs.AdminUserGlobalSignOutRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    Username = field("Username")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AdminUserGlobalSignOutRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminUserGlobalSignOutRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdvancedSecurityAdditionalFlowsType:
    boto3_raw_data: "type_defs.AdvancedSecurityAdditionalFlowsTypeTypeDef" = (
        dataclasses.field()
    )

    CustomAuthMode = field("CustomAuthMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AdvancedSecurityAdditionalFlowsTypeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdvancedSecurityAdditionalFlowsTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsConfigurationType:
    boto3_raw_data: "type_defs.AnalyticsConfigurationTypeTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    ApplicationArn = field("ApplicationArn")
    RoleArn = field("RoleArn")
    ExternalId = field("ExternalId")
    UserDataShared = field("UserDataShared")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsConfigurationTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsConfigurationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetTypeOutput:
    boto3_raw_data: "type_defs.AssetTypeOutputTypeDef" = dataclasses.field()

    Category = field("Category")
    ColorMode = field("ColorMode")
    Extension = field("Extension")
    Bytes = field("Bytes")
    ResourceId = field("ResourceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetTypeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssetTypeOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateSoftwareTokenRequest:
    boto3_raw_data: "type_defs.AssociateSoftwareTokenRequestTypeDef" = (
        dataclasses.field()
    )

    AccessToken = field("AccessToken")
    Session = field("Session")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateSoftwareTokenRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateSoftwareTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChallengeResponseType:
    boto3_raw_data: "type_defs.ChallengeResponseTypeTypeDef" = dataclasses.field()

    ChallengeName = field("ChallengeName")
    ChallengeResponse = field("ChallengeResponse")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChallengeResponseTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChallengeResponseTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventContextDataType:
    boto3_raw_data: "type_defs.EventContextDataTypeTypeDef" = dataclasses.field()

    IpAddress = field("IpAddress")
    DeviceName = field("DeviceName")
    Timezone = field("Timezone")
    City = field("City")
    Country = field("Country")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventContextDataTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventContextDataTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventFeedbackType:
    boto3_raw_data: "type_defs.EventFeedbackTypeTypeDef" = dataclasses.field()

    FeedbackValue = field("FeedbackValue")
    Provider = field("Provider")
    FeedbackDate = field("FeedbackDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventFeedbackTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventFeedbackTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventRiskType:
    boto3_raw_data: "type_defs.EventRiskTypeTypeDef" = dataclasses.field()

    RiskDecision = field("RiskDecision")
    RiskLevel = field("RiskLevel")
    CompromisedCredentialsDetected = field("CompromisedCredentialsDetected")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventRiskTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventRiskTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NewDeviceMetadataType:
    boto3_raw_data: "type_defs.NewDeviceMetadataTypeTypeDef" = dataclasses.field()

    DeviceKey = field("DeviceKey")
    DeviceGroupKey = field("DeviceGroupKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NewDeviceMetadataTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NewDeviceMetadataTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangePasswordRequest:
    boto3_raw_data: "type_defs.ChangePasswordRequestTypeDef" = dataclasses.field()

    ProposedPassword = field("ProposedPassword")
    AccessToken = field("AccessToken")
    PreviousPassword = field("PreviousPassword")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChangePasswordRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangePasswordRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchLogsConfigurationType:
    boto3_raw_data: "type_defs.CloudWatchLogsConfigurationTypeTypeDef" = (
        dataclasses.field()
    )

    LogGroupArn = field("LogGroupArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CloudWatchLogsConfigurationTypeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLogsConfigurationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeDeliveryDetailsType:
    boto3_raw_data: "type_defs.CodeDeliveryDetailsTypeTypeDef" = dataclasses.field()

    Destination = field("Destination")
    DeliveryMedium = field("DeliveryMedium")
    AttributeName = field("AttributeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodeDeliveryDetailsTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeDeliveryDetailsTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompleteWebAuthnRegistrationRequest:
    boto3_raw_data: "type_defs.CompleteWebAuthnRegistrationRequestTypeDef" = (
        dataclasses.field()
    )

    AccessToken = field("AccessToken")
    Credential = field("Credential")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CompleteWebAuthnRegistrationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompleteWebAuthnRegistrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompromisedCredentialsActionsType:
    boto3_raw_data: "type_defs.CompromisedCredentialsActionsTypeTypeDef" = (
        dataclasses.field()
    )

    EventAction = field("EventAction")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CompromisedCredentialsActionsTypeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompromisedCredentialsActionsTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeviceSecretVerifierConfigType:
    boto3_raw_data: "type_defs.DeviceSecretVerifierConfigTypeTypeDef" = (
        dataclasses.field()
    )

    PasswordVerifier = field("PasswordVerifier")
    Salt = field("Salt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeviceSecretVerifierConfigTypeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeviceSecretVerifierConfigTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserContextDataType:
    boto3_raw_data: "type_defs.UserContextDataTypeTypeDef" = dataclasses.field()

    IpAddress = field("IpAddress")
    EncodedData = field("EncodedData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserContextDataTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserContextDataTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpHeader:
    boto3_raw_data: "type_defs.HttpHeaderTypeDef" = dataclasses.field()

    headerName = field("headerName")
    headerValue = field("headerValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HttpHeaderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HttpHeaderTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGroupRequest:
    boto3_raw_data: "type_defs.CreateGroupRequestTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    UserPoolId = field("UserPoolId")
    Description = field("Description")
    RoleArn = field("RoleArn")
    Precedence = field("Precedence")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIdentityProviderRequest:
    boto3_raw_data: "type_defs.CreateIdentityProviderRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    ProviderName = field("ProviderName")
    ProviderType = field("ProviderType")
    ProviderDetails = field("ProviderDetails")
    AttributeMapping = field("AttributeMapping")
    IdpIdentifiers = field("IdpIdentifiers")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateIdentityProviderRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIdentityProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityProviderType:
    boto3_raw_data: "type_defs.IdentityProviderTypeTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    ProviderName = field("ProviderName")
    ProviderType = field("ProviderType")
    ProviderDetails = field("ProviderDetails")
    AttributeMapping = field("AttributeMapping")
    IdpIdentifiers = field("IdpIdentifiers")
    LastModifiedDate = field("LastModifiedDate")
    CreationDate = field("CreationDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentityProviderTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityProviderTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceServerScopeType:
    boto3_raw_data: "type_defs.ResourceServerScopeTypeTypeDef" = dataclasses.field()

    ScopeName = field("ScopeName")
    ScopeDescription = field("ScopeDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceServerScopeTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceServerScopeTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTermsRequest:
    boto3_raw_data: "type_defs.CreateTermsRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    ClientId = field("ClientId")
    TermsName = field("TermsName")
    TermsSource = field("TermsSource")
    Enforcement = field("Enforcement")
    Links = field("Links")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTermsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTermsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TermsType:
    boto3_raw_data: "type_defs.TermsTypeTypeDef" = dataclasses.field()

    TermsId = field("TermsId")
    UserPoolId = field("UserPoolId")
    ClientId = field("ClientId")
    TermsName = field("TermsName")
    TermsSource = field("TermsSource")
    Enforcement = field("Enforcement")
    Links = field("Links")
    CreationDate = field("CreationDate")
    LastModifiedDate = field("LastModifiedDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TermsTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TermsTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserImportJobRequest:
    boto3_raw_data: "type_defs.CreateUserImportJobRequestTypeDef" = dataclasses.field()

    JobName = field("JobName")
    UserPoolId = field("UserPoolId")
    CloudWatchLogsRoleArn = field("CloudWatchLogsRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUserImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserImportJobType:
    boto3_raw_data: "type_defs.UserImportJobTypeTypeDef" = dataclasses.field()

    JobName = field("JobName")
    JobId = field("JobId")
    UserPoolId = field("UserPoolId")
    PreSignedUrl = field("PreSignedUrl")
    CreationDate = field("CreationDate")
    StartDate = field("StartDate")
    CompletionDate = field("CompletionDate")
    Status = field("Status")
    CloudWatchLogsRoleArn = field("CloudWatchLogsRoleArn")
    ImportedUsers = field("ImportedUsers")
    SkippedUsers = field("SkippedUsers")
    FailedUsers = field("FailedUsers")
    CompletionMessage = field("CompletionMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserImportJobTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserImportJobTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RefreshTokenRotationType:
    boto3_raw_data: "type_defs.RefreshTokenRotationTypeTypeDef" = dataclasses.field()

    Feature = field("Feature")
    RetryGracePeriodSeconds = field("RetryGracePeriodSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RefreshTokenRotationTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RefreshTokenRotationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TokenValidityUnitsType:
    boto3_raw_data: "type_defs.TokenValidityUnitsTypeTypeDef" = dataclasses.field()

    AccessToken = field("AccessToken")
    IdToken = field("IdToken")
    RefreshToken = field("RefreshToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TokenValidityUnitsTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TokenValidityUnitsTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomDomainConfigType:
    boto3_raw_data: "type_defs.CustomDomainConfigTypeTypeDef" = dataclasses.field()

    CertificateArn = field("CertificateArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomDomainConfigTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomDomainConfigTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeviceConfigurationType:
    boto3_raw_data: "type_defs.DeviceConfigurationTypeTypeDef" = dataclasses.field()

    ChallengeRequiredOnNewDevice = field("ChallengeRequiredOnNewDevice")
    DeviceOnlyRememberedOnUserPrompt = field("DeviceOnlyRememberedOnUserPrompt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeviceConfigurationTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeviceConfigurationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailConfigurationType:
    boto3_raw_data: "type_defs.EmailConfigurationTypeTypeDef" = dataclasses.field()

    SourceArn = field("SourceArn")
    ReplyToEmailAddress = field("ReplyToEmailAddress")
    EmailSendingAccount = field("EmailSendingAccount")
    From = field("From")
    ConfigurationSet = field("ConfigurationSet")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmailConfigurationTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailConfigurationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SmsConfigurationType:
    boto3_raw_data: "type_defs.SmsConfigurationTypeTypeDef" = dataclasses.field()

    SnsCallerArn = field("SnsCallerArn")
    ExternalId = field("ExternalId")
    SnsRegion = field("SnsRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SmsConfigurationTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SmsConfigurationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsernameConfigurationType:
    boto3_raw_data: "type_defs.UsernameConfigurationTypeTypeDef" = dataclasses.field()

    CaseSensitive = field("CaseSensitive")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UsernameConfigurationTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UsernameConfigurationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerificationMessageTemplateType:
    boto3_raw_data: "type_defs.VerificationMessageTemplateTypeTypeDef" = (
        dataclasses.field()
    )

    SmsMessage = field("SmsMessage")
    EmailMessage = field("EmailMessage")
    EmailSubject = field("EmailSubject")
    EmailMessageByLink = field("EmailMessageByLink")
    EmailSubjectByLink = field("EmailSubjectByLink")
    DefaultEmailOption = field("DefaultEmailOption")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VerificationMessageTemplateTypeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerificationMessageTemplateTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomEmailLambdaVersionConfigType:
    boto3_raw_data: "type_defs.CustomEmailLambdaVersionConfigTypeTypeDef" = (
        dataclasses.field()
    )

    LambdaVersion = field("LambdaVersion")
    LambdaArn = field("LambdaArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomEmailLambdaVersionConfigTypeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomEmailLambdaVersionConfigTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomSMSLambdaVersionConfigType:
    boto3_raw_data: "type_defs.CustomSMSLambdaVersionConfigTypeTypeDef" = (
        dataclasses.field()
    )

    LambdaVersion = field("LambdaVersion")
    LambdaArn = field("LambdaArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomSMSLambdaVersionConfigTypeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomSMSLambdaVersionConfigTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGroupRequest:
    boto3_raw_data: "type_defs.DeleteGroupRequestTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    UserPoolId = field("UserPoolId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIdentityProviderRequest:
    boto3_raw_data: "type_defs.DeleteIdentityProviderRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    ProviderName = field("ProviderName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteIdentityProviderRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIdentityProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteManagedLoginBrandingRequest:
    boto3_raw_data: "type_defs.DeleteManagedLoginBrandingRequestTypeDef" = (
        dataclasses.field()
    )

    ManagedLoginBrandingId = field("ManagedLoginBrandingId")
    UserPoolId = field("UserPoolId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteManagedLoginBrandingRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteManagedLoginBrandingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourceServerRequest:
    boto3_raw_data: "type_defs.DeleteResourceServerRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourceServerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourceServerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTermsRequest:
    boto3_raw_data: "type_defs.DeleteTermsRequestTypeDef" = dataclasses.field()

    TermsId = field("TermsId")
    UserPoolId = field("UserPoolId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTermsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTermsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserAttributesRequest:
    boto3_raw_data: "type_defs.DeleteUserAttributesRequestTypeDef" = dataclasses.field()

    UserAttributeNames = field("UserAttributeNames")
    AccessToken = field("AccessToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteUserAttributesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserPoolClientRequest:
    boto3_raw_data: "type_defs.DeleteUserPoolClientRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    ClientId = field("ClientId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteUserPoolClientRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserPoolClientRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserPoolDomainRequest:
    boto3_raw_data: "type_defs.DeleteUserPoolDomainRequestTypeDef" = dataclasses.field()

    Domain = field("Domain")
    UserPoolId = field("UserPoolId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteUserPoolDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserPoolDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserPoolRequest:
    boto3_raw_data: "type_defs.DeleteUserPoolRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteUserPoolRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserPoolRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserRequest:
    boto3_raw_data: "type_defs.DeleteUserRequestTypeDef" = dataclasses.field()

    AccessToken = field("AccessToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWebAuthnCredentialRequest:
    boto3_raw_data: "type_defs.DeleteWebAuthnCredentialRequestTypeDef" = (
        dataclasses.field()
    )

    AccessToken = field("AccessToken")
    CredentialId = field("CredentialId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteWebAuthnCredentialRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWebAuthnCredentialRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIdentityProviderRequest:
    boto3_raw_data: "type_defs.DescribeIdentityProviderRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    ProviderName = field("ProviderName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeIdentityProviderRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIdentityProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeManagedLoginBrandingByClientRequest:
    boto3_raw_data: "type_defs.DescribeManagedLoginBrandingByClientRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    ClientId = field("ClientId")
    ReturnMergedResources = field("ReturnMergedResources")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeManagedLoginBrandingByClientRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeManagedLoginBrandingByClientRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeManagedLoginBrandingRequest:
    boto3_raw_data: "type_defs.DescribeManagedLoginBrandingRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    ManagedLoginBrandingId = field("ManagedLoginBrandingId")
    ReturnMergedResources = field("ReturnMergedResources")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeManagedLoginBrandingRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeManagedLoginBrandingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourceServerRequest:
    boto3_raw_data: "type_defs.DescribeResourceServerRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeResourceServerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourceServerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRiskConfigurationRequest:
    boto3_raw_data: "type_defs.DescribeRiskConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    ClientId = field("ClientId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeRiskConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRiskConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTermsRequest:
    boto3_raw_data: "type_defs.DescribeTermsRequestTypeDef" = dataclasses.field()

    TermsId = field("TermsId")
    UserPoolId = field("UserPoolId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTermsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTermsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserImportJobRequest:
    boto3_raw_data: "type_defs.DescribeUserImportJobRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    JobId = field("JobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUserImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserPoolClientRequest:
    boto3_raw_data: "type_defs.DescribeUserPoolClientRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    ClientId = field("ClientId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeUserPoolClientRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserPoolClientRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserPoolDomainRequest:
    boto3_raw_data: "type_defs.DescribeUserPoolDomainRequestTypeDef" = (
        dataclasses.field()
    )

    Domain = field("Domain")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeUserPoolDomainRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserPoolDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserPoolRequest:
    boto3_raw_data: "type_defs.DescribeUserPoolRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUserPoolRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserPoolRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailMfaConfigType:
    boto3_raw_data: "type_defs.EmailMfaConfigTypeTypeDef" = dataclasses.field()

    Message = field("Message")
    Subject = field("Subject")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmailMfaConfigTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailMfaConfigTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirehoseConfigurationType:
    boto3_raw_data: "type_defs.FirehoseConfigurationTypeTypeDef" = dataclasses.field()

    StreamArn = field("StreamArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FirehoseConfigurationTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FirehoseConfigurationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ForgetDeviceRequest:
    boto3_raw_data: "type_defs.ForgetDeviceRequestTypeDef" = dataclasses.field()

    DeviceKey = field("DeviceKey")
    AccessToken = field("AccessToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ForgetDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ForgetDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCSVHeaderRequest:
    boto3_raw_data: "type_defs.GetCSVHeaderRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCSVHeaderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCSVHeaderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeviceRequest:
    boto3_raw_data: "type_defs.GetDeviceRequestTypeDef" = dataclasses.field()

    DeviceKey = field("DeviceKey")
    AccessToken = field("AccessToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDeviceRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupRequest:
    boto3_raw_data: "type_defs.GetGroupRequestTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    UserPoolId = field("UserPoolId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGroupRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetGroupRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentityProviderByIdentifierRequest:
    boto3_raw_data: "type_defs.GetIdentityProviderByIdentifierRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    IdpIdentifier = field("IdpIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetIdentityProviderByIdentifierRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentityProviderByIdentifierRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLogDeliveryConfigurationRequest:
    boto3_raw_data: "type_defs.GetLogDeliveryConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetLogDeliveryConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLogDeliveryConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSigningCertificateRequest:
    boto3_raw_data: "type_defs.GetSigningCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSigningCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSigningCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTokensFromRefreshTokenRequest:
    boto3_raw_data: "type_defs.GetTokensFromRefreshTokenRequestTypeDef" = (
        dataclasses.field()
    )

    RefreshToken = field("RefreshToken")
    ClientId = field("ClientId")
    ClientSecret = field("ClientSecret")
    DeviceKey = field("DeviceKey")
    ClientMetadata = field("ClientMetadata")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetTokensFromRefreshTokenRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTokensFromRefreshTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUICustomizationRequest:
    boto3_raw_data: "type_defs.GetUICustomizationRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    ClientId = field("ClientId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUICustomizationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUICustomizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UICustomizationType:
    boto3_raw_data: "type_defs.UICustomizationTypeTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    ClientId = field("ClientId")
    ImageUrl = field("ImageUrl")
    CSS = field("CSS")
    CSSVersion = field("CSSVersion")
    LastModifiedDate = field("LastModifiedDate")
    CreationDate = field("CreationDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UICustomizationTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UICustomizationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserAttributeVerificationCodeRequest:
    boto3_raw_data: "type_defs.GetUserAttributeVerificationCodeRequestTypeDef" = (
        dataclasses.field()
    )

    AccessToken = field("AccessToken")
    AttributeName = field("AttributeName")
    ClientMetadata = field("ClientMetadata")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetUserAttributeVerificationCodeRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUserAttributeVerificationCodeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserAuthFactorsRequest:
    boto3_raw_data: "type_defs.GetUserAuthFactorsRequestTypeDef" = dataclasses.field()

    AccessToken = field("AccessToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUserAuthFactorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUserAuthFactorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserPoolMfaConfigRequest:
    boto3_raw_data: "type_defs.GetUserPoolMfaConfigRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUserPoolMfaConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUserPoolMfaConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SoftwareTokenMfaConfigType:
    boto3_raw_data: "type_defs.SoftwareTokenMfaConfigTypeTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SoftwareTokenMfaConfigTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SoftwareTokenMfaConfigTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebAuthnConfigurationType:
    boto3_raw_data: "type_defs.WebAuthnConfigurationTypeTypeDef" = dataclasses.field()

    RelyingPartyId = field("RelyingPartyId")
    UserVerification = field("UserVerification")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WebAuthnConfigurationTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebAuthnConfigurationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserRequest:
    boto3_raw_data: "type_defs.GetUserRequestTypeDef" = dataclasses.field()

    AccessToken = field("AccessToken")

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
class GlobalSignOutRequest:
    boto3_raw_data: "type_defs.GlobalSignOutRequestTypeDef" = dataclasses.field()

    AccessToken = field("AccessToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlobalSignOutRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalSignOutRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PreTokenGenerationVersionConfigType:
    boto3_raw_data: "type_defs.PreTokenGenerationVersionConfigTypeTypeDef" = (
        dataclasses.field()
    )

    LambdaVersion = field("LambdaVersion")
    LambdaArn = field("LambdaArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PreTokenGenerationVersionConfigTypeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PreTokenGenerationVersionConfigTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDevicesRequest:
    boto3_raw_data: "type_defs.ListDevicesRequestTypeDef" = dataclasses.field()

    AccessToken = field("AccessToken")
    Limit = field("Limit")
    PaginationToken = field("PaginationToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDevicesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDevicesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsRequest:
    boto3_raw_data: "type_defs.ListGroupsRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListGroupsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentityProvidersRequest:
    boto3_raw_data: "type_defs.ListIdentityProvidersRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdentityProvidersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentityProvidersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProviderDescription:
    boto3_raw_data: "type_defs.ProviderDescriptionTypeDef" = dataclasses.field()

    ProviderName = field("ProviderName")
    ProviderType = field("ProviderType")
    LastModifiedDate = field("LastModifiedDate")
    CreationDate = field("CreationDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProviderDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProviderDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceServersRequest:
    boto3_raw_data: "type_defs.ListResourceServersRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourceServersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceServersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTermsRequest:
    boto3_raw_data: "type_defs.ListTermsRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTermsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTermsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TermsDescriptionType:
    boto3_raw_data: "type_defs.TermsDescriptionTypeTypeDef" = dataclasses.field()

    TermsId = field("TermsId")
    TermsName = field("TermsName")
    Enforcement = field("Enforcement")
    CreationDate = field("CreationDate")
    LastModifiedDate = field("LastModifiedDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TermsDescriptionTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TermsDescriptionTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserImportJobsRequest:
    boto3_raw_data: "type_defs.ListUserImportJobsRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    MaxResults = field("MaxResults")
    PaginationToken = field("PaginationToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUserImportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserImportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserPoolClientsRequest:
    boto3_raw_data: "type_defs.ListUserPoolClientsRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUserPoolClientsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserPoolClientsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserPoolClientDescription:
    boto3_raw_data: "type_defs.UserPoolClientDescriptionTypeDef" = dataclasses.field()

    ClientId = field("ClientId")
    UserPoolId = field("UserPoolId")
    ClientName = field("ClientName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserPoolClientDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserPoolClientDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserPoolsRequest:
    boto3_raw_data: "type_defs.ListUserPoolsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUserPoolsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserPoolsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsersInGroupRequest:
    boto3_raw_data: "type_defs.ListUsersInGroupRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    GroupName = field("GroupName")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUsersInGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersInGroupRequestTypeDef"]
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

    UserPoolId = field("UserPoolId")
    AttributesToGet = field("AttributesToGet")
    Limit = field("Limit")
    PaginationToken = field("PaginationToken")
    Filter = field("Filter")

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
class ListWebAuthnCredentialsRequest:
    boto3_raw_data: "type_defs.ListWebAuthnCredentialsRequestTypeDef" = (
        dataclasses.field()
    )

    AccessToken = field("AccessToken")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWebAuthnCredentialsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWebAuthnCredentialsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebAuthnCredentialDescription:
    boto3_raw_data: "type_defs.WebAuthnCredentialDescriptionTypeDef" = (
        dataclasses.field()
    )

    CredentialId = field("CredentialId")
    FriendlyCredentialName = field("FriendlyCredentialName")
    RelyingPartyId = field("RelyingPartyId")
    AuthenticatorTransports = field("AuthenticatorTransports")
    CreatedAt = field("CreatedAt")
    AuthenticatorAttachment = field("AuthenticatorAttachment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WebAuthnCredentialDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebAuthnCredentialDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ConfigurationType:
    boto3_raw_data: "type_defs.S3ConfigurationTypeTypeDef" = dataclasses.field()

    BucketArn = field("BucketArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3ConfigurationTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ConfigurationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotifyEmailType:
    boto3_raw_data: "type_defs.NotifyEmailTypeTypeDef" = dataclasses.field()

    Subject = field("Subject")
    HtmlBody = field("HtmlBody")
    TextBody = field("TextBody")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NotifyEmailTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NotifyEmailTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NumberAttributeConstraintsType:
    boto3_raw_data: "type_defs.NumberAttributeConstraintsTypeTypeDef" = (
        dataclasses.field()
    )

    MinValue = field("MinValue")
    MaxValue = field("MaxValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.NumberAttributeConstraintsTypeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NumberAttributeConstraintsTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PasswordPolicyType:
    boto3_raw_data: "type_defs.PasswordPolicyTypeTypeDef" = dataclasses.field()

    MinimumLength = field("MinimumLength")
    RequireUppercase = field("RequireUppercase")
    RequireLowercase = field("RequireLowercase")
    RequireNumbers = field("RequireNumbers")
    RequireSymbols = field("RequireSymbols")
    PasswordHistorySize = field("PasswordHistorySize")
    TemporaryPasswordValidityDays = field("TemporaryPasswordValidityDays")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PasswordPolicyTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PasswordPolicyTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeTokenRequest:
    boto3_raw_data: "type_defs.RevokeTokenRequestTypeDef" = dataclasses.field()

    Token = field("Token")
    ClientId = field("ClientId")
    ClientSecret = field("ClientSecret")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RevokeTokenRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RiskExceptionConfigurationTypeOutput:
    boto3_raw_data: "type_defs.RiskExceptionConfigurationTypeOutputTypeDef" = (
        dataclasses.field()
    )

    BlockedIPRangeList = field("BlockedIPRangeList")
    SkippedIPRangeList = field("SkippedIPRangeList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RiskExceptionConfigurationTypeOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RiskExceptionConfigurationTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RiskExceptionConfigurationType:
    boto3_raw_data: "type_defs.RiskExceptionConfigurationTypeTypeDef" = (
        dataclasses.field()
    )

    BlockedIPRangeList = field("BlockedIPRangeList")
    SkippedIPRangeList = field("SkippedIPRangeList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RiskExceptionConfigurationTypeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RiskExceptionConfigurationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StringAttributeConstraintsType:
    boto3_raw_data: "type_defs.StringAttributeConstraintsTypeTypeDef" = (
        dataclasses.field()
    )

    MinLength = field("MinLength")
    MaxLength = field("MaxLength")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StringAttributeConstraintsTypeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StringAttributeConstraintsTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignInPolicyTypeOutput:
    boto3_raw_data: "type_defs.SignInPolicyTypeOutputTypeDef" = dataclasses.field()

    AllowedFirstAuthFactors = field("AllowedFirstAuthFactors")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SignInPolicyTypeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SignInPolicyTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignInPolicyType:
    boto3_raw_data: "type_defs.SignInPolicyTypeTypeDef" = dataclasses.field()

    AllowedFirstAuthFactors = field("AllowedFirstAuthFactors")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SignInPolicyTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SignInPolicyTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartUserImportJobRequest:
    boto3_raw_data: "type_defs.StartUserImportJobRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    JobId = field("JobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartUserImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartUserImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartWebAuthnRegistrationRequest:
    boto3_raw_data: "type_defs.StartWebAuthnRegistrationRequestTypeDef" = (
        dataclasses.field()
    )

    AccessToken = field("AccessToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartWebAuthnRegistrationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartWebAuthnRegistrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopUserImportJobRequest:
    boto3_raw_data: "type_defs.StopUserImportJobRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    JobId = field("JobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopUserImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopUserImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAuthEventFeedbackRequest:
    boto3_raw_data: "type_defs.UpdateAuthEventFeedbackRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    Username = field("Username")
    EventId = field("EventId")
    FeedbackToken = field("FeedbackToken")
    FeedbackValue = field("FeedbackValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAuthEventFeedbackRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAuthEventFeedbackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDeviceStatusRequest:
    boto3_raw_data: "type_defs.UpdateDeviceStatusRequestTypeDef" = dataclasses.field()

    AccessToken = field("AccessToken")
    DeviceKey = field("DeviceKey")
    DeviceRememberedStatus = field("DeviceRememberedStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDeviceStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDeviceStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGroupRequest:
    boto3_raw_data: "type_defs.UpdateGroupRequestTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    UserPoolId = field("UserPoolId")
    Description = field("Description")
    RoleArn = field("RoleArn")
    Precedence = field("Precedence")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIdentityProviderRequest:
    boto3_raw_data: "type_defs.UpdateIdentityProviderRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    ProviderName = field("ProviderName")
    ProviderDetails = field("ProviderDetails")
    AttributeMapping = field("AttributeMapping")
    IdpIdentifiers = field("IdpIdentifiers")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateIdentityProviderRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIdentityProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTermsRequest:
    boto3_raw_data: "type_defs.UpdateTermsRequestTypeDef" = dataclasses.field()

    TermsId = field("TermsId")
    UserPoolId = field("UserPoolId")
    TermsName = field("TermsName")
    TermsSource = field("TermsSource")
    Enforcement = field("Enforcement")
    Links = field("Links")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTermsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTermsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserAttributeUpdateSettingsTypeOutput:
    boto3_raw_data: "type_defs.UserAttributeUpdateSettingsTypeOutputTypeDef" = (
        dataclasses.field()
    )

    AttributesRequireVerificationBeforeUpdate = field(
        "AttributesRequireVerificationBeforeUpdate"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UserAttributeUpdateSettingsTypeOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserAttributeUpdateSettingsTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserAttributeUpdateSettingsType:
    boto3_raw_data: "type_defs.UserAttributeUpdateSettingsTypeTypeDef" = (
        dataclasses.field()
    )

    AttributesRequireVerificationBeforeUpdate = field(
        "AttributesRequireVerificationBeforeUpdate"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UserAttributeUpdateSettingsTypeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserAttributeUpdateSettingsTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifySoftwareTokenRequest:
    boto3_raw_data: "type_defs.VerifySoftwareTokenRequestTypeDef" = dataclasses.field()

    UserCode = field("UserCode")
    AccessToken = field("AccessToken")
    Session = field("Session")
    FriendlyDeviceName = field("FriendlyDeviceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VerifySoftwareTokenRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifySoftwareTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyUserAttributeRequest:
    boto3_raw_data: "type_defs.VerifyUserAttributeRequestTypeDef" = dataclasses.field()

    AccessToken = field("AccessToken")
    AttributeName = field("AttributeName")
    Code = field("Code")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VerifyUserAttributeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyUserAttributeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountRecoverySettingTypeOutput:
    boto3_raw_data: "type_defs.AccountRecoverySettingTypeOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RecoveryMechanisms(self):  # pragma: no cover
        return RecoveryOptionType.make_many(self.boto3_raw_data["RecoveryMechanisms"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AccountRecoverySettingTypeOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountRecoverySettingTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountRecoverySettingType:
    boto3_raw_data: "type_defs.AccountRecoverySettingTypeTypeDef" = dataclasses.field()

    @cached_property
    def RecoveryMechanisms(self):  # pragma: no cover
        return RecoveryOptionType.make_many(self.boto3_raw_data["RecoveryMechanisms"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountRecoverySettingTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountRecoverySettingTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountTakeoverActionsType:
    boto3_raw_data: "type_defs.AccountTakeoverActionsTypeTypeDef" = dataclasses.field()

    @cached_property
    def LowAction(self):  # pragma: no cover
        return AccountTakeoverActionType.make_one(self.boto3_raw_data["LowAction"])

    @cached_property
    def MediumAction(self):  # pragma: no cover
        return AccountTakeoverActionType.make_one(self.boto3_raw_data["MediumAction"])

    @cached_property
    def HighAction(self):  # pragma: no cover
        return AccountTakeoverActionType.make_one(self.boto3_raw_data["HighAction"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountTakeoverActionsTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountTakeoverActionsTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminCreateUserConfigType:
    boto3_raw_data: "type_defs.AdminCreateUserConfigTypeTypeDef" = dataclasses.field()

    AllowAdminCreateUserOnly = field("AllowAdminCreateUserOnly")
    UnusedAccountValidityDays = field("UnusedAccountValidityDays")

    @cached_property
    def InviteMessageTemplate(self):  # pragma: no cover
        return MessageTemplateType.make_one(
            self.boto3_raw_data["InviteMessageTemplate"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdminCreateUserConfigTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminCreateUserConfigTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminCreateUserRequest:
    boto3_raw_data: "type_defs.AdminCreateUserRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    Username = field("Username")

    @cached_property
    def UserAttributes(self):  # pragma: no cover
        return AttributeType.make_many(self.boto3_raw_data["UserAttributes"])

    @cached_property
    def ValidationData(self):  # pragma: no cover
        return AttributeType.make_many(self.boto3_raw_data["ValidationData"])

    TemporaryPassword = field("TemporaryPassword")
    ForceAliasCreation = field("ForceAliasCreation")
    MessageAction = field("MessageAction")
    DesiredDeliveryMediums = field("DesiredDeliveryMediums")
    ClientMetadata = field("ClientMetadata")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdminCreateUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminCreateUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminUpdateUserAttributesRequest:
    boto3_raw_data: "type_defs.AdminUpdateUserAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    Username = field("Username")

    @cached_property
    def UserAttributes(self):  # pragma: no cover
        return AttributeType.make_many(self.boto3_raw_data["UserAttributes"])

    ClientMetadata = field("ClientMetadata")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AdminUpdateUserAttributesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminUpdateUserAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeviceType:
    boto3_raw_data: "type_defs.DeviceTypeTypeDef" = dataclasses.field()

    DeviceKey = field("DeviceKey")

    @cached_property
    def DeviceAttributes(self):  # pragma: no cover
        return AttributeType.make_many(self.boto3_raw_data["DeviceAttributes"])

    DeviceCreateDate = field("DeviceCreateDate")
    DeviceLastModifiedDate = field("DeviceLastModifiedDate")
    DeviceLastAuthenticatedDate = field("DeviceLastAuthenticatedDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeviceTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeviceTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserAttributesRequest:
    boto3_raw_data: "type_defs.UpdateUserAttributesRequestTypeDef" = dataclasses.field()

    @cached_property
    def UserAttributes(self):  # pragma: no cover
        return AttributeType.make_many(self.boto3_raw_data["UserAttributes"])

    AccessToken = field("AccessToken")
    ClientMetadata = field("ClientMetadata")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUserAttributesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateSoftwareTokenResponse:
    boto3_raw_data: "type_defs.AssociateSoftwareTokenResponseTypeDef" = (
        dataclasses.field()
    )

    SecretCode = field("SecretCode")
    Session = field("Session")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateSoftwareTokenResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateSoftwareTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfirmDeviceResponse:
    boto3_raw_data: "type_defs.ConfirmDeviceResponseTypeDef" = dataclasses.field()

    UserConfirmationNecessary = field("UserConfirmationNecessary")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfirmDeviceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfirmDeviceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfirmSignUpResponse:
    boto3_raw_data: "type_defs.ConfirmSignUpResponseTypeDef" = dataclasses.field()

    Session = field("Session")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfirmSignUpResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfirmSignUpResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserPoolDomainResponse:
    boto3_raw_data: "type_defs.CreateUserPoolDomainResponseTypeDef" = (
        dataclasses.field()
    )

    ManagedLoginVersion = field("ManagedLoginVersion")
    CloudFrontDomain = field("CloudFrontDomain")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUserPoolDomainResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserPoolDomainResponseTypeDef"]
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
class GetCSVHeaderResponse:
    boto3_raw_data: "type_defs.GetCSVHeaderResponseTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    CSVHeader = field("CSVHeader")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCSVHeaderResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCSVHeaderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSigningCertificateResponse:
    boto3_raw_data: "type_defs.GetSigningCertificateResponseTypeDef" = (
        dataclasses.field()
    )

    Certificate = field("Certificate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSigningCertificateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSigningCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserAuthFactorsResponse:
    boto3_raw_data: "type_defs.GetUserAuthFactorsResponseTypeDef" = dataclasses.field()

    Username = field("Username")
    PreferredMfaSetting = field("PreferredMfaSetting")
    UserMFASettingList = field("UserMFASettingList")
    ConfiguredUserAuthFactors = field("ConfiguredUserAuthFactors")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUserAuthFactorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUserAuthFactorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartWebAuthnRegistrationResponse:
    boto3_raw_data: "type_defs.StartWebAuthnRegistrationResponseTypeDef" = (
        dataclasses.field()
    )

    CredentialCreationOptions = field("CredentialCreationOptions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartWebAuthnRegistrationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartWebAuthnRegistrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserPoolDomainResponse:
    boto3_raw_data: "type_defs.UpdateUserPoolDomainResponseTypeDef" = (
        dataclasses.field()
    )

    ManagedLoginVersion = field("ManagedLoginVersion")
    CloudFrontDomain = field("CloudFrontDomain")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUserPoolDomainResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserPoolDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifySoftwareTokenResponse:
    boto3_raw_data: "type_defs.VerifySoftwareTokenResponseTypeDef" = dataclasses.field()

    Status = field("Status")
    Session = field("Session")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VerifySoftwareTokenResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifySoftwareTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminDisableProviderForUserRequest:
    boto3_raw_data: "type_defs.AdminDisableProviderForUserRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")

    @cached_property
    def User(self):  # pragma: no cover
        return ProviderUserIdentifierType.make_one(self.boto3_raw_data["User"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AdminDisableProviderForUserRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminDisableProviderForUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminLinkProviderForUserRequest:
    boto3_raw_data: "type_defs.AdminLinkProviderForUserRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")

    @cached_property
    def DestinationUser(self):  # pragma: no cover
        return ProviderUserIdentifierType.make_one(
            self.boto3_raw_data["DestinationUser"]
        )

    @cached_property
    def SourceUser(self):  # pragma: no cover
        return ProviderUserIdentifierType.make_one(self.boto3_raw_data["SourceUser"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AdminLinkProviderForUserRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminLinkProviderForUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminGetUserResponse:
    boto3_raw_data: "type_defs.AdminGetUserResponseTypeDef" = dataclasses.field()

    Username = field("Username")

    @cached_property
    def UserAttributes(self):  # pragma: no cover
        return AttributeType.make_many(self.boto3_raw_data["UserAttributes"])

    UserCreateDate = field("UserCreateDate")
    UserLastModifiedDate = field("UserLastModifiedDate")
    Enabled = field("Enabled")
    UserStatus = field("UserStatus")

    @cached_property
    def MFAOptions(self):  # pragma: no cover
        return MFAOptionType.make_many(self.boto3_raw_data["MFAOptions"])

    PreferredMfaSetting = field("PreferredMfaSetting")
    UserMFASettingList = field("UserMFASettingList")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdminGetUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminGetUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminSetUserSettingsRequest:
    boto3_raw_data: "type_defs.AdminSetUserSettingsRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    Username = field("Username")

    @cached_property
    def MFAOptions(self):  # pragma: no cover
        return MFAOptionType.make_many(self.boto3_raw_data["MFAOptions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdminSetUserSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminSetUserSettingsRequestTypeDef"]
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

    Username = field("Username")

    @cached_property
    def UserAttributes(self):  # pragma: no cover
        return AttributeType.make_many(self.boto3_raw_data["UserAttributes"])

    @cached_property
    def MFAOptions(self):  # pragma: no cover
        return MFAOptionType.make_many(self.boto3_raw_data["MFAOptions"])

    PreferredMfaSetting = field("PreferredMfaSetting")
    UserMFASettingList = field("UserMFASettingList")

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
class SetUserSettingsRequest:
    boto3_raw_data: "type_defs.SetUserSettingsRequestTypeDef" = dataclasses.field()

    AccessToken = field("AccessToken")

    @cached_property
    def MFAOptions(self):  # pragma: no cover
        return MFAOptionType.make_many(self.boto3_raw_data["MFAOptions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetUserSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetUserSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserType:
    boto3_raw_data: "type_defs.UserTypeTypeDef" = dataclasses.field()

    Username = field("Username")

    @cached_property
    def Attributes(self):  # pragma: no cover
        return AttributeType.make_many(self.boto3_raw_data["Attributes"])

    UserCreateDate = field("UserCreateDate")
    UserLastModifiedDate = field("UserLastModifiedDate")
    Enabled = field("Enabled")
    UserStatus = field("UserStatus")

    @cached_property
    def MFAOptions(self):  # pragma: no cover
        return MFAOptionType.make_many(self.boto3_raw_data["MFAOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminListGroupsForUserRequestPaginate:
    boto3_raw_data: "type_defs.AdminListGroupsForUserRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Username = field("Username")
    UserPoolId = field("UserPoolId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AdminListGroupsForUserRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminListGroupsForUserRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminListUserAuthEventsRequestPaginate:
    boto3_raw_data: "type_defs.AdminListUserAuthEventsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    Username = field("Username")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AdminListUserAuthEventsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminListUserAuthEventsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListGroupsRequestPaginateTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentityProvidersRequestPaginate:
    boto3_raw_data: "type_defs.ListIdentityProvidersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListIdentityProvidersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentityProvidersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceServersRequestPaginate:
    boto3_raw_data: "type_defs.ListResourceServersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceServersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceServersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserPoolClientsRequestPaginate:
    boto3_raw_data: "type_defs.ListUserPoolClientsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListUserPoolClientsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserPoolClientsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserPoolsRequestPaginate:
    boto3_raw_data: "type_defs.ListUserPoolsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUserPoolsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserPoolsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsersInGroupRequestPaginate:
    boto3_raw_data: "type_defs.ListUsersInGroupRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    GroupName = field("GroupName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListUsersInGroupRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersInGroupRequestPaginateTypeDef"]
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

    UserPoolId = field("UserPoolId")
    AttributesToGet = field("AttributesToGet")
    Filter = field("Filter")

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
class AdminListGroupsForUserResponse:
    boto3_raw_data: "type_defs.AdminListGroupsForUserResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Groups(self):  # pragma: no cover
        return GroupType.make_many(self.boto3_raw_data["Groups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AdminListGroupsForUserResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminListGroupsForUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGroupResponse:
    boto3_raw_data: "type_defs.CreateGroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def Group(self):  # pragma: no cover
        return GroupType.make_one(self.boto3_raw_data["Group"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupResponse:
    boto3_raw_data: "type_defs.GetGroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def Group(self):  # pragma: no cover
        return GroupType.make_one(self.boto3_raw_data["Group"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGroupResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsResponse:
    boto3_raw_data: "type_defs.ListGroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Groups(self):  # pragma: no cover
        return GroupType.make_many(self.boto3_raw_data["Groups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGroupResponse:
    boto3_raw_data: "type_defs.UpdateGroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def Group(self):  # pragma: no cover
        return GroupType.make_one(self.boto3_raw_data["Group"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminSetUserMFAPreferenceRequest:
    boto3_raw_data: "type_defs.AdminSetUserMFAPreferenceRequestTypeDef" = (
        dataclasses.field()
    )

    Username = field("Username")
    UserPoolId = field("UserPoolId")

    @cached_property
    def SMSMfaSettings(self):  # pragma: no cover
        return SMSMfaSettingsType.make_one(self.boto3_raw_data["SMSMfaSettings"])

    @cached_property
    def SoftwareTokenMfaSettings(self):  # pragma: no cover
        return SoftwareTokenMfaSettingsType.make_one(
            self.boto3_raw_data["SoftwareTokenMfaSettings"]
        )

    @cached_property
    def EmailMfaSettings(self):  # pragma: no cover
        return EmailMfaSettingsType.make_one(self.boto3_raw_data["EmailMfaSettings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AdminSetUserMFAPreferenceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminSetUserMFAPreferenceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetUserMFAPreferenceRequest:
    boto3_raw_data: "type_defs.SetUserMFAPreferenceRequestTypeDef" = dataclasses.field()

    AccessToken = field("AccessToken")

    @cached_property
    def SMSMfaSettings(self):  # pragma: no cover
        return SMSMfaSettingsType.make_one(self.boto3_raw_data["SMSMfaSettings"])

    @cached_property
    def SoftwareTokenMfaSettings(self):  # pragma: no cover
        return SoftwareTokenMfaSettingsType.make_one(
            self.boto3_raw_data["SoftwareTokenMfaSettings"]
        )

    @cached_property
    def EmailMfaSettings(self):  # pragma: no cover
        return EmailMfaSettingsType.make_one(self.boto3_raw_data["EmailMfaSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetUserMFAPreferenceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetUserMFAPreferenceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserPoolAddOnsType:
    boto3_raw_data: "type_defs.UserPoolAddOnsTypeTypeDef" = dataclasses.field()

    AdvancedSecurityMode = field("AdvancedSecurityMode")

    @cached_property
    def AdvancedSecurityAdditionalFlows(self):  # pragma: no cover
        return AdvancedSecurityAdditionalFlowsType.make_one(
            self.boto3_raw_data["AdvancedSecurityAdditionalFlows"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserPoolAddOnsTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserPoolAddOnsTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedLoginBrandingType:
    boto3_raw_data: "type_defs.ManagedLoginBrandingTypeTypeDef" = dataclasses.field()

    ManagedLoginBrandingId = field("ManagedLoginBrandingId")
    UserPoolId = field("UserPoolId")
    UseCognitoProvidedValues = field("UseCognitoProvidedValues")
    Settings = field("Settings")

    @cached_property
    def Assets(self):  # pragma: no cover
        return AssetTypeOutput.make_many(self.boto3_raw_data["Assets"])

    CreationDate = field("CreationDate")
    LastModifiedDate = field("LastModifiedDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedLoginBrandingTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedLoginBrandingTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetType:
    boto3_raw_data: "type_defs.AssetTypeTypeDef" = dataclasses.field()

    Category = field("Category")
    ColorMode = field("ColorMode")
    Extension = field("Extension")
    Bytes = field("Bytes")
    ResourceId = field("ResourceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssetTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetUICustomizationRequest:
    boto3_raw_data: "type_defs.SetUICustomizationRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    ClientId = field("ClientId")
    CSS = field("CSS")
    ImageFile = field("ImageFile")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetUICustomizationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetUICustomizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthEventType:
    boto3_raw_data: "type_defs.AuthEventTypeTypeDef" = dataclasses.field()

    EventId = field("EventId")
    EventType = field("EventType")
    CreationDate = field("CreationDate")
    EventResponse = field("EventResponse")

    @cached_property
    def EventRisk(self):  # pragma: no cover
        return EventRiskType.make_one(self.boto3_raw_data["EventRisk"])

    @cached_property
    def ChallengeResponses(self):  # pragma: no cover
        return ChallengeResponseType.make_many(
            self.boto3_raw_data["ChallengeResponses"]
        )

    @cached_property
    def EventContextData(self):  # pragma: no cover
        return EventContextDataType.make_one(self.boto3_raw_data["EventContextData"])

    @cached_property
    def EventFeedback(self):  # pragma: no cover
        return EventFeedbackType.make_one(self.boto3_raw_data["EventFeedback"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuthEventTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AuthEventTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthenticationResultType:
    boto3_raw_data: "type_defs.AuthenticationResultTypeTypeDef" = dataclasses.field()

    AccessToken = field("AccessToken")
    ExpiresIn = field("ExpiresIn")
    TokenType = field("TokenType")
    RefreshToken = field("RefreshToken")
    IdToken = field("IdToken")

    @cached_property
    def NewDeviceMetadata(self):  # pragma: no cover
        return NewDeviceMetadataType.make_one(self.boto3_raw_data["NewDeviceMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthenticationResultTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticationResultTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ForgotPasswordResponse:
    boto3_raw_data: "type_defs.ForgotPasswordResponseTypeDef" = dataclasses.field()

    @cached_property
    def CodeDeliveryDetails(self):  # pragma: no cover
        return CodeDeliveryDetailsType.make_one(
            self.boto3_raw_data["CodeDeliveryDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ForgotPasswordResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ForgotPasswordResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserAttributeVerificationCodeResponse:
    boto3_raw_data: "type_defs.GetUserAttributeVerificationCodeResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CodeDeliveryDetails(self):  # pragma: no cover
        return CodeDeliveryDetailsType.make_one(
            self.boto3_raw_data["CodeDeliveryDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetUserAttributeVerificationCodeResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUserAttributeVerificationCodeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResendConfirmationCodeResponse:
    boto3_raw_data: "type_defs.ResendConfirmationCodeResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CodeDeliveryDetails(self):  # pragma: no cover
        return CodeDeliveryDetailsType.make_one(
            self.boto3_raw_data["CodeDeliveryDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ResendConfirmationCodeResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResendConfirmationCodeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignUpResponse:
    boto3_raw_data: "type_defs.SignUpResponseTypeDef" = dataclasses.field()

    UserConfirmed = field("UserConfirmed")

    @cached_property
    def CodeDeliveryDetails(self):  # pragma: no cover
        return CodeDeliveryDetailsType.make_one(
            self.boto3_raw_data["CodeDeliveryDetails"]
        )

    UserSub = field("UserSub")
    Session = field("Session")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SignUpResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SignUpResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserAttributesResponse:
    boto3_raw_data: "type_defs.UpdateUserAttributesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CodeDeliveryDetailsList(self):  # pragma: no cover
        return CodeDeliveryDetailsType.make_many(
            self.boto3_raw_data["CodeDeliveryDetailsList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUserAttributesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompromisedCredentialsRiskConfigurationTypeOutput:
    boto3_raw_data: (
        "type_defs.CompromisedCredentialsRiskConfigurationTypeOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Actions(self):  # pragma: no cover
        return CompromisedCredentialsActionsType.make_one(
            self.boto3_raw_data["Actions"]
        )

    EventFilter = field("EventFilter")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CompromisedCredentialsRiskConfigurationTypeOutputTypeDef"
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
                "type_defs.CompromisedCredentialsRiskConfigurationTypeOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompromisedCredentialsRiskConfigurationType:
    boto3_raw_data: "type_defs.CompromisedCredentialsRiskConfigurationTypeTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Actions(self):  # pragma: no cover
        return CompromisedCredentialsActionsType.make_one(
            self.boto3_raw_data["Actions"]
        )

    EventFilter = field("EventFilter")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CompromisedCredentialsRiskConfigurationTypeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompromisedCredentialsRiskConfigurationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfirmDeviceRequest:
    boto3_raw_data: "type_defs.ConfirmDeviceRequestTypeDef" = dataclasses.field()

    AccessToken = field("AccessToken")
    DeviceKey = field("DeviceKey")

    @cached_property
    def DeviceSecretVerifierConfig(self):  # pragma: no cover
        return DeviceSecretVerifierConfigType.make_one(
            self.boto3_raw_data["DeviceSecretVerifierConfig"]
        )

    DeviceName = field("DeviceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfirmDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfirmDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfirmForgotPasswordRequest:
    boto3_raw_data: "type_defs.ConfirmForgotPasswordRequestTypeDef" = (
        dataclasses.field()
    )

    ClientId = field("ClientId")
    Username = field("Username")
    ConfirmationCode = field("ConfirmationCode")
    Password = field("Password")
    SecretHash = field("SecretHash")

    @cached_property
    def AnalyticsMetadata(self):  # pragma: no cover
        return AnalyticsMetadataType.make_one(self.boto3_raw_data["AnalyticsMetadata"])

    @cached_property
    def UserContextData(self):  # pragma: no cover
        return UserContextDataType.make_one(self.boto3_raw_data["UserContextData"])

    ClientMetadata = field("ClientMetadata")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfirmForgotPasswordRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfirmForgotPasswordRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfirmSignUpRequest:
    boto3_raw_data: "type_defs.ConfirmSignUpRequestTypeDef" = dataclasses.field()

    ClientId = field("ClientId")
    Username = field("Username")
    ConfirmationCode = field("ConfirmationCode")
    SecretHash = field("SecretHash")
    ForceAliasCreation = field("ForceAliasCreation")

    @cached_property
    def AnalyticsMetadata(self):  # pragma: no cover
        return AnalyticsMetadataType.make_one(self.boto3_raw_data["AnalyticsMetadata"])

    @cached_property
    def UserContextData(self):  # pragma: no cover
        return UserContextDataType.make_one(self.boto3_raw_data["UserContextData"])

    ClientMetadata = field("ClientMetadata")
    Session = field("Session")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfirmSignUpRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfirmSignUpRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ForgotPasswordRequest:
    boto3_raw_data: "type_defs.ForgotPasswordRequestTypeDef" = dataclasses.field()

    ClientId = field("ClientId")
    Username = field("Username")
    SecretHash = field("SecretHash")

    @cached_property
    def UserContextData(self):  # pragma: no cover
        return UserContextDataType.make_one(self.boto3_raw_data["UserContextData"])

    @cached_property
    def AnalyticsMetadata(self):  # pragma: no cover
        return AnalyticsMetadataType.make_one(self.boto3_raw_data["AnalyticsMetadata"])

    ClientMetadata = field("ClientMetadata")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ForgotPasswordRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ForgotPasswordRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InitiateAuthRequest:
    boto3_raw_data: "type_defs.InitiateAuthRequestTypeDef" = dataclasses.field()

    AuthFlow = field("AuthFlow")
    ClientId = field("ClientId")
    AuthParameters = field("AuthParameters")
    ClientMetadata = field("ClientMetadata")

    @cached_property
    def AnalyticsMetadata(self):  # pragma: no cover
        return AnalyticsMetadataType.make_one(self.boto3_raw_data["AnalyticsMetadata"])

    @cached_property
    def UserContextData(self):  # pragma: no cover
        return UserContextDataType.make_one(self.boto3_raw_data["UserContextData"])

    Session = field("Session")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InitiateAuthRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InitiateAuthRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResendConfirmationCodeRequest:
    boto3_raw_data: "type_defs.ResendConfirmationCodeRequestTypeDef" = (
        dataclasses.field()
    )

    ClientId = field("ClientId")
    Username = field("Username")
    SecretHash = field("SecretHash")

    @cached_property
    def UserContextData(self):  # pragma: no cover
        return UserContextDataType.make_one(self.boto3_raw_data["UserContextData"])

    @cached_property
    def AnalyticsMetadata(self):  # pragma: no cover
        return AnalyticsMetadataType.make_one(self.boto3_raw_data["AnalyticsMetadata"])

    ClientMetadata = field("ClientMetadata")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ResendConfirmationCodeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResendConfirmationCodeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RespondToAuthChallengeRequest:
    boto3_raw_data: "type_defs.RespondToAuthChallengeRequestTypeDef" = (
        dataclasses.field()
    )

    ClientId = field("ClientId")
    ChallengeName = field("ChallengeName")
    Session = field("Session")
    ChallengeResponses = field("ChallengeResponses")

    @cached_property
    def AnalyticsMetadata(self):  # pragma: no cover
        return AnalyticsMetadataType.make_one(self.boto3_raw_data["AnalyticsMetadata"])

    @cached_property
    def UserContextData(self):  # pragma: no cover
        return UserContextDataType.make_one(self.boto3_raw_data["UserContextData"])

    ClientMetadata = field("ClientMetadata")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RespondToAuthChallengeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RespondToAuthChallengeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignUpRequest:
    boto3_raw_data: "type_defs.SignUpRequestTypeDef" = dataclasses.field()

    ClientId = field("ClientId")
    Username = field("Username")
    SecretHash = field("SecretHash")
    Password = field("Password")

    @cached_property
    def UserAttributes(self):  # pragma: no cover
        return AttributeType.make_many(self.boto3_raw_data["UserAttributes"])

    @cached_property
    def ValidationData(self):  # pragma: no cover
        return AttributeType.make_many(self.boto3_raw_data["ValidationData"])

    @cached_property
    def AnalyticsMetadata(self):  # pragma: no cover
        return AnalyticsMetadataType.make_one(self.boto3_raw_data["AnalyticsMetadata"])

    @cached_property
    def UserContextData(self):  # pragma: no cover
        return UserContextDataType.make_one(self.boto3_raw_data["UserContextData"])

    ClientMetadata = field("ClientMetadata")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SignUpRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SignUpRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContextDataType:
    boto3_raw_data: "type_defs.ContextDataTypeTypeDef" = dataclasses.field()

    IpAddress = field("IpAddress")
    ServerName = field("ServerName")
    ServerPath = field("ServerPath")

    @cached_property
    def HttpHeaders(self):  # pragma: no cover
        return HttpHeader.make_many(self.boto3_raw_data["HttpHeaders"])

    EncodedData = field("EncodedData")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContextDataTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContextDataTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIdentityProviderResponse:
    boto3_raw_data: "type_defs.CreateIdentityProviderResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IdentityProvider(self):  # pragma: no cover
        return IdentityProviderType.make_one(self.boto3_raw_data["IdentityProvider"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateIdentityProviderResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIdentityProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIdentityProviderResponse:
    boto3_raw_data: "type_defs.DescribeIdentityProviderResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IdentityProvider(self):  # pragma: no cover
        return IdentityProviderType.make_one(self.boto3_raw_data["IdentityProvider"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeIdentityProviderResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIdentityProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentityProviderByIdentifierResponse:
    boto3_raw_data: "type_defs.GetIdentityProviderByIdentifierResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IdentityProvider(self):  # pragma: no cover
        return IdentityProviderType.make_one(self.boto3_raw_data["IdentityProvider"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetIdentityProviderByIdentifierResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentityProviderByIdentifierResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIdentityProviderResponse:
    boto3_raw_data: "type_defs.UpdateIdentityProviderResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IdentityProvider(self):  # pragma: no cover
        return IdentityProviderType.make_one(self.boto3_raw_data["IdentityProvider"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateIdentityProviderResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIdentityProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourceServerRequest:
    boto3_raw_data: "type_defs.CreateResourceServerRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    Identifier = field("Identifier")
    Name = field("Name")

    @cached_property
    def Scopes(self):  # pragma: no cover
        return ResourceServerScopeType.make_many(self.boto3_raw_data["Scopes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateResourceServerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourceServerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceServerType:
    boto3_raw_data: "type_defs.ResourceServerTypeTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    Identifier = field("Identifier")
    Name = field("Name")

    @cached_property
    def Scopes(self):  # pragma: no cover
        return ResourceServerScopeType.make_many(self.boto3_raw_data["Scopes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceServerTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceServerTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResourceServerRequest:
    boto3_raw_data: "type_defs.UpdateResourceServerRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    Identifier = field("Identifier")
    Name = field("Name")

    @cached_property
    def Scopes(self):  # pragma: no cover
        return ResourceServerScopeType.make_many(self.boto3_raw_data["Scopes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateResourceServerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResourceServerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTermsResponse:
    boto3_raw_data: "type_defs.CreateTermsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Terms(self):  # pragma: no cover
        return TermsType.make_one(self.boto3_raw_data["Terms"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTermsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTermsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTermsResponse:
    boto3_raw_data: "type_defs.DescribeTermsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Terms(self):  # pragma: no cover
        return TermsType.make_one(self.boto3_raw_data["Terms"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTermsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTermsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTermsResponse:
    boto3_raw_data: "type_defs.UpdateTermsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Terms(self):  # pragma: no cover
        return TermsType.make_one(self.boto3_raw_data["Terms"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTermsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTermsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserImportJobResponse:
    boto3_raw_data: "type_defs.CreateUserImportJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def UserImportJob(self):  # pragma: no cover
        return UserImportJobType.make_one(self.boto3_raw_data["UserImportJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUserImportJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserImportJobResponse:
    boto3_raw_data: "type_defs.DescribeUserImportJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UserImportJob(self):  # pragma: no cover
        return UserImportJobType.make_one(self.boto3_raw_data["UserImportJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeUserImportJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserImportJobsResponse:
    boto3_raw_data: "type_defs.ListUserImportJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def UserImportJobs(self):  # pragma: no cover
        return UserImportJobType.make_many(self.boto3_raw_data["UserImportJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    PaginationToken = field("PaginationToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUserImportJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserImportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartUserImportJobResponse:
    boto3_raw_data: "type_defs.StartUserImportJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def UserImportJob(self):  # pragma: no cover
        return UserImportJobType.make_one(self.boto3_raw_data["UserImportJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartUserImportJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartUserImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopUserImportJobResponse:
    boto3_raw_data: "type_defs.StopUserImportJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def UserImportJob(self):  # pragma: no cover
        return UserImportJobType.make_one(self.boto3_raw_data["UserImportJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopUserImportJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopUserImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserPoolClientRequest:
    boto3_raw_data: "type_defs.CreateUserPoolClientRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    ClientName = field("ClientName")
    GenerateSecret = field("GenerateSecret")
    RefreshTokenValidity = field("RefreshTokenValidity")
    AccessTokenValidity = field("AccessTokenValidity")
    IdTokenValidity = field("IdTokenValidity")

    @cached_property
    def TokenValidityUnits(self):  # pragma: no cover
        return TokenValidityUnitsType.make_one(
            self.boto3_raw_data["TokenValidityUnits"]
        )

    ReadAttributes = field("ReadAttributes")
    WriteAttributes = field("WriteAttributes")
    ExplicitAuthFlows = field("ExplicitAuthFlows")
    SupportedIdentityProviders = field("SupportedIdentityProviders")
    CallbackURLs = field("CallbackURLs")
    LogoutURLs = field("LogoutURLs")
    DefaultRedirectURI = field("DefaultRedirectURI")
    AllowedOAuthFlows = field("AllowedOAuthFlows")
    AllowedOAuthScopes = field("AllowedOAuthScopes")
    AllowedOAuthFlowsUserPoolClient = field("AllowedOAuthFlowsUserPoolClient")

    @cached_property
    def AnalyticsConfiguration(self):  # pragma: no cover
        return AnalyticsConfigurationType.make_one(
            self.boto3_raw_data["AnalyticsConfiguration"]
        )

    PreventUserExistenceErrors = field("PreventUserExistenceErrors")
    EnableTokenRevocation = field("EnableTokenRevocation")
    EnablePropagateAdditionalUserContextData = field(
        "EnablePropagateAdditionalUserContextData"
    )
    AuthSessionValidity = field("AuthSessionValidity")

    @cached_property
    def RefreshTokenRotation(self):  # pragma: no cover
        return RefreshTokenRotationType.make_one(
            self.boto3_raw_data["RefreshTokenRotation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUserPoolClientRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserPoolClientRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserPoolClientRequest:
    boto3_raw_data: "type_defs.UpdateUserPoolClientRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    ClientId = field("ClientId")
    ClientName = field("ClientName")
    RefreshTokenValidity = field("RefreshTokenValidity")
    AccessTokenValidity = field("AccessTokenValidity")
    IdTokenValidity = field("IdTokenValidity")

    @cached_property
    def TokenValidityUnits(self):  # pragma: no cover
        return TokenValidityUnitsType.make_one(
            self.boto3_raw_data["TokenValidityUnits"]
        )

    ReadAttributes = field("ReadAttributes")
    WriteAttributes = field("WriteAttributes")
    ExplicitAuthFlows = field("ExplicitAuthFlows")
    SupportedIdentityProviders = field("SupportedIdentityProviders")
    CallbackURLs = field("CallbackURLs")
    LogoutURLs = field("LogoutURLs")
    DefaultRedirectURI = field("DefaultRedirectURI")
    AllowedOAuthFlows = field("AllowedOAuthFlows")
    AllowedOAuthScopes = field("AllowedOAuthScopes")
    AllowedOAuthFlowsUserPoolClient = field("AllowedOAuthFlowsUserPoolClient")

    @cached_property
    def AnalyticsConfiguration(self):  # pragma: no cover
        return AnalyticsConfigurationType.make_one(
            self.boto3_raw_data["AnalyticsConfiguration"]
        )

    PreventUserExistenceErrors = field("PreventUserExistenceErrors")
    EnableTokenRevocation = field("EnableTokenRevocation")
    EnablePropagateAdditionalUserContextData = field(
        "EnablePropagateAdditionalUserContextData"
    )
    AuthSessionValidity = field("AuthSessionValidity")

    @cached_property
    def RefreshTokenRotation(self):  # pragma: no cover
        return RefreshTokenRotationType.make_one(
            self.boto3_raw_data["RefreshTokenRotation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUserPoolClientRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserPoolClientRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserPoolClientType:
    boto3_raw_data: "type_defs.UserPoolClientTypeTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    ClientName = field("ClientName")
    ClientId = field("ClientId")
    ClientSecret = field("ClientSecret")
    LastModifiedDate = field("LastModifiedDate")
    CreationDate = field("CreationDate")
    RefreshTokenValidity = field("RefreshTokenValidity")
    AccessTokenValidity = field("AccessTokenValidity")
    IdTokenValidity = field("IdTokenValidity")

    @cached_property
    def TokenValidityUnits(self):  # pragma: no cover
        return TokenValidityUnitsType.make_one(
            self.boto3_raw_data["TokenValidityUnits"]
        )

    ReadAttributes = field("ReadAttributes")
    WriteAttributes = field("WriteAttributes")
    ExplicitAuthFlows = field("ExplicitAuthFlows")
    SupportedIdentityProviders = field("SupportedIdentityProviders")
    CallbackURLs = field("CallbackURLs")
    LogoutURLs = field("LogoutURLs")
    DefaultRedirectURI = field("DefaultRedirectURI")
    AllowedOAuthFlows = field("AllowedOAuthFlows")
    AllowedOAuthScopes = field("AllowedOAuthScopes")
    AllowedOAuthFlowsUserPoolClient = field("AllowedOAuthFlowsUserPoolClient")

    @cached_property
    def AnalyticsConfiguration(self):  # pragma: no cover
        return AnalyticsConfigurationType.make_one(
            self.boto3_raw_data["AnalyticsConfiguration"]
        )

    PreventUserExistenceErrors = field("PreventUserExistenceErrors")
    EnableTokenRevocation = field("EnableTokenRevocation")
    EnablePropagateAdditionalUserContextData = field(
        "EnablePropagateAdditionalUserContextData"
    )
    AuthSessionValidity = field("AuthSessionValidity")

    @cached_property
    def RefreshTokenRotation(self):  # pragma: no cover
        return RefreshTokenRotationType.make_one(
            self.boto3_raw_data["RefreshTokenRotation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserPoolClientTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserPoolClientTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserPoolDomainRequest:
    boto3_raw_data: "type_defs.CreateUserPoolDomainRequestTypeDef" = dataclasses.field()

    Domain = field("Domain")
    UserPoolId = field("UserPoolId")
    ManagedLoginVersion = field("ManagedLoginVersion")

    @cached_property
    def CustomDomainConfig(self):  # pragma: no cover
        return CustomDomainConfigType.make_one(
            self.boto3_raw_data["CustomDomainConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUserPoolDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserPoolDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainDescriptionType:
    boto3_raw_data: "type_defs.DomainDescriptionTypeTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    AWSAccountId = field("AWSAccountId")
    Domain = field("Domain")
    S3Bucket = field("S3Bucket")
    CloudFrontDistribution = field("CloudFrontDistribution")
    Version = field("Version")
    Status = field("Status")

    @cached_property
    def CustomDomainConfig(self):  # pragma: no cover
        return CustomDomainConfigType.make_one(
            self.boto3_raw_data["CustomDomainConfig"]
        )

    ManagedLoginVersion = field("ManagedLoginVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainDescriptionTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainDescriptionTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserPoolDomainRequest:
    boto3_raw_data: "type_defs.UpdateUserPoolDomainRequestTypeDef" = dataclasses.field()

    Domain = field("Domain")
    UserPoolId = field("UserPoolId")
    ManagedLoginVersion = field("ManagedLoginVersion")

    @cached_property
    def CustomDomainConfig(self):  # pragma: no cover
        return CustomDomainConfigType.make_one(
            self.boto3_raw_data["CustomDomainConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUserPoolDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserPoolDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SmsMfaConfigType:
    boto3_raw_data: "type_defs.SmsMfaConfigTypeTypeDef" = dataclasses.field()

    SmsAuthenticationMessage = field("SmsAuthenticationMessage")

    @cached_property
    def SmsConfiguration(self):  # pragma: no cover
        return SmsConfigurationType.make_one(self.boto3_raw_data["SmsConfiguration"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SmsMfaConfigTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SmsMfaConfigTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUICustomizationResponse:
    boto3_raw_data: "type_defs.GetUICustomizationResponseTypeDef" = dataclasses.field()

    @cached_property
    def UICustomization(self):  # pragma: no cover
        return UICustomizationType.make_one(self.boto3_raw_data["UICustomization"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUICustomizationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUICustomizationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetUICustomizationResponse:
    boto3_raw_data: "type_defs.SetUICustomizationResponseTypeDef" = dataclasses.field()

    @cached_property
    def UICustomization(self):  # pragma: no cover
        return UICustomizationType.make_one(self.boto3_raw_data["UICustomization"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetUICustomizationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetUICustomizationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaConfigType:
    boto3_raw_data: "type_defs.LambdaConfigTypeTypeDef" = dataclasses.field()

    PreSignUp = field("PreSignUp")
    CustomMessage = field("CustomMessage")
    PostConfirmation = field("PostConfirmation")
    PreAuthentication = field("PreAuthentication")
    PostAuthentication = field("PostAuthentication")
    DefineAuthChallenge = field("DefineAuthChallenge")
    CreateAuthChallenge = field("CreateAuthChallenge")
    VerifyAuthChallengeResponse = field("VerifyAuthChallengeResponse")
    PreTokenGeneration = field("PreTokenGeneration")
    UserMigration = field("UserMigration")

    @cached_property
    def PreTokenGenerationConfig(self):  # pragma: no cover
        return PreTokenGenerationVersionConfigType.make_one(
            self.boto3_raw_data["PreTokenGenerationConfig"]
        )

    @cached_property
    def CustomSMSSender(self):  # pragma: no cover
        return CustomSMSLambdaVersionConfigType.make_one(
            self.boto3_raw_data["CustomSMSSender"]
        )

    @cached_property
    def CustomEmailSender(self):  # pragma: no cover
        return CustomEmailLambdaVersionConfigType.make_one(
            self.boto3_raw_data["CustomEmailSender"]
        )

    KMSKeyID = field("KMSKeyID")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LambdaConfigTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaConfigTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentityProvidersResponse:
    boto3_raw_data: "type_defs.ListIdentityProvidersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Providers(self):  # pragma: no cover
        return ProviderDescription.make_many(self.boto3_raw_data["Providers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListIdentityProvidersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentityProvidersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTermsResponse:
    boto3_raw_data: "type_defs.ListTermsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Terms(self):  # pragma: no cover
        return TermsDescriptionType.make_many(self.boto3_raw_data["Terms"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTermsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTermsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserPoolClientsResponse:
    boto3_raw_data: "type_defs.ListUserPoolClientsResponseTypeDef" = dataclasses.field()

    @cached_property
    def UserPoolClients(self):  # pragma: no cover
        return UserPoolClientDescription.make_many(
            self.boto3_raw_data["UserPoolClients"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUserPoolClientsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserPoolClientsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWebAuthnCredentialsResponse:
    boto3_raw_data: "type_defs.ListWebAuthnCredentialsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Credentials(self):  # pragma: no cover
        return WebAuthnCredentialDescription.make_many(
            self.boto3_raw_data["Credentials"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWebAuthnCredentialsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWebAuthnCredentialsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogConfigurationType:
    boto3_raw_data: "type_defs.LogConfigurationTypeTypeDef" = dataclasses.field()

    LogLevel = field("LogLevel")
    EventSource = field("EventSource")

    @cached_property
    def CloudWatchLogsConfiguration(self):  # pragma: no cover
        return CloudWatchLogsConfigurationType.make_one(
            self.boto3_raw_data["CloudWatchLogsConfiguration"]
        )

    @cached_property
    def S3Configuration(self):  # pragma: no cover
        return S3ConfigurationType.make_one(self.boto3_raw_data["S3Configuration"])

    @cached_property
    def FirehoseConfiguration(self):  # pragma: no cover
        return FirehoseConfigurationType.make_one(
            self.boto3_raw_data["FirehoseConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LogConfigurationTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogConfigurationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotifyConfigurationType:
    boto3_raw_data: "type_defs.NotifyConfigurationTypeTypeDef" = dataclasses.field()

    SourceArn = field("SourceArn")
    From = field("From")
    ReplyTo = field("ReplyTo")

    @cached_property
    def BlockEmail(self):  # pragma: no cover
        return NotifyEmailType.make_one(self.boto3_raw_data["BlockEmail"])

    @cached_property
    def NoActionEmail(self):  # pragma: no cover
        return NotifyEmailType.make_one(self.boto3_raw_data["NoActionEmail"])

    @cached_property
    def MfaEmail(self):  # pragma: no cover
        return NotifyEmailType.make_one(self.boto3_raw_data["MfaEmail"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotifyConfigurationTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotifyConfigurationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaAttributeType:
    boto3_raw_data: "type_defs.SchemaAttributeTypeTypeDef" = dataclasses.field()

    Name = field("Name")
    AttributeDataType = field("AttributeDataType")
    DeveloperOnlyAttribute = field("DeveloperOnlyAttribute")
    Mutable = field("Mutable")
    Required = field("Required")

    @cached_property
    def NumberAttributeConstraints(self):  # pragma: no cover
        return NumberAttributeConstraintsType.make_one(
            self.boto3_raw_data["NumberAttributeConstraints"]
        )

    @cached_property
    def StringAttributeConstraints(self):  # pragma: no cover
        return StringAttributeConstraintsType.make_one(
            self.boto3_raw_data["StringAttributeConstraints"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SchemaAttributeTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchemaAttributeTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserPoolPolicyTypeOutput:
    boto3_raw_data: "type_defs.UserPoolPolicyTypeOutputTypeDef" = dataclasses.field()

    @cached_property
    def PasswordPolicy(self):  # pragma: no cover
        return PasswordPolicyType.make_one(self.boto3_raw_data["PasswordPolicy"])

    @cached_property
    def SignInPolicy(self):  # pragma: no cover
        return SignInPolicyTypeOutput.make_one(self.boto3_raw_data["SignInPolicy"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserPoolPolicyTypeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserPoolPolicyTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserPoolPolicyType:
    boto3_raw_data: "type_defs.UserPoolPolicyTypeTypeDef" = dataclasses.field()

    @cached_property
    def PasswordPolicy(self):  # pragma: no cover
        return PasswordPolicyType.make_one(self.boto3_raw_data["PasswordPolicy"])

    @cached_property
    def SignInPolicy(self):  # pragma: no cover
        return SignInPolicyType.make_one(self.boto3_raw_data["SignInPolicy"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserPoolPolicyTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserPoolPolicyTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminGetDeviceResponse:
    boto3_raw_data: "type_defs.AdminGetDeviceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Device(self):  # pragma: no cover
        return DeviceType.make_one(self.boto3_raw_data["Device"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdminGetDeviceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminGetDeviceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminListDevicesResponse:
    boto3_raw_data: "type_defs.AdminListDevicesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Devices(self):  # pragma: no cover
        return DeviceType.make_many(self.boto3_raw_data["Devices"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    PaginationToken = field("PaginationToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdminListDevicesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminListDevicesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeviceResponse:
    boto3_raw_data: "type_defs.GetDeviceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Device(self):  # pragma: no cover
        return DeviceType.make_one(self.boto3_raw_data["Device"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDeviceResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeviceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDevicesResponse:
    boto3_raw_data: "type_defs.ListDevicesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Devices(self):  # pragma: no cover
        return DeviceType.make_many(self.boto3_raw_data["Devices"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    PaginationToken = field("PaginationToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDevicesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDevicesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminCreateUserResponse:
    boto3_raw_data: "type_defs.AdminCreateUserResponseTypeDef" = dataclasses.field()

    @cached_property
    def User(self):  # pragma: no cover
        return UserType.make_one(self.boto3_raw_data["User"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdminCreateUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminCreateUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsersInGroupResponse:
    boto3_raw_data: "type_defs.ListUsersInGroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def Users(self):  # pragma: no cover
        return UserType.make_many(self.boto3_raw_data["Users"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUsersInGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersInGroupResponseTypeDef"]
        ],
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
        return UserType.make_many(self.boto3_raw_data["Users"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    PaginationToken = field("PaginationToken")

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
class CreateManagedLoginBrandingResponse:
    boto3_raw_data: "type_defs.CreateManagedLoginBrandingResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ManagedLoginBranding(self):  # pragma: no cover
        return ManagedLoginBrandingType.make_one(
            self.boto3_raw_data["ManagedLoginBranding"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateManagedLoginBrandingResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateManagedLoginBrandingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeManagedLoginBrandingByClientResponse:
    boto3_raw_data: "type_defs.DescribeManagedLoginBrandingByClientResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ManagedLoginBranding(self):  # pragma: no cover
        return ManagedLoginBrandingType.make_one(
            self.boto3_raw_data["ManagedLoginBranding"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeManagedLoginBrandingByClientResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeManagedLoginBrandingByClientResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeManagedLoginBrandingResponse:
    boto3_raw_data: "type_defs.DescribeManagedLoginBrandingResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ManagedLoginBranding(self):  # pragma: no cover
        return ManagedLoginBrandingType.make_one(
            self.boto3_raw_data["ManagedLoginBranding"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeManagedLoginBrandingResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeManagedLoginBrandingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateManagedLoginBrandingResponse:
    boto3_raw_data: "type_defs.UpdateManagedLoginBrandingResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ManagedLoginBranding(self):  # pragma: no cover
        return ManagedLoginBrandingType.make_one(
            self.boto3_raw_data["ManagedLoginBranding"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateManagedLoginBrandingResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateManagedLoginBrandingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminListUserAuthEventsResponse:
    boto3_raw_data: "type_defs.AdminListUserAuthEventsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AuthEvents(self):  # pragma: no cover
        return AuthEventType.make_many(self.boto3_raw_data["AuthEvents"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AdminListUserAuthEventsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminListUserAuthEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminInitiateAuthResponse:
    boto3_raw_data: "type_defs.AdminInitiateAuthResponseTypeDef" = dataclasses.field()

    ChallengeName = field("ChallengeName")
    Session = field("Session")
    ChallengeParameters = field("ChallengeParameters")

    @cached_property
    def AuthenticationResult(self):  # pragma: no cover
        return AuthenticationResultType.make_one(
            self.boto3_raw_data["AuthenticationResult"]
        )

    AvailableChallenges = field("AvailableChallenges")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdminInitiateAuthResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminInitiateAuthResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminRespondToAuthChallengeResponse:
    boto3_raw_data: "type_defs.AdminRespondToAuthChallengeResponseTypeDef" = (
        dataclasses.field()
    )

    ChallengeName = field("ChallengeName")
    Session = field("Session")
    ChallengeParameters = field("ChallengeParameters")

    @cached_property
    def AuthenticationResult(self):  # pragma: no cover
        return AuthenticationResultType.make_one(
            self.boto3_raw_data["AuthenticationResult"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AdminRespondToAuthChallengeResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminRespondToAuthChallengeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTokensFromRefreshTokenResponse:
    boto3_raw_data: "type_defs.GetTokensFromRefreshTokenResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AuthenticationResult(self):  # pragma: no cover
        return AuthenticationResultType.make_one(
            self.boto3_raw_data["AuthenticationResult"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTokensFromRefreshTokenResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTokensFromRefreshTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InitiateAuthResponse:
    boto3_raw_data: "type_defs.InitiateAuthResponseTypeDef" = dataclasses.field()

    ChallengeName = field("ChallengeName")
    Session = field("Session")
    ChallengeParameters = field("ChallengeParameters")

    @cached_property
    def AuthenticationResult(self):  # pragma: no cover
        return AuthenticationResultType.make_one(
            self.boto3_raw_data["AuthenticationResult"]
        )

    AvailableChallenges = field("AvailableChallenges")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InitiateAuthResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InitiateAuthResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RespondToAuthChallengeResponse:
    boto3_raw_data: "type_defs.RespondToAuthChallengeResponseTypeDef" = (
        dataclasses.field()
    )

    ChallengeName = field("ChallengeName")
    Session = field("Session")
    ChallengeParameters = field("ChallengeParameters")

    @cached_property
    def AuthenticationResult(self):  # pragma: no cover
        return AuthenticationResultType.make_one(
            self.boto3_raw_data["AuthenticationResult"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RespondToAuthChallengeResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RespondToAuthChallengeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminInitiateAuthRequest:
    boto3_raw_data: "type_defs.AdminInitiateAuthRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    ClientId = field("ClientId")
    AuthFlow = field("AuthFlow")
    AuthParameters = field("AuthParameters")
    ClientMetadata = field("ClientMetadata")

    @cached_property
    def AnalyticsMetadata(self):  # pragma: no cover
        return AnalyticsMetadataType.make_one(self.boto3_raw_data["AnalyticsMetadata"])

    @cached_property
    def ContextData(self):  # pragma: no cover
        return ContextDataType.make_one(self.boto3_raw_data["ContextData"])

    Session = field("Session")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdminInitiateAuthRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminInitiateAuthRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminRespondToAuthChallengeRequest:
    boto3_raw_data: "type_defs.AdminRespondToAuthChallengeRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    ClientId = field("ClientId")
    ChallengeName = field("ChallengeName")
    ChallengeResponses = field("ChallengeResponses")
    Session = field("Session")

    @cached_property
    def AnalyticsMetadata(self):  # pragma: no cover
        return AnalyticsMetadataType.make_one(self.boto3_raw_data["AnalyticsMetadata"])

    @cached_property
    def ContextData(self):  # pragma: no cover
        return ContextDataType.make_one(self.boto3_raw_data["ContextData"])

    ClientMetadata = field("ClientMetadata")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AdminRespondToAuthChallengeRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminRespondToAuthChallengeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourceServerResponse:
    boto3_raw_data: "type_defs.CreateResourceServerResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourceServer(self):  # pragma: no cover
        return ResourceServerType.make_one(self.boto3_raw_data["ResourceServer"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateResourceServerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourceServerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourceServerResponse:
    boto3_raw_data: "type_defs.DescribeResourceServerResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourceServer(self):  # pragma: no cover
        return ResourceServerType.make_one(self.boto3_raw_data["ResourceServer"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeResourceServerResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourceServerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceServersResponse:
    boto3_raw_data: "type_defs.ListResourceServersResponseTypeDef" = dataclasses.field()

    @cached_property
    def ResourceServers(self):  # pragma: no cover
        return ResourceServerType.make_many(self.boto3_raw_data["ResourceServers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourceServersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceServersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResourceServerResponse:
    boto3_raw_data: "type_defs.UpdateResourceServerResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourceServer(self):  # pragma: no cover
        return ResourceServerType.make_one(self.boto3_raw_data["ResourceServer"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateResourceServerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResourceServerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserPoolClientResponse:
    boto3_raw_data: "type_defs.CreateUserPoolClientResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UserPoolClient(self):  # pragma: no cover
        return UserPoolClientType.make_one(self.boto3_raw_data["UserPoolClient"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUserPoolClientResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserPoolClientResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserPoolClientResponse:
    boto3_raw_data: "type_defs.DescribeUserPoolClientResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UserPoolClient(self):  # pragma: no cover
        return UserPoolClientType.make_one(self.boto3_raw_data["UserPoolClient"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeUserPoolClientResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserPoolClientResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserPoolClientResponse:
    boto3_raw_data: "type_defs.UpdateUserPoolClientResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UserPoolClient(self):  # pragma: no cover
        return UserPoolClientType.make_one(self.boto3_raw_data["UserPoolClient"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUserPoolClientResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserPoolClientResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserPoolDomainResponse:
    boto3_raw_data: "type_defs.DescribeUserPoolDomainResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DomainDescription(self):  # pragma: no cover
        return DomainDescriptionType.make_one(self.boto3_raw_data["DomainDescription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeUserPoolDomainResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserPoolDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserPoolMfaConfigResponse:
    boto3_raw_data: "type_defs.GetUserPoolMfaConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SmsMfaConfiguration(self):  # pragma: no cover
        return SmsMfaConfigType.make_one(self.boto3_raw_data["SmsMfaConfiguration"])

    @cached_property
    def SoftwareTokenMfaConfiguration(self):  # pragma: no cover
        return SoftwareTokenMfaConfigType.make_one(
            self.boto3_raw_data["SoftwareTokenMfaConfiguration"]
        )

    @cached_property
    def EmailMfaConfiguration(self):  # pragma: no cover
        return EmailMfaConfigType.make_one(self.boto3_raw_data["EmailMfaConfiguration"])

    MfaConfiguration = field("MfaConfiguration")

    @cached_property
    def WebAuthnConfiguration(self):  # pragma: no cover
        return WebAuthnConfigurationType.make_one(
            self.boto3_raw_data["WebAuthnConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUserPoolMfaConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUserPoolMfaConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetUserPoolMfaConfigRequest:
    boto3_raw_data: "type_defs.SetUserPoolMfaConfigRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")

    @cached_property
    def SmsMfaConfiguration(self):  # pragma: no cover
        return SmsMfaConfigType.make_one(self.boto3_raw_data["SmsMfaConfiguration"])

    @cached_property
    def SoftwareTokenMfaConfiguration(self):  # pragma: no cover
        return SoftwareTokenMfaConfigType.make_one(
            self.boto3_raw_data["SoftwareTokenMfaConfiguration"]
        )

    @cached_property
    def EmailMfaConfiguration(self):  # pragma: no cover
        return EmailMfaConfigType.make_one(self.boto3_raw_data["EmailMfaConfiguration"])

    MfaConfiguration = field("MfaConfiguration")

    @cached_property
    def WebAuthnConfiguration(self):  # pragma: no cover
        return WebAuthnConfigurationType.make_one(
            self.boto3_raw_data["WebAuthnConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetUserPoolMfaConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetUserPoolMfaConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetUserPoolMfaConfigResponse:
    boto3_raw_data: "type_defs.SetUserPoolMfaConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SmsMfaConfiguration(self):  # pragma: no cover
        return SmsMfaConfigType.make_one(self.boto3_raw_data["SmsMfaConfiguration"])

    @cached_property
    def SoftwareTokenMfaConfiguration(self):  # pragma: no cover
        return SoftwareTokenMfaConfigType.make_one(
            self.boto3_raw_data["SoftwareTokenMfaConfiguration"]
        )

    @cached_property
    def EmailMfaConfiguration(self):  # pragma: no cover
        return EmailMfaConfigType.make_one(self.boto3_raw_data["EmailMfaConfiguration"])

    MfaConfiguration = field("MfaConfiguration")

    @cached_property
    def WebAuthnConfiguration(self):  # pragma: no cover
        return WebAuthnConfigurationType.make_one(
            self.boto3_raw_data["WebAuthnConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetUserPoolMfaConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetUserPoolMfaConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserPoolDescriptionType:
    boto3_raw_data: "type_defs.UserPoolDescriptionTypeTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")

    @cached_property
    def LambdaConfig(self):  # pragma: no cover
        return LambdaConfigType.make_one(self.boto3_raw_data["LambdaConfig"])

    Status = field("Status")
    LastModifiedDate = field("LastModifiedDate")
    CreationDate = field("CreationDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserPoolDescriptionTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserPoolDescriptionTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogDeliveryConfigurationType:
    boto3_raw_data: "type_defs.LogDeliveryConfigurationTypeTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")

    @cached_property
    def LogConfigurations(self):  # pragma: no cover
        return LogConfigurationType.make_many(self.boto3_raw_data["LogConfigurations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LogDeliveryConfigurationTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogDeliveryConfigurationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetLogDeliveryConfigurationRequest:
    boto3_raw_data: "type_defs.SetLogDeliveryConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")

    @cached_property
    def LogConfigurations(self):  # pragma: no cover
        return LogConfigurationType.make_many(self.boto3_raw_data["LogConfigurations"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetLogDeliveryConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetLogDeliveryConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountTakeoverRiskConfigurationType:
    boto3_raw_data: "type_defs.AccountTakeoverRiskConfigurationTypeTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Actions(self):  # pragma: no cover
        return AccountTakeoverActionsType.make_one(self.boto3_raw_data["Actions"])

    @cached_property
    def NotifyConfiguration(self):  # pragma: no cover
        return NotifyConfigurationType.make_one(
            self.boto3_raw_data["NotifyConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AccountTakeoverRiskConfigurationTypeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountTakeoverRiskConfigurationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddCustomAttributesRequest:
    boto3_raw_data: "type_defs.AddCustomAttributesRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")

    @cached_property
    def CustomAttributes(self):  # pragma: no cover
        return SchemaAttributeType.make_many(self.boto3_raw_data["CustomAttributes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddCustomAttributesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddCustomAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserPoolType:
    boto3_raw_data: "type_defs.UserPoolTypeTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")

    @cached_property
    def Policies(self):  # pragma: no cover
        return UserPoolPolicyTypeOutput.make_one(self.boto3_raw_data["Policies"])

    DeletionProtection = field("DeletionProtection")

    @cached_property
    def LambdaConfig(self):  # pragma: no cover
        return LambdaConfigType.make_one(self.boto3_raw_data["LambdaConfig"])

    Status = field("Status")
    LastModifiedDate = field("LastModifiedDate")
    CreationDate = field("CreationDate")

    @cached_property
    def SchemaAttributes(self):  # pragma: no cover
        return SchemaAttributeType.make_many(self.boto3_raw_data["SchemaAttributes"])

    AutoVerifiedAttributes = field("AutoVerifiedAttributes")
    AliasAttributes = field("AliasAttributes")
    UsernameAttributes = field("UsernameAttributes")
    SmsVerificationMessage = field("SmsVerificationMessage")
    EmailVerificationMessage = field("EmailVerificationMessage")
    EmailVerificationSubject = field("EmailVerificationSubject")

    @cached_property
    def VerificationMessageTemplate(self):  # pragma: no cover
        return VerificationMessageTemplateType.make_one(
            self.boto3_raw_data["VerificationMessageTemplate"]
        )

    SmsAuthenticationMessage = field("SmsAuthenticationMessage")

    @cached_property
    def UserAttributeUpdateSettings(self):  # pragma: no cover
        return UserAttributeUpdateSettingsTypeOutput.make_one(
            self.boto3_raw_data["UserAttributeUpdateSettings"]
        )

    MfaConfiguration = field("MfaConfiguration")

    @cached_property
    def DeviceConfiguration(self):  # pragma: no cover
        return DeviceConfigurationType.make_one(
            self.boto3_raw_data["DeviceConfiguration"]
        )

    EstimatedNumberOfUsers = field("EstimatedNumberOfUsers")

    @cached_property
    def EmailConfiguration(self):  # pragma: no cover
        return EmailConfigurationType.make_one(
            self.boto3_raw_data["EmailConfiguration"]
        )

    @cached_property
    def SmsConfiguration(self):  # pragma: no cover
        return SmsConfigurationType.make_one(self.boto3_raw_data["SmsConfiguration"])

    UserPoolTags = field("UserPoolTags")
    SmsConfigurationFailure = field("SmsConfigurationFailure")
    EmailConfigurationFailure = field("EmailConfigurationFailure")
    Domain = field("Domain")
    CustomDomain = field("CustomDomain")

    @cached_property
    def AdminCreateUserConfig(self):  # pragma: no cover
        return AdminCreateUserConfigType.make_one(
            self.boto3_raw_data["AdminCreateUserConfig"]
        )

    @cached_property
    def UserPoolAddOns(self):  # pragma: no cover
        return UserPoolAddOnsType.make_one(self.boto3_raw_data["UserPoolAddOns"])

    @cached_property
    def UsernameConfiguration(self):  # pragma: no cover
        return UsernameConfigurationType.make_one(
            self.boto3_raw_data["UsernameConfiguration"]
        )

    Arn = field("Arn")

    @cached_property
    def AccountRecoverySetting(self):  # pragma: no cover
        return AccountRecoverySettingTypeOutput.make_one(
            self.boto3_raw_data["AccountRecoverySetting"]
        )

    UserPoolTier = field("UserPoolTier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserPoolTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserPoolTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateManagedLoginBrandingRequest:
    boto3_raw_data: "type_defs.CreateManagedLoginBrandingRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    ClientId = field("ClientId")
    UseCognitoProvidedValues = field("UseCognitoProvidedValues")
    Settings = field("Settings")
    Assets = field("Assets")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateManagedLoginBrandingRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateManagedLoginBrandingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateManagedLoginBrandingRequest:
    boto3_raw_data: "type_defs.UpdateManagedLoginBrandingRequestTypeDef" = (
        dataclasses.field()
    )

    UserPoolId = field("UserPoolId")
    ManagedLoginBrandingId = field("ManagedLoginBrandingId")
    UseCognitoProvidedValues = field("UseCognitoProvidedValues")
    Settings = field("Settings")
    Assets = field("Assets")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateManagedLoginBrandingRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateManagedLoginBrandingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserPoolsResponse:
    boto3_raw_data: "type_defs.ListUserPoolsResponseTypeDef" = dataclasses.field()

    @cached_property
    def UserPools(self):  # pragma: no cover
        return UserPoolDescriptionType.make_many(self.boto3_raw_data["UserPools"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUserPoolsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserPoolsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLogDeliveryConfigurationResponse:
    boto3_raw_data: "type_defs.GetLogDeliveryConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LogDeliveryConfiguration(self):  # pragma: no cover
        return LogDeliveryConfigurationType.make_one(
            self.boto3_raw_data["LogDeliveryConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetLogDeliveryConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLogDeliveryConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetLogDeliveryConfigurationResponse:
    boto3_raw_data: "type_defs.SetLogDeliveryConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LogDeliveryConfiguration(self):  # pragma: no cover
        return LogDeliveryConfigurationType.make_one(
            self.boto3_raw_data["LogDeliveryConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetLogDeliveryConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetLogDeliveryConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RiskConfigurationType:
    boto3_raw_data: "type_defs.RiskConfigurationTypeTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    ClientId = field("ClientId")

    @cached_property
    def CompromisedCredentialsRiskConfiguration(self):  # pragma: no cover
        return CompromisedCredentialsRiskConfigurationTypeOutput.make_one(
            self.boto3_raw_data["CompromisedCredentialsRiskConfiguration"]
        )

    @cached_property
    def AccountTakeoverRiskConfiguration(self):  # pragma: no cover
        return AccountTakeoverRiskConfigurationType.make_one(
            self.boto3_raw_data["AccountTakeoverRiskConfiguration"]
        )

    @cached_property
    def RiskExceptionConfiguration(self):  # pragma: no cover
        return RiskExceptionConfigurationTypeOutput.make_one(
            self.boto3_raw_data["RiskExceptionConfiguration"]
        )

    LastModifiedDate = field("LastModifiedDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RiskConfigurationTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RiskConfigurationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetRiskConfigurationRequest:
    boto3_raw_data: "type_defs.SetRiskConfigurationRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    ClientId = field("ClientId")
    CompromisedCredentialsRiskConfiguration = field(
        "CompromisedCredentialsRiskConfiguration"
    )

    @cached_property
    def AccountTakeoverRiskConfiguration(self):  # pragma: no cover
        return AccountTakeoverRiskConfigurationType.make_one(
            self.boto3_raw_data["AccountTakeoverRiskConfiguration"]
        )

    RiskExceptionConfiguration = field("RiskExceptionConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetRiskConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetRiskConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserPoolResponse:
    boto3_raw_data: "type_defs.CreateUserPoolResponseTypeDef" = dataclasses.field()

    @cached_property
    def UserPool(self):  # pragma: no cover
        return UserPoolType.make_one(self.boto3_raw_data["UserPool"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUserPoolResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserPoolResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserPoolResponse:
    boto3_raw_data: "type_defs.DescribeUserPoolResponseTypeDef" = dataclasses.field()

    @cached_property
    def UserPool(self):  # pragma: no cover
        return UserPoolType.make_one(self.boto3_raw_data["UserPool"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUserPoolResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserPoolResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserPoolRequest:
    boto3_raw_data: "type_defs.CreateUserPoolRequestTypeDef" = dataclasses.field()

    PoolName = field("PoolName")
    Policies = field("Policies")
    DeletionProtection = field("DeletionProtection")

    @cached_property
    def LambdaConfig(self):  # pragma: no cover
        return LambdaConfigType.make_one(self.boto3_raw_data["LambdaConfig"])

    AutoVerifiedAttributes = field("AutoVerifiedAttributes")
    AliasAttributes = field("AliasAttributes")
    UsernameAttributes = field("UsernameAttributes")
    SmsVerificationMessage = field("SmsVerificationMessage")
    EmailVerificationMessage = field("EmailVerificationMessage")
    EmailVerificationSubject = field("EmailVerificationSubject")

    @cached_property
    def VerificationMessageTemplate(self):  # pragma: no cover
        return VerificationMessageTemplateType.make_one(
            self.boto3_raw_data["VerificationMessageTemplate"]
        )

    SmsAuthenticationMessage = field("SmsAuthenticationMessage")
    MfaConfiguration = field("MfaConfiguration")
    UserAttributeUpdateSettings = field("UserAttributeUpdateSettings")

    @cached_property
    def DeviceConfiguration(self):  # pragma: no cover
        return DeviceConfigurationType.make_one(
            self.boto3_raw_data["DeviceConfiguration"]
        )

    @cached_property
    def EmailConfiguration(self):  # pragma: no cover
        return EmailConfigurationType.make_one(
            self.boto3_raw_data["EmailConfiguration"]
        )

    @cached_property
    def SmsConfiguration(self):  # pragma: no cover
        return SmsConfigurationType.make_one(self.boto3_raw_data["SmsConfiguration"])

    UserPoolTags = field("UserPoolTags")

    @cached_property
    def AdminCreateUserConfig(self):  # pragma: no cover
        return AdminCreateUserConfigType.make_one(
            self.boto3_raw_data["AdminCreateUserConfig"]
        )

    @cached_property
    def Schema(self):  # pragma: no cover
        return SchemaAttributeType.make_many(self.boto3_raw_data["Schema"])

    @cached_property
    def UserPoolAddOns(self):  # pragma: no cover
        return UserPoolAddOnsType.make_one(self.boto3_raw_data["UserPoolAddOns"])

    @cached_property
    def UsernameConfiguration(self):  # pragma: no cover
        return UsernameConfigurationType.make_one(
            self.boto3_raw_data["UsernameConfiguration"]
        )

    AccountRecoverySetting = field("AccountRecoverySetting")
    UserPoolTier = field("UserPoolTier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUserPoolRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserPoolRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserPoolRequest:
    boto3_raw_data: "type_defs.UpdateUserPoolRequestTypeDef" = dataclasses.field()

    UserPoolId = field("UserPoolId")
    Policies = field("Policies")
    DeletionProtection = field("DeletionProtection")

    @cached_property
    def LambdaConfig(self):  # pragma: no cover
        return LambdaConfigType.make_one(self.boto3_raw_data["LambdaConfig"])

    AutoVerifiedAttributes = field("AutoVerifiedAttributes")
    SmsVerificationMessage = field("SmsVerificationMessage")
    EmailVerificationMessage = field("EmailVerificationMessage")
    EmailVerificationSubject = field("EmailVerificationSubject")

    @cached_property
    def VerificationMessageTemplate(self):  # pragma: no cover
        return VerificationMessageTemplateType.make_one(
            self.boto3_raw_data["VerificationMessageTemplate"]
        )

    SmsAuthenticationMessage = field("SmsAuthenticationMessage")
    UserAttributeUpdateSettings = field("UserAttributeUpdateSettings")
    MfaConfiguration = field("MfaConfiguration")

    @cached_property
    def DeviceConfiguration(self):  # pragma: no cover
        return DeviceConfigurationType.make_one(
            self.boto3_raw_data["DeviceConfiguration"]
        )

    @cached_property
    def EmailConfiguration(self):  # pragma: no cover
        return EmailConfigurationType.make_one(
            self.boto3_raw_data["EmailConfiguration"]
        )

    @cached_property
    def SmsConfiguration(self):  # pragma: no cover
        return SmsConfigurationType.make_one(self.boto3_raw_data["SmsConfiguration"])

    UserPoolTags = field("UserPoolTags")

    @cached_property
    def AdminCreateUserConfig(self):  # pragma: no cover
        return AdminCreateUserConfigType.make_one(
            self.boto3_raw_data["AdminCreateUserConfig"]
        )

    @cached_property
    def UserPoolAddOns(self):  # pragma: no cover
        return UserPoolAddOnsType.make_one(self.boto3_raw_data["UserPoolAddOns"])

    AccountRecoverySetting = field("AccountRecoverySetting")
    PoolName = field("PoolName")
    UserPoolTier = field("UserPoolTier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUserPoolRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserPoolRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRiskConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeRiskConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RiskConfiguration(self):  # pragma: no cover
        return RiskConfigurationType.make_one(self.boto3_raw_data["RiskConfiguration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRiskConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRiskConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetRiskConfigurationResponse:
    boto3_raw_data: "type_defs.SetRiskConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RiskConfiguration(self):  # pragma: no cover
        return RiskConfigurationType.make_one(self.boto3_raw_data["RiskConfiguration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetRiskConfigurationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetRiskConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
