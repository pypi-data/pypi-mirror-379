# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_chime_sdk_messaging import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AppInstanceUserMembershipSummary:
    boto3_raw_data: "type_defs.AppInstanceUserMembershipSummaryTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")
    ReadMarkerTimestamp = field("ReadMarkerTimestamp")
    SubChannelId = field("SubChannelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AppInstanceUserMembershipSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppInstanceUserMembershipSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateChannelFlowRequest:
    boto3_raw_data: "type_defs.AssociateChannelFlowRequestTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")
    ChannelFlowArn = field("ChannelFlowArn")
    ChimeBearer = field("ChimeBearer")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateChannelFlowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateChannelFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Identity:
    boto3_raw_data: "type_defs.IdentityTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IdentityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IdentityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateChannelMembershipError:
    boto3_raw_data: "type_defs.BatchCreateChannelMembershipErrorTypeDef" = (
        dataclasses.field()
    )

    MemberArn = field("MemberArn")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateChannelMembershipErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateChannelMembershipErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateChannelMembershipRequest:
    boto3_raw_data: "type_defs.BatchCreateChannelMembershipRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")
    MemberArns = field("MemberArns")
    ChimeBearer = field("ChimeBearer")
    Type = field("Type")
    SubChannelId = field("SubChannelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateChannelMembershipRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateChannelMembershipRequestTypeDef"]
        ],
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
class ChannelAssociatedWithFlowSummary:
    boto3_raw_data: "type_defs.ChannelAssociatedWithFlowSummaryTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    ChannelArn = field("ChannelArn")
    Mode = field("Mode")
    Privacy = field("Privacy")
    Metadata = field("Metadata")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ChannelAssociatedWithFlowSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelAssociatedWithFlowSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelSummary:
    boto3_raw_data: "type_defs.ChannelSummaryTypeDef" = dataclasses.field()

    Name = field("Name")
    ChannelArn = field("ChannelArn")
    Mode = field("Mode")
    Privacy = field("Privacy")
    Metadata = field("Metadata")
    LastMessageTimestamp = field("LastMessageTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChannelSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PushNotificationPreferences:
    boto3_raw_data: "type_defs.PushNotificationPreferencesTypeDef" = dataclasses.field()

    AllowNotifications = field("AllowNotifications")
    FilterRule = field("FilterRule")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PushNotificationPreferencesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PushNotificationPreferencesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PushNotificationConfiguration:
    boto3_raw_data: "type_defs.PushNotificationConfigurationTypeDef" = (
        dataclasses.field()
    )

    Title = field("Title")
    Body = field("Body")
    Type = field("Type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PushNotificationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PushNotificationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelMessageStatusStructure:
    boto3_raw_data: "type_defs.ChannelMessageStatusStructureTypeDef" = (
        dataclasses.field()
    )

    Value = field("Value")
    Detail = field("Detail")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ChannelMessageStatusStructureTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelMessageStatusStructureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageAttributeValueOutput:
    boto3_raw_data: "type_defs.MessageAttributeValueOutputTypeDef" = dataclasses.field()

    StringValues = field("StringValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessageAttributeValueOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageAttributeValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Target:
    boto3_raw_data: "type_defs.TargetTypeDef" = dataclasses.field()

    MemberArn = field("MemberArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElasticChannelConfiguration:
    boto3_raw_data: "type_defs.ElasticChannelConfigurationTypeDef" = dataclasses.field()

    MaximumSubChannels = field("MaximumSubChannels")
    TargetMembershipsPerSubChannel = field("TargetMembershipsPerSubChannel")
    MinimumMembershipPercentage = field("MinimumMembershipPercentage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ElasticChannelConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ElasticChannelConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpirationSettings:
    boto3_raw_data: "type_defs.ExpirationSettingsTypeDef" = dataclasses.field()

    ExpirationDays = field("ExpirationDays")
    ExpirationCriterion = field("ExpirationCriterion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExpirationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpirationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelBanRequest:
    boto3_raw_data: "type_defs.CreateChannelBanRequestTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")
    MemberArn = field("MemberArn")
    ChimeBearer = field("ChimeBearer")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateChannelBanRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelBanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelMembershipRequest:
    boto3_raw_data: "type_defs.CreateChannelMembershipRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")
    MemberArn = field("MemberArn")
    Type = field("Type")
    ChimeBearer = field("ChimeBearer")
    SubChannelId = field("SubChannelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateChannelMembershipRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelMembershipRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelModeratorRequest:
    boto3_raw_data: "type_defs.CreateChannelModeratorRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")
    ChannelModeratorArn = field("ChannelModeratorArn")
    ChimeBearer = field("ChimeBearer")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateChannelModeratorRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelModeratorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteChannelBanRequest:
    boto3_raw_data: "type_defs.DeleteChannelBanRequestTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")
    MemberArn = field("MemberArn")
    ChimeBearer = field("ChimeBearer")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteChannelBanRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteChannelBanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteChannelFlowRequest:
    boto3_raw_data: "type_defs.DeleteChannelFlowRequestTypeDef" = dataclasses.field()

    ChannelFlowArn = field("ChannelFlowArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteChannelFlowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteChannelFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteChannelMembershipRequest:
    boto3_raw_data: "type_defs.DeleteChannelMembershipRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")
    MemberArn = field("MemberArn")
    ChimeBearer = field("ChimeBearer")
    SubChannelId = field("SubChannelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteChannelMembershipRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteChannelMembershipRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteChannelMessageRequest:
    boto3_raw_data: "type_defs.DeleteChannelMessageRequestTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")
    MessageId = field("MessageId")
    ChimeBearer = field("ChimeBearer")
    SubChannelId = field("SubChannelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteChannelMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteChannelMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteChannelModeratorRequest:
    boto3_raw_data: "type_defs.DeleteChannelModeratorRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")
    ChannelModeratorArn = field("ChannelModeratorArn")
    ChimeBearer = field("ChimeBearer")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteChannelModeratorRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteChannelModeratorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteChannelRequest:
    boto3_raw_data: "type_defs.DeleteChannelRequestTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")
    ChimeBearer = field("ChimeBearer")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMessagingStreamingConfigurationsRequest:
    boto3_raw_data: "type_defs.DeleteMessagingStreamingConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    AppInstanceArn = field("AppInstanceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteMessagingStreamingConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMessagingStreamingConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelBanRequest:
    boto3_raw_data: "type_defs.DescribeChannelBanRequestTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")
    MemberArn = field("MemberArn")
    ChimeBearer = field("ChimeBearer")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChannelBanRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelBanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelFlowRequest:
    boto3_raw_data: "type_defs.DescribeChannelFlowRequestTypeDef" = dataclasses.field()

    ChannelFlowArn = field("ChannelFlowArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChannelFlowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelMembershipForAppInstanceUserRequest:
    boto3_raw_data: (
        "type_defs.DescribeChannelMembershipForAppInstanceUserRequestTypeDef"
    ) = dataclasses.field()

    ChannelArn = field("ChannelArn")
    AppInstanceUserArn = field("AppInstanceUserArn")
    ChimeBearer = field("ChimeBearer")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeChannelMembershipForAppInstanceUserRequestTypeDef"
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
                "type_defs.DescribeChannelMembershipForAppInstanceUserRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelMembershipRequest:
    boto3_raw_data: "type_defs.DescribeChannelMembershipRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")
    MemberArn = field("MemberArn")
    ChimeBearer = field("ChimeBearer")
    SubChannelId = field("SubChannelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeChannelMembershipRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelMembershipRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelModeratedByAppInstanceUserRequest:
    boto3_raw_data: (
        "type_defs.DescribeChannelModeratedByAppInstanceUserRequestTypeDef"
    ) = dataclasses.field()

    ChannelArn = field("ChannelArn")
    AppInstanceUserArn = field("AppInstanceUserArn")
    ChimeBearer = field("ChimeBearer")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeChannelModeratedByAppInstanceUserRequestTypeDef"
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
                "type_defs.DescribeChannelModeratedByAppInstanceUserRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelModeratorRequest:
    boto3_raw_data: "type_defs.DescribeChannelModeratorRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")
    ChannelModeratorArn = field("ChannelModeratorArn")
    ChimeBearer = field("ChimeBearer")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeChannelModeratorRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelModeratorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelRequest:
    boto3_raw_data: "type_defs.DescribeChannelRequestTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")
    ChimeBearer = field("ChimeBearer")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateChannelFlowRequest:
    boto3_raw_data: "type_defs.DisassociateChannelFlowRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")
    ChannelFlowArn = field("ChannelFlowArn")
    ChimeBearer = field("ChimeBearer")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateChannelFlowRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateChannelFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChannelMembershipPreferencesRequest:
    boto3_raw_data: "type_defs.GetChannelMembershipPreferencesRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")
    MemberArn = field("MemberArn")
    ChimeBearer = field("ChimeBearer")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetChannelMembershipPreferencesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChannelMembershipPreferencesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChannelMessageRequest:
    boto3_raw_data: "type_defs.GetChannelMessageRequestTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")
    MessageId = field("MessageId")
    ChimeBearer = field("ChimeBearer")
    SubChannelId = field("SubChannelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetChannelMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChannelMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChannelMessageStatusRequest:
    boto3_raw_data: "type_defs.GetChannelMessageStatusRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")
    MessageId = field("MessageId")
    ChimeBearer = field("ChimeBearer")
    SubChannelId = field("SubChannelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetChannelMessageStatusRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChannelMessageStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMessagingSessionEndpointRequest:
    boto3_raw_data: "type_defs.GetMessagingSessionEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    NetworkType = field("NetworkType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMessagingSessionEndpointRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMessagingSessionEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessagingSessionEndpoint:
    boto3_raw_data: "type_defs.MessagingSessionEndpointTypeDef" = dataclasses.field()

    Url = field("Url")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessagingSessionEndpointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessagingSessionEndpointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMessagingStreamingConfigurationsRequest:
    boto3_raw_data: "type_defs.GetMessagingStreamingConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    AppInstanceArn = field("AppInstanceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMessagingStreamingConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMessagingStreamingConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamingConfiguration:
    boto3_raw_data: "type_defs.StreamingConfigurationTypeDef" = dataclasses.field()

    DataType = field("DataType")
    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaConfiguration:
    boto3_raw_data: "type_defs.LambdaConfigurationTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    InvocationType = field("InvocationType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelBansRequest:
    boto3_raw_data: "type_defs.ListChannelBansRequestTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")
    ChimeBearer = field("ChimeBearer")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelBansRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelBansRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelFlowsRequest:
    boto3_raw_data: "type_defs.ListChannelFlowsRequestTypeDef" = dataclasses.field()

    AppInstanceArn = field("AppInstanceArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelFlowsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelFlowsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelMembershipsForAppInstanceUserRequest:
    boto3_raw_data: (
        "type_defs.ListChannelMembershipsForAppInstanceUserRequestTypeDef"
    ) = dataclasses.field()

    ChimeBearer = field("ChimeBearer")
    AppInstanceUserArn = field("AppInstanceUserArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListChannelMembershipsForAppInstanceUserRequestTypeDef"
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
                "type_defs.ListChannelMembershipsForAppInstanceUserRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelMembershipsRequest:
    boto3_raw_data: "type_defs.ListChannelMembershipsRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")
    ChimeBearer = field("ChimeBearer")
    Type = field("Type")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    SubChannelId = field("SubChannelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListChannelMembershipsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelMembershipsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelModeratorsRequest:
    boto3_raw_data: "type_defs.ListChannelModeratorsRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")
    ChimeBearer = field("ChimeBearer")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelModeratorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelModeratorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelsAssociatedWithChannelFlowRequest:
    boto3_raw_data: "type_defs.ListChannelsAssociatedWithChannelFlowRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelFlowArn = field("ChannelFlowArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListChannelsAssociatedWithChannelFlowRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelsAssociatedWithChannelFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelsModeratedByAppInstanceUserRequest:
    boto3_raw_data: "type_defs.ListChannelsModeratedByAppInstanceUserRequestTypeDef" = (
        dataclasses.field()
    )

    ChimeBearer = field("ChimeBearer")
    AppInstanceUserArn = field("AppInstanceUserArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListChannelsModeratedByAppInstanceUserRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelsModeratedByAppInstanceUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelsRequest:
    boto3_raw_data: "type_defs.ListChannelsRequestTypeDef" = dataclasses.field()

    AppInstanceArn = field("AppInstanceArn")
    ChimeBearer = field("ChimeBearer")
    Privacy = field("Privacy")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubChannelsRequest:
    boto3_raw_data: "type_defs.ListSubChannelsRequestTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")
    ChimeBearer = field("ChimeBearer")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSubChannelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubChannelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubChannelSummary:
    boto3_raw_data: "type_defs.SubChannelSummaryTypeDef" = dataclasses.field()

    SubChannelId = field("SubChannelId")
    MembershipCount = field("MembershipCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubChannelSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubChannelSummaryTypeDef"]
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

    ResourceARN = field("ResourceARN")

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
class MessageAttributeValue:
    boto3_raw_data: "type_defs.MessageAttributeValueTypeDef" = dataclasses.field()

    StringValues = field("StringValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessageAttributeValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageAttributeValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedactChannelMessageRequest:
    boto3_raw_data: "type_defs.RedactChannelMessageRequestTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")
    MessageId = field("MessageId")
    ChimeBearer = field("ChimeBearer")
    SubChannelId = field("SubChannelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedactChannelMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedactChannelMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchField:
    boto3_raw_data: "type_defs.SearchFieldTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")
    Operator = field("Operator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SearchFieldTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
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
class UpdateChannelMessageRequest:
    boto3_raw_data: "type_defs.UpdateChannelMessageRequestTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")
    MessageId = field("MessageId")
    Content = field("Content")
    ChimeBearer = field("ChimeBearer")
    Metadata = field("Metadata")
    SubChannelId = field("SubChannelId")
    ContentType = field("ContentType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateChannelMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChannelReadMarkerRequest:
    boto3_raw_data: "type_defs.UpdateChannelReadMarkerRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")
    ChimeBearer = field("ChimeBearer")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateChannelReadMarkerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelReadMarkerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChannelRequest:
    boto3_raw_data: "type_defs.UpdateChannelRequestTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")
    ChimeBearer = field("ChimeBearer")
    Name = field("Name")
    Mode = field("Mode")
    Metadata = field("Metadata")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchChannelMemberships:
    boto3_raw_data: "type_defs.BatchChannelMembershipsTypeDef" = dataclasses.field()

    @cached_property
    def InvitedBy(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["InvitedBy"])

    Type = field("Type")

    @cached_property
    def Members(self):  # pragma: no cover
        return Identity.make_many(self.boto3_raw_data["Members"])

    ChannelArn = field("ChannelArn")
    SubChannelId = field("SubChannelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchChannelMembershipsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchChannelMembershipsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelBanSummary:
    boto3_raw_data: "type_defs.ChannelBanSummaryTypeDef" = dataclasses.field()

    @cached_property
    def Member(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["Member"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelBanSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelBanSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelBan:
    boto3_raw_data: "type_defs.ChannelBanTypeDef" = dataclasses.field()

    @cached_property
    def Member(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["Member"])

    ChannelArn = field("ChannelArn")
    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def CreatedBy(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["CreatedBy"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelBanTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChannelBanTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelMembershipSummary:
    boto3_raw_data: "type_defs.ChannelMembershipSummaryTypeDef" = dataclasses.field()

    @cached_property
    def Member(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["Member"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChannelMembershipSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelMembershipSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelMembership:
    boto3_raw_data: "type_defs.ChannelMembershipTypeDef" = dataclasses.field()

    @cached_property
    def InvitedBy(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["InvitedBy"])

    Type = field("Type")

    @cached_property
    def Member(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["Member"])

    ChannelArn = field("ChannelArn")
    CreatedTimestamp = field("CreatedTimestamp")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    SubChannelId = field("SubChannelId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelMembershipTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelMembershipTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelModeratorSummary:
    boto3_raw_data: "type_defs.ChannelModeratorSummaryTypeDef" = dataclasses.field()

    @cached_property
    def Moderator(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["Moderator"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChannelModeratorSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelModeratorSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelModerator:
    boto3_raw_data: "type_defs.ChannelModeratorTypeDef" = dataclasses.field()

    @cached_property
    def Moderator(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["Moderator"])

    ChannelArn = field("ChannelArn")
    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def CreatedBy(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["CreatedBy"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelModeratorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelModeratorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelFlowCallbackResponse:
    boto3_raw_data: "type_defs.ChannelFlowCallbackResponseTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")
    CallbackId = field("CallbackId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChannelFlowCallbackResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelFlowCallbackResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelBanResponse:
    boto3_raw_data: "type_defs.CreateChannelBanResponseTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")

    @cached_property
    def Member(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["Member"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateChannelBanResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelBanResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelFlowResponse:
    boto3_raw_data: "type_defs.CreateChannelFlowResponseTypeDef" = dataclasses.field()

    ChannelFlowArn = field("ChannelFlowArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateChannelFlowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelMembershipResponse:
    boto3_raw_data: "type_defs.CreateChannelMembershipResponseTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")

    @cached_property
    def Member(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["Member"])

    SubChannelId = field("SubChannelId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateChannelMembershipResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelMembershipResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelModeratorResponse:
    boto3_raw_data: "type_defs.CreateChannelModeratorResponseTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")

    @cached_property
    def ChannelModerator(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["ChannelModerator"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateChannelModeratorResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelModeratorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelResponse:
    boto3_raw_data: "type_defs.CreateChannelResponseTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelResponseTypeDef"]
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
class RedactChannelMessageResponse:
    boto3_raw_data: "type_defs.RedactChannelMessageResponseTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")
    MessageId = field("MessageId")
    SubChannelId = field("SubChannelId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedactChannelMessageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedactChannelMessageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChannelFlowResponse:
    boto3_raw_data: "type_defs.UpdateChannelFlowResponseTypeDef" = dataclasses.field()

    ChannelFlowArn = field("ChannelFlowArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateChannelFlowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChannelReadMarkerResponse:
    boto3_raw_data: "type_defs.UpdateChannelReadMarkerResponseTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateChannelReadMarkerResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelReadMarkerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChannelResponse:
    boto3_raw_data: "type_defs.UpdateChannelResponseTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelsAssociatedWithChannelFlowResponse:
    boto3_raw_data: "type_defs.ListChannelsAssociatedWithChannelFlowResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Channels(self):  # pragma: no cover
        return ChannelAssociatedWithFlowSummary.make_many(
            self.boto3_raw_data["Channels"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListChannelsAssociatedWithChannelFlowResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelsAssociatedWithChannelFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelMembershipForAppInstanceUserSummary:
    boto3_raw_data: "type_defs.ChannelMembershipForAppInstanceUserSummaryTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ChannelSummary(self):  # pragma: no cover
        return ChannelSummary.make_one(self.boto3_raw_data["ChannelSummary"])

    @cached_property
    def AppInstanceUserMembershipSummary(self):  # pragma: no cover
        return AppInstanceUserMembershipSummary.make_one(
            self.boto3_raw_data["AppInstanceUserMembershipSummary"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChannelMembershipForAppInstanceUserSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelMembershipForAppInstanceUserSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelModeratedByAppInstanceUserSummary:
    boto3_raw_data: "type_defs.ChannelModeratedByAppInstanceUserSummaryTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ChannelSummary(self):  # pragma: no cover
        return ChannelSummary.make_one(self.boto3_raw_data["ChannelSummary"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChannelModeratedByAppInstanceUserSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelModeratedByAppInstanceUserSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelsResponse:
    boto3_raw_data: "type_defs.ListChannelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Channels(self):  # pragma: no cover
        return ChannelSummary.make_many(self.boto3_raw_data["Channels"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchChannelsResponse:
    boto3_raw_data: "type_defs.SearchChannelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Channels(self):  # pragma: no cover
        return ChannelSummary.make_many(self.boto3_raw_data["Channels"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchChannelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchChannelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelMembershipPreferences:
    boto3_raw_data: "type_defs.ChannelMembershipPreferencesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PushNotifications(self):  # pragma: no cover
        return PushNotificationPreferences.make_one(
            self.boto3_raw_data["PushNotifications"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChannelMembershipPreferencesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelMembershipPreferencesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChannelMessageStatusResponse:
    boto3_raw_data: "type_defs.GetChannelMessageStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Status(self):  # pragma: no cover
        return ChannelMessageStatusStructure.make_one(self.boto3_raw_data["Status"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetChannelMessageStatusResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChannelMessageStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendChannelMessageResponse:
    boto3_raw_data: "type_defs.SendChannelMessageResponseTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")
    MessageId = field("MessageId")

    @cached_property
    def Status(self):  # pragma: no cover
        return ChannelMessageStatusStructure.make_one(self.boto3_raw_data["Status"])

    SubChannelId = field("SubChannelId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendChannelMessageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendChannelMessageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChannelMessageResponse:
    boto3_raw_data: "type_defs.UpdateChannelMessageResponseTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")
    MessageId = field("MessageId")

    @cached_property
    def Status(self):  # pragma: no cover
        return ChannelMessageStatusStructure.make_one(self.boto3_raw_data["Status"])

    SubChannelId = field("SubChannelId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateChannelMessageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelMessageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelMessageSummary:
    boto3_raw_data: "type_defs.ChannelMessageSummaryTypeDef" = dataclasses.field()

    MessageId = field("MessageId")
    Content = field("Content")
    Metadata = field("Metadata")
    Type = field("Type")
    CreatedTimestamp = field("CreatedTimestamp")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    LastEditedTimestamp = field("LastEditedTimestamp")

    @cached_property
    def Sender(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["Sender"])

    Redacted = field("Redacted")

    @cached_property
    def Status(self):  # pragma: no cover
        return ChannelMessageStatusStructure.make_one(self.boto3_raw_data["Status"])

    MessageAttributes = field("MessageAttributes")
    ContentType = field("ContentType")

    @cached_property
    def Target(self):  # pragma: no cover
        return Target.make_many(self.boto3_raw_data["Target"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChannelMessageSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelMessageSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelMessage:
    boto3_raw_data: "type_defs.ChannelMessageTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")
    MessageId = field("MessageId")
    Content = field("Content")
    Metadata = field("Metadata")
    Type = field("Type")
    CreatedTimestamp = field("CreatedTimestamp")
    LastEditedTimestamp = field("LastEditedTimestamp")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")

    @cached_property
    def Sender(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["Sender"])

    Redacted = field("Redacted")
    Persistence = field("Persistence")

    @cached_property
    def Status(self):  # pragma: no cover
        return ChannelMessageStatusStructure.make_one(self.boto3_raw_data["Status"])

    MessageAttributes = field("MessageAttributes")
    SubChannelId = field("SubChannelId")
    ContentType = field("ContentType")

    @cached_property
    def Target(self):  # pragma: no cover
        return Target.make_many(self.boto3_raw_data["Target"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChannelMessageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Channel:
    boto3_raw_data: "type_defs.ChannelTypeDef" = dataclasses.field()

    Name = field("Name")
    ChannelArn = field("ChannelArn")
    Mode = field("Mode")
    Privacy = field("Privacy")
    Metadata = field("Metadata")

    @cached_property
    def CreatedBy(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["CreatedBy"])

    CreatedTimestamp = field("CreatedTimestamp")
    LastMessageTimestamp = field("LastMessageTimestamp")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    ChannelFlowArn = field("ChannelFlowArn")

    @cached_property
    def ElasticChannelConfiguration(self):  # pragma: no cover
        return ElasticChannelConfiguration.make_one(
            self.boto3_raw_data["ElasticChannelConfiguration"]
        )

    @cached_property
    def ExpirationSettings(self):  # pragma: no cover
        return ExpirationSettings.make_one(self.boto3_raw_data["ExpirationSettings"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChannelTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutChannelExpirationSettingsRequest:
    boto3_raw_data: "type_defs.PutChannelExpirationSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")
    ChimeBearer = field("ChimeBearer")

    @cached_property
    def ExpirationSettings(self):  # pragma: no cover
        return ExpirationSettings.make_one(self.boto3_raw_data["ExpirationSettings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutChannelExpirationSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutChannelExpirationSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutChannelExpirationSettingsResponse:
    boto3_raw_data: "type_defs.PutChannelExpirationSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")

    @cached_property
    def ExpirationSettings(self):  # pragma: no cover
        return ExpirationSettings.make_one(self.boto3_raw_data["ExpirationSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutChannelExpirationSettingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutChannelExpirationSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelRequest:
    boto3_raw_data: "type_defs.CreateChannelRequestTypeDef" = dataclasses.field()

    AppInstanceArn = field("AppInstanceArn")
    Name = field("Name")
    ClientRequestToken = field("ClientRequestToken")
    ChimeBearer = field("ChimeBearer")
    Mode = field("Mode")
    Privacy = field("Privacy")
    Metadata = field("Metadata")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ChannelId = field("ChannelId")
    MemberArns = field("MemberArns")
    ModeratorArns = field("ModeratorArns")

    @cached_property
    def ElasticChannelConfiguration(self):  # pragma: no cover
        return ElasticChannelConfiguration.make_one(
            self.boto3_raw_data["ElasticChannelConfiguration"]
        )

    @cached_property
    def ExpirationSettings(self):  # pragma: no cover
        return ExpirationSettings.make_one(self.boto3_raw_data["ExpirationSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelRequestTypeDef"]
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

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class GetMessagingSessionEndpointResponse:
    boto3_raw_data: "type_defs.GetMessagingSessionEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Endpoint(self):  # pragma: no cover
        return MessagingSessionEndpoint.make_one(self.boto3_raw_data["Endpoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMessagingSessionEndpointResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMessagingSessionEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMessagingStreamingConfigurationsResponse:
    boto3_raw_data: "type_defs.GetMessagingStreamingConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StreamingConfigurations(self):  # pragma: no cover
        return StreamingConfiguration.make_many(
            self.boto3_raw_data["StreamingConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMessagingStreamingConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMessagingStreamingConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutMessagingStreamingConfigurationsRequest:
    boto3_raw_data: "type_defs.PutMessagingStreamingConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    AppInstanceArn = field("AppInstanceArn")

    @cached_property
    def StreamingConfigurations(self):  # pragma: no cover
        return StreamingConfiguration.make_many(
            self.boto3_raw_data["StreamingConfigurations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutMessagingStreamingConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutMessagingStreamingConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutMessagingStreamingConfigurationsResponse:
    boto3_raw_data: "type_defs.PutMessagingStreamingConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StreamingConfigurations(self):  # pragma: no cover
        return StreamingConfiguration.make_many(
            self.boto3_raw_data["StreamingConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutMessagingStreamingConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutMessagingStreamingConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProcessorConfiguration:
    boto3_raw_data: "type_defs.ProcessorConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def Lambda(self):  # pragma: no cover
        return LambdaConfiguration.make_one(self.boto3_raw_data["Lambda"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProcessorConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProcessorConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelMessagesRequest:
    boto3_raw_data: "type_defs.ListChannelMessagesRequestTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")
    ChimeBearer = field("ChimeBearer")
    SortOrder = field("SortOrder")
    NotBefore = field("NotBefore")
    NotAfter = field("NotAfter")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    SubChannelId = field("SubChannelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelMessagesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelMessagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubChannelsResponse:
    boto3_raw_data: "type_defs.ListSubChannelsResponseTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")

    @cached_property
    def SubChannels(self):  # pragma: no cover
        return SubChannelSummary.make_many(self.boto3_raw_data["SubChannels"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSubChannelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubChannelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchChannelsRequest:
    boto3_raw_data: "type_defs.SearchChannelsRequestTypeDef" = dataclasses.field()

    @cached_property
    def Fields(self):  # pragma: no cover
        return SearchField.make_many(self.boto3_raw_data["Fields"])

    ChimeBearer = field("ChimeBearer")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchChannelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchChannelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateChannelMembershipResponse:
    boto3_raw_data: "type_defs.BatchCreateChannelMembershipResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BatchChannelMemberships(self):  # pragma: no cover
        return BatchChannelMemberships.make_one(
            self.boto3_raw_data["BatchChannelMemberships"]
        )

    @cached_property
    def Errors(self):  # pragma: no cover
        return BatchCreateChannelMembershipError.make_many(
            self.boto3_raw_data["Errors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateChannelMembershipResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateChannelMembershipResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelBansResponse:
    boto3_raw_data: "type_defs.ListChannelBansResponseTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")

    @cached_property
    def ChannelBans(self):  # pragma: no cover
        return ChannelBanSummary.make_many(self.boto3_raw_data["ChannelBans"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelBansResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelBansResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelBanResponse:
    boto3_raw_data: "type_defs.DescribeChannelBanResponseTypeDef" = dataclasses.field()

    @cached_property
    def ChannelBan(self):  # pragma: no cover
        return ChannelBan.make_one(self.boto3_raw_data["ChannelBan"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChannelBanResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelBanResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelMembershipsResponse:
    boto3_raw_data: "type_defs.ListChannelMembershipsResponseTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")

    @cached_property
    def ChannelMemberships(self):  # pragma: no cover
        return ChannelMembershipSummary.make_many(
            self.boto3_raw_data["ChannelMemberships"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListChannelMembershipsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelMembershipsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelMembershipResponse:
    boto3_raw_data: "type_defs.DescribeChannelMembershipResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ChannelMembership(self):  # pragma: no cover
        return ChannelMembership.make_one(self.boto3_raw_data["ChannelMembership"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeChannelMembershipResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelMembershipResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelModeratorsResponse:
    boto3_raw_data: "type_defs.ListChannelModeratorsResponseTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")

    @cached_property
    def ChannelModerators(self):  # pragma: no cover
        return ChannelModeratorSummary.make_many(
            self.boto3_raw_data["ChannelModerators"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListChannelModeratorsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelModeratorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelModeratorResponse:
    boto3_raw_data: "type_defs.DescribeChannelModeratorResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ChannelModerator(self):  # pragma: no cover
        return ChannelModerator.make_one(self.boto3_raw_data["ChannelModerator"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeChannelModeratorResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelModeratorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelMembershipForAppInstanceUserResponse:
    boto3_raw_data: (
        "type_defs.DescribeChannelMembershipForAppInstanceUserResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def ChannelMembership(self):  # pragma: no cover
        return ChannelMembershipForAppInstanceUserSummary.make_one(
            self.boto3_raw_data["ChannelMembership"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeChannelMembershipForAppInstanceUserResponseTypeDef"
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
                "type_defs.DescribeChannelMembershipForAppInstanceUserResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelMembershipsForAppInstanceUserResponse:
    boto3_raw_data: (
        "type_defs.ListChannelMembershipsForAppInstanceUserResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def ChannelMemberships(self):  # pragma: no cover
        return ChannelMembershipForAppInstanceUserSummary.make_many(
            self.boto3_raw_data["ChannelMemberships"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListChannelMembershipsForAppInstanceUserResponseTypeDef"
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
                "type_defs.ListChannelMembershipsForAppInstanceUserResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelModeratedByAppInstanceUserResponse:
    boto3_raw_data: (
        "type_defs.DescribeChannelModeratedByAppInstanceUserResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Channel(self):  # pragma: no cover
        return ChannelModeratedByAppInstanceUserSummary.make_one(
            self.boto3_raw_data["Channel"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeChannelModeratedByAppInstanceUserResponseTypeDef"
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
                "type_defs.DescribeChannelModeratedByAppInstanceUserResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelsModeratedByAppInstanceUserResponse:
    boto3_raw_data: (
        "type_defs.ListChannelsModeratedByAppInstanceUserResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Channels(self):  # pragma: no cover
        return ChannelModeratedByAppInstanceUserSummary.make_many(
            self.boto3_raw_data["Channels"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListChannelsModeratedByAppInstanceUserResponseTypeDef"
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
                "type_defs.ListChannelsModeratedByAppInstanceUserResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChannelMembershipPreferencesResponse:
    boto3_raw_data: "type_defs.GetChannelMembershipPreferencesResponseTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")

    @cached_property
    def Member(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["Member"])

    @cached_property
    def Preferences(self):  # pragma: no cover
        return ChannelMembershipPreferences.make_one(self.boto3_raw_data["Preferences"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetChannelMembershipPreferencesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChannelMembershipPreferencesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutChannelMembershipPreferencesRequest:
    boto3_raw_data: "type_defs.PutChannelMembershipPreferencesRequestTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")
    MemberArn = field("MemberArn")
    ChimeBearer = field("ChimeBearer")

    @cached_property
    def Preferences(self):  # pragma: no cover
        return ChannelMembershipPreferences.make_one(self.boto3_raw_data["Preferences"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutChannelMembershipPreferencesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutChannelMembershipPreferencesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutChannelMembershipPreferencesResponse:
    boto3_raw_data: "type_defs.PutChannelMembershipPreferencesResponseTypeDef" = (
        dataclasses.field()
    )

    ChannelArn = field("ChannelArn")

    @cached_property
    def Member(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["Member"])

    @cached_property
    def Preferences(self):  # pragma: no cover
        return ChannelMembershipPreferences.make_one(self.boto3_raw_data["Preferences"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutChannelMembershipPreferencesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutChannelMembershipPreferencesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelMessagesResponse:
    boto3_raw_data: "type_defs.ListChannelMessagesResponseTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")

    @cached_property
    def ChannelMessages(self):  # pragma: no cover
        return ChannelMessageSummary.make_many(self.boto3_raw_data["ChannelMessages"])

    SubChannelId = field("SubChannelId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelMessagesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelMessagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChannelMessageResponse:
    boto3_raw_data: "type_defs.GetChannelMessageResponseTypeDef" = dataclasses.field()

    @cached_property
    def ChannelMessage(self):  # pragma: no cover
        return ChannelMessage.make_one(self.boto3_raw_data["ChannelMessage"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetChannelMessageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChannelMessageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelResponse:
    boto3_raw_data: "type_defs.DescribeChannelResponseTypeDef" = dataclasses.field()

    @cached_property
    def Channel(self):  # pragma: no cover
        return Channel.make_one(self.boto3_raw_data["Channel"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Processor:
    boto3_raw_data: "type_defs.ProcessorTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Configuration(self):  # pragma: no cover
        return ProcessorConfiguration.make_one(self.boto3_raw_data["Configuration"])

    ExecutionOrder = field("ExecutionOrder")
    FallbackAction = field("FallbackAction")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProcessorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProcessorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelMessageCallback:
    boto3_raw_data: "type_defs.ChannelMessageCallbackTypeDef" = dataclasses.field()

    MessageId = field("MessageId")
    Content = field("Content")
    Metadata = field("Metadata")

    @cached_property
    def PushNotification(self):  # pragma: no cover
        return PushNotificationConfiguration.make_one(
            self.boto3_raw_data["PushNotification"]
        )

    MessageAttributes = field("MessageAttributes")
    SubChannelId = field("SubChannelId")
    ContentType = field("ContentType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChannelMessageCallbackTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelMessageCallbackTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendChannelMessageRequest:
    boto3_raw_data: "type_defs.SendChannelMessageRequestTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")
    Content = field("Content")
    Type = field("Type")
    Persistence = field("Persistence")
    ClientRequestToken = field("ClientRequestToken")
    ChimeBearer = field("ChimeBearer")
    Metadata = field("Metadata")

    @cached_property
    def PushNotification(self):  # pragma: no cover
        return PushNotificationConfiguration.make_one(
            self.boto3_raw_data["PushNotification"]
        )

    MessageAttributes = field("MessageAttributes")
    SubChannelId = field("SubChannelId")
    ContentType = field("ContentType")

    @cached_property
    def Target(self):  # pragma: no cover
        return Target.make_many(self.boto3_raw_data["Target"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendChannelMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendChannelMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelFlowSummary:
    boto3_raw_data: "type_defs.ChannelFlowSummaryTypeDef" = dataclasses.field()

    ChannelFlowArn = field("ChannelFlowArn")
    Name = field("Name")

    @cached_property
    def Processors(self):  # pragma: no cover
        return Processor.make_many(self.boto3_raw_data["Processors"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChannelFlowSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelFlowSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelFlow:
    boto3_raw_data: "type_defs.ChannelFlowTypeDef" = dataclasses.field()

    ChannelFlowArn = field("ChannelFlowArn")

    @cached_property
    def Processors(self):  # pragma: no cover
        return Processor.make_many(self.boto3_raw_data["Processors"])

    Name = field("Name")
    CreatedTimestamp = field("CreatedTimestamp")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelFlowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChannelFlowTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelFlowRequest:
    boto3_raw_data: "type_defs.CreateChannelFlowRequestTypeDef" = dataclasses.field()

    AppInstanceArn = field("AppInstanceArn")

    @cached_property
    def Processors(self):  # pragma: no cover
        return Processor.make_many(self.boto3_raw_data["Processors"])

    Name = field("Name")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateChannelFlowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChannelFlowRequest:
    boto3_raw_data: "type_defs.UpdateChannelFlowRequestTypeDef" = dataclasses.field()

    ChannelFlowArn = field("ChannelFlowArn")

    @cached_property
    def Processors(self):  # pragma: no cover
        return Processor.make_many(self.boto3_raw_data["Processors"])

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateChannelFlowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelFlowCallbackRequest:
    boto3_raw_data: "type_defs.ChannelFlowCallbackRequestTypeDef" = dataclasses.field()

    CallbackId = field("CallbackId")
    ChannelArn = field("ChannelArn")

    @cached_property
    def ChannelMessage(self):  # pragma: no cover
        return ChannelMessageCallback.make_one(self.boto3_raw_data["ChannelMessage"])

    DeleteResource = field("DeleteResource")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChannelFlowCallbackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelFlowCallbackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelFlowsResponse:
    boto3_raw_data: "type_defs.ListChannelFlowsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ChannelFlows(self):  # pragma: no cover
        return ChannelFlowSummary.make_many(self.boto3_raw_data["ChannelFlows"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelFlowsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelFlowsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelFlowResponse:
    boto3_raw_data: "type_defs.DescribeChannelFlowResponseTypeDef" = dataclasses.field()

    @cached_property
    def ChannelFlow(self):  # pragma: no cover
        return ChannelFlow.make_one(self.boto3_raw_data["ChannelFlow"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChannelFlowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
